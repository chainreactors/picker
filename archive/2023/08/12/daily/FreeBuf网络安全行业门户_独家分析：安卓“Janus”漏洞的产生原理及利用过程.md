---
title: 独家分析：安卓“Janus”漏洞的产生原理及利用过程
url: https://www.freebuf.com/articles/endpoint/156862.html
source: FreeBuf网络安全行业门户
date: 2023-08-12
fetch_date: 2025-10-04T12:01:45.078173
---

# 独家分析：安卓“Janus”漏洞的产生原理及利用过程

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

独家分析：安卓“Janus”漏洞的产生原理及利用过程

* ![]()
* 关注

* [终端安全](https://www.freebuf.com/articles/endpoint)

独家分析：安卓“Janus”漏洞的产生原理及利用过程

2023-08-11 16:32:30

**\*本文中涉及到的相关漏洞已报送厂商并得到修复，本文仅限技术研究与讨论，严禁用于非法用途，否则产生的一切后果自行承担。**

**近日，Google在12月发布的安卓系统安全公告中披露了一个名为“Janus”安卓漏洞（漏洞编号：CVE-2017-13156）。该漏洞可以让攻击者绕过安卓系统的signature scheme V1签名机制，进而直接对App进行篡改。而且由于安卓系统的其他安全机制也是建立在签名和校验基础之上，该漏洞相当于绕过了安卓系统的整个安全机制。**

一旦攻击者将植入恶意代码的仿冒的App投放到安卓商店等第三方应用市场，就可替代原有的App做下载、更新。网友安装这些仿冒App后，不仅会泄露个人账号、密码、照片、文件等隐私信息，手机更可能被植入木马病毒，进而或导致手机被ROOT，甚至被远程操控。详情可以参考[漏洞介绍](https://mp.weixin.qq.com/s?__biz=MzUzNDExNTc4Nw==&mid=2247484173&idx=1&sn=726b9021910e1ce8ff6a12eeef0ee2db&chksm=fa98e7a9cdef6ebfa5190e47a3b0f0c18059ef700359d0a05f0e88da025ddfbd1023cd6cc3a2&scene=21#wechat_redirect)及[预警文章](http://www.freebuf.com/vuls/156821.html)。

![timg.jpg](https://image.3001.net/images/20171211/15129757868468.jpg!small)

在第一时间监测到“janus”漏洞的情况后，顶象技术及时更新了“安全SDK”的防御策略，并率先发布了针对该漏洞的防护方案，以帮助广大用户防范基于该漏洞的攻击威胁。

分析显示，安卓5.0到8.0系统以及基于signature scheme V1签名机制的App均受“Janus”漏洞影响；基于signature scheme V2签名的App则不受影响。

### 安卓用户：

> 1、尽快升级到最新版安卓系统；
>
> 2、短期内，尽量到官方网站更新、下载App。

### 安卓开发者：

> 1、尽快将App APK(安装包）升级到最新的Signature scheme V2签名机制；
>
> 2、及时校验App APK文件的开始字节，以确保App是未被篡改；
>
> 3、顶象技术的“安全SDK”以更新防御机制，可以有效防护该漏洞。

## “Janus”漏洞爆发原因是什么？

为了提升安卓系统的安全性，Google发布了新的签名认证体系signature scheme V2。由于，signature scheme V2需要对App进行重新发布，而大量的已经存在的App APK无法使用V2校验机制，所以为了保证向前兼容性，V1的校验方式的还被保留，这就导致了“Janus”漏洞的出现。

Google为什么发布signaturescheme V2呢？那就盘点一下，近年来安卓系统曾爆出的一系列安全问题吧。

## 这些年，安卓系统爆出的签名漏洞

### “MasterKey”漏洞

“Janus”是一个签名与校验漏洞，其实，这不是安卓第一次爆出此类漏洞。在2013年 Black Hat上，Bluebox的安全团队公布了一个“MasterKey”漏洞。该漏洞影响包括当时最新的安卓6.0系统及以下所有系统。那么，这些漏洞是怎么形成的呢？

“MasterKey”漏洞原理是基于APK（ZIP文件格式）里面的多个ZipEntry实现的，具体如下：

> 1. 向原始的App APK的前部添加一个攻击的classes.dex文件（A)；
>
> 2. 安卓系统在校验时计算了A文件的hash值，并以”classes.dex”字符串做为key保存；
>
> 3. 然后安卓计算原始的classes.dex文件（B），并再次以”classes.dex”字符串做为key保存，这次保存会覆盖掉A文件的hash值，导致Android系统认为APK没有被修改，完成安装；
>
> 4. APK程序运行时，系统优先以先找到的A文件执行，忽略了B，导致漏洞的产生。

修复方式：

禁止安装有多个同名ZipEntry的APK文件。

![1.png](https://image.3001.net/images/20171211/15129746307112.png!small)

### “9695860”漏洞

MasterKey漏洞爆出后没多久，国内的“安卓安全小分队”再爆出一个类似的漏洞。这个漏洞非常精巧：利用了Zip local file header在计算时候的一个整形溢出漏洞。

具体原因：

> 1. 向原有的APK中的classes.dex文件B替换为攻击文件A，并添加一个大小为0xFFFD的extrafield；
>
> 2. 将原始dex文件B去除头3个字节写入extrafield；
>
> 3. Android系统在校验签名时使用的是Java代码的short，将0xFFFD以16位带符号整形的方式解析得到-3, 并解析出原始的文件B，Android认为程序APK无修改，正常安装；
>
> 4. 系统在执行时使用C代码的uint16，将0xFFFD以16位无符号整形方式，得到攻击文件B。

这个漏洞的精巧之处在于，DEX文件以‘dex’字符串开头，而classes.dex以这个字符串结尾，通过-3的值将这两个内容在文件中重叠起来，因此这也限制了“9695860”漏洞只能对classes.dex进行攻击。

![2.png](https://image.3001.net/images/20171211/15129746393762.png!small)

### **“9950697”漏洞**

在“9695860”漏洞爆出不久后，APK文件中被发现存在类似的整形溢出漏洞，这个比“9695860”漏洞更容易利用且可以攻击APK中的任意文件。

原因是安卓默认认为Zip中localfile header和central directory entry中的文件名长度和和extra的长度是一致的。安装过程中java代码在处理时出现溢出，读取到了正常的文件B，通过校验，APK正常安装。运行过程中，C代码处理时没有溢出，读取到了攻击的文件A。

![3.png](https://image.3001.net/images/20171211/15129746494130.png!small)

Google发布了signature scheme V2签名机制

以上的一系列漏洞全部出在基于jarsigner机制建立起来的签名和校验机制signature scheme V1出现。Google也意识到了这套机制的缺陷，所以，发布了重新设计的Siginature scheme V2签名机制。

Siginature scheme V2 APK文件整个内容进行签名，目标是任何对APK的修改都会导致检验的失败。

目前signature scheme V2已经在安卓7.0系统及以上的版本中支持。

## “Janus”漏洞的攻击原理、利用过程

### 攻击原理

1、安卓在4.4中引入了新的执行虚拟机ART，这个虚拟机经过重新的设计，实现了大量的优化，提高了应用的运行效率。与“Janus”有关的一个技术点是，ART允许运行一个raw dex，也就是一个纯粹的dex文件，不需要在外面包装一层zip。而ART的前任DALVIK虚拟机就要求dex必须包装在一个zip内部且名字是classes.dex才能运行。当然ART也支持运行包装在ZIP内部的dex文件，要区别文件是ZIP还是dex，就通过文件头的magic字段进行判断：ZIP文件的开头是‘PK’, 而dex文件的开头是’dex’.

2、ZIP文件的读取方式是通过在文件末尾定位central directory, 然后通过里面的索引定位到各个zip entry，每个entry解压之后都对应一个文件。

![4.png](https://image.3001.net/images/20171211/15129746601615.png!small)

### **影响的范围**

> 1. 安卓5.0-8.0的各个版本系统；
>
> 2. 使用安卓Signaturescheme V1签名的App APK文件。

### **利用过程**

1、攻击者可以向APK文件的开始位置放置一个攻击的DEX文件A；

2. 安卓系统在安装时用ZIP的读取机制从末尾开始进行文件的读取，读取到了原始的APK内容，并且以V1的方式进行校验，认为这个文件是正常的，没有篡改，APK安装成功；

3. 在运行时，Android的ART虚拟机从文件头开始读取，发现是一个DEX文件，直接执行，攻击文件A被最终执行。

### 带来的威胁

可以在没有apk所有者的证书的情况下对apk进行修改，并且绕过校验机制安装在用户的手机上，造成的可能后果如下：

> 1. 对存储在原手机上的数据进行读取，例如金融类APP的银行密码、支付密码、token; 通信类APP的聊天记录、图片、通信录
>
> 2. 对用户的输入做各种监听、拦截、欺诈，引导用户输入密码，转账。
>
> 3. 利用这个漏洞可以更新Android的系统APP，从获得更高的系统权限，甚至root/越狱，为其他攻击做准备

## 顶象技术的防护及修复建议

顶象技术一直关注移动端、WEB端上的各类风险以及各平台的业务威胁。及时分析监测到漏洞和威胁，并做好针对性的防护措施，由此积累了大量与黑灰产对抗的实战经验。顶象技术将这些实战经验以“安全SDK”的产品方式共享给用户，从而帮助用户建立高效的防御体系，有效防御各类新型的、复杂的恶意攻击和威胁。

在第一时间监测到“janus”漏洞的情况后，顶象技术及时更新了“安全SDK”的防御策略，并率先发布了针对该漏洞的安全防护方案，以帮助广大用户防范基于该漏洞的攻击威胁。

### **安卓用户：**

> 1、尽快升级到最新版安卓系统；
>
> 2、尽量到官方网站更新、下载App，短期内不用使用第三方安卓应用市场更新或下载App。

### **安卓开发者：**

> 1、将App APK升级到最新的Signature scheme V2签名机制；
>
> 2、开发者及时校验App APK文件的开始字节，以确保App未被篡改;
>
> 3、使用顶象技术提供的安全SDK，以防范该漏洞的攻击。

顶象技术是互联网业务安全的引导者，致力于打造零风险的数字世界，成立于2017年4月，红杉资本中国基金成员企业。顶象技术拥有领先的风控技术和智能终端安全技术，其首创的“共享安全”理念已成为新一代安全产品的标准架构。通过全景式业务安全风控体系、无感验证、虚机源码保护、安全SDK等方案和产品，赋予电商、金融、IoT、航空、游戏、社交等企业提供BAT级的业务安全能力，让平台和用户免受薅羊毛、交易欺诈、账号盗用、内容被恶意抓取、系统和App遭破解等风险威胁。

**\*本文作者：Bob，转载请注明来自FreeBuf.COM**

# 漏洞 # 安卓 # Janus

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