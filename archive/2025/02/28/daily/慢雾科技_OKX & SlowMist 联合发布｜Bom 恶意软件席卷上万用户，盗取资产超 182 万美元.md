---
title: OKX & SlowMist 联合发布｜Bom 恶意软件席卷上万用户，盗取资产超 182 万美元
url: https://mp.weixin.qq.com/s?__biz=MzU4ODQ3NTM2OA==&mid=2247501336&idx=2&sn=fd4597e1846db1f94a777977951fde9a&chksm=fddeb89fcaa93189ff6fa7dfa5c9a0405664cc357827e613dcb6f4d5338d07248640b523eaf0&scene=58&subscene=0#rd
source: 慢雾科技
date: 2025-02-28
fetch_date: 2025-10-06T20:38:54.855886
---

# OKX & SlowMist 联合发布｜Bom 恶意软件席卷上万用户，盗取资产超 182 万美元

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/qsQ2ibEw5pLZJBtUlXow7INKOj3Bw8mEU4gwH7fv7POzlLr2hz1kGET9qYsYia6yT0vOWV9YA3bM9AKicPdkEuZDA/0?wx_fmt=jpeg)

# OKX & SlowMist 联合发布｜Bom 恶意软件席卷上万用户，盗取资产超 182 万美元

原创

OKX & SlowMist

慢雾科技

