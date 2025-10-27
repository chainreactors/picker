---
title: SSH终端修改为彩色显示（修改SSH颜色）
url: https://buaq.net/go-148961.html
source: unSafe.sh - 不安全
date: 2023-02-12
fetch_date: 2025-10-04T06:25:24.836812
---

# SSH终端修改为彩色显示（修改SSH颜色）

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

![](https://8aqnet.cdn.bcebos.com/128bd04491ed514348528da4b9f7ca51.jpg)

SSH终端修改为彩色显示（修改SSH颜色）

介绍SSH终端一般都是黑底白字，看久了也就看腻了，改成彩色试了下，还真不错~彩色显示更加醒目，也容易区分，大家也可以试试；修改注意：.bashrc是一个
*2023-2-11 17:29:0
Author: [blog.upx8.com(查看原文)](/jump-148961.htm)
阅读量:39
收藏*

---

![](https://imgsrc.baidu.com/super/pic/item/6b600c338744ebf80337bff99cf9d72a6159a7b6.jpg)

## 介绍

SSH终端一般都是黑底白字，看久了也就看腻了，改成彩色试了下，还真不错~

## 修改

注意：`.bashrc`是一个隐藏的文件，如果无法打开需要用`ls -a`命令找到`.bashrc`文件，然后再打开即可；
编辑文件：`vi ~/.bashrc`
找到代码：`#force_color_prompt=yes`
去掉#号：`force_color_prompt=yes`
保存退出：然后使用`source`命令使其生效：`source ~/.bashrc`

OK，现在SSH端的颜色已经显示为彩色了，如果想要更多的颜色可以参考下面代码进行修改；

## 颜色

继续编辑`vi ~/.bashrc`文件，颜色设置在`if [ "$color_prompt" = yes ]; then`的下面一行，替换掉其代码即可；
**原始代码：**

```
    PS1='${debian_chroot:+($debian_chroot)}\[\033[01;32m\]\[email protected]\h\[\033[00m\]:\[\033[01;34m\]\w\[\033[00m\]\$ '
```

**替换风格一：**

```
    PS1='${debian_chroot:+($debian_chroot)}\[\033[01;32m\]\u\[\033[01;31m\]@\[\033[01;36m\]\h\[\033[00m\]:\[\033[01;34m\]\W\[\033[00m\]\$ '
```

**替换风格二：**

```
    PS1='${debian_chroot:+($debian_chroot)}\[\033[01;31m\]\u\[\033[01;33m\]@\[\033[01;36m\]\h \[\033[01;33m\]\w \[\033[01;35m\]\$ \[\033[00m\]'
```

![](https://imgsrc.baidu.com/super/pic/item/8a82b9014a90f603a01547817c12b31bb151ed54.jpg)

我改了**风格2**

## 色位

****修改色位并非必要，没有特殊要求可以不用修改，有些色位在SSH终端比较暗淡，写在这里只是为了备忘；****

```
# 更新系统ncurse
apt-get install ncurses-base

# 查看当前系统色彩位数（一般默认为：8）
tput colors

# 编辑bashrc文件
vi ~/.bashrc

# 添加以下代码后保存
if [ -e /lib/terminfo/x/xterm-256color ]; then
        export TERM='xterm-256color'
else
        export TERM='xterm-color'
fi

# 重置bashrc使其生效
source ~/.bashrc
```

文章来源: https://blog.upx8.com/3218
 如有侵权请联系:admin#unsafe.sh

© [unSafe.sh - 不安全](https://unsafe.sh) Powered By [PaperCache](https://github.com/code-scan/PaperCache)

* admin#unsafe.sh
* [安全马克](https://aq.mk)
* [星际黑客](https://xj.hk)
* [T00ls](https://t00ls.net)