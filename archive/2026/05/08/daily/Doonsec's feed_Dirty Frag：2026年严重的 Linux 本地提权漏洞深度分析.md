---
title: Dirty Frag：2026年严重的 Linux 本地提权漏洞深度分析
url: https://mp.weixin.qq.com/s/y1IH1fPjfFda83yWGsC9eg
source: Doonsec's feed
date: 2026-05-08
fetch_date: 2026-05-09T05:06:43.020315
---

# Dirty Frag：2026年严重的 Linux 本地提权漏洞深度分析

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/mqibEhCEN2lhE8jdORlaPBdibarUhicHJYWLUg0JWp0rF2G2zibUZg21NKNeaXZNoVDVUAPeuG5d4smYLIB1GbD5tn1vTcBWZcz8MmkERGvoh84/0?wx_fmt=jpeg)

# Dirty Frag：2026年严重的 Linux 本地提权漏洞深度分析

酷酷信安

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

![](https://mmbiz.qpic.cn/mmbiz_gif/LicngnvC2AYJLaFkGPyjibguibsTp9PQfSeiaLqiap9nA5f6RQMprBDAbqhfnV9x6DA7JYljfSvW3lXY3CT9ysxia9gg/640?wx_fmt=gif)

# 01

—

# 1概述

Dirty Frag 是一个于 2026 年 5 月公开披露的 Linux 内核本地提权漏洞（Local Privilege Escalation, LPE），CVE编号尚待分配。该漏洞通过链式利用两个独立的页缓存写入缺陷，使任意无特权本地用户能够在几乎所有主流 Linux 发行版上获取 root 权限，且攻击一条命令即可完成。

该漏洞与历史上著名的 Dirty COW（CVE-2016-5195） 和 Dirty Pipe（CVE-2022-0847） 同属一类漏洞，但攻击目标是内核 struct sk\_buff 的 frag 成员，因此命名为 Dirty Frag。

![](https://mmbiz.qpic.cn/mmbiz_png/mqibEhCEN2lhnxnVwB5mYFJ2QbtKAagmC4yiazjO70ojjyPGaNmYX2o2CBKxcbhZfgU0w2XtyqTdZqNaUx7zZnFFyN6XLrZTOLUpzuwKn7EAE/640?wx_fmt=png&from=appmsg)

# 02

—

# 漏洞发现与披露背景

发现者

漏洞由安全研究员 Hyunwoo Kim（GitHub: @v4bel）发现并报告。

披露时间线

![](https://mmbiz.qpic.cn/mmbiz_png/mqibEhCEN2lia8uVp2k2CicR1RItIYdahdrPHge7syg46r0wFZjo1d3KQAxGnt1AtcCB4wnlB6YQk4qrAn4WbAVH3veGBvE6EWtXqNIoo9eglc/640?wx_fmt=png&from=appmsg)

由于禁运提前被打破，两个子漏洞均未分配 CVE 编号，且公开的 PoC 已在互联网广泛流传。

# 03

—

# 技术原理深度解析

## 3.1 漏洞类别：页缓存写入（Page-Cache Write）

Dirty Frag 属于页缓存污染类漏洞。其核心机制是：

1. splice() / MSG\_SPLICE\_PAGES 零拷贝路径允许用户空间将只读页缓存页面（如 /etc/passwd、/usr/bin/su）的引用植入发送方 socket buffer（skb）的 frag 槽位。

2. 内核在接收路径进行原地（in-place）加密运算时，直接在该 frag 上操作，从而永久修改 RAM 中的页缓存内容。

这是一个纯逻辑漏洞，不依赖竞争条件，不会导致内核崩溃，首次攻击即可成功。

---

## 3.2 子漏洞一：xfrm-ESP 页缓存写入

位置： esp\_input() — IPsec ESP 接收路径（esp4/esp6 模块）

引入时间： 内核 commit cac2661c53f3，2017 年，漏洞已存在约 9 年。

触发路径：

用户空间 splice(2) → 植入只读页缓存 frag → esp\_input()

→ 跳过 skb\_cow\_data() COW 检查

→ 直接对 frag 执行 AEAD 原地解密

→ 页缓存被覆写

关键问题： 当 skb 是非线性（non-linear）但无 frag list 时，代码跳过了强制的 skb\_cow\_data() 缓冲区分配步骤，直接对攻击者植入的 frag 进行原地 AEAD 解密。

利用方式： 通过 XFRMA\_REPLAY\_ESN\_VAL netlink 属性，攻击者可以精确控制每次写操作的文件偏移量（位置）和写入值（4字节），实现对 /usr/bin/su 等 SUID

程序页缓存的任意字节覆写。

---

## 3.3 子漏洞二：RxRPC 页缓存写入

位置： rxkad\_verify\_packet\_1() — RxRPC/rxkad 子系统

引入时间： 2023 年 6 月

关键特点：

* 无需任何命名空间特权（user namespace 等）
* 执行 8 字节 pcbc(fcrypt) 原地解密，直接作用于同类型的 splice 固定页
* 攻击者可在用户空间完全暴力穷举合适的解密密钥，再触发内核写操作，整个过程完全确定性，无随机性

---

## 3.4 链式利用策略

两个子漏洞互相补盲：

攻击者二进制

├── 尝试 xfrm-ESP exploit

│ 适用：大多数内核版本（2017–2026）

│ 需要：可以加载 esp4/esp6 模块

│

└── 尝试 RxRPC exploit

适用：2023-06 至今的内核

优势：无需任何特权，可绕过 Copy Fail 缓解措施

两者串联后，单个二进制可在所有主流发行版上获取 root。

---

## 3.5 绕过 Copy Fail 缓解措施

▎ "Dirty Frag 无论 algif\_aead 模块是否可用均可触发。换句话说，即使在已应用 Copy Fail 公开缓解措施（algif\_aead 黑名单）的系统上，你的 Linux 对 Dirty Frag 依然脆弱。"

▎ — Hyunwoo Kim

---

# 四、影响范围

受影响的发行版

![](https://mmbiz.qpic.cn/sz_mmbiz_png/mqibEhCEN2lg01ctQpPqicwdcOesxwibrkpCJuTfFxwwXwmeJ63aicMHnmF6PF623A4U3ebCT78JRaHZ6ISgExRnBwhIKXvysNvr8icURcrxIDok/640?wx_fmt=png&from=appmsg)

影响内核版本范围：

- ESP 子漏洞：2017年（commit cac2661c53f3）至今，约 9 年

- RxRPC 子漏洞：2023年6月至今

# 五、漏洞严重性分析

![](https://mmbiz.qpic.cn/mmbiz_png/mqibEhCEN2lhexLiceO0qOU2qLIsKoPJRIa0QYT1YsgHBYTNES2aBiaHrjhvAobI05PvQLibVxJx9VIDeTrbywLTzGVEIaUyUQjTNywgKgwFswM/640?wx_fmt=png&from=appmsg)

# 六、补丁状态

![](https://mmbiz.qpic.cn/sz_mmbiz_png/mqibEhCEN2ljkYc8gy9pRGnpW4Evv9kfUicawRntT0bxYLdfxAXttLnqqyBw5R2NGpUYc3v0uGGVhiaffkNRQhvmKOibr3bicriaTBLvibQ0KFWODo/640?wx_fmt=png&from=appmsg)

# 七、缓解措施

## 7.1 立即缓解（推荐）

若服务器不依赖 IPsec VPN 隧道，立即执行：

```
sudo sh -c "printf 'install esp4 /bin/false\ninstall esp6 /bin/false\ninstall rxrpc /bin/false\n' \  > /etc/modprobe.d/dirtyfrag.conf; rmmod esp4 esp6 rxrpc 2>/dev/null; true"
```

此命令将：

1. 将上述模块加入黑名单，防止自动加载

2. 尝试卸载已加载的模块

▎ 警告： esp4/esp6 是 IPsec 的内核 ESP 变换模块。禁用它们将破坏依赖内核数据路径的 IPsec 隧道（如 strongSwan、Libreswan）。使用 IPsec VPN 的服务器需权衡利弊。

## 7.2 系统加固措施（纵深防御）

* 确保 SELinux 处于强制模式（enforcing）
* 限制 SSH 访问，减少本地账户暴露面
* 容器环境中使用默认 Security Context Constraints（SCC）
* 工作负载以非 root 运行
* 限制 oc debug 访问权限（OpenShift 环境）

## 7.3 等待官方补丁

各发行版正在积极回溯补丁，建议关注官方安全公告：

- AlmaLinux 已率先发布测试补丁

- CloudLinux 提供 KernelCare 无重启实时补丁

- 其他发行版补丁陆续发布中

---

# 八、攻击指标（IoC）

已发现与该漏洞相关的 Bash 脚本 IoC，该脚本自动化完成：

1. 准备 payload

2. 编译 exploit 二进制

3. 执行提权操作

相关脚本已被 Imunify360 加入黑名单。

# 九、与历史"Dirty"系列漏洞对比

![](https://mmbiz.qpic.cn/sz_mmbiz_png/mqibEhCEN2liafda2dz72UpGeKDiavhR23eFQNItr5048uy3RJmYjwuZcA2IK2yGGNOceuUwfa6B7dKBZvXkX2R9icS15075icccKQKAtEBXtuNs/640?wx_fmt=png&from=appmsg)

总结:

Dirty Frag 是迄今为止最危险的"Dirty"系列漏洞之一。其核心危险性在于：

1. 9年历史积累，影响范围极广

2. 纯逻辑漏洞，利用可靠、无崩溃风险

3. 绕过已知缓解措施（Copy Fail 的 algif\_aead 黑名单无效）

4. 禁运被打破，补丁就绪前 PoC 已公开

5. WSL2 也受影响，攻击面延伸至 Windows 用户

建议所有 Linux 系统管理员立即评估并应用模块黑名单缓解措施，并持续关注各发行版官方补丁动态。

参考链接：

[官方通告] Red Hat (RHSB-2026-003)https://access.redhat.com/security/vulnerabilities/RHSB-2026-003

[概念验证] GitHub - V4bel/dirtyfrag该漏洞的公开 PoC (概念验证代码)，证明漏洞可被稳定利用。

[开源社区] Phoronix报道了 Dirty Frag 漏洞被过早公开对 Linux 上游维护者造成的被动局面。

[安全资讯] CyberSecurityNews聚焦于该 Linux 漏洞对全球网络安全设备和服务器的潜在冲击。

![](https://mmbiz.qpic.cn/mmbiz_gif/LicngnvC2AYJLaFkGPyjibguibsTp9PQfSeD1clNISC4IJc5jrc4hCwFGUyU8wkLlmia8badUdyMBIY2AIBDjUhbRg/640?wx_fmt=gif)

预览时标签不可点

修改于

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/LicngnvC2AYLLP1XTZO2VmESctbhgz9PGJTo6uJ4yRqaSalTRLaTlc0RfKjpRLS9GLpVkL5lx7klx8LC30Z2gDA/0?wx_fmt=png)

酷酷信安

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/LicngnvC2AYLLP1XTZO2VmESctbhgz9PGJTo6uJ4yRqaSalTRLaTlc0RfKjpRLS9GLpVkL5lx7klx8LC30Z2gDA/0?wx_fmt=png)

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