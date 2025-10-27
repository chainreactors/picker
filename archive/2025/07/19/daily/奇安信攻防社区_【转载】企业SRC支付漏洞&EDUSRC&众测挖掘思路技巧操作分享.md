---
title: 【转载】企业SRC支付漏洞&EDUSRC&众测挖掘思路技巧操作分享
url: https://forum.butian.net/share/4463
source: 奇安信攻防社区
date: 2025-07-19
fetch_date: 2025-10-06T23:16:24.115248
---

# 【转载】企业SRC支付漏洞&EDUSRC&众测挖掘思路技巧操作分享

#

[问答](https://forum.butian.net/questions)

*发起*

* [提问](https://forum.butian.net/question/create)
* [文章](https://forum.butian.net/share/create)

[攻防](https://forum.butian.net/community)
[活动](https://forum.butian.net/movable)

Toggle navigation

* [首页 (current)](https://forum.butian.net)
* [问答](https://forum.butian.net/questions)
* [商城](https://forum.butian.net/shop)
* [实战攻防技术](https://forum.butian.net/community)
* [漏洞分析与复现](https://forum.butian.net/articles)
  NEW
* [活动](https://forum.butian.net/movable)
* [摸鱼办](https://forum.butian.net/questions/Play)

搜索

* [登录](https://forum.butian.net/login)
* [注册](https://user.skyeye.qianxin.com/user/register?next=http://forum.butian.net/btlogin)

### 【转载】企业SRC支付漏洞&EDUSRC&众测挖掘思路技巧操作分享

* [渗透测试](https://forum.butian.net/topic/47)

案例的描述蛮详细的，师傅们可以多看看，或者直接上网找下对应的资料，漏洞报告文档之类的看看，还是对于我们后期的一个学习还行有帮助的！

声明
--
本文章所分享内容仅用于网络安全技术讨论，切勿用于违法途径，所有渗透都需获取授权，违者后果自行承担，与本号及作者无关，请谨记守法.
作者：一个想当文人的黑客
原文链接：<https://xz.aliyun.com/news/18389>
0x1 前言
------
这篇文章也是给师傅们分享几个SRC漏洞挖掘中的技巧点，两个企业SRC漏洞案例，支付漏洞中，师傅们碰到都可以进行尝试验证下，要是挖到了，像众测中就是中、高危起步了。赏金的价格还不错，两个案例也写的很详细了，第一个使用两个手机号支付漏洞案例比较新奇一点，很多师傅应该都还没有了解。
然后后面还是老规矩，给师傅们分享一个以前挖过的EDUSRC的漏洞案例，目前也是已经修复了的漏洞案例了，UEditor1.4.3编辑器漏洞，我记得之前我挖过好几个这样的编辑器漏洞，特别是在后台的编辑功能点，文件上传漏洞导致的getshell漏洞场景。
后面还给师傅们分享了几个众测的漏洞案例，思路和操作总体来说还算是不错的，有时候漏洞挖掘的过程中看着感觉漏洞快出来了，但是有时候可能被开发隐藏了一些东西，漏洞搞不出来，其实这个时候，我们细节点，有时候SRC就是可以出漏洞的，漏洞挖掘过程中并没有那么多的牛逼漏洞，主要还是细节！
![](https://cdn.nlark.com/yuque/0/2025/png/55850010/1751442623360-275bacf2-e4fa-4147-9c23-436868ae93a2.png)
0x2 支付漏洞
--------
### 一、两手机支付（卡在订单支付界面导致的优惠券复用）
首先第一个分享的支付漏洞，需要我们准备两个手机，得支持可以同时登陆一个账号的应用，要不然无法完成我们下面的支付漏洞的一个操作，且这个漏洞跟我们使用优惠卷有关系。
然后我们这里直接在两个手机上分别登陆这个应用，然后点击里面的会员付费功能，我们先拿一个手机进入订单页面（首先声明下这个下单每个人都有一个新人优惠卷），正常使用一个优惠券去创建一个订单
![](https://cdn.nlark.com/yuque/0/2025/png/55850010/1751442623498-1352cdb5-be14-4458-9055-49ec9afa7df1.png)
然后这个手机一定要停留在这个支付页面（先不支付）
![](https://cdn.nlark.com/yuque/0/2025/png/55850010/1751442623559-2ab6121b-8ec3-43d3-9f64-f970567abcc9.png)
然后使用另一个手机，也登录这个 app(要求 app 可以同时登录)
这时候再回去取消订单，这时候可以看到优惠券已经重新返回给我们了
![](https://cdn.nlark.com/yuque/0/2025/png/55850010/1751442623618-dad31c88-9e0b-45af-a409-58618fb2c459.png)
点击取消订单后，优惠券成功返回回来了
![](https://cdn.nlark.com/yuque/0/2025/png/55850010/1751442623716-73afcb13-7693-406e-a418-52e16efd4cfc.png)
然后使用这张优惠券，在第二个手机上继续下单，然后两个手机同时支付，就可以造成两个订单都重复使用优惠券
![](https://cdn.nlark.com/yuque/0/2025/png/55850010/1751442623794-cc5e0899-e8f4-4e78-9b58-ab904bf3c1ed.png)
### 二、优惠卷并发重复使用漏洞
这里优先关注这样的优惠卷订单，很容易产生优惠卷并发领取+优惠卷并发重复使用漏洞
![](https://cdn.nlark.com/yuque/0/2025/png/55850010/1751442623874-7676d738-6012-43e3-8e21-a0da61dedf88.png)
在提交订单的时候，抓包进行并发操作
![](https://cdn.nlark.com/yuque/0/2025/png/55850010/1751442623936-6b18d75e-7434-434f-9f53-017f7e53a225.png)
然后使用并发插件，数量20个，并发的race.py脚本如下，需要的师傅自取即可
```php
def queueRequests(target, wordlists):
engine = RequestEngine(endpoint=target.endpoint,
concurrentConnections=20,
requestsPerConnection=100,
pipeline=False
)
for i in range(20):
engine.queue(target.req, target.baseInput, gate='race1')
engine.openGate('race1')
engine.complete(timeout=60)
def handleResponse(req, interesting):
table.add(req)
```
![](https://cdn.nlark.com/yuque/0/2025/png/55850010/1751442624015-b8fb088c-f059-4cd5-94d4-facc05f5ad75.png)
可以看到数据包的状态200和长度都是一样的，那就说明我们成功进行了并发操作
![](https://cdn.nlark.com/yuque/0/2025/png/55850010/1751442624090-e69e6920-23b8-4ae8-a5a8-1eef77957aa0.png)
后门进行支付页面订单查看，可以看到，直接可以进行并发操作成功，每个都订单优惠了100元
0x3 EDUSRC中UEditor编辑器高危
-----------------------
首先访问该学校的教师职工登陆系统，这里可以看到登陆界面，可以感觉系统有点老，可能存在Nday漏洞
![](https://cdn.nlark.com/yuque/0/2025/png/55850010/1751442624150-6d80c589-d443-41c7-8b4b-189278a0970c.png)
这里我通过信息收集，收集到了很多个职工号，然后使用默认密码123456进行尝试爆破，成功登陆了该系统后台
![](https://cdn.nlark.com/yuque/0/2025/png/55850010/1751442624220-3e13592b-3f41-42f5-bd6a-3d16c693b70d.png)
然后使用功能点中的文档管理功能，编辑器，发现是UEditor编辑器，且版本不高，猜测可能存在漏洞
![](https://cdn.nlark.com/yuque/0/2025/png/55850010/1751442624275-a981f3f5-b73f-4f4b-aee1-385b4ea55639.png)
然后使用Google浏览器搜索UEditor1.4.3漏洞，可以看到存在漏洞poc
![](https://cdn.nlark.com/yuque/0/2025/png/55850010/1751442624331-14d4cd84-6de7-40de-ad8a-5323abbcaeac.png)
然后这里直接使用网上文章的poc进行测试，在cookie中发现是net版本语言是aspx
![](https://cdn.nlark.com/yuque/0/2025/png/55850010/1751442624391-48ae5902-4cf1-46dd-8d75-d095a18f6037.png)
最后通过poc打了一个getshell上传路径，然后成功使用蚁剑连接了getshell
![](https://cdn.nlark.com/yuque/0/2025/png/55850010/1751442624473-df45039d-b203-49ba-a914-e44ddf126aca.png)
0x4 某EDU大学官网搜索框SQL注入
--------------------
这个漏洞是存在搜索栏这个地方
![](https://nc0.cdn.zkaq.cn/md/21977/20250620/e55f78c2-f981-424b-a24f-7ceeb6865672.png)
输入1'，网页报错同时爆出绝对路径，初步判定为POST型注入
然后直接使用burp抓包分析请求，并保存至txt文件中
![](https://nc0.cdn.zkaq.cn/md/21977/20250620/a81fabac-e72c-456a-91be-8f85c0aaae61.png)
打开sqlmap进行注入，此处可以通过注入获取库名，表名等
![](https://nc0.cdn.zkaq.cn/md/21977/20250620/678966c7-e6ec-465c-a16d-6ec1f1cda52e.png)
最终在数据库中拿到了管理员admin的账号密码，成功登陆后台。
![](https://nc0.cdn.zkaq.cn/md/21977/20250620/c52c59e2-968c-472f-8ada-cd5d8ab0ad63.png)
0x5 有意思的众测案例
------------
这个众测案例中漏洞目前已经都修复了，所以拿出来给师傅们分享下两个漏洞都是高危（众测给的高点），漏洞没有那么牛逼，其实就是我之前经常分享的挖微信小程序楼——sessionkey泄露和数据包分析的手法，但是又不是那种直接能看出来的，要是没有那么细节的师傅们可能就容易错过这个漏洞。
因为这个众测目标大多都是服务行业，酒店、旅游什么的多，像这样的资产，app和微信小程序功能和资产肯定偏多，功能多，漏洞相对来说就好测试点，这里直接从小程序入手。
![](https://nc0.cdn.zkaq.cn/md/21977/20250620/60037284-dec6-4e1e-95ed-c4b8a9b3c023.png)
可以看到这里小程序很常见的手机号一键登陆，很容易出那种sessionkey三要素泄露，伪造用户信息未授权登陆漏洞
![](https://nc0.cdn.zkaq.cn/md/21977/20250620/938f038f-0405-48c6-a5b9-b33135ee8bb2.png)
这个小程序也不例外，也存在这个泄露
![](https://nc0.cdn.zkaq.cn/md/21977/20250620/5f3da409-0f5d-4e57-a195-6c254042afc9.png)
然后解密得到如下，182开头的手机号
![](https://nc0.cdn.zkaq.cn/md/21977/20250620/29fe6768-309d-489d-a781-7010457bee98.png)
老规矩，这里直接改成我别的手机号，然后加密，再重新退出182的账户，点击上面的手机号一键登陆，直接抓包，然后把数据包进行替换（我166的手机号加密字段）
![](https://nc0.cdn.zkaq.cn/md/21977/20250620/caf47f3a-5f79-4d74-8901-f5045349cab1.png)
按道理直接放包就可以登陆成功，但是这里直接点击放包，登陆失败了，这里猜测之前可能有师傅搞众测已经交过漏洞，那边后端对这里做了校验，行不通了。
但是峰回路转，我直接在重现测试，然后我直接看返回包，发现返回包出现了下面两个参数，且都是明文显示（看到这两个参数心里很开心，因为很大概率存在漏洞）
```php
{"phoneNumber":"xxxxxxxxx",
"purePhoneNumber":"xxxxxxxxxx"}
```
![](https://cdn.nlark.com/yuque/0/2025/png/55850010/1751442624534-8ed935ae-08e6-4e0d-9498-3269841b390c.png)
后面我直接修改一键登陆页面的返回包中的这两个参数，修改成我16的手机号，直接可以登陆成功
![](https://cdn.nlark.com/yuque/0/2025/png/55850010/1751442624613-099d94c9-832b-4293-81ee-7939f7e7cf93.png)
![](https://nc0.cdn.zkaq.cn/md/21977/20250620/49330e35-c9b1-4f4d-90d3-455af06596cc.png)
然后还有一个比较有意思的案例下次再分享，刚才没有找到之前的报告了，不太好分享，等下次找到了报告再做分享，因为漏洞已经修复了，复现不了了。
0x6 总结
------
这篇文章就分享到这里就结束了，主要还是以企业SRC和EDUSRC两个方面去给师傅们分享漏洞案例，然后师傅们比如在挖掘EDUSRC的时候，很多师傅都觉得官网挖不到漏洞，特别是那种SQL注入top10类型的，其实不然，漏洞挖掘的过程中就是比谁更具细节，把别人没有测试到的功能点进行测试，那么人家就大概率能够挖到漏洞。跟很多大牛师傅们交流，我看他们赏金漏洞大部分都是那种细节漏洞，但是赏金的价格也不低。
案例的描述蛮详细的，师傅们可以多看看，或者直接上网找下对应的资料，漏洞报告文档之类的看看，还是对于我们后期的一个学习还行有帮助的！

* 发表于 2025-07-18 09:00:01
* 阅读 ( 3810 )
* 分类：[渗透测试](https://forum.butian.net/community/Pen_Testing)

8 推荐
 收藏

## 0 条评论

请先 [登录](https://forum.butian.net/login) 后评论

[![routing](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/b069dce95c0518975caf9c3f06666af311e4423.png)](https://forum.butian.net/people/29988)

[routing](https://forum.butian.net/people/29988)

网络安全工作者

5 篇文章

[奇安信攻防社区](https://forum.butian.net)|
联系我们

|
[sitemap](https://forum.butian.net/sitemap)

Copyright © 2013-2023 BUTIAN.NET 版权所有 [京ICP备18014330号-2](https://beian.miit.gov.cn/#/Integrated/index)

×

#### 发送私信

请先 [登录](https://forum.butian.net/login) 后发送私信

×

#### 举报此文章

垃圾广告信息：
广告、推广、测试等内容

违规内容：
色情、暴力、血腥、敏感信息等内容

不友善内容：
人身攻击、挑衅辱骂、恶意行为

其他原因：
请补充说明

举报原因:

取消
举报

×

#### ![routing](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/b069dce95c0518975caf9c3f06666af311e4423.png)

如果觉得我的文章对您有用，请随意打赏。你的支持将鼓励我继续创作！

![]()

---