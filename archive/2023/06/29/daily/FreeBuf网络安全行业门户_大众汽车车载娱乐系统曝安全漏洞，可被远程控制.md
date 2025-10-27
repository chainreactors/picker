---
title: 大众汽车车载娱乐系统曝安全漏洞，可被远程控制
url: https://www.freebuf.com/news/370513.html
source: FreeBuf网络安全行业门户
date: 2023-06-29
fetch_date: 2025-10-04T11:48:10.015190
---

# 大众汽车车载娱乐系统曝安全漏洞，可被远程控制

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

大众汽车车载娱乐系统曝安全漏洞，可被远程控制

* ![]()
* 关注

* [资讯](https://www.freebuf.com/news)

大众汽车车载娱乐系统曝安全漏洞，可被远程控制

2023-06-28 13:47:21

所属地 上海

![](https://image.3001.net/images/20230628/1687920131_649b9e03cb5b70321000b.png!small)

根据GitHub的一份报告，大众汽车Discover Media信息娱乐系统的漏洞是在2023年2月28日发现的。

该漏洞可能会使未打补丁的系统遭到拒绝服务（DoS）攻击。该漏洞起初是由大众汽车的用户发现的，随后大众汽车方面确认了该漏洞，漏洞的标识为CVE-2023-34733。

## 关于漏洞详情

根据GitHub的报告，发现并报告该漏洞的人所使用的车型是大众捷达2021。根据NIST的报告，该漏洞的评分是6.8，是一个中等严重漏洞。

![](https://image.3001.net/images/20230628/1687921123_649ba1e3ddb4f94b7252e.png!small)

起初该用户将他的笔记本电脑连接到大众汽车的USB端口，并用模糊器生成媒体文件。随后进行模糊测试，以找出大众汽车媒体系统的漏洞。该实验是在包括MP3、WMA、WAV等媒体文件上进行的。

该用户在GitHub上写道，"由于大众汽车的媒体播放器比预期的更强大，我专门为大众汽车的信息娱乐系统创建了一个单独的媒体文件模糊器。我每天模糊处理2万多个媒体文件，经过一天的模糊测试，发现了OGG文件的漏洞"。

然后通过模糊测试识别了一个媒体文件，导致大众汽车媒体系统中的漏洞被触发。这也导致了大众汽车信息娱乐系统在关闭后无法打开。

当USB插入端口时，媒体文件会自动播放，信息娱乐系统会被强行终止，这个现象可以通过手动重启大众汽车信息娱乐系统来解决。

据观察，该漏洞可能导致远程代码执行等安全问题。

## 大众汽车对该漏洞的回应

该漏洞是在大众汽车媒体信息娱乐系统软件版本0876中发现的。在收到用户的这份报告后，德国汽车巨头对该漏洞进行了确认。

![](https://image.3001.net/images/20230628/1687921036_649ba18c58eb44fe815fc.png!small)大众汽车给用户的回复截图（照片：GitHub）

该公司让其事件响应小组分析了大众汽车信息娱乐系统的漏洞，后来又让研发部门分析了这个漏洞。随后他们向上述电子邮件截图中名为 "zj3t "的用户确认了该漏洞，并表示该漏洞是一个产品质量的问题，会及时改进。

![1687950373_649c1425607bd1cadef52.jpg!small?1687950374532](https://image.3001.net/images/20230628/1687950373_649c1425607bd1cadef52.jpg!small?1687950374532)

![1687950384_649c14303e6cb514682fd.jpg!small](https://image.3001.net/images/20230628/1687950384_649c14303e6cb514682fd.jpg!small)

【如群已满或有疑问，可扫码添加FB小蜜蜂微信哦！】

> 参考链接：https://thecyberexpress.com/vulnerability-in-volkswagen-discover-media/

# 资讯 # 漏洞

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

关于漏洞详情

大众汽车对该漏洞的回应

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