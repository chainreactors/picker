---
title: Linux进程冻结术之 kill -stop
url: https://mp.weixin.qq.com/s/wUW8ZR9SklftwuEpg44cjQ
source: Doonsec's feed
date: 2026-04-19
fetch_date: 2026-04-20T04:53:02.294857
---

# Linux进程冻结术之 kill -stop

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/FaZFJ7xrqJZ6V6EzMEV5WjZKO6cQRGICicAELTTrybqoL0wRjmSe6vUlIzM1t5RlicQeef2VdI2DbuIYS3Ph5gpicibBhwCvIvx9IVaQrsKlH7Q/0?wx_fmt=jpeg)

# Linux进程冻结术之 kill -stop

原创

网安布道师
网安布道师

六边形攻防安全

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

![](https://mmbiz.qpic.cn/mmbiz_jpg/FaZFJ7xrqJaZCE2yYCaicnFYUxWZVs1RYWG6u8icYBo7szq82PeyPYcFGDPeUIE4YOGoeMOcVH9dkl9JTFjvOZShWtae9icGRpmlRUmo1Tb8MQ/640?wx_fmt=jpeg)

> 在 Linux 的世界里，有些命令表面平平无奇，却蕴含巨大的能量。 今天我们要讲的，就是一条能让进程瞬间"静止"的命令：`kill -STOP`。尤其在应急时，如发现了恶意进程，为防止恶意其外连、进一步系统破坏遏制其影响，但这时又不能暴力结束进程(如果恶意程序是内存加载结束进程会导致无法分析)的情况下，"冷冻"这个进程是最佳的处置方式。

---

## 💡 一、`kill` 并不只是"杀死"进程

很多人以为 `kill` 就是"强制终止程序"。 但实际上：

> **`kill` 的作用是：向进程发送一个信号（signal）。**

在 Linux 中，信号是内核与进程通信的方式。 常见信号如下 👇：

| 信号 | 名称 | 含义 |
| --- | --- | --- |
| `2` | SIGINT | 终止（相当于 Ctrl+C） |
| `9` | SIGKILL | 强制杀死（不可拦截） |
| `15` | SIGTERM | 请求程序正常退出 |
| `19` | **SIGSTOP** | 🧊 **强制暂停 不可忽略** |
| `18` | **SIGCONT** | ▶️ **继续执行** |

所以，`kill` 并不总是"杀死进程"， 有时它只是在轻声说一句——"**先停一停"**。

---

## 二、让进程暂停：`kill -STOP`

假设你有一个高 CPU 占用的程序，可以直接用：`kill -STOP <PID>`

来挂起（暂停）它。 被挂起的进程会立即停止运行，不再消耗 CPU。

要恢复，只需：`kill -CONT <PID>`

✅ 就能继续执行，完全无损。

---

## 三、动手实验：亲眼见证"暂停魔法"

新建脚本 `loop.sh`：`#!/bin/bash
i=1
while true; do
  echo "Running... $i"
  ((i++))
  sleep 1
done`

给执行权限并运行：`chmod +x loop.sh
./loop.sh`

你会看到

![](https://mmbiz.qpic.cn/sz_mmbiz_png/FaZFJ7xrqJbib8snXFzCLX5zdibluUf42tTSpuRzNCsEhhWB96dAyPUV8ibCwD3SID2nhnrST9cSF2fN2sSevx5abQnVZYafT1guCbzAjd5fuE/640?wx_fmt=png&from=appmsg)

---

### 步骤 1：找到进程号

![](https://mmbiz.qpic.cn/sz_mmbiz_png/FaZFJ7xrqJalEsY2Mf4009Bo7ja5HD8m7UrCLqRgVBJ49tHgsf8nOkpWYyeUBiaAOQBcgpDbF9W9YZEpdzpxIEqBlDGUyYgnAGov1AlUDGTI/640?wx_fmt=png&from=appmsg)

---

### 步骤 2：暂停它`kill -STOP 12345`

输出立刻停止！查看状态：`ps -o pid,stat,cmd -p 12345`

输出：

![](https://mmbiz.qpic.cn/mmbiz_png/FaZFJ7xrqJZ4DyvkxopOGSo4Ar0dUAfQyueXQbJmpNWCibcVRveia8mCvq15JZHXv6W67WoL3lGytnzMUdJluCySr8wfSRIKwwyvKNVKZ1k9c/640?wx_fmt=png&from=appmsg)

`T` 表示进程被 **挂起（Stopped）**。

![](https://mmbiz.qpic.cn/mmbiz_png/FaZFJ7xrqJb6gCkkhs9Ku1byNGdMSCeubq7na8fwibVgqg6OmYG9Hq69X7HbktTSUOay589B4vWGGSsu1PiaXDiaX8QCUwZjicq6cccq8UV5ZbU/640?wx_fmt=png&from=appmsg)

同时可以看到有suspended(挂起)的signal(信号)。

---

### 步骤 3：恢复运行`kill -CONT 12345`

程序继续输出：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/FaZFJ7xrqJYnKr8ISUNgdLlDAPcp3nc1QRReqM4sTQqOHL744O6VhwHiblibflN57ytul15HyIiaJMzCEicwOkpb2xtF7pzlpmkmX5icxRvWmYdo/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/FaZFJ7xrqJZmYlViaSgUADHbBDuUdEBWluDvU5DrwWHDjMfwpJYf9Iq3VRMiatAicibO0nA2S8CiaKO9da7dOWelwvS7daETl0hdZsuXkEpOSpZA/640?wx_fmt=png&from=appmsg)

是不是有点像按下了"暂停 / 继续播放"的按钮？ 🎬

---

## 四、常见应用场景

### ✅ 1. 临时暂停高占用任务或恶意程序`sudo kill -STOP <PID> # 一段时间后 sudo kill -CONT <PID>`

### ✅ 2. 调试进程

配合 `strace`、`gdb` 使用，可冻结目标程序以便分析。

### ✅ 3. 控制服务执行节奏`sudo kill -STOP $(pidof mysqld) sudo kill -CONT $(pidof mysqld)`

---

## 五、SIGSTOP 与 Ctrl+Z 的区别

| 信号 | 来源 | 是否可被忽略 |
| --- | --- | --- |
| `SIGTSTP` | Ctrl+Z | ✅ 可被进程捕获或忽略 |
| `SIGSTOP` | kill -STOP | ❌ 强制暂停，不可忽略 |

> !!! Ctrl+Z 是"礼貌的请求"， 而 `kill -STOP` 是"系统的命令"。

---

## 六、总结回顾

| 操作 | 命令 | 说明 |
| --- | --- | --- |
| 暂停进程 | `kill -STOP PID` | 强制挂起，不可忽略 |
| 恢复进程 | `kill -CONT PID` | 继续运行 |
| 查看状态 | `ps -o pid,stat,cmd -p PID` | 状态为 `T` 表示暂停 |

> kill -stop 就像应急侠🦸的冷冻🥶魔法术🪄： 它不会杀死进程，却能瞬间被冰冻，防止它对系统进行进一步破坏，同时应急侠🦸可以把恶意程序进行分析找到恶意特征、溯源等操作。

**🏷️ 标签：**`#Linux基础``#信号机制``#进程管理``#系统调试`

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/9qM7NQ3lGkBM9HNjOYhrvc9CNKbbd8pAl3cpffjDBworJnpCOkbD3Flx1XxRPlQbBAicglpPl0ZEGWVzdtCHsdA/0?wx_fmt=png)

六边形攻防安全

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/9qM7NQ3lGkBM9HNjOYhrvc9CNKbbd8pAl3cpffjDBworJnpCOkbD3Flx1XxRPlQbBAicglpPl0ZEGWVzdtCHsdA/0?wx_fmt=png)

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