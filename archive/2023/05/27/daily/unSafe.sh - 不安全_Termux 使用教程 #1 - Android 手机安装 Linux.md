---
title: Termux 使用教程 #1 - Android 手机安装 Linux
url: https://buaq.net/go-165922.html
source: unSafe.sh - 不安全
date: 2023-05-27
fetch_date: 2025-10-04T11:37:16.281078
---

# Termux 使用教程 #1 - Android 手机安装 Linux

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

![](https://8aqnet.cdn.bcebos.com/2e3c552a09fb06eb2127f7c02c838547.jpg)

Termux 使用教程 #1 - Android 手机安装 Linux

前言Termux 是一个 An­droid 下的终端模拟器，可以在手机上模拟 Linux 环境。它是一个手机 App，可以从应用商店直接下载安装，打开就
*2023-5-26 20:42:0
Author: [blog.upx8.com(查看原文)](/jump-165922.htm)
阅读量:41
收藏*

---

## 前言

Termux 是一个 An­droid 下的终端模拟器，可以在手机上模拟 Linux 环境。它是一个手机 App，可以从应用商店直接下载安装，打开就能使用，它提供一个命令行界面，让用户与系统交互。它支持 apt 软件包管理，可以十分方便安装软件包，而且完美支持 Python 、 PHP 、 Ruby 、 Go 、 Nodejs 、 MySQL 等工具。随着智能设备的普及和性能的不断提升，如今手机、平板等设备的硬件标准已经直逼入门级桌面计算机，使用 Ter­mux 完全可以把手机变成一个强大的小型服务器。你甚至可以使用 Ter­mux 通过 Nmap、Sqlmap、BB­Scan、sub­Do­mains­Brute、Hy­dra、Router­Sploit 等工具实现端口扫描、注入检测、子域名爆破、多协议弱口令爆破、路由器漏洞检测框架多种功能，把手机打造成一个随身携带的渗透神器，成为现实版的艾登・皮尔斯。

## 下载安装

官方推荐从 [F-Droid](https://f-droid.org/packages/com.termux/) 和 [Google Play](https://play.google.com/store/apps/details?id=com.termux) 这两个平台下载，安装完打开就是下面这个样子。

[![](https://imgcdn.p3terx.com/post/20190919225945.jpg#vwid=1080&vhei=1857)](https://imgcdn.p3terx.com/post/20190919225945.jpg#vwid=1080&vhei=1857)

## 基本操作

俗话说” 会跑之前，要先学会走 “，先了解基本操作，以后搞一些骚操作就轻而易举了。

### 选项和菜单

长按屏幕会出现可选择的复制光标，同时会显示 `Copy`（复制）、`Paste`（粘贴）、`More...`（更多）这几个选项。

[![](https://imgcdn.p3terx.com/post/20190920185125.jpg#vwid=673&vhei=367)](https://imgcdn.p3terx.com/post/20190920185125.jpg#vwid=673&vhei=367)

点击 `More...` 进入到下一级菜单。

[![](https://imgcdn.p3terx.com/post/20190922142041.jpg#vwid=1080&vhei=1860)](https://imgcdn.p3terx.com/post/20190922142041.jpg#vwid=1080&vhei=1860)

```
长按屏幕
├── COPY: 复制
├── PASTE: 粘贴
├── More: 更多
   ├── Select URL: 选择 URL
   └── Share transcipt: 传输当前会话的所有输出(通过Android api)
   └── Reset: 重置
   └── Kill process: 杀掉当前终端会话进程
   └── Style: 风格配色（需安装 Termux:Styling 插件）
   └── Keep screen on: 保持屏幕开启
   └── Help: 帮助文档(Termux Wiki)
```

从左侧屏幕边缘向右滑动可以拖出导航栏，在这里可以新建、切换、重命名会话 (ses­sion) 和调出输入法。

[![](https://imgcdn.p3terx.com/post/20190920192124.jpg#vwid=1080&vhei=1851)](https://imgcdn.p3terx.com/post/20190920192124.jpg#vwid=1080&vhei=1851)

### 常用快捷键

在使用终端时，需要使用到 `Alt`、`Ctrl`、`Esc` 等键，但手机上并没有这些键。

Ter­mux 中可以使用`音量减`按钮来模拟 `Ctrl` 键。例如，`音量减` +`L` 相当于在键盘上按下 `Ctrl`+`L`。

以下是一些在终端中常用的快捷键，同样适用于 Ter­mux 中。

* **`Ctrl`+`A`** -> 光标移动到开始位置
* **`Ctrl`+`E`** -> 光标移动到最末尾
* **`Ctrl`+`K`** -> 剪切此处至末尾的所有内容
* **`Ctrl`+`U`** -> 剪切此处至开始的所有内容
* **`Ctrl`+`W`** -> 剪切此处到左边的单词
* **`Ctrl`+`Y`** -> 粘贴由`Ctrl + U`、`Ctrl + D`、`Ctrl + W`剪切的单词
* **`Ctrl`+`L`** -> 相当于`clear`命令，清屏
* **`Ctrl`+`C`** -> 终止进程/命令
* **`Ctrl`+`D`** -> 关闭终端
* **`Ctrl`+`Z`** -> 挂起（发送 SIGTSTP 到）当前进程

`音量加`按钮可以作为产生特定输入的特殊键，可以粗略的理解为笔记本电脑上的 `Fn` 键。

* **`音量加`+`E`** -> `Esc`键
* **`音量加`+`T`** -> `Tab`键
* **`音量加`+`1`** -> `F1`键（`音量增加 + 2`相当于`F2`，以此类推）
* **`音量加`+`0`** -> `F10`键
* **`音量加`+`B`** -> `Alt`+`B`，使用readline时返回一个单词
* **`音量加`+`F`** -> `Alt`+`F`，使用readline时转发一个单词
* **`音量加`+`X`** -> `Alt`+`X`
* **`音量加`+`W`** -> 向上箭头键
* **`音量加`+`A`** -> 向左箭头键
* **`音量加`+`S`** -> 向下箭头键
* **`音量加`+`D`** -> 向右箭头键
* **`音量加`+`L`** -> `|`（管道字符）
* **`音量加`+`H`** -> `〜`（波浪号字符）
* **`音量加`+`U`** -> `_`(下划线字符)
* **`音量加`+`P`** -> `Page Up`键（上一页）
* **`音量加`+`N`** -> `Page Down`键（下一页）
* **`音量加`+`.`** -> `Ctrl`+`\`（SIGQUIT）
* **`音量加`+`V`** -> 显示音量控制
* **`音量加`+`Q`** -> 显示额外的按键视图
* **`音量加`+`K`** -> 同上

### 扩展功能按键

前面提到 Ter­mux 可以使用音量键来实现快捷键操作，个人感觉使用音量键不是很不方便。Ter­mux 还提供屏幕扩展功能按键。可以使用`音量加` +`Q` 或者`音量加` +`K` 可以显示和隐藏。

[![](https://imgcdn.p3terx.com/post/20190919214058.jpg#vwid=1080&vhei=108)](https://imgcdn.p3terx.com/post/20190919214058.jpg#vwid=1080&vhei=108)

此外，功能按键向左滑动可以调出文本输入框，可以更方便的粘贴和对待输入的指令进行更精细的修改。

[![](https://imgcdn.p3terx.com/post/20190920193543.jpg#vwid=1080&vhei=1039)](https://imgcdn.p3terx.com/post/20190920193543.jpg#vwid=1080&vhei=1039)

### 软件包管理

Ter­mux 除了支持 `apt` 命令外，还在此基础上封装了 `pkg` 命令，`pkg` 命令向下兼容 `apt` 命令。官方建议使用 `pkg` 命令，因为它会在安装或升级包时会自动更新 apt 列表，也就是说执行 `pkg upgrade` 相当于执行了 `apt update && apt upgrade`，简化了操作流程。

| 命令 | 作用 |
| --- | --- |
| pkg search | 搜索包 |
| pkg install | 安装包，简写`pkg i` |
| pkg uninstall | 卸载包 |
| pkg reinstall | 重新安装包 |
| pkg update / pkg upgrade | 升级软件包，简写`pkg up` |
| pkg list-all | 列出可供安装的所有包 |
| pkg list-installed | 列出已经安装的包 |
| pkg shoe | 显示某个包的详细信息 |
| pkg files | 显示某个包的相关文件夹路径 |

## Termux 与标准 Linux 目录结构的区别

与大多数 Linux 发行版不同，Ter­mux 不遵循[文件系统层次结构标准](https://p3terx.com/go/aHR0cHM6Ly9lbi53aWtpcGVkaWEub3JnL3dpa2kvRmlsZXN5c3RlbV9IaWVyYXJjaHlfU3RhbmRhcmQ)，你无法在标准路径找到 `/bin`、`/etc`、`/usr`、`/tmp` 等目录。为了方便，`Termux` 提供了一个特殊的环境变量：`PREFIX`，它相当于 `/usr` 目录。

```
$ tree -d -L 1 $PREFIX
/data/data/com.termux/files/usr
├── bin
├── etc
├── include
├── lib
├── libexec
├── share
├── src
├── tmp
└── var
```

此外用户主目录也在非常规位置。

```
$ echo $HOME
/data/data/com.termux/files/home
```

由于没有 root 权限，想对根目录进行操作是不可能的。

```
$ ls /
ls: cannot open directory '/': Permission denied
```

对此可以安装 `proot`，并使用 `termux-chroot` 命令可以模拟 root 环境与标准的 Linux 目录结构。

```
$ pkg i -y proot
$ termux-chroot
$ ls /
bin  data  dev  etc  home  lib  proc  root  sbin  share  storage  system  tmp  usr  var  vendor
$ ls /usr
bin  etc  include  lib  libexec  share  src  tmp  var
```

这对某些必须要用到标准路径的一些程序会非常有用。

## root 权限

前面提到的 `proot` 毕竟是模拟的方式，会有一定的局限性。如果手机已经 root ，在 Ter­mux 中使用 `su` 虽然可以切换为 root 用户，但是会有一些 Ter­mux 的命令无法正常使用，毕竟这不是一个标准的 Linux 环境。解决方案是安装 `tsu` 来获取 root 权限，`tsu` 是 Ter­mux 中的 `su` 替代方案。

安装 `tsu`：

```
pkg i -y tsu
```

使用 root 权限执行命令：

```
tsudo command
```

切换到 root 用户：

```
tsu
```

在 root 用户下，输入 `exit` 命令或者按 `Ctrl`+`D` 可以回到普通用户。

## 访问外部存储

Ter­mux 默认只能访问自身内部的数据，如果要访问手机中其它的数据，输入下面的命令后，手机弹出对请求权限的窗口，允许即可。

```
termux-setup-storage
```

这个操作将创建 `$HOME/storage` 目录，此目录中的子目录将通过符号链接到手机存储中的一些常用目录。

```
$ tree storage
storage
├── dcim -> /storage/emulated/0/DCIM
├── downloads -> /storage/emulated/0/Download
├── movies -> /storage/emulated/0/Movies
├── music -> /storage/emulated/0/Music
├── pictures -> /storage/emulated/0/Pictures
└── shared -> /storage/emulated/0
```

此外还可以通过 `/sdcard` 来访问外部存储的根目录。

## SSH 连接

作为 Linux 终端或者服务器，SSH 都是必须的。不管你是 SSH 连接到 Ter­mux ，还是使用 Ter­mux 去连其它主机，都需要先安装 `openssh`。

```
pkg i -y openssh
```

### Termux 使用 SSH 连接其它主机

基本操作，ssh 命令：

```
ssh [email protected] -p Port
```

### SSH 连接到 Termux

手机操作起来毕竟束缚太多，在电脑上通过 SSH 连接再进行操作是一件非常优雅的事情。

* 设置密码：

  ```
  passwd
  ```
* 查看用户名：

  ```
  whoami
  ```

  > 由于 Ter­mux 是单用户环境，所以这个步骤不是必须的。使用任何用户名都可以进行登录。
* 查看 IP 地址：

  ```
  ifconfig
  ```
* 启动 SSH 服务端：

  ```
  sshd
  ```

  > SSH 服务端程序默认是不启动的，且每次应用关闭再打开也需要再次启动。后面会讲如何自启 SSH 服务端。

集齐 SSH 三要素，现在可以在电脑终端中输入 `ssh` 命令或者使用其它 SSH 客户端进行连接了。需要注意的是 Ter­mux 的 SSH 端口是 `8022`。

```
ssh [email protected] -p 8022
```

执行 `ssh` 命令后，输入密码就可以连上了，然后就可以在电脑上方便的进行各种骚操作了。

[![](https://imgcdn.p3terx.com/post/20190921141822.png#vwid=1100&vhei=739)](https://imgcdn.p3terx.com/post/20190921141822.png#vwid=1100&vhei=739)

### 配置 SSH 密钥登录

如果需要将 Ter­mux 的 SSH 端口暴露在公网，为了安全建议配置密钥登录。

操作和一般的 Linux 发行版没有区别，属于基本操作。如果你不知道如何配置可以去看《[使用 ssh-keygen 和 ssh-copy-id 配置 SSH 密钥实现免密登陆](https://p3terx.com/archives/configuring-ssh-keys-with-sshkeygen-and-sshcopyid.html)》和《[使用 Xshell 给 Linux VPS 配置 SSH 密钥实现免密登录](https://p3terx.com/archives/configuring-ssh-key-with-xshell.html)》这两篇教程补补课，这里不再赘述。

> **友情提示：**`sshd_config`文件的路径是`$PREFIX/etc/ssh/sshd_config`

推荐使用 [SSH 密钥一键配置脚本](https://p3terx.com/archives/ssh-key-installer.html)，它可以从 GitHub 或者链接中获取公钥并自动配置。只要你在 GitHub 上设置过公钥，配置后就直接可以使用连接 GitHub 仓库的 SSH 密钥进行登录。

### SSH 服务端(sshd)自启

如果不想每次 ssh 连接 Ter­mux 前去输入 `sshd` 命令可以设置自启。sshd 自启分两种情况，一种是打开 Ter­mux 应用时自启，还有一种是手机开机后自启。

#### 打开应用时自启 SSH 服务端

把 `sshd` 命令添加到 Shell 配置文件中即可，比如我使用的是 zsh ，那么就添加到 `~/.zshrc` 中。如果是 bash ，那么就添加到 `~/.bashrc`。

```
echo "sshd" >> ~/.zshrc
```

#### 手机开机后自启 SSH 服务端

首先安装 [Termux:Boot](https://p3terx.com/go/aHR0cHM6Ly93aWtpLnRlcm11eC5jb20vd2lraS9UZXJtdXg6Qm9vdA) 插件，安装后给予该插件开机启动的权限，这样 Ter­mux 就可以在开机后自启了。

创建 `~/.termux/boot/` 目录（这个目录中放置的脚本会在开机启动 Ter­mux 后执行）。

```
mkdi...