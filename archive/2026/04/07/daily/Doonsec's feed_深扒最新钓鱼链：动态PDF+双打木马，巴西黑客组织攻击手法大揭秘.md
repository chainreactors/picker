---
title: 深扒最新钓鱼链：动态PDF+双打木马，巴西黑客组织攻击手法大揭秘
url: https://mp.weixin.qq.com/s/Z6SQPK5pbGB-EneA-sg9Ig
source: Doonsec's feed
date: 2026-04-07
fetch_date: 2026-04-08T04:35:22.378617
---

# 深扒最新钓鱼链：动态PDF+双打木马，巴西黑客组织攻击手法大揭秘

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/bHeteOibsicdhc1rrla8c6R7ibHwiamCf2ZNMToS1TATYxK4shExbrZjHkU9rdPepVQEYIMnO4ibXjh7esnp3lSDB9hMicXJSdCicvbibVVG8EhYfKU/0?wx_fmt=jpeg)

# 深扒最新钓鱼链：动态PDF+双打木马，巴西黑客组织攻击手法大揭秘

原创

Kit Chung
Kit Chung

安全圈动向

![]()

在小说阅读器中沉浸阅读

![](https://mmbiz.qpic.cn/mmbiz_png/bHeteOibsicdgGPQ4O3Ft5SYSOA8icb6IeIBahAeC0yMjEEUzhJYlj9pqOCTpvia7ERXN2dVcrJZX7j8ynOa1FMenVuicrt4LEibic4QZPFckDsmyw/640?wx_fmt=png&from=appmsg)

哈喽，大家好！最近在跟进最新威胁情报时，我捕获到了一个非常有意思、且技术手段相当“卷”的钓鱼攻击链路。

不知道大家平时在做安全攻防或者逆向分析时有没有发现，现在的黑产组织早就脱离了单纯“扔个木马看天意”的阶段。今天咱们要聊的这个来自巴西的黑客组织（业内追踪代号为 **Augmented Marauder** 或 **Water Saci**），直接把自动化、多态免杀和社工套路玩出了花。

他们针对拉美和欧洲企业发起了一波猛烈攻击，核心载荷是我们熟悉的 **Casbaneiro（又名 Metamorfo）银行木马**，但真正让我眼前一亮的，是它背后用来做横向传播的 **Horabot** 引擎。

今天，我就带大家硬核拆解一下这条攻击链的底层逻辑，看看这帮黑客是如何一步步绕过现代安全防御体系的。各位师傅，系好安全带，咱们发车！

### 🎣 第一层套路：带密码的“法庭传票”与初始突破

这次攻击的初始入口依然是我们熟悉的**钓鱼邮件**，但他们很懂得拿捏人性，用了“西班牙法庭传票”作为诱饵主题。

当你点开邮件，会看到一个带密码保护的PDF附件。这里就是一个典型的**反沙箱技巧**：带密码的PDF可以有效阻挡大部分传统邮件安全网关的自动化静态扫描。

> **技术重现点：**
> 用户输入密码打开PDF后，里面并没有直接嵌入恶意代码（规避PDF解析漏洞查杀），而是内嵌了一个恶意链接。用户一旦点击，就会自动下载一个ZIP压缩包。这个ZIP解压后，真正的“前菜”——**HTA（HTML Application）和 VBS 脚本**才会落地执行。

### 🛡️ 第二层对抗：VBS环境检测与AutoIt加载器

进入到脚本执行阶段，这帮黑客的防御意识极其强烈。

落地的 VBS 脚本并没有急于下载核心木马，而是先进行了一系列**环境与反分析检测**。这和早期 Horabot 变种的特征高度一致。比如，它会遍历系统进程和注册表，专门去检测宿主机上有没有安装 **Avast 等主流杀毒软件**。一旦嗅到虚拟机或分析环境的味道，直接静默退出。

确认环境安全后，VBS 脚本才会向远程 C2 服务器发起请求，拉取下一阶段的 Payload。

**敲黑板！这里的加载机制非常经典：**
他们下发的是基于 **AutoIt** 编写的加载器。AutoIt 因为其合法性和灵活性，一直是黑灰产用来做“白加黑”或规避检测的利器。这些加载器会在内存中解密并运行后缀名为 `.ia` 或 `.at` 的加密载荷文件，最终释放出真正的恶魔：

* `staticdata.dll`

  —— **Casbaneiro 银行木马**（主攻核心资产）
* `at.dll`

  —— **Horabot 传播组件**（主攻横向感染）

### 🧠 核心技术解析：Horabot 的“动态 PDF”生成术

Casbaneiro 窃取金融数据咱们就不多说了（常规的 Delphi DLL 模块），今天重点要扒的是 **Horabot 这个传播引擎**。这也是整篇文章中最具技术含量的部分。

以前的木马怎么传播？要么本地写死一个恶意附件，要么挂一个固定的下载链接，遍历通讯录群发。这种静态特征分分钟被安全设备的 Hash 黑名单秒杀。

**但 Horabot 是怎么干的？他们实现了 Payload 的“动态按需生成”。**

具体执行路径如下：

1. Casbaneiro 的 Delphi 模块会联系 C2 服务器，拉取一段 **PowerShell 脚本**。
2. 这个 PS 脚本就是 Horabot 的核心调度器。它会去抓取被感染用户 Microsoft Outlook 里的联系人列表。
3. **高能预警：**

   脚本会向远端的一个 PHP API（例如：`hxxps://tt.grupobedfs[.]com/.../gera_pdf.php`）发起 **HTTP POST 请求**，并在请求中携带一个随机生成的4位 PIN 码。
4. C2 服务器接收到请求后，会**动态渲染并伪造**一份全新的、带有密码保护（密码就是那个随机 PIN 码）的“法庭传票” PDF 文件，并返回给受害者机器。
5. 最后，脚本利用受害者本人的合法邮箱账号，将这份独一无二的 PDF 作为附件，精准发送给通讯录里的联系人。

配合另一个关联的 DLL 组件（`at.dll`），Horabot 甚至能劫持 Yahoo、Live 和 Gmail 账户，通过 Outlook 接口无缝发送垃圾邮件。

> **💡 思考：** 这种每次请求都动态生成独立 PDF、且携带随机密码的机制，让每一个诱饵的 Hash 值都完全不同（**多态性**），极大地增加了安全分析师提取静态特征的难度。利用合法的受害者账号发送，也完美绕过了 SPF/DKIM 等邮件防伪造协议。

### 🔄 攻击手法的降维打击：ClickFix 与 WhatsApp 自动化

除了邮件这条线，Water Saci 组织在多渠道武器化部署上也表现出了惊人的敏捷性。

根据近期的威胁情报交叉比对，这帮人还在并行使用以下攻击手段：

* **WhatsApp Web 自动化传播：**

  像蠕虫一样，利用网页版 WhatsApp 接口自动给好友发送包含 Casbaneiro 或 Maverick 木马的恶意链接。
* **ClickFix 社工技术：**

  这是一种新兴的浏览器级诱导技术。他们会伪造虚假的浏览器报错或系统更新提示，诱导用户通过复制粘贴运行恶意 PowerShell 或 HTA 脚本，最终部署 Casbaneiro 和 Horabot。

### 总结与防护建议

纵观整个攻击链路，我们能看到 Water Saci 组织展现出了极强的**架构解耦与动态演进能力**。他们维持着一个多管齐下的庞大攻击基础设施：一边用 ClickFix 和 WhatsApp 自动化主攻普通消费者；另一边利用 Horabot 的邮件劫持和动态 PDF 生成引擎，疯狂撕裂企业内网的边界。

对于我们安全从业者（特别是负责企业邮件网关和终端安全响应的同学）来说，面对这种级别的对手，传统的静态特征匹配已经捉襟见肘。

**我们在防御策略上需要重点关注：**

1. **行为监控（EDR）：**

   加强对 Outlook/邮件客户端调用 PowerShell、VBS 或发起异常 HTTP POST 请求的行为审计。
2. **脚本与加载器拦截：**

   重点监控 AutoIt、HTA 脚本的无文件执行行为，限制非常规后缀文件（如 `.ia`, `.at`）在内存中的解密动作。
3. **零信任理念：**

   哪怕是内部可信邮箱发来的带密码附件，也要引导员工进行二次核实。

技术的对抗永远是道高一尺，魔高一丈。了解对手的底牌，咱们才能在攻防演练中立于不败之地。

如果你对这次的恶意样本分析感兴趣，或者在企业安全建设中遇到过类似的头疼问题，欢迎在评论区留言，咱们一起探讨交流！觉得文章有硬货，别忘了点个**在看**和**转发**，支持一下！

#网络安全 #威胁情报 #钓鱼攻击 #Casbaneiro #Horabot #银行木马 #逆向分析 #ClickFix #AutoIt #企业安全防护

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/cGfIHiaxhOAibibTsJVcHDbhtFv0ag2IA9b81ZpnotG5eND55SagiagYFdpes4L0YOekWuhScYdKGVGky9M9m9qP4g/0?wx_fmt=png)

安全圈动向

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/cGfIHiaxhOAibibTsJVcHDbhtFv0ag2IA9b81ZpnotG5eND55SagiagYFdpes4L0YOekWuhScYdKGVGky9M9m9qP4g/0?wx_fmt=png)

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