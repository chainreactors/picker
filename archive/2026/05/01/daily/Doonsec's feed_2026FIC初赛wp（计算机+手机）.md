---
title: 2026FIC初赛wp（计算机+手机）
url: https://mp.weixin.qq.com/s/GGWotBuAjkespYeaKTAlWg
source: Doonsec's feed
date: 2026-05-01
fetch_date: 2026-05-02T04:56:21.429215
---

# 2026FIC初赛wp（计算机+手机）

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/T5C6icTcSx9Pxd7ARnC7fbKTuD9JiaeWuApBctefPgzXkxKCb1QupbfkWeIJjlWPXmSDpdUPzM8WfQqWNt1hTNM7CiaOwEvhwTMUFvdVwiaiaTMY/0?wx_fmt=jpeg)

# 2026FIC初赛wp（计算机+手机）

原创

Serendipity
Serendipity

Serendipity的小屋

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

检材密码：`FIC-{e404d6e66586e9460c23755afab5a872bcf78ab4}`

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/T5C6icTcSx9PJF0NhzAzuupk3zSxaVDcBicMJ8tdibwURhKISKiaUl3waINmryLhSibv3D61w7GicfeoznnvibgRb237hC1Fwm0lTcPJ5jn6px5RGA/640?wx_fmt=jpeg&from=appmsg "null")

> 比赛排名22，与大佬们的差距还是太大了orz......好消息是晋级了，大佬们决赛见！
>
> 本来想着全写完发的，实在是太忙了，就先发计算机和手机吧

## 计算机部分

计算机VC密码在手机便签中

