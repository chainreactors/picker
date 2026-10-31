---
title: 群晖 NAS 勒索事件引热议：你的公网入口，谁在把关？
url: https://mp.weixin.qq.com/s/vcW_RhXxZcorXyUIclaq3w
source: Doonsec's feed
date: 2026-10-30
fetch_date: 2026-10-31T07:43:30.998833
---

# 群晖 NAS 勒索事件引热议：你的公网入口，谁在把关？

# 群晖 NAS 勒索事件引热议：你的公网入口，谁在把关？

网络防护选雷池
网络防护选雷池

雷池SafeLine

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

继此前的 PHP （[PHP 高危漏洞，雷池率先发布应对规则](https://mp.weixin.qq.com/s?__biz=Mzg4MjgyNDIzOA==&mid=2247513490&idx=1&sn=de7747c4d5aff7828597a67e981d3c54&scene=21#wechat_redirect)）漏洞话题之后，这两天，群晖 NAS 勒索事件又在雷池社群里引发了讨论。

![社群讨论：雷池 WAF 能防吗？](https://mmbiz.qpic.cn/sz_mmbiz_png/o2rSpTXlXYkia7Zt3JrHnVpCBibUTMDItCU7ro9lxCNibvk9ibufYFaicjrUkFnoO0rZsN43nD6KXsicLgk30rAhbrDfGtNB2It9rtNmtTryPzbjk/640?wx_fmt=png&from=appmsg)

![社群讨论：怎么防？](https://mmbiz.qpic.cn/mmbiz_png/o2rSpTXlXYl3fDfTmIOJwjmF5X6SXiaTghuWFfl3ckeZicR7ay5qADS8Fk1fIXftNeOcd7K8Ams6mWCXZLQ2ZohftN9MAw044p7t9ebZTejS8/640?wx_fmt=png&from=appmsg)

![社群讨论：NAS 公网访问与防护配置](https://mmbiz.qpic.cn/mmbiz_png/o2rSpTXlXYnzgHFa1ibzCpjyVgSqaX8tHKzibe5y9oTuxlHbHC4bEZrOehSaAyVf1YjD6ZeLmSiaS8G9ZWFsRL7iaeVtOnFt7e6liaicjrTRPekzU/640?wx_fmt=png&from=appmsg)

补丁早就有了。没升上去的群晖，这周正在被加密。

这几天大量群晖 NAS 中了 C3RB3R，文件被改成 `.L0CK3D`。群晖 10 月 29 日已经确认：打的是 2024 年 12 月就修好的远程代码执行漏洞 CVE-2024-10441，目标就是还在跑旧 DSM 的设备。安全厂商同时指向今年 9 月公开的 CVE-2026-13639、CVE-2026-13684，都是 CVSS 9.8、未登录即可读写任意文件。补丁在 9 月 18 日就发了，一个多月后还在被当 1day 打。不是没有补丁，是补丁没装上。

![群晖官方公告](https://mmbiz.qpic.cn/mmbiz_png/o2rSpTXlXYmBnarhiclWSJR3kWWgsVibOWricYs7JkBvvOtkXU0hu6Yv55Pb28I8xibzPsnVs5qXuTmR8cnKQVyRJM2CY2pVvhn5sMNia8dxCldY/640?wx_fmt=png&from=appmsg)

图源：群晖官方公告，2026 年 10 月 29 日。

尚未完成安全更新的设备，需要尽快核对修复状态，并尽快通过官方更新通道完成升级更新。管理口 5000/5001 是否直接映射到公网，也值得马上检查。对于暂时无法升级的设备，应优先收紧外部访问，并根据设备型号和 DSM 版本确认适用的安全更新。

DSM 的管理面就是一个网站。所有接口都进 `/webapi/entry.cgi`，群晖自己没有 Web 层防护。利用请求只要打到这个入口，WAF 可以在它碰到 NAS 之前丢掉。

**不同来源对攻击入口的描述存在差异，不能把所有案例归为同一个漏洞。但已知漏洞已有补丁，仍值得每一位 NAS 用户立即检查。**

除了补丁，还要检查访问入口和备份

NAS 的风险排查不能只看版本号，还要看哪些服务能被外部直接访问：

* **收回非必要的公网入口。**

  检查 5000/5001 管理端口、SSH、端口映射、IPv6 和穿透服务。远程管理优先通过 VPN，并限制访问来源。
* **检查账号安全。**

  排查异常登录、陌生账号及权限变更，启用多因素认证。账号保护与漏洞修复需要同时做好。
* **验证备份可恢复。**

  保留离线或不可变备份，并实际测试恢复流程，避免备份与原始数据一起受到影响。
* **为必须开放的 Web 服务增加防护。**

  接入雷池等 WAF 时，同时限制源站直连，确保请求经过检测；WAF 是补充防线，不能替代补丁和备份。

雷池社区这两天已经拦住了对 `entry.cgi` 的命令注入探测：同一个来源，443 和 5001 一起打。根据目前提供的社区反馈，已有用户在雷池中看到针对 `/webapi/entry.cgi` 的命令注入请求被拦截。

![社群用户分享拦截反馈](https://mmbiz.qpic.cn/mmbiz_png/o2rSpTXlXYmgej48up8BobFv3uPC8AYPRdr4v8uIDfRA2kYgv9d4SHJeyjRSaO5MAic2eYp5nX9wVArtgz8pfYjicfiaHlqm8gYrZ8BBF5I8cc/640?wx_fmt=png&from=appmsg)

![雷池拦截记录](https://mmbiz.qpic.cn/mmbiz_png/o2rSpTXlXYnibDP9dfKicSc7W7HZ9T08h7DlTzlPpUZmZibyic8SdFcotbhbARIsEGORa2JBCunPZIs8BLbvfucxDhR2qZtuU7sj9n2xZAh61BA/640?wx_fmt=png&from=appmsg)

这类记录说明雷池对相关 Web 攻击请求进行了检测和拦截，**尚不能据此认定请求属于本轮勒索攻击，或证明雷池能够阻断其完整攻击链。**

雷池 SafeLine 社区版可以为接入的 HTTP/HTTPS 服务提供补充防护。对于确需保留的 Web 入口，可以结合访问控制部署使用；暂时无法升级的设备，则应先收紧访问，再补充防护措施。

雷池专业版试用

希望进一步体验雷池功能的用户，可通过官方版本页申请专业版试用，体验加强 Web 攻击防护、流量统计分析等能力。

欢迎加入雷池交流群，交流 NAS Web 服务接入、防护配置和日常运维经验。

![雷池社群二维码](https://mmbiz.qpic.cn/sz_mmbiz_png/o2rSpTXlXYkOIp8m5O6GaCxKCLs5ucOjYgFzYj9HNJ4HgCicrUg4qAqkwOxMTibfkzIPXCuS3xmeNJssHxN3egpedbj1w30ib7aelRSgjce4aw/640?wx_fmt=png&from=appmsg)

**长按识别二维码，加入雷池交流群。**

预览时标签不可点

阅读原文

不喜欢

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/1HSdSibDdRfsPL7VnlPQV4QrV6ceaXHYc1PpFKEFBBCcvXOlt64ic82fY8cZyRxG8bBAdpMiaOZ13kUlSYgpM2lgw/0?wx_fmt=png)

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