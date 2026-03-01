---
title: 阿里CTF2026-license
url: https://mp.weixin.qq.com/s/tL-QO8GQSxX71nTcGz10AA
source: Doonsec's feed
date: 2026-02-28
fetch_date: 2026-03-01T04:16:30.408129
---

# 阿里CTF2026-license

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/Cpo2XCpI7K3ruht6NPE4dof1bS9wAHLCtOuLtOmpGI9DBl1SxvOQFVeAUBhod2biaCsJy99AHHyZ0q3Q6w1P0JRuO7J94BGQ8f4UNFQFXict8/0?wx_fmt=jpeg)

# 阿里CTF2026-license

Xherlock
Xherlock

看雪学苑

![]()

在小说阅读器中沉浸阅读

记录下第一次搞协议逆向，很遗憾比赛过程中卡在最后一步了。

总体协议流程如下：

1.数据包=长度（4字节）+nonce（12字节）+数据流（长度-12字节）

2.数据流做AES-GCM解密

3.zstd解压缩

4.base64解码

5.protobuf解析出来四个字段，enc\_data、password、salt、sha256\_hash

6.AES-160解密（魔改了SBOX、mixcolumn、加密解密互换了，同时是CBC模式加PKC#7），密钥是password、salt做PBKDF2-HMAC-SHA256得到48字节，前28字节作为密钥，后20字节作为iv

7.解密后是一个json格式字符串，要求包含license\_code和sign字段，license\_code就是license启动时随机生成的字符串，sign是RSA4096签名（比赛分析到这里了，签名没分析出来，题目应该是给了个d，需要用密码学攻击还原e，但实际上e就是65537）

8.上面全部通过读取和打印FLAG环境变量

## ELF加载

直接分析license可以发现他和build\_token建立了通信：

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/Cpo2XCpI7K1Y1rqFTIC8uiaZLRDuYTqvKtyLGWm5T5myas8mRhwCjRPYu7RydV955AFlt0wF9m42kr9cIESdSSs6q6TQ296ggIVMXqtoxicc8/640?wx_fmt=other&from=appmsg)

运行过程中打印了`license code: xxxx-uuid`这样的字符串，但并没有在license文件里找到，猜测是从build\_token发送elf回来加载到主elf内存里执行代码。

直接上调试，ida里按照run.sh里设置`--no-redirect -c 127.0.0.1:12345`，本地跑`./build_token -p 'r&FGW9RpqTc*aqof' -s -l 0.0.0.0:12345`，从main函数return 0开始调试。

