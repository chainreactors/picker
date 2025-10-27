---
title: 挖了这么久才发现，漏洞挖掘可以更简单
url: https://www.freebuf.com/fevents/408519.html
source: FreeBuf网络安全行业门户
date: 2024-08-14
fetch_date: 2025-10-06T18:03:13.828314
---

# 挖了这么久才发现，漏洞挖掘可以更简单

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

挖了这么久才发现，漏洞挖掘可以更简单

* ![]()
* 关注

* [活动](https://www.freebuf.com/fevents)

挖了这么久才发现，漏洞挖掘可以更简单

2024-08-13 16:06:59

大家好，我是地图大师returnwrong。最近，我在与多位新手白帽子接触后发现，环境配置常常成为他们面临的一大难题。无论是灯塔、oneforall、水泽，还是subfinder等信息收集工具，许多白帽子在安装和配置这些工具时都会遇到各种困扰。针对这一问题，我不禁思考：如果能找到一种方法，从根本上解决环境配置的难题，那该多好。

基于这个想法，我们团队开发了一系列工具，旨在简化挖洞的基础流程，提高挖掘效率。

首先，我们推出了地图os-u和地图os-w两款集成环境，大大简化了工具配置的过程。传统的信息收集和渗透测试需要逐一安装和配置多个工具，费时且繁琐。地图os-u将各种信息收集工具整合在一个环境中，而地图os-w则提供了一个完整的渗透测试虚拟机，省去了繁琐的配置步骤，让你可以专注于实际的漏洞挖掘。

接下来，我们推出了几款原创的BurpSuite插件，包括captchados、Smart URL Parameter Modifier、Url-Path-Extractor和url路径批量处理工具。这些插件针对不同的漏洞挖掘挑战而设计。captchados专门解决破解图片验证码的问题；Smart URL Parameter Modifier帮助发现SSRF、XSS等漏洞；Url-Path-Extractor和url路径批量处理工具则使路径数据的处理和整理更加得心应手，从而识别出更多潜在的攻击面。

这些工具不仅提升了漏洞挖掘的效率，还简化了配置和处理步骤，帮助你更专注于挖掘真正的漏洞。每一款工具都是我们团队的精心之作，旨在使你的挖掘工作更加高效。

## 工具的简单介绍

### **两款集成环境**

1.  地图os-u

一站式信息收集工具包，集成改装过的灯塔、subfinder、projectdiscover全部工具、水泽、oneforall等，无需繁琐配置，直接使用。

再也不用为了信息收集搭建繁杂的环境，不愁没有资产挖。

2.  地图os-w

一站式挖洞环境，渗透测试专用Windows虚拟机，集成了BurpSuite改装、多种常用渗透字典、多种渗透测试环境，简化配置。

### **几款原创Burpsuite插件**

3.  captchados

彻底解决图片验证码dos漏洞挖掘难题，半自动化拼接参数。

指哪打哪，让天下没有难挖的验证码dos漏洞。

4.  Smart URL Parameter Modifier

被动拼接payload，让url跳转ssrf、xss等漏洞无处遁形。

没有固定的漏洞类型，你挖洞经验越丰富，能用他自定义挖掘的漏洞就更多。

5.  Url-Path-Extractor

原创BurpSuite插件，多种场景下路径收集工具，将流量日志中多个路径去重递归拆分。

不同的路径代表不同的攻击面，作为白帽的你，我想已经理解了。没错，能扩展更多挖洞攻击面。

6.  url路径批量处理工具

结合Url-Path-Extractor使用，去除无用文件，还原真实接口。

做到一键路径处理，快速处理路径数据，提升工作效率。

7.  xxx工具——具体功能先保密，将于直播间亮相，师傅们敬请期待！

除了这些好用的原创工具外，我们还将分享自制的Hae挖洞规则、Burp杂包过滤脚本、灯塔本地拉取版本等等，以及其他好用的工具及挖洞经验总结。

此外，我们还有地图大师专属群组——根据组员需求定制化开发插件，进行长期更新。每一个工具都是多次迭代的经验总结。

为了让师傅们更了解我们的工具，我将在8月14号（下周三）晚上20点，在知识大陆上进行一场直播，详细介绍这些工具并逐一演示使用操作。

## 更多内容——明天（周三）晚上8点，来直播间，包讲明白的

![1723535688_66bb11483926168f47191.png!small?1723535689114](https://image.3001.net/images/20240813/1723535688_66bb11483926168f47191.png!small?1723535689114)

### 直播预约可扫码↓↓↓

![1723535933_66bb123d4e187f212177c.png!small?1723535933573](https://image.3001.net/images/20240813/1723535933_66bb123d4e187f212177c.png!small?1723535933573)

## 直播嘉宾：地图大师returnwrong

* Day1安全团队核心成员
* 2023年智联招聘SRC第5
* 2023年银联SRC第10
* 2023年知识星球SRC第4
* 2022年猎聘SRC第8
* 2022年BOSS直聘SRC第7
* 2024年HackingClub议题嘉宾
* 2024年平安SRC漏洞挖掘经验分享嘉宾
* 进入联合国、欧盟等网络安全名人堂，收到Nasa漏洞报送感谢信等

## 6款工具已发布于帮会中

目前仅需：

**180元/永久**

PS：这个月月底帮会将**涨价**

点击链接即可永久买断：<https://wiki.freebuf.com/societyDetail?society_id=194>

或者扫描下方二维码↓↓↓

![1723536087_66bb12d713bde3db2c78e.png!small?1723536087173](https://image.3001.net/images/20240813/1723536087_66bb12d713bde3db2c78e.png!small?1723536087173)

## 免费的挖洞实战插件包等你拿

进交流群，免费领取多个好用的挖洞实战插件

扫下方二维码，vivi拉你进群

PS：加好友请备注**【大师】**

![1723536129_66bb1301a4b4544ac4470.jpg!small?1723536129989](https://image.3001.net/images/20240813/1723536129_66bb1301a4b4544ac4470.jpg!small?1723536129989)

# 工具 # 活动 # 挖洞

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

工具的简单介绍

* 两款集成环境
* 几款原创Burpsuite插件

更多内容——明天（周三）晚上8点，来直播间，包讲明白的

* 直播预约可扫码↓↓↓

直播嘉宾：地图大师returnwrong

6款工具已发布于帮会中

免费的挖洞实战插件包等你拿

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