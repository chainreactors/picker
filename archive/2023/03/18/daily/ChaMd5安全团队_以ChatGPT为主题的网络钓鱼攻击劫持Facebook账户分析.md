---
title: 以ChatGPT为主题的网络钓鱼攻击劫持Facebook账户分析
url: https://mp.weixin.qq.com/s?__biz=MzIzMTc1MjExOQ==&mid=2247508388&idx=1&sn=5c2b3b25d6fea561e21849fb77446bf5&chksm=e89d897cdfea006a9b034479ff90b572c3307f72deec9e6806fa7f32487fbcc5510037f70002&scene=58&subscene=0#rd
source: ChaMd5安全团队
date: 2023-03-18
fetch_date: 2025-10-04T09:58:16.888295
---

# 以ChatGPT为主题的网络钓鱼攻击劫持Facebook账户分析

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/PUubqXlrzBQgRo9Z6ytnQEa8ODISwEOayDYKM2DABrl5jeKcNu2xv6FFYdMwvibChVfjOz0ONyicQZ9LhPc1W0kA/0?wx_fmt=jpeg)

# 以ChatGPT为主题的网络钓鱼攻击劫持Facebook账户分析

原创

gongyouxiu

ChaMd5安全团队

# 概述:

ChatGPT模型是自然语言处理领域的一个热门话题,近期,随着ChatGPT出圈,它越来越受到人们的关注和追捧。许多人想要亲身体验ChatGPT所带来的强大功能和优势,这也吸引了一些黑客利用网络钓鱼攻击手段来窃取用户的Facebook账户信息,从而实施恶意行为,例如发布虚假信息、发送欺诈邮件或劫持账户等。网络钓鱼是一种常见的攻击手段,它通过伪造合法的网站或应用程序,欺骗用户输入其账户名和密码或是下载恶意程序,从而达到窃取账户信息的目的。

