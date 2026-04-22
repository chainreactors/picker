---
title: 网络攻击助推物流行业货物盗窃激增
url: https://mp.weixin.qq.com/s/TqKqrvaaxkzCeea9ZlC8SA
source: Doonsec's feed
date: 2026-04-21
fetch_date: 2026-04-22T04:42:05.927254
---

# 网络攻击助推物流行业货物盗窃激增

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/icBE3OpK1IX0ODjaAKRibjRRJhHz7gCc5rPfVzqOznXllTHISg9B7OYhVILnAOMgBaXW32xiaOBWKaKKe9oNWnnDq5MYDDoojyicNND9RaIGEVM/0?wx_fmt=jpeg)

# 网络攻击助推物流行业货物盗窃激增

FreeBuf

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

![](https://mmbiz.qpic.cn/mmbiz_gif/qq5rfBadR38jUokdlWSNlAjmEsO1rzv3srXShFRuTKBGDwkj4gvYy34iajd6zQiaKl77Wsy9mjC0xBCRg0YgDIWg/640?wx_fmt=gif)

## ![](https://mmbiz.qpic.cn/sz_mmbiz_png/icBE3OpK1IX0r9FkPKiadYf0NrlqqnXcjrmLOJCefG8xwMMVUpzE6k7Gibics3kcgpcrVoK7hUwuJlh3Ln41QnLHM3IghRib3GfeB1ye2ArmbQtk/640?wx_fmt=png&from=appmsg)

##

**Part01**

## ****黑客渗透物流企业窃取货物转移资金****

Proofpoint研究人员发现，犯罪分子针对卡车运输和物流公司发起协同远程访问攻击，窃取货物并转移资金。这些攻击似乎与有组织犯罪有关。

研究结果凸显了网络助力的货物盗窃呈上升趋势，数字入侵直接支持现实世界的犯罪活动。这种威胁正在迅速扩大，2025年北美地区损失达66亿美元，显示出网络攻击正越来越多地被用于破坏供应链并牟利。

Proofpoint在报告中指出："2026年2月下旬，Proofpoint研究人员在我们合作伙伴Deception.pro运营的受控诱饵环境中，执行了针对运输机构的威胁攻击者投放的恶意载荷。虽然该环境并非真实的运输载体，但仍持续被入侵超过一个月——这为入侵后的操作、工具使用和决策过程提供了罕见的长期可见性。"

**Part02**

## ****攻击手法与攻击链****

2025年11月，Proofpoint首次报告网络犯罪分子使用RMM工具（远程监控和管理软件）针对卡车运输和物流公司窃取货物。该组织自2025年6月开始活跃，与有组织犯罪合作掠夺货物，主要是食品和饮料。

犯罪分子渗透物流公司，劫持货物投标并窃取商品，推动了网络助力货运盗窃的增长。2026年2月27日，攻击者入侵货运平台并向承运商发送虚假运输工作的电子邮件。

![](https://mmbiz.qpic.cn/mmbiz_png/icBE3OpK1IX2a5UCD828eJNq6jcVQ4sxEsibf5plpUDOVyn193bhZoIDaok3xLFMkaNjEx1Bcqt7gLG5Cib4bNZwnpfn6nUvaGQsfN5QO8JckI/640?wx_fmt=png&from=appmsg)

邮件投递的恶意VBS文件会启动PowerShell脚本，安装ScreenConnect实现远程访问，并显示虚假协议以掩盖攻击行为。获得访问权限后，攻击者通过安装多个远程管理工具确保持久性。一个月内，他们部署了多个ScreenConnect实例以及Pulseway和SimpleHelp，即使某个工具被检测或删除也能保持持续访问。

**Part03**

## ****新型规避技术****

研究人员报告称，攻击者使用新型"签名即服务"方法部署隐蔽的ScreenConnect实例。PowerShell链绕过控制措施，下载安装程序，使用欺诈性但有效的证书重新签名，然后静默安装。它还使用签名版本替换原始组件以避免检测，绕过已撤销的证书，并保持持久、可信的远程访问。

获得稳定访问后，攻击者转向手动操作。他们手动检查PayPal等账户，并运行自定义工具查找和窃取加密货币钱包数据，将结果发送至Telegram。他们使用十几个PowerShell脚本分析受害者，收集用户数据、浏览器历史记录以及访问银行、支付、物流和会计平台的迹象。脚本复制锁定文件，搜索有价值的服务，将数据存储在隐藏文件夹中，并以SYSTEM权限运行。

**Part04**

## ****目标与最终阶段****

攻击者持续扫描浏览器数据库，匹配模式并通过Telegram报告发现，有时使用延迟任务来规避控制。目标包括银行、汇款服务、车队支付系统和货运平台——显示出对金融欺诈和货物盗窃的明确关注。

在最后阶段，另一个脚本悄悄收集系统详细信息，检查安全工具和金融应用程序，并通过现有远程会话将结果发回而不触发警报。此次入侵表明，以经济利益为动机的攻击者远不止于初始访问。他们专注于保持隐蔽、收集情报和窃取凭证以利用支付系统和物流平台——这种行为也与货运盗窃和货物转移准备相一致。

报告总结道："值得注意的是，'签名即服务'能力的使用突显了攻击者越来越多地利用合法信任机制来逃避检测的趋势。对于运输、物流和货运组织而言，这些发现强化了监控未经授权的远程管理工具、可疑PowerShell活动以及与金融平台访问相关的异常浏览器遥测的重要性。"

**参考来源：**

Cyber attacks fuel surge in cargo theft across logistics industry

https://securityaffairs.com/191008/security/cyber-attacks-fuel-surge-in-cargo-theft-across-logistics-industry.html

---

**推荐阅读**

[![](https://mmbiz.qpic.cn/sz_mmbiz_png/icBE3OpK1IX1NlibR8DpnkZguk1so3ThwkXScRIP7SKicZdaVeLa1eMHdfLgFsOaFCP6qt2JaDlnDPzLe5MJBV1micoP6YM0SG5C9X1ibsshUiccM/640?wx_fmt=png&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MjM5NjA0NjgyMA==&mid=2651337140&idx=1&sn=134af642d92b85fc1076a8c83c09945c&scene=21#wechat_redirect)

### **电报讨论**![](https://mmbiz.qpic.cn/mmbiz_png/icBE3OpK1IX1bKq2xLKwFuy1Yl63ibm7kJUCW7hP4uRIhllVu6icLPkYcerZIx5264cbnPu5uCLCpb0ic16Gm32GC3B6ou34yFia9Nm4YJTGU4iag/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/qq5rfBadR3ibvNluUKZ6RPy7h2fbYibRbLQDHPFqj89KkFsXBRibx5YTLiaTUfFOy9PKicps3l56iazUPNQrwdhkZ7jA/640?wx_fmt=png&from=appmsg)

**![](https://mmbiz.qpic.cn/mmbiz_png/qq5rfBadR3ibqyrdrvYXibMZM7K7gQW9ymeNepaIkpwPmicPSSoVicLBPXZ3a19uvVicYOjUZOibNeYRbrIOToCHjLAg/640?wx_fmt=png&from=appmsg)**

预览时标签不可点

阅读原文

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/qq5rfBadR3ibLOEAnkkKa2dHtqcjZ55KLsqibib6n4UDNUhLIuMRdAJ9ibfZkSK5LViaGJLEQN7p9OGo7mNnVv3EmkQ/0?wx_fmt=png)

FreeBuf

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/qq5rfBadR3ibLOEAnkkKa2dHtqcjZ55KLsqibib6n4UDNUhLIuMRdAJ9ibfZkSK5LViaGJLEQN7p9OGo7mNnVv3EmkQ/0?wx_fmt=png)

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