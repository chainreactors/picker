---
title: Host碰撞红队实战工具 -- hoststrike（3月27更新）
url: https://mp.weixin.qq.com/s/2WLsgTX0cCVknXXbf8nPbw
source: Doonsec's feed
date: 2026-03-28
fetch_date: 2026-03-29T04:36:39.066317
---

# Host碰撞红队实战工具 -- hoststrike（3月27更新）

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/U7LDNXUGXQsAndhsHLILNAPibMvwP167Jv1ibfGexJW51skx7wXgG3FkKibfLbHhC8SV8gpW5PTNfE0tgVrkf3HTFEYKq1icDBmxM0ugFSCow6U/0?wx_fmt=jpeg)

# Host碰撞红队实战工具 -- hoststrike（3月27更新）

Zer08Bytes
Zer08Bytes

Web安全工具库

![]()

在小说阅读器中沉浸阅读

===================================

**免责声明**

请勿利用文章内的相关技术从事非法测试，由于传播、利用此文所提供的信息而造成的任何直接或者间接的后果及损失，均由使用者本人负责，作者不为此承担任何责任。工具来自网络，安全性自测，大家都要把工具当做病毒对待，在虚拟机运行。如有侵权请联系删除。个人微信：ivu123ivu

**0x01 工具介绍**

Host碰撞红队实战工具。

![](https://mmbiz.qpic.cn/mmbiz_png/U7LDNXUGXQvNK1E0kQIFRYQBb94obgmpZqJcysDRWkTY0tFWPyP9FEIvmhhzNvbrRldrgicjFyUtu2JjfKhlJ6gAOMZ5PrqJ2XBMfbQNxxGI/640?wx_fmt=png&from=appmsg)

**0x02 安装与使用**

没把Host碰撞做好，直接少了一半入口。.

| 序号 | 实战作用 | 具体说明 | 红队价值 |
| --- | --- | --- | --- |
| 1 | 发现隐藏资产 | 在已知 IP 上，通过不同 Host 头撞出未暴露的虚拟主机。 | 增加可攻击目标数量，找到未登记系统。 |
| 2 | 绕过 DNS/资产管理 | 即使域名未解析或未在资产平台登记，也能发现站点。 | 避开蓝队防守视野，获取“隐形入口”。 |
| 3 | 寻找低防护系统 | 通常是测试/开发/运维系统，未加 WAF 或弱口令。 | 快速获得易利用入口，提高效率。 |
| 4 | 初始访问点 | 提供登录后台、API 或管理界面等入口。 | 支撑后续漏洞利用、内网渗透、横向移动。 |
| 5 | 横向打点 | 扫描已掌握 IP，可发现内网或边界系统。 | 为红队建立内网拓扑，规划进一步渗透。 |
| 6 | 高价值资产识别 | 可直接找到 OA、CRM、Gitlab、Jenkins 等核心系统。 | 定位关键资产，提高攻击收益和演练效果。 |
| 7 | 攻击链关键环节 | 在信息收集 → 漏洞利用 → 内网渗透链中承上启下。 | 决定红队是否能打入关键系统，差异化效果明显。 |

Host 碰撞vs子域名爆破(实战强度对比)

| 对比维度 | 子域名爆破 | Host 碰撞 | 谁更强 & 为什么 |
| --- | --- | --- | --- |
| 发现能力 | 只能发现有 DNS 解析的域名 | 可发现无 DNS 的隐藏站点 | ✅ Host 碰撞更强（能打“隐形资产”） |
| 依赖条件 | 必须 DNS 存在 | 只需要 IP 可访问 | ✅ Host 碰撞更强（限制更少） |
| 目标范围 | 公网资产 | 公网 + 内网 + 未登记系统 | ✅ Host 碰撞覆盖更广 |
| 命中质量 | 多为正式站点（防护强） | 多为测试/后台系统（防护弱） | ✅ Host 碰撞更容易打进去 |
| 防御可见性 | 容易被 DNS 监控发现 | 很难被发现（HTTP 层伪装） | ✅ Host 碰撞更隐蔽 |
| 资产完整性 | 只能看到“被公开的” | 能看到“被隐藏的” | ✅ Host 碰撞信息更全 |
| 攻击价值 | 辅助收集 | 直接提供突破口 | ✅ Host 碰撞更偏“进攻” |

网盘下载链接（一定要在虚拟机运行）：

链接：https://pan.quark.cn/s/14f7261c5060

**·****今 日 推 荐****·**

|  |  |
| --- | --- |
| ![](https://mmbiz.qpic.cn/mmbiz_jpg/U7LDNXUGXQsQuAaHn1aZPtVsISCQEuxZia7HgYHBPJ2yZ4TI5v5mXyeCHRIyltlfQgfQMbp6MCnp59YldfqBlP4Sy2QUZwf6kM5xppPIFjfo/640?wx_fmt=jpeg&from=appmsg) | ![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/8H1dCzib3UibsC4yYFwgTnJrN0q57DearHJhaWSE6XQllpkUviaibg5MqTYgdUQYDNt8ysfV2v6o4jsN34pmq3DAOg/640?wx_fmt=jpeg&from=appmsg) |

![](https://mmbiz.qpic.cn/sz_mmbiz_png/U7LDNXUGXQubZVWBWQQtxvvuJKMSjurIKbOx1uqmgP1AIq0RWfwicRQuRzYAkjy4bia4JdGaqXOFwiaiat2affEjLJZu60icVMmN5ibM7ov33oCVU/640?wx_fmt=png&from=appmsg)

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/8H1dCzib3UibvAJDLSoAcyS63uxfNryXVibVJx8MiaiaibYmLj4Zk1fPdTYCsDjIEEoiaF1BPQydFZornyvv10iarEPCkg/0?wx_fmt=png)

Web安全工具库

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/8H1dCzib3UibvAJDLSoAcyS63uxfNryXVibVJx8MiaiaibYmLj4Zk1fPdTYCsDjIEEoiaF1BPQydFZornyvv10iarEPCkg/0?wx_fmt=png)

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