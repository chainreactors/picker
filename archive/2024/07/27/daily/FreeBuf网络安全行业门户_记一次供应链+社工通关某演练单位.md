---
title: 记一次供应链+社工通关某演练单位
url: https://www.freebuf.com/articles/web/406681.html
source: FreeBuf网络安全行业门户
date: 2024-07-27
fetch_date: 2025-10-06T17:42:53.685823
---

# 记一次供应链+社工通关某演练单位

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

记一次供应链+社工通关某演练单位

* ![]()
* 关注

* [Web安全](https://www.freebuf.com/articles/web)

记一次供应链+社工通关某演练单位

2024-07-26 11:17:29

![](https://image.3001.net/images/20240308/1709876354_65eaa4828e91d155430d9.png)
本文由
创作，已纳入「FreeBuf原创奖励计划」，未授权禁止转载

## 0x01 背景介绍

金融行业的攻防演练早已过了简单扫描通过1/Nday漏洞可以直接突破边界的时期，社工和供应链攻击成了攻击常态。

本文介绍某一次演练项目，通过供应链+社工的组合攻击，绕过安全设备防护，打穿目标的案例。

喜欢的师傅可以关注公众号“灵悉实验室”

## 0x02 突破路径

1、伪造登录页钓鱼获取账号密码

2、登录系统后台文件上传getshell（云服务器）

3、登录页水坑攻击获取办公pc权限（dns上线cs）

4、对抗绕过安全厂商ac设备防护，转http上线cs

5、内网横向打下域控

## 0x03 突破详情

经过简单的扫描踩点，发现该单位暴露面小，且系统都为自主研发，没有发现边界突破的入口点。并且边界存在waf防护，没有0day漏洞的情况下举步维艰。

针对收集到的web资产逐一分析，发现带有该单位logo的电子学习平台，但是资产在云上，不属于客户it资产。在没有找到其他登录口的情况下，只能以此为突破口进行尝试。

制作钓鱼页面，使用EmailAll收集目标邮箱，并批量发送100封钓鱼邮件。

![1721635431_669e1267a3000a68c5387.png!small?1721635434496](https://image.3001.net/images/20240722/1721635431_669e1267a3000a68c5387.png!small?1721635434496)

经过了一晚上的等待，运气不错，终于等到了一人提交

![1721635448_669e1278920040ee94bff.png!small?1721635449595](https://image.3001.net/images/20240722/1721635448_669e1278920040ee94bff.png!small?1721635449595)

成功登录

![1721635461_669e1285104ce56bc3c0b.png!small?1721635463115](https://image.3001.net/images/20240722/1721635461_669e1285104ce56bc3c0b.png!small?1721635463115)

文件上传漏洞getshell，并通过cs上线。由于是一台云服务器，与实际内网不通，所以想着只能刷一些数据分。

![1721635473_669e12918ed3c18e09ffa.png!small?1721635474671](https://image.3001.net/images/20240722/1721635473_669e12918ed3c18e09ffa.png!small?1721635474671)

找到数据库配置文件，发现该单位员工信息

![1721635494_669e12a6b6e5200b14b82.png!small?1721635495759](https://image.3001.net/images/20240722/1721635494_669e12a6b6e5200b14b82.png!small?1721635495759)

基于上述信息可以得到该平台为第三方供应商提供的在线电子学习平台，所有员工会定期登录平台进行学习。加上我们基本获取了该单位所有员工的信息，可以进一步进行精准打击。

所以下一步的思路：登录页面水坑攻击打个人办公pc进办公网！！

和裁判报备通过，水坑攻击走起！

![1721635509_669e12b5f12574c58a755.png!small?1721635513255](https://image.3001.net/images/20240722/1721635509_669e12b5f12574c58a755.png!small?1721635513255)

将运维人员邮箱筛选出来进行鱼叉攻击，发送邮件告知其需要登录学习网站修改密码。如果点了“立即升级”并运行，电脑就立即上线。这里遇到一个问题，很多金融单位会限制办公电脑上网，但是一般只会限制http，而很容易把dns给忽略，所以走cs dns上线可以尽量多的上线目标。

很快，上线了一台pc，成功进入办公网

![1721635523_669e12c39595028eddcc4.png!small?1721635524286](https://image.3001.net/images/20240722/1721635523_669e12c39595028eddcc4.png!small?1721635524286)

如果试过dns协议进行cs操作，延迟是非常之高的，正常的执行一条命令可能要等待1分钟，内网横向在这样的时间成本下基本冲不动。尝试上线http listener，但是失败了。。。

简单的信息收集后，发现使用了某安全厂商的ac上网设备，pc终端输入账号密码通过ac认证后可以访问互联网，而限制用户能否访问目标网站，一般都是通过配置http host头白名单来实现。

试了下公司官网，http可以正常访问，所以cs listener中配置host为公司官网域名，成功http上线。

![1721635537_669e12d15c26c166ec179.png!small?1721635538098](https://image.3001.net/images/20240722/1721635537_669e12d15c26c166ec179.png!small?1721635538098)

接下来就是愉快的内网横向，扫到域控，与裁判报备后，使用CVE-2020-1472获取域控权限。

![1721635549_669e12dd8771abb5836a2.png!small?1721635550524](https://image.3001.net/images/20240722/1721635549_669e12dd8771abb5836a2.png!small?1721635550524)

至此结束。

## 0x04 复盘总结

1、员工安全意识薄弱

2、供应商系统未定期进行安全测试

3、内网系统普遍防护薄弱，未加固

4、安全设备未更新至最新，导致被绕过

进技术交流群请添加 wxid\_022wcbhglw0d22

# 渗透测试 # 网络安全 # web安全 # 内网渗透 # 网络安全技术

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

0x01 背景介绍

0x02 突破路径

0x03 突破详情

0x04 复盘总结

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