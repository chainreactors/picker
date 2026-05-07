---
title: GodPotatoBOF — 在Cobalt Strike中一键提权到SYSTEM
url: https://mp.weixin.qq.com/s/cTGIsTLPKLBWPQSWNBqbfA
source: Doonsec's feed
date: 2026-05-06
fetch_date: 2026-05-07T05:29:39.747149
---

# GodPotatoBOF — 在Cobalt Strike中一键提权到SYSTEM

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/tbTbtBE6TibeqnZibRqrs5hlic13LicZ8QYcstC9oRRmqWOH10XvyqVa5ppLXV3XASnsvCLPwktpXp96J4XNJfpU6iadkAlnfJ5ddZAgthEh8BEE/0?wx_fmt=jpeg)

# GodPotatoBOF — 在Cobalt Strike中一键提权到SYSTEM

原创

工具党
工具党

幻泉之洲

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

> GodPotatoBOF 是把 GodPotato 提权工具移植到 Cobalt Strike 的 BOF 版本。你可以在 Beacon 里直接执行，拿到 SYSTEM 令牌执行命令，或者把令牌丢给当前的 Beacon 会话使用。支持自定义命名管道，用法简单，几分钟就能上手。

## 01 这玩意儿能干啥

搞内网渗透的兄弟都懂，拿到一个普通权限的 Beacon 之后，下一步就是想办法提权到 SYSTEM。传统的提权工具有一堆，但大部分都得单独上传 exe、dll，容易被杀软盯上。GodPotatoBOF 就是来解决这个问题的——它是 GodPotato 的 BOF 移植版，直接跑在 Cobalt Strike 的 Beacon 内存里，不进磁盘，干净利落。

它的核心逻辑只有两件事：

* **默认模式**：偷一个 SYSTEM 令牌，然后派生一个新进程来执行你指定的命令。
* **令牌模式**：偷到 SYSTEM 令牌之后，直接调用 BeaconUseToken() 把这个令牌塞给当前的 Beacon，这样你就在 Beacon 里变成 SYSTEM 了。

## 02 怎么装怎么用

首先你得有个 Cobalt Strike 环境（废话）。然后按下面几步来：

**编译项目**

* 在目录里跑 `make`，等它编译完。

**加载到 Cobalt Strike**

* 打开 Cobalt Strike 客户端，Script Manager 加载 `godpotato.cna` 文件。
* 加载成功后，你就能在 Beacon 里直接用 `godpotato` 命令了。

命令格式长这样：

godpotato [token] [-cmd <命令>] [-pipe <管道名>]

参数说明：

| 参数 | 作用 |
| --- | --- |
| 无参数 | 默认执行 `cmd /c whoami` 来验证是否拿到 SYSTEM |
| token | 把偷到的 SYSTEM 令牌应用到当前 Beacon |
| -cmd "命令" | 在新进程中以 SYSTEM 权限执行指定命令 |
| -pipe "名称" | 指定命名管道名称（不指定就随机生成） |
| help -h --help /? | 显示帮助信息 |

## 03 动手跑几个例子

搞技术的不看例子不过瘾。下面几个场景你直接套着用：

* **验证提权是否生效**：
  `godpotato`
  执行后等待几秒，你会看到 `nt authority\system` 的输出。
* **直接给当前 Beacon 穿 SYSTEM 马甲**：
  `godpotato token`
  之后你在 Beacon 里敲任何命令都是 SYSTEM 身份。可以用 `getsystem` 类似的思路。
* **执行自定义命令看权限**：
  `godpotato -cmd "cmd /c whoami /priv"`
  会弹出新窗口？这里不是交互窗口，它会后台执行并把结果打回来。
* **指定管道名防止冲突**：
  `godpotato -cmd "cmd /c whoami" -pipe "MyPipe123"`
  如果你在对抗环境中做测试，固定管道名有时更稳定。

## 04 原理一句话

GodPotato 的工作原理是利用 Windows 的 RPCSS 服务（COM 相关）的漏洞，配合命名管道模拟来完成提权。BOF 版本只是把整个流程用 C 语言重新实现，封装成 Beacon Object File，这样就能在目标机器的内存里直接跑，不动硬盘。更底层的细节可以去看原项目 GodPotato（https://github.com/BeichenDream/GodPotato）的源码。

## 05 靠不靠谱？有啥坑？

咱说实话，这个 BOF 不是万能的。它依赖几个前提：

* 目标系统必须启用 RPCSS 服务（默认就是启用的）。
* 你得有能访问命名管道的权限（一般 admin 权限就行）。
* 某些杀软可能会拦截 NtCreateNamedPipeFile 相关的调用，不过因为 BOF 本身不写磁盘，它比 exe 版本隐蔽不少。

优点很明显：轻量、无文件落地、和 Cobalt Strike 无缝集成。缺点的话，就是依赖环境，部分加固系统可能失效。另外它只支持 Windows，别想在 Linux 上跑。

## 06 适合谁用

内网渗透测试人员、红队队员、玩 Cobalt Strike 的兄弟。如果你日常打靶场或者做授权测试，这个工具能让你少写好多轮子。推荐指数：⭐⭐⭐⭐（四星）

最后列一下致敬的原作者项目：

* GodPotato 原版：https://github.com/BeichenDream/GodPotato
* BOF 模板参考：https://github.com/MEhrn00/boflink
* CS-Situational-Awareness-BOF：https://github.com/trustedsec/CS-Situational-Awareness-BOF/tree/master/src/base\_template
* bof\_template：https://github.com/CodeXTF2/bof\_template

**获取方式：私信回复"GodPotatoBOF"获取**

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/KK6rkaWbMNbNvNRWVlQ1KyqceSk3WZAqKUsEjFj2Mfib1H7RQOOarzKolWvdD1W3PGicFOEABZLLpNoL2u9RdAXg/0?wx_fmt=png)

幻泉之洲

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/KK6rkaWbMNbNvNRWVlQ1KyqceSk3WZAqKUsEjFj2Mfib1H7RQOOarzKolWvdD1W3PGicFOEABZLLpNoL2u9RdAXg/0?wx_fmt=png)

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