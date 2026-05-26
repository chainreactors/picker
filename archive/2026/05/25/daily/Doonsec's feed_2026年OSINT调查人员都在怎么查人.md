---
title: 2026年OSINT调查人员都在怎么查人
url: https://mp.weixin.qq.com/s/8yGRKh_a8WxylyZt6Km67g
source: Doonsec's feed
date: 2026-05-25
fetch_date: 2026-05-26T06:04:07.692660
---

# 2026年OSINT调查人员都在怎么查人

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/SmpxklM1IWzc4d0kiaR4tTThOgGUo4ic7eMkIR66mNNabria26JyB8GbwLdngFyRuiapPOcWcod2L4Az1prRr9bciaQLWMWbDickib4pj3jwMuBh38/0?wx_fmt=jpeg)

# 2026年OSINT调查人员都在怎么查人

原创

Owllntel
Owllntel

猫头鹰OSINT

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

在当下的信息环境中，一个人的数字足迹，往往比现实身份更加完整。社交媒体、邮箱、代码仓库、PDF文档、历史网页缓存、论坛留言、Git提交记录……这些看似碎片化的数据，经过关联分析后，往往能够拼出一个极其清晰的人物画像。

以下是一套较为系统的人物开源情报（OSINT）调查方法论，核心目标是通过公开信息、数据关联与行为分析，对目标的数字足迹进行映射与画像。

# 阶段0：调查前先定义目标上下文

真正有效的OSINT调查，并不是一上来就疯狂搜信息。第一步，是明确目标的“上下文”。调查者通常会先思考几个问题：

* 这个人从事什么职业？
* 他生活在哪个国家或地区？
* 兴趣爱好是什么？
* 是否有个人网站？
* 活跃于哪些社交圈？
* 是否属于技术、安全、学术或商业社区？

这些信息决定了后续调查方向。

实战案例：

* 目标：Precious Vincent
* 领域：网络安全 / OSINT / 威胁情报
* 地区：非洲
* 任务：数字足迹分析

有了这些基础画像后，后续搜索就不会陷入无意义的信息泥潭。

# 阶段1：高级谷歌语法

在掌握了目标的姓名和背景后，第一步必然是动用 Google 或 Yandex 的高级搜索语法。交替使用这两个搜索引擎进行数据交叉对比和三角定位至关重要——因为在某一平台上被屏蔽或未收录的数据，往往会完好地呈现在另一个平台上。

通常可直接在这两个引擎中构造如下的高级搜索指令：

