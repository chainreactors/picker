---
title: 斯巴鲁漏洞让黑客可以远程控制数百万辆汽车
url: https://www.freebuf.com/news/420728.html
source: FreeBuf网络安全行业门户
date: 2025-01-25
fetch_date: 2025-10-06T20:10:13.477263
---

# 斯巴鲁漏洞让黑客可以远程控制数百万辆汽车

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

斯巴鲁漏洞让黑客可以远程控制数百万辆汽车

* ![]()
* 关注

* [资讯](https://www.freebuf.com/news)

斯巴鲁漏洞让黑客可以远程控制数百万辆汽车

2025-01-24 11:06:57

所属地 上海

据Cyber Security News消息，斯巴鲁STARLINK互联汽车服务中心在2024年底被发现一个关键漏洞，美国、加拿大和日本的数百万辆汽车和车主账户可能受到网络攻击。

![](https://image.3001.net/images/20250124/1737688120_67930438b5952610c41e6.png!small)

该安全漏洞允许攻击者使用最少的信息（如姓氏和邮政编码、电子邮件地址、电话号码或车牌）远程访问敏感的车辆和个人数据，包括：

* 远程启动、停止、锁定和解锁车辆。
* 访问实时车辆位置并检索过去一年的详细位置历史记录。
* 提取客户的个人身份信息 （PII），包括地址、账单详细信息（部分信用卡信息）、紧急联系人和车辆 PIN。
* 查询其他用户数据，例如支持呼叫历史记录、里程表读数、销售记录等。

研究人员通过仅使用车牌号成功接管车辆证明了这种漏洞的危害性。他们还从一辆测试车辆中检索了一年多的精确位置数据，这些数据包括每次发动机启动时更新的数千个 GPS 坐标。

## **漏洞发现过程**

研究人员最初检查了斯巴鲁的 MySubaru 移动应用程序，发现其十分安全，便将重点转移到面向员工的系统上，他们通过子域扫描发现了 STARLINK 服务的管理门户。 起初，该网站似乎没有太多内容，只有一个登录面板，并且没有任何可用的凭据。

然而，在研究网站的源代码时，发现 /assets/\_js/ 文件夹中有一些 JavaScript 文件。 为了深入挖掘，研究人员对该目录进行了暴力破解。在一个名为 login.js 的文件中，发现有段代码可以在无需任何令牌的条件下重置员工账户。因此，攻击者可以使用任何有效的员工电子邮件进行账户接管。

为了验证这一点，研究人员发送了一个 POST 请求，以检查该功能是否已暴露并处于运行状态。 该门户网站包含一个密码重置端点，允许在不需要确认令牌的情况下接管账户。 利用 LinkedIn 和其他来源的公开信息，他们确定了有效的员工电子邮件地址，从而利用了这一漏洞。

进入管理系统后，研究人员通过禁用客户端安全覆盖，绕过了双因素身份验证（2FA），进而可以不受限制地访问 STARLINK 的后台功能，包括查看和导出任何已连接斯巴鲁车辆的详细位置历史记录、使用邮政编码或车辆识别码等基本标识符搜索车主帐户、在不通知车主的情况下为车辆添加未经授权的用户。

为了进一步验证其发现，研究人员在朋友的汽车上测试了他们获得的访问权限，最终成功地远程解锁了车辆且没有触发任何警报或通知。

研究人员于 2024 年 11 月 20 日向斯巴鲁报告了该漏洞，并在次日就得到了修复。据研究人员称，没有证据表明该漏洞在修补之前被恶意利用。

这一事件凸显了人们对联网汽车网络安全的广泛担忧，这些车辆收集了大量数据，并依赖于难以全面保障安全的互联系统。 研究人员指出，作为日常工作的一部分，员工通常可以广泛访问敏感信息，这使得此类系统本身就很脆弱。

**参考来源：**

> [Subaru Car Vulnerability Lets Hackers Control Millions of Cars Remotely Using Starlink](https://cybersecuritynews.com/subaru-car-vulnerability-lets-hackers-control-the-millions-of-cars-remotely/)

# 终端安全

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

漏洞发现过程

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