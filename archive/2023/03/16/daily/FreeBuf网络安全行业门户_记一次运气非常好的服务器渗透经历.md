---
title: 记一次运气非常好的服务器渗透经历
url: https://www.freebuf.com/vuls/360538.html
source: FreeBuf网络安全行业门户
date: 2023-03-16
fetch_date: 2025-10-04T09:44:53.539728
---

# 记一次运气非常好的服务器渗透经历

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

记一次运气非常好的服务器渗透经历

* ![]()
* 关注

* [漏洞](https://www.freebuf.com/articles/vuls)

记一次运气非常好的服务器渗透经历

2023-03-15 16:10:17

所属地 湖南省

![](https://image.3001.net/images/20240308/1709876354_65eaa4828e91d155430d9.png)
本文由
创作，已纳入「FreeBuf原创奖励计划」，未授权禁止转载

平平无奇的客服平台：

![202303151533719.png](https://image.3001.net/images/20230315/1678867817_64117d69ace9fc36b7975.png!small)

这个客服平台是有RCE的，如果上传到的不是oss服务器，存储在本地服务器的话，

在返回端口的url是存在st2。

![202303151533720.png](https://image.3001.net/images/20230315/1678867818_64117d6abae0933b094cd.png!small)

![202303151533722.png](https://image.3001.net/images/20230315/1678867819_64117d6bce64ba219cdbb.png!small)

root权限，由于是客服后台服务器，没有啥有用价值的信息。

![202303151533723.png](https://image.3001.net/images/20230315/1678867821_64117d6d9a6a0d628d5ce.png!small)

直接替换私钥连服务器。

![202303151533724.png](https://image.3001.net/images/20230315/1678867823_64117d6f015200b8e4d82.png!small)

继续翻找有用的信息。

【----帮助网安学习，以下所有学习资料免费领！加vx：yj009991，备注“freebuf”获取！】

① 网安学习成长路径思维导图
② 60+网安经典常用工具包
③ 100+SRC漏洞分析报告
④ 150+网安攻防实战技术电子书
⑤ 最权威CISSP 认证考试指南+题库
⑥ 超1800页CTF实战技巧手册
⑦ 最新网安大厂面试题合集（含答案）
⑧ APP客户端安全检测指南（安卓+IOS）

![202303151533725.png](https://image.3001.net/images/20230315/1678867825_64117d718ac270ae0ef1d.png!small)

![202303151533726.png](https://image.3001.net/images/20230315/1678867826_64117d727ea1e1202d249.png!small)

配置文件里也只有mongodb和redis的连接信息。

![202303151533727.png](https://image.3001.net/images/20230315/1678867827_64117d73ba520ec9a71fe.png!small)

历史命令和登录ip历史是阿里云服务器。

![202303151533728.png](https://image.3001.net/images/20230315/1678867829_64117d75aee69c4b152e0.png!small)

扫下端口，8092有个目录遍历，好像是专门用来放项目的。

![202303151533729.png](https://image.3001.net/images/20230315/1678867830_64117d76a291e911e2d76.png!small)

点开test看看：

![202303151533730.png](https://image.3001.net/images/20230315/1678867831_64117d777a50528b4a768.png!small)

下载过来解包看看：

![202303151533731.png](https://image.3001.net/images/20230315/1678867832_64117d78860814bcfdfcb.png!small)

这咋有个ip，root和密码，不会是那个开发人才留下的吧，泪目了家人们。

![202303151533732.png](https://image.3001.net/images/20230315/1678867833_64117d7979bec36a87eb1.png!small)

尝试连接，还真可以。

![202303151533733.png](https://image.3001.net/images/20230315/1678867834_64117d7aa00dde354f786.png!small)

连接数据库看看，8w多受害者，佩服。

![202303151533734.png](https://image.3001.net/images/20230315/1678867836_64117d7c2c0c9be79f780.png!small)

然后再回到之前扫出来的端口，

8094是有个web项目。

![202303151533735.png](https://image.3001.net/images/20230315/1678867837_64117d7d8308cddbc400e.png!small)

在数据库获取到后台url

![202303151533736.png](https://image.3001.net/images/20230315/1678867838_64117d7eb5ab3a4b81d49.png!small)

配合数据库和登录日志获取到国内技术嫌疑人。

![202303151533737.png](https://image.3001.net/images/20230315/1678867840_64117d8068d521a740cb9.png!small)

![202303151533738.jpeg](https://image.3001.net/images/20230315/1678867841_64117d81acff6576772ad.jpeg!small)

IP和经纬度是在国内。

总结一下，下班。

![202303151533739.png](https://image.3001.net/images/20230315/1678867843_64117d83712dcdb2a5ed6.png!small)

**更多网安技能的在线实操练习，[请点击这里>>](https://www.hetianlab.com/)**

# 渗透测试 # 漏洞挖掘 # 服务器

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