![](https://mmbiz.qpic.cn/mmbiz_jpg/Cpo2XCpI7K0Oic54plGFPryIvia4jiaNp19hIQ7ffj1MSLLaCccmgTnuHDAticLDXNFjGhSoSnrGqqFGSYQLZSXFKiabhlW4ftfibkrBCicox0yln4/640?wx_fmt=other&from=appmsg)![]()

刚开始可以看到retn后来到了新的区域：

![](https://mmbiz.qpic.cn/mmbiz_jpg/Cpo2XCpI7K3NaYC2vtkVlpw5Uekq8qpPcQYIrW7gvQIKlFzLHM8mWQJd6qljxlDPmhBYb2KPpibCetO1Tv9vkb41aGhpibcTpjZbgbSTGhHqU/640?wx_fmt=other&from=appmsg)![]()

慢慢调试可以发现有一些脱壳的感觉，在解密一些数据代码，按照经验不停的跳过循环，最终可以发现来到一块非常大的函数。

![](https://mmbiz.qpic.cn/mmbiz_jpg/Cpo2XCpI7K24fUeiaVopuGscmAIm3ucpgwcicw3SM4meVQPy01cLz3K0YYhblYmcfuQ3YhpCib5xWDFmJhVBLePficTzbU1qyWor0ztZE2Esbno/640?wx_fmt=other&from=appmsg)![]()

单步进入反编译后可以看到license、flag等字符串，说明这里才是真正的check逻辑：

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/Cpo2XCpI7K323lIdPsTfOZlsl0MuwMRHYriaeaf2eyKuiaCxicGu71RWMTM5os6BY2PvJ82ryvkvc7C9qqZaiarP10HSZHL2yqHvGs2KibgibgGKE/640?wx_fmt=other&from=appmsg)![]()

## 数据包结构

开头部分是在生成随机的UUID，慢慢调试直到要求输入，发现下图红框位置要求输入数据，分别要求4、12长度（注意回车符也算输入）。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/Cpo2XCpI7K35Y843xmE01czZxBRlt5O3bMvVOzUbicqXhziaS2M1kSGcznJpkvtRico1GHFLjZicgZ8flbVhCvZdLb2cYKElxe8PA3pibjjdmteo/640?wx_fmt=other&from=appmsg)![]()

第三处要求输入长度的正是第一处输入的数值-12（不太可控，因为手动输入只能输可打印字符），因此调试到这里时我手动在第三处输入前把要求长度修改掉，从而得以输入可控长度的测试数据，我们这里成为数据流。

## 数据流AES-GCM解密

数据包结构分析完后，下图中sub\_403D10函数会返回CPU架构是否支持AVX并设置一个bool字节（随后很多if-else会根据这个值选择进入到的代码，这些分支代码逻辑是相同的，可以省略很多分析过程）。

我的CPU支持AVX，进入到下图红框中的数据初始化，AI分析可知是密钥扩展，但这里的密钥通过一定运算才能得到。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/Cpo2XCpI7K24VZJu8vPDTpP0TqCdk1qLK1HujibDqDGglSOxtj0DictLdYSkwUsyFpTBxiaPliaMw0ULEMiaiaxGBugzFUP8XaSicj7mMWcDT8M7S0/640?wx_fmt=other&from=appmsg)![]()

所以直接来到最后最终轮密钥结果处，提取出来前32字节即可获得密钥为`f6778d8728d8f17ce8c5c81f45c3d5fd869ca851b7575be540776f4f26c1140d`

if-else出来后发现对16个0字节做了加密：

