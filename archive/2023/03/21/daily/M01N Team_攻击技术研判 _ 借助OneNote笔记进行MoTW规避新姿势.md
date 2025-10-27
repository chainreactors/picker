---
title: 攻击技术研判 | 借助OneNote笔记进行MoTW规避新姿势
url: https://mp.weixin.qq.com/s?__biz=MzkyMTI0NjA3OA==&mid=2247491074&idx=1&sn=500ab115fc9e491ddaa0bdf74709b1ec&chksm=c187de13f6f05705f211f1cce11ba8908ab5c888bcfdf0d646233782340af308fb1aa223c915&scene=58&subscene=0#rd
source: M01N Team
date: 2023-03-21
fetch_date: 2025-10-04T10:09:34.463254
---

# 攻击技术研判 | 借助OneNote笔记进行MoTW规避新姿势

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/TPGibEO8KBwYSKT7e5OKt5ozRt570BMNu9TnSDFoialgXnIkjEw069F8B2mKgRy9giayuFpP0djicJ9wtDGbk9GCkg/0?wx_fmt=jpeg)

# 攻击技术研判 | 借助OneNote笔记进行MoTW规避新姿势

原创

天元实验室

M01N Team

![](https://mmbiz.qpic.cn/mmbiz_gif/TPGibEO8KBwYoKzb0BELnlJsfZuowWqWCNNmRkYQap144u0PSc9QwHicdsPt47otkltpk1A6wfPxricjASZHQwRTQ/640?wx_fmt=gif)

**情报背景**

在CVE-2022-41091的安全补丁更新后，Windows会将MoTW标记传播到ISO中包含的所有内容并在文件打开时显示安全警告，这意味着用ISO等非NTFS格式文件打包恶意宏文档进行投递以规避MoTW标记的方式基本失效。近期，攻击者开始转向利用OneNote笔记文件（.one）来进行恶意载荷的分发，利用.one文件搭载WSF文件诱导受害者执行，使之成为宏文档的替代方式。本文将围绕其中的技术细节进行分析研判。

|  |  |
| --- | --- |
| **组织名称** | Emotet |
| **战术标签** | 初始访问 |
| **技术标签** | 鱼叉式钓鱼附件 |
| **情报来源** | https://www.bleepingcomputer.com/news/security/emotet-malware-now-distributed-in-microsoft-onenote-files-to-evade-defenses/ |

**01** 攻击技术分析

**要点：利用OneNote文件分发恶意文件规避MoTW**

在安装了CVE-2022-41091的安全补丁后，Windows会将Web标记从ISO传播到其内容文件上：

![](https://mmbiz.qpic.cn/mmbiz_png/TPGibEO8KBwYoKzb0BELnlJsfZuowWqWCnHgyXia5saghZPfC9NREoHEaAdicXPibFKgcDmyAwrkPHazhAJBD8Qp4A/640?wx_fmt=png)

为了规避步步紧逼的WEB标记防御策略，攻击者转向OneNote笔记文件的恶意利用。OneNote笔记文件后缀为.one，微软允许用户创建包含嵌入文件的OneNote文档。但当嵌入文件所在的位置被双击时，即使其上被图片覆盖仍会启动对应文件。恶意OneNote文件以钓鱼邮件的形式分发，受害者会被攻击者引导双击图片上的某一特定位置以查看被模糊化的内容，导致潜藏在图片之下的格式为.wsf的VBScript文件被执行：

![](https://mmbiz.qpic.cn/mmbiz_png/TPGibEO8KBwYoKzb0BELnlJsfZuowWqWC0u7JHUTOd1TeVrTXm7gKJDI7icJ18XKcTor9b0Cx4s2nAYT4GMBRu1g/640?wx_fmt=png)

VBScript附件的执行会触发微软安全警告：

![](https://mmbiz.qpic.cn/mmbiz_jpg/TPGibEO8KBwYoKzb0BELnlJsfZuowWqWCnibwzA5BTXloFkXacic46ILmZVw3licWYbHLhhXW23qJhgAWu3OkkdaLQ/640?wx_fmt=jpeg)

但对于缺乏安全意识的用户而言，这种攻击形式仍然具有较强的诱惑性。

**端侧防守策略**

借助系统自带的防护功能策略，目前针对这类钓鱼攻击手段的主要限制方法有三种：

**1.禁止所有嵌入式OneNote附件**

![](https://mmbiz.qpic.cn/mmbiz_png/TPGibEO8KBwYoKzb0BELnlJsfZuowWqWCTrA18uEWMJpibdhQ3RhLmurCBSMTSfnK6hbpePrvKc2LJQbkibhGHiczQ/640?wx_fmt=png)

组策略的配置将创建注册表键值：[HKEY\_CURRENT\_USER\SOFTWARE\Policies\Microsoft\office\16.0\onenote\options]

"disableembeddedfiles"=dword:00000001

当尝试打开OneNote附件时会被阻止并收到警告。一棒子打死的方案的确阻止了利用OneNote附件传播恶意文件的可能性，但也在很大程度上限制了OneNote本身的功能以及共享信息的便捷性；

**2.配置组策略**

通过配置组策略“Embedded Files Blocked Extensions”，可以指定默认阻止的OneNote附件文件类型，限定附件的文件类型能够在尽可能少地影响正常功能的前提下很好地限制恶意文件的出现。组策略对应的注册表键值为：[HKEY\_CURRENT\_USER\SOFTWARE\Policies\Microsoft\office\16.0\onenote\options\embeddedfileopenoptions]

"blockedextensions"=".js;.exe;.bat;.vbs;.com;.scr;.cmd;.ps1"

这种方式能够更加有针对性地对指定文件类型进行拦截，但也潜藏了被攻击者发现新文件扩展利用方式以绕过拦截的风险。

**3.ASR攻击面减少规则**

ASR是Microsoft Defender for Endpoint提供的内置组策略配置，能够对邮件、Office文档等常见攻击媒介的行为做针对性的检测与拦截。通过启用规则：“阻止所有Office应用程序创建子进程”（GUID：d4f940ab-401b-4efc-aadc-ad5f3c50688a）能够有效拦截相关行为。

**02**总结

随着OneNote附件这种文件类型在传播恶意文件上的功能被发掘，尤其是在交互时能够直接运行图片下的附件文件的特性，使得.one成为后宏时代又一重要诱饵文件类型。对其的限制主要还是依赖于主动的策略配置，在社工场景下的安全意识不足依然能够带给这种攻击方式很大的发挥空间。

**附录** 参考文献

[1]https://www.bleepingcomputer.com/news/microsoft/microsoft-fixes-windows-zero-day-bug-exploited-to-push-malware/

[2]https://www.bleepingcomputer.com/news/security/how-to-prevent-microsoft-onenote-files-from-infecting-windows-with-malware/

[3]https://www.bleepingcomputer.com/news/microsoft/microsoft-onenote-to-get-enhanced-security-after-recent-malware-abuse/

[4]https://learn.microsoft.com/zh-cn/microsoft-365/security/defender-endpoint/attack-surface-reduction-rules-reference?view=o365-worldwide#block-office-applications-from-creating-executable-content

![](https://mmbiz.qpic.cn/mmbiz_png/TPGibEO8KBwYoKzb0BELnlJsfZuowWqWC2qz9OHLw62Uy8HaoUiawBnHzukW8mrIvUibQ5daru2uibSoR0XxRMSwLw/640?wx_fmt=png)

**绿盟科技天元实验室**专注于新型实战化攻防对抗技术研究。

研究目标包括：漏洞利用技术、防御绕过技术、攻击隐匿技术、攻击持久化技术等蓝军技术，以及攻击技战术、攻击框架的研究。涵盖Web安全、终端安全、AD安全、云安全等多个技术领域的攻击技术研究，以及工业互联网、车联网等业务场景的攻击技术研究。通过研究攻击对抗技术，从攻击视角提供识别风险的方法和手段，为威胁对抗提供决策支撑。

![](https://mmbiz.qpic.cn/mmbiz_jpg/TPGibEO8KBwYoKzb0BELnlJsfZuowWqWChy1dWyGNf22a9P0vTomLJIia6QnYpczd2kNj1fYBILU5zLmqISJSfVA/640?wx_fmt=jpeg)

**M01N Team公众号**

聚焦高级攻防对抗热点技术

绿盟科技蓝军技术研究战队

![](https://mmbiz.qpic.cn/mmbiz_png/TPGibEO8KBwYoKzb0BELnlJsfZuowWqWCIDdI53T3pOunyQBOon8HWlHboxo8icNffhuVCMia32naaO0sJVwd0hHg/640?wx_fmt=png)

**官方攻防交流群**

网络安全一手资讯

攻防技术答疑解惑

扫码加好友即可拉群

**往期推荐**

[攻击技术研判 | 使用蜂鸣器对抗沙箱检测技术](http://mp.weixin.qq.com/s?__biz=MzkyMTI0NjA3OA==&mid=2247490989&idx=1&sn=22346fc6a4586c666c2eb23478d3cd83&chksm=c187ddbcf6f054aa17b85b2d007c2949b5a606a19423365c3992e302e44ef40a4de28196a447&scene=21#wechat_redirect)

![](https://mmbiz.qpic.cn/mmbiz_png/TPGibEO8KBwYoKzb0BELnlJsfZuowWqWCg1g7QKcyPkib7IfdziabZicLsFicEZ8T06RbGaAr5jzr03rCopYAReF9xA/640?wx_fmt=png)

[攻击技术研判 | Earth Kitsune滥用vcruntime140.dll和Chrome扩展等实现持久化](http://mp.weixin.qq.com/s?__biz=MzkyMTI0NjA3OA==&mid=2247490905&idx=1&sn=2c1426495bfdc73b5ca85a0dfba899c6&chksm=c187dd48f6f0545e04c5a10a2a04126f7ff9671068053f09eb8cf50e9401c5fc30597b6f86a3&scene=21#wechat_redirect)

![](https://mmbiz.qpic.cn/mmbiz_png/TPGibEO8KBwYoKzb0BELnlJsfZuowWqWCg1g7QKcyPkib7IfdziabZicLsFicEZ8T06RbGaAr5jzr03rCopYAReF9xA/640?wx_fmt=png)

[攻击技术研判 | 曝光一周年，向日葵RCE漏洞在野利用再现](http://mp.weixin.qq.com/s?__biz=MzkyMTI0NjA3OA==&mid=2247490787&idx=1&sn=a87fa18a4b7e8e4b01b67abd9a8c0c51&chksm=c187dcf2f6f055e41de2982d637ae09a257cacf3e7bf2b23fcfcded679911d1682d49a5485ba&scene=21#wechat_redirect)

![](https://mmbiz.qpic.cn/mmbiz_png/TPGibEO8KBwYoKzb0BELnlJsfZuowWqWCg1g7QKcyPkib7IfdziabZicLsFicEZ8T06RbGaAr5jzr03rCopYAReF9xA/640?wx_fmt=png)

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/TPGibEO8KBwa3nTcsDs91X6JY6LnXNhPLatIoU1PEVBLzWXTcnyiahhYUB9hcwX2MJkOmo9NEM2jVO8ib8yutnJxw/0?wx_fmt=png)

M01N Team

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/TPGibEO8KBwa3nTcsDs91X6JY6LnXNhPLatIoU1PEVBLzWXTcnyiahhYUB9hcwX2MJkOmo9NEM2jVO8ib8yutnJxw/0?wx_fmt=png)

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