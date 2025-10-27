---
title: 终端复用器：Tmux 的简单使用
url: https://buaq.net/go-154744.html
source: unSafe.sh - 不安全
date: 2023-03-23
fetch_date: 2025-10-04T10:21:04.472012
---

# 终端复用器：Tmux 的简单使用

* [unSafe.sh - 不安全](https://unsafe.sh)
* [我的收藏](/user/collects)
* [今日热榜](/?hot=true)
* [公众号文章](/?gzh=true)
* [导航](/nav/index)
* [Github CVE](/cve)
* [Github Tools](/tools)
* [编码/解码](/encode)
* [文件传输](/share/index)
* [Twitter Bot](https://twitter.com/buaqbot)
* [Telegram Bot](https://t.me/aqinfo)
* [Search](/search/search)

[Rss](/rss.xml)

[ ]
黑夜模式

![]()

终端复用器：Tmux 的简单使用

当我们远程ssh连接服务器进行操作的时候，如果网络断开，则整个ssh会话会全部丢失，其上正在运行的前台任务也会直接挂掉。虽然linux下有个简单的noh
*2023-3-22 22:45:0
Author: [blog.upx8.com(查看原文)](/jump-154744.htm)
阅读量:32
收藏*

---

当我们远程ssh连接服务器进行操作的时候，如果网络断开，则整个ssh会话会全部丢失，其上正在运行的前台任务也会直接挂掉。虽然linux下有个简单的nohup命令可以将任务挪到后台，但实际使用很麻烦（每一条命令前都得加nohup），并且不太稳定（搭配 bg，fg，ctrl +z 时有可能卡死）。

此时多路复用器： screen 和 tmux 的优点就凸显出来了。简而言之，就是通过 screen / tmux 命令直接在服务器上生成了一个虚拟的第三方终端 ，网络断开也只是我们的xshell等连接工具与“虚拟终端”之间的连接断开，并不会影响该“虚拟终端”与服务器的连接。能稳定保持回话的持续进行。

博主之前一直用的是 screen，后来转而使用 tmux。总体来说日常的简单使用2者都可以，但 tmux 细节上做的更好一点，同时也更稳定。

这里就简单说说 tmux 的安装与日常简单使用。

#### 1. 安装

#### 2. 创建会话

```
# 创建新的会话
tmux

# 创建新的会话，并自定义会话名为test
tmux new -s test

# 创建新的终端，并自定义终端名为test, 但不进入会话
tmux new -s test -d
```

#### 3. 暂时离开会话（分离会话）

```
tumx有 2 种方法当当前会话置于后台:
方法1:
ctrl + b , 松开2键后再输入d
方法2:
直接输入：tmux detach
```

#### 4.查看已创建会话

#### 5. 进入已创建并置于后台的会话

```
# 默认进入第一个会话
tmux a

# 进入到名称为test的会话
tmux a -t test

# 其实完整命令为 tmux attach-session, 使用中一般都是简写为tmux a
```

#### 6.退出并删除会话

#### 7.强制删除会话

```
# 仅仅删除test会话(即使是attached状态,也会删除)
tmux kill-session -t test

# 删除所有会话(attached状态的会略过)
tmux kill-session
```

#### 8.在会话中切换其他会话

```
ctrl + b, 松开后输入s，即可弹出选择界面,使用上下箭头回车确认即可
```

#### 9.重命名会话

```
tmux rename-session -t 0 <new-name>
```

#### 10.强行中断传输

```
如果出现卡死现象,可以按住ctrl ,再连点5次 X 键,即可恢复正常
```

#### 其他说明

1.快捷键

`TMUX`拥有大量的快捷键，如何使用，可以通过 `tmux list-keys` 命令查阅。

2.前缀键

`TMUX`所有快捷键都要通过前缀键唤起。默认的前缀键是`Ctrl+b`，即先按下`Ctrl+b`，快捷键才会生效。

举例来说，帮助命令的快捷键是`Ctrl+b ?`。它的用法是，在 Tmux 窗口中，先按下`Ctrl+b`，再按下`?`，就会显示帮助信息。然后，按下 ESC 键或`q`键，就可以退出帮助。

如果有兴趣的，可以自行搜索`TMUX` 相关内容自行学习。

文章来源: https://blog.upx8.com/3327
 如有侵权请联系:admin#unsafe.sh

© [unSafe.sh - 不安全](https://unsafe.sh) Powered By [PaperCache](https://github.com/code-scan/PaperCache)

* admin#unsafe.sh
* [安全马克](https://aq.mk)
* [星际黑客](https://xj.hk)
* [T00ls](https://t00ls.net)