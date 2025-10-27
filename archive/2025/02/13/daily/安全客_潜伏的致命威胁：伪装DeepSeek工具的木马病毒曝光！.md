---
title: 潜伏的致命威胁：伪装DeepSeek工具的木马病毒曝光！
url: https://mp.weixin.qq.com/s?__biz=MzA5ODA0NDE2MA==&mid=2649787860&idx=1&sn=9df4d802e487ddb74e23a5fbfb301c0f&chksm=8893bdbbbfe434ad3c6dceb868fcad9854116c4dbb50d53f84d5664f65e620770f178025189b&scene=58&subscene=0#rd
source: 安全客
date: 2025-02-13
fetch_date: 2025-10-06T20:35:46.364873
---

# 潜伏的致命威胁：伪装DeepSeek工具的木马病毒曝光！

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/Ok4fxxCpBb5Lt5avhTNYtdMtNeH8CVtliaYQaHvHzVzVEOBnrmv3PiaagDGTJGOibSlChokRUs7Jw1oTtSw6ryOog/0?wx_fmt=jpeg)

# 潜伏的致命威胁：伪装DeepSeek工具的木马病毒曝光！

安全客

随着DeepSeek在人工智能领域的持续走红，不法分子开始利用其市场热度作为攻击诱饵。近日，360安全大脑就监测到了一款木马，伪装成深受欢迎的 DeepSeek工具，内部实则隐藏了**危害性极大的后门功能**。

经分析，该木马基于Electron框架构建，并集成了反调试和虚拟机检测能力，能够规避常规的安全分析环境。木马在执行前会悄然下载并部署特定版本的Node.js环境，通过多重加密验证及解密手段对关键组件进行保护。同时，木马还会直接从云端获取并解密远程恶意载荷以实现**动态更新**和**远控操作**。

**01**

**钓鱼传播**

该木马从传播开始就是利用了DeepSeek的热度。其幕后黑客精心构建了一个与DeepSeek官网高度相似的钓鱼页面，普通用户一旦被诱导访问该页面，是难以分辨其真伪的。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Ok4fxxCpBb5Lt5avhTNYtdMtNeH8CVtljxD8toal1eQEqO5jjO3qUibaUSWa8Bl3cibsuND7eL2a9O1rqYUfydVw/640?wx_fmt=png&from=appmsg)

图1. 黑客精心构建的钓鱼页面

不明真相的用户一旦点击了页面中的下载按钮，就会下载攻击者准备的木马安装包。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Ok4fxxCpBb5Lt5avhTNYtdMtNeH8CVtlKx9xJcrjpn6xia824gHq6p6YkCA5CvQAYzcQKVYxpYT0ur9bxibvwrvw/640?wx_fmt=png&from=appmsg)

图2. 下载木马

**02**

**样本行为分析**

**前期准备**

用户被诱导后，会下载到如下图所示的这样一款所谓的DeepSeek工具安装包。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/Ok4fxxCpBb5Lt5avhTNYtdMtNeH8CVtlibZzZvPIYnSdsic4wkwLAvynj3OJtfpMqN57NmCIiaK97Su98fibZnppGg/640?wx_fmt=jpeg&from=appmsg)

图3. 木马图标

木马安装包被执行后，会检测特定分析工具类进程。如果存在则退出执行，以此来避免自身被安全人员分析。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/Ok4fxxCpBb5Lt5avhTNYtdMtNeH8CVtl2oqicUk27MeMOicfb1M3ECRibT8tJibXSVB662OCekAtZicU2H9k4NjwDNA/640?wx_fmt=jpeg&from=appmsg)

图4. 木马检测分析工具相关代码

被检测的相关分析工具完整检测列表如下图：

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/Ok4fxxCpBb5Lt5avhTNYtdMtNeH8CVtl4nlJXMUnfwuoFKtGmwmib3ia73P8mMhERa2icFt2L0dXx8EjnxzViasCWA/640?wx_fmt=jpeg&from=appmsg)

图5. 被检测的分析工具完整列表

而在木马的代码前部，就加载了JavaScript脚本并访问C2服务器。这些相关内容均通过Base64算法进行了编码。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/Ok4fxxCpBb5Lt5avhTNYtdMtNeH8CVtlp4ojdb8YsO8qpfQlA8icrmdXcOsV6IsPEwsKE7sxswHCd9xesKUFlsw/640?wx_fmt=jpeg&from=appmsg)