![](https://mmbiz.qpic.cn/mmbiz_png/qsQ2ibEw5pLZJBtUlXow7INKOj3Bw8mEUkNHyCpufiafcJTeq272AdrvTUicNdjRtGL52UmnBDqLptiaKtV3C0DvCQ/640?wx_fmt=png&from=appmsg)

2025 年 2 月 14 日，多名用户集中反馈钱包资产被盗。经链上数据分析，被盗案例均符合助记词/私钥泄漏的特征。进一步回访受害用户后发现，他们大多曾安装并使用过一款名为 BOM 的应用。深入调查表明，该应用实为精心伪装的诈骗软件，不法分子通过该软件诱导用户授权后，非法获取助记词/私钥权限，进而实施系统性资产转移并隐匿。因此，SlowMist AML 团队和 OKX Web3 安全团队对该恶意软件的作案手法进行调查和披露，并进行链上追踪分析，希望能为用户提供安全警示与建议。

![](https://mmbiz.qpic.cn/mmbiz_png/qsQ2ibEw5pLZJBtUlXow7INKOj3Bw8mEUVP7zhXg6k8TgoZyI5kIhofdI5JkP0ic8O3YbZekCbkiahBRlxoxA33bw/640?wx_fmt=png&from=appmsg)

**恶意软件分析**

经过用户同意，OKX Web3 安全团队收集了部分用户手机上的 BOM 应用程序的 apk 文件进行分析，具体细节如下：

**（一）结论**

1. 该恶意 app 在进入合约页面后，以应用运行需要为由，欺骗用户授权本地文件以及相册权限。

2. 获取用户授权后，该应用在后台扫描并收集设备相册中的媒体文件，打包并上传至服务端。如果用户文件或相册中有存储助记词、私钥相关信息，不法分子有可能利用该应用收集到的相关信息盗取用户钱包资产。

**（二）分析过程**

1. 样本初步分析

1）应用签名分析

签名 subject 不规范，解析后为 adminwkhvjv，是一堆没有意义的随机字符，正常应用一般为一段有意义的字母组合。

![](https://mmbiz.qpic.cn/mmbiz_png/qsQ2ibEw5pLZJBtUlXow7INKOj3Bw8mEUzQLCZZzX9XE60U5fj8g34XkW7bhXaBZOjBDVql5EfotLzVshbNnVcw/640?wx_fmt=png&from=appmsg)

2）恶意权限分析

在该应用的 AndroidManifest 文件中可以看到，注册了大量权限。其中包含一些信息敏感的权限，包括读写本地文件、读取媒体文件、相册等。

![](https://mmbiz.qpic.cn/mmbiz_png/qsQ2ibEw5pLZJBtUlXow7INKOj3Bw8mEUm7YNSpbZUIeEl6Y6FD0Zj5UNgrtvReLTCMo21Cz2cdtCkG64t91MJA/640?wx_fmt=png&from=appmsg)

2. 动态分析

由于分析时 app 后端接口服务已下线，app 无法正常运行，暂无法进行动态分析。

3. 反编译分析

反编译后发现，该应用中 dex 中的类数量非常少，针对这些类进行代码层面的静态分析。

![](https://mmbiz.qpic.cn/mmbiz_png/qsQ2ibEw5pLZJBtUlXow7INKOj3Bw8mEUXWZ067V18Nic1lxxWvoNouCKhmOwH4UwZoWXCkLpaYibMVQf5ZjnsKRg/640?wx_fmt=png&from=appmsg)

其主要逻辑为解密一些文件，并加载 application：

![](https://mmbiz.qpic.cn/mmbiz_png/qsQ2ibEw5pLZJBtUlXow7INKOj3Bw8mEU9648xcNCcNwscxPiak8OsXaOz0WQx2zf2rtNeVRTu83yMe5PTzQdibRQ/640?wx_fmt=png&from=appmsg)

在 assets 目录下发现 uniapp 的产物文件，表明该 app 使用了跨平台框架 uniapp 进行开发：

![](https://mmbiz.qpic.cn/mmbiz_png/qsQ2ibEw5pLZJBtUlXow7INKOj3Bw8mEUaYpqKkkvic0AfYptoVR8qHKWMZNWnFp3tu407o5dxtz8wNR44U0BvMw/640?wx_fmt=png&from=appmsg)

在 uniapp 框架下开发的应用的主要逻辑在产物文件 app-service.js 中，部分关键代码被加密至 app-confusion.js 中，我们主要从 app-service.js 开始分析。

1）触发入口

在注册各个页面的入口处，找到了名为 contract 页面的入口：

![](https://mmbiz.qpic.cn/mmbiz_png/qsQ2ibEw5pLZJBtUlXow7INKOj3Bw8mEUE4KgheZuoDpDUvpsuR4FJjDHwVrVO3RgNDvdUn16C3oacSH4E6yYkg/640?wx_fmt=png&from=appmsg)

对应的函数 index 是 6596：

![](https://mmbiz.qpic.cn/mmbiz_png/qsQ2ibEw5pLZJBtUlXow7INKOj3Bw8mEUJN0SGJic8IxUn3lyibD7x7QOqTibpRdShiaick6yvwoeeBStSicyZWxIXM7g/640?wx_fmt=png&from=appmsg)

2）设备信息初始化上报

contract 页面加载后的回调 onLoad() 会调用到 doContract()：

![](https://mmbiz.qpic.cn/mmbiz_png/qsQ2ibEw5pLZJBtUlXow7INKOj3Bw8mEUF8EMicH2YvOKvl2j03JAsDmVgbZAZ3BasbfF9yFzp7apuk1IFuthUmg/640?wx_fmt=png&from=appmsg)

在 doContract() 中会调用 initUploadData()：

![](https://mmbiz.qpic.cn/mmbiz_png/qsQ2ibEw5pLZJBtUlXow7INKOj3Bw8mEUy3hLbpqELfn0FCvbqdBI2AeFlPrn7PymyEU2EftY17v0tLyuz2cCibQ/640?wx_fmt=png&from=appmsg)

initUploadData() 中，会先判断网络情况，同时也会判断图片和视频列表是否为空。最后调用回调 e()：

![](https://mmbiz.qpic.cn/mmbiz_png/qsQ2ibEw5pLZJBtUlXow7INKOj3Bw8mEU2Q9YObnUx1XGsibKoVWjfEf7kaL3WKo8HBbTice4fwqp68FwjS7mzpuA/640?wx_fmt=png&from=appmsg)

回调 e() 就是 getAllAndIOS()：

![](https://mmbiz.qpic.cn/mmbiz_png/qsQ2ibEw5pLZJBtUlXow7INKOj3Bw8mEUJcQsAexia9icQB3via9pCpQspQ6TN0mfj1gqicgiaQCyNkrcC5cMep0Q5icQ/640?wx_fmt=png&from=appmsg)

3）检查和请求权限

这里在 iOS 中会先请求权限，并以应用正常运行需要的文案欺骗用户同意。这里的请求授权行为就比较可疑了，作为一个区块链相关的应用程序，它的正常运行和相册的权限没有必然的联系，这一请求明显超出应用运行的正常需求。

![](https://mmbiz.qpic.cn/mmbiz_png/qsQ2ibEw5pLZJBtUlXow7INKOj3Bw8mEUEnYE1cfkGWcNfhZm0OgE9thWOXpWum3xZgcAjuBAYuVYgcHFiafbzyQ/640?wx_fmt=png&from=appmsg)

在 Android 上，同样先判断和申请相册权限。

![](https://mmbiz.qpic.cn/mmbiz_png/qsQ2ibEw5pLZJBtUlXow7INKOj3Bw8mEUCicPAlTfPvYicq2zJ9h4TLK76yiaCh8VDJnwzHciallAjiaFfTIJY7kIQVQ/640?wx_fmt=png&from=appmsg)

4）收集读取相册文件

然后在 androidDoingUp 中读取图片和视频并打包。

![](https://mmbiz.qpic.cn/mmbiz_png/qsQ2ibEw5pLZJBtUlXow7INKOj3Bw8mEUV2dWVAmrm7VIics1mlPIVGKJlTia0GYhBdNTbjW83IGTfrpDsrzS6gcA/640?wx_fmt=png&from=appmsg)

5）上传相册文件

最后在 uploadBinFa()、uploadZipBinFa() 和 uploadDigui() 中进行上传，可以看到上传的接口 path 也是一段随机的字符。

![](https://mmbiz.qpic.cn/mmbiz_png/qsQ2ibEw5pLZJBtUlXow7INKOj3Bw8mEUsicnIMPu4qicfibsicic5JOOg6ywOY6j4G6ibCPo8Upwiby2qfHMCN4pcVEUA/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/qsQ2ibEw5pLZJBtUlXow7INKOj3Bw8mEUKCI0DqJsyuKagibY98emA2Z35IfhXFDxSbMTg1w8E9UUiciaYrYCcNnxQ/640?wx_fmt=png&from=appmsg)

iOS 流程类似，获取权限之后，iOS 上通过 getScreeshotAndShouchang() 开始收集上传的内容。

![](https://mmbiz.qpic.cn/mmbiz_png/qsQ2ibEw5pLZJBtUlXow7INKOj3Bw8mEUSOjx7TYwdbS1b2Qj0v0Mb7vaJx8tIlW6Z4kkSWfreFu79fcibicAkcRg/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/qsQ2ibEw5pLZJBtUlXow7INKOj3Bw8mEU8NKaoHxMcohcqAibWLFib7Q3QZ5n7xmN7lUogMq74icdib6X9QLpqibNY3Q/640?wx_fmt=png&from=appmsg)

6）上传接口

上报 url 中的 commonUrl 域名来自 /api/bf9023/c99so 接口的返回。

![](https://mmbiz.qpic.cn/mmbiz_png/qsQ2ibEw5pLZJBtUlXow7INKOj3Bw8mEUicwcCaBGIYibyyamR4LrhveNt132Cia0FspbxvzIexiaWib9rC6WLtqs7nQ/640?wx_fmt=png&from=appmsg)

该接口的 domain 来自 uniapp 的本地缓存。

![](https://mmbiz.qpic.cn/mmbiz_png/qsQ2ibEw5pLZJBtUlXow7INKOj3Bw8mEU7xB9kZTUl9NicPicarslqLZIV6D4Wx41CZSawzkov8jbx66rFic7mkHRA/640?wx_fmt=png&from=appmsg)

未找到写入缓存的代码，可能被加密混淆后存在于 app-confusion.js 中，在一次历史运行时于应用缓存中看到该 domain。

![](https://mmbiz.qpic.cn/mmbiz_png/qsQ2ibEw5pLZJBtUlXow7INKOj3Bw8mEUxiaiamKeSHSWZhHj8rV4MDvYKCI21kP9n3ApFrUlIDOGottjUm4NiahPw/640?wx_fmt=png&from=appmsg)

**链上追踪分析**

据 SlowMist AML 旗下的链上追踪和反洗钱工具 MistTrack 分析，目前主要盗币地址 (0x49aDd3E8329f2A2f507238b0A684d03EAE205aab) 已盗取至少 1.3 万名用户的资金，获利超 182 万美元。

![](https://mmbiz.qpic.cn/mmbiz_jpg/qsQ2ibEw5pLZJBtUlXow7INKOj3Bw8mEUyZRF0r5Po6tyOs4iaZvCmRx7f9rVf7ibS8MXRkyb0ibyVrjospCCmkDUQ/640?wx_fmt=jpeg&from=appmsg)

(https://dune.com/queries/4721460)

![](https://mmbiz.qpic.cn/mmbiz_png/qsQ2ibEw5pLZJBtUlXow7INKOj3Bw8mEU8aK5PiaxezaBR9tsjSoNLNjzW9dUpYXUB5mKElwDRwaUnnvrxTm1BFA/640?wx_fmt=png&from=appmsg)

该地址 0x49aDd3E8329f2A2f507238b0A684d03EAE205aab 首笔交易出现在 2025 年 2 月 12 日，由地址 0x9AEf1CA082c17f9D52Aa98ca861b50c776dECC35 转入的 0.001 BNB 作为初始资金：

![](https://mmbiz.qpic.cn/mmbiz_png/qsQ2ibEw5pLZJBtUlXow7INKOj3Bw8mEUEyGrFhUVkKJwQgD3MfmEA3d8TDSa9M9X3IvUNlCR5mbwY5nt0WyXBg/640?wx_fmt=png&from=appmsg)

分析地址 0x9AEf1CA082c17f9D52Aa98ca861b50c776dECC35，该地址首笔交易也出现在 2025 年 2 月 12 日，其初始资金来自被 MistTrack 标记为“Theft-盗取私钥”的地址 0x71552085c854EeF431EE55Da5B024F9d845EC976：

![](https://mmbiz.qpic.cn/mmbiz_png/qsQ2ibEw5pLZJBtUlXow7INKOj3Bw8mEUwgeRuXX1nEs2siaSD3WHc9RPuNYB0ENsn8kic9xVNrAM5vLwOI14iaHBA/640?wx_fmt=png&from=appmsg)

继续分析初始黑客地址 0x49aDd3E8329f2A2f507238b0A684d03EAE205aab 的资金流向：

BSC：获利约 3.7 万美元，包括 USDC, USDT, WBTC 等币种，常使用 PancakeSwap 将部分代币换为 BNB：

![](https://mmbiz.qpic.cn/mmbiz_png/qsQ2ibEw5pLZJBtUlXow7INKOj3Bw8mEU053DSicIknQezveeGA5hYZOrFPLkkKgDBmBjoxRjOw8wSHBttLgYAMw/640?wx_fmt=png&from=appmsg)

目前地址余额为 611 BNB 和价值约 12 万美元的其他代币，如 USDT, DOGE, FIL。

![](https://mmbiz.qpic.cn/mmbiz_png/qsQ2ibEw5pLZJBtUlXow7INKOj3Bw8mEUPbCREkTJYp74pZ5FUaU51KHJmpuWG3l6Z5rfQ5WE9W1UhALDAsfS7Q/640?wx_fmt=png&from=appmsg)

Ethereum：获利约 28 万美元，大部分来自从其他链转入的 ETH，接着转移 100 ETH 到 0x7438666a4f60c4eedc471fa679a43d8660b856e0，该地址还收到了上述地址 0x71552085c854EeF431EE55Da5B024F9d845EC976 转入的 160 ETH ，共 260 ETH 暂未转出。

![](https://mmbiz.qpic.cn/mmbiz_png/qsQ2ibEw5pLZJBtUlXow7INKOj3Bw8mEUNFEzGfpqvnlufP6lJQtmMphd97ltofubelAu328HjLtva8ibDAfBT6g/640?wx_fmt=png&from=appmsg)

Polygon：获利约 6.5 万美元，包括 WBTC, SAND, STG 等币种，大部分代币已通过 OKX-DEX 兑换为 66,986 POL，目前黑客地址余额如下：

![](https://mmbiz.qpic.cn/mmbiz_png/qsQ2ibEw5pLZJBtUlXow7INKOj3Bw8mEUhJTetvtzU7fqcK5gicRtjWGa7DMEy7iaKIm7oks11SIEyQBss54KHKaw/640?wx_fmt=png&from=appmsg)

Arbitrum：获利约 3.7 万美元，包括 USDC, USDT, WBTC 等币种，代币兑换为 ETH，共 14 ETH 通过 OKX-DEX 跨链到 Ethereum：

![](https://mmbiz.qpic.cn/mmbiz_png/qsQ2ibEw5pLZJBtUlXow7INKOj3Bw8mEUxKha9QuiczrRKmvDsJSlmy0qX4ACIvumOeZBIxznKUd58ql8oaaWCiaw/640?wx_fmt=png&from=appmsg)

Base：获利约 1.2 万美元，包括 FLOCK, USDT, MOLLY 等币种，代币兑换为 ETH，共 4.5 ETH 通过 OK...