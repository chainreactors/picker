---
title: Windows PE 文件签名的解析与验证
url: https://mp.weixin.qq.com/s?__biz=MjM5NTc2MDYxMw==&mid=2458576190&idx=1&sn=79242aea27f03e30257a6d7aaf07e3b8&chksm=b18dd5b486fa5ca28b164aad909ece01e3c2638a4774143cefc9723c24c5f8487ef9fa36d228&scene=58&subscene=0#rd
source: 看雪学苑
date: 2024-09-28
fetch_date: 2025-10-06T18:27:37.627104
---

# Windows PE 文件签名的解析与验证

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1UG7KPNHN8HesnpdrWKQ4QcTTKic0HXb8dNZhUqoYkzqyiaH9gBAd6KVUCBzk4SocAaIwiaawvN6aHt4j7yj5KNaQ/0?wx_fmt=jpeg)

# Windows PE 文件签名的解析与验证

techliu

看雪学苑

本文分享的是开发该工具之前做的一些签名研究内容。

```
一

导出签名数据
```

具体的 PE 格式可以参考MSDN（https://learn.microsoft.com/en-us/windows/win32/debug/pe-format）。

签名证书的位置在 Certificate Table 里（也称为 Security Directory）：

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1UG7KPNHN8GSicqO5VbJiaicexTT573ThrKMttLrn2uaeVsWoe7V7MER2NLFq0k09oNYlg6GdXRqZeibVfia4CoFysg/640?wx_fmt=jpeg&from=appmsg)

可以从 Optional Header 的 Data Directories 里找到 Security Directory 的文件偏移：

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1UG7KPNHN8GSicqO5VbJiaicexTT573ThrKP27k7sWTJapse0bpyFyiaAXEwetv5P6PTsFcEUQNeTjqSvy0ib1kyicVw/640?wx_fmt=jpeg&from=appmsg)

如图表示，ProcessHacker.exe 文件的签名数据在 0x1A0400 位置，长度 0x3A20。

导航到这个偏移位置即可看到这里就是签名数据：

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1UG7KPNHN8GSicqO5VbJiaicexTT573ThrKLhuQHnMYGKhQEiaTXkOdY5htXr9f14ASTGBOaS1RsicD8nqN53ZglHhw/640?wx_fmt=jpeg&from=appmsg)

参考MSDN， 签名数据的结构如下：

```
typedef struct _WIN_CERTIFICATE {
  DWORD dwLength;
  WORD  wRevision;
  WORD  wCertificateType;
  BYTE  bCertificate[ANYSIZE_ARRAY];
} WIN_CERTIFICATE, *LPWIN_CERTIFICATE;
```

所以，bCertificate 是实际的证书内容，wCertificateType 表示签名证书类型，根据这个字段可知支持三种证书类型：PKCS #1、PKCS #7、X509，我看到过的文件都是使用 PKCS #7 签名。

找到 Security Directory 偏移之后，跳过前面的 8 字节就是实际的 PKCS #7 证书内容，DER 格式，代码示意：

```
fn extract_pkcs7_from_pe(file: &PathBuf) -> Result<Vec<u8>, Box<dyn Error>> {
    // ...
    let image = VecPE::from_disk_file(file.to_str().unwrap())?;
    let security_directory =
        image.get_data_directory(exe::ImageDirectoryEntry::Security)?;
    let signature_data =
        exe::Buffer::offset_to_ptr(&image, security_directory.virtual_address.into())?; // security_data_directory rva is equivalent to file offset

    Ok(unsafe {
        let vec = std::slice::from_raw_parts(signature_data, security_directory.size as usize).to_vec();    // cloned
        vec.into_iter().skip(8).collect()   // _WIN_CERTIFICATE->bCertificate
    })
}
```

使用项目中的 pe-sign 工具可以直接导出：

```
pe-sign extract <input_file> > pkcs7.cer
```

使用`--pem`参数可以将 DER 格式转换为 PEM 格式：

```
pe-sign extract <input_file> --pem > pkcs7.pem
```

##

```
二

使用 openssl 解析证书
```

解析导出的证书，如果是 PEM 格式，`-inform DER`改为`-inform PEM`：

```
openssl pkcs7 -inform DER -in .\pkcs7.cer -print_certs -text -noout
```

