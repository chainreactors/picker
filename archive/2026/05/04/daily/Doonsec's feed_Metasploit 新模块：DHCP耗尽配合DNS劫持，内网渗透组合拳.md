---
title: Metasploit 新模块：DHCP耗尽配合DNS劫持，内网渗透组合拳
url: https://mp.weixin.qq.com/s/a5YFSn-Gy6pqgmzSg4pePQ
source: Doonsec's feed
date: 2026-05-04
fetch_date: 2026-05-05T05:01:51.947721
---

# Metasploit 新模块：DHCP耗尽配合DNS劫持，内网渗透组合拳

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/nGzNudUIJ6MwUsDNMkzx9y10U9XSLHibBHwiaiabZrbwONaELUNA3MXynN7tpQCGSgxPBs1LecFeeJNkMJhUPXY0CvrzFNePVXyNxY4QFGjE4Q/0?wx_fmt=jpeg)

# Metasploit 新模块：DHCP耗尽配合DNS劫持，内网渗透组合拳

原创

A译
A译

黑白之道

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

> **导语**：在内部网络搞事情，先拿到网络控制权。DHCP耗尽配合DNS中间人，这套组合拳能让整个子网的流量都经过你的"过滤器"。现在 Metasploit 把这两个攻击做成了现成的模块。

---

攻击场景是这样的：正常状态下，客户端从 DHCP 服务器获取 IP，通过真实 DNS 解析访问目标。攻击后，客户端从攻击者（伪 DHCP）获取 IP，DNS 请求被劫持到攻击者指定的地址，流向钓鱼页面或被监控。

攻击链的逻辑很简单：先通过 DHCP 耗尽让合法 DHCP 服务器无地址可分，然后"替补"成为新的 DHCP 服务器，把攻击者控制的 DNS 服务器地址一并"推销"给受害者。

![DHCP耗尽+DNS劫持攻击示意图](https://mmbiz.qpic.cn/sz_mmbiz_png/nGzNudUIJ6PocK8icAC1Y9v2k40Xd3AiaLJN9IQe5H0ibjIApFx0m0w51N8oonypHnoH8QJd0TjYeFs6ZaXrF9YWmrI06WoZJCtIVZcD9xkX08/640?wx_fmt=png "DHCP耗尽+DNS劫持攻击示意图")

有兩個模塊配合使用。DHCP耗尽模块（`auxiliary/digininja/dhcp_exhaustion/exhaust`）持续发送 DHCP REQUEST 申请新地址，直到服务器不再响应——这意味着地址池已经耗尽。使用前提是需要将网卡置为混杂模式，才能监听到所有的 DHCP OFFER 和 ACK。DNS中间人模块（`auxiliary/digininja/dns_mitm/dns_mitm`）加载一个 hosts 文件，文件中存在的域名返回伪造 IP，其他域名转发给真实 DNS 处理。

有个很实用的特性：支持热重载 hosts 文件。在 hosts 文件中加入特殊条目 `digininja.reload`，然后查询这个域名，模块会自动重新加载 hosts 文件，无需重启模块。

这个攻击动静不小——DHCP 耗尽会导致子网内设备陆续断网，容易被发现。实际红队通常不会一次性耗尽所有地址，而是维持"慢性缺氧"状态，或者分时段攻击在非工作时间进行。也可以只劫持特定域名减少对业务的影响，降低被发现概率。

防御方面，交换机启用 DHCP Snooping 可以忽略非授权 DHCP 响应；端口安全限制每个端口分配的 IP 数量；ARP 检测启用动态 ARP 检测（DAI）；流量监控关注异常的 DHCP 请求频率。

对于渗透测试工程师，这是快速获取网络控制权的有效手段；对于防御者，理解攻击原理才能更好地设计防护方案。最好的防御是理解攻击。

**版权声明**：本文由华盟网原创发布，保留所有权利。配图由华盟网授权使用。

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/3xxicXNlTXLicpdp8GZxicJpcFIZglvakzYRZiaqt6W61hfgibjeymOgiaGqRsgNvgWIacMj7Gk4PIZ4o2NtW1zb9P6Q/0?wx_fmt=png)

黑白之道

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/3xxicXNlTXLicpdp8GZxicJpcFIZglvakzYRZiaqt6W61hfgibjeymOgiaGqRsgNvgWIacMj7Gk4PIZ4o2NtW1zb9P6Q/0?wx_fmt=png)

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