---
title: 飞牛OS多个重大漏洞已被多团伙广泛利用，升级到最新版本无法确保安全
url: https://blog.upx8.com/%E9%A3%9E%E7%89%9BOS%E5%A4%9A%E4%B8%AA%E9%87%8D%E5%A4%A7%E6%BC%8F%E6%B4%9E%E5%B7%B2%E8%A2%AB%E5%A4%9A%E5%9B%A2%E4%BC%99%E5%B9%BF%E6%B3%9B%E5%88%A9%E7%94%A8-%E5%8D%87%E7%BA%A7%E5%88%B0%E6%9C%80%E6%96%B0%E7%89%88%E6%9C%AC%E6%97%A0%E6%B3%95%E7%A1%AE%E4%BF%9D%E5%AE%89%E5%85%A8
source: 黑海洋Wiki | Web开发工具包 | 网络安全攻防实战 | 区块链技术文档教程 - 免费资源平台
date: 2026-01-31
fetch_date: 2026-02-01T04:26:38.010922
---

# 飞牛OS多个重大漏洞已被多团伙广泛利用，升级到最新版本无法确保安全

# [黑海洋 | Wiki](/ "黑海洋Wiki | Web开发工具包 | 网络安全攻防实战 | 区块链技术文档教程 - 免费资源平台 - 点击返回首页")

# 飞牛OS多个重大漏洞已被多团伙广泛利用，升级到最新版本无法确保安全

发布时间:
2026-01-31 New Article

分类:
[新闻简报/News](https://blog.upx8.com/news)

热度:
4046

本次针对 fnOS 的漏洞利用活动呈现多团伙、多基础设施特征：疑似存在 2–3 个利用团伙，攻击流程较为成熟，并观察到多个 C2（命令与控制）域名用于回连与任务下发。当前已明确捕捉到 DDoS 攻击指令，被入侵设备存在被纳入僵尸网络风险。根据网络空间测绘（网站空间）统计，全网可直接访问并暴露 fnOS Web 页面设备约 306,766 台。最早入侵记录可追溯到12天前（1月21日）。

现在可验证的国内流量已经到达了1TB。

研究发现了更多可被犯罪组织利用的飞牛OS重大漏洞：包括一个路径遍历漏洞、一个websocket鉴权漏洞。

当前用户最可靠的安全措施之一是立即物理切断Web 管理面板与公网的访问连接。“升级到新版本”并不等于风险解除。目前无法确认新版本已覆盖全部修复点，仅依赖升级不能作为安全保证；在 Web 仍暴露公网的情况下仍可能被再次利用或二次入侵。

已被感染的用户应立即关闭公网访问，撤销端口映射/公网反代/暴露端口；仅允许内网访问，或使用 VPN/零信任网关进入内网后访问管理面；在网关处限制来源 IP（最小化暴露面）。之后在断网环境下清除与排查。

—— [DNSPODT](https://blog.upx8.com/go/aHR0cHM6Ly90Lm1lL0ROU1BPRFQvMTMwNDQ) （含处置详情）

[取消回复](https://blog.upx8.com/%E9%A3%9E%E7%89%9BOS%E5%A4%9A%E4%B8%AA%E9%87%8D%E5%A4%A7%E6%BC%8F%E6%B4%9E%E5%B7%B2%E8%A2%AB%E5%A4%9A%E5%9B%A2%E4%BC%99%E5%B9%BF%E6%B3%9B%E5%88%A9%E7%94%A8-%E5%8D%87%E7%BA%A7%E5%88%B0%E6%9C%80%E6%96%B0%E7%89%88%E6%9C%AC%E6%97%A0%E6%B3%95%E7%A1%AE%E4%BF%9D%E5%AE%89%E5%85%A8#respond-post-5627)

### 在下方留下您的评论.[加入TG群](https://t.me/).[打赏🍗](/reward.html)

提交评论

* [Post](/author/1)
* [Link](/links.html)
* [工具](https://tools.upx8.com/)
* [关于](/about.html)
* [文库](/WooyunDrops)

[![](/usr/uploads/ypyun.png)](https://www.upyun.com/?utm_source=lianmeng&utm_medium=referral "赞助商")
Copyright © 2026 黑海洋. All rights reserved. [看雪赞助](https://www.kanxue.com/ "看雪学院赞助")

[浙ICP备2021040518号](http://beian.miit.gov.cn "浙ICP备2021040518号")