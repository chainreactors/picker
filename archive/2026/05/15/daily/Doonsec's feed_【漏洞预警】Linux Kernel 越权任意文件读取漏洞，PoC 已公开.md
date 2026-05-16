---
title: 【漏洞预警】Linux Kernel 越权任意文件读取漏洞，PoC 已公开
url: https://mp.weixin.qq.com/s/mutmN1nje_x5bZAmQm8I9g
source: Doonsec's feed
date: 2026-05-15
fetch_date: 2026-05-16T05:11:09.993730
---

# 【漏洞预警】Linux Kernel 越权任意文件读取漏洞，PoC 已公开

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/VL7Qr6N3skiaIzcxMqUxekezcibCpLl3mZNP5dnSSjLzibLUbBWooJ8x3Q7XZ0l32CBsKVGac0LR5cCgKxiaQGxKhkzyibuBlEBoE4YH7bhib5Uqw/0?wx_fmt=jpeg)

# 【漏洞预警】Linux Kernel 越权任意文件读取漏洞，PoC 已公开

原创

腾讯云安全
腾讯云安全

云鼎实验室

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

## 漏洞描述

Linux Kernel 是 Linux 操作系统的核心组件，承担进程调度、内存管理、文件系统、设备驱动与系统调用接口等基础职责，是绝大多数云服务器与终端环境的运行底座。

近期，Linux Kernel 中的 `pidfd_getfd()` 系统调用被披露存在一个越权任意文件读取漏洞。漏洞根因位于 `__ptrace_may_access()` 函数：当目标进程的 `task->mm` 已被释放（即内存映射已经被回收）时，权限校验中的 dumpable 检查会被跳过。

进入 `do_exit()` 进程退出流程后，内核会先调用 `exit_mm()` 释放内存映射，随后才调用 `exit_files()` 关闭文件描述符。在两步之间存在一个短暂的时间窗口，目标进程的内存已被释放，但其原本打开的文件描述符仍处于存活状态。攻击者只要本地低权限身份与目标进程 uid 匹配，即可通过 `pidfd_getfd()` 在该窗口内窃取目标进程已打开但本无权访问的敏感文件句柄，进而读取受保护文件内容。

公开资料中已展示了两类典型利用路径：通过 `ssh-keysign` 进程窃取 SSH 主机私钥，以及通过 `chage` 进程读取 `/etc/shadow` 中的密码哈希。鉴于漏洞细节与 PoC 代码已在公开渠道发布，建议受影响用户尽快升级内核或采取临时缓解措施。

## 漏洞详情

|  |  |
| --- | --- |
| 漏洞名称 | Linux Kernel 越权任意文件读取漏洞 |
| 漏洞编号 | 暂无 |
| 危害等级 | 高风险 |
| 漏洞类型 | 内核漏洞 / 越权访问 |
| 影响范围 | Linux Kernel < commit `31e62c2ebbfd` |
| 参考链接 | git.kernel.org 官方补丁 |

## 影响版本

**受影响版本：**

* Linux Kernel < commit `31e62c2ebbfd`（2026 年 5 月 14 日修复版本之前）

**官方修复后的安全版本：**

* Linux Kernel >= commit `31e62c2ebbfd`

**补丁地址：**

* https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/commit/?id=31e62c2ebbfdc3fe3dbdf5e02c92a9dc67087a3a

## 漏洞风险

成功利用该漏洞可导致：

* **凭证泄露：**

  SSH 主机私钥、`/etc/shadow` 密码哈希等敏感文件可被读取；
* **横向移动：**

  泄露的私钥可被用于跳板登录其他主机；
* **离线密码破解：**

  泄露的密码哈希可在攻击者本地实施离线爆破。

由于利用过程发生在内核层、且无需额外提权动作，单台主机沦陷后可快速演化为内网级别的凭证扩散事件。

## 处置建议

**1、官方修复方案：**

评估业务受影响情况后，按发行版的更新通道升级到包含 commit `31e62c2ebbfd` 的内核版本，并按运维流程完成内核重启生效。

**注：**升级前请做好数据备份，避免出现意外。

**2、临时缓解措施：**

在无法立即升级的环境下，可结合实际场景考虑以下加固方向：

* 限制 `pidfd_getfd()` 系统调用的可达性（如通过 seccomp、SELinux/AppArmor 策略收敛）；
* 对暴露 `ssh-keysign`、`chage` 等 setuid/setgid 程序的多用户主机优先排查；
* 监控同一 uid 下异常的 `pidfd_open` + `pidfd_getfd` 调用组合。

## 参考链接

* **官方补丁：**https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/commit/?id=31e62c2ebbfdc3fe3dbdf5e02c92a9dc67087a3a
* **腾讯云安全中心：**https://cloud.tencent.com/announce/detail/2291

![图片](https://mmbiz.qpic.cn/mmbiz_gif/FIBZec7ucChYUNicUaqntiamEgZ1ZJYzLRasq5S6zvgt10NKsVZhejol3iakHl3ItlFWYc8ZAkDa2lzDc5SHxmqjw/640?wx_fmt=gif&wxfrom=5&wx_lazy=1&tp=webp#imgIndex=6)

**END**

更多精彩内容点击下方扫码关注哦~

关注云鼎实验室，获取更多安全情报

![图片](https://mmbiz.qpic.cn/mmbiz_png/NNSr7XSrt0mfEkibaEU8uriaORBdj9W37EhEIZlIFuzudKVafyia4vTv1q1usxN57bsdeAY4icwcKw9qJ1W4COeR4Q/640?wx_fmt=jpeg&wxfrom=5&wx_lazy=1&tp=webp#imgIndex=7)

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/NNSr7XSrt0miaxYvNtxDpUF6cHu3RxDXicIEQ8f8tephDpMFS0sczGA1vwwZKyT2sEjgwh1D5yxVxLRoalY8x2ZA/0?wx_fmt=png)

云鼎实验室

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/NNSr7XSrt0miaxYvNtxDpUF6cHu3RxDXicIEQ8f8tephDpMFS0sczGA1vwwZKyT2sEjgwh1D5yxVxLRoalY8x2ZA/0?wx_fmt=png)

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