图6. 经Base64编码后的JavaScript脚本及C2服务器

此外，木马还巧妙的利用了Google日历的记录功能，通过自定义其中内容来实现随时在线调整跳转C2服务的配置信息。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/Ok4fxxCpBb5Lt5avhTNYtdMtNeH8CVtlTCr3k0tU4h2657tWGdDtybKnlYfkJF4vRlLPoQkx99DHAYMfARGrtg/640?wx_fmt=jpeg&from=appmsg)

图7. 利用Google日历远程调整C2配置

而黑客在编写木马时，还使用了AES-CBC加密算法加密了木马载荷。而加密时所用的KEY和IV为随机生成，并存入到了Redis数据库中并设置了15天的缓存时常。数据库地址为如下：

redis://45.93.20.174:6379

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/Ok4fxxCpBb5Lt5avhTNYtdMtNeH8CVtlNwVibgwu5jQ1iaYsvZjw8I6vodFfHmLrA2qUtVaLVOao1wg5xDNCvLAQ/640?wx_fmt=jpeg&from=appmsg)

图8. 木马访问在线Redis数据库

**下载并部署Node.js 环境**

木马会从Node.js官网下载特定版本的压缩包并解压到本地，以便后续利用该 Node.js 执行环境来运行后续任务。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Ok4fxxCpBb5Lt5avhTNYtdMtNeH8CVtleCFMQzeo89Vp5WzfPchdjyibPpf3vBQLxAvW6Ticq9En10sBABm9kw7A/640?wx_fmt=png&from=appmsg)

图9. 下载并部署特定版本的Node.js

而在完成Node.js的部署后，会进行下一步的操作。木马首先会通过一段动态构造的脚本代码来实现远程动态加载与解密执行过程。而该代码还会根据传入的模块路径生成一段 JavaScript代码，并将其转换为Base64编码后的字符串。

在其生成的代码中，首先会通过fetch函数从如下远程地址中获取数据：

**hxxps://appliedaibusiness.com/ get\_encrypt\_file**

在获取到远程的响应后，便可从响应头中读取到被用于AES解密的密钥(X-Encryption-Key)与IV值(X-Encryption-IV)。接下来，木马会对响应内容的加密数据进行解密，再调用传入模块中的run方法处理解密后的数据。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Ok4fxxCpBb5Lt5avhTNYtdMtNeH8CVtlU93IOcmibVM9HOm8mzDvCIhE0gvnWkObTIlgVq09sIovvd48HjOeia8Q/640?wx_fmt=png&from=appmsg)

图10. 远程动态加载与解密执行恶意功能

**本地模块的解密与执行**

木马会在这部分功能代码中构造目标文件路径，根据 process.resourcesPath 的值找到 index.node 模块文件，再通过checkFileHash验证目标文件的完整性。若校验通过，则利用预设的Key与IV对index.node内容进行解密，并写回到index.node的同路径中。

解密完成后，木马会等待2秒再通过childProcess.execSync创建一个子进程来执行命令。执行的命令会调用Node.js可执行文件，并通过-e参数执行内嵌的代码。内嵌代码由上文提及的script函数生成，执行时会进一步从远程服务器获取加密数据解密后执行。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Ok4fxxCpBb5Lt5avhTNYtdMtNeH8CVtl4HJIC8Oo3ffON2RFPcd9VyykUym9v8LUN2kaibY6KJokFAJ2oXuyciaw/640?wx_fmt=png&from=appmsg)

图11. 解密并执行本地模块

利用工具对该木马的网络通信进行抓包分析，我们对其中一个载荷进行了解密。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Ok4fxxCpBb5Lt5avhTNYtdMtNeH8CVtl9iaWMicFZiawBMfsxaS5xO2jnZiamicMmYPAVLzBNvLKzT2xSbcHfRStzWA/640?wx_fmt=png&from=appmsg)

图12. 对木马传输通信进行抓包

根据抓包数据中捕获到的加密相关密钥及参数，对该载荷中的JavaScript脚本进行解密。我们发现该脚本主要用于窃取虚拟货币钱包，并替换转账钱包地址。此外，该脚本还会创建启动项的PowerShell脚本以实现持久化攻击。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Ok4fxxCpBb5Lt5avhTNYtdMtNeH8CVtl1ecMoF41iadJW7licgkTYoJ37GialNa3msZpianKsOaiaGicMU2ibxicdRUouA/640?wx_fmt=png&from=appmsg)

