---
title: [技术深潜] 潜伏9年的Copy-Fail：内核0-Day通杀Root
url: https://mp.weixin.qq.com/s/VdVFHrfk9hVcBxIBzFc2KA
source: Doonsec's feed
date: 2026-05-02
fetch_date: 2026-05-03T05:22:40.262442
---

# [技术深潜] 潜伏9年的Copy-Fail：内核0-Day通杀Root

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/L7VicJKsiaibFABicQB2K3lypHblfkRbr4bxiaR7NbSofMFFw2SmvuvnicmZvdbkMuriaA68Z1tVhZiaAkkeXws3iaxZZ53f6ibmp4jwplaiaKdDuJqqvc/0?wx_fmt=jpeg)

# [技术深潜] 潜伏9年的Copy-Fail：内核0-Day通杀Root

原创

极客零零七
极客零零七

极客零零七

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

导语

还记得当年让安全圈深夜爬起来打补丁的 **Dirty Cow（脏牛）** 和 **Dirty Pipe（脏管）** 吗？

这一次，情况可能更糟。

近日，一个名为 **“Copy Fail”（CVE-2026-31431）** 的 Linux 内核 0-Day 漏洞被公开。与它的前辈们不同，这个漏洞**不需要极其苛刻的条件竞争（Race Condition），不需要计算内核版本偏移，甚至不需要你懂 C 语言去编译 Payload！**

攻击者只需运行一个 700 多字节的 Python 原生脚本，就能在 2017 年之后发布的几乎所有主流 Linux 发行版上，100% 稳定地拿到 `root` 权限。更致命的是，它可以轻松实现 Kubernetes 容器逃逸。

---

## 01. 漏洞档案 (Vulnerability Profile)

* **漏洞名称**：Copy Fail
* **漏洞编号**：CVE-2026-31431
* **漏洞发现者**：Taeyang Lee (Theori)
* **武器化利用团队**：Xint Code Research Team（借助 AI 辅助分析完成完整 Exploit）
* **影响范围**：自 **Kernel 4.14 (2017年发布)** 以来的所有主流 Linux 系统（包括 Ubuntu 24.04, RHEL 14.3, SUSE 16, Amazon Linux 2023 等）。
* **漏洞危害**：本地权限提升 (LPE) 至 Root、Kubernetes/容器逃逸。

---

## 02. 硬核原理解析：无痕的“隔山打牛”

“Copy Fail” 是一个存在于 Linux 内核 `authencesn` 密码学模板中的**纯逻辑漏洞**，它通过 `AF_ALG` 套接字接口与 `splice()` 系统调用的组合拳来触发。

### 攻击的底层逻辑：

1. **盯上 Page Cache（页缓存）**：Linux 系统为了加速文件读取，会将磁盘文件缓存在内存中（Page Cache）。攻击者的目标正是这些内存页面。
2. **巧妙的越界写入**：攻击者利用 `splice()` 将一个普通文件（比如对任何人都可读的 `/usr/bin/su`）传入管道，并喂给密码学接口 `AF_ALG`。
3. **9年前的历史遗留问题**：2017 年，内核在 `algif_aead.c` 中引入了一个本意是为了提高性能的“原地优化（in-place optimization）”（commit 72548b093ee3）。它直接让 `req->src = req->dst`，导致源数据和目标数据共享同一个 scatterlist（分散聚集表）。
4. **致命一击**：这使得本应受保护的页缓存（Page Cache）被直接暴露在了**可写的**目标缓冲区中。随后，IPsec 协议使用的 ESN（扩展序列号）机制在整理内存时，会向越界的偏移量直接写入 **4 个字节** 的脏数据，**这 4 个字节直接写进了内存中属于 `/usr/bin/su` 等特权程序的页缓存里**！

### 极致的隐蔽性：文件完整性监控（FIM）直接瞎眼

