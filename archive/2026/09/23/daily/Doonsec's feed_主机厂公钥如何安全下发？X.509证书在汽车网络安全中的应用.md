---
title: 主机厂公钥如何安全下发？X.509证书在汽车网络安全中的应用
url: https://mp.weixin.qq.com/s/bTQOurADaHDlVGBnFZje0g
source: Doonsec's feed
date: 2026-09-23
fetch_date: 2026-09-24T06:59:42.213282
---

# 主机厂公钥如何安全下发？X.509证书在汽车网络安全中的应用

# 主机厂公钥如何安全下发？X.509证书在汽车网络安全中的应用

谈思实验室

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

以下文章来源于开心果 Need Car
，作者开心果 Need Car

![](https://wx.qlogo.cn/mmhead/Q3auHgzwzM7xmZWjMxkpzia4Ft2qUbKVib3waicn3vUKRjoL8iaKrC191A/0)

**开心果 Need Car**
.

号主：开心果 Need Car，主要从事汽车Autosar开发，公众号主要分享 通信、诊断、存储、网络管理、标定、Bootloader等工程开发问题。致力于将学到的知识，分享给更多的Autosar从业者，努力解答一线开发工程师的困顿！

点击上方蓝字谈思实验室

获取更多汽车网络安全资讯

[![](https://mmbiz.qpic.cn/mmbiz_png/zQ19N6bPViaDLV3N3hBGwAkd9SkRVQEf7mgAabpVcLd2pJviaAFlVMnVQ0ibyJRnkBZGlYSwrh0TP60dG5tWAsy54w0qYHa9BjHzyib7H2xhDdM/640?wx_fmt=png&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MzIzOTc2OTAxMg==&mid=2247580896&idx=1&sn=36a65f68d014c79310fdeb0e1e55b6b0&scene=21#wechat_redirect)

在信息安全的话题里，非对称算法中的公钥传递是一个常见问题。这里的传递场景之一：主机厂将开发公钥分发给供应商。所以，这个过程就需要关注几个问题：

1. 公钥存储的文件格式
2. 如何基于这些文件解析公钥（比如X.509）

......

**01**

**公钥存储的文件格式**

以RSA2048算法为例，它的公钥使用 .pem、.crt 或 .der 格式。

**02**

**如何解析公钥**

**（一）基于Openssl的公钥文件解析**

PEM（Privacy Enhanced Mail）格式（Base64编码的 ASCII 文本）。

```
openssl rsa -pubin -in publickey.pem -text -noout
```

X.509 证书（如 .crt 文件），可以是PEM（文本）或DER（二进制）格式。

```
openssl x509 -in certificate.crt -text -noout
```

可以使用 -inform DER/PEM参数来确认使用的是DER还是PEM格式：

```
openssl x509 -in certificate.crt -inform DER -text -nooutopenssl x509 -in certificate.crt -inform PEM -text -noout
```

DER（Distinguished Encoding Rules）格式（如 .der 文件），二进制编码（ASN.1 DER 编码）。

```
openssl x509 -in certificate.der -inform der -text -noout
```

三种格式对比如下：

|  |  |  |  |
| --- | --- | --- | --- |
| 扩展名 | 全称 | 编码格式 | 常见用途 |
| .pem | Privacy Enhanced Mail | Base64 + ASCII | 通用证书、公钥、私钥 |
| .crt | Certificate | PEM 或 DER | SSL/TLS 证书 |
| .der | Distinguished Encoding Rules | 二进制 | Java、嵌入式系统 |

**03**

**使用OpenSSL工具来生成一个 X.509 格式的证书（.crt 文件）**

通常包括以下几个步骤：

步骤 1：生成私钥

```
openssl genrsa -out private.key 2048
```

步骤 2：生成证书签名请求（CSR）

```
openssl req -new -key private.key -out request.csr
```

会被提示输入一些信息，例如：国家（Country Name）、省份（State or Province）、城市（Locality）、组织（Organization Name）、通用名称（Common Name，例如域名）、邮箱地址。也可以直接回车。

步骤 3：使用 CSR 自签名生成 X.509 证书（.crt）

```
openssl x509 -req -in request.csr -signkey private.key -out certificate.crt -days 365
```

这会生成一个有效期为 365 天的自签名证书 certificate.crt。

如上流程执行示意如下：

![](https://mmbiz.qpic.cn/mmbiz_png/eEEQvxEw8vwsmNjPzTUOLtxSLELZphe6XtunZ7OPTXYBuqmSyYzkgtf8iaC9pUdbYjgdwS3vdxzTSXbkqoMMNew/640?wx_fmt=png&from=appmsg)

最终会得到三个文件：

|  |  |
| --- | --- |
| 文件名 | 说明 |
| private.key | 私钥（保密） |
| request.csr | 证书签名请求（可用于申请 CA 签名） |
| certificate.crt | X.509 格式的公钥证书 |

得到的文件如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/eEEQvxEw8vwsmNjPzTUOLtxSLELZphe6WbfTn64jsG0LdVSxZb0NRUBOw5mwqevR4qQobls73UziaYUCiahG0vuQ/640?wx_fmt=png&from=appmsg)

可以生成用于嵌入式的DER格式自签名证书；

```
openssl x509 -req -in request.csr -signkey private.key -outform DER -out certificate.der -days 365
```

X.509 证书规范本身就是基于ASN.1（Abstract Syntax Notation One）定义的结构。-outform DER 表示输出为 DER（Distinguished Encoding Rules）格式，它是 ASN.1 的一种二进制编码方式。所以，生成的 certificate.der 文件是一个ASN.1编码的X.509证书，符合 RFC 5280的结构规范。

生成的certificate.der证书，示意如下：

![](https://mmbiz.qpic.cn/mmbiz_png/eEEQvxEw8vwsmNjPzTUOLtxSLELZphe64PdOCicltHV1tMWOcBl2g1aw8mCNZq39csMknKhH6JWWPfoCHcj664Q/640?wx_fmt=png&from=appmsg)

可以使用如下命令解析certificate.der证书：

```
openssl x509 -in certificate.der -inform DER -text -noout
```

**04**

**X509证书中的签名和验签过程**

**（一）签名的内容**

X.509 签名的内容包括：证书版本号、序列号、签名算法标识符（用于签名的算法，如 SHA256 with RSA）、颁发者信息（Issuer）、有效期（Not Before / Not After）、主题信息（Subject）、公钥信息（Subject Public Key Info）、扩展字段（如 Key Usage、Subject Alternative Name 等）、可选的唯一标识符（Issuer/Subject Unique ID）

这些内容构成了证书的 TBS（To Be Signed）部分。

**（二）签名过程简述**

1. 证书颁发机构（CA，Certificate Authority）将上述 TBS 内容进行哈希处理（如 SHA-256）。
2. 使用 CA 的私钥对哈希值进行加密，生成签名。
3. 签名附加在证书末尾，形成完整的 X.509 证书。

**（三）验证签名时**

1. 使用 CA 的公钥解密签名，得到原始哈希值。
2. 对 TBS 部分重新计算哈希值。
3. 比较两个哈希值是否一致，以验证证书是否被篡改。
4. 使用SREC\_CAT将\*.der证书转换成\*.s19文件

嵌入式工程中，传输给ECU的是二进制文件（eg：\*.s19、\*.hex、\*.bin等），如何将\*.der证书转换成\*.s19文件？使用SREC\_CAT.exe转换命令如下：

```
srec_cat certificate.der -binary -offset 0x0000 -o certificate.s19 -motorola
```

参数说明：

certificate.der：输入文件（DER 格式）

-binary：指定输入格式为二进制

-offset 0x0000：从地址 0 开始写入（可根据需要修改）

-o certificate.s19：输出文件名

-motorola：指定输出格式为 Motorola S-record（即 S19）

输出文件，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/eEEQvxEw8vwsmNjPzTUOLtxSLELZphe6cA2T7CrmqT9UINCEpMgk9Dp32bcOgEiapeojwmyMPcTkqtwa6CUcjrA/640?wx_fmt=png&from=appmsg)

https://www.cnblogs.com/linianhui/p/security-x509.html

参考链接：

https://www.cnblogs.com/charlieroro/p/10948173.html

Windows的SRecord下载链接：

https://sourceforge.net/projects/srecord/files/srecord-win32/1.65/srecord-1.65.0-win64.zip/download

注意：记得将SRecord添加到“系统变量”的path中，以便于在任何位置使用。

包含的工具：

* srec\_cat.exe：用于格式转换、合并、裁剪等操作
* srec\_cmp.exe：比较两个固件文件
* srec\_info.exe：查看文件信息

将.s19 文件转换为二进制（.bin 或 .der）：

```
srec_cat.exe DER_CERT.s19 -Motorola -o DER_CERT.der -Binary
```

然后可以使用 OpenSSL 解析 DER\_CERT.der：

```
openssl asn1parse -in DER_CERT.der -inform DER
```

DER\_CERT.der文件解析如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/eEEQvxEw8vxS6ZsySlReDibpE9HoIeBiazMQkfCVGJia0cgFrYOVyOsn5wevyKS69oj1gLF5cIAzMsjRR0ABgZnibQ/640?wx_fmt=png&from=appmsg)

将DER\_CERT.der文件解析的内容输出到\*.txt文件，命令示意如下：

```
openssl asn1parse -in DER_CERT.der -inform DER > RootKey.txt
```

openssl操作如下：

![](https://mmbiz.qpic.cn/mmbiz_png/eEEQvxEw8vxS6ZsySlReDibpE9HoIeBiazddWMOaLABGc1EK8yhNgxrXkgOMkySKJfjZZjfDySOXSPKoNxRuOQ0g/640?wx_fmt=png&from=appmsg)

DER\_CERT.der文件在线解析如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/eEEQvxEw8vxS6ZsySlReDibpE9HoIeBiazt4AubCw33RXGUkGGvxiaUT2hFAxnGFX1aQnicmZ75icsnrf53JleciaW6Q/640?wx_fmt=png&from=appmsg)

\*.der文件在线解析链接：

https://aks.jd.com/tools/sec/

```
pip install pyasn1
```

ASN1\_DER\_Parser.py脚本内容如下所示：

```
from pyasn1.codec.der.decoder import decodefrom pyasn1.codec.der.encoder import encodefrom pyasn1.type.univ import Sequence, BitStringimport binasciiimport textwrapimport sysdef format_hex(data: bytes, width: int = 16) -> str:    hex_str = binascii.hexlify(data).decode()    lines = textwrap.wrap(hex_str, width * 2)    return '\n'.join(        f"{' '.join(['0x'+line[j:j+2]+',' for j in range(0, len(line), 2)])}"        for i, line in enumerate(lines)    )def display_structure(obj, level=0, label=""):    indent = '  ' * level    encoded = encode(obj)    hex_output = format_hex(encoded)    typename = type(obj).__name__    value = obj.prettyPrint()    # 自动识别公钥字段    if isinstance(obj, BitString) and len(obj) > 256:        label = "Public Key"    print(f"{indent}{label or typename}: {value}")    print(f"{indent}Hex Dump:\n{indent}{hex_output.replace('\n', '\n' + indent)}\n")    if isinstance(obj, Sequence):        for i, component in enumerate(obj):            display_structure(component, level + 1, f"Element[{i}]")def parse_der_file(file_path):    with open(file_path, 'rb') as f:        der_data = f.read()    asn1_obj, _ = decode(der_data)    print(f"\n Parsing DER file: {file_path}\n")    display_structure(asn1_obj)if __name__ == "__main__":    if len(sys.argv) != 1:        print("Usage: python ASN1_DER_Parser.py <DER_FILE_PATH>")    else:        parse_der_file('C:/Code/src/DER_CERT.der')
```

运行命令：

```
 python ASN1_DER_Parser.py
```

运行结果：

![](https://mmbiz.qpic.cn/mmbiz_png/eEEQvxEw8vxS6ZsySlReDibpE9HoIeBiazFOcu8Ncgb0tEAZKmKKpnoZLyngkOdPyPvTib42VlDnO7fZcrpqhyK8g/640?wx_fmt=png&from=appmsg)

**end**

![](https://mmbiz.qpic.cn/mmbiz_jpg/3g8Dklb9Twicgqayv6EVjeHah3Bpvw2ZJlH8rNickiaaHhLM4PaibcicFO9usS5xIOrWYjZibuvwV8g9DwnI6xZ4RvHg/640?wx_fmt=jpeg&from=appmsg)

**谈思汽车媒体门户**

[![](https://mmbiz.qpic.cn/mmbiz_png/3g8Dklb9Tw9hgqzDyib0J4ico1LVFEZ2QnqGKQhnxdoZeiaZAHaGnnTnFGDvlfibtd8h389z8H20gh1icn8yhxrx8yw/640?wx_fmt=png&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MzkyODQzMDI3Mw==&mid=2247549590&idx=1&sn=b5ea25965c057d1ca2913d900f77799d&scene=21#wechat_redirect)

**精品活动推荐**

[![](https://mmbiz.qpic.cn/sz_mmbiz_png/zQ19N6bPViaAI8KMQg42koBCmQ8xCYRUVtiaem7dsJtOqV3DGOX6iaYEHyxflLz2KpKog3fHia0MOsJl0uRNIdyy32iaibZKpdT4LKv907eGCWcdA/640?wx_fmt=png&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MzIzOTc2OTAxMg==&mid=2247572036&i...