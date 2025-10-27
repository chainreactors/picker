---
title: 后门病毒伪装PDF文档，利用钓鱼邮件实现远控
url: https://mp.weixin.qq.com/s?__biz=MzI3NjYzMDM1Mg==&mid=2247519661&idx=1&sn=b8d73bb46b5385a712097813c7384df4&chksm=eb705392dc07da842eac0a6043182ef90d66ae5ad62246409fe10d51b30ec206109218bb88fa&scene=58&subscene=0#rd
source: 火绒安全
date: 2024-08-14
fetch_date: 2025-10-06T18:04:11.893452
---

# 后门病毒伪装PDF文档，利用钓鱼邮件实现远控

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/0icdicRft8tz6RWCaZ7I4bPicen4nYUiaI7e8ibDqYAI4fTGvaklU8tVOe4Qheb6x1mubOpyribUaq7Ch5hkmdzXEmoA/0?wx_fmt=jpeg)

# 后门病毒伪装PDF文档，利用钓鱼邮件实现远控

原创

火绒安全

火绒安全

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/0icdicRft8tz4nrnOI1emtFr0UYnrLKytAvy2gia6ZuIUJs14h2pEIwpiaWPCTTuCQIDibx9dlfXoyrNyVEWb8DVUUA/640?wx_fmt=gif&from=appmsg)

近期，火绒威胁情报中心在日常巡视中发现一恶意 GitHub 存储仓库存在病毒风险行为，火绒安全工程师第一时间提取样本进行分析。分析中发现该样本通过混淆 JavaScript 作为执行体，先下载 PDF 文档用以迷惑用户，接着下载另一个带有成熟后门功能的样本混淆 JavaScript 执行控制功能。结合相关威胁情报和攻击者的 TTP(Tactics, techniques, and procedures)，可以确认利用的是名为 WSHRAT 的成熟 JavaScript 后门，并基于钓鱼邮件进行分发。目前，火绒安全产品可对上述病毒进行拦截查杀，请广大用户及时更新病毒库以提高防御能力。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/0icdicRft8tz6RWCaZ7I4bPicen4nYUiaI7eOsCxY2Y9RBVqElZUFERUzlJUpdgkfIvD1dLv8tZtEicAO2kx7mE90eA/640?wx_fmt=png&from=appmsg)

火绒查杀图

恶意 GitHub 仓库作者信息如下，项目和账号均为近期设立，此外，根据相关威胁情报，还关联到其它同类恶意仓库，这里仅以当前仓库的 Cleodf 项目进行分析展示：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/0icdicRft8tz6RWCaZ7I4bPicen4nYUiaI7e5Pe2ubp8IuURdPWfsexWeZzVf1iauOYADHlKs57VIfiaeUFCDTxsI5JQ/640?wx_fmt=png&from=appmsg)

恶意仓库截图

样本执行流程如下所示：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/0icdicRft8tz6RWCaZ7I4bPicen4nYUiaI7eAISqtrnG3ujcVdAPpiacjp3jJAoK4vNrsJcgGM5T6ibVLuM2sUNK8Mibg/640?wx_fmt=png&from=appmsg)

执行流程图

**一**

**样本分析**

**Tran\_ID-Details009192\_End\_Ids\_58788719853478\_Pdf.js**

该样本一打开就是大型 JavaScript 混淆：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/0icdicRft8tz6RWCaZ7I4bPicen4nYUiaI7eemUibKgAhEjO6J6w9kibsycDj4wJAqrsKyNfmaS4Wosz6yoPxhGBcx6A/640?wx_fmt=png&from=appmsg)

混淆代码示例

简单查看该混淆脚本，可以发现其加密字符串集中来源于 \_0x28502，在需要时逐层解密：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/0icdicRft8tz6RWCaZ7I4bPicen4nYUiaI7eBpCAUSJByGZ7bGiaxQiatPYzKpJibnZKJXBFa4GicaGzj4qP2WQ3tRKsOg/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/0icdicRft8tz6RWCaZ7I4bPicen4nYUiaI7eM9PHmdQWxaRxrUJxLwjAe8pJfZ77mtG1OEaP8giahC7PqHVPdqALTiaA/640?wx_fmt=png&from=appmsg)

部分字符串解密

由于混淆较多，这里直接以动态分析搭配行为监测为主， "Tran\_ID-Details009192\_End\_Ids\_58788719853478\_Pdf.js" 是第一阶段的 downloader，会下载下一阶段用的 JavaScript 文件和一个 PDF 文件并打开用以迷惑用户，安全分析工具监测行为如下：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/0icdicRft8tz6RWCaZ7I4bPicen4nYUiaI7eicia5E8gmpuMZeG68yn7ibxQqR1U6PHibgiasEmu7bibibcu3F9hnhMiaV0FFQ/640?wx_fmt=png&from=appmsg)

安全分析工具行为监测