图13. 从载荷中解密出的JavaScript脚本内容

该脚本中的虚拟币钱包相关的部分内容如下：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Ok4fxxCpBb5Lt5avhTNYtdMtNeH8CVtlsOuahUtVxHoCoo8WAUkrJHsUbGHx8mP0W47nPCrm5KTjibwvkkqodgw/640?wx_fmt=png&from=appmsg)

**03**

**安全提示**

目前监测数据显示，该木马主要在境外传播。但仍需要提醒广大用户——尤其是需要部署或测试DeepSeek的IT从业人员注意外部应用的来源可信度。

除了提高自身安全意识及警惕性外，还建议安装具有足够安全功能的浏览器对访问的页面进行安全性鉴定。同时，安装并启用安全软件，对下载的文件进行安全扫描。以此来确保系统得到全方位的安全防护。

**IOCs**

**SHA1**

c01b0664c7a42b394a465e20b750f61d77fb967e

**URLs**

hxxp://95.179.216.217/5ou0TFIDJzHNchpRhdRV1w%3D%3D

hxxps://calendar.app.google/ff2VfSHoCZWzFD9D8

redis://45.93.20.174:6379

**SIGNATURE**

K.MY TRADING TRANSPORT COMPANY LIMITED

**推荐阅读**

|  |
| --- |
| **01**  ｜[特斯拉充电桩一天被入侵两次](https://mp.weixin.qq.com/s?__biz=MzA5ODA0NDE2MA==&mid=2649787811&idx=1&sn=4927212fd9debdf7d94032ffd45aa0a9&scene=21#wechat_redirect) |
| **02**  ｜[PyPI现DeepSeek恶意软件包](https://mp.weixin.qq.com/s?__biz=MzA5ODA0NDE2MA==&mid=2649787822&idx=1&sn=11f1cb7ddc2d6d5a9478505fff19fb17&scene=21#wechat_redirect) |
| **03**  ｜[Meta因使用盗版数据训练AI面临集体诉讼](https://mp.weixin.qq.com/s?__biz=MzA5ODA0NDE2MA==&mid=2649787829&idx=1&sn=677e98e81db6517c8514fb239ceb0ee3&scene=21#wechat_redirect) |

**安全KER**

安全KER致力于搭建国内安全人才学习、工具、淘金、资讯一体化开放平台，推动数字安全社区文化的普及推广与人才生态的链接融合。目前，安全KER已整合全国数千位白帽资源，联合南京、北京、广州、深圳、长沙、上海、郑州等十余座城市，与ISC、XCon、看雪SDC、Hacking Group等数个中大型品牌达成合作。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Ok4fxxCpBb5Lt5avhTNYtdMtNeH8CVtlAkqDrK3cuwmPCgknzlvKMoDWEeVWD3dFd3JGibjz2SfuBniaWFHhU1nw/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Ok4fxxCpBb5Lt5avhTNYtdMtNeH8CVtlgqClGIicV5yR5UbumjOQCPt45D8tw4w8y2KORibw6R4FbM5vkiaO7ibsVg/640?wx_fmt=png&from=appmsg)

**注册安全KER社区**

**链接最新“圈子”动态**

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/sz_mmbiz_png/Ok4fxxCpBb7PGibphJ1WF3d1yIRaNsuRas4r2SWiaKK9yAoKpicYWBaibyGcHNiaEbrDauSywRrvcn4UFEkZvEo3S6Q/0?wx_fmt=png)

安全客

向上滑动看下一个

知道了

![]()
微信扫一扫
使用小程序

取消
允许

取消
允许

取消
允许

×
分析

![跳转二维码]()

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/Ok4fxxCpBb7PGibphJ1WF3d1yIRaNsuRas4r2SWiaKK9yAoKpicYWBaibyGcHNiaEbrDauSywRrvcn4UFEkZvEo3S6Q/0?wx_fmt=png)

微信扫一扫可打开此内容，
使用完整服务

：
，
，
，
，
，
，
，
，
，
，
，
，
。

视频
小程序
赞
，轻点两下取消赞
在看
，轻点两下取消在看
分享
留言
收藏
听过