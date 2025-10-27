---
title: Js逆向实战案例
url: https://www.freebuf.com/articles/web/358924.html
source: FreeBuf网络安全行业门户
date: 2023-03-01
fetch_date: 2025-10-04T08:20:23.608028
---

# Js逆向实战案例

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

Js逆向实战案例

* ![]()
* 关注

* [Web安全](https://www.freebuf.com/articles/web)

Js逆向实战案例

2023-02-28 18:19:00

所属地 广东省

### 案例一：某平台数据加密

测试时抓包发现数据包的请求包和返回包内容都进行了加密，且请求包内容形如：abchtrne/rerhn34rhnfe，而返回包内容则为{"data":"reene43jygrnd534htrfdre"}，由此可见该站请求包和返回包内容的加密方式不相同

![1677508806_63fcc0c63128ac9452051.png!small?1677508807349](https://image.3001.net/images/20230227/1677508806_63fcc0c63128ac9452051.png!small?1677508807349)

点击调试器，选中要查看的js文件，点击下方的{}使代码更容易查看

![1677508828_63fcc0dc334a7ed7e70f8.png!small?1677508829056](https://image.3001.net/images/20230227/1677508828_63fcc0dc334a7ed7e70f8.png!small?1677508829056)

寻找加解密关键点，在encryption文件夹下的js文件可以看到该项目很有可能使用的是国密加密算法SM3，SM4

![1677508886_63fcc1168cbb8ebdf3c67.png!small?1677508887134](https://image.3001.net/images/20230227/1677508886_63fcc1168cbb8ebdf3c67.png!small?1677508887134)

在app.js中搜索关键词sm3，sm4，encryptData等关键词，找到加解密方法，以下os和rs方法为请求包加密方法，而cs和ls则为返回包解密函数。由于从数据包中看到的请求体数据和返回包数据的格式分别为字符和json数据。os方法加密后的数据为json格式，因此请求包加密方式为先使用SM4的CBC模式加密，然后使用ECB模式进行加密，最后使用SM3对json数据加密。

![1677508914_63fcc132b896cfd1b1602.png!small?1677508915728](https://image.3001.net/images/20230227/1677508914_63fcc132b896cfd1b1602.png!small?1677508915728)

由于返回包json数据中并没有iv，但是存在data参数，因此返回包的解密方式为先使用ls方法再使用cs方法

![1677508939_63fcc14bca418a1603aff.png!small?1677508940557](https://image.3001.net/images/20230227/1677508939_63fcc14bca418a1603aff.png!small?1677508940557)

使用控制台先调用ls方法第一次解密返回包内容

![1677508957_63fcc15d9b9d93ca30fb0.png!small?1677508958453](https://image.3001.net/images/20230227/1677508957_63fcc15d9b9d93ca30fb0.png!small?1677508958453)

查看第一次解密后的数据

![1677508976_63fcc170c264aebf19278.png!small?1677508977632](https://image.3001.net/images/20230227/1677508976_63fcc170c264aebf19278.png!small?1677508977632)

调用cs方法获取真实数据

![1677508995_63fcc183b517e9448820b.png!small?1677508996290](https://image.3001.net/images/20230227/1677508995_63fcc183b517e9448820b.png!small?1677508996290)

在控制台中debuge调试，t字段中包含加密前的数据

![1677510422_63fcc7160f9633473dcb9.png!small?1677510423836](https://image.3001.net/images/20230227/1677510422_63fcc7160f9633473dcb9.png!small?1677510423836)

在控制台中修改t中的数据即可在加密前修改请求包内容

![1677509040_63fcc1b08ed44bf7f9c7a.png!small?1677509041132](https://image.3001.net/images/20230227/1677509040_63fcc1b08ed44bf7f9c7a.png!small?1677509041132)

### 案例二：某平台数据加密+签名

某平台登记完基础信息后点击提交信息查看数据包可以看到数据均被加密

![1677509783_63fcc497d9c38a01abaaa.png!small?1677509784838](https://image.3001.net/images/20230227/1677509783_63fcc497d9c38a01abaaa.png!small?1677509784838)

同时该功能点存在反调试相关代码

![1677509803_63fcc4ab5cfebd701d33f.png!small?1677509804203](https://image.3001.net/images/20230227/1677509803_63fcc4ab5cfebd701d33f.png!small?1677509804203)

当右键点击检查时网页自动进入调试状态

![1677509822_63fcc4bed4ae9b8ddaace.png!small?1677509823395](https://image.3001.net/images/20230227/1677509822_63fcc4bed4ae9b8ddaace.png!small?1677509823395)

在debugger处下断点选择修改断点

![1677509838_63fcc4ce3ed898e3ebdd9.png!small?1677509839119](https://image.3001.net/images/20230227/1677509838_63fcc4ce3ed898e3ebdd9.png!small?1677509839119)

设置为false即可

![1677509853_63fcc4dd819d27da890ed.png!small?1677509854028](https://image.3001.net/images/20230227/1677509853_63fcc4dd819d27da890ed.png!small?1677509854028)

请求包和返回包中均存在三个参数，x、x1、sign

查看js代码寻找加密逻辑其中x1疑似aes加密，直接搜索关键词定位到关键代码代码逻辑大致如下（代码经过简化）

![1677509868_63fcc4ec056d16a38d8c5.png!small?1677509868930](https://image.3001.net/images/20230227/1677509868_63fcc4ec056d16a38d8c5.png!small?1677509868930)

通过查看代码知道x为AES加密后的json数据，x1是经过RSA加密后的AES密钥，sign则是某种签名，且AES加密的密钥为动态密钥。继续查看RSA加密方法，key\_1就是RSA加密的私钥

![1677509880_63fcc4f8d4e7863a72e4a.png!small?1677509881631](https://image.3001.net/images/20230227/1677509880_63fcc4f8d4e7863a72e4a.png!small?1677509881631)

既然知道了RSA私钥，且数据包中存在x1参数，那些直接使用RSA私钥解密X1参数获取AES加密的密钥

![1677509900_63fcc50c148f11bcd5227.png!small?1677509900883](https://image.3001.net/images/20230227/1677509900_63fcc50c148f11bcd5227.png!small?1677509900883)

然后再用获取的AES密钥解密X内容获取真实请求数据

![1677509930_63fcc52ab8c065b9a317b.png!small?1677509931580](https://image.3001.net/images/20230227/1677509930_63fcc52ab8c065b9a317b.png!small?1677509931580)

而签名可以直接通过调用js的sign()去计算

![1677509946_63fcc53a12eb3d69c8c73.png!small?1677509947012](https://image.3001.net/images/20230227/1677509946_63fcc53a12eb3d69c8c73.png!small?1677509947012)

# web安全

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