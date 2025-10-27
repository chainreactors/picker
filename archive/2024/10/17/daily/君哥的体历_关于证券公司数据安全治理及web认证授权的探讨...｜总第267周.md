---
title: 关于证券公司数据安全治理及web认证授权的探讨...｜总第267周
url: https://mp.weixin.qq.com/s?__biz=MzI2MjQ1NTA4MA==&mid=2247491540&idx=1&sn=a1d7c10a2bf5aa6557b50343d334fd4a&chksm=ea4bb593dd3c3c85fd557bb69b7a19599d6af16fda8b8d88216e0becdb2d0739179b395b6162&scene=58&subscene=0#rd
source: 君哥的体历
date: 2024-10-17
fetch_date: 2025-10-06T18:52:16.474920
---

# 关于证券公司数据安全治理及web认证授权的探讨...｜总第267周

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/yXsxtS2cfwYwJLxcxNCGWicrKRcIgkCIaiaXGS91Beq7nicAvxBoVO0BYFJPC8kA5NQVG0O1aS71f9oPEYbFPpv0A/0?wx_fmt=jpeg)

# 关于证券公司数据安全治理及web认证授权的探讨...｜总第267周

原创

群秘

君哥的体历

![](https://mmbiz.qpic.cn/mmbiz_gif/yXsxtS2cfwYLicju4TyAeQhibftSnibn1R9dnxB7tCR0JyCicooUTh4rDmWsBv1wBniaFHVGdaNmMeJOl1hVIicPKkzg/640?wx_fmt=gif)

**0x1本周话题**

*话题一**：**请教一下，证券公司数据安全治理，特别是办公环境和远程办公的安全控制访问，很多投研人员希望在办公环境访问组合持仓等信息，这种需求怎么做好安全控制的？*

A1：云桌面或数据沙箱封装，水印威慑，应用侧做数据操作记录。

A2：这个不是安全问题，属于业务问题，是否允许。只读还是可以操作。目前监管对投研的远程办公有限制。

A3：我们的做法是前置化处理，在应用侧前面部署零信任应用数据安全网关，做入口统一管控，不用改造业务去实现几个目的。

* 收敛应用暴露面，包括办公网内的暴露面，防止被攻击，包括1day、0day防护；
* 做权限动态收敛，基于场景去收敛权限，比如远程访问时和内部访问时权限动态调整，实现最小化授权防止内部越权；
* 管控数据操作，比如跨网的应用在办公网不允许下载，交易网可以正常下载，防止不该出去的数据被下载；
* 人员行为审计，以人的视角对完整行为审计，人/部门访问什么应用获取了什么数据；
* 最后对数据处置，基于场景来动态处理数据，非安全区域访问增加水印和脱敏，交易区这种安全区域访问不做特殊数据处理。这样把数据的管控行为前置化，避免不该访问的数据被访问，不该在特定环境获取的数据被下载，完整行为被审计。对于必须下载的数据，在终端侧用VDI或是沙箱来防止数据外发。

A4：按照你的这个方案，业务方需要做如下动作：

* 业务系统配合反向代理接入数据网关；
* 结合业务场景和角色提供明确的授权配置以及环境依赖信息，用于做动态调整，比如人资数据，业务和角色的操作关系，合理时间段等；
* 需要代理文件流做劫持阻断，配合给出对应的文件数据类型用于网关配置规则；
* 提供脱敏数据字段用于配制规则；
* 安装终端沙箱用于落盘。

  ‍

![](https://mmbiz.qpic.cn/mmbiz_jpg/yXsxtS2cfwZSeZo0a7Whsqnlu9xDF9M7ViaSqZLJ2Dz0TGpH9BA6fsdwnUIzEcIHKLay3Sibiac5aLeFgKeWw0ksw/640?wx_fmt=jpeg&from=appmsg)

*话题二:请教个web认证授权方面的问题：内网有个应用a http://a.xxx.com/，没有认证功能，互联网DMZ区有个java应用，https://d.xxx.com/d1/d2/带用户认证功能，d需要调用a，a返回的结果为url http://a.xxx.com/a1/a2/suijishu/，带用户交互反馈。*

*现在需要应用d的互联网用户，登录d后可以访问a的url页面，未经登录d不能访问a的url页面（最好a的页面不直接暴露在互联网）。请问有啥办法吗？**【目前开发提供的方案】没有认证授权功能（说没法做），在d中web嵌入iframe让用户访**问**http://d.xxx.com/a1/a2/suijishu/*

*（实际以代理方式映射到http://a.xxx.com/a1/a2/suijishu/ 完全绕开d的认证），这样互联网侧就相当于无限制访问 http://a.xxx.com/a1/a2/suijishu/ 以及整个应用a。*

A1：内网调互联网？可以在a的前面插一个ng，必须经过它，然后ng必须认证。

A2：是互联网应用，调用内网的页面。没明白，新的ng跟d是什么关系呢？怎么做认证？原文是这样，“希望应用d的互联网用户登录d后可以访问a的url页面，未经登录d不能访问a的url页面（最好a的页面不直接暴露在互联网）”。

A3：ng可以用跟d一样的授权系统，是sso就sso，把不可改造的外部系统转化成了可改造的系统，然后这个可控系统(ng)通过转发鉴权控制着每个uri的访问逻辑，没鉴权的拒绝访问。

A4：加一个中间层。不要通过 iframe 直接暴露a。

A5：可以参考这个。

https://blog.csdn.net/u010260632/article/details/139173856

A6：主要是iframe没用，后面出了问题还是安全来背锅。

A7：可以将a站点通过API网关暴露来解决，认证网关可以实现。如果没有网关，可以通过b站点包一层来实现认证。加网关其实更好了，相当于把请求单独处理了，内部解析交互数据，外部碰不到a。

![](https://mmbiz.qpic.cn/mmbiz_jpg/yXsxtS2cfwY8ng18pFfGia3TJicRibJhDymqianCWicvx1V31wWia2pCwoe2SSpugexibyEv5JCkK21PqlxVI5fYtRHbg/640?wx_fmt=jpeg&from=appmsg)

A8：我单位现在也面临这种API对外暴露的情况，我在考虑这个方案是否有复用性。对于“b站点包一层来实现认证”再访问a，开发说不知道怎么做。

A9：API网关可以做认证、加签验签、限流等安全措施，对安全来说非常友好，可以统一做API安全管控。我感觉类似于用户和b站点交互，b站点再和a交互，b站点可以拦截请求做检查，但是这需要研发改代码。

也要视具体情况分析，这样的架构设计是否合理，研发运维是否接受，是否符合内部规范。

A10：现在在金融，研发自己就重视底线。以前在互联网，没有强制要求，但是有SRC，这种问题，最后都是要交钱的，结果是开发也重视、主动出解决方案、出过滤器、出统一网关 所谓不会，根本还是不想动，觉得不关自己事。

A11：感觉是b站点研发和a站点研发会扯皮了，b站点研发要负责解决a站点的认证问题。 长期建议建设统一的解决方案，再来一个c站点怎么办？

A12：这个对我们应该比较好做，如果没有理解错的话，可以把我们应用网关部署到前面，DNS引流过来，网关上判断请求是否来自互联网。

如果来自互联网就触发用户强制认证（网关来触发，应用不需要改造）内网或是其他地方访问，可以不用走交互认证（根据位置或是请求方式判断）。

如果需要经D认证，网关调用认证时使用D的认证方式来进行，这样实现会话一致性。

A13：不会就引入外部技术也是个解决方案。

A14：这个对我们是很成熟的方式，相当于在前面作为应用网关，请求过来后，基于条件和身份来判断，什么样的需要经过认证，什么样的不需要。

做业务访问入口后，业务接入进来后不用改造，通过网关的技术来动态帮业务完成认证、鉴权或是更深的数据控制的一些场景。

A15：鉴权要做成标准服务，可以通过SAML或者OAuth2.0进行对接的。

![](https://mmbiz.qpic.cn/mmbiz_jpg/yXsxtS2cfwY8ng18pFfGia3TJicRibJhDymUHV85NPAJWuy489bKB8O8Z6jTsz4nJc178RBF8kovWQlcJDq28IBEg/640?wx_fmt=jpeg&from=appmsg)

*话题三：请教个技术问题。如果云上web公网暴露，通过域名cname到waf到透明模式fw到alb到ecs，这种架构下ecs安全组允许互联网访问到80/443的源ip是否都只允许云WAF回源ip，因为waf会将做公网源地址转换。*

A1：应该要这样限制，不然可以绕过waf。ecs安全组是内网了，你这个应该LB上做访问控制。如果waf是私有化部署，那看LB是不是内网的，那就不存在这个问题了。

A2：不应该在那个ALB上做防护么？为啥要直接在ecs上做？

A3：fw也行。流量都会过透明fw。像公有云fw都会自己收集回源地址，不用太关注回源地址的变化。

A4：为什么alb接到一个公网的ecs上面的？alb（独立IP/动态IP）->vip（内网）->内网服务群。应该是这样才对吧。

A5：Ecs是内网的，用的是云waf。我是想确认，如果这种架构，是不是fw，alb，ecs上看到来自互联网的数据包，三层IP地址都是WAF回源的公网ip。

如果是这种，就可以把web server的入向安全组从允许0.0.0.0收成仅允许WAF回源的公网ip。

A6：fw或alb配waf回源ip，ecs的web端口只需要配alb的内网ip。alb的安全组入栈应该是waf的地址，ecs的安全组入栈应该是alb对应的vip。

A7：建议直接启用alb的waf透明模式。waf肯定会做源ip地址转换，alb是否做了源ip转换需要确认是吧。这个会产生什么效果呢？

A8：不需要配waf回源ip。

A9：这些制度要求需要员工签署吗？

A10：有个确认函，名称叫关于知悉公司规章制度及录用条件的确认函。你去网上搜一下模板，就是把公司相关的管理制度、安全制度啥的都写进去，然后关于这些制度的阅读位置存放位置都写进去，签署即表示阅读，即表示知悉。

![](https://mmbiz.qpic.cn/mmbiz_jpg/yXsxtS2cfwYuOg5DmleORocRpynfNP3zLUmLoic12hOibgibjzzJR2yl9KGmEKEf0Zs8UYKNdaicktzic8u4ibVdKNFQ/640?wx_fmt=jpeg&from=appmsg)

---

**0x2 群友分享**

**【安全资讯】**

[**美国大幅下修就业数据，过去一年造假注水50%**](https://mp.weixin.qq.com/s?__biz=MzU5MzcyMzc2OQ==&mid=2247782889&idx=1&sn=19e636aee381e231f0359f49c999d7ca&scene=21#wechat_redirect)

[**黎巴嫩驻联合国代表团：爆炸的通信设备抵黎前就被植入炸药！美媒爆料：以色列多年前设立空壳公司实施该计划**](https://mp.weixin.qq.com/s?__biz=Mzg3NTA5MjkyNQ==&mid=2248366091&idx=1&sn=6ac4738e81b29f4a19bc6cf19f080ecc&scene=21#wechat_redirect)

[**起底“台独”网军“匿名者64”**](https://mp.weixin.qq.com/s?__biz=Mzk0OTUyOTc1Ng==&mid=2247493635&idx=1&sn=26bb923e72d7ea712f170ffeba6d4bbe&scene=21#wechat_redirect)

[**【新闻联播】多项政策发力 进一步支持经济稳增长**](https://mp.weixin.qq.com/s?__biz=Mzk0NDAwMDExMA==&mid=2247566814&idx=1&sn=602ddadb0828cdb01705ff9907064a7d&scene=21#wechat_redirect)

[**众议院听证会上，CrowdStrike 将蓝屏事件归咎于“多种因素叠加”**](https://mp.weixin.qq.com/s?__biz=MjM5NjA0NjgyMA==&mid=2651302721&idx=1&sn=e6122589b699df7e25b6d5a48c959e51&scene=21#wechat_redirect)

[**太“疯狂”！运营商“内鬼”搭建特殊通道，发送短信805万余条……**](https://mp.weixin.qq.com/s?__biz=MjM5ODMzOTYwMA==&mid=2650820222&idx=1&sn=79613de5be442b46cbd801adda2e20cd&scene=21#wechat_redirect)

[**炫技未果 黑客落网 一案双查！**](https://mp.weixin.qq.com/s?__biz=MzU0MTA3OTU5Ng==&mid=2247547600&idx=1&sn=0600a22e6dc9c61ff64d757c21851846&scene=21#wechat_redirect)

[**细思恐极；供应链植入 PETN，远程遥控引爆 BP 机！**](https://mp.weixin.qq.com/s?__biz=MzU5ODYzNjI4Ng==&mid=2247522942&idx=1&sn=436e11a607f0536073f00cbd59cba759&scene=21#wechat_redirect)

关于公开征求对《工业和信息化领域数据安全合规指引（征求意见稿）》意见的通知

**[2024网络安全执法案例集](https://mp.weixin.qq.com/s?__biz=MjM5OTk4MDE2MA==&mid=2655255046&idx=1&sn=a81aa1a270549d0917de7445f2626bc7&scene=21#wechat_redirect)**

****【行业思考】****

[**金融安全架构设计中的反思**](https://mp.weixin.qq.com/s?__biz=Mzg3ODAzNjg5OA==&mid=2247485266&idx=1&sn=46b03ae8317f257778080688fc4f821c&scene=21#wechat_redirect)

**【安全技术】**

**[CVE-2024-20017 的四种利用方式](https://mp.weixin.qq.com/s?__biz=MzU4OTk0NDMzOA==&mid=2247489594&idx=1&sn=443dcb55acbdba010032ccc3f2f38d2a&scene=21#wechat_redirect)**

---

由于微信修改了推送规则，需读者经常留言或点“在看”“点赞”，否则会逐渐收不到推送！如果你还想看到我们的推送，**请点赞收藏周报，将****【****君哥的体历】****加为星标或每次看完后点击一下页面下端的“在看”“点赞”。**

![](https://mmbiz.qpic.cn/mmbiz_jpg/yXsxtS2cfwYaBZeQPdr2gbHqon58JxAIpZTicPdU1I8I0lBV82ur0C278ycyU7FKAvOEibactZPNC8L1mu7zMZAQ/640?wx_fmt=jpeg)

【金融业企业安全建设实践群】和【企业安全建设实践群】每周讨论的精华话题会同步在本公众号推送（每周）。**根据话题整理的群周报完整版——每个话题甲方朋友们的****展开讨论内容——每周会上传知识星球**，方便大家查阅。

---

**往期群周报：**

**[linux主机如何防护？APP端的报文传输安全业内怎样防御？应用系统版本迭代，上线前都要做安全测试及漏扫吗？｜总第266周](http://mp.weixin.qq.com/s?__biz=MzI2MjQ1NTA4MA==&mid=2247491535&idx=1&sn=e33448e598b34171723635693204fb84&chksm=ea4bb588dd3c3c9e095e95cfc647683de83dde44eea3fced7d620cf50b6d8c0315ec049e32c6&scene=21#wechat_redirect)**

**[如何做软件正版化管控？是否有项目能同时解决安全、运维和开发的问题？以及在生产环境开web应用漏扫策略的探讨...｜总第265周](http://mp.weixin.qq.com/s?__biz=MzI2MjQ1NTA4MA==&mid=2247491530&idx=1&sn=be1ffd6982afc3ae34f5396a53521e58&chksm=ea4bb58ddd3c3c9b57bad6eadb7e343e9c3a9420fc0e120d96c5af7deca2a62558f2efb20c69&scene=21#wechat_redirect)**

**[基于运维/安全角度下的资产治理，以及探讨开发终端装agent做解密和监控进程，影响编译效率时有无更好解决方案...｜总第264周](http://mp.weixin.qq.com/s?__biz=MzI2MjQ1NTA4MA==&mid=2247491519&idx=1&sn=df1460756caa4a32b179674c2392b7e0&chksm=ea4bb5f8dd3c3cee2ba636f1f2594a13bcc0d063239ac947a12701ba11271917b20412d0c53f&scene=21#wechat_redirect)**

---

## **如何进群？**

**如何下载群周报完整版？**

**请见下图：**

![](https://mmbiz.qpic.cn/mmbiz_jpg/yXsxtS2cfwbppZu5PBSictiaObD2Bnru4z5nSyfMrsqjPO0micwA8CsIDUxRb73kIPomrYtYpWuWqPwMU17LHAIpg/640?wx_fmt=jpeg)

‍

‍

‍

‍

‍

‍

预览时标签不可点

阅读原文

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/yXsxtS2cfwbbrvrPJc9bTvZFr7n5ZgdWsRKc2GvxcQNogPzLOcveKPP2vpaicqWsRiaASYeEsbAYNsDUWPQ6pyeg/0?wx_fmt=png)

君哥的体历

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/yXsxtS2cfwbbrvrPJc9bTvZFr7n5ZgdWsRKc2GvxcQNogPzLOcveKPP2vpaicqWsRiaASYeEsbAYNsDUWPQ6pyeg/0?wx_fmt=png)

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
...