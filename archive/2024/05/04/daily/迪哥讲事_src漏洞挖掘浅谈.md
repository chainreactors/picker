---
title: src漏洞挖掘浅谈
url: https://mp.weixin.qq.com/s?__biz=MzIzMTIzNTM0MA==&mid=2247494493&idx=1&sn=813f79d75e12afa42d4a4437f808868b&chksm=e8a5e13edfd268285404dfccc3c441edd2f0beccb9de83dad8fd6954f75861ce6ef8f3b14c58&scene=58&subscene=0#rd
source: 迪哥讲事
date: 2024-05-04
fetch_date: 2025-10-06T17:17:11.477961
---

# src漏洞挖掘浅谈

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/YmmVSe19Qj7MRmSsffUXwydibZibDh8JuNsW3ML72ZHZHmgrQibll5iaJK2GdpRv1o7wjGdwmh8aql8yVMRdDhSTfg/0?wx_fmt=jpeg)

# src漏洞挖掘浅谈

迪哥讲事

以下文章来源于雷石安全实验室
，作者雷石安全实验室

![](http://wx.qlogo.cn/mmhead/Q3auHgzwzM6OicTicQtrdBtWeYMQ6vta7YVCcKBsB2xR615pO1a1EnYg/0)

**雷石安全实验室**
.

雷石安全实验室以团队公众号为平台向安全工作者不定期分享渗透、APT、企业安全建设等新鲜干货，团队公众号致力于成为一个实用干货分享型公众号。

# **前言**

渗透测试的灵魂是信息收集，本体是在漏洞利用。收集到的资产和信息越多，你的突破点就越多，因为你找到了别人没有找到的，你测了他没有测试的，你已经领先在了起跑线上，而src得用大量的时间去做信息收集，src比的不只是技术，更比的的是耐心，细心。

# **信息收集篇**

第一步：厂商域名:厂商的域名可以通过爱企查，企查查这类的工具去搜索主域名他曾用过的一些域名

免费会员:

[*https://mp.weixin.qq.com/s/h1qdBXeS4KoFzLyRVAf\_LQ*](https://mp.weixin.qq.com/s?__biz=Mzg5NDQ2OTU3Nw==&mid=2247533762&idx=1&sn=ff05b30bab9ec5842338936b6a748a82&scene=21#wechat_redirect)

![](https://mmbiz.qpic.cn/mmbiz_png/RXib24CCXQ0ibWDwBjhvBWsFYRibuicNN3MwhqsxWRmuswZJlNQY1FwibP7icRY1v4ycr3k9a684Y85ica8p08PEcwzhw/640?wx_fmt=png)

icp备案也可以，但是注意要输入公司名全称

![](https://mmbiz.qpic.cn/mmbiz_png/RXib24CCXQ0ibWDwBjhvBWsFYRibuicNN3MwGiba2Kuz1qI76MDg7cjic16WkUbRibUYsdibM6fQgOPuYfNlzmOIekJ7wA/640?wx_fmt=png)

另外推荐奇安信的鹰图平台，可以用关键词查询备案网站

![](https://mmbiz.qpic.cn/mmbiz_png/RXib24CCXQ0ibWDwBjhvBWsFYRibuicNN3MwgZoHbhjxlEdcXDmHmYdAxXzJJmm7ngkczrM3p0BcDtNV5qGy79QiaibA/640?wx_fmt=png)

第二步：子域名：将收集到的域名进行子域名挖掘，针对子域名以下几点：

通过SSL证书查询:crt.sh 可以查到域名证书相关子域名

第三方接口网站：censys.io 、 fofa、dnsdb.io等等

工具挖掘：oneforall、 layer等

在线子域名挖掘（个人认为比较好用）:phpinfo.me

![](https://mmbiz.qpic.cn/mmbiz_png/RXib24CCXQ0ibWDwBjhvBWsFYRibuicNN3MwykTEgeemf5Ep5AAJekvtjk12NRfPdodfPdo8IxUZYbqNyspn6foEsA/640?wx_fmt=png)

通过github进行收集：这个不好细说，懂得都懂。

![](https://mmbiz.qpic.cn/mmbiz_png/RXib24CCXQ0ibWDwBjhvBWsFYRibuicNN3MwDOicQ0f8GVt8xQFlFofQzPbyl9jaEiaymRdiaV5WFicGH3OurXF79ibBBVg/640?wx_fmt=png)

第三步：查询IP段，在查询玩子域名后我们已经获得了大量的IP 我们可以通过IP所属网络进行反差查找厂商所拥有的IP段：

https://ipwhois.cnnic.cn/index.jsp

这个不仅可以通过IP查询所属单位和网络名称还可以通过网络名称再反查网络段

![](https://mmbiz.qpic.cn/mmbiz_png/RXib24CCXQ0ibWDwBjhvBWsFYRibuicNN3Mw8fDsO2t3ibicKNYlnic9zqFRdWTExOBAticicU2HibxgiaVX8CmicibibwM8JvoQ/640?wx_fmt=png)

第四步：获取IP后，进行批量的端口扫描，这里各位就各凭本事，谁还不会个端口扫描了？

信息收集就说到这里，信息收集的主要目的就是扩大可利用面，10000万个资产你可能碰到弱口令，但1个资产你肯定没有弱口令

# **挖掘前篇**

前边已经讲了信息收集，在测试前为了能高效的挖掘src，就需要有数据进行测试，这个数据就是我们常说的字典，字典怎么来，整理，收集，经验，积累。先说以下字典的类型：

目录字典：目录探测、后台探测、功能探测

漏洞字典：除了常规的目录字典，收集漏洞字典也是很有必要的，如spring-boot框架的字典、git泄漏、压缩文件泄漏、系统配置等

参数字典：这类的字典很多，需要自己收集，比如密码，用户名，常见参数，等字典

漏洞fuzz：xss payload、上传payload等

![](https://mmbiz.qpic.cn/mmbiz_png/RXib24CCXQ0ibWDwBjhvBWsFYRibuicNN3MwlFC49WesyoYTwBJ1Q4AH9yAFBjA9cPzDQKkXORNib2gb2qHzHNjeMWQ/640?wx_fmt=png)

这些都需要进行灵活的使用，能极大的我们的挖掘漏洞过程中的效率。

# **挖掘篇**

首先讲一下漏洞挖掘的方向

一般来讲个大src的侧重不同，如果经常跟一家src，那么有新功能上线就能快人一步发现漏洞，其次除了web业务应用，app、小程序等服务也是挖掘的重点。当然在挖掘的过程中会遇到抓不到数据包、app闪退、全流量加密、waf拦截等各种问题，这些网上都有相应的解决方法，只能在遇到的过程中逐步解决，也可以参考雷石之前发的文章。

最后着重讲一下逻辑漏洞，其他漏洞也有多，但是大厂除了逻辑漏洞外，其他漏洞相对少些，上传、csrf、xss、sql注入等也是有的，重点还是从功能上看，尽可能对相关业务功能很熟悉，可以猜测参数意义，看到某些参数就能去知道该测哪些漏洞，漏洞挖掘自然不在话下。

这里我主要讲述自己常用来测试逻辑楼的功能点，供大家参考：

逻辑漏洞容易出现的地方及相应问题：

支付处（订单生成、订单处理）

注册处（恶意注册、绑定）

登录处（第三方认证、登陆绕过、凭证伪造、凭证窃取）

验证码（验证码无效、不刷新）

业务处理（权限管理、业务逻辑绕过）

密码找回处（任意密码重置、认证绕过）

先说登录处的逻辑缺陷：

1，通过用户直接爆破密码

2，做了用户登录锁定，通过密码爆破用户

3，存在返回提示用户名错误，爆破用户名

4，Cookie的伪造，修改字段中的某种来进行登录

5，固定的session，比如修改session中的会话ID造成越权行为

验证码：

现在的验证码各种各样，最常见的就是手机验证码登录，这也是逻辑漏洞的所在而验证码的测试主要分为以下种类：

时间，和次数的突破：重复提交，待验证码的数据包看返回结果

绕过验证：直接删除cookie或者验证码绕过

篡改：修改相关数值，造成短信轰炸

![](https://mmbiz.qpic.cn/mmbiz_png/RXib24CCXQ0ibWDwBjhvBWsFYRibuicNN3Mw7icmic6YZDe2GrIDmc5Ldn3MNyuJPU1oticgaaLtmxUSyrgDUqIqmtTGQ/640?wx_fmt=png)

密码找回：

在密码找回时通过修改用户名，导致被修改的用户名密码被修改

查看请z求连接中是否携带验证

手机找回密码时，返回包中携带验证码

密码或密保问题出现在源码中

业务逻辑漏洞:

业务逻辑出现问题最容易出现的问题就是越权，

越权可分为两种，一个是水平越权和垂直越权越权漏洞的常见电

修改、重置、找回其他账户密码

查看、修改其他账户未公开的信息，例如个人资料、文件、数据、程序等

与账户关联的权限操作

水平越权：

基于用户身份：比如说可控参数修改1变成2 从张三的账号变成李四

基于文件名：比如下载文件需要收费，通过接口功能访问文件名直接进行下载，读取等操作

基于对象id:通过修改id值去访问其他用户信息

垂直越权：

未认证直接访问功能点

不具备某功能权限绕过认证 比如登录后台先访问后台，再跳转到登录界面，通过丢弃验证包直接进入后台，访问后台功能点和数据

支付漏洞：

支付漏洞就一句话：数据篡改（当然好多漏洞都可以这么说，哈哈）

比如将参数改成1毛通过1毛购买苹果收集等操作。金额，数量都是可以篡改的地方

# **小结**

挖掘src漏洞最主要还是挖掘逻辑漏洞，无非就是耐心，细节，多留意数据包的可疑数据，数据包所实现的功能。

如果你是一个长期主义者，欢迎加入我的知识星球，我们一起往前走，每日都会更新，精细化运营，微信识别二维码付费即可加入，如不满意，72 小时内可在 App 内无条件自助退款
前面有同学问我有没优惠券，这里发放100张100元的优惠券,用完今年不再发放

![](https://mmbiz.qpic.cn/mmbiz_png/YmmVSe19Qj7N5nMaJbtnMPVw96ZcVbWfp6SGDicUaGZyrWOM67xP8Ot3ftyqOybMqbj1005WvMNbDJO0hOWkCaQ/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/YmmVSe19Qj5jYW8icFkojHqg2WTWTjAnvcuF7qGrj3JLz1VgSFDDMOx0DbKjsia5ibMpeISsibYJ0ib1d2glMk2hySA/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1)

## 往期回顾

[dom-xss精选文章](http://mp.weixin.qq.com/s?__biz=MzIzMTIzNTM0MA==&mid=2247488819&idx=1&sn=5141f88f3e70b9c97e63a4b68689bf6e&chksm=e8a61f50dfd1964692f93412f122087ac160b743b4532ee0c1e42a83039de62825ebbd066a1e&scene=21#wechat_redirect)

[年度精选文章](http://mp.weixin.qq.com/s?__biz=MzIzMTIzNTM0MA==&mid=2247487187&idx=1&sn=622438ee6492e4c639ebd8500384ab2f&chksm=e8a604b0dfd18da6c459b4705abd520cc2259a607dd9306915d845c1965224cc117207fc6236&scene=21#wechat_redirect)

[Nuclei权威指南-如何躺赚](http://mp.weixin.qq.com/s?__biz=MzIzMTIzNTM0MA==&mid=2247487122&idx=1&sn=32459310408d126aa43240673b8b0846&chksm=e8a604f1dfd18de737769dd512ad4063a3da328117b8a98c4ca9bc5b48af4dcfa397c667f4e3&scene=21#wechat_redirect)

[漏洞赏金猎人系列-如何测试设置功能IV](http://mp.weixin.qq.com/s?__biz=MzIzMTIzNTM0MA==&mid=2247486973&idx=1&sn=6ec419db11ff93d30aa2fbc04d8dbab6&chksm=e8a6079edfd18e88f6236e237837ee0d1101489d52f2abb28532162e2937ec4612f1be52a88f&scene=21#wechat_redirect)

[漏洞赏金猎人系列-如何测试注册功能以及相关Tips](http://mp.weixin.qq.com/s?__biz=MzIzMTIzNTM0MA==&mid=2247486764&idx=1&sn=9f78d4c937675d76fb94de20effdeb78&chksm=e8a6074fdfd18e59126990bc3fcae300cdac492b374ad3962926092aa0074c3ee0945a31aa8a&scene=21#wechat_redirect)

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/YmmVSe19Qj4k2mXPm8xlXujVgicTGvZbcictoGLuPERQn9lRPAKkKUB5ut9XMicric8PxLRmSOq0tT5LuGuD1WemBQ/0?wx_fmt=png)

迪哥讲事

向上滑动看下一个

知道了

![]()
微信扫一扫
使用小程序

取消
允许

取消
允许

取消
允许

×
分析

![跳转二维码]()

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/YmmVSe19Qj4k2mXPm8xlXujVgicTGvZbcictoGLuPERQn9lRPAKkKUB5ut9XMicric8PxLRmSOq0tT5LuGuD1WemBQ/0?wx_fmt=png)

微信扫一扫可打开此内容，
使用完整服务

：
，
，
，
，
，
，
，
，
，
，
，
，
。

视频
小程序
赞
，轻点两下取消赞
在看
，轻点两下取消在看
分享
留言
收藏
听过