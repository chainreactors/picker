---
title: PamStealer使用假的网站和PAM检查来窃取Mac登录密码
url: https://mp.weixin.qq.com/s/UuZtriYw2blX83lxsScOiA
source: Doonsec's feed
date: 2026-07-03
fetch_date: 2026-07-04T05:42:15.959484
---

# PamStealer使用假的网站和PAM检查来窃取Mac登录密码

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/oPZcPicUADsicUiaJTeSkibIR1JWibu5ANq2ZmXM03CCNwurFaBibVYpHeicZSzXXOa8r3DQq5TYrkq0WOJTlAFNlibmWvgMYWZZCsTj2SYGmLwEZt0/0?wx_fmt=jpeg)

# PamStealer使用假的网站和PAM检查来窃取Mac登录密码

HackSee安全团队
HackSee安全团队

HackSee安全生活

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/oPZcPicUADs8e2Cic1Y0ickKkOaIFbHJxTBwBE8lFhVnesYG9Hd5LGenvhiaM5GuAnDZ32TM5YAibg2oeXbqGMhC30EYOYa9X48p61qPGzcNpxAc/640?wx_fmt=jpeg&from=appmsg)

网络安全研究人员发现了一种新的macOS信息窃取软件PamStealer，它采用了一系列巧妙的技巧来感染系统并窃取敏感数据。

由Jamf威胁实验室发现的窃取程序，以编译后的AppleScript （.scpt）文件的形式分发，该文件冒充Maccy，一个合法的开源剪贴板管理器。它的代号为PamStealer，因为它能够在捕获受害者的登录密码之前，通过macOS可插拔身份验证模块（PAM）验证受害者的登录密码。

恶意软件分为两个阶段：编译后的AppleScript分布在磁盘映像中，旨在下载并执行后续有效负载。次要工件是一个基于rust的信息收集器，能够进行凭证盗窃、浏览器数据收集、持久化和泄露。

恶意软件的初始访问向量是一个类似的网站（"maccyapp[.]com"），模仿Maccy （" Maccy [.]app"）。磁盘映像中的AppleScript （"Maccy.scpt"）执行一个自包含的JavaScript for Automation （JXA）下载程序，该下载程序使用本机Objective-C api获取和执行窃取负载。

这里值得注意的是，脚本一旦通过脚本编辑器启动，就会显示使用键盘快捷键或单击脚本编辑器中的运行按钮来运行它的说明，从而导致隐藏在一大块空行下面的文件中的恶意逻辑被执行。

安全研究员Thijs Xhaflaire说：“值得注意的是，即使文件仍然带有com.apple.quarantine属性，这种方法也能起作用，这使得这种方法对攻击者很有吸引力，因为苹果公司继续加强Gatekeeper和Terminal。”结合基于rust的第二阶段和通过PAM本地验证凭证的密码捕获工作流，结果是一个比我们通常在商品macOS窃取器中观察到的更安静的执行链。

AppleScript dropper集成了环境感知功能，允许只有在对主机进行指纹识别并确定它在Apple Silicon上运行后才能继续执行。它通过基于指纹（包括CPU架构、区域设置、键盘布局和时区等详细信息）派生密钥，然后使用它来解锁包含有效负载URL和安装路径的加密配置，从而实现这一点。

在基于英特尔的mac电脑上，导出的解密密钥不同，无法解码配置，导致dropper终止。该脚本还避免在沙盒或分析环境中执行，以及在时区、系统区域设置和键盘输入解析为位于东欧的国家的系统中执行，例如俄罗斯、白俄罗斯、哈萨克斯坦、亚美尼亚、阿塞拜疆、吉尔吉斯斯坦、摩尔多瓦、塔吉克斯坦、乌兹别克斯坦、土库曼斯坦和格鲁吉亚。

一旦检查通过，脚本就会连接到外部服务器并下载用Rust编写的Mach-O二进制文件，该文件伪装成Finder应用程序，负责从web浏览器、加密货币钱包扩展、iCloud Keychain和剪贴板内容中收集数据。然后，捕获的信息被加密并通过出站HTTP请求泄露到攻击者控制的基础设施（复仇者同步[.]live]）。

除了强迫用户授予其完整的文件系统访问权限外，窃取者还提供一个本地密码提示，收集受害者的系统密码，然后通过PAM API交叉检查输入的密码，从而验证密码。如果验证失败，它要求用户重新输入密码，并重复该循环，直到提供正确的密码。

一旦获得有效密码，窃贼就会显示第二道伪造警报：“梅西百货已损坏，无法打开。”“你应该把它移到垃圾箱里，”詹姆说，“这是真正的守门人信息的一个完整副本。”这是一个诱饵。当它出现时，有效载荷已经运行，捕获密码并注册持久化，因此该消息只会使受害者放弃诱饵并认为下载已被破坏。

Rust二进制文件中还内置了一个小型arm64 Mach-O，它模拟macOS系统设置，用于设置持久性。

这一事态发展促使Maccy的开发者亚历克斯·罗迪奥诺夫（Alex Rodionov）在他们的网站和GitHub存储库上发布了一条警告，称“小心假冒Maccy的虚假网站。”恶意网站(如maccyapp[. .]. net和maccyapp[. net]com)分发伪装成macy的恶意软件。maccy。App是唯一官方网站。"；

Jamf说：“总之，这些行为说明了商用macOS窃取者如何继续发展，采用更安静的执行链和本地实现，减少传统的检测机会，同时保持与标准macOS功能的兼容。”

预览时标签不可点

![]()

微信扫一扫
关注该公众号

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/M8pOVgDSPVI7jF9IeH2p6icHIDM6ZMlreAbOiciaoho809sdhhiaE7t8DRlhgSg3h1s7k7eDlfX32AfCLXUnLwXYsw/0?wx_fmt=png)

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