该 downloader 会解密出域名 "ddfcbb9325637bcdeff.mxttbszhh1.free.hr"，随后拼接路径 "/oauth/pdf/Monetary\_Funding\_Sheet\_2024.js"，通过 GET 请求获取下一阶段 JavaScript 文件，放置在开机启动目录中以执行持久化操作：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/0icdicRft8tz6RWCaZ7I4bPicen4nYUiaI7erAic8IibYDoff233Nttzkm9I8gplhBY5HWVMmoOAgxrVFgFk3JcSTtog/640?wx_fmt=png&from=appmsg)

获取 JavaScript 文件

![](https://mmbiz.qpic.cn/sz_mmbiz_png/0icdicRft8tz6RWCaZ7I4bPicen4nYUiaI7e4bTwJBUfo0gPIlfAnBicicZaZMQh2NxY7FjpO3vLBlJBiciaPxXu5gzvaA/640?wx_fmt=png&from=appmsg)

文件下发展示

接着继续拼接路径 "/oauth/pdf/Monetary\_Funding\_Sheet\_2024.pdf" 下载 PDF 到 "C:\User\Administrator" 目录下，随即打开文档以迷惑受害者，让受害者以为自己打开的是正常的 PDF 加载程序：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/0icdicRft8tz6RWCaZ7I4bPicen4nYUiaI7e25iabFWhmCibMHD4YYHI4X48JibHArribnGybntokQYJlbkZpibmibibacNmQ/640?wx_fmt=png&from=appmsg)

获取 PDF 文件

![](https://mmbiz.qpic.cn/sz_mmbiz_png/0icdicRft8tz6RWCaZ7I4bPicen4nYUiaI7eak5NZv6KnTy93tsqNM7mDIB2IaW8fUKSWicjuoZXdugKJQriaB5mNLPg/640?wx_fmt=png&from=appmsg)

PDF 内容截图

目前该 PDF 链接地址已被标记为钓鱼文档：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/0icdicRft8tz6RWCaZ7I4bPicen4nYUiaI7e4UefPpmmic8KRkbUC4DCV5foM94gVQb3eZBy5QRlzUC0TonibFZuYNaA/640?wx_fmt=png&from=appmsg)

钓鱼文档标记

**Monetary\_Funding\_Sheet\_2024.js**

下载的另一个混淆 JavaScript 名为 "Monetary\_Funding\_Sheet\_2024.js"，这是一个 WSHRAT JavaScript 后门，且与前面用的是同一套混淆方法，部分内容截图如下所示：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/0icdicRft8tz6RWCaZ7I4bPicen4nYUiaI7eXrp40upg8DaVmGTpCNQ5Alox4vELCmIt56WNJo5clgJ6dD4QnQaKog/640?wx_fmt=png&from=appmsg)

混淆代码展示

"Monetary\_Funding\_Sheet\_2024.js" 在执行过程中会链接第一个 url："https://pastie.io/raw/yjuddx"，通过 pastie.io 网址做中转获取真实 C2 IP "45.88.91.57"：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/0icdicRft8tz6RWCaZ7I4bPicen4nYUiaI7ekmSHlZAPdKp5jzX5Lsz3sjrCz7YKUmP0r0UkicLf5zQYkSgUkbcAgvg/640?wx_fmt=png&from=appmsg)

获取 C2 IP

![](https://mmbiz.qpic.cn/sz_mmbiz_png/0icdicRft8tz6RWCaZ7I4bPicen4nYUiaI7eokgYvADboWRHmM7wGicfsxsREicO4bRusE9ajSH29pndptINNwxT24Tw/640?wx_fmt=png&from=appmsg)

网页内容截图

Pastie.io 是一个在线的代码分享工具，类似于 Pastebin 和 GitHub Gists。用户可以在 Pastie.io 上创建代码片段或文本片段，并生成一个唯一的 URL，而在 URL 路径中添加 raw 后会得到只包含文本的页面，没有任何其它杂乱元素，方便分享和访问，这里是被恶意软件作为中转：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/0icdicRft8tz6RWCaZ7I4bPicen4nYUiaI7e5RFRLaPO9PmdEUwVdjTjzUJOO6icpLOKUS0pKj8Ph0761CMWKFicIMHg/640?wx_fmt=png&from=appmsg)

Pastie 网页展示

"Monetary\_Funding\_Sheet\_2024.js" 接着会把自身复制到 AppData\Roaming 目录下：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/0icdicRft8tz6RWCaZ7I4bPicen4nYUiaI7eg3LNzzLgKWXKDITdnMECv40Hr2aIUJuRsZ2vscowW3DIDH9KONg8yw/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/0icdicRft8tz6RWCaZ7I4bPicen4nYUiaI7evTeLeHgYy3whryLD4VnLeJK4cOfeg6bKOQVtPtcDxmdnUhK07uUZxA/640?wx_fmt=png&from=appmsg)

文件复制展示