![](https://mmbiz.qpic.cn/mmbiz_jpg/Cpo2XCpI7K3icDlic7u79ibBmZB4bSN2vgSic9arJWtvCy6B2HYBgJBEfOkhmpXOfXPLNBTgU3iaqMicOgEyBtwntybnSXe1KRzweRF76xvqA5st0/640?wx_fmt=other&from=appmsg)![]()

```
void __fastcall sub_40C1B0(__m128i *_RDI, const __m128i *a2, _OWORD *a3)
{
  _XMM0 = _mm_xor_si128(_mm_loadu_si128(a2), *_RDI);
  __asm
  {
    aesenc  xmm0, xmmword ptr [rdi+10h]
    aesenc  xmm0, xmmword ptr [rdi+20h]
    aesenc  xmm0, xmmword ptr [rdi+30h]
    aesenc  xmm0, xmmword ptr [rdi+40h]
    aesenc  xmm0, xmmword ptr [rdi+50h]
    aesenc  xmm0, xmmword ptr [rdi+60h]
    aesenc  xmm0, xmmword ptr [rdi+70h]
    aesenc  xmm0, xmmword ptr [rdi+80h]
    aesenc  xmm0, xmmword ptr [rdi+90h]
    aesenc  xmm0, xmmword ptr [rdi+0A0h]
    aesenc  xmm0, xmmword ptr [rdi+0B0h]
    aesenc  xmm0, xmmword ptr [rdi+0C0h]
    aesenc  xmm0, xmmword ptr [rdi+0D0h]
    aesenclast xmm0, xmmword ptr [rdi+0E0h]
  }
  *a3 = _XMM0;
}
```

这种模式符合AES-256-GCM模式，里面包含2部分，CTR+GHASH随后的调试里都可以看到特征，比如下图里检查了数据流最后16字节是否等于一组结果。

![](https://mmbiz.qpic.cn/mmbiz_jpg/Cpo2XCpI7K0RTV9CNFTppseXNdXhe3ty8G8xqyXmfOx2DZf4KxCcNKrEzXw8a9F2O2yJwjFoHEiaibnvuKRAViczHVl2lic8gUPfCwOic6zht9No/640?wx_fmt=other&from=appmsg)![]()

可以写一个代码来加密数据，结果放入数据包中的数据流部分，从而调试通过这部分AES解密。

## zstd解压缩

解密完的数据发现检查了大小，要求不小于13字节

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/Cpo2XCpI7K2iasMZOqM4ADibDqUM0mSQGq2uN4xWz8jpUo665icibDSO3yJc6KkQREa7SZmLL9qy1htVG5y1FPDzdRqXP4bsicqY15hiaBJIAvOk8/640?wx_fmt=other&from=appmsg)![]()

在往下调试的过程中发现报错`Unknown frame descriptor`，搜索字符串可以定位一堆报错case：

```
const char *__fastcall sub_7FFFF7D68AA6(unsigned __int64 a1)
{
  int v1; // r8d
const char *result; // rax

  v1 = 0;
if ( a1 > 0xFFFFFFFFFFFFFF88LL )
    v1 = -(int)a1;
  switch ( v1 )
  {
    case 0:
      result = "No error detected";
break;
    case 1:
      result = "Error (generic)";
break;
    case 2:
    case 3:
    case 4:
    case 5:
    case 6:
    case 7:
    case 8:
    case 9:
    case 11:
    case 13:
    case 15:
    case 17:
    case 18:
    case 19:
    case 21:
    case 23:
LABEL_38:
      result = "Unspecified error code";
break;
    case 10:
      result = "Unknown frame descriptor";
break;
    case 12:
      result = "Version not supported";
break;
    case 14:
      result = "Unsupported frame parameter";
break;
    case 16:
      result = "Frame requires too much memory for decoding";
break;
    case 20:
      result = "Data corruption detected";
break;
    case 22:
      result = "Restored data doesn't match checksum";
break;
    case 24:
      result = "Header of Literals' block doesn't respect format specification";
break;
    default:
      switch ( v1 )
      {
        case 30:
          result = "Dictionary is corrupted";
break;
        case 32:
          result = "Dictionary mismatch";
break;
        case 34:
          result = "Cannot create Dictionary from provided samples";
break;
        case 40:
          result = "Unsupported parameter";
break;
        case 41:
          result = "Unsupported combination of parameters";
break;
        case 42:
          result = "Parameter is out of bound";
break;
        case 44:
          result = "tableLog requires too much memory : unsupported";
break;
        case 46:
          result = "Unsupported max Symbol Value : too large";
break;
        case 48:
          result = "Specified maxSymbolValue is too small";
break;
        case 49:
          result = "This mode cannot generate an uncompressed block";
break;
        case 50:
          result = "pledged buffer stability condition is not respected";
break;
        case 60:
          result = "Operation not authorized at current processing stage";
break;
        case 62:
          result = "Context should be init first";
break;
        case 64:
          result = "Allocation error : not enough memory";
break;
        case 66:
          result = "workSpace buffer is not large enough";
break;
        case 70:
          result = "Destination buffer is too small";
break;
        case 72:
          result = "Src size is incorrect";
break;
        case 74:
          result = "Operation on NULL destination buffer";
break;
        case 80:
          result = "Operation made no progress over multiple calls, due to output buffer being full";
break;
        case 82:
          result = "Operation made no progress over multiple calls, due to input being empty";
break;
        case 100:
          result = "Frame index is too large";
break;
        case 102:
          result = "An I/O error occurred when reading/seeking";
break;
        case 104:
          result = "Destination buffer is wrong";
break;
        case 105:
          result = "Source buffer is wrong";
break;
        case 106:
          result = "Block-level external sequence producer returned an error code";
break;
        case 107:
          result = "External sequences are not valid";
break;
        default:
          goto LABEL_38;
      }
break;
  }
return result;
}
```

搜索可知是Zstandard解码器报错，解码器在输入数据开头没有识别出合法的魔数（`28 B5 2F FD`，可以IDA搜索到多个比较），所以才报错。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/Cpo2XCpI7K3ia7AEUgZekZciaEEd9oMMc5ArZhicSnK7GBUhWc...