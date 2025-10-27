---
title: Palo Alto防火墙又被黑：最新漏洞披露后第二天就遭利用
url: https://mp.weixin.qq.com/s?__biz=MzI4NDY2MDMwMw==&mid=2247513752&idx=1&sn=39cc6a0e87b2d70d65cdc8731d42f1e2&chksm=ebfaf1b8dc8d78aed3b262ebed3c3e9207675e5c248f4b6c714f4f7c338ca163c87d2b47751b&scene=58&subscene=0#rd
source: 安全内参
date: 2025-02-18
fetch_date: 2025-10-06T20:39:52.909644
---

# Palo Alto防火墙又被黑：最新漏洞披露后第二天就遭利用

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/FzZb53e8g7v9vAhAezhAuvtmnYAbzTaT2MImOha2fgejIoLt2erZth32LVnR3CcI1JXOWQXicOAU3ia8cqlE6QfA/0?wx_fmt=jpeg)

# Palo Alto防火墙又被黑：最新漏洞披露后第二天就遭利用

安全内参编译

安全内参

**关注我们**

**带你读懂网络安全**

![图片](https://mmbiz.qpic.cn/sz_mmbiz_jpg/FzZb53e8g7sCJ9An5FeDcUKJA1xL2QdPJVK970AnWEKrIdG8dHcGVicLOBLzrSsIHpxZ6rWB8N1cV3ibV4iauyvsw/640?wx_fmt=other&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

**多方原因造成了这一状况。一方面，该漏洞利用方式与1月披露的已被利用漏洞CVE-2025-0108类似；另一方面，有安全团队在漏洞披露后马上公布了技术细节。**

前情回顾·**国际漏洞利用态势**

* [网安巨头Palo Alto全球数千防火墙被攻陷：因开发低级错误造成零日漏洞](https://mp.weixin.qq.com/s?__biz=MzI4NDY2MDMwMw==&mid=2247513156&idx=1&sn=4ff7c148a1693c0de1be122e65851155&scene=21#wechat_redirect)
* [警惕！近期Fortinet防火墙频遭攻击，疑似零日漏洞被利用](https://mp.weixin.qq.com/s?__biz=MzI4NDY2MDMwMw==&mid=2247513504&idx=1&sn=838af406a4e2aec5e99b37399b5f1a2e&scene=21#wechat_redirect)
* [警惕！国产工业路由器零日漏洞疑遭攻击者利用](https://mp.weixin.qq.com/s?__biz=MzI4NDY2MDMwMw==&mid=2247513393&idx=1&sn=1a9e508382839d999a5a0058560e6b35&scene=21#wechat_redirect)
* [警惕！2024年全球零日漏洞利用呈现七大趋势](https://mp.weixin.qq.com/s?__biz=MzI4NDY2MDMwMw==&mid=2247513353&idx=1&sn=cc572d3391797a15aa66590d70d0ac96&scene=21#wechat_redirect)

安全内参2月17日消息，据美国威胁情报公司GreyNoise报告，影响Palo Alto Networks防火墙的身份验证绕过漏洞（CVE-2025-0108）在公开披露后，短短1天内便遭到攻击者利用。

Palo Alto Networks于2月12日发布了针对CVE-2025-0108的补丁和缓解措施。该漏洞允许未经身份验证的攻击者访问防火墙管理界面并执行特定的PHP脚本。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/FzZb53e8g7v9vAhAezhAuvtmnYAbzTaTBd9pxAMQ3GIPicPtvJQlbIRJNC1UxP78VUj7cNCddw72jibuNiaKcSNtw/640?wx_fmt=png&from=appmsg)

GreyNoise于2月13日透露，其已开始检测到针对CVE-2025-0108的攻击尝试。截至2月14日上午，该公司已观测到来自5个不同IP地址的攻击活动。

GreyNoise将这些攻击尝试标记为“恶意”，表明这些攻击更可能由威胁行为者发起，而非安全研究人员在评估易受攻击系统的数量。

**此前有安全团队公布细节**

发现该漏洞的研究团队Assetnote，在Palo Alto发布补丁公告当天就公开了漏洞的技术细节。这一举动可能使威胁行为者更容易将CVE-2025-0108纳入其攻击武器库。

不过Assetnote也指出，CVE-2025-0108需要与另一个漏洞组合使用，才能实现远程代码执行。

其中一个可能的相关漏洞是CVE-2024-9474，该漏洞已被积极利用。威胁行为者可能已经发现了一个类似于CVE-2024-9474的新漏洞，或者他们正在针对数月未更新的系统发动攻击（CVE-2024-9474的补丁于2024年11月发布）。

Assetnote还表示，CVE-2025-0108与CVE-2024-0012类似。CVE-2024-0012是一个已被在野利用的身份验证绕过漏洞，通常与CVE-2024-9474联合使用。威胁行为者可能只是调整了CVE-2024-0012的利用代码，以攻击CVE-2024-0108，而无需依赖安全公司发布的具体信息。

外媒SecurityWeek已联系Assetnote，询问其为何在漏洞披露后立即公开技术细节，同时也联系了Palo Alto Networks，以确认CVE-2024-0108是否已被用于实际攻击。

Palo Alto Networks在其针对CVE-2024-0108发布的公告中仍表示，公司尚未发现该漏洞在野外被利用。尽管该漏洞被评为“高危”，但厂商给予的紧急性评级仅为“中等”。

**参考资料：securityweek.com**

**推荐阅读**

* [网安智库平台长期招聘兼职研究员](http://mp.weixin.qq.com/s?__biz=MzI4NDY2MDMwMw==&mid=2247499450&idx=2&sn=2da3ca2e0b4d4f9f56ea7f7579afc378&chksm=ebfab99adc8d308c3ba6e7a74bd41beadf39f1b0e38a39f7235db4c305c06caa49ff63a0cc1d&scene=21#wechat_redirect)
* [欢迎加入“安全内参热点讨论群”](https://mp.weixin.qq.com/s?__biz=MzI4NDY2MDMwMw==&mid=2247501251&idx=1&sn=8b6ebecbe80c1c72317948494f87b489&chksm=ebfa82e3dc8d0bf595d039e75b446e14ab96bf63cf8ffc5d553b58248dde3424fb18e6947440&token=525430415&lang=zh_CN&scene=21#wechat_redirect)

---

点击下方卡片关注我们，

带你一起读懂网络安全 ↓

预览时标签不可点

阅读原文

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/FzZb53e8g7u3766XzHf0XHoQ1HkzDV0M7wC5zTyTO6daqAZ6LMD0Lykps2WumsWj2KMQJAGhwOYDcb3E8AicxSw/0?wx_fmt=png)

安全内参

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/FzZb53e8g7u3766XzHf0XHoQ1HkzDV0M7wC5zTyTO6daqAZ6LMD0Lykps2WumsWj2KMQJAGhwOYDcb3E8AicxSw/0?wx_fmt=png)

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