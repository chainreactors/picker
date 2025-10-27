---
title: 打靶日记--Misdirection
url: https://www.freebuf.com/articles/web/428500.html
source: FreeBuf网络安全行业门户
date: 2025-04-24
fetch_date: 2025-10-06T22:05:54.964350
---

# 打靶日记--Misdirection

[![freeBuf](/images/logoMax.png)](/)

主站

分类

云安全

AI安全

开发安全

终端安全

数据安全

Web安全

基础安全

企业安全

关基安全

移动安全

系统安全

其他安全

特色

热点

工具

漏洞

人物志

活动

安全招聘

攻防演练

政策法规

[报告](https://www.freebuf.com/report)[专辑](/column)

* ···
* [公开课](https://live.freebuf.com)
* ···
* [商城](https://shop.freebuf.com)
* ···
* 用户服务
* ···

行业服务

政 府

CNCERT
CNNVD

会员体系（甲方）
会员体系（厂商）
产品名录
企业空间

[知识大陆](https://wiki.freebuf.com/page)

搜索

![](/freebuf/img/7aa3bf7.svg) ![](/freebuf/img/181d733.svg)

创作中心

[登录](https://www.freebuf.com/oauth)[注册](https://www.freebuf.com/oauth)

官方公众号企业安全新浪微博

![](/images/gzh_code.jpg)

FreeBuf.COM网络安全行业门户，每日发布专业的安全资讯、技术剖析。

![FreeBuf+小程序](/images/xcx-code.jpg)

FreeBuf+小程序把安全装进口袋

[![](https://image.3001.net/images/20231020/1697804527_653270ef7570cc7356ba8.png)](https://wiki.freebuf.com)

打靶日记--Misdirection

* ![]()
* 关注

* [Web安全](https://www.freebuf.com/articles/web)

打靶日记--Misdirection

2025-04-23 21:49:22

所属地 湖北省

## 前期信息搜集

主机发现

![1745413007_6808e38f717aae3eb5223.png!small?1745412987635](https://image.3001.net/images/20250423/1745413007_6808e38f717aae3eb5223.png!small?1745412987635)

端口扫描，发现开了 22 80 3306 8080 这几个端口，我的优先级是 80 和 8080 然后是 3306 和 22

![1745413295_6808e4af7b218bc780936.png!small?1745413275634](https://image.3001.net/images/20250423/1745413295_6808e4af7b218bc780936.png!small?1745413275634)

再去进一步的进行版本扫描，发现 80 端口是 python 搭建的网络服务但也没其他有用的信息了

![1745413383_6808e5073a40076eb20e1.png!small?1745413363591](https://image.3001.net/images/20250423/1745413383_6808e5073a40076eb20e1.png!small?1745413363591)

进行简单的漏洞扫描，80 这边报了一个 SQL （试了下好像没有）8080 这边报了几个目录

![1745413914_6808e71ae002c4d453be1.png!small?1745413896006](https://image.3001.net/images/20250423/1745413914_6808e71ae002c4d453be1.png!small?1745413896006)

## 渗透阶段

先看看 80 端口是什么东西，发现是一个类似于投票系统的东西

![1745413503_6808e57f16398dcd1794c.png!small?1745413488320](https://image.3001.net/images/20250423/1745413503_6808e57f16398dcd1794c.png!small?1745413488320)

看了一圈后发现也没有什么可以打的地方，于是决定先注册一个账户看看登录后能不能有什么进一步的信息（顺带提一下 web2py 是一套开发框架有漏洞但是用起来比较麻烦所以先放着）

![1745413670_6808e626f1dcd699f2081.png!small?1745413651018](https://image.3001.net/images/20250423/1745413670_6808e626f1dcd699f2081.png!small?1745413651018)

但是好像是他邮件端口没有配置导致注册不了账户所以暂时搁置 80 端口，如果 8080 这边也没什么东西那就去爆破一下目录（因为是框架开发的会扫出来一堆东西）或者去用 web2py 的洞，打开 8080 发现是一个网站搭建成功的页面，需要进一步的目录爆破看看有什么东西（虽然刚刚 nmap 已经扫出来了几个目录但还是要再扫一遍）。

![1745413851_6808e6db893e1a6a3176f.png!small?1745413831650](https://image.3001.net/images/20250423/1745413851_6808e6db893e1a6a3176f.png!small?1745413831650)

看到还是扫出来了不少东西的

![1745414112_6808e7e0c89cfcfcbbcf6.png!small?1745414093277](https://image.3001.net/images/20250423/1745414112_6808e7e0c89cfcfcbbcf6.png!small?1745414093277)

一个个看下来发现要么是空目录要么隐藏了但是在 debug 目录下发现一个很有价值的东西，一个 shell

![1745414229_6808e855872bcc5a7486e.png!small?1745414209495](https://image.3001.net/images/20250423/1745414229_6808e855872bcc5a7486e.png!small?1745414209495)

经过尝试发现是一个跟正常 shell 没什么区别的 shell 用户是功能用户 www-data 不多废话先弹一个 shell 到kali 上再说，由于直接把 shell 给我们了所以可以直接用 bash 去弹shell，当然也可以上传一个 shell 文件去进行 shell 的反弹，这里我是用 wget 传了一个 shell 到 shell 目录下（当时没想到直接弹，传文件记得要给传上去的文件权限）

![1745414450_6808e9325263c48bc39bb.png!small?1745414430375](https://image.3001.net/images/20250423/1745414450_6808e9325263c48bc39bb.png!small?1745414430375)

得到初始 shell

![1745414565_6808e9a5b1731346408e9.png!small?1745414546057](https://image.3001.net/images/20250423/1745414565_6808e9a5b1731346408e9.png!small?1745414546057)

## 提权

先看看我们当前用户有没有什么特权，发现可以不用密码得到到 brexit 这个用户的 bash 环境，所以这里我们先换个权限较高的账户

![1745414699_6808ea2b8e4ddc0040013.png!small?1745414679833](https://image.3001.net/images/20250423/1745414699_6808ea2b8e4ddc0040013.png!small?1745414679833)

成功得到 brexit 这个用户的 bash 环境

![1745414736_6808ea508df803c2b0c73.png!small?1745414716781](https://image.3001.net/images/20250423/1745414736_6808ea508df803c2b0c73.png!small?1745414716781)

先提升一下 shell 的交互性

```
#用python模拟一个高交互性的shell
python -c 'import pty;pty.spawn("/bin/sh")'
#指定一下终端的类型
export TERM=xterm-color
```

![1745414910_6808eafe97df59024d59f.png!small?1745414890585](https://image.3001.net/images/20250423/1745414910_6808eafe97df59024d59f.png!small?1745414890585)

然后先尝试一下常规的提权手段，找一下当前权限可以写的文件，发现我们可以直接操作 /etc/passwd 文件，那我们可以直接模仿 root 账户写入一个账户就可以了

```
#ban了一些没什么用的路径
find / -writable -type f -not -path "/proc/*" -not -path "/sys/*" -not -path "/var/*" 2>/dev/null
```

![1745415006_6808eb5ee28a81f7bbe46.png!small?1745414989035](https://image.3001.net/images/20250423/1745415006_6808eb5ee28a81f7bbe46.png!small?1745414989035)

我们先看看 root 账户在 /etc/passwd 里面是怎么写的，发现我们只用去生成一个密码就行了（不会的话直接去 /etc/shadow 里面复制也行）

![1745415292_6808ec7c6c9fe6c064119.png!small?1745415272573](https://image.3001.net/images/20250423/1745415292_6808ec7c6c9fe6c064119.png!small?1745415272573)

这里拿 openssl 去生成一个密码

![1745415460_6808ed2410282d27ef61c.png!small?1745415440360](https://image.3001.net/images/20250423/1745415460_6808ed2410282d27ef61c.png!small?1745415440360)

然后拿到生成好的密码去拼一个 root 权限的账户（上面的图片里面的 root 信息是我 kali 里的与靶机上的略微有一些不同）

![1745415577_6808ed99575a0073e9c91.png!small?1745415557612](https://image.3001.net/images/20250423/1745415577_6808ed99575a0073e9c91.png!small?1745415557612)

写入我们创建的用户

![1745415916_6808eeec99204aa084572.png!small?1745415896826](https://image.3001.net/images/20250423/1745415916_6808eeec99204aa084572.png!small?1745415896826)

尝试去登录但发现系统提示我们没有 /bin/bash 这个文件

![1745415953_6808ef1150814c1049add.png!small?1745415933413](https://image.3001.net/images/20250423/1745415953_6808ef1150814c1049add.png!small?1745415933413)

这里去看了一下发现是 /bin/sh 于是把最后的那一点改成 /bin/sh 再次写入后登录，提权成功（flag 就不找了）

![1745416053_6808ef75c0115ca027599.png!small?1745416034196](https://image.3001.net/images/20250423/1745416053_6808ef75c0115ca027599.png!small?1745416034196)

## PS

是一台挺简单的靶机比较考验对目标的优先级排序

# vulnhub靶机 # OSCP

免责声明

1.一般免责声明：本文所提供的技术信息仅供参考，不构成任何专业建议。读者应根据自身情况谨慎使用且应遵守《中华人民共和国网络安全法》，作者及发布平台不对因使用本文信息而导致的任何直接或间接责任或损失负责。

2. 适用性声明：文中技术内容可能不适用于所有情况或系统，在实际应用前请充分测试和评估。若因使用不当造成的任何问题，相关方不承担责任。

3. 更新声明：技术发展迅速，文章内容可能存在滞后性。读者需自行判断信息的时效性，因依据过时内容产生的后果，作者及发布平台不承担责任。

本文为 独立观点，未经授权禁止转载。
如需授权、对文章有疑问或需删除稿件，请联系 FreeBuf
客服小蜜蜂（微信：freebee1024）

被以下专辑收录，发现更多精彩内容

+ 收入我的专辑

+ 加入我的收藏

展开更多

相关推荐

![]()

关 注

* 0 文章数
* 0 关注者

文章目录

前期信息搜集

渗透阶段

提权

PS

![](/images/logo_b.png)

本站由阿里云 提供计算与安全服务

### 用户服务

* [有奖投稿](https://www.freebuf.com/write)
* [提交漏洞](https://www.vulbox.com/bounties/detail-72)
* [参与众测](https://www.vulbox.com/projects/list)
* [商城](https://shop.freebuf.com)

### 企业服务

* [安全咨询](https://company.freebuf.com)
* [产业全景图](https://www.freebuf.com/news/307349.html)
* [企业SRC](https://www.vulbox.com/service/src)
* [安全众测](https://www.vulbox.com/)

### 合作信息

* [斗象官网](https://www.tophant.com/)
* [广告投放](https://www.freebuf.com/articles/444331.html)
* [联系我们](https://www.freebuf.com/articles/444332.html)

### 关于我们

* [关于我们](https://www.freebuf.com/news/others/864.html)
* 微信公众号
* [新浪微博](http://weibo.com/freebuf)

### 战略伙伴

* [![](https://image.3001.net/images/20191017/1571306518_5da83c1686dd9.png)](http://www.aliyun.com/?freebuf)

### FreeBuf知识大陆

![](https://image.3001.net/images/20250703/1751535036_68664dbcae34ac40bb9e7.png)

扫码把安全装进口袋

* [斗象科技](https://www.tophant.com/)
* [FreeBuf](https://www.freebuf.com)
* [漏洞盒子](https://www.vulbox.com/)
* [斗象智能安全](https://ai.tophant.com/)
* [免责条款](https://www.freebuf.com/dis)
* [协议条款](https://my.freebuf.com/AgreeProtocol/duty)

Copyright © 2025 WWW.FREEBUF.COM All Rights Reserved
[沪ICP备2024099014号](https://beian.miit.gov.cn/#/Integrated/index) | [沪公安网备
![](https://image.3001.net/images/20200106/1578291342_5e12d08ec2379.png)](http://www.beian.gov.cn/portal/registerSystemInfo?recordcode=31011502009321)