这里有个小疑问，从属性里看 ProcessHacker.exe 文件有两个签名，一个是 sha1,另一个是 sha256：

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1UG7KPNHN8GSicqO5VbJiaicexTT573ThrKvLfyRqEwGWwX3NI6hapadDCRicpVMNyOIKJuYj2kp7zbviaRFmg8Zic4Q/640?wx_fmt=jpeg&from=appmsg)

openssl 打印的证书信息只有 sha1 证书的，使用`-print`参数打印 pkcs7 结构也可以看到是有 sha256 证书内容的但是没正确解析。

看了下微步沙箱也只解析到了 1 个签名：https://s.threatbook.com/report/file/bd2c2cf0631d881ed382817afcce2b093f4e412ffb170a719e2762f250abfea4

##

## 解析内嵌证书

经过一番观察，发现 sha256 这个证书是在 sha1 证书属性里内嵌的，并不是平级：

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1UG7KPNHN8GSicqO5VbJiaicexTT573ThrKGR37uXRNgTIoib4ibibic3b7YiaoMXmKTWtthcq5QaIvDDFmDNLR9SbsGicg/640?wx_fmt=jpeg&from=appmsg)

然后就搜了一个这个属性名`1.3.6.1.4.1.311.2.4.1`有什么特殊的地方，从MSDN可知，这个值表示的是`szOID_NESTED_SIGNATURE`内容（实际就是一个 pkcs#7 格式证书），ChatGPT 是这么解释这个属性的：

> szOID\_NESTED\_SIGNATURE 是一个表示嵌套签名的对象标识符（OID），其对应的 OID 是 1.3.6.1.4.1.311.2.4.1。在 PKCS7 或 CMS（Cryptographic Message Syntax）中，嵌套签名允许在签名数据中嵌套另一个签名数据块。这种机制用于实现多层次的签名或加密操作。

使用 openssl 的 asn1parse 命令可以找出嵌套签名的偏移位置：

```
PS C:\dev\windows_pe_signature_research> openssl asn1parse -i -inform DER -in \pkcs7.cer | Select-String -Context 1,3 1.3.6.1.4.1.311.2.4.1

   7638:d=6  hl=4 l=7223 cons:       SEQUENCE
>  7642:d=7  hl=2 l=  10 prim:        OBJECT            :1.3.6.1.4.1.311.2.4.1
   7654:d=7  hl=4 l=7207 cons:        SET
   7658:d=8  hl=4 l=7203 cons:         SEQUENCE
   7662:d=9  hl=2 l=   9 prim:          OBJECT            :pkcs7-signedData
```

SET 后面开始就是嵌入数据，7658 就是嵌套数据开始的文件偏移，hl 表示头大小，l 表示数据大小，所以总的嵌套数据大小为 4+7203=7207。使用 powershell 提取这个嵌套签名：

```
$offset = 7658
$size = 7207
$fileStream = [System.IO.File]::OpenRead(".\pkcs7.cer")
$buffer = New-Object byte[] $size
$fileStream.Seek($offset, [System.IO.SeekOrigin]::Begin)
$fileStream.Read($buffer, 0, $size)
$fileStream.Close()
[System.IO.File]::WriteAllBytes(".\pkcs7_embed.cer", $buffer)
```

再次使用 openssl 就可以解析出这个嵌套签名证书：

