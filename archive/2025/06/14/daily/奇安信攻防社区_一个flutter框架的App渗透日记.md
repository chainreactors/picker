---
title: 一个flutter框架的App渗透日记
url: https://forum.butian.net/share/4405
source: 奇安信攻防社区
date: 2025-06-14
fetch_date: 2025-10-06T22:50:38.760295
---

# 一个flutter框架的App渗透日记

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

### 一个flutter框架的App渗透日记

* [渗透测试](https://forum.butian.net/topic/47)

客户安排了一个App的渗透测试，但是App抓不了包，于是展开一顿分析，最终进入内网………….

\*\*测试过程\*\*
1.使用Clash，打开全局代理进行抓包测试，发现验证码未加载，此时疑惑是否检测代理软件。
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/05/attach-ccb0bde42f0066f88b3fea65c3f9a22e162819b2.png)
2.使用clash透明代理将防火墙转发流量进行抓包测试，竟然抓到了相关的数据包，但是此时还是没有成功通信。
![](https://xz.aliyun.com/api/v2/files/762f2a69-c0f8-339a-939e-3aeb2217d7e4)
3.这时还是非常纳闷为什么抓到了包还是无法访问，于是将数据包发送至repeater进行单独的服务器访问分析。
![](https://xz.aliyun.com/api/v2/files/c8e7f4f5-0a36-33f8-a7e9-3b82edcf0c51)
4.很显然，这个数据超乎我想象的简单，也就是说它不像是APP构造的包，更不像浏览器构造XHRrequest包，尤其这个user-agent特别具有标识，这时对useragent信息进行收集，因为最初猜测可能和证书相关，最终确认是flutter框架开发的App，特征都能吻合上，so库以及useragent等特征。
![](https://xz.aliyun.com/api/v2/files/08008249-b80e-3881-b057-a1d50bd68b93)
![](https://xz.aliyun.com/api/v2/files/f83b12b4-d729-36c9-9dab-6e83dd14d9b5)
5.请教大佬以及熟人是否做过相关分析。
![](https://xz.aliyun.com/api/v2/files/209cc7a0-34be-3a8a-9044-e9df82fdbb52)
![](https://xz.aliyun.com/api/v2/files/3d4bc180-7ff4-3312-97bf-d219bb701865)
![](https://xz.aliyun.com/api/v2/files/4c8f4ad2-cb4a-3726-a2b1-1dd34cdb60fd)
6.由于在我收集的信息里，大量的flutter证书bypass的文章，我下意识就认为ssl的问题，但是师傅说的又没错，这是一个http的包。于是震惊我中华的第二天早上，我发现这tm居然是个内网地址。
![](https://xz.aliyun.com/api/v2/files/cfa2e472-fc40-3cfe-a103-90591790e4aa)
7.于是我百思不得其解，初步我设想是App做成本地请求+SDK(ssl认证转发发送)，于是我又尝试一些常规方法，对App源码进行分析，但是这个App源码竟然全体进行混淆，虽然没有加壳，但是这个混淆却异常的牛逼(有无师傅知道源码混淆如何还原，求求)，我尝试了关键词搜索，例如okhttp分析，libssl.so分析，以及一些字符串，JSON数据包hook分析，竟然没有找到任何与这个Dart发出来的请求相关的信息。然后就只能将希望寄托于网上的flutter分析，希望足够简单能够支持我解决抓包问题。
![](https://xz.aliyun.com/api/v2/files/90391eee-a9d0-3cee-93a2-523f871590eb)
文章参考链接: <https://www.ctfiot.com/217117.html>
![](https://xz.aliyun.com/api/v2/files/e9352205-2c62-3797-8229-4474fd079cc0)
8.于是拿到了so的ssl bypasshook函数。
![](https://xz.aliyun.com/api/v2/files/f299e0e8-4977-3af5-b4eb-732fe4358fde)
9.万幸互联网居然有对这个地址的分析，我以为十拿九稳了，将地址填充进代码测试。![](https://xz.aliyun.com/api/v2/files/2924cc35-1c93-3853-a491-87c45e263129)
10.如图下代码，进行hook测试，发现依旧无法成功抓包。
![](https://xz.aliyun.com/api/v2/files/84371798-9c7a-3cc8-86aa-83bdee625a71)
11.此时心态有点崩溃，但是重新振作了一下，在github找寻所有的libflutter.so分析，终于找到了一个可以用的项目，这个点赞量以及项目更新时间都非常符合我心意。
![](https://xz.aliyun.com/api/v2/files/5950aed4-8229-32c1-a24e-f02bc4065e1b)
12.使用该脚本我成功做到抓包自由，当然该脚本细节也非常牛逼，将SO文件内存解析然后拿到导出地址来进行操作，对逆向分析flutter框架特别感兴趣的师傅可以研究一下。地址<https://github.com/hackcatml/frida-flutterproxy>
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/05/attach-7c738e998cb6ff523607ed0546dcae64c64c48af.png)
13.但是这个发出来的包还是，无法访问，但是我自作聪明的是，我有这个prod-api的公网地址，于是我用mitm给他替换成公网地址，侥幸通过了通信问题。
![](https://xz.aliyun.com/api/v2/files/0f2b7033-be90-3231-8fef-e000b352ec31)
14.我也拿到了验证码成功的登录进了系统，我以为我能狸猫换太子这样的安安静静的测试了，但是！这个App核心业务是内置了的h5应用，也就是说有一部分请求是走的webview。也就是说该hook脚本只能抓包soket的包，也是通过flutter.so发起请求的包。并不能抓到js发起请求的包。于是我又开始对webview的分析。这里直接放送代码。
Java.perform(function () {
//实例化一个对象
var WebView = Java.use('android.webkit.WebView');
//重写WebView类的重载方法，因为setWebContentsDebuggingEnabled不是静态方法，所以需要一个对象来调用这个方法
WebView.$init.overload('android.content.Context').implementation = function (a) {
console.log("WebView.$init is called!1");
var retval = this.$init(a);
this.setWebContentsDebuggingEnabled(true);
return retval;
}
WebView.$init.overload('android.content.Context', 'android.util.AttributeSet').implementation = function (a, b) {
console.log("WebView.$init is called!2");
var retval = this.$init(a, b);
this.setWebContentsDebuggingEnabled(true);
return retval;
}
WebView.$init.overload('android.content.Context', 'android.util.AttributeSet', 'int').implementation = function (a, b, c) {
console.log("WebView.$init is called!3");
var retval = this.$init(a, b, c);
this.setWebContentsDebuggingEnabled(true);
return retval;
}
//始终设置为true,打开调试
WebView.setWebContentsDebuggingEnabled.implementation = function () {
this.setWebContentsDebuggingEnabled(true);
console.log("setWebContentsDebuggingEnabled is called!");
}
});
// frida -U -f package\\_name -l .\\hook.js --no-pause
15.该代码可以打开CDP分析的入口，于是我用inspect打开看了一下请求网络，我发现通往其他应用的入口竟然也是内网地址。
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/05/attach-8ff9b472f92b0531d7d6a5b01f5dee417638101a.png)
16.这时候我突然就意识到不对劲了，各种信息告诉我事情并非我想象的那样，于是我总结了一下信息，各位师傅还记得第一张图吗？是否关注到这里面有一个SanforidClient，组件里面也有大量的深信服的SDK。不会吧，因为我是第一次碰见深信服sslvpn sdk的App，但是我自认为应该没有开发那么蠢，在App里内置了一个默认的用户吧。
![](https://xz.aliyun.com/api/v2/files/5d647a73-a25b-331e-8014-4ad909440406)
![](https://xz.aliyun.com/api/v2/files/790d3f98-4e85-3bd8-b16c-20193a7fce8e)
17.带着深信服Sdk的核心特征去github搜索，我从源码中关注到了认证方法。
![](https://xz.aliyun.com/api/v2/files/b4e66c43-077c-3855-93f5-af787c99363b)
18.于是我成功拿到了认证的用户名以及密码以及服务器地址，成功拨进vpn。
![](https://xz.aliyun.com/api/v2/files/3d7042fc-7dfa-3ef3-877c-64203ef4ce86)![](https://xz.aliyun.com/api/v2/files/db2ed904-9bf4-3e79-8d14-97902637fcab)
19.总结，也就是说，为什么抓不到包，是因为内置了深信服的sdk去通信，将流量通过sokcet或者回环也好转发至burp，由于PC并不能访问内网地址所以导致抓到了包也无法访问接口，同时也学习到了flutter的常规特征。后续如果碰到类似深信服SDK的可以直接进行相关账户找寻........

* 发表于 2025-06-13 09:00:02
* 阅读 ( 4706 )
* 分类：[漏洞分析](https://forum.butian.net/community/Vul_analysis)

3 推荐
 收藏

## 2 条评论

[![](https://forum.butian.net/static/images/default_avatar.jpg)](https://forum.butian.net/people/29807)

**[andyzzx](https://forum.butian.net/people/29807)**
2025-06-16 11:20

good！

* [0 条评论](#comment-2550)
* 0

请先 [登录](https://forum.butian.net/login) 后评论

[![](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/b35f9ec5dd87bbfd70f4490a6eab00aec5adc8e.jpg)](https://forum.butian.net/people/16588)

**[爸爸的爸爸](https://forum.butian.net/people/16588)**
2025-07-03 16:27

nice 我要站在你这个巨人的肩膀上

* [0 条评论](#comment-2575)
* 0

请先 [登录](https://forum.butian.net/login) 后评论

请先 [登录](https://forum.butian.net/login) 后评论

[![nstkm](https://forum.butian.net/static/images/default_avatar.jpg)](https://forum.butian.net/people/13699)

[nstkm](https://forum.butian.net/people/13699)

2 篇文章

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

#### ![nstkm](https://forum.butian.net/static/images/default_avatar.jpg)

如果觉得我的文章对您有用，请随意打赏。你的支持将鼓励我继续创作！

![](https://shs3.b.qianxin.com/attack_forum/2025/04/qrcode-592a28b3f06582a20c042fb8be3aa437a3445508.jpg)

---