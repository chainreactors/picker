---
title: 寄生云端：滥用Google Cloud服务的高级钓鱼新手段
url: https://mp.weixin.qq.com/s/hwAUaFFl5sOyMB15Y-SUXg
source: Doonsec's feed
date: 2026-02-27
fetch_date: 2026-02-28T03:51:40.425756
---

# 寄生云端：滥用Google Cloud服务的高级钓鱼新手段

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/8C1NLS8ickpfMrCzkAUiaAZVxCtnOARxfO6EfqtDhib17RJogiastRMmW0yY9v08y4mjic8KeyhOTic1xp6tvichc6NiaCicCmp7tiaDvZ71uHicbme9h0/0?wx_fmt=jpeg)

# 寄生云端：滥用Google Cloud服务的高级钓鱼新手段

走狗是狗哥
走狗是狗哥

安在

![]()

在小说阅读器中沉浸阅读

![图片](https://mmbiz.qpic.cn/mmbiz_gif/5eH7xATwT3icpLmjpDSQkXx16oAygiaJncke0vYYJvIkuzECibrQJcUW4oAedTuib1G9m372rleJRDNXNs54fBEVicg/640?wx_fmt=gif&wxfrom=5&wx_lazy=1&tp=webp)

2026年初，一场隐蔽而高效的网络钓鱼风暴悄然席卷全球企业邮箱。与以往不同，这场攻击的发起者并非来自阴暗的地下服务器，而是“寄生”于全球最受信任的云基础设施之上。

安全研究人员披露，自2026年1月起，攻击者开始系统性滥用Google Cloud Application Integration服务的合法邮件发送功能，使发出的钓鱼邮件显示来自“google.com”等官方子域，从而轻松绕过传统邮件网关的层层检测。

这场攻击不仅技术手法新颖，其造成的广泛影响与暴露的防御盲区，为云时代的网络安全敲响了新的警钟。

 ![](https://mmbiz.qpic.cn/mmbiz_jpg/8C1NLS8ickpcUxiaaVPNym6GLiaFZ1DbolgX2xn4uhwpoMNVcquE0a9u0lPPuw8uSTF7n4JxjTGsPwC3icJ0Z851n0pKePZicFnAJKGJ7VyBBJDc/640?wx_fmt=jpeg&from=appmsg)

**0****1**

**攻击手法剖析：对“信任基础设施”的精准寄生**

此次攻击的核心在于“信任传递”机制的滥用。攻击者不再费力伪造发件人域名，而是直接利用Google云平台自身的自动化工具作为攻击发射台。

他们创建看似合法的Google Cloud项目，通过 “Google Cloud Application Integration” 这一用于工作流自动化的服务，从noreply-application-integration@google.com等官方地址直接向受害者发送恶意邮件。

由于邮件源自Google的真实服务器，其SPF、DKIM、DMARC等邮件身份验证协议均完美通过，这使得传统基于发件人信誉和域名验证的安全体系瞬间失效。

攻击流程设计精巧，采用多阶段策略以最大化欺骗性并规避检测：

初始接触：受害者收到一封来自Google官方基础设施的邮件，内容通常伪装成“新语音邮件通知”、“Q4文件待查看”或“文件共享提醒”等高频办公场景。邮件的格式、语言风格均高度仿照谷歌官方通知，极具迷惑性。

中间跳转：邮件中的链接首先指向storage.cloud.google.com或googleusercontent.com等真实的Google云服务域名。这一设计旨在进一步降低用户警惕，因为链接确实指向了可信的谷歌域名。在此阶段，攻击者有时会设置伪造的图形验证码页面，此举既能阻挡自动化安全扫描工具的检测，又不影响真实用户操作。

终极窃取：通过验证后，受害者最终被引导至一个精心伪造的Microsoft 365或Google Workspace登录页面。一旦用户在此页面输入账号密码，凭证便会被攻击者窃取。更有安全厂商披露，该攻击团伙还同步开展OAuth授权钓鱼，诱导受害者授权恶意应用，以获取长期有效的云资源访问令牌。

**0****2**

**全球影响与行业危害**

此次攻击在短时间内造成了广泛影响。监测数据显示，在为期14天的观测周期内，攻击者累计向全球约3200家机构的用户发送了超过9394封钓鱼邮件。

从地域分布看，美国受影响最为严重（占比48.6%），其次是亚太地区（20.7%）和欧洲（19.8%），拉丁美洲则以巴西和墨西哥为主。这表明跨国企业和涉外机构面临显著的潜在风险。

攻击目标具有明确的行业倾向性。受影响最重的行业包括制造业（19.6%）、科技业（18.9%）以及金融银行业（14.8%）。此外，专业服务、零售、医疗健康、能源及政府部门等也未能幸免。

这些行业普遍依赖自动化通知、文档协作与云端身份认证，使得来自“谷歌”的品牌通知具备天然的可信度优势，更容易让员工放松警惕。

此次事件暴露出一种全新的攻击模式：攻击者正将主流云服务商的基础设施本身转化为攻击面。从利用Google服务发送邮件，到使用Google Cloud Storage或Amazon S3托管中间页面，再到最终窃取Microsoft 365凭证，攻击链的每个环节都寄生在合法的、高信誉的云服务之上。

这种“合法通道滥用”使得攻击行为在各个环节都难以被单独检测和阻断，对传统安全防护体系构成了结构性挑战。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/8C1NLS8ickpeKq9SgAc2tic3jG0kJcb8SJyxDcicwViaXAcDHzOsWibDMOlA8QkJoMHJzEmBRzw2QJSNj6yWLrIh6ibf5ROIyAFH2wWQWsYaspUyM/640?wx_fmt=jpeg&from=appmsg)

**0****3**

**深层反思与防御启示**

谷歌方面在事件披露后已采取紧急措施，阻断了攻击者对相关邮件通知功能的滥用通道。然而，此次事件留给企业安全团队的思考远不止于此。它揭示了在云原生时代，基于“来源可信即内容可信”的静态防御假设已然过时。

为应对此类及类似的高级钓鱼威胁，企业和组织需构建多层纵深的防御体系：

升级技术防护：企业应部署能够进行高级邮件行为分析和上下文检测的安全解决方案。不能仅验证发件人身份，还需分析邮件内容语义、链接跳转行为、以及发件人与收件人之间的历史交互关系是否异常。对来自云服务商的自动通知邮件，也应保持审查能力。

强化身份验证：针对旨在窃取凭证和会话令牌的中间人（AiTM）攻击，组织应强制实施基于FIDO2的硬件安全密钥等抗钓鱼身份验证方式。这类方法不依赖于可能被截获的密码或一次性验证码，能有效阻断凭据窃取。

实施零信任策略：在云环境中配置严格的条件访问策略，限制仅允许从受信任的设备、地理位置或网络访问敏感应用和数据。同时，加强对OAuth应用的治理，定期审计和清理已授权的第三方应用，防止授权被滥用。

筑牢“人的防火墙”：持续对员工进行针对性的安全意识培训至关重要。培训应教会员工识别伪装成合法服务通知的钓鱼邮件，特别强调：即使邮件来自可信域名，也需对其中索要凭证或紧急操作的链接保持警惕；切勿直接点击邮件中的链接登录关键系统，而应手动输入官方网址访问。定期进行模拟钓鱼演练，并将报告可疑邮件的行为纳入正向安全文化。

加强云资源管控：企业管理员需在自身的云环境中实施严格的访问控制和监控策略，防止企业拥有的云资源被攻击者滥用于发起类似攻击。

这场始于2026年初的钓鱼风暴，标志着网络攻击的战术演进进入了一个新阶段：

攻击者正熟练地将全球数字经济的信任基石——大型云平台，转化为他们的攻击武器。防御者必须随之进化，从单纯的信赖边界转向持续的风险评估，在充分利用云便利的同时，构建起适应云原生威胁环境的动态、智能、以身份为中心的安全新防线。

**加入诸子云知识星球**

**获取更多“安全意识资料”和“网络安全报告”**

![](https://mmbiz.qpic.cn/mmbiz_png/5eH7xATwT3ibNFRaXRrrAqFhwTopSZARuBRHia2QlOqWeskibze2BGdcOicic1fjo9AQhQnz6fhWaaxyQeWRg5Glftw/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/5eH7xATwT3ibNFRaXRrrAqFhwTopSZARu8oQyecNb3DGI3xrjDk4ibHAsLXrVK6IuibJxkbPia2GibDW368rMC8sjew/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_jpg/5eH7xATwT3ibNFRaXRrrAqFhwTopSZARu7DrjQIryjzUEd52QC8CwRs7TcK1Ym1ko59IQh1L6CRmRzMMTWKAJTA/640?wx_fmt=jpeg&from=appmsg)

**<**

**左滑了解更多详情**

**>**

**安在安全意识团购服务**

安在新媒体面向企业用户，推出“网络安全意识团购服务”，涵盖宣传素材、培训课程、威胁体验、游戏互动等，采用线上线下融合的方式，帮助员工掌握安全要点，并提供定制化安全策略咨询。

![](https://mmbiz.qpic.cn/mmbiz_png/5eH7xATwT38ItohfRTzvpcE07AIbkJ25dha55ibNRFTkSiaLooM0IVnFWxIAAsKcotGXxaib6xoxGOWXUflQgAc1w/640?wx_fmt=png&from=appmsg#imgIndex=10)

![](https://mmbiz.qpic.cn/mmbiz_png/5eH7xATwT3ibNFRaXRrrAqFhwTopSZARuA1k9KjC2qjwVPqxoj2GuTePvj9P3iatARbJH4lK7CQbnYXAPiad4nKBw/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/5eH7xATwT3ibNFRaXRrrAqFhwTopSZARuFo8ZxbWXsYcN5ic3FIWj3qVO3KcQL4MvyjUGS3fUkBvP8aib2tOrEuRg/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/5eH7xATwT3ibNFRaXRrrAqFhwTopSZARufFJj4S2JlzLRRGaoExkhn9qlM4BKTwb1eiaI4wKdKz1qIqdlyxicjZ9A/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/5eH7xATwT3ibNFRaXRrrAqFhwTopSZARuqrYGia5Z3MCQxvEVYYY6LmCd7w0kicdRgibVWRYFgV5weldBnaXuf2MlA/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/5eH7xATwT3ibNFRaXRrrAqFhwTopSZARuNux88BfNOclEKzic77stzKgHS95fGj0P7Wd0ZNZibHZyt124R0WuXxtQ/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/5eH7xATwT3ibNFRaXRrrAqFhwTopSZARuaQruu45sCpTmhAyKmG3LeQKr8ZnribzeMCkH6ic7dPzeVR2eDCT4ueicA/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/5eH7xATwT3ibNFRaXRrrAqFhwTopSZARuDz8rCnJfRySqe8icxxd2PicmfCa8icjk3m6jRyWCpiatUFdJg9ySWNRtug/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/5eH7xATwT3ibNFRaXRrrAqFhwTopSZARuXF2brGqFXKu2LD0J5h9w9VByqyibTKGEX3oEga61KdlaWMyHzibkMe0Q/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/5eH7xATwT3ibNFRaXRrrAqFhwTopSZARurRCicPuyWq2VzYcag0E6XjiaXOHQ5yRoOjicBL3nB417bf88hBD8tASdg/640?wx_fmt=png&from=appmsg)

**<**

**左滑了解更多详情**

**>**

![](https://mmbiz.qpic.cn/mmbiz_jpg/5eH7xATwT3ibHrKXnibCLKxkSputrnSQP1LAhnuTXgOibjQickqxxwM7IicW64x3dUFUewqBlE2mZADc6cYOjA87G9Q/640?wx_fmt=jpeg&from=appmsg&randomid=yg0vqu25#imgIndex=8)

**部分展示，以作参考

更多服务，详情洽谈**

Tina 诸子云群秘

**END**

![图片](https://mmbiz.qpic.cn/mmbiz_jpg/5eH7xATwT38j3Ndib8YhjyiaBQhdzUe1AAfIzicyojXwPTCxD0QGZHhyRcRicJAHhUv382sYFibICoxjzktlJwEEPag/640?wx_fmt=jpeg&wxfrom=5&wx_lazy=1&tp=webp)

![图片](https://mmbiz.qpic.cn/mmbiz_png/5eH7xATwT38ZuAFVBGW0sBXwme9OON2yYzpnFcekibgKG9tHopXXuCyjSpRk8BVXaapbWyErKPJTBBHFzzT4kMg/640?wx_fmt=png&wxfrom=5&wx_lazy=1&tp=webp)

[![图片](https://mmbiz.qpic.cn/mmbiz_png/5eH7xATwT38j3Ndib8YhjyiaBQhdzUe1AApXU9ib7vkMD4KMHhjVfkTqOCUrDibUaBDoH0OGGCMasLLJyv5xppK6rA/640?wx_fmt=png&wxfrom=5&wx_lazy=1&tp=webp)](https://mp.weixin.qq.com/s?__biz=MzU5ODgzNTExOQ==&mid=2247636140&idx=1&sn=8b53ff22bbfa15b46b0ed22fcb3a5f71&scene=21#wechat_redirect)

![图片](https://mmbiz.qpic.cn/mmbiz_jpg/5eH7xATwT38HPkvxLkOy5rLCeVBtj8H9SUbVPNZbibc4N2knPCDFjTKduRLhiaAZVQShUa2IZqsBShI2GG2dpqBg/640?wx_fmt=jpeg&wxfrom=5&wx_lazy=1&tp=webp)

点击这里阅读原文

预览时标签不可点

阅读原文

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/5eH7xATwT39OIA4MxWIQmVzjc3H2rbMa0sv6no7gMEXOV63OW7hvwk4EDjOaurIkrnPOjBpCmIN00ELKRf16qg/0?wx_fmt=png)

安在

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/5eH7xATwT39OIA4MxWIQmVzjc3H2rbMa0sv6no7gMEXOV63OW7hvwk4EDjOaurIkrnPOjBpCmIN00ELKRf16qg/0?wx_fmt=png)

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