---
title: 关于 CTF 中 Bcrypt 考点的思考
url: https://mp.weixin.qq.com/s/FrPWBaK8cw50zb493AF8zQ
source: Doonsec's feed
date: 2026-04-30
fetch_date: 2026-05-01T05:34:39.920624
---

# 关于 CTF 中 Bcrypt 考点的思考

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/g673ce4c7rnJibMWFUvSUR2FK6IryPqWSnjzAb6ia1MOmg4RPPRsSh61uezeiahYOn3P5tia2IYoInibdEu5TUlz5v6icJI4icUagZJTF9mzCTrsSk/0?wx_fmt=jpeg)

# 关于 CTF 中 Bcrypt 考点的思考

studying-egg
studying-egg

正在思考ing

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

## 参考链接

https://xz.aliyun.com/news/91875

## 引言

最近在复现polarisctf的过程中，想到了软件系统安全区域赛有一道题很类似。都考察了控制流平坦化和bcrypt加密。 看题解的过程中对于预期值的寻找感觉没有说明清楚，这里分享一下个人的思考。

## polarisctf2026 - easyre

![](https://mmbiz.qpic.cn/mmbiz_png/g673ce4c7rm5iapCgRmtCE9QrldrQSK6G4PSsB7QHTwUOAFsLcWOrAM2ibJicf3nOP17cJ484wYuc8zDUsqlgg70wf7Lz9ewwceKPSWibPHVZicg/640?wx_fmt=png&from=appmsg)

通过程序的控制流程图，可以得出考察的是控制流平坦化

![](https://mmbiz.qpic.cn/mmbiz_png/g673ce4c7rmaJt0BBia8XCf0H4hy0D2Jec1cbJJ8rVF5pzKJlhfLS3zMhJgUurIfFLkPcsPOicb5qWTcFnNh5fQCodo05gvxpCYvDib8cgcZXc/640?wx_fmt=png&from=appmsg)

这里通过改变`r8`的来实现改变控制流 我们在`Import`表，发现导入了`bcrypt.dll`

![](https://mmbiz.qpic.cn/mmbiz_png/g673ce4c7rktk6UsjCicjgDKOSDodUXajbRS99hibzCNebtt1KEe1dicFwC7H4AUoMoRDibv11ur72UoktQQUY6F2pBsIFlrX8HtHcxgUNCw6nI/640?wx_fmt=png&from=appmsg)

**bcrypt.dll** 是 Windows 系统自带的核心加密动态链接库,我们通过劫持这里的传参，分析加密方式 我们需要重点关注下面几个API

```
// attributes: thunk
NTSTATUS __stdcall BCryptOpenAlgorithmProvider(
        BCRYPT_ALG_HANDLE *phAlgorithm,
        LPCWSTR pszAlgId,
        LPCWSTR pszImplementation,
        ULONG dwFlags)
{
  return __imp_BCryptOpenAlgorithmProvider(phAlgorithm, pszAlgId, pszImplementation, dwFlags);
}

phAlgorithm:算法句柄
pszAlgId : 加密算法字符串
LPCWSTR pszImplementation:算法提供者（默认是微软）
dwFlags: 功能标志。默认是0
// `BCRYPT_ALG_HANDLE_HMAC_FLAG` → HMAC 模式
// `BCRYPT_ALG_HANDLE_AES_GMAC_FLAG` → AES GMAC 模式
```

指明加密算法

```
// attributes: thunk
NTSTATUS __stdcall BCryptGenerateSymmetricKey(
        BCRYPT_ALG_HANDLE hAlgorithm,
        BCRYPT_KEY_HANDLE *phKey,
        PUCHAR pbKeyObject,
        ULONG cbKeyObject,
        PUCHAR pbSecret,
        ULONG cbSecret,
        ULONG dwFlags)
{
  return __imp_BCryptGenerateSymmetricKey(hAlgorithm, phKey, pbKeyObject, cbKeyObject, pbSecret, cbSecret, dwFlags);
}

BCRYPT_ALG_HANDLE hAlgorithm, // [in] 算法句柄
BCRYPT_KEY_HANDLE *phKey, // [out] 输出：密钥句柄
PUCHAR pbKeyObject, // [out] 密钥内存缓冲区
ULONG cbKeyObject, // [in] 缓冲区大小
PUCHAR pbSecret, // [in] 原始密钥数据
ULONG cbSecret, // [in] 原始密钥长度
ULONG dwFlags // [in] 标志位
```

指明密钥

```
// attributes: thunk
NTSTATUS __stdcall BCryptEncrypt(
        BCRYPT_KEY_HANDLE hKey,
        PUCHAR pbInput,
        ULONG cbInput,
        void *pPaddingInfo,
        PUCHAR pbIV,
        ULONG cbIV,
        PUCHAR pbOutput,
        ULONG cbOutput,
        ULONG *pcbResult,
        ULONG dwFlags)
{
  return __imp_BCryptEncrypt(hKey, pbInput, cbInput, pPaddingInfo, pbIV, cbIV, pbOutput, cbOutput, pcbResult, dwFlags);
}

NTSTATUS __stdcall BCryptEncrypt( BCRYPT_KEY_HANDLE hKey, // [in] 密钥句柄
PUCHAR pbInput, // [in] 明文数据（要加密的内容）
ULONG cbInput, // [in] 明文长度（字节）
void* pPaddingInfo, // [in] 填充信息指针（大部分传NULL）
PUCHAR pbIV, // [in] 初始化向量 IV
ULONG cbIV, // [in] IV长度（字节）
PUCHAR pbOutput, // [out] 输出：密文数据
ULONG cbOutput, // [in] 输出缓冲区大小
ULONG* pcbResult, // [out] 实际加密后的密文长度
ULONG dwFlags // [in] 功能标志 );
```

通过服务端和客户端两个程序可以大胆猜测，这道题的校验逻辑存在于服务端中 开始动态调试

![](https://mmbiz.qpic.cn/mmbiz_png/g673ce4c7rlJicG1zE6tnzwz0k0H5vZTibaJ98clBphVJ9eCQUmicaWq70PNuXu1f2wE3AN66DuxiaRNRTh0LVaLqz2ObRTaEllaggYick780Qicw/640?wx_fmt=png&from=appmsg)

开始是一个`RC4`加密 这里是将客户端的数据进行解密，这里我们直接跳过，查看下一个加密算法

![](https://mmbiz.qpic.cn/mmbiz_png/g673ce4c7rnXYGa1wP2hMWGbJtXwjfpKWGOXP1CMlj4IAtXZUKqoPXAfkuermzsBNst5UicIDeJANZKRewgyyXYl2KRQ0q0f7FibsBCIEsCvo/640?wx_fmt=png&from=appmsg)

这次是`MD5`我们需要再在`BCryptHashData`处打上断点

```
// attributes: thunk
NTSTATUS __stdcall BCryptHashData(BCRYPT_HASH_HANDLE hHash, PUCHAR pbInput, ULONG cbInput, ULONG dwFlags)
{
  return __imp_BCryptHashData(hHash, pbInput, cbInput, dwFlags);
}
```

我们查看`pbinput`的值，发现是我们的输入

![](https://mmbiz.qpic.cn/mmbiz_png/g673ce4c7rmTgPqb47h1kpnIs8stK9aM7kpS93vZwJ6nEiapVOYwenQiaTBsWA4eQjE0ZZK7km62mdLeYOsIiatOPtpQhWbcicFNL5ia9PV87hrY/640?wx_fmt=png&from=appmsg)

我们需要再在`BCryptFinishHash`处打上断点，查看我们最终的哈希计算值

```
// attributes: thunk
NTSTATUS __stdcall BCryptFinishHash(BCRYPT_HASH_HANDLE hHash, PUCHAR pbOutput, ULONG cbOutput, ULONG dwFlags)
{
  return __imp_BCryptFinishHash(hHash, pbOutput, cbOutput, dwFlags);
}
```

运行到这里，我们查看`pbOutput`的值，发现其中并不是输入值(`123456`)的`MD5`哈希值，不着急，我们步进进入`BCryptFinishHash`函数内部

![](https://mmbiz.qpic.cn/mmbiz_png/g673ce4c7rkIDFXOcibnM5xibRdIdNwoc8WHQVEOLLkA5QxDXMicE9IPgDa7WrLicJtdiaDSPiaEuMMVttcJK6s1gtxicmwpeN6chLHsibGqpH2VmS4/640?wx_fmt=png&from=appmsg)

这里通过观察，`pbOutput`的地址指针保存在`RDX`指针中，我们定位到具体位置，观察变化

![](https://mmbiz.qpic.cn/mmbiz_png/g673ce4c7rlg1WJlIFQQ2BAnYuDXuBobEMI9cF2pY1Cv1fichlvz4KDpEibOe1WuKhdsUoG7qhK8Y1YdeqvMPykwPleTia0aFbHxmBHwV44DUc/640?wx_fmt=png&from=appmsg)

通过变化，最终该地址得到了正确的`MD5`哈希值，后面程序的逻辑应该是对该值与预期值进行比较，所以这里我们给这里打上硬件断点 PS:IDA里面不知道怎么打硬件断点，这里换到`x64dbg`打硬件断点吧

![](https://mmbiz.qpic.cn/mmbiz_png/g673ce4c7rlaKtZ8Uy3undbiapOhWpVFfgM5Cp8uuHzTmReXP1HBPKbU86wia4m0yWuUyTVpR6ibMBIrs30NJST2lRiagAIJRynzwtC6YHENwfM/640?wx_fmt=png&from=appmsg)

继续运行程序

![](https://mmbiz.qpic.cn/mmbiz_png/g673ce4c7rm8AgyHzuj4G5pkv810qLKIck1h0BaA43e9gPHPWrfOl1c6GoUKWBkVuMB7ia1Vdv46LQsRgMPdRswbgzqZhQUA9VXBG6364Itk/640?wx_fmt=png&from=appmsg)

停到了这段代码上，分析可得这段代码的作用是将输入的`MD5`值由ASCII值转换为16进制，最终保存到`[rsp+100]`地址处。同理我们对这里的地址打上硬件断点

![](https://mmbiz.qpic.cn/mmbiz_png/g673ce4c7rmHfCw9wLib9yM9xibQJVibGUbskYHt58UiaPSuVSMQjGDzficmYln8odg7Ov70Tf0Yic7q5iazjZr7jJMVPV4OvhbX5VS4Rviau8mQybg/640?wx_fmt=png&from=appmsg)

这里我们找到了期待值`E5D489FD91431D5438EB28F7490F9CE0`我们通过脚本进行爆破

```
import hashlib

import itertools

import string

from multiprocessing import Pool

# 目标MD5哈希值

target_hash = "E5D489FD91431D5438EB28F7490F9CE0"

# 生成可能的字符串

def generate_strings(length):

   chars = string.ascii_lowercase # 使用小写字母

   return itertools.product(chars, repeat=length)

# 验证MD5

def verify_md5(candidate):

   candidate_str = ''.join(candidate)

   if candidate_str == "ctfer":

       print(candidate_str)

   md5_hash = hashlib.md5(candidate_str.encode()).hexdigest()

   if md5_hash == target_hash.lower():

       return candidate_str

   returnNone

# 爆破函数

def crack_md5(length):

   for candidate in generate_strings(length):

       result = verify_md5(candidate)

       if result:

           return result

   returnNone

if __name__ == "__main__":

   # 设置最大尝试长度

   max_length = 5

   with Pool() as pool:

        result = pool.apply_async(crack_md5, (max_length,))

        if result.get():

            print(f"找到匹配字符串: {result.get()}")

# ctfer
```

用户名爆破成功后，序列号采取同样的方法进行爆破 最终flag`62001be6b65779c64e67deb560164745`

## 软件系统安全赛区域赛 - crackme

思路基本同上

![](https://mmbiz.qpic.cn/sz_mmbiz_png/g673ce4c7rleiaLNGNyo63wibReicFnFwz0vIm1NnZSibVKicqx7s3AVFVichHAEWGIontJDtiaYV602ktJyXJlwBwyhGibLGxNIbZiblCpCE0kII5C8/640?wx_fmt=png&from=appmsg)

随意个一输入错误输入，可以看到预期值 预期值为：`FC 8F 2B 91 3A 35 B5 E8 70 EB 18 63 79 F4 CB A0 C4 B0 CC 19 8D 3F A6 39 C5 4E E2 0D 1A 8E 3E 6C 79 16 BD 4C A3 BE 71 4B 95 FC A7 CD 77 73 A2 56`

在`BCryptOpenAlgorithmProvider`和`BCryptGenerateSymmetricKey`以及`BCryptEncrypt`处打上断点

程序逻辑为先进行`DES`加密，再进行`AES-CBC`加密，并与预期值进行比较

通过`BCryptGenerateSymmetricKey`找到密钥

![](https://mmbiz.qpic.cn/sz_mmbiz_png/g673ce4c7rldGibNjO3VRvVQrsB3VaicZ22rODzVZmVeRJqcUADOCdrnvc6hlhkzmfC7IzeA7hfHOgbb3QhQ1RXLyV4JQNV0XZic6xWS2Vh3ng/640?wx_fmt=png&from=appmsg)

密钥值为：91adf387c9b48aeed2a19fc7b3d985e4 在`BCryptEncrypt`找到`IV`值

![](https://mmbiz.qpic.cn/sz_mmbiz_png/g673ce4c7rlNUq7Irib53hDd9OSLV6rKhicP5SazyJzxyRtphPMdYqJDojceFjDH2PukonHDJ2cpvaOnKvtO2fDLxHMO1rNtrngtTsibboCxBA/640?wx_fmt=png&from=appmsg)

IV值为：6ec1a237589f03d4b5e70c92fa418b66 进行解密

![](https://mmbiz.qpic.cn/sz_mmbiz_png/g673ce4c7rnfVIC6dJ9UrXNwwJ0cru5u55V6maJoy7sCsbZPcibdEvicZ8Xibh5tbMFjmlFrMXBrnVMicpFHk8eia97s5sfSic4UdhwqSdgqW2eEQ/640?wx_fmt=png&from=appmsg)

检验：

![](https://mmbiz.qpic.cn/mmbiz_png/g673ce4c7rl54nVJUXiaU0blQNVywGc2XAuzpVLBy43Lfg009XxvPrR515Rex5Nfpu4Eu8RN8jem1HS60ss59SibEDkmXeJZhMEUKxZIKpTLo/640?wx_fmt=png&from=appmsg)

## 结语

其实软件系统安全赛区域赛看到crackme的时候就联想到polarisc...