然后拼接字符串 WScript.exe //B "C:\Users\Administrator\AppData\Roaming\Monetary\_Funding\_Sheet\_2024.js" 写入到注册表 "HKEY\_LOCAL\_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\Run" 中，进行第二个持久化操作。其中 /B 参数将启用 “批处理模式” 并禁用执行期间可能发生的任何潜在警告或警报：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/0icdicRft8tz6RWCaZ7I4bPicen4nYUiaI7eXo7WupCavtmibWxRw14TsyENicm02TfuhskOSMpJpBogWdHvmdutOasg/640?wx_fmt=png&from=appmsg)

写入开机自启动注册表

最后继续用命令 WScript.exe //B "C:\Users\Administrator\AppData\Roaming\Monetary\_Funding\_Sheet\_2024.js" 执行复制的文件，退出当前进程：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/0icdicRft8tz6RWCaZ7I4bPicen4nYUiaI7epVJMWmNMfjLNWJLicicD8EYYQWZzDP51xRu3tiaRV6yPhtokRpHWXe9Ig/640?wx_fmt=png&from=appmsg)

启动子进程

"C:\Users\Administrator\AppData\Roaming\Monetary\_Funding\_Sheet\_2024.js" 被执行后才会进入最后的 while 循环，该循环负责与 C2 IP "45.88.91.57" 的通信操作：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/0icdicRft8tz6RWCaZ7I4bPicen4nYUiaI7ebicUgDFtDwZm06V1mLRTbPlVgQXMqto6GMF7O4yu0KZfqRroBxqZ0DA/640?wx_fmt=png&from=appmsg)

通信循环

其会先解密出请求路径 "/is-ready" 拼接到前面获取的 C2 中，接着把收集到的本地相关信息作为 user-agent 字段数据回传给 C2：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/0icdicRft8tz6RWCaZ7I4bPicen4nYUiaI7etyiaY24tpicjepcyNDVXjQqDia8VPibyJShZMufYEA3G2pVlNI8BQc3X9g/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/0icdicRft8tz6RWCaZ7I4bPicen4nYUiaI7e85kljqznibfGC3pdfZVicLDwaXGBacovfCTXKjbRUemuhyyINwzBrq0w/640?wx_fmt=png&from=appmsg)

构造数据包

![](https://mmbiz.qpic.cn/sz_mmbiz_png/0icdicRft8tz6RWCaZ7I4bPicen4nYUiaI7eW81vVqfdIibI1EWEic03cvF5Aqd1SXriaxdV6r92pL7koFHPrp5oghV9g/640?wx_fmt=png&from=appmsg)

流量包截图

user-agent 字段中包含了 "Monetary\_Funding\_Sheet\_2024.js" 在运行过程中收集的相关信息，整理格式如下：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/0icdicRft8tz6RWCaZ7I4bPicen4nYUiaI7e1o6NSCSI41RMC7fqx1WT6J53eQAUz73Mb0jYLO4px8UALichicAIK4cw/640?wx_fmt=png&from=appmsg)

格式整理

随后根据 C2 回传的指令，在 switch 中进行匹配以执行指定的操作，从而实现远程控制。

"Monetary\_Funding\_Sheet\_2024.js" 涉及的操作指令包括 execute、update、uninstall、send、site-send、recv、enum-driver、enum-faf、enum-process、cmd-shell、delete、exit-process、sleep ：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/0icdicRft8tz6RWCaZ7I4bPicen4nYUiaI7easzZgzg02DonWiakO0UeicjE8ySkGq6Kmbw4qZIdTNbAiaLaDcyZHib5cA/640?wx_fmt=png&from=appmsg)

操作指令匹配

下图是国外研究人员在 Houdini is Back Delivered Through a JavaScript Dropper 捕获到的不带混淆的 Houdini RAT，这是 WSHRAT 的前身，可以看到控制命令基本相同：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/0icdicRft8tz6RWCaZ7I4bPicen4nYUiaI7ejr39diaeiccicwNVRZRrORjaib0D28w8huVXjuWUXF8YWKhTU9aGibdS23g/640?wx_fmt=png&from=appmsg)

Houdini RAT 功能代码

此外，在分析 "Monetary\_Funding\_Sheet\_2024.js" 时根据其 C2 IP "45.88.91.57" 关联到另一篇出自 JAMESWT 写的关于 Twitter 威胁情报，该研究人员列出了其它同源的样本。目前，火绒对这些关联样本均支持查杀：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/0icdicRft8tz6RWCaZ7I4bPicen4nYUiaI7e7ds0qjmpluicQLLQBpVoymSdAqHcwBSPCDicX2tZRhibxaSghd5ftZKLA/640?wx_fmt=png&from=appmsg)

Twitter 情报

**二**

**附录**

**C&C：**

![](https://mmbiz.qpic.cn/sz_mmbiz_png/0icdicRft8tz6RWCaZ7I4bPicen4nYUiaI7edhc7ZSc9VhJJaHiaswVb7zFGhG1LhL2NapgImFpxk6L5daJoxKbh9PA/640?wx_fmt=png&from=appmsg)

**HASH：**

![](https://mmbiz.qpic.cn/sz_mmbiz_png/0icdi...