```
"Precious Vincent" "cybersecurity" OR "OSINT"
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/SmpxklM1IWzfXCcVadgnGNfFquDn1oE5LbhS04wabic161mKGuY1s0w7SkEiafU0yQ86YTxsfsyDfQUhRIgLg5ibSUkEoSq7BXKrhcGrSO1q9s/640?wx_fmt=png&from=appmsg)

通过此类语法，我们能够将搜索引擎的算力死死锁定在目标身上，瞬间过滤掉互联网上同名同姓的杂音。

紧接着，采取反向检索策略：遍历论坛、视频、新闻、图片中可能存在的姓名标签。同时，务必将检索的时间线往前推，查看目标在往年（甚至更早时期）是否发布过有价值的信息。很多时候，早期的幼稚言论或无意识暴露往往包含了当前已被其刻意清理的绝密线索。

![](https://mmbiz.qpic.cn/mmbiz_png/SmpxklM1IWy1vFyUkcXzkewkmCx2Cq3DUVmaicrdmmjvTOLkGsXHgF1kfsiauAxiarCGwIElsNy7F3kGPH3uyLlv0ic3mbfdrUkBcrnqqPmVG8E/640?wx_fmt=png&from=appmsg)

这一阶段有一个非常关键的原则：数字足迹越大，可收集情报越多。数字足迹越小，越容易进入死胡同。因此，调查过程中必须不断进行数据关联、特征匹配、身份交叉验证。而不是看到一个用户名就直接下结论。

# 利用Sherlock扩充足迹网络

除了传统搜索外，用户名枚举工具也是关键环节。其中比较经典的工具包括WhatsMyName和Sherlock。

Sherlock的核心能力，是对大量网站进行用户名存在性检测。因此可以利用Sherlock枚举目标用户名在全网各大平台的注册情况。当然，自动化工具之后永远需要人工介入分析，以剔除虚警噪声，聚焦于真正有价值的数据收集。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/SmpxklM1IWySSDfyQF6IbnpMkoFTYHorQ8eyUJ866XHcfvfPoAtw2PVmyI2NjICA2TR7dT5I2EblHhR1ZbcYMeYIlqcfibM9odib5GSxJibSj0/640?wx_fmt=png&from=appmsg)

# 阶段2：目标电子邮箱深度挖掘

在很多调查中，邮箱地址才是真正的核心情报节点。因为大量用户会长期复用同一个邮箱。一个邮箱可能关联Facebook、LinkedIn、GitHub、Telegram、Twitter/X、数据泄露记录、公司系统、第三方服务等关键信息。因此，一个邮箱往往就是完整数字身份的聚合器。

如果没有直接找到目标邮箱，调查者通常会使用邮箱排列法。

逻辑是利用名字、姓氏、昵称、用户名、公司域名构造可能的邮箱格式。

例如目标是Precious Vincent：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/SmpxklM1IWy2q3kiauZxf1o1rv26Mf3p1cCncW0ZspuJ1zvibkUIpUVibhnovQw1wCmT0rqOvib3mVqOibb4KStjkcXc2MQKWYonJMo66H5EfR1w/640?wx_fmt=png&from=appmsg)

如果目标属于公司：

precious.vincent@company.com

p.vincent@company.com

如果你不想手工去套用排列模板，完全可以借助AI工具，丢给它目标姓名和公司域名，让它为你批量吐出最符合命名规范的邮箱格式：

常见概率最高的邮箱格式：

1.firstname.lastname@gmail.com

2.firstnamelastname@gmail.com

3.firstinitiallastname@gmail.com（名字首字母+姓氏）

4.firstname.lastname+年份/数字

5.熟知的网络别名/ID的直接复用

# GitHub：很多人的“邮箱泄露中心”

如果常规方法找不到邮箱，GitHub往往是巨大突破口。很多开发者会在Git提交中暴露邮箱。可以手动查，也可以直接调用 GitHub API来实现全自动化、规模化的 Commit 邮箱提炼：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/SmpxklM1IWyhKDh3UIcuBGUD6iaJQicXpHgo0L83jGOPmdmdXt9c2GiaFOBmibhYCgGVKXgia9D1TJH37pwCiaKiaBoe1c1eWiae7Vh628cCELSzgIM/640?wx_fmt=png&from=appmsg)

GitHub API：

```
https://api.github.com/repos/[owner]/[repo]/commits
```

该 API 请求会返回什么？

向该 URL 发送 GET 请求后，GitHub 会返回一个包含 Commit 对象的 JSON 数组。其中包含了无处遁形的数据：

* Git Author 元数据：编写这段代码的人的姓名、提交日期以及其 Git 配置的公开邮箱地址。
* Git Committer 元数据：将这段代码合并应用到仓库中的人的姓名、日期和邮箱。
* GitHub Profile 链接：与该邮箱绑定的 GitHub 账户名及个人主页数据（若该邮箱关联了活跃账户）。
* Commit 详情：唯一的 SHA 哈希值、提交日志信息以及指向具体代码变更的 URL。

为什么它是挖掘邮箱的“外挂”？

* 它提取的是直接嵌入在 Git 配置文件（git config user.email）中的底层邮箱，即使开发者已经在网页前端删除了公开邮箱，这里依然存在。
* 它绕过了源码文件内容本身的限制，哪怕代码里没有写邮箱，底层的提交历史里也洗不掉。
* 你可以用 jq 命令行工具或 Python 脚本轻松解析 JSON 响应，一秒提取出所有独特的 commit.author.email 字段。

一些工具能进一步自动化GitHub情报收集，如Ghintel等。

# 邮箱有效性验证与“找回密码”反查技术

在使用电子邮件地址之前，至关重要的第一步是验证其有效性。验证通过后，可使用“忘记密码”功能来追踪其他社交媒体活动。这种方法对于挖掘更多信息尤为有效。

如果全靠人工手动去各大网站测试“找回密码”，会耗费海量时间。因此，可使用Holehe（通过各平台的“忘记密码”或注册接口，返回该邮箱“是否”在该平台注册了账号）这类工具来实现全自动化测试。

一旦确认该邮箱在某平台已注册，就可以优先在该平台上检索其邮箱前缀或常见的用户名变体（如 vincentprecious 等），从而高概率锁定其真身账号。

假设验证出vincentprecious867@gmail.com真实存在，可以推导其可能复用的用户名变体，例如vincentprecious867、vincentprecious。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/SmpxklM1IWzdznYtQVw9dysIBnt2EOfBjiaQxIWrJROxJ9FaBEPp4icv3ZicicbvgcAs82xmlrP6W5QKnfhR4IwtMtlxH2XvqiajQnwyynGeQsl4/640?wx_fmt=png&from=appmsg)

随后，将这些邮箱或用户名输入到各大平台（如 Facebook、X、LinkedIn）的“忘记密码”界面，利用平台返回的模糊信息（如 a\*\*\*\*\*\*@gmail.com 或 \*\*\*\*\*\*\*\*45）进行二次验证。这种反查技术在身份确认和关系分析中非常高效。

# 阶段 3：高级邮箱情报工具

在现在的开源情报调查中，仅靠搜索引擎已经远远不够。很多调查人员会使用Epieos、Intelbase、BehindTheEmail。这类工具能够提供社交媒体关联、注册平台、活跃时间线、数据泄露记录、用户名、Google个人资料以及评论记录。

其中，Epieos更偏Google生态分析。而Intelbase与 BehindTheEmail往往能提供更完整的邮箱画像。特别是在平台注册记录、泄露数据、历史账户方面，价值很高。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/SmpxklM1IWwEeqjmwQOWnFv7b2C9Jh9H1fCiabe4iaVm5Hd1D60CrxQyCZXtYic5YOA0m68Uia9F2cAluEBHVv1IQYkg8AqAwqjJetCeUSjsLib8/640?wx_fmt=png&from=appmsg)

# 邮箱域名逆向重构

但是，有时候你费尽心思挖到了一个邮箱，扔进工具里一查，却什么有用的情报都没有。

例如你挖到了邮箱precious.vincent@yahoo.com，但是在Holehe、Intelbase、Epieos 中均无结果。

很多调查到这里就结束了。

但真正高级的OSINT会进行“邮箱域重建”。逻辑是：随着时代的变迁，人们会不断更换自己的电子邮箱服务商。十年前用 Yahoo 的人，今天大概率在用 Gmail、Outlook 或 ProtonMail。

最关键的是：人类极度倾向于在不同的域名后，重复使用相同的“本地部分”（Local-part，即 @ 符号前面的那一串用户名）。

既然 precious.vincent@yahoo.com 毫无所获，那就保持前半部分不变，强行重构其域名后缀。

例如将precious.vincent@yahoo.com重建为：

precious.vincent@gmail.com

precious.vincent@outlook.com

precious.vincent@protonmail.com

![](https://mmbiz.qpic.cn/sz_mmbiz_png/SmpxklM1IWzVoOYGUqJibfia4uLRdTRDcqBkF7xPDUNw2aYrq9WziaccBnDBV85ZgW12RQhsYLPFfsicgXgLaAmW9rDj46kWCpLSiaE4xUtW2sFU/640?wx_fmt=png&from=appmsg)

再重新执行社交媒体搜索、忘记密码、数据泄露检测、平台关联分析。

如果目标人员对邮箱前半部分也做了微调，可同步测试以下变体：

* 缩写变形：precious.vincent $\rightarrow$ pvincent $\rightarrow$ pvince $\rightarrow$ vincentp
* 点号的有无：precious.vincent@gmail.com vs preciousvincent@gmail.com
* 数字的塞入或剔除：pvincent867@yahoo.com $\rightarrow$ pvincent@outlook.com

这种方法经常能从“死数据”中重新找到突破口。

# 头像反向搜索

下一步，对上述步骤中扒出来的目标头像进行反向图片检索。人们往往会在不同平台上长期复用同一张自己满意的相片（或裁剪版）。通过人脸/图片特征的交叉比对，能轻松帮我们把各孤立平台的账号串联到一起。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/SmpxklM1IWwpia1o94ibXtOboibetW8oEuV5A8T0pLH2cWrpakOXcq08CibibXUILxuqWklcGJWJDKUexQZRfqZlzH53o7fjLFg9szR7wG9DLp1A/640?wx_fmt=png&from=appmsg)

可使用Google Lens、Yandex Images、TinEye等工具。

很多匿名用户，最终就是因为头像复用被串联起来。

# 阶段4：Wayback Machine

人类会随着时间的推移刻意清洗、重塑自己的网络形象，但是互联网从来没有真正遗忘过任何事。

将调查中收集到的所有 URL（哪怕已经 404 或者是已被清空的 GitHub 仓库、死掉的旧博客、注销的 LinkedIn 档案、多年前的论坛水贴）统统喂进 Wayback Machine (archive.org)。

核心搜寻目标包括：

* 已被主人亲手抹去的早期非主流社交主页（MySpace、早期的 Tumblr、Reddit 老帖）
* 目标多年前撰写的个人简报或作品集（里面往往记录了其当时的物理位置、第一份工作或青涩的个人兴趣）
* 其政治立场、意识形态随时间推移发生的剧烈转变轨迹
* 被废弃但依旧在底层静静躺着元数据（Metadata）的网络曾用名/马甲

例如，实战检索中，发现目标在多年前曾拥有一个WordPress博客（如 preciousvincent.wordpress.com），虽然现在访问什么都没了，但把它扔进网页时光机，疯狂翻阅从十几年前至今的快照历史。

在这里经常能意外斩获其多年前无意间敲下的亲人真实姓名、早期的职场履历、甚至当年在线下某咖啡馆物理打卡的签到记录。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/SmpxklM1IWyDYYvLGLFIokscocV6qpUmj27r1ibzpv2jicmlDfBzTicoI3Nh0buBwjEvYeaQdFCyavCDUIibAJkbkjAU68eEscEzqgt67Zg93Ss/640?wx_fmt=png&from=appmsg)

一些辅助工具：

* Archive.today：专治各种不服，能强行绕过一部分反爬及 robots.txt 协议的屏蔽限制。
* Lumen Database：专门去检索该 URL 是否涉及历史版权或敏感内容下架请求，从而顺藤摸瓜找到删除者的身份。

# 阶段5：目标PDF文档深度剖析

很多调查人员会忽略PDF。但实际上PDF往往是最容易泄露元数据的载体之一。包括：简历、白皮书、PPT、学术论文、合同、演讲稿都可能泄露大量信息。

# 查找目标文件

第一步，利用高级语法定向把目标散落在互联网各个角落的文档全部挖掘出来。

针对文档的 Google Dorking 语法：

```
关键词 filetype:扩展名"Precious Vincent" filetype:pdf"Precious Vincent" filetype:doc OR filetype:docx"Precious Vincent" filetype:ppt OR filetype:pptx"Precious Vincent" filetype:xls OR filetype:xlsx"vincentprecious" filetype:pdf
```

高级检索语法支持极限自定义。通过精细化调整 filetype: 检索范围，可将搜索范围缩小到目标人物的职业生活：

![](https://mmbiz.qpic.cn/mmbiz_png/SmpxklM1IWw3yE9DTrswH4PTxtvqPkYXDl7ice9v4zwibdtZxMsU5EmZTxIfBxj9U69t0G0wNgzuoTH1tXxjsQhkGcpq72icoBsKUISZT1JcO0/640?wx_fmt=png&from=appmsg)

通过这些被其随手上传的文档，就能顺藤摸瓜剥离出：目标工作生活足迹 > 经理姓名 > 个人/工作邮箱地址 > 电话号码 > 实际地址/位置 > 内部住宿登记数据

# 获取文档的替代搜索引擎与垂直渠道：

* Yandex / Bing：经常能捞到被谷歌出于隐私保护机制隐去的“漏网之鱼”文档。
* PDF Search Engine (pdf-downloads.net)：专门针对 PDF 的垂直搜索引擎。
* Google Scholar（谷歌学术）：专门针对具有学术、科研背景的目标。
* GitHub 仓库检索：使用指令 extension:pdf "目标姓名"，直接洗劫上传在代码仓库里的文档。
* 垂直共享平台：ResearchGate、Academia.edu（学术圈）、SlideShare（行业会议 PPT 圣地）、Scribd、DocDroid。

# 从每个文档中提取4维核心情报

## A. 嵌入式元数据

使用 ExifTool（命令行）或 Metadata2Go 等图形界面工具处理每个文档。

要找的是：

* 作者姓名（可能透露曾用名或别名）
* 公司或组织（现任或前任雇主）
* 软件版本（Microsoft Word 2016 与 ...