更可怕的是，由于内核**根本不知道**这个页缓存被修改了，它永远不会将这页内存标记为“脏页（Dirty）”并刷回磁盘。
**这意味着什么？**
磁盘上的 `/usr/bin/su` 文件其实完好无损，MD5/SHA256 校验值完全不变，所有的传统主机安全软件（如 Tripwire 或各类 HIDS/EDR 检测）都不会报警！但在内存中，它已经被改造成了黑客的提权后门。

---

## 03. 爆炸半径：不仅是提权，更是 K8s 容器的噩梦

“Copy Fail” 对云原生环境的杀伤力是巨大的。

在 Kubernetes 或 Docker 环境中，**宿主机的 Page Cache 是在所有容器之间共享的**。这意味着，哪怕你把一个黑客关在一个权限极低的隔离容器里，他依然可以通过 “Copy Fail” 修改共享的内存页缓存。

一旦内存中用于身份验证的 Setuid 二进制文件（如宿主机上的 `su`、`sudo`）被恶意污染，**不仅本容器可以提权，甚至其他不相关的容器，乃至整个 Kubernetes Node（宿主机节点）都会随之沦陷**。

---

## 04. 救命稻草：如何紧急修复与缓解？

目前，Linux 官方安全团队已经紧急合并了补丁（commit a664bf3d603d）。官方的修复思路非常直接：**回滚 2017 年那个致命的优化**，永久分离 TX 和 RX 的 Scatterlist，彻底斩断页缓存被误写的可能。

### 蓝队应对策略：

**1. 打补丁（首选）**
如果你使用的是受支持的主流发行版，请立即使用 `apt` / `yum` / `dnf` 执行内核更新，并重启服务器。

**2. 紧急缓解措施（如果无法立即重启）**
如果你暂时无法重启服务器更新内核，可以直接**禁用 `algif_aead` 内核模块**，从而彻底关闭该漏洞的攻击面。

请在终端中执行以下 Root 命令：

```
# 阻止模块在未来被加载echo "install algif_aead /bin/false" > /etc/modprobe.d/disable-algif-aead.conf
# 卸载当前已加载的恶意模块（可能需要先停止依赖它的IPsec服务）rmmod algif_aead 2>/dev/null
```

---

## 05. 关键收获

* **纯逻辑漏洞，不依赖竞争窗口**：与 Dirty COW / Dirty Pipe 不同，Copy-Fail 是 `algif_aead` 模板里 `req->src = req->dst` 这一行优化导致的源/目标 scatterlist 共用，触发条件稳定，PoC 100% 成功率。
* **攻击面极广，潜伏 9 年**：自 Kernel 4.14（2017）起持续存在，几乎覆盖了过去 9 年的主流发行版与云原生镜像，需要全量内核回归排查。
* **磁盘哈希不变，传统 FIM/HIDS 失效**：篡改只发生在内存页缓存，文件 `MD5/SHA256` 不变；Tripwire、AIDE、各类 EDR 文件完整性检测都不会告警，必须依赖**内存级**或 **eBPF 行为级**监控。
* **K8s 容器逃逸成本极低**：宿主机 Page Cache 在容器间共享，一个低权限 Pod 就能污染宿主机 `/usr/bin/su`，进而横扫整个 Node 上所有容器。
* **临时缓解不能等**：在内核 patch 落地之前，最快的兜底是用 `modprobe` 黑名单禁用 `algif_aead`，并对 IPsec 等依赖业务做兼容性回归。

> 关注「极客零零七」，每周实战攻防干货
>
> 公众号后台回复「提权」获取 Windows + Linux 提权速查表
>
> 公众号后台回复「AD攻击」获取 AD 域攻击手册

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/vRBYx9F4Zf6FIrWa8y7Avoujo7CWGRp0ICqvZGJIdtQgzNlzefeHiaeibmBZbcl5Oyj9wBNTsPiczEeKCelS9xjibw/0?wx_fmt=png)

极客零零七

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/vRBYx9F4Zf6FIrWa8y7Avoujo7CWGRp0ICqvZGJIdtQgzNlzefeHiaeibmBZbcl5Oyj9wBNTsPiczEeKCelS9xjibw/0?wx_fmt=png)

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