![](https://mmbiz.qpic.cn/mmbiz_png/T5C6icTcSx9OGVSl7YV3icuuUBO8aS0VfFAlOnbpBFuWMJAYtmNXawo5OXPq85ViaBIRcSBjfdEz5vRzA7d3rIpo4qenIF9EOug5fVic1crWW1M/640?wx_fmt=png&from=appmsg "null")

### 1. 分析计算机检材，操作系统版本号为 【参考格式：1.1】

**23.1**

在基本信息里可以看到

![](https://mmbiz.qpic.cn/sz_mmbiz_png/T5C6icTcSx9NIgsJks7aRUU35qKQ6hnicnpdEeYicHWZpr9GWDZLia4UJZt6V6pAIicLPQSvc6n8y5YYyKtxibE51UpnMMuFkPsicEJyic4ncVzzO0c/640?wx_fmt=png&from=appmsg "null")

### 2. 分析计算机检材，李安弘曾收到一份免费领取token的邮件的疑似钓鱼邮件，其发送用户邮箱为【参考格式：123@qq.com】

**hf13338261292@outlook.com**

在邮件中一眼可以看到

![](https://mmbiz.qpic.cn/mmbiz_png/T5C6icTcSx9NJHI8e9ZsCB6VcfVicKz06los9Vrgt98caic9sCJsIQNgicGrzHHpk43IUm9wrYVB5wibBXYw7s57yvQQSxN0HtnL9y11mTx21iaPs/640?wx_fmt=png&from=appmsg "null")

### 3. 分析计算机检材，李安弘电脑中记录的黄金换现金的商家联系方式为 【参考格式：110】

**13612817854**

仿真之后再开始页面找到了一个记事本

![](https://mmbiz.qpic.cn/sz_mmbiz_png/T5C6icTcSx9MCEdU0UvwTibMddD3edcZDeAoVvwvfpsl781vYeMX8Eu2rOYQ9Dygx9CcllsicC9QV9mzt5ADqMQg94OlVPupOcaERN0RYRYRuU/640?wx_fmt=png&from=appmsg "null")

打开看到黄金换现金的商家联系方式

![](https://mmbiz.qpic.cn/sz_mmbiz_png/T5C6icTcSx9NICYOuJcvYZqqJPSducIHQJM3RWGoIdTiaOe2Ld4UKBLkxrW2tSFicFFh5icLWibYky9cLLibxcSib923F4N58UgEcQeiaD0yWv13clM/640?wx_fmt=png&from=appmsg "null")

### 4. 分析计算机检材，推广设计图中的apk下载链接为【参考格式：http:///?\*】

**https://drive.google.com/file/d/1z3aRS-lkaJYKm7Cp1XjtUmVPsOEVW2fV/view?usp=sharing**

在下载文件夹中看到了推广设计图

![](https://mmbiz.qpic.cn/sz_mmbiz_png/T5C6icTcSx9OoFIUTJv6nRFzIvGdq2E0KpQeuQyuxdibx4hmEGcn5gaicMLnQ5lBsibmtSwzljs9b7apHMG9JibiaEIuuLWfxibR1KxWXt6NOjicq1o/640?wx_fmt=png&from=appmsg "null")

这个图片是被加密的，这个html可以查看加密图片，私钥是rsa的n和d![](https://mmbiz.qpic.cn/mmbiz_png/T5C6icTcSx9PN6lQu0Sb7bbzWYUmknryS2zRSXCTlMVhbG8cg3pyoMNgRJL0G2cianXz3cVypwHNZjicbuy62FhGBcXiaaWMFqLqdyEZC1YMdPo/640?wx_fmt=png&from=appmsg "null")

在public.txt中看到了n和e，算出d，写出解密脚本

```
import sympyimport libnum
n = 57751892008149574447756694613209346511056045951970458143905594411398554113111623746466692172544473909892773600617029641656248235151775166339061269972238018743173330948084699695182438765935110193323089354031112350869626121317836465551360104372140181097747761558797918522051881262043738603183528521379831286761e = 65537
# 分解 np, q = sympy.factorint(n).keys()  # 只适用于小 np, q = list(sympy.factorint(n).keys())print(f"p={p}, q={q}")
phi = (p-1)*(q-1)d = libnum.invmod(e, phi)print(f"d = {d}")
```

![](https://mmbiz.qpic.cn/mmbiz_png/T5C6icTcSx9MeGBDp9RjHe17LlBMZiaLFEueBswUlM1v6jNAhb7jq1NVrd32T2oaOMgIjgtwksL5eJbDsXzLBIYaufL2Tz002ibiapPr6ibNiau00/640?wx_fmt=png&from=appmsg "null")
接下来解密一下图片

![](https://mmbiz.qpic.cn/sz_mmbiz_png/T5C6icTcSx9OMMibl8nKOGwcrELA1FlStmKyCicLFLbWgBjEBiaHicuzxkeia2IP0LKhHrmfNKH6iaicoM53wfCobbPMxeRYtxic3ibY8ZRzzZ4vryHCI/640?wx_fmt=png&from=appmsg "null")

扫码识别一下

![](https://mmbiz.qpic.cn/sz_mmbiz_png/T5C6icTcSx9PVxz1NqINjhSJYUnncYicMpNPEWmicDLg0UAPAQfnYyqJ4rWVmjCbxTtYSlibn9ySRIyJYyqiaU7j4BadkHgm5mszNwghk9HWNG84/640?wx_fmt=png&from=appmsg "null")

### 5. 分析计算机检材，李安弘电脑vpn软件开放的代理端口为 【参考格式：80】

**9527**

在开始菜单这里看到clash

![](https://mmbiz.qpic.cn/sz_mmbiz_png/T5C6icTcSx9P4Ods1ibibpg1NfSeF5dpChDfo7B9rqGqUe7eVmibSNSvCDOKoeAgN7UmW3UibISGGicN9X2OL9nqW7zT7xvzjzCr8P5H2Gj5Ty7ds/640?wx_fmt=png&from=appmsg "null")

查看设置

![](https://mmbiz.qpic.cn/mmbiz_png/T5C6icTcSx9OvBu4K2nmKgC27SqlcyKOMicLwRib5gZ9DhKQwpBPiaZEhuQAv1w3mMSibMjtQIp3dDO8u9yQsG2kV55J19sWFqhklDrA8GiaFmIMs/640?wx_fmt=png&from=appmsg "null")

### 6. 分析计算机检材，李安弘电脑中AI软件当前使用的模型类型为 【参考格式：deepseek】

**OpenRouter**

在电脑右下角看到了ai软件

![](https://mmbiz.qpic.cn/mmbiz_png/T5C6icTcSx9MtNhEFu8hIpDI8YHkHSm6LdQurlkyAeiaWOuoFnSSclsB4TspxWFeyrsSbhxE7yX1wEyjmZj6iaMzrIYEuicPxEcF8CS8DWgKl9I/640?wx_fmt=png&from=appmsg "null")

查看设置

![](https://mmbiz.qpic.cn/sz_mmbiz_png/T5C6icTcSx9P4fyEYiczLP4FI3c9fGzgmCfLM2pH02X1eZ29OB8elL4RBRcfVtKsiaHU2TzzbQoFLribTczaKLRsMrZOzYKoELTmDn5Q3QFYFIY/640?wx_fmt=png&from=appmsg "null")

### 7. 分析计算机检材，李安弘电脑中AI软件当前使用的模型apiKey为【参考格式：sk-abcd...】

**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**

搜索一下有关这个ai的文件夹，找到一堆，从文件数量最多的开始看

![](https://mmbiz.qpic.cn/mmbiz_png/T5C6icTcSx9PKf20BgqMx9lrvQHIoG6SD7OteqUpicagr5lqNbB3mtF4n75bbKGTxz7WQBfeZtYg4K1AOCCJibWMAbEzLOGPkkWaUBp0Y9f2hI/640?wx_fmt=png&from=appmsg "null")

在`/home/lha/.local/share/deepin/uos-ai-assistant`文件夹下找到db文件![](https://mmbiz.qpic.cn/sz_mmbiz_png/T5C6icTcSx9MSlDibdedHNbxquF7Sq4X7E7wwr9a3mAzlApxTLJsRKDVEDS3tkKxCsBLwa30zu5OPwF4mwGyIcWmE7QEl5cpYPoib40MZ7vo4M/640?wx_fmt=png&from=appmsg "null")

![](https://mmbiz.qpic.cn/mmbiz_png/T5C6icTcSx9PW0dibnM3VvbStNFT4WImHnvOlqzvfxLaebK87icG4Rjb6SPSuuNrHBvE2OPZG4mbw7sia5P4RVCapVUNtmfnXhR3r7OJe3AGWeQ/640?wx_fmt=png&from=appmsg "null")

### 8. 分析计算机检材，李安弘电脑中勒索软件提供的解密服务联系方式为 【参考格式：abcd123232】

**beijixin996@tutanota.com**

用手机中的VC密码解密一下磁盘`9ed2@99y8.com.cn`

![](https://mmbiz.qpic.cn/sz_mmbiz_png/T5C6icTcSx9MaPVuibmdlC0RXeLcBRWXI5O6edR8xJ9ydGCRKhU6V5dJopeGj6umbI9ZuRQepPN4JVGAuVeGaoIjhCjHwsVSBgVyMibJHjwp4s/640?wx_fmt=png&from=appmsg "null")

看到文件中有个get\_token\_linux文件，在浏览器的历史记录中看到访问了github中类似的文件![](https://mmbiz.qpic.cn/mmbiz_png/T5C6icTcSx9NWrEfoCr24gx9retP60D3ssSuZGPcMTMf5yv0JkWddn3H3Mgu41DxtYVZ6YlOryicJKQvqrOib6AibpEEGEcEicaVI2Q0iaBWAFrmc/640?wx_fmt=png&from=appmsg "null")

![](https://mmbiz.qpic.cn/sz_mmbiz_png/T5C6icTcSx9OK4xUqNsasickJxibwmju6GxkMFibqr2oaA60fCGzZfib1Wcgxa3Xx3uZjicakZf0WSKmPKia7ks8e2ic4icUcl9sXVbeB8khc5PXicZPk/640?wx_fmt=png&from=appmsg "null")

将这个文件导出拿ida查看一下，反编译main\_main,看到有个邮箱

![](https://mmbiz.qpic.cn/sz_mmbiz_png/T5C6icTcSx9NsdYACxWIMzPnF9M3yfjk0exWQJib6ibFKfibM3libpRT5GsyDsWSNiaxxP0wQmichbibiaz9Rj7t3NYcYQQsMaqeClTPgCVrw44SkzWc/640?wx_fmt=png&from=appmsg "null")

转换一下邮箱上面两行可以看到  `解密请系系`，所以就是这个邮箱

![](https://mmbiz.qpic.cn/mmbiz_png/T5C6icTcSx9MTT3dFe71YfQEiaNiaysmZxKlmsvziaxU6DA9MnMfyJFZ7Mlh3v8cT9advmvlHJdt08ezJb8waNXw9FyKNMibWAlrSE72XZD1prKg/640?wx_fmt=png&from=appmsg "null")

### 9. 分析计算机检材，李安弘电脑中记录的存放黄金的保险柜编号是 【参考格式：1】

**997546**

分析main\_main和main\_a两个函数可知，这个程序会将mp4文件进行加密，然后同目录下.hidden文件也有提示

![](https://mmbiz.qpic.cn/mmbiz_png/T5C6icTcSx9N5LHqNMmJCC7yc44l9diaLUUY9FZSdPxsicVT2RBmBia026kSrAKL8xgibdk4QofmRliaVAfAxiaiaia1Ve3pfvXyialX1JDa4SxVGR3CY/640?wx_fmt=png&from=appmsg "null")

写一个解密脚本，解密一下与这个程序同目录下的mp4文件

```
#!/usr/bin/env python3import struct, sys, shutilfor f in sys.argv[1:]:    shutil.copy2(f, f+'.bak')    d = bytearray(open(f,'rb').read())    p = 0    while (p := d.find(b'stco', p)) != -1:        n = struct.unpack('>I', d[p+8:p+12])[0]        for i in range(n):            e = p+12+i*4            d[e:e+4] = struct.pack('>I', (struct.unpack('>I', d[e:e+4])[0]-1337)&0xFFFFFFFF)        p = p+12+n*4    open(f,'wb').write(d)    print(f'已修复: {f}')
```

修复之后打开mp4文件

![](https://mmbiz.qpic.cn/sz_mmbiz_png/T5C6icTcSx9Njl3cs7LEH6MkgciaZ384dlj0FhcMMFicKQmDgtmUuzZPnjbPwEYraEdx491E7yIiaHMUiavyQU3EH6gsWSuxRiae15SQ1sZLVWwMw/640?wx_fmt=png&from=appmsg "null")

### 10. 分析计算机检材，李安弘电脑中记录的保险柜密码是 【参考格式：123456】

**583985**

在`/root/文档/zhongyao`看到有关保险箱密码的文件

![](https://mmbiz.qpic.cn/sz_mmbiz_png/T5C6icTcSx9MJsddiayB4miatp0p9ibV76gAFyeTemdXbVetwfMibZvZUnnESibK14icJ34UTxpckyZvuHAC0a3wTfrWxSse18lYdDH2xicS1FSIa2Q/640?wx_fmt=png&from=appmsg "null")

导出发现没有内容，在电脑中看到excel的加密代码

![](https://mmbiz.qpic.cn/mmbiz_png/T5C6icTcSx9MuGC1bCic78v4JGWK31QiaBcCYKWlDxK3SFKXBCHIMgRnSHdHqfFHf1Lt6Ev1pYHQoNJdj1gIsQ25Pv0qnFib4ibKICOrDylDGMpI/640?wx_fmt=png&from=appmsg "null")

让ai写一个脚本解密一下

```
import olefileimport struct
ole = olefile.OleF...