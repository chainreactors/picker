---
title: 工信部：关于防范SafePay勒索病毒的风险提示
url: https://mp.weixin.qq.com/s?__biz=MzI4NDY2MDMwMw==&mid=2247513393&idx=2&sn=e05b5393422e6a439d4f1c16bb878b2e&chksm=ebfaf211dc8d7b073fe23c80121d4d4b62820898cfbcb294b8b2c0a02e52e63b5da3c7fdfedf&scene=58&subscene=0#rd
source: 安全内参
date: 2025-01-01
fetch_date: 2025-10-06T20:07:52.813886
---

# 工信部：关于防范SafePay勒索病毒的风险提示

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/FzZb53e8g7tK1txjTibvJm2kDODtV6MP65apic6ot13YBnJ6KdTxDUtKynSqicM6KicrHuL3wfpJE7aKFbxUvXMdXw/0?wx_fmt=jpeg)

# 工信部：关于防范SafePay勒索病毒的风险提示

安全内参

**关注我们**

**带你读懂网络安全**

**其通过数据窃取和文件加密双重勒索机制开展攻击，可能导致数据泄露、业务中断等安全风险。**

近日，工业和信息化部网络安全威胁和漏洞信息共享平台（CSTIS）监测到一种名为SafePay的新型勒索病毒，其通过数据窃取和文件加密双重勒索机制开展攻击，可能导致数据泄露、业务中断等安全风险。

SafePay勒索病毒与LockBit勒索病毒密切相关，并深度借鉴INC和ALPHV/BlackCat等勒索病毒攻击策略。在数据窃取阶段，SafePay利用已知漏洞或弱口令实施攻击入侵，成功感染目标终端后，通过WinRAR、FileZilla等工具归档、盗取目标文件。在加密部署阶段，SafePay通过远程桌面协议（RDP）访问目标终端，利用PowerShell脚本实施文件加密、禁用恢复和删除卷影副本，对加密文件添加“.safepay”扩展名，并留下名为“readme\_safepay.txt”的勒索文件。在攻击过程中，SafePay会通过COM对象技术绕过用户账户控制（UAC）和提升权限，采用禁用Windows Defender、字符串混淆、线程创建、重复安装卸载工具等机制规避检测。

建议相关单位及用户立即组织排查，加强RDP等远程访问的安全管理，使用强密码和多因素身份验证，实施全盘病毒查杀，及时修复已知安全漏洞，谨慎警惕来源不明的文件，定期备份重要数据，防范网络攻击风险。

**推荐阅读**

* [网安智库平台长期招聘兼职研究员](http://mp.weixin.qq.com/s?__biz=MzI4NDY2MDMwMw==&mid=2247499450&idx=2&sn=2da3ca2e0b4d4f9f56ea7f7579afc378&chksm=ebfab99adc8d308c3ba6e7a74bd41beadf39f1b0e38a39f7235db4c305c06caa49ff63a0cc1d&scene=21#wechat_redirect)
* [欢迎加入“安全内参热点讨论群”](https://mp.weixin.qq.com/s?__biz=MzI4NDY2MDMwMw==&mid=2247501251&idx=1&sn=8b6ebecbe80c1c72317948494f87b489&chksm=ebfa82e3dc8d0bf595d039e75b446e14ab96bf63cf8ffc5d553b58248dde3424fb18e6947440&token=525430415&lang=zh_CN&scene=21#wechat_redirect)

---

文章来源：网络安全威胁和漏洞信息共享平台

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