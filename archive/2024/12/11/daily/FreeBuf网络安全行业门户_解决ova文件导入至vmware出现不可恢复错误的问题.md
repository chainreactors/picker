---
title: 解决ova文件导入至vmware出现不可恢复错误的问题
url: https://www.freebuf.com/sectool/390811.html
source: FreeBuf网络安全行业门户
date: 2024-12-11
fetch_date: 2025-10-06T19:40:58.317486
---

# 解决ova文件导入至vmware出现不可恢复错误的问题

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

解决ova文件导入至vmware出现不可恢复错误的问题

* ![]()
* 关注

* [工具](https://www.freebuf.com/articles/sectool)

解决ova文件导入至vmware出现不可恢复错误的问题

2024-12-10 14:54:55

所属地 广东省

最近在打vulnhub靶机时，有时候下载的.ova文件导入进vmware里面，但是无法修改网络模式，一点击就会出现不可恢复错误

这里我用me and my girlfriend靶机做测试

刚开始就正常导入，在vmware左侧空白处右键选择导入的靶机

![1706276961_65b3b86113625edbb3bf9.png!small](https://image.3001.net/images/20240126/1706276961_65b3b86113625edbb3bf9.png!small)

然后进行命名，点击导入

![1706279486_65b3c23e8b2aa0fa76400.png!small](https://image.3001.net/images/20240126/1706279486_65b3c23e8b2aa0fa76400.png!small)

然后会出现这个问题，点击重试即可

![1706277069_65b3b8cd15351a5b8adb0.png!small](https://image.3001.net/images/20240126/1706277069_65b3b8cd15351a5b8adb0.png!small)

这里则可以成功导入![1706279504_65b3c2502a7c3af3b4876.png!small](https://image.3001.net/images/20240126/1706279504_65b3c2502a7c3af3b4876.png!small)

导入成功后，我们要更改靶机的网络设置，把kali和靶机都设置为nat模式，才能扫到靶机的ip

但是这里我们点击网络适配器进行修改时，则会出现不可恢复错误

![1706279604_65b3c2b421f20941946ab.png!small](https://image.3001.net/images/20240126/1706279604_65b3c2b421f20941946ab.png!small)

然后闪退

这里上网看了很多博客，**发现是版本不兼容问题，解决方法就是让靶机版本降级**

先点击导入好的靶机，然后点击虚拟机->管理->更改硬件兼容性

![1706279647_65b3c2df807a3f129f4a6.png!small](https://image.3001.net/images/20240126/1706279647_65b3c2df807a3f129f4a6.png!small)然后下一步

![1706277534_65b3ba9e90026d98e2530.png!small](https://image.3001.net/images/20240126/1706277534_65b3ba9e90026d98e2530.png!small)

这里我们选择16.2版本即可，点击下一步

![1706277587_65b3bad31615015d612ca.png!small](https://image.3001.net/images/20240126/1706277587_65b3bad31615015d612ca.png!small)

创建新克隆然后下一步

![1706277621_65b3baf5e1c0042d83284.png!small](https://image.3001.net/images/20240126/1706277621_65b3baf5e1c0042d83284.png!small)

重新命名然后完成克隆即可

![1706279689_65b3c309c224aad307df3.png!small](https://image.3001.net/images/20240126/1706279689_65b3c309c224aad307df3.png!small)

![1706277713_65b3bb51e8624733c8e6a.png!small](https://image.3001.net/images/20240126/1706277713_65b3bb51e8624733c8e6a.png!small)

完成克隆后关闭

![1706277781_65b3bb95ed54baf6520ba.png!small](https://image.3001.net/images/20240126/1706277781_65b3bb95ed54baf6520ba.png!small)

这里我们打开克隆好的靶机，再把网络模式设置为nat模式，没有任何问题

![1706279984_65b3c430f19194babb30e.png!small](https://image.3001.net/images/20240126/1706279984_65b3c430f19194babb30e.png!small)

# 渗透测试 # 靶机环境 # 靶机渗透

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