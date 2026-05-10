---
title: 高危Linux内核漏洞Dirty Frag已遭利用，可稳定提权至root
url: https://mp.weixin.qq.com/s/qbqw7TMWhH-z_laLUozvnw
source: Doonsec's feed
date: 2026-05-09
fetch_date: 2026-05-10T05:30:14.331844
---

# 高危Linux内核漏洞Dirty Frag已遭利用，可稳定提权至root

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/icBE3OpK1IX3ia69xy07KmYHMnVKZVKqT3kJicu118qAgJamV3A4IjH8jVqaiavaqk0Inu2nEqx6e6owiaqxniaUQnmxiaUmqPJXWebRvgZqmvnFl0/0?wx_fmt=jpeg)

# 高危Linux内核漏洞Dirty Frag已遭利用，可稳定提权至root

FreeBuf

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

![](https://mmbiz.qpic.cn/mmbiz_gif/qq5rfBadR38jUokdlWSNlAjmEsO1rzv3srXShFRuTKBGDwkj4gvYy34iajd6zQiaKl77Wsy9mjC0xBCRg0YgDIWg/640?wx_fmt=gif)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/icBE3OpK1IX0dLnfNS0batXIY2y3FMzzxKRNuJWz1QKxYNw9iciaBZo3QBtn0zq0uFd7mq6ibPqXP9n9NWIS9eU8bI7hkMdXboIfudyFoljyicgc/640?wx_fmt=png&from=appmsg)

##

安全研究人员披露了 Linux 内核中一个未修复的高危漏洞（代号 Dirty Frag），该漏洞允许本地低权限用户在全系主流 Linux 发行版（包括 Ubuntu、RHEL、Fedora、AlmaLinux 和 CentOS Stream）上获取完整 root 权限。

##

**Part01**

## ****技术关联性与独特性****

Dirty Frag 属于 Dirty Pipe 漏洞家族，但不受 Copy Fail 缓解措施影响——这意味着即使系统已部署 algif\_aead 黑名单防护，仍会完全暴露在攻击风险下。技术公告指出："该漏洞通过串联 xfrm-ESP 页缓存写入 和 RxRPC 页缓存写入 两个漏洞实现提权。Dirty Frag 扩展了 Dirty Pipe 和 Copy Fail 所属的漏洞类型，由于这是不依赖时间窗口的确定性逻辑缺陷，无需竞争条件即可触发，且利用失败时不会导致内核崩溃，成功率极高。"

**Part02**

## ****漏洞成因与影响范围****

该漏洞由研究员 Hyunwoo Kim（@v4bel）率先披露，其危害性源于两个独立缺陷的串联利用：

1. xfrm-ESP 页缓存写入缺陷：植根于 Linux IPsec 子系统，源自 2017 年 1 月的源代码提交（该提交同时导致了影响多发行版的缓冲区溢出漏洞 CVE-2022-27666）
2. RxRPC 页缓存写入缺陷：2023 年 6 月引入

技术分析显示："两个漏洞的共同点在于，当攻击者在零拷贝发送路径上通过 splice() 将只读权限的页缓存页面引用植入发送方 skb 的 frag 槽时，接收方内核代码会直接在该 frag 上执行加密操作。最终导致低权限用户仅具读取权限的文件（如 /etc/passwd 或 /usr/bin/su）页缓存被内存篡改，后续所有读取操作都将获取被篡改的副本。"

**Part03**

## ****利用特性与应对建议****

Dirty Frag 的确定性逻辑特性使其具备极高可靠性——不同于依赖精确时间窗口或竞争条件的常规内核漏洞，该漏洞利用失败不会引发内核崩溃，且成功率极高。目前公开的 PoC 已实现单条命令完成攻击。

由于第三方未经协调提前披露技术细节和利用代码，该漏洞尚未分配 CVE 编号。研究报告指出："两种攻击路径形成互补：在允许创建用户命名空间的环境中，ESP 利用链率先生效；而在禁用用户命名空间但加载 rxrpc.ko 模块的 Ubuntu 系统上，RxRPC 利用链可发挥作用。"

目前临时缓解方案建议通过黑名单机制禁用 esp4、esp6 和 rxrpc 内核模块加载。

**参考来源：**

Dirty Frag: A new Linux privilege escalation vulnerability is already in the wild

https://securityaffairs.com/191847/hacking/dirty-frag-a-new-linux-privilege-escalation-vulnerability-is-already-in-the-wild.html

---

**推荐阅读**

[![](https://mmbiz.qpic.cn/sz_mmbiz_png/icBE3OpK1IX3sibbWQvVRVyGlKyVa2716Kwag7P05S8W9d2stbD2I5yumphAxFoD6wiaIuexgPZb927DudHtwckQpG2OichmhfROaGh45gNKibko/640?wx_fmt=png&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MjM5NjA0NjgyMA==&mid=2651337545&idx=1&sn=772e37039accf79521a5b80e0032e89f&scene=21#wechat_redirect)

### **电报讨论**![](https://mmbiz.qpic.cn/sz_mmbiz_png/icBE3OpK1IX2AOA5HHVAjjGL1apmJN5zViaA4qX4mqict654rZb5qTMaUlxME4oNUU4ngFWCibn78oGgXB9d6A3hSLVwasycm2JrIwhUlllVWws/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/qq5rfBadR3ibvNluUKZ6RPy7h2fbYibRbLQDHPFqj89KkFsXBRibx5YTLiaTUfFOy9PKicps3l56iazUPNQrwdhkZ7jA/640?wx_fmt=png&from=appmsg)

**![](https://mmbiz.qpic.cn/mmbiz_png/qq5rfBadR3ibqyrdrvYXibMZM7K7gQW9ymeNepaIkpwPmicPSSoVicLBPXZ3a19uvVicYOjUZOibNeYRbrIOToCHjLAg/640?wx_fmt=png&from=appmsg)**

预览时标签不可点

阅读原文

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/qq5rfBadR3ibLOEAnkkKa2dHtqcjZ55KLsqibib6n4UDNUhLIuMRdAJ9ibfZkSK5LViaGJLEQN7p9OGo7mNnVv3EmkQ/0?wx_fmt=png)

FreeBuf

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/qq5rfBadR3ibLOEAnkkKa2dHtqcjZ55KLsqibib6n4UDNUhLIuMRdAJ9ibfZkSK5LViaGJLEQN7p9OGo7mNnVv3EmkQ/0?wx_fmt=png)

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