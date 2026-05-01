---
title: Linux内核曝漏洞：可使黑客攻破所有主流Linux发行版获取Root权限
url: https://blog.upx8.com/Linux%E5%86%85%E6%A0%B8%E6%9B%9D%E6%BC%8F%E6%B4%9E-%E5%8F%AF%E4%BD%BF%E9%BB%91%E5%AE%A2%E6%94%BB%E7%A0%B4%E6%89%80%E6%9C%89%E4%B8%BB%E6%B5%81Linux%E5%8F%91%E8%A1%8C%E7%89%88%E8%8E%B7%E5%8F%96Root%E6%9D%83%E9%99%90
source: 黑海洋Wiki | AI机器人硬件开发 | 网络安全攻防实战 | 区块链技术文档教程 - 免费资源平台
date: 2026-04-30
fetch_date: 2026-05-01T05:38:28.337461
---

# Linux内核曝漏洞：可使黑客攻破所有主流Linux发行版获取Root权限

# [黑海洋 | Wiki](/ "黑海洋Wiki | AI机器人硬件开发 | 网络安全攻防实战 | 区块链技术文档教程 - 免费资源平台 - 点击返回首页")

# Linux内核曝漏洞：可使黑客攻破所有主流Linux发行版获取Root权限

发布时间:
2026-04-30 New Article

分类:
[新闻简报/News](https://blog.upx8.com/news)

热度:
2489

Linux内核中发现了一个名为“Copy Fail”（CVE-2026-31431）的逻辑漏洞，该漏洞位于authencesn加密模板中。它允许非特权本地用户在无需竞态条件或重试的情况下，对任何可读文件的页缓存执行确定性的4字节写入。一个732字节的Python脚本即可修改setuid二进制文件，从而在包括Ubuntu、Amazon Linux、RHEL和SUSE在内的几乎所有主流Linux发行版上获取root权限。由于仅修改内存中的页缓存，因此硬盘上的文件保持不变，难以被常规文件完整性工具检测。此漏洞还可穿透容器边界。其根本原因是AF\_ALG与splice()结合，将页缓存页置于可写散列列表中，并被authencesn的越界写入利用。修复方案是撤销2017年引入的in-place优化。

—— [xint.io](https://blog.upx8.com/go/aHR0cHM6Ly94aW50LmlvL2Jsb2cvY29weS1mYWlsLWxpbnV4LWRpc3RyaWJ1dGlvbnM)

[取消回复](https://blog.upx8.com/Linux%E5%86%85%E6%A0%B8%E6%9B%9D%E6%BC%8F%E6%B4%9E-%E5%8F%AF%E4%BD%BF%E9%BB%91%E5%AE%A2%E6%94%BB%E7%A0%B4%E6%89%80%E6%9C%89%E4%B8%BB%E6%B5%81Linux%E5%8F%91%E8%A1%8C%E7%89%88%E8%8E%B7%E5%8F%96Root%E6%9D%83%E9%99%90#respond-post-7816)

### 在下方留下您的评论.[加入TG群](https://t.me/).[打赏🍗](/reward.html)

提交评论

* [All](/all.html)
* [Link](/links.html)
* [工具](https://tools.upx8.com/)
* [便签](https://txt.upx8.com)
* [关于](/about.html)

[![又拍云赞助商](/usr/uploads/ypyun.png)](https://www.upyun.com/?utm_source=lianmeng&utm_medium=referral "赞助商")
Copyright © 2026 黑海洋. All rights reserved. [看雪赞助](https://www.kanxue.com/ "看雪学院赞助")

[浙ICP备2021040518号](http://beian.miit.gov.cn "浙ICP备2021040518号")