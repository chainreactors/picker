---
title: CloudFlare 完全禁用缓存
url: https://blog.upx8.com/3249
source: 黑海洋 - WIKI
date: 2023-03-02
fetch_date: 2025-10-04T08:27:12.334396
---

# CloudFlare 完全禁用缓存

# [黑海洋 - Wiki](/ "黑海洋 - Wiki - 点击返回首页")

# CloudFlare 完全禁用缓存

发布时间:
2023-03-01

分类:
[Web开发/Code](https://blog.upx8.com/code/)

热度:
20231

[CloudFlare](https://blog.upx8.com/go/aHR0cHM6Ly9kYXNoLmNsb3VkZmxhcmUuY29t) 的缓存可以提高网站的访问速度，但有时也会带来一些管理上的麻烦。好在，CloudFlare 允许禁用缓存。

[CloudFlare](https://blog.upx8.com/go/aHR0cHM6Ly9kYXNoLmNsb3VkZmxhcmUuY29t) CF没有直接的配置项可以禁用缓存，但它提供了缓存规则。

添加两条规则，都选择 缓存等级，值为 绕过.

操作流程：

```
选择左侧 - 规则 - 页面规则 - 创建页面规则 输入 upx8.com/* - 则设置将为：缓存级别 - 选择缓存级别：绕过 - 保存和部署页面规则 - 搞定
```

最后不要忘了在CloudFlare面板中，清除所有缓存。

这样就禁用了你整个网站的缓存了。

CloudFlare相关文献：[https://bbs.yun.rip/f/10.html](https://blog.upx8.com/go/aHR0cHM6Ly9iYnMueXVuLnJpcC9mLzEwLmh0bWw)

[取消回复](https://blog.upx8.com/3249#respond-post-3249)

### 在下方留下您的评论.[加入TG群](https://t.me/).[打赏🍗](/reward.html)

提交评论

* [Post](/author/1)
* [Link](/links.html)
* [工具](https://tools.upx8.com/)
* [关于](/about.html)
* [文库](/WooyunDrops)

[![](/usr/uploads/ypyun.png)](https://www.upyun.com/?utm_source=lianmeng&utm_medium=referral "赞助商")
Copyright © 2024 黑海洋. All rights reserved.
[看雪赞助](https://www.kanxue.com/ "看雪学院赞助")

[浙ICP备2021040518号](http://beian.miit.gov.cn "浙ICP备2021040518号") [Sitemap](sitemap.xml?type=index "Sitemap")