---
title: ClickFix 无文件方式新一轮攻击 Windows 系统从而部署 StealC 窃取程序
url: https://mp.weixin.qq.com/s/DQyBh-eYmLJImVXV451CVg
source: Doonsec's feed
date: 2026-02-14
fetch_date: 2026-02-15T04:25:01.775975
---

# ClickFix 无文件方式新一轮攻击 Windows 系统从而部署 StealC 窃取程序

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/zdwoicOrrJb0cTmWI5aibibhQvDAzSJ8wR4Gw516cO2wAicJsHKTQd0C6T9icJTsgZVVrM7zbj2ClJW0d8mlYAibUIkWs0RlHvPmZbnAIX6APxrkQ/0?wx_fmt=jpeg)

# ClickFix 无文件方式新一轮攻击 Windows 系统从而部署 StealC 窃取程序

原创

ZM
ZM

暗镜

![]()

在小说阅读器中沉浸阅读

一场精心策划的社会工程攻击活动正通过虚假的 CAPTCHA 验证页面，以 Windows 用户为目标，传播 StealC 信息窃取恶意软件。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/zdwoicOrrJb1ia4npFvLvGAgwYfSP1DbMia7aBdJ6lepgO7P3icJ9p7mJrqCaPiaIO2DEEHcztVMlE2IccdGriaiclUicrdibGiabEntCWESFkVqiarmG0/640?wx_fmt=png&from=appmsg)

攻击始于受害者访问被入侵的网站，这些网站会显示欺诈性的 Cloudflare 安全检查，诱骗他们执行恶意PowerShell 命令。

此次网络犯罪活动代表了网络犯罪策略的危险演变，它将心理操纵与先进的技术规避方法相结合，以窃取敏感数据。

攻击始于看似合法的网站，这些网站已被恶意攻击者入侵。当用户访问这些网站时，恶意 JavaScript 会加载一个伪造的验证码页面，该页面模仿 Cloudflare 的验证系统。

该页面指示受害者按下 Windows 键 + R，然后按 Ctrl + V 粘贴隐藏命令，最后按 Enter 键执行。ClickFix 的这种技术利用了用户的信任，让受害者误以为自己在进行例行安全检查，而实际上却是在启动恶意软件。

LevelBlue 的研究人员发现了这种多阶段攻击链，该攻击链下载位置无关 shellcode，反射加载 64 位 PE 下载器，最后将 StealC 恶意软件注入到合法的 Windows 进程中。

该窃取程序的目标是 Chrome、Edge、Firefox 和其他浏览器的浏览器凭据、包括 MetaMask 和 Coinbase Wallet 在内的加密货币钱包扩展程序、Steam 帐户身份验证文件、Outlook 电子邮件凭据以及带有屏幕截图的系统信息。

该恶意软件采用无文件执行技术，完全在内存中运行，无需将文件写入磁盘，因此极难检测。

初始 PowerShell 命令执行完毕后，它会连接到远程服务器，下载使用 Donut 框架生成的 shellcode。

然后，该 shellcode 加载一个用 Microsoft Visual C++ 编译的自定义 PE 下载器，该下载器检索最终的 StealC 有效载荷并将其注入到 svchost.exe（一个合法的 Windows 服务进程）中。

StealC 使用 Base64 和 RC4 编码加密的 HTTP 流量与其命令和控制服务器通信。

该恶意软件使用双层字符串混淆技术来隐藏关键配置数据，包括 C2 服务器 URL、目标文件路径和数据库查询。

组织应监控可疑的 User-Agent 字符串（例如“Loader”），标记使用编码命令执行的 PowerShell，检测指示shellcode 注入的VirtualAlloc 和 CreateThread 模式，并对异常访问浏览器凭据数据库发出警报。

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/mibm5daOCSt98X08oaiaa3t79eUW2Q5RyicXA1ebXOdyVvQ2mdiayVWnfWZeNbC4wzpSaLvicougSWgvOiaORBOk6UOw/0?wx_fmt=png)

暗镜

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/mibm5daOCSt98X08oaiaa3t79eUW2Q5RyicXA1ebXOdyVvQ2mdiayVWnfWZeNbC4wzpSaLvicougSWgvOiaORBOk6UOw/0?wx_fmt=png)

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