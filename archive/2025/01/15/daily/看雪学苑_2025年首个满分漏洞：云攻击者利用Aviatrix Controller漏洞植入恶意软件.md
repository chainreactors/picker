---
title: 2025年首个满分漏洞：云攻击者利用Aviatrix Controller漏洞植入恶意软件
url: https://mp.weixin.qq.com/s?__biz=MjM5NTc2MDYxMw==&mid=2458588667&idx=3&sn=af4f2eb4bededa0cea574e3cd7963382&chksm=b18c257186fbac670637d659a7511de8c3ead88069367df522ef629a278eaa02c9daf567134d&scene=58&subscene=0#rd
source: 看雪学苑
date: 2025-01-15
fetch_date: 2025-10-06T20:10:48.066304
---

# 2025年首个满分漏洞：云攻击者利用Aviatrix Controller漏洞植入恶意软件

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1UG7KPNHN8GhB2YhPKZEztqohjYnMYVp1YL93qHYzh96299iaTkP0ogsavmqMFDjlNTTWVdHdkiaib7rc5ibbE1gpg/0?wx_fmt=jpeg)

# 2025年首个满分漏洞：云攻击者利用Aviatrix Controller漏洞植入恶意软件

看雪学苑

看雪学苑

2025年1月14日，网络安全研究人员发现，云攻击者正在利用一个名为Max-Critical Aviatrix RCE的漏洞（编号**CVE-2024-50603），该漏洞在CVSS评分中高达10分（满分10分），****能够在受影响系统上执行未经身份验证的远程代码，**网络犯罪分子借此漏洞植入恶意软件。

该漏洞存在于所有版本低于7.2.4996或7.1.4191的受支持Aviatrix Controller版本中。Aviatrix Controller是一款强大的云网络管理平台，提供简化的跨云网络管理、自动化配置、安全策略、流量监控等功能，帮助企业实现更加灵活、安全和高效的云网络架构，特别适用于多云和混合云环境。**该漏洞是由于Aviatrix Controller未能正确检查或验证用户通过其应用程序编程接口（API）发送的数据而产生的。**

研究人员指出，该漏洞在亚马逊Web服务（AWS）云环境中尤为危险，因为在此环境中，Aviatrix Controller默认允许权限提升。据Wiz Security的研究，约3%的云企业环境部署了Aviatrix Controller，而在这些环境里，托管Aviatrix Controller的虚拟机中有65%存在通向管理云控制平面权限的横向移动路径。数百家大型企业运用Aviatrix的技术管理AWS、Azure、谷歌云平台（GCP）以及其他多云环境中的云网络，其客户包括Heineken、Raytheon、Yara和IHG Hotels and Resorts等大型集团企业。

安全研究员Jakub Korepta（来自SecuRing）发现了这一漏洞并向Aviatrix报告，于1月7日公开披露了该漏洞的详细信息。仅一天之后，一个针对该漏洞的概念验证利用程序就在GitHub上可获取，随即引发了近乎立即利用的网络攻击与入侵活动。Wiz人工智能与威胁研究副总裁Alon Schindel表示，自概念验证发布以来，Wiz观察到大多数易受攻击的企业都未曾更新修复补丁。目前攻击者利用此漏洞在易受攻击的目标上部署XMRig加密货币挖矿恶意软件和Sliver后门。

Aviatrix已经发布了针对该漏洞的补丁，并且建议相关组织进行补丁安装或者升级到Controller的7.1.4191或7.2.4996版本。Aviatrix公司指出：“在某些情形下，补丁在控制器升级过程中并非完全持久有效，即便控制器状态显示为‘已打补丁’，也必须重新应用，例如在不受支持的控制器版本上应用补丁这种情况。” 对于无法立即打补丁的组织，Schindel建议应立即限制对Aviatrix Controller的网络访问，仅允许受信任的来源进行访问。他们还应当密切监控日志和系统行为中的可疑活动或者已知利用指标，针对与Aviatrix相关的异常行为设置警报，并减少云身份之间不必要的横向移动路径。

Ray Kelly称，Aviatrix Controller漏洞再次让人们意识到API端点日益增长的风险，以及应对这些风险所面临的挑战。该漏洞表明仅仅一个简单的网络调用就可能攻破服务器，凸显了对API进行彻底测试的必要性。鉴于API的规模、复杂性以及相互依赖性，并且许多API是由外部软件和服务提供商开发和管理的，这样的测试可能极具挑战性。Kelly进一步表示：“缓解这些风险的一个有效方法是建立针对第三方软件明确的‘治理规则’。这包括实施针对第三方供应商的全面审查流程、执行一致的安全措施以及持续监控软件性能和漏洞。”

资讯来源：darkreading

转载请注明出处和本文链接

﹀

﹀

﹀

![](https://mmbiz.qpic.cn/mmbiz_jpg/Uia4617poZXP96fGaMPXib13V1bJ52yHq9ycD9Zv3WhiaRb2rKV6wghrNa4VyFR2wibBVNfZt3M5IuUiauQGHvxhQrA/640?wx_fmt=jpeg)

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/1UG7KPNHN8E9S6vNnUMRCOictT4PicNGMgHmsIkOvEno4oPVWrhwQCWNRTquZGs2ZLYic8IJTJBjxhWVoCa47V9Rw/640?wx_fmt=gif)

**球分享**

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/1UG7KPNHN8E9S6vNnUMRCOictT4PicNGMgHmsIkOvEno4oPVWrhwQCWNRTquZGs2ZLYic8IJTJBjxhWVoCa47V9Rw/640?wx_fmt=gif)

**球点赞**

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/1UG7KPNHN8E9S6vNnUMRCOictT4PicNGMgHmsIkOvEno4oPVWrhwQCWNRTquZGs2ZLYic8IJTJBjxhWVoCa47V9Rw/640?wx_fmt=gif)

**球在看**

![](https://mmbiz.qpic.cn/mmbiz_gif/1UG7KPNHN8FxuBNT7e2ZEfQZgBuH2GkFjvK4tzErD5Q56kwaEL0N099icLfx1ZvVvqzcRG3oMtIXqUz5T9HYKicA/640?wx_fmt=gif)

戳“阅读原文”一起来充电吧！

预览时标签不可点

阅读原文

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/1UG7KPNHN8EGLfh77kFmnicd9WOic2ibvhCibFdB4bL4srJCgo2wnvdoXLxpIvAkfCmmcptXZB0qKWMoIP8iaibYN2FA/0?wx_fmt=png)

看雪学苑

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/1UG7KPNHN8EGLfh77kFmnicd9WOic2ibvhCibFdB4bL4srJCgo2wnvdoXLxpIvAkfCmmcptXZB0qKWMoIP8iaibYN2FA/0?wx_fmt=png)

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