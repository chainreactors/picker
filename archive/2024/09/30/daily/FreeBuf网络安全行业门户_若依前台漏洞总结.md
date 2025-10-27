---
title: 若依前台漏洞总结
url: https://www.freebuf.com/articles/web/411980.html
source: FreeBuf网络安全行业门户
date: 2024-09-30
fetch_date: 2025-10-06T18:24:52.027067
---

# 若依前台漏洞总结

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

若依前台漏洞总结

* ![]()
* 关注

* [Web安全](https://www.freebuf.com/articles/web)

若依前台漏洞总结

2024-09-29 09:24:51

所属地 福建省

![](https://image.3001.net/images/20240308/1709876354_65eaa4828e91d155430d9.png)
本文由
创作，已纳入「FreeBuf原创奖励计划」，未授权禁止转载

# 一、若依特征

绿若依：icon\_hash=”706913071”

![1727572725_66f8aaf5913854af7b059.png!small?1727572727336](https://image.3001.net/images/20240929/1727572725_66f8aaf5913854af7b059.png!small?1727572727336)

![1727572746_66f8ab0acfbd90eff09bb.png!small?1727572748450](https://image.3001.net/images/20240929/1727572746_66f8ab0acfbd90eff09bb.png!small?1727572748450)绿若依常见登录页面

![1727572755_66f8ab13c1e10317f12ce.png!small?1727572757872](https://image.3001.net/images/20240929/1727572755_66f8ab13c1e10317f12ce.png!small?1727572757872)

蓝若依：icon\_hash=” -1231872293”

![1727572765_66f8ab1d95d8980459c26.png!small?1727572767228](https://image.3001.net/images/20240929/1727572765_66f8ab1d95d8980459c26.png!small?1727572767228)![1727572770_66f8ab22ca3194344356a.png!small?1727572772478](https://image.3001.net/images/20240929/1727572770_66f8ab22ca3194344356a.png!small?1727572772478)

蓝若依常见登录界面![1727572783_66f8ab2fda870fbbfce26.png!small?1727572785725](https://image.3001.net/images/20240929/1727572783_66f8ab2fda870fbbfce26.png!small?1727572785725)

若依框架通常使用的组件有springboot、webpack、shiro、druid、swagger、redis、zookeeper、mysql等

# 二、未授权访问

常见为绿若依，绿若依一般都会常用webpack组件，F12查看js文件，找到一个名为appxxxxxx.js的文件，搜索baseurl，找到api路径![1727572792_66f8ab387656bfe3b22d2.png!small?1727572794339](https://image.3001.net/images/20240929/1727572792_66f8ab387656bfe3b22d2.png!small?1727572794339)

常见的api路径有：/api、/dev-api、/prod-api等

也有一些api路径指向的是另一个网址![1727572798_66f8ab3e79f5aec4a9f85.png!small?1727572800300](https://image.3001.net/images/20240929/1727572798_66f8ab3e79f5aec4a9f85.png!small?1727572800300)

访问后为如下界面![1727572806_66f8ab4688d3c483c8dd7.png!small?1727572808185](https://image.3001.net/images/20240929/1727572806_66f8ab4688d3c483c8dd7.png!small?1727572808185)

对其进行目录扫描能发现许多信息

常见的未授权有druid、springboot、swagger

在api后面拼接对应路径

## druid未授权

druid：<http://ip/baseurl/druid/login.html>![1727572819_66f8ab536bd4b0f14a210.png!small?1727572821055](https://image.3001.net/images/20240929/1727572819_66f8ab536bd4b0f14a210.png!small?1727572821055)

如果有未授权可以直接访问，需要账号密码的可以配合若依系统弱口令进行登录

常见弱口令有：admin/admin、admin\admin123、admin\123456、ry\123456、ruoyi\123456

登录后重点查看Session监控和URI监控两处

Session监控里存在历史登录的Session，可以尝试替换Session值进行登录![1727572829_66f8ab5d50e2ecf0c6ff4.png!small?1727572833031](https://image.3001.net/images/20240929/1727572829_66f8ab5d50e2ecf0c6ff4.png!small?1727572833031)

URI监控处存在大量接口路径，可以进一步访问获取敏感信息![1727572856_66f8ab78c27eb5bd8fffc.png!small?1727572864241](https://image.3001.net/images/20240929/1727572856_66f8ab78c27eb5bd8fffc.png!small?1727572864241)

## swagger未授权

swagger：<http://ip/baseurl/swagger-ui/>![1727572857_66f8ab79ecea1486169a3.png!small?1727572864242](https://image.3001.net/images/20240929/1727572857_66f8ab79ecea1486169a3.png!small?1727572864242)

可以通过接口文档进行下一步操作，如果发现大量接口可以使用工具进行自动化测试，如swagger-hack![1727572861_66f8ab7dbdea8c67925dd.png!small?1727572864243](https://image.3001.net/images/20240929/1727572861_66f8ab7dbdea8c67925dd.png!small?1727572864243)

## springboot未授权

springboot：<http://ip/baseurl/actuator>![1727572858_66f8ab7ade9ee2f89361e.png!small?1727572864241](https://image.3001.net/images/20240929/1727572858_66f8ab7ade9ee2f89361e.png!small?1727572864241)

重点关注/actuator/heapdump路径

访问下载后使用工具对其进行分析可获得大量敏感信息![1727572864_66f8ab806136b32a8aef6.png!small?1727572866062](https://image.3001.net/images/20240929/1727572864_66f8ab806136b32a8aef6.png!small?1727572866062)![1727572868_66f8ab849db7e63eaf82b.png!small?1727572870734](https://image.3001.net/images/20240929/1727572868_66f8ab849db7e63eaf82b.png!small?1727572870734)

## redis未授权

若依系统通常会用到mysql和redis数据库，可以尝试redis未授权访问，或者对数据库进行弱口令爆破

# 三、弱口令+默认密码

常见登录界面路径为：/login

如果页面访问显示不正常，可添加默认访问路径尝试是否显示正常

/login?redirect=%2Findex

/baseurl/login?redirect=%2Findex

有些若依系统的账号密码会直接显示在前台登录框中，可以直接利用进行登录![1727572877_66f8ab8da613b0452cabe.png!small?1727572881914](https://image.3001.net/images/20240929/1727572877_66f8ab8da613b0452cabe.png!small?1727572881914)

常见的弱口令有：admin/admin、admin\admin123、admin\123456、ry\123456、ry\admin123、ruoyo\admin123、ruoyi\123456

# 四、注册接口

在弱口令等方法都试过之后还无法登录，可以尝试访问注册接口看看系统是否允许注册

访问：/register

不允许注册![1727572884_66f8ab94974e7f5c473b4.png!small?1727572886504](https://image.3001.net/images/20240929/1727572884_66f8ab94974e7f5c473b4.png!small?1727572886504)

允许注册

![1727572890_66f8ab9a1d4a5be7a0db6.png!small?1727572891925](https://image.3001.net/images/20240929/1727572890_66f8ab9a1d4a5be7a0db6.png!small?1727572891925)

注册成功后就可以使用注册账号登录进一步测试

# 五、shiro反序列化

若依登录界面通常都采用了rememberMe字段，如果存在默认的key值，则可以进一步利用，实现shiro反序列化

![1727572902_66f8aba685d91c4bc655b.png!small?1727572904315](https://image.3001.net/images/20240929/1727572902_66f8aba685d91c4bc655b.png!small?1727572904315)

# 六、未授权文件上传

常见于绿若依系统，F12查找js中的app.js，搜索uploadurl![1727572910_66f8abae9a9f0ccc475f2.png!small?1727572912373](https://image.3001.net/images/20240929/1727572910_66f8abae9a9f0ccc475f2.png!small?1727572912373)

访问对应路径/baseurl/common/upload

有鉴权![1727572916_66f8abb40de0f700e847c.png!small?1727572917672](https://image.3001.net/images/20240929/1727572916_66f8abb40de0f700e847c.png!small?1727572917672)

未授权![1727572920_66f8abb8c423200a3ff48.png!small?1727572922849](https://image.3001.net/images/20240929/1727572920_66f8abb8c423200a3ff48.png!small?1727572922849)

构造对应的文件上传请求包![1727572929_66f8abc1e52370d7d1772.png!small?1727572931753](https://image.3001.net/images/20240929/1727572929_66f8abc1e52370d7d1772.png!small?1727572931753)

访问返回的文件路径![1727572934_66f8abc6f045c980da676.png!small?1727572936659](https://image.3001.net/images/20240929/1727572934_66f8abc6f045c980da676.png!small?1727572936659)

有些网站做了限制，只允许白名单上传![1727572940_66f8abccc7b2feb5310e7.png!small?1727572942465](https://image.3001.net/images/20240929/1727572940_66f8abccc7b2feb5310e7.png!small?1727572942465)

这种情况可以打带有xss的html文件，造成存储xss

没限制的网站可以直接getshell

# 安全漏洞 # 若依

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

druid未授权

swagger未授权

springboot未授权

redis未授权

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
*...