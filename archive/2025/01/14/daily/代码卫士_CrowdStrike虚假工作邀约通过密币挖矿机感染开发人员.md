---
title: CrowdStrike虚假工作邀约通过密币挖矿机感染开发人员
url: https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247522044&idx=2&sn=f72144000ab0d2c1280f017af0018e6e&chksm=ea94a796dde32e802b549f6142713bd6d30abcff4fb2dad9a2d96d274145d96f5962e976b84c&scene=58&subscene=0#rd
source: 代码卫士
date: 2025-01-14
fetch_date: 2025-10-06T20:11:02.295869
---

# CrowdStrike虚假工作邀约通过密币挖矿机感染开发人员

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/oBANLWYScMTicSxCiaH3vW2G3Ga7NqIWC1iaKFvK0BtKUeskAQ1GNwTuSv50P4yReXQjaCtxQe0zt77xzU80ya8TA/0?wx_fmt=jpeg)

# CrowdStrike虚假工作邀约通过密币挖矿机感染开发人员

Bill Toulas

代码卫士

![](https://mmbiz.qpic.cn/mmbiz_gif/Az5ZsrEic9ot90z9etZLlU7OTaPOdibteeibJMMmbwc29aJlDOmUicibIRoLdcuEQjtHQ2qjVtZBt0M5eVbYoQzlHiaw/640?wx_fmt=gif) 聚焦源代码安全，网罗国内外最新资讯！

**编译：代码卫士**

**CrowdStrike 公司提醒称，攻击者正在模拟该公司发送虚假工作邀约邮件，通过门罗币挖矿机 (XMRig) 感染开发人员。**

CrowdStrike 公司在2025年1月7日发现该恶意活动，从该钓鱼邮件的内容来看，可能开始时间不算太早。

攻击始于发送给求职者的一份钓鱼邮件，假装来自 CrowdStrike 公司的招聘代理，感谢他们申请该公司的开发人员岗位。该邮件诱骗目标从看似是合法 CrowdStrike 门户的网站下载“员工CRM申请”，并称此举是为了“推出一款新的申请者CRM应用来拉通招聘流程”。点击该嵌入式链接的岗位候选人被引到一个站点 (“cscrm-hiring[.]com”)，其中包含适用于 Windows 或 macOS 的上述应用。

所下载的工具在提取其它payload之前会执行沙箱检查，确保它不在分析环境中运行，会检查进程号码、CPU核心数以及调试程序的情况。一旦检查结束，说明受害者具备受感染的条件，那么应用就会生成一条恶意错误信息称安装文件可能受损。该下载器会在后台检索包含用于运行XMRig的所需参数的文本文件。之后会从GitHub 仓库下载包含该挖矿机的ZIP压缩文档并在 '%TEMP%\System\.' 中解压文件。该挖矿机在后台被设置为运行，消耗最小处理能力（最多10%）来避免被检测到。攻击者会在开始目录启动目录添加一个批处理脚本，重启之后仍能保持可持久性，同时会在注册表中编写登录自动启动密钥。

求职者应当验证属于所求职公司的官方域名的邮件地址，并通过官网页面联系相关人员。应警惕紧急或异常请求、好得不真实的工作邀约、在自己电脑上下载可执行文件（通常会以招聘需求为借口）的邀请。招聘单位，极少会要求候选人下载第三方应用参加面试且从来不会要求付款。

代码卫士试用地址：https://codesafe.qianxin.com

开源卫士试用地址：https://oss.qianxin.com

---

---

**推荐阅读**

[CrowdStrike 宕机后，微软拟让EDR厂商在内核模式外”运行](https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247520848&idx=3&sn=4a3ec7b673c6f5a5650610d98d80b076&scene=21#wechat_redirect)

[CrowdStrike：测试软件中的bug导致Windows蓝屏死机](https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247520213&idx=1&sn=315d12b373fb85e4b9c485117694c9ba&scene=21#wechat_redirect)

[npm恶意包瞄准以太坊开发人员的私钥](https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247521982&idx=2&sn=96ae7195cbcc72a978eda7a5303a971d&scene=21#wechat_redirect)

[微软紧急提醒开发人员更新 .NET 安装程序，以免遭供应链攻击](https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247521944&idx=1&sn=357a81205db555dba57e13b2d91e4d0c&scene=21#wechat_redirect)

[Lazarus利用虚假密码管理器编程测试诱骗Python开发人员](https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247520782&idx=2&sn=cce5137652ee5a865b8d94f6c0c4d5d5&scene=21#wechat_redirect)

**原文链接**

https://www.bleepingcomputer.com/news/security/fake-crowdstrike-job-offer-emails-target-devs-with-crypto-miners/

题图：Pexels License

**本文由奇安信编译，不代表奇安信观点。转载请注明“转自奇安信代码卫士 https://codesafe.qianxin.com”。**

![](https://mmbiz.qpic.cn/mmbiz_jpg/oBANLWYScMSf7nNLWrJL6dkJp7RB8Kl4zxU9ibnQjuvo4VoZ5ic9Q91K3WshWzqEybcroVEOQpgYfx1uYgwJhlFQ/640?wx_fmt=jpeg)

![](https://mmbiz.qpic.cn/mmbiz_jpg/oBANLWYScMSN5sfviaCuvYQccJZlrr64sRlvcbdWjDic9mPQ8mBBFDCKP6VibiaNE1kDVuoIOiaIVRoTjSsSftGC8gw/640?wx_fmt=jpeg)

**奇安信代码卫士 (codesafe)**

国内首个专注于软件开发安全的产品线。

![](https://mmbiz.qpic.cn/mmbiz_gif/oBANLWYScMQ5iciaeKS21icDIWSVd0M9zEhicFK0rbCJOrgpc09iaH6nvqvsIdckDfxH2K4tu9CvPJgSf7XhGHJwVyQ/640?wx_fmt=gif) 觉得不错，就点个 “在看” 或 "赞” 吧~

预览时标签不可点

阅读原文

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/oBANLWYScMQnXWuOU95T0gnUjHe8IhdLQuqwxvDpLf7GwP25ntfz6W8dhDhUS3BstsPLPL9YBRXE1QhF9eIjiaw/0?wx_fmt=png)

代码卫士

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/oBANLWYScMQnXWuOU95T0gnUjHe8IhdLQuqwxvDpLf7GwP25ntfz6W8dhDhUS3BstsPLPL9YBRXE1QhF9eIjiaw/0?wx_fmt=png)

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