Facebook上存在着模仿Chatgpt官方账号的虚假钓鱼账号,根据发布的帖子来看本次行动最早可以追溯到`2022.5.10`![](https://mmbiz.qpic.cn/mmbiz_png/PUubqXlrzBQgRo9Z6ytnQEa8ODISwEOaFicZrRkHzGFaPwW3zq2L1kickKtdjjAoJ2ZUrZKHQVuQHdsOiam6ialBdA/640?wx_fmt=png)![](https://mmbiz.qpic.cn/mmbiz_png/PUubqXlrzBQgRo9Z6ytnQEa8ODISwEOayqRPFkLUz4rJ7MD24lCaG4yz1ZGNd71a3rjUeTq6QTricnWtbtdYcVw/640?wx_fmt=png)该账号不断发布帖子诱导用户点击克隆的 "官方" 网址下载 "ChatGPT客户端"![](https://mmbiz.qpic.cn/mmbiz_png/PUubqXlrzBQgRo9Z6ytnQEa8ODISwEOa2zjNpIgJ6lELODCoMJFMdgMOR26c2ibEHic1sjVgTibLPwdJcVQlqic7gA/640?wx_fmt=png)钓鱼页面均为克隆原openai官网,并将原本的跳转网页按钮改成了下载应用程序![](https://mmbiz.qpic.cn/mmbiz_png/PUubqXlrzBQgRo9Z6ytnQEa8ODISwEOaSUyUiaia0VhMibUGVQQlEQMeLWCB0TRrTOvo09okEZV0CMOAjvrmmQqew/640?wx_fmt=png)可以根据钓鱼账号历史发布的帖子收集到几个钓鱼域名

| https://openai-pc-pro.online |
| --- |
| https://chat-gpt-pc.online |
| https://chatgpt-go.online |
| http://chatgpt-go.online |
| https://gptopenai.chat |

# 样本分析:

通过网页下载的恶意程序整体比较大,目前捕获到的几个样本大小均在50M以上,并且该样本加载的方式比较少见,虽然属于是`.exe`可执行文件,实际上是使用到pkg工具将node.js以及运行环境和恶意js脚本打包成应用程序来执行恶意功能,常见情况下js相关病毒样本都是通过windows自带脚本解释器`**wscript.exe**`去执行的,故对其执行流程做详细分析

## pkg打包node.js项目原理:

篇幅有限,简要介绍 Node.js是能够在服务器端运行 JavaScript 的代码和实现跨平台执行的环境,易于移植,基于Chrome V8引擎 而pkg可以将 Node.js项目打包到可执行文件中,使得可执行文件可以在未安装 Node.js 的设备上运行,能够生成Linux , macOS和Windows的程序 在程序运行时,首先会在临时目录下创建一个pkg目录,并在其中解压缩可执行文件中的环境文件,然后它会使用解压后的 Node.exe文件来执行程序打包的js代码,并且pkg默认不会直接存储 JavaScript源文件,而是通过 V8编译器 编译JavaScript 生成bytecode存储V8快照,也就是v8 bytecode

### 打包后程序的文件结构:

pkg版本: 5.8.0 node版本: 18.14.2![](https://mmbiz.qpic.cn/mmbiz_png/PUubqXlrzBQgRo9Z6ytnQEa8ODISwEOaVTC3rJyuicET3MqVAGpG7pPpgvn77TZtATMakia89zPsp3nu05Us27OQ/640?wx_fmt=png)

#### Node.exe结构中:

通过解析当前环境的测试文件发现node.exe这部分结构的总大小为35.8 MB,这也是所有打包程序体积都比较大的原因 且node文件中包含着一段关键结构`"internal/bootstrap/**pkg.js**"`该结构代码会定义程序中的虚拟文件系统和prelude.js的起始地址和大小

#### 虚拟文件系统:

里面存放了 js 代码和相关的资源文件,pkg打包默认是将源代码编译成v8 bytecode

#### prelude.js

每个生成的 prelude.js 文件基本相同,因为它是从 pkg 工具的代码库中提取的标准文件,而不是在应用程序的打包过程中根据应用程序的特定需求生成的,prelude.js 文件包含了启动 Node.js 环境所需的代码 并且在文件末尾,固定的注释`"//# sourceMappingURL=common.js.map"`后会写入打包的`文件名`,`路径`,`偏移量`,`长度`项目结构的json对象,对应着执行的文件在虚拟文件系统中的偏移量![](https://mmbiz.qpic.cn/mmbiz_png/PUubqXlrzBQgRo9Z6ytnQEa8ODISwEOaXCTLSU0p2NUGH9jttfJNibHLGJCeyZ2jApf9MicjPtH2HjGOQo1hC5vQ/640?wx_fmt=png)

可以根据末尾的prelude.js和json对象去解析文件将脚本还原,也可以利用github现有的工具进行还原https://github.com/LockBlock-dev/pkg-unpacker

## package.json文件信息

`package.json`结构中一般会包含许多元信息,比如攻击者设备安装的node环境的版本,项目名称,项目版本等 攻击者将其命名为bot0-1![](https://mmbiz.qpic.cn/mmbiz_png/PUubqXlrzBQgRo9Z6ytnQEa8ODISwEOaoBgRpv9DESUPOpow7EmL462lg4C5GGO9YY2Qoto2mPdQFu9LVP3kzA/640?wx_fmt=png)

## 恶意js分析

pkg打包程序默认会将源js文件编译成字节码,但是通过解包发现该样本的js文件未被编译 从执行的js代码固定格式可以很明显看出代码经过Obfuscator混淆,常规操作是转成AST还原代码,github也有相关项目![](https://mmbiz.qpic.cn/mmbiz_png/PUubqXlrzBQgRo9Z6ytnQEa8ODISwEOaHmOQIK0XOcz2lib3VckBNIXLzoGvd4AOnQvMxKAm8dTiaiacibxmHEWynA/640?wx_fmt=png)

分析发现该脚本的主要功能是窃取用户在 Chrome、OperaGX、OperaDefault、MicrosoftEdge 和 Brave 等浏览器中存储的 Cookies 和账号密码。然而,与其他常见的窃密程序不同的是,这个样本只针对三个平台：Google、Outlook 和 Facebook。![](https://mmbiz.qpic.cn/mmbiz_png/PUubqXlrzBQgRo9Z6ytnQEa8ODISwEOaMbCAvwVMgoxk3D3R3Ah84nJAMdcNFp670BCbYsw5ibmwAuc2icHDqPnA/640?wx_fmt=png)![](https://mmbiz.qpic.cn/mmbiz_png/PUubqXlrzBQgRo9Z6ytnQEa8ODISwEOaqs46btJV4ug5XWppglF2BkJey1PVXWNBwa8UU9tcUoHamAibsmvORicw/640?wx_fmt=png)

### 信息发送:

整个信息发送出去的体系比较完善,发送信息的途径分为两种:

1. 直接将数据回传给c2`https://cloudimagesv.top/avata2`

![](https://mmbiz.qpic.cn/mmbiz_png/PUubqXlrzBQgRo9Z6ytnQEa8ODISwEOalE40XjQMWMFKViaWtZuFL9EClJLkdsvmXhaRt9SsPbv8Ytw6CfRglRg/640?wx_fmt=png)

image.png

2. 直接通过telegram api发送出去,并且使用了两个bot

![](https://mmbiz.qpic.cn/mmbiz_png/PUubqXlrzBQgRo9Z6ytnQEa8ODISwEOaiaDYGKsr1FLvqUicMHIH1C1c84wsZYSMPSIzq4x1KQ6rkoNt5R81h8MA/640?wx_fmt=png)![](https://mmbiz.qpic.cn/mmbiz_png/PUubqXlrzBQgRo9Z6ytnQEa8ODISwEOaAGR6APzSmEKjEW0GtDpE3ibRG7dXxanm0qa98kF3OjBfq1aUCncHybg/640?wx_fmt=png)并且窃取的信息都严格进行格式化处理,同样分为两种方式:

1. 将收集到的重要信息按照人物基本画像后,将其json格式化后发送

![](https://mmbiz.qpic.cn/mmbiz_png/PUubqXlrzBQgRo9Z6ytnQEa8ODISwEOaAiasMMM3aQzZBI1zxaxTwIKMiaia5RCuvxY91Qc6ssnPEQ8n97ePPTkDQ/640?wx_fmt=png)

image.png

2. 将窃取到的cookie,账号密码打包成zip后发送出去

![](https://mmbiz.qpic.cn/mmbiz_png/PUubqXlrzBQgRo9Z6ytnQEa8ODISwEOaUHHjQkI86dO94ziaNwZtCx5Vib037FL3IS0Cx4GOhic4PcYVSPstSLWOw/640?wx_fmt=png)

image.png

### fackbook广告业务劫持:

样本特殊的地方在于大量关于fackbook商业用户的信息窃取,首先是通过访问facebook广告管理平台`"https://www.facebook.com/ads/adbuilder"`获取响应，截取以下信息:

| 字段 | 作用 |
| --- | --- |
| accessToken | 用于访问 Facebook 平台 API 的凭证 |
| DTSGInitialData Token | 验证用户身份和保护用户信息安全的令牌 |
| \_\_spin\_r | 表示一个随机字符串，用于生成动态 JavaScript 代码中的 \_r 参数 |
| \_\_spin\_t | 表示一个时间戳，用于生成动态 JavaScript 代码中的 \_t 参数 |
| \_\_spin\_b | 表示一个布尔值，用于生成动态 JavaScript 代码中的 \_b 参数 |
| fbid | Facebook 中表示用户或页面的唯一标识符 |
| userFullName | 用户在 Facebook 上的全名，包括名字和姓氏 |

然后利用获取到的凭证在`https://graph.facebook.com`,也就是Facebook Graph API 上多次检索关于用户的更多信息,例如`id,name,email,birthday,location,fan_count`等字段 还会进一步通过以下接口去获取到更多关于用户的广告业务信息![](https://mmbiz.qpic.cn/mmbiz_png/PUubqXlrzBQgRo9Z6ytnQEa8ODISwEOay6FanDia1yxciaxKj7U8DI1KhDHE89AAPxRP7Lhibgl3WrxgHlziceiafTg/640?wx_fmt=png)窃取的部分信息![](https://mmbiz.qpic.cn/mmbiz_png/PUubqXlrzBQgRo9Z6ytnQEa8ODISwEOavM1jMw5mYKTZzBSB23ibYibwpbOedLEyvycWznOYJz7T8WYfHew2ltFQ/640?wx_fmt=png)

| **属性名称** | **对应的值** |
| --- | --- |
| id | 广告账户 ID |
| adminAn | 管理员数量 |
| ten | 广告账户名称 |
| gioiHanChiTieu | 广告账户的预算限制 |
| loaiTaiKhoan | 广告账户的类型 |
| radioToUsd | 货币汇率，换算成美元 |
| muiGio | 时区 |
| currency | 币种 |
| ngayLapHoaDon | 下次账单日期 |
| ngayTao | 账户创建时间 |
| nguongHienTai | 当前阈值 |
| soDu | 广告账户余额 |
| theThanhToan | 支付卡信息 |
| ngayHetHan | 卡的过期日期 |
| trangThaiThe | 卡的状态 |
| tongChiTieu | 广告账户总花费 |
| trangThai | 广告账户状态，1 表示正常，3 表示被禁用，其他数字表示其他状态。 |
| name | 商业账户名称 |
| permitted\_roles | 允许的角色列表，指明该商业账户可以被哪些角色访问 |
| is\_disabled\_for\_integrity\_reasons | 商业账户是否因不良行为而被禁用 |
| business\_invoices | 商业账户发票信息 |
| created\_time | 商业账户创建时间 |
| verification\_status | 商业账户验证状态 |
| owned\_ad\_accounts | 商业账户所拥有的广告账户信息，包括账户 ID、名称、账户状态、账户余额等 |

后续也可能会访问和操作平台上的数据和资源,以达到更多经济利益的目的,例如

* 发布和编辑用户或页面的帖子、评论等内容
* 创建和管理广告、应用程序等资源
* ...

# 关联分析:

从使用到的变量名和代码中的输出调试语句可以初步判断攻击者为越南语使用者![](https://mmbiz.qpic.cn/mmbiz_png/PUubqXlrzBQgRo9Z6ytnQEa8ODISwEOajg4sFNO2ibsUic5ib8wokH9SRAibyg5spejgcMc483XLP3ZFvYbUn5iaAxw/640?wx_fmt=png)该次行动开始活跃时间`2022.5.10`恰好也和已披露的DUCKTAIL组织活跃时间重合,并且是以经济利益为目的信息窃取和 Facebook 业务劫持,根据样本的特征,可以将此次行动归因于越南组织DUCKTAIL,该组织从2021年开始活跃,其最初目标就是劫持Facebook 商业帐户,并且攻击者会将自己的电子邮件地址添加到被劫持的企业帐户下,以此来冒充受害者,该组织最初使用的恶意软件样本是用 .NET编写的,后续其攻击手法不断在提升,通过各种方式去部署恶意程序

# 总结:

近期以ChatGPT为主题的钓鱼事件非常多,对于该样本,本人目前没有再进一步去溯源相关攻击链,但是在分析样本的时候发现代码中存在判断系统类型和型号的操作,再加上攻击组织选择使用`.NET`,`js`去开发恶意程序,可能通过重新定位代码库或通过网络钓鱼等其他攻击媒介,DUCKTAIL大概率还存在其他跨操作系统平台的攻击(Android,iOS,MacOS)

end

招新小广告

ChaMd5 Venom 招收大佬入圈

新成立组IOT+工控+样本分析 长期招新

欢迎联系admin@chamd5.org

![](https://mmbiz.qpic.cn/mmbiz_png/PUubqXlrzBR8nk7RR7HefBINILy4PClwoEMzGCJovye9KIsEjCKwxlqcSFsGJSv3OtYIjmKpXzVyfzlqSicWwxQ/640?wx_fmt=jpeg&wxfrom=5&wx_lazy=1&wx_co=1)

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/PUubqXlrzBRyftF8Oqhh2V8ib6wEgOiaCMdKBLfkLlHAvKibMgjerLzeXXxRmyI9VpjX7e37vjeW2scODia9KHGoqQ/0?wx_fmt=png)

ChaMd5安全团队

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/PUubqXlrzBRyftF8Oqhh2V8ib6wEgOiaCMdKBLfkLlHAvKibMgjerLzeXXxRmyI9VpjX7e37vjeW2scODia9KHGoqQ/0?wx_fmt=png)

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