---
title: SSH终端修改为彩色显示（修改SSH颜色）
url: https://blog.upx8.com/3218
source: 黑海洋 - WIKI
date: 2023-02-12
fetch_date: 2025-10-04T06:26:11.328779
---

# SSH终端修改为彩色显示（修改SSH颜色）

# [黑海洋 - Wiki](/ "黑海洋 - Wiki - 点击返回首页")

# SSH终端修改为彩色显示（修改SSH颜色）

发布时间:
2023-02-11

分类:
[系统安全/os\_security](https://blog.upx8.com/os_security/)

热度:
22639

![](https://i.111666.best/image/PZfglNsQ9Lq9EBOWfvlC01.jpg)

## 介绍

SSH终端一般都是黑底白字，看久了也就看腻了，改成彩色试了下，还真不错~
彩色显示更加醒目，也容易区分，大家也可以试试；

# ubuntu修改方法

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
    PS1='${debian_chroot:+($debian_chroot)}\[\033[01;32m\]\u@\h\[\033[00m\]:\[\033[01;34m\]\w\[\033[00m\]\$ '
```

**替换风格一：**

```
    PS1='${debian_chroot:+($debian_chroot)}\[\033[01;32m\]\u\[\033[01;31m\]@\[\033[01;36m\]\h\[\033[00m\]:\[\033[01;34m\]\W\[\033[00m\]\$ '
```

**替换风格二：**

```
    PS1='${debian_chroot:+($debian_chroot)}\[\033[01;31m\]\u\[\033[01;33m\]@\[\033[01;36m\]\h \[\033[01;33m\]\w \[\033[01;35m\]\$ \[\033[00m\]'
```

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

# debian修改方法

看图操作：

![](https://image.dooo.ng/c/2024/11/29/67499f817f4d2.webp)

1、编辑文件：`vi ~/.bashrc`
2、找到代码，去掉#号。
3、保存退出：`:wq` 命令使其生效：`source ~/.bashrc`

# 插件美化方法

### [zsh 安装与配置，使用 oh-my-zsh 美化SSH终端](https://blog.upx8.com/go/LzQ0ODY)

[取消回复](https://blog.upx8.com/3218#respond-post-3218)

### 在下方留下您的评论.[加入TG群](https://t.me/).[打赏🍗](/reward.html)

提交评论

* [Post](/author/1)
* [Link](/links.html)
* [工具](https://tools.upx8.com/)
* [关于](/about.html)
* [文库](/WooyunDrops)

[![](/usr/uploads/ypyun.png)](https://www.upyun.com/?utm_source=lianmeng&utm_medium=referral "赞助商")
Copyright © 2024 黑海洋. All rights reserved.
[看雪赞助](https://www.kanxue.com/ "看雪学院赞助")

[浙ICP备2021040518号](http://beian.miit.gov.cn "浙ICP备2021040518号") [Sitemap](sitemap.xml?type=index "Sitemap")