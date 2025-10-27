---
title: 钓鱼对抗之Coremail安全拦截
url: https://www.4hou.com/posts/YY7O
source: 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com
date: 2023-05-23
fetch_date: 2025-10-04T11:36:44.403948
---

# 钓鱼对抗之Coremail安全拦截

钓鱼对抗之Coremail安全拦截 - 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com

[![](https://www.4hou.com/sihou/images/new4hou/newlogoss.png)](https://www.4hou.com)

* [首页](https://www.4hou.com)
* [企业中心](https://www.4hou.com/corp/newindex)
* [产业研究院](https://www.4hou.com/real-time)

![](https://www.4hou.com/sihou/images/new4hou/search-icon.png)

[投稿](https://www.4hou.com/contribute)

[登录](https://www.4hou.com/login)
  |
[注册](https://www.4hou.com/register)

* 导读 ▾
* [活动](https://www.4hou.com/newticket)
* [专题](https://www.4hou.com/category/special)
* [图谱](https://www.4hou.com/atlas/index)
* [报告](https://www.4hou.com/new-report-info)
* [嘶票](https://www.4hou.com/tickets)
* [嘶货](https://www.4hou.com/shop)
* [企业查询](https://www.4hou.com/corp/new-search-company)
* [招聘](https://www.4hou.com/recruit)![](https://www.4hou.com/sihou/images/1561626446625934.png)

* [新闻](https://www.4hou.com/category/news)
* [行业](https://www.4hou.com/category/industry)
* [趋势](https://www.4hou.com/category/observation)
* [访谈](https://www.4hou.com/category/people)
* [漏洞](https://www.4hou.com/category/vulnerable)
* [WEB安全](https://www.4hou.com/category/web)
* [业务安全](https://www.4hou.com/category/business)
* [系统安全](https://www.4hou.com/category/system)
* [内网渗透](https://www.4hou.com/category/penetration)
* [勒索软件](https://www.4hou.com/category/typ)
* [安全工具](https://www.4hou.com/category/tools)

# 钓鱼对抗之Coremail安全拦截

CACTER
[行业](https://www.4hou.com/category/industry)
2023-05-22 11:03:01

![](https://img.4hou.com/article/%E6%B5%8F%E8%A7%88.png)116241

收藏

导语：攻击者为绕过邮件系统的安全网关，针对钓鱼邮件进行了各种绕过，伪装。其中最为常见的就是二维码钓鱼，附件WORD文档中嵌入二维码图片，附件嵌入图片，这种攻击方式，普通常见邮件安全网关，邮件分析系统很难做到防御分析，存在被安全绕过的情况。基于此，我们可以通过Coremail自身的安全策略，关键字策略，实现对钓鱼邮件的拦截防护。

钓鱼邮件，是一种常见的网络诈骗手段。一般目的是用来欺骗收件人，将账号、口令或密码等信息回复给指定的接收者，或附有超链接引导收件人连接到特制的钓鱼网站或者带毒网页，这些网页通常会伪装成和真实网站一样，令收件人信以为真。钓鱼邮件由于攻击成本低，收益大，被不法分子以及红蓝对抗攻防中红队广泛使用。获取到组织中一个用户的账户密码，已此为跳板，可能会造成整个组织邮件，电话信息泄露，并进一步对组织内的其他用户进行钓鱼诈骗，危害十分严重。

攻击者为绕过邮件系统的安全网关，针对钓鱼邮件进行了各种绕过，伪装。其中最为常见的就是二维码钓鱼，附件WORD文档中嵌入二维码图片，附件嵌入图片，这种攻击方式，普通常见邮件安全网关，邮件分析系统很难做到防御分析，存在被安全绕过的情况。基于此，我们可以通过Coremail自身的安全策略，关键字策略，实现对钓鱼邮件的拦截防护。

基于平常安全监控，运维，我们可以把钓鱼类邮件分为以下几类，并采取相应拦截策略：

**一、补贴诈骗类**

 补贴诈骗类主要是通过以劳动补贴和退税等主题给用户发送钓鱼邮件。用户使用手机进行扫描二维码后，自动打开钓鱼网站，钓鱼网站会诱导用户输入自己的银行卡账号和密码等信息。

![图片1.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230522/1684724503852663.png "1684394596169077.png")

1.补贴诈骗\_主题\_丢弃

补+.\*贴+.\*通+.\*知|.\*当天未完成视为放弃申领.\*|.\*薪资补贴到账.\*|.\*个.\*人.\*劳.\*动.\*补贴.\*|.\*工资补贴.\*|.\*个.\*人.\*劳.\*动.\*补.\*贴.\*申.\*领.\*通.\*知.\*|.\*个.\*人.\*劳.\*动.\*已.\*下.\*发.\*|.\*劳动补贴已下发.\*|.\*个人劳动津贴.\*|.\*本月补助通知.\*|.\*薪资补助下发.\*|.\*本月补助.\*|.\*劳动补贴领取.\*|.\*工薪补助登记.\*|.\*工薪补助相关材料登记.\*|.\*生活补贴请查收.\*|.\*个人所得税资料补充.\*|.\*个人所得税补贴资料.\*![2.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230522/1684724504201482.png "1684394628205167.png")

2. 补贴诈骗\_附件\_丢弃

.\*补贴通知.\*|.\*个人劳动补贴.\*|.\*薪资补贴.\*

3. 补贴诈骗\_正文\_丢弃

(补[\s\S]\*贴[\s\S]\*二维码[\s\S]\*)|(补[\s\S]\*贴[\s\S]\*[附咐][\s\S]\*件)|(补[\s\S]\*贴[\s\S]\*领取)

**二、钓鱼攻击**

攻击者会使用自身服务器进行搭建，通过对一些开源CMS系统代码进行简单修改搭建，从而达到钓取账号密码的效果。

![3.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230522/1684724505172662.png "1684394642226166.png")

1. 钓鱼\_主题\_丢弃

.\*关于邮箱系统更改.\*|.\*关于邮箱账户报备.\*|.\*新邮件系统通知.\*|.\*启用新邮件系统通知.\*|.\*邮箱系统提醒.\*|.\*邮局系统升级备案.\*|.\*邮箱安全警告.\*|.\*公司启用新邮件系统通知.\*|.\*账号停用通知.\*|.\*您有一条未读邮件.\*|.\*新的邮件请查收.\*|.\*was hacked! Change your password now.\*|.\*电子邮件终止通知.\*|.\*DHL Consignment Notification To.\*|.\*Your Password Expires Today.\*|.\*OA更新提示.\*|.\*Update Your Mailbox.\*|.\*邮箱迁移通知.\*|.\*您的密码即将失效请及时.\*|.\*管理员通知.\*|.\*管理员提示.\*|.\*管理员提醒.\*|.\*A new invoice is available.\*|.\*密码今天过期.\*|.\*OA邮箱提示.\*|.\*关于bankalliance.com.cn升级扩容的通知.\*|.\*OA系统邮件.\*|.\*邮箱安全升级重要公告.\*|.\*邮箱管理员.\*|.\*账号暂停.\*|.\*账户已暂停收发信权限.\*|.\*系统检测到账户.\*|.\*您的账户异常登录请及时处理.\*|.\*未读邮件类别 .\*|.\*Urgent Account Information.\*|.\*您的账户异常登陆请及时处理.\*|.\*保护您的电子邮件帐户.\*|.\*今天到期,请及时确认.\*|.\*异地登录提醒.\*|.\*OA待处理.\*|.\*邮箱升级.\*|.\*OA管理提醒.\*|.\*关于邮服系统个人备案通知.\*|.\*邮箱系统备案升级.\*|.\*邮箱外发服务关闭.\*|.\*邮箱更新通知.\*|.\*邮箱系统升级备案.\*|.\*邮箱消息.\*|.\*OA系统更新.\*|.\*三日后无法使用.\*|.\*邮箱系统迁移.\*|.\*账户异常登录活动.\*|.\*邮件系统的安全性通知.\*|.\*电子邮件帐户终止.\*|.\*邮箱系统升级.\*|.\*电子邮件终止请求.\*|.\*您的邮箱存在安全隐患.\*|.\*您有一条新的邮件.\*|.\*新的邮件通知.\*|.\*邮箱过期提醒.\*|.\*OA系统升级通知.\*|.\*您的邮箱账户收到可疑邮件.\*|.\*邮箱账户已暂停使用.\*

2. 钓鱼\_正文\_丢弃

[\s\S]\*邮箱配额通知[\s\S]\*|[\s\S]\*保持当前密码[\s\S]\*

![4.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230522/1684724506165004.png "1684394670168943.png")**三、广告推广**

广告邮件禁止投递

.\*HRBP.职.业.培.训.\*|.\*项目全过程管理控制与实践.\*|.\*销售渠道建设与管理.\*|.\*PPT商务设计与呈现技巧.\*|.\*五星服务：客户服务创新与投诉处理.\*|.\*4个G内容涵盖了企业各个方面.\*|.\*代开增值税发.\*|.\*需要正规普票加微信.\*|.\*代开普.\*|.\*鼓励比价的礼品采购.\*|.\*PPT美化与设计服务.\*|.\*购买发票加微信.\*|.\*代.\*开.\*增.\*值.\*税.\*发.\*票.\*加.\*微.\*信.\*|.\*发票加微信.\*|.\*.\*开.\*普.\*票.\*加.\*微.\*信.\*|.\*标杆参访的计划，以及近期公开课安排.\*|.\*标杆参访的计划，以及近期公开课安排.\*|.\*如何打造高绩效的研发团队.\*|.\*我想和你做生意.\*|.\*需.\*要.\*普.\*票.\*加.\*微.\*信.\*|.\*开正规普票加微信.\*|.\*HRBP职业培训.\*

    通过设置拦截策略，可实现对绝大部分通用钓鱼的拦截防护，实施具体效果如图：

![5.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230522/1684724507182350.png "1684394685717240.png")

针对邮箱管理员配置建议

1. 根据Coremail官方解释，丢弃：先把邮件收下来，再把邮件丢弃。（在smtp连接的时候，给发信人回复250 OK，告诉对方邮件已经收到了，之后再把邮件丢弃）这样做的目的是，让对方以为邮件投递成功了，没有退信。拒绝投递：在smtp阶段会给对方返回550，并给对方退信，给出退信的原因。针对钓鱼类邮件主题建议进行丢弃，如拦截攻击者会收到退信原因，从而针对性对邮件进行变化。而广告垃圾邮件对服务器负载会有影响，建议进行拦截。

2. 安全拦截关键字不是通用，只是作为参考。设置完策略，务必一直对邮件拦截日志进行实施监控，以免正则错误，造成大面积邮件业务拦截影响。

3. 根据拦截的具体措施，单独设置策略，比如主题，正文，附件分离，如果加多层策略，通过日志无法分析具体是哪条安全策略导致的拦截。

4. 关键字正文匹配需要谨慎使用，如使用错误，非常容易导致邮件大面积拦截，建议在Coremail技术确认无误情况下，同时每个拦截单独设置策略。

作者简介：

胡晓磊，男，山东省城市商业银行合作联盟有限公司邮箱管理员，Coremail管理员社区特邀大咖

本文为山东省城市商业银行合作联盟有限公司胡晓磊先生的原创文章，文章首发于Coremail云服务中心管理员社区。转载请附上原文出处链接及本声明。

* 分享至

![取消](https://www.4hou.com/sihou/images/close.jpg)
![嘶吼](https://www.4hou.com/sihou/images/logo.png)

感谢您的支持，我会继续努力的!

![扫码支持]( "扫一扫")

打开微信扫一扫后点击右上角即可分享哟

### 发表评论

评论

![](https://www.4hou.com/captcha/flat?9FCfPm4j)

#### 你可能感兴趣的

* [![]()

  Exchange/M365最新防范攻略！CACTER三步补齐原生防护短板](https://www.4hou.com/posts/l03l)
* [![]()

  【附下载】2025我们身边的 网信安全 典型案例等 官方视频汇编](https://www.4hou.com/posts/kg3x)
* [![]()

  蝉联荣誉！梆梆安全再度获选 “北京市委网信办第二届网络安全技术支撑单位”](https://www.4hou.com/posts/9jKP)
* [![]()

  聚焦可信AI安全！SDC2025 议题重磅揭晓](https://www.4hou.com/posts/gy39)
* [![]()

  2025第五届太原网络安全高峰论坛成功举办](https://www.4hou.com/posts/8gJl)
* [![]()

  特勤局手册 | 监听办公室](https://www.4hou.com/posts/42B2)

![](https://img.4hou.com/portraits/789873803bbe1d5cf9b06a0859e2af0b.png)

# [CACTER](https://www.4hou.com/member/64Y9)

国内领先企业级邮件安全解决方案提供商，提供一站式防护。

#### 最新文章

* [Exchange/M365最新防范攻略！CACTER三步补齐原生防护短板](https://www.4hou.com/posts/l03l)
  2025-09-29 17:48:04
* [【附下载】2025我们身边的 网信安全 典型案例等 官方视频汇编](https://www.4hou.com/posts/kg3x)
  2025-09-29 14:55:37
* [蝉联荣誉！梆梆安全再度获选 “北京市委网信办第二届网络安全技术支撑单位”](https://www.4hou.com/posts/9jKP)
  2025-09-29 14:23:50
* [聚焦可信AI安全！SDC2025 议题重磅揭晓](https://www.4hou.com/posts/gy39)
  2025-09-28 17:20:40

[查看更多](https://www.4hou.com/member/64Y9)

# 相关热文

* [Exchange/M365最新防范攻略！CACTER三步补齐原生防护短板](https://www.4hou.com/posts/l03l)

  CACTER
* [【附下载】2025我们身边的 网信安全 典型案例等 官方视频汇编](https://www.4hou.com/posts/kg3x)

  网络伍豪
* [蝉联荣誉！梆梆安全再度获选 “北京市委网信办第二届网络安全技术支撑单位”](https://www.4hou.com/posts/9jKP)

  梆梆安全
* [聚焦可信AI安全！SDC2025 议题重磅揭晓](https://www.4hou.com/posts/gy39)

  企业资讯
* [2025第五届太原网络安全高峰论坛成功举办](https://www.4hou.com/posts/8gJl)

  企业资讯
* [特勤局手册 | 监听办公室](https://www.4hou.com/posts/42B2)

  RC2反窃密实验室

![]()

[公司简介](https://www.4hou.com/about?title=公司简介)
|
[我要投稿](https://www.4hou.com/about?title=我要投稿)
|
[更新日志](https://www.4hou.com/about?title=更新日志)
|
[友情链接](https://www.4hou.com/about?title=友情链接)
|
[隐私政策](https://www.4hou.com/about?title=隐私政策)
|

[![](https://www.4hou.com/sihou/images/new4hou/weibo.png)](http://weibo.com/u/6069423878)
![](https://www.4hou.com/sihou/images/new4hou/wechat.png)

本站4hou.com，所使用的字体和图片文字等素材部分来源于原作者或互联网共享平台。如使用任何字体和图片文字有侵犯其版权所有方的，嘶吼将配合联系原作者核实，并做出删除处理。

[©2024 北京嘶吼文化传媒有限公司 京ICP备16063439号-1](https://beian.miit.gov.cn/)
本站由 ![](https://www.4hou.com/sihou/images/new4hou/txcloud.png) ![](https://www.4hou.com/sihou/images/new4hou/bdcloud.png) ![](https://www.4hou.com/sihou/images/new4hou/ucloud.png) 提供云计算服务

微信

[微博](htt...