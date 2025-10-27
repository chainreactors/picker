---
title: 源海拾贝 | DarkAngel - 全自动白帽漏洞扫描器
url: https://www.anquanke.com/post/id/284346
source: 安全客-有思想的安全新媒体
date: 2023-01-06
fetch_date: 2025-10-04T03:08:33.101110
---

# 源海拾贝 | DarkAngel - 全自动白帽漏洞扫描器

首页

阅读

* [安全资讯](https://www.anquanke.com/news)
* [安全知识](https://www.anquanke.com/knowledge)
* [安全工具](https://www.anquanke.com/tool)

活动

社区

学院

安全导航

内容精选

* [专栏](/column/index.html)
* [精选专题](https://www.anquanke.com/subject-list)
* [安全KER季刊](https://www.anquanke.com/discovery)
* [360网络安全周报](https://www.anquanke.com/week-list)

# 源海拾贝 | DarkAngel - 全自动白帽漏洞扫描器

阅读量**1091650**

发布时间 : 2023-01-05 12:00:37

**x**

##### 译文声明

本文是翻译文章

译文仅供参考，具体内容表达以及含义原文为准。

![]()

---

DarkAngel 是一款全自动白帽漏洞扫描器，从hackerone、bugcrowd资产监听到漏洞报告生成、企业微信通知。

DarkAngel 下载地址：[github.com/Bywalks/DarkAngel](https://github.com/Bywalks/DarkAngel)

当前已支持的功能：

* hackerone资产监听；
* bugcrowd资产监听；
* 自定义资产添加；
* 子域名扫描；
* 网站指纹识别；
* 漏洞扫描；
* 漏洞报告自动生成；
* 企业微信通知扫描结果；
* 前端显示扫描结果；

## 自动生成漏洞报告

自动生成漏洞报告 – MarkDown格式 – 存放地址/root/darkangel/vulscan/results/report

![]()

支持自添加漏洞报告模板，目前已添加漏洞报告模板如下，漏洞名配置为nuclei模板文件名即可

![]()

自定义漏洞报告模板格式

![]()

## 企业微信通知

可先查看如何获取配置：[企业微信开发接口文档](https://developer.work.weixin.qq.com/document/path/90487)

获取参数后，在/root/darkangel/vconfig/config.ini中配置参数，即可启用企业微信通知

微信通知 – 漏洞结果

![]()

微信通知 – 扫描进程

![]()

## 安装

整体项目架构ES+Kibana+扫描器，所以安装需要三个部分

ES镜像：

```
拉取ES镜像
docker pull bywalkss/darkangel:es7.9.3

部署ES镜像
docker run -e ES_JAVA_OPTS="-Xms1024m -Xms1024m" -d -p 9200:9200 -p 9300:9300 --name elasticsearch elasticsearch:7.9.3

查看日志
docker logs -f elasticsearch

出现问题，执行命令
sysctl -w vm.max_map_count=262144

重启docker
docker start elasticsearch
```

Kibana镜像：

```
拉取Kibana镜像
docker pull bywalkss/darkangel:kibana7.9.3

部署Kibana镜像（修改一下es-ip）
docker run --name kibana -e ELASTICSEARCH_URL=http://es-ip:9200 -p 5601:5601 -d docker.io/bywalkss/darkangel:kibana7.9.3

查看日志
docker logs -f elasticsearch

出现问题，执行命令
sysctl -w vm.max_map_count=262144

重启docker
docker start elasticsearch
```

扫描器镜像：

```
拉取扫描器镜像
docker pull bywalkss/darkangel:v1

部署扫描器
docker run -it -d -v /root/darkangel:/root/darkangel --name darkangel bywalkss/darkangel:v1
```

docker容器内挂载目录无权限
运行容器时：—privileged=true

## 用法

```
usage:  [-h] [--scan-new-domain]
        [--add-domain-and-scan ADD_DOMAIN_AND_SCAN [ADD_DOMAIN_AND_SCAN ...]]
        [--offer-bounty {yes,no}] [--nuclei-file-scan]
        [--nuclei-file-scan-by-new-temp NUCLEI_FILE_SCAN_BY_NEW_TEMP]
        [--nuclei-file-scan-by-new-add-temp NUCLEI_FILE_SCAN_BY_NEW_ADD_TEMP]
        [--nuclei-file-scan-by-temp-name NUCLEI_FILE_SCAN_BY_TEMP_NAME]
        [--nuclei-file-polling-scan] [--delete]

DarkAngel is a white hat scanner. Every user makes the Internet more secure.

--------------------------------------------------------------------------------

optional arguments:
  -h, --help            show this help message and exit
  --scan-new-domain     scan new domain from h1 and bc
  --add-domain-and-scan ADD_DOMAIN_AND_SCAN [ADD_DOMAIN_AND_SCAN ...]
                        scan new domain from h1 and bc
  --offer-bounty {yes,no}
                        set add domain is bounty or no bounty
  --nuclei-file-scan    scan new domain from h1 and bc
  --nuclei-file-scan-by-new-temp NUCLEI_FILE_SCAN_BY_NEW_TEMP
                        use new template scan five file by nuclei
  --nuclei-file-scan-by-new-add-temp NUCLEI_FILE_SCAN_BY_NEW_ADD_TEMP
                        add new template scan five file by nuclei
  --nuclei-file-scan-by-temp-name NUCLEI_FILE_SCAN_BY_TEMP_NAME
                        use template scan five file by nuclei
  --nuclei-file-polling-scan
                        five file polling scan by nuclei
```

### —scan-new-domain

`$ python3 darkangel.py --scan-new-domain`

* 监听hackerone和bugcrowd域名并进行扫描（第一次使用时会把hackerone和bugcrowd域名全部添加进去，资产过多的情况下做好准备，扫描时间很长）

![]()

### —add-domain-and-scan

`$ python3 darkangel.py --add-domain-and-scan program-file-name1 program-file-name2 --offer-bounty yes/no`

* 自定义添加扫描域名，并对这些域名进行漏洞扫描
* 文件名为厂商名称，文件内存放需扫描域名
* 需提供—offer-bounty参数，设置域名是否提供赏金

![]()

![]()

扫描结束后，会把子域名结果存在在/root/darkangel/vulscan/results/urls目录，按照是否提供赏金分别存放在，bounty\_temp\_urls\_output.txt、nobounty\_temp\_urls\_output.txt文件内

### —nuclei-file-scan

`$ python3 darkangel.py --nuclei-file-scan`

* 用nuclei扫描20个url文件

![]()

url列表存放位置

![]()

### —nuclei-file-polling-scan

`$ python3 darkangel.py --nuclei-file-polling-scan`

* 轮询用nuclei扫描20个url文件，可把该进程放在后台，轮询扫描，监听是否url列表是否存在新漏洞出现

### —nuclei-file-scan-by-new-temp

`$ python3 darkangel.py --nuclei-file-scan-by-new-temp nuclei-template-version`

* 监听nuclei-template更新，当更新时，对url列表进行扫描

当前nuclei-template版本为9.3.1

![]()

执行命令，监听9.3.2版本更新

![]()

企业微信通知

![]()

url列表存放位置

![]()

### —nuclei-file-scan-by-new-add-temp

`$ python3 darkangel.py --nuclei-file-scan-by-new-add-temp nuclei-template-id`

* 监听nuclei单template更新，当更新时，用该template对url列表进行扫描，这里是打了个时间差，某些时候先提交tempalte，验证后才会加入nuclei模板，在还未加入时，我们已经监听并进行扫描，扫描后id会自动增加，监听并进行扫描

查看nuclei单template的id，这里为6296

![]()

执行命令，对该template进行扫描

![]()

url列表存放位置

![]()

### —nuclei-file-scan-by-temp-name

`$ python3 darkangel.py --nuclei-file-scan-by-temp-name nuclei-template-name`

* 用单template对url列表进行扫描

![]()

## 结果显示

前端 – 扫描厂商

![]()

前端 – 扫描域名

![]()

前端 – 扫描结果

![]()

微信通知 – 扫描进程

![]()

微信通知 – 漏洞结果

![]()

## 注意事项

* 本工具仅用于合法合规用途，严禁用于违法违规用途。

本文翻译自 原文链接。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**bywalks**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/284346](/post/id/284346)

安全KER - 有思想的安全新媒体

本文转载自:

如若转载,请注明出处：

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [安全工具](/tag/%E5%AE%89%E5%85%A8%E5%B7%A5%E5%85%B7)
* [扫描器](/tag/%E6%89%AB%E6%8F%8F%E5%99%A8)

**+1**32赞

收藏

![](https://p5.ssl.qhimg.com/t010857340ce46bb672.jpg)bywalks

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p4.ssl.qhimg.com/t014757b72460d855bf.png)

[![](https://p5.ssl.qhimg.com/t010857340ce46bb672.jpg)](/member.html?memberId=167970)

[bywalks](/member.html?memberId=167970)

这个人太懒了，签名都懒得写一个

* 文章
* **1**

* 粉丝
* **0**

### TA的文章

* ##### [源海拾贝 | DarkAngel - 全自动白帽漏洞扫描器](/post/id/284346)

  2023-01-05 12:00:37

### 相关文章

* ##### [SiCat：漏洞检测新工具](/post/id/293257)

  2024-02-18 16:36:45
* ##### [使用 gopacket 从网络捕获及重组数据包](/post/id/288460)

  2023-06-12 15:58:16
* ##### [负载测试框架 Locust](/post/id/288620)

  2023-06-12 15:46:47
* ##### [UI 和 API 自动化测试神器 - Playwright](/post/id/286627)

  2023-02-23 10:30:37
* ##### [基于蜻蜓打造在线SQL注入检测系统](/post/id/286061)

  2023-02-07 12:00:32
* ##### [用 Goby 通过反序列化漏洞一键打入内存马【利用篇】](/post/id/285539)

  2023-01-17 15:30:43
* ##### [高效率开发Web安全扫描器之路（一）](/post/id/283900)

  2023-01-06 14:00:19

### 热门推荐

文章目录

* [自动生成漏洞报告](#h2-0)
* [企业微信通知](#h2-1)
* [安装](#h2-2)
* [用法](#h2-3)
  + [—scan-new-domain](#h3-4)
  + [—add-domain-and-scan](#h3-5)
  + [—nuclei-file-scan](#h3-6)
  + [—nuclei-file-polling-scan](#h3-7)
  + [—nuclei-file-scan-by-new-temp](#h3-8)
  + [—nuclei-file-scan-by-new-add-temp](#h3-9)
  + [—nuclei-file-scan-by-temp-name](#h3-10)
* [结果显示](#h2-11)
* [注意事项](#h2-12)

![](https://p0.qhimg.com/t11098f6bcd5614af4bf21ef9b5.png)

安全KER

* [关于我们](/about)
* [联系我们](/note/contact)
* [用户协议](/note/protocol)
* [隐私协议](/note/privacy)

商务合作

* [合作内容](/note/business)
* [联系方式](/note/contact)
* [友情链接](/link)

内容需知

* [投稿须知](https://www.anquanke.com/contribute/tips)
* [转载须知](/note/repost)
* 官网QQ群：568681302

合作单位

* [![安全KER](https://p0.ssl.qhimg.com/t01592a959354157bc0.png)](http://www.cert.org.cn/)
* [![安全KER](https://p0.ssl.qhimg.com/t014f76fcea94035e47.png)](http://www.cnnvd.org.cn/)

Copyright © 北京奇虎科技有限公司 三六零数字安全科技集团有限公司 安全KER All Rights Reserved [京ICP备08010314号-66](https://beian.miit.gov.cn/)[![](https://icon.cnzz.com/img/pic.gif)](https://www.cnzz.com/stat/website.php?web_id=1271278035 "站长统计")

微信二维码

**X**![安全KER](https://p0.ssl.qhimg.com/t0151209205b47f2270.jpg)