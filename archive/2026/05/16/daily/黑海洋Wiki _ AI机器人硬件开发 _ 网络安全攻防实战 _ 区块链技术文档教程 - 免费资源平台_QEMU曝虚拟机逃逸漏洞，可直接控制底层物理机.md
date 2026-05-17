---
title: QEMU曝虚拟机逃逸漏洞，可直接控制底层物理机
url: https://blog.upx8.com/QEMU%E6%9B%9D%E8%99%9A%E6%8B%9F%E6%9C%BA%E9%80%83%E9%80%B8%E6%BC%8F%E6%B4%9E-%E5%8F%AF%E7%9B%B4%E6%8E%A5%E6%8E%A7%E5%88%B6%E5%BA%95%E5%B1%82%E7%89%A9%E7%90%86%E6%9C%BA
source: 黑海洋Wiki | AI机器人硬件开发 | 网络安全攻防实战 | 区块链技术文档教程 - 免费资源平台
date: 2026-05-16
fetch_date: 2026-05-17T05:47:45.071711
---

# QEMU曝虚拟机逃逸漏洞，可直接控制底层物理机

# [黑海洋 | Wiki](/ "黑海洋Wiki | AI机器人硬件开发 | 网络安全攻防实战 | 区块链技术文档教程 - 免费资源平台 - 点击返回首页")

# QEMU曝虚拟机逃逸漏洞，可直接控制底层物理机

发布时间:
2026-05-16 New Article

分类:
[新闻简报/News](https://blog.upx8.com/news)

热度:
2519

QEMU CXL Type-3 设备仿真模块被曝出名为“QEMUtiny”的漏洞链。具备 Guest 系统 Root 权限的攻击者，可利用该漏洞实现虚拟机逃逸，获取宿主机进程甚至宿主机 Root 权限，风险较高（暂无 CVE 编号）。
**漏洞原理**
该漏洞链源于 CXL mailbox 逻辑（hw/cxl/cxl-mailbox-utils.c）中的两个致命缺陷：
1. **越界读（GET\_LOG）**：指针运算错误，导致泄露宿主机内存地址。
2. **越界写（SET\_FEATURE）**：边界检查缺失，允许破坏设备对象字段，进而劫持程序执行流。
**影响范围**
仅影响**启用了 CXL 支持**（启动参数含 cxl=on、cxl-type3等）且向 Guest 暴露了该设备的 QEMU 实例。普通 QEMU 虚拟机及物理 CXL 硬件不受影响。
**安全建议**
1. **排查参数**：检查 QEMU 启动配置，移除不必要的 CXL 相关参数。
2. **切断暴露**：严禁向不可信的 Guest 虚拟机暴露 CXL Type-3 设备。
3. **隔离降险**：临时禁用该仿真功能，或仅在严格隔离的测试环境中使用。

—— [LoopDNS](https://blog.upx8.com/go/aHR0cHM6Ly90Lm1lL0ROU1BPRFQvMTM4ODQ) 、 [GitHub](https://blog.upx8.com/go/aHR0cHM6Ly9naXRodWIuY29tL3YxMi1zZWN1cml0eS9wb2NzL3RyZWUvbWFpbi9xZW11)

[取消回复](https://blog.upx8.com/QEMU%E6%9B%9D%E8%99%9A%E6%8B%9F%E6%9C%BA%E9%80%83%E9%80%B8%E6%BC%8F%E6%B4%9E-%E5%8F%AF%E7%9B%B4%E6%8E%A5%E6%8E%A7%E5%88%B6%E5%BA%95%E5%B1%82%E7%89%A9%E7%90%86%E6%9C%BA#respond-post-8175)

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