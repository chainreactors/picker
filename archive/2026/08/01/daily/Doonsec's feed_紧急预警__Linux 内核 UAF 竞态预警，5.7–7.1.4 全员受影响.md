---
title: 紧急预警>>Linux 内核 UAF 竞态预警，5.7–7.1.4 全员受影响
url: https://mp.weixin.qq.com/s/V9ImpXO1CpaA67HWKVYnxQ
source: Doonsec's feed
date: 2026-08-01
fetch_date: 2026-08-02T05:08:28.691221
---

# 紧急预警>>Linux 内核 UAF 竞态预警，5.7–7.1.4 全员受影响

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/LAQpgdWQScuZm7SS1WGz4Mh7sCvqhQmjK25mhiacsicibvPic6wU8odoibJfaiaNU8kUukUUt0NzK9DA8pNzxXVQxQhtuQrmm7tGPh4pcg1VmBO4Q/0?wx_fmt=jpeg)

# 紧急预警>>Linux 内核 UAF 竞态预警，5.7–7.1.4 全员受影响

YGnight
YGnight

night安全

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

![](https://mmbiz.qpic.cn/sz_mmbiz_png/LAQpgdWQSctVS8Ps0NsFTqMiasz8uDibcvoib0spt17ORFYGT7Lk8y0JElHpWukiczXboIicO8mrOUut0DwfE4PvMwpuReeibS0yQHqN8Tictdm4Z4/640?wx_fmt=png&from=appmsg)

前两天公布了一个linux内核UAF漏洞CVE-2026-64560，我盯着那段竞态时序图看了好一会儿。Linux 内核从 5.7 一路到 7.1.4，只要版本没跟上补丁，本地一个低权用户就能靠 exec() 和定时器删除的竞态，把内核内存戳出个释放后使用（UAF）。轻则整机直接宕机，重则顺着内存破坏摸到提权。影响面大到离谱，基本覆盖这几年大部分线上服务器。

一、危害

Linux 内核的 posix-cpu-timers 子系统存在一个释放后使用（UAF）漏洞，根因是 non-leader exec() 和定时器删除之间的竞态。从 5.7 引入、到 7.1.5 才修，中间近六个大版本全都带着这个雷。本地低权用户就能触发，CVSS 直接给到 7.8 高危。

**CVSS 3.1** 7.8（High），向量 AV:L/AC:L/PR:L/UI:N/S:U/C:H/I:H/A:H，本地利用、低权限即可、机密性完整性可用性全高。

**官方 CVE 编号** CVE-2026-64560，由 Linux 内核 CVE 团队于 2026-07-29 分配，GitHub 安全公告 GHSA-78ph-mc3q-52vv 同步收录。

|  |  |
| --- | --- |
| 版本区间 | 状态 |
| 5.6.x 及更早 | 不受影响 |
| 5.7 至 6.x | 受影响 |
| 7.0 至 7.1.4 | 受影响 |
| 7.1.5（stable）及以上 / 7.2-rc3（mainline）及以上 | 已修复 |

⚠️ 风险定性，攻击者要的是本地落脚点，不是远程入口。可一旦本地低权用户拿到这个竞态，就能把内核内存玩坏，宕机只是开胃菜，内存破坏往上堆就是提权。跑在 5.7 到 7.1.4 的服务器、容器宿主，只要版本没跟上，都该把它当头等大事。

二、原理分析

POSIX CPU 定时器是个挂在进程（线程组）上的内核对象。正常删定时器时，内核要先找到目标线程、锁住它的信号处理结构 `sighand`，再动定时器。问题出在 exec() 这个动作上，它在某些情况下会换掉线程组的 leader，顺手把旧 leader 的信号结构拆掉。

删除定时器和 exec 是两条独立的系统调用路径，谁先谁后全看调度。一旦删定时器那条路在 exec 切换 leader 的瞬间读到旧 leader，等它想去锁 sighand，那块内存已经被 exec 一侧置空，删除流程就草草收场、没把定时器从队列里摘干净。

定时器对象被 free 之后，它仍然挂在 `p->signal` 的 timerqueue 里。后续任何 CPU 定时器相关操作（`run_posix_cpu_timers`、别的定时器增删）再来遍历这个队列，访问的就是一块已归还给 slab 的野内存。读写野指针，内核态的 UAF 就成型了，崩溃、信息泄露、提权都从这儿长出来。同样的坑还连着 `posix_cpu_timer_set` 和 `posix_cpu_timer_rearm`，修的时候一并填了。

三、完整攻击链

这串利用走的是本地竞态，不需要联网，靠的是时间窗口。把步骤拆开看就很清楚。

1低权用户拉起多线程进程

本地低权账户起一个带多个线程的进程，给某线程创建并 arm 一个面向 TGID 的 POSIX CPU 定时器（`timer_create` + `timer_settime`）。

2非 leader 线程调用 exec

进程里某个非 group leader 的线程执行 exec()，内核走 `de_thread()` 把 group leader 换成自己，再 `release_task()` 把旧 leader 释放掉。

3另一线程同时删定时器 ⚡

几乎在同一时刻，另一线程调用 `timer_delete()`（进 `sys_timer_delete` → `posix_cpu_timer_del`），和上面的 exec 抢同一个时间窗口。

4竞态读出旧 leader 已失效

删除路径先 `pid_task` 取到旧 leader，等它去锁 sighand 时，旧 leader 的 sighand 已经被 exec 那一侧置成 NULL，于是它返回 NULL 后直接 return 0，啥也没干。

5释放后使用被触发

紧接着 `free_posix_timer()` 把定时器对象交还给内核 slab。但那个定时器早就挂在 `p->signal` 的队列里，`run_posix_cpu_timers()` 或别的定时器增删操作再来碰它的 timerqueue 节点，就踩到了已释放内存，UAF 落地。

📌 关键认知，这套不是远程打点，是本地竞态。可它覆盖了 5.7 到 7.1.4 的几乎全部内核，云主机、容器宿主、生产服务器只要版本没跟上，本地低权用户就能用一段竞态把内核内存戳坏，轻则整机宕机重则顺藤摸瓜提权。patch 早就合进 7.1.5 和 7.2-rc3，别等出事才动。

四、自主排查

1. 看运行内核版本

```
uname -r # 例: 6.8.0-45-generic # 5.7 ~ 7.1.4 区间 = 受影响
```

2. 自编译内核核对修复提交

```
git log --oneline v7.1.4..v7.1.5 -- kernel/time/posix-cpu-timers.c # 修复提交: ad1cafa1bdaa (7.1.5) / 920f893f735e (7.2-rc3)
```

uname -r 落在 5.7 到 7.1.4 就中招，升到 7.1.5 或 7.2-rc3 往上才算干净。发行版 backport 的别只盯大版本号，对着它的安全公告确认修复版本更稳。

五、修复防御方案

① 升内核，整版升到 7.1.5+ stable 或 7.2-rc3+ mainline，发行版装对应 -security 内核包。社区不建议单独 cherry-pick 那两个提交，整版升最稳，装完重启。

② 暂时不能重启，先 `sysctl user.max_user_namespaces=0` 关掉非特权用户命名空间，再用 seccomp 拦掉 `timer_create` / `timer_delete`，少给对方留构造竞态的口子。

③ 生产环境开 kdump，dmesg 里盯 BUG、slab-out-of-bounds、general protection fault。容器宿主优先级最高，宿主一垮，上面全没。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/LAQpgdWQSctTWicwicwovsVtMLAjYPfEB9lMRmJJiaIozWIuicwrbneXZ3pGly4lRNAd1WrP6AKYA925Iz4c1EbnMLCOqWzkCmdCLXDQibsG4VQw/640?wx_fmt=png&from=appmsg)

预览时标签不可点

![]()

微信扫一扫
关注该公众号

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/SaibaRNhOjqiaCicRfSc5cJ3oiaCRqb97SmncCWWvuTyytibyIDxB9ZXWOuNaiaGAX2t0DYAAbdJ7aicS6WeCz4wfMoUg/0?wx_fmt=png)

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