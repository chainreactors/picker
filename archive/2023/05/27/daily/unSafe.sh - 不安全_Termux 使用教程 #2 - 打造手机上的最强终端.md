---
title: Termux 使用教程 #2 - 打造手机上的最强终端
url: https://buaq.net/go-165921.html
source: unSafe.sh - 不安全
date: 2023-05-27
fetch_date: 2025-10-04T11:37:15.043938
---

# Termux 使用教程 #2 - 打造手机上的最强终端

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

![](https://8aqnet.cdn.bcebos.com/3f9ca1176eb452efdf9ee15ecf2ad4c2.jpg)

Termux 使用教程 #2 - 打造手机上的最强终端

前言虽然 Ter­mux 下载安装后就直接可以使用了，但是为了让它用起来更顺手、看起来更顺眼，我进行了一系列的客制化操作。自定义扩展功能按键默认的功能按
*2023-5-26 20:42:0
Author: [blog.upx8.com(查看原文)](/jump-165921.htm)
阅读量:29
收藏*

---

## 前言

虽然 Ter­mux 下载安装后就直接可以使用了，但是为了让它用起来更顺手、看起来更顺眼，我进行了一系列的客制化操作。

## 自定义扩展功能按键

默认的功能按键实在是太简陋，连左右方向键都没有，使用起来并不方便。好在可以通过 `~/.termux/termux.properties` 这个配置文件对按键进行定制。

[![](https://imgcdn.p3terx.com/post/20190919214059.jpg#vwid=1080&vhei=188)](https://imgcdn.p3terx.com/post/20190919214059.jpg#vwid=1080&vhei=188)

如果想设置成这样，可以在配置文件中添加如下内容：

```
extra-keys = [['ESC','/','-','HOME','UP','END','PGUP','DEL'],['TAB','CTRL','ALT','LEFT','DOWN','RIGHT','PGDN','BKSP']]
```

作为一个懒人，通常我都会一键操作：

```
mkdir -p ~/.termux && echo "extra-keys = [['ESC','/','-','HOME','UP','END','PGUP','DEL'],['TAB','CTRL','ALT','LEFT','DOWN','RIGHT','PGDN','BKSP']]" > ~/.termux/termux.properties
```

最后输入以下命令重载配置，或者关闭应用再打开。

```
termux-reload-settings
```

## 更换国内软件源

默认情况下软件包下载的速度非常慢，可以通过更换国内的软件源来加快软件包下载速度。

为了防止修改出错，先备份源列表文件：

```
cp $PREFIX/etc/apt/sources.list $PREFIX/etc/apt/sources.list.bak
```

> 还原：`cp $PREFIX/etc/apt/sources.list.bak $PREFIX/etc/apt/sources.list`

使用 `sed` 命令一键修改：

```
sed -i '[email protected]^\(deb.*stable main\)[email protected]#\1\ndeb https://mirrors.tuna.tsinghua.edu.cn/termux stable [email protected]' $PREFIX/etc/apt/sources.list
```

> 也可以输入`apt edit-sources`手动编辑源文件。将默认的官方源替换为清华大学的镜像源`https://mirrors.tuna.tsinghua.edu.cn/termux`。

检查修改：

```
$ cat $PREFIX/etc/apt/sources.list
# The main termux repository:
#deb https://dl.bintray.com/termux/termux-packages-24 stable main
deb https://mirrors.tuna.tsinghua.edu.cn/termux stable main
```

最后更新一下：

```
pkg up
```

> 如果卡进度条了，退出 Ter­mux 的进程，重新打开，并运行`dpkg --configure -a` 即可修复。

## 安装常用工具

安装一些基本的常用工具，方便后续的折腾。

```
pkg i -y git curl wget tree vim nano tmux htop
```

## 安装和配置 Oh My Zsh

> **Oh My Zsh will not make you a 10x developer...but you may feel like one.**

上面那句话来自 Oh My Zsh README，意思是 “装逼是第一生产力”。(大雾

我使用 Oh My Zsh 倒不是为把终端搞得花里胡哨去装逼，作为一个实用主义者，我非常喜欢自动建议、补全和代码高亮功能，这极大的提高了终端的输入效率。所以不管什么平台，都会安装 Oh My Zsh 。

### 安装 zsh

```
pkg i -y zsh
```

### 安装 Oh My Zsh

使用 curl 下载安装

```
sh -c "$(curl -fsSL https://raw.githubusercontent.com/robbyrussell/oh-my-zsh/master/tools/install.sh)"
```

使用 wget 下载安装

```
sh -c "$(wget -O- https://raw.githubusercontent.com/robbyrussell/oh-my-zsh/master/tools/install.sh)"
```

Oh My Zsh 安装完成后会提示你设置 zsh 为默认 sehll 。如果没有提示，输入下面的命令进行设置：

```
chsh -s zsh
```

### 修改 Oh My Zsh 主题

Oh My Zsh 有很多内置主题，只需要修改配置文件即可启用。也可以选择安装外置主题，比如 Powerlevel10k 。

我使用的主题是 ys，简单实用，不花里胡哨。使用 `sed` 命令一键修改：

```
sed -i '/^ZSH_THEME=/c\ZSH_THEME="ys"' ~/.zshrc
```

修改后输入下面的命令刷新配置就可以看到效果：

```
source ~/.zshrc
```

### 安装 Oh My Zsh 插件

安装 zsh-syntax-highlighting（代码高亮）

```
git clone https://github.com/zsh-users/zsh-syntax-highlighting $ZSH_CUSTOM/plugins/zsh-syntax-highlighting
```

安装 zsh-autosuggestions（自动建议）

```
git clone https://github.com/zsh-users/zsh-autosuggestions $ZSH_CUSTOM/plugins/zsh-autosuggestions
```

安装 zsh-completions（自动补全）

```
git clone https://github.com/zsh-users/zsh-completions $ZSH_CUSTOM/plugins/zsh-completions
```

zsh-com­ple­tions 插件还需把 `autoload -U compinit && compinit` 添加到`.zshrc`。输入命令可一键添加：

```
[ -z "`grep "autoload -U compinit && compinit" ~/.zshrc`" ] && echo "autoload -U compinit && compinit" >> ~/.zshrc
```

把需要启用的插件写入到配置文件中，使用 `sed` 命令一键操作。

```
sed -i '/^plugins=/c\plugins=(git z zsh-syntax-highlighting zsh-autosuggestions zsh-completions)' ~/.zshrc
```

> 如果你有自己想添加的插件，写在括号内即可，插件名称用空格隔开。

最后应用配置

```
source ~/.zshrc
```

## 修改终端配色

修改配色需要安装 [Termux:Styling](https://wiki.termux.com/wiki/Termux%3AStyling) 这个插件，安装好后长按屏幕，进入 `More...` 菜单，选择 `Style` 就可以对配色和字体进行设置。这在上篇文章中介绍菜单和选项时有提到过。

[![](https://imgcdn.p3terx.com/post/20190924184057.jpg#vwid=1080&vhei=1135)](https://imgcdn.p3terx.com/post/20190924184057.jpg#vwid=1080&vhei=1135)

选择好你自己喜欢的配色和字体，设置好后会在 `~/.termux` 目录中生成配色文件 `colors.properties` 和字体文件 `font.ttf`，可以把这两个文件进行备份，以后只需要导入即可，就不再需要安装这个插件了。

```
$ tree ~/.termux
/data/data/com.termux/files/home/.termux
├── colors.properties
├── font.ttf
├── shell -> /data/data/com.termux/files/usr/bin/zsh
└── termux.properties
```

## 修改启动页面的问候语

[![](https://imgcdn.p3terx.com/post/20190923144615.jpg#vwid=1080&vhei=929)](https://imgcdn.p3terx.com/post/20190923144615.jpg#vwid=1080&vhei=929)

刚接触 Ter­mux 时这些信息会对使用有帮助，但随着对 Ter­mux 的深入了解，和人类本能的控制欲，肯定会想把它换掉，我发现多数小伙伴都会使用自己的 ID 以大字体的方式呈现。

```
vi $PREFIX/etc/motd
```

而对于我这种崇尚极简主义的人来说，选择让它不显示。

```
touch ~/.hushlogin
```

## 尾巴

Ter­mux 给我的第一印象是好难用，连左右方向键都没有，差点就卸载了。因为最近在研究路由器，于是就尝试在 Ter­mux 中输入 `pkg install iperf3` 来安装 iPerf3 ，没想到装上了，然后就拿着手机满屋子测 WiFi 吞吐量。这也使我对它产生了兴趣，后来慢慢开始深入了解，一发不可收拾，也促使我进行了客制化的尝试。

文章来源: https://blog.upx8.com/3588
 如有侵权请联系:admin#unsafe.sh

© [unSafe.sh - 不安全](https://unsafe.sh) Powered By [PaperCache](https://github.com/code-scan/PaperCache)

* admin#unsafe.sh
* [安全马克](https://aq.mk)
* [星际黑客](https://xj.hk)
* [T00ls](https://t00ls.net)