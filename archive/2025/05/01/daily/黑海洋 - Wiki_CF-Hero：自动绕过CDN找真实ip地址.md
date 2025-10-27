---
title: CF-Hero：自动绕过CDN找真实ip地址
url: https://blog.upx8.com/4781
source: 黑海洋 - Wiki
date: 2025-05-01
fetch_date: 2025-10-06T22:27:38.057878
---

# CF-Hero：自动绕过CDN找真实ip地址

# [黑海洋 - Wiki](/ "黑海洋 - Wiki - 点击返回首页")

# CF-Hero：自动绕过CDN找真实ip地址

发布时间:
2025-04-30

分类:
[系统安全/os\_security](https://blog.upx8.com/os_security/)

热度:
67034

CF-Hero 是一个全面的侦察工具，用于发现受 Cloudflare 保护的 Web 应用程序的真实 IP 地址。它通过各种方法执行多源情报收集。

目前仅支持Cloudflare的cdn服务查找真实ip，但从原理上来说查找方法都是通用的，所以非Cloudflare cdn服务也可以尝试使用此工具查找ip。

### **CF-Hero 工具核心功能**

1. **目标**
   绕过 Cloudflare CDN 保护，发现目标网站的真实 IP 地址（也可尝试用于其他 CDN 服务）。
2. **支持的方法**

   * **DNS 侦查**
     + 当前 DNS 记录（A、TXT 等）
     + 历史 DNS 数据（通过 SecurityTrails 等平台）
     + 关联域名分析（如子域名、同一注册者的其他域名）
   * **多源情报收集**
     + 主动 DNS 枚举（如暴力破解子域名）
     + 搜索引擎扫描（Censys、Shodan）
     + 历史记录分析（SecurityTrails 的 IP/域名变更记录）
3. **适用场景**

   * 渗透测试中识别 Cloudflare 背后的真实服务器。
   * 研究 CDN 隐匿性时验证其安全性。

![](https://cdn.skyimg.net/up/2025/4/30/17e38297.webp)

![](https://cdn.skyimg.net/up/2025/4/30/41620e0c.webp)

### **技术原理补充**

* **为什么能绕过 Cloudflare？**
  Cloudflare 作为反向代理，隐藏了真实 IP，但以下情况可能导致泄露：

  + 管理员错误配置（如未全流量代理，某些服务直连真实 IP）。
  + 历史 DNS 记录未清理（通过 Wayback Machine 或 SecurityTrails 可查）。
  + 关联域名使用相同服务器但未启用 CDN。

* **非 Cloudflare CDN 的兼容性**

### **使用建议**

1. **合法授权**
2. **结合其他工具**
   * 配合 **Sublist3r**（子域名枚举）、**Amass**（网络测绘）提高覆盖率。
   * 手动验证 IP：通过 `curl -H "Host: target.com" http://<疑似IP>` 测试响应。
3. **防御建议（针对管理员）**
   * 严格配置 CDN（确保所有流量强制代理）。
   * 定期清理历史 DNS 记录。
   * 隔离关键服务（如 API、数据库）到独立 IP/网络。

### **项目地址与资源**

* GitHub: [musana/CF-Hero](https://blog.upx8.com/go/aHR0cHM6Ly9naXRodWIuY29tL211c2FuYS9DRi1IZXJv)
* 扩展阅读：[Shodan/Censys 高级查询语法](https://blog.upx8.com/go/aHR0cHM6Ly9oZWxwLnNob2Rhbi5pby8)

[取消回复](https://blog.upx8.com/4781#respond-post-4781)

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