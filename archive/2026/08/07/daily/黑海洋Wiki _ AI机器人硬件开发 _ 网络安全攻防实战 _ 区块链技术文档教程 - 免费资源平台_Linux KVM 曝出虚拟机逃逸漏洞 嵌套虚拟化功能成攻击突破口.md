---
title: Linux KVM 曝出虚拟机逃逸漏洞 嵌套虚拟化功能成攻击突破口
url: https://blog.upx8.com/Linux-KVM-%E6%9B%9D%E5%87%BA%E8%99%9A%E6%8B%9F%E6%9C%BA%E9%80%83%E9%80%B8%E6%BC%8F%E6%B4%9E-%E5%B5%8C%E5%A5%97%E8%99%9A%E6%8B%9F%E5%8C%96%E5%8A%9F%E8%83%BD%E6%88%90%E6%94%BB%E5%87%BB%E7%AA%81%E7%A0%B4%E5%8F%A3
source: 黑海洋Wiki | AI机器人硬件开发 | 网络安全攻防实战 | 区块链技术文档教程 - 免费资源平台
date: 2026-08-07
fetch_date: 2026-08-08T03:23:51.818343
---

# Linux KVM 曝出虚拟机逃逸漏洞 嵌套虚拟化功能成攻击突破口

# [黑海洋 | Wiki](/ "黑海洋Wiki | AI机器人硬件开发 | 网络安全攻防实战 | 区块链技术文档教程 - 免费资源平台 - 点击返回首页")

# Linux KVM 曝出虚拟机逃逸漏洞 嵌套虚拟化功能成攻击突破口

发布时间:
2026-08-07 New Article

分类:
[新闻简报/News](https://blog.upx8.com/news)

热度:
2764

近日，Linux KVM/x86 shadow MMU 曝光严重的虚拟机逃逸漏洞（CVE-2026-64561，PoC 名称：Zapscape），攻击者借此可实现 KVM 虚拟机逃逸与宿主机内核代码执行。该漏洞潜伏于 KVM/x86 的 shadow MMU 页回收逻辑中，攻击者可利用其实现**虚拟机逃逸**，并在宿主机（L0）内核空间中以最高权限执行任意代码。

**核心原理与受影响范围**

> • 影响版本： 涵盖从 f95eec9bed76 (2020-07-08) 到 2abd5287f083 (2026-07-21) 的内核范围。主要威胁向不受信任租户开放嵌套虚拟化（nested virtualization）的 KVM/x86 云计算宿主机，以及低权限用户可访问 /dev/kvm 的主机。

> • 漏洞原理： 修复前，失效检查发生在回收之前；若回收使 root 失效，后续 fetch 仍会在该 root 下创建映射，破坏 invalid page 不得位于 active list 的约束。攻击者借此形成 use-after-free，最终通过 usermode helper 以 L0 内核凭据执行系统命令。

**处置建议**

> • 优先升级： 升级至包含 2abd5287f083 或对应 stable backport 的内核，并重启宿主机。

> • 临时防范： 无法立即升级时，关闭不必要的 KVM nested virtualization；收紧 /dev/kvm 权限，禁止无业务需要的低权限用户创建虚拟机。

—— [V4bel GitHub](https://blog.upx8.com/go/aHR0cHM6Ly9naXRodWIuY29tL1Y0YmVsL1phcHNjYXBl) , [LoopDNS](https://blog.upx8.com/go/aHR0cHM6Ly90Lm1lL0ROU1BPRFQvMTQ1Nzg)

[取消回复](https://blog.upx8.com/Linux-KVM-%E6%9B%9D%E5%87%BA%E8%99%9A%E6%8B%9F%E6%9C%BA%E9%80%83%E9%80%B8%E6%BC%8F%E6%B4%9E-%E5%B5%8C%E5%A5%97%E8%99%9A%E6%8B%9F%E5%8C%96%E5%8A%9F%E8%83%BD%E6%88%90%E6%94%BB%E5%87%BB%E7%AA%81%E7%A0%B4%E5%8F%A3#respond-post-9970)

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