```
PS C:\dev\windows_pe_signature_research> openssl pkcs7 -inform der -in .\pkcs7_embed.cer -print_certs -text -noout
Certificate:
    Data:
        Version: 3 (0x2)
        Serial Number:
            04:0c:b4:1e:4f:b3:70:c4:5c:43:44:76:51:62:58:2f
        Signature Algorithm: sha256WithRSAEncryption
        Issuer: C=US, O=DigiCert Inc, OU=www.digicert.com, CN=DigiCert SHA2 High Assurance Code Signing CA
        Validity
            Not Before: Oct 30 00:00:00 2013 GMT
            Not After : Jan  4 12:00:00 2017 GMT
        Subject: C=AU, ST=New South Wales, L=Sydney, O=Wen Jia Liu, CN=Wen Jia Liu
        Subject Public Key Info:
            Public Key Algorithm: rsaEncryption
                Public-Key: (2048 bit)
                Modulus:
                    00:97:a8:e8:af:59:2a:05:f3:d5:0e:36:66:eb:89:
                    95:52:1a:3b:dd:41:12:63:b2:81:b9:f4:d0:cb:3d:
                    df:7d:f5:9b:f1:55:35:c0:9b:0a:ae:39:f6:ed:d8:
                    da:58:dd:ab:0e:ca:ce:b2:de:de:f0:fd:9d:6d:77:
                    1e:9d:05:ae:51:e6:02:27:8d:a4:c2:43:2f:2b:07:
                    cf:04:0b:00:a0:46:5d:61:13:f6:a3:b6:ab:bd:04:
                    b3:e4:b6:a2:9e:bd:94:d6:95:cf:28:bb:d9:5f:dc:
                    fb:06:2c:52:00:3d:63:6c:64:f8:68:ca:02:5a:1f:
                    25:b8:1c:d5:af:6e:bb:11:61:c0:f5:72:97:32:c1:
                    66:af:41:b8:7b:59:b0:da:e5:5b:9b:25:db:56:b4:
                    44:fc:52:5f:44:40:3b:5f:b0:02:37:53:d1:9f:96:
                    a5:a0:a5:47:87:19:c8:3d:a6:5b:91:05:01:b1:d4:
                    00:96:14:31:80:04:8a:e0:a6:a3:a5:32:31:92:37:
                    1a:93:85:da:b1:e9:79:ec:1a:bb:a6:1a:34:c7:70:
                    80:2d:8a:d6:89:38:d3:8c:54:ae:6e:86:3d:3a:c5:
                    49:d6:72:7b:b7:94:b6:6b:ee:f0:d0:70:11:c2:f0:
                    a2:5d:d8:87:5c:47:a4:7e:8e:36:29:d5:64:cf:49:
                    79:85
                Exponent: 65537 (0x10001)
        X509v3 extensions:
            X509v3 Authority Key Identifier:
                67:9D:0F:20:09:0C:CC:8A:3A:E5:82:46:72:62:FC:F1:CC:90:E5:40
            X509v3 Subject Key Identifier:
                13:86:9A:3B:EF:68:31:53:BC:6B:18:9B:34:C6:FF:0A:8B:4D:68:28
            X509v3 Key Usage: critical
                Digital Signature
            X509v3 Extended Key Usage:
                Code Signing
            X509v3 CRL Distribution Points:
                Full Name:
                  URI:http://crl3.digicert.com/sha2-ha-cs-g1.crl
                Full Name:
                  URI:http://crl4.digicert.com/sha2-ha-cs-g1.crl
            X509v3 Certificate Policies:
                Policy: 2.16.840.1.114412.3.1
                  CPS: https://www.digicert.com/CPS
                Policy: 2.23.140.1.4.1
            Authority Information Access:
                OCSP - URI:http://ocsp.digicert.com
                CA Issuers - URI:http://cacerts.digicert.com/DigiCertSHA2HighAssuranceCodeSigningCA.crt
            X509v3 Basic Constraints: critical
                CA:FALSE
    Signature Algorithm: sha256WithRSAEncryption
    Signature Value:
        91:87:ac:23:c2:84:07:cb:c7:6a:c1:f8:1a:6c:78:3b:21:9f:
        c2:48:1b:08:e8:f5:e3:41:f7:eb:e2:d9:41:b1:48:e6:1b:ff:
        55:ab:79:c1:a2:d8:16:7a:2d:d2:94:f5:32:c8:00:5a:5f:dd:
        f2:f8:b2:19:86:47:fb:e7:aa:a7:16:e6:ff:0a:c3:37:f9:64:
        c0:5b:51:64:ef:8a:23:c4:7a:d0:8f:d7:37:b8:70:dd:35:6f:
        19:06:4e:a5:cd:ea:0a:ef:a4:f2:2a:1c:b3:49:f8:a6:89:ac:
        a5:67:f3:8b:b3:de:01:23:20:4f:9f:f5:56:0c:59:ec:e4:01:
        32:3f:2c:e5:84:be:e0:ea:5b:b7:39:31:26:ff:32:7f:eb:15:
        cc:82:d0:b0:16:f8:fc:6f:1d:c8:b2:1b:9c:85:68:27:7d:45:
        b0:e0:7a:7c:dd:26:f4:9a:d4:7d:0f:a6:ac:04:c1:48:65:1c:
        ef:49:33:0b:d2:...