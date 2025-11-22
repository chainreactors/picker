---
title: Debian12/11/10 一键开启BBR
url: https://blog.cctv.com.im/4271
source: 醉卧烟雨's Blog
date: 2025-11-21
fetch_date: 2025-11-22T03:06:00.593798
---

# Debian12/11/10 一键开启BBR

# Debian12/11/10 一键开启BBR

* [首页](https://blog.cctv.com.im/)
* [留言](/2002)
* [归档](https://blog.cctv.com.im/archives)

##

2025-11-21 /
 0评 /
0赞

赏

码

*移动设备上继续阅读*

## 一键开启

```
echo -e "\nnet.core.default_qdisc=fq\nnet.ipv4.tcp_congestion_control=bbr" >> /etc/sysctl.conf && sysctl -p
```

##

## 验证是否开启成功

```
sysctl net.ipv4.tcp_congestion_control
```

如果成功开启，那么会看到以下输出结果

```
net.ipv4.tcp_congestion_control = bbr
```

##

## 错误排查

输入一键开启命令后，如输出以下结果，则表示系统可能不支持BBR。

```
net.core.default_qdisc = fq
sysctl: setting key "net.ipv4.tcp_congestion_control": No such file or directory
```

进一步检验是否支持
输入

```
modprobe tcp_bbr
```

输出结果如下，则表示系统不支持BBR

```
modprobe: ERROR: could not insert 'tcp_bbr': Unknown symbol in module, or unknown parameter (see dmesg)
```

解决方案

```
apt update && apt-get upgrade
```

运行完成后，重启VPS。

* [bbr](https://blog.cctv.com.im/tag/bbr)
* [debian](https://blog.cctv.com.im/tag/debian)
* [linux](https://blog.cctv.com.im/tag/linux)

[国内服务器安装哪吒监控](https://blog.cctv.com.im/4255)

### 发表回复 [取消回复](/4271#respond)

您的邮箱地址不会被公开。 必填项已用 \* 标注

显示名称 \*

邮箱 \*

网站

[ ]  在此浏览器中保存我的显示名称、邮箱地址和网站地址，以便下次评论时使用。

评论 \*

![](https://blog.cctv.com.im/wp-content/plugins/wp-alu-master/static/img/icon_mrgreen.gif)![](https://blog.cctv.com.im/wp-content/plugins/wp-alu-master/static/img/icon_neutral.gif)![](https://blog.cctv.com.im/wp-content/plugins/wp-alu-master/static/img/icon_twisted.gif)![](https://blog.cctv.com.im/wp-content/plugins/wp-alu-master/static/img/icon_arrow.gif)![](https://blog.cctv.com.im/wp-content/plugins/wp-alu-master/static/img/icon_eek.gif)![](https://blog.cctv.com.im/wp-content/plugins/wp-alu-master/static/img/icon_smile.gif)![](https://blog.cctv.com.im/wp-content/plugins/wp-alu-master/static/img/icon_confused.gif)![](https://blog.cctv.com.im/wp-content/plugins/wp-alu-master/static/img/icon_cool.gif)![](https://blog.cctv.com.im/wp-content/plugins/wp-alu-master/static/img/icon_evil.gif)![](https://blog.cctv.com.im/wp-content/plugins/wp-alu-master/static/img/icon_biggrin.gif)![](https://blog.cctv.com.im/wp-content/plugins/wp-alu-master/static/img/icon_idea.gif)![](https://blog.cctv.com.im/wp-content/plugins/wp-alu-master/static/img/icon_redface.gif)![](https://blog.cctv.com.im/wp-content/plugins/wp-alu-master/static/img/icon_razz.gif)![](https://blog.cctv.com.im/wp-content/plugins/wp-alu-master/static/img/icon_rolleyes.gif)![](https://blog.cctv.com.im/wp-content/plugins/wp-alu-master/static/img/icon_wink.gif)![](https://blog.cctv.com.im/wp-content/plugins/wp-alu-master/static/img/icon_cry.gif)![](https://blog.cctv.com.im/wp-content/plugins/wp-alu-master/static/img/icon_surprised.gif)![](https://blog.cctv.com.im/wp-content/plugins/wp-alu-master/static/img/icon_lol.gif)![](https://blog.cctv.com.im/wp-content/plugins/wp-alu-master/static/img/icon_mad.gif)![](https://blog.cctv.com.im/wp-content/plugins/wp-alu-master/static/img/icon_sad.gif)![](https://blog.cctv.com.im/wp-content/plugins/wp-alu-master/static/img/icon_exclaim.gif)![](https://blog.cctv.com.im/wp-content/plugins/wp-alu-master/static/img/icon_question.gif)

Δ

* [关于](https://blog.cctv.com.im/about)
* [订阅](/feed)

© 2025 [醉卧烟雨's Blog](https://blog.cctv.com.im)

Theme by [Adams](https://biji.io)

* 默认
* 护眼
* 夜晚
* Serif
* Sans