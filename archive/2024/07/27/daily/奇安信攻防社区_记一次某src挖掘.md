---
title: 记一次某src挖掘
url: https://forum.butian.net/share/3103
source: 奇安信攻防社区
date: 2024-07-27
fetch_date: 2025-10-06T17:38:28.517758
---

# 记一次某src挖掘

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

### 记一次某src挖掘

* [渗透测试](https://forum.butian.net/topic/47)

本文作者：Track - blueaurora，渗透思路往往不要太局限了。当我们对某一个登录框站点没有思路时，可以尝试找找是否存在一些说明手册，因为功能点繁多，面向大量的不同单位人群，可能会存在qq群等，好对一些用户问题进行处理，那么就可以通过谷歌语法，对网站名 + 群等关键字搜索，也可以直接在qq群搜索网站名称，或开发商名称进行查找，当你进入他们内部的群时，就可以获取很多敏感信息了，甚至可以直接向运维人员申请修改密码等操作。

### 一、获取web端管理员权限
#### 0x01简单查看一下，发现存在登录以及证书查询操作指南等功能
因该站特征较为明显，所以对页面进行了强打码
![img](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/07/attach-334f09bd2b2468ebd2d5576949fd1d9cf31664f5.png)
#### 0x02弱口令测试（无成果）
既然存在登录口，那么肯定要试试弱口令了，开干！
![img](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/07/attach-87ad379672f10a574fd22bb6af8bd1421906cd8a.png)
经过尝试发现可以对登录用户进行爆破，密码加密了，看着像base64但发现并不是，只能通过爆破发现的用户名手动的测试几个密码了。
![img](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/07/attach-3f7802c6d27ce8e032f0f5e7db3f83b57b29156a.png)
经过手工测试，最后发现一个也没成功的，这运气有点衰啊?，好好好，那就看看注册页面吧
#### 0x03注册用户（无成果）
简单的测试下看看是否存在xss和sql注入，发现并不存在，只能老实注册用户了，但是最后发现需要管理员审核，一直没有通过?
中间注册时发现密码是高强度密码（密码由特殊符号、大小写字母和数字3种组合并且长度大于8位!）这就算爆破也很难爆破到了，直接放弃。
![img](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/07/attach-5298cd055a8fd7dbc16537127365f87388606cf3.png)
![img](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/07/attach-870e39fb862824138d38dc2297f25943fd9f1101.png)
#### 0x04打入内部群组（获取账号名和默认密码格式）
突然发现存在操作手册！看看是否存在什么可利用信息（部分手册可能泄露账号和密码，以及一些其它可供后期利用的信息）
发现默认用户名是手机号码，且存在默认密码和一个技术支持qq群。
![img](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/07/attach-1ce0886d6461c83df1b68fae8a5beaea7485bf7d.png)
然后申请加入qq群，查看聊天记录发现了默认密码格式和手机号，默认密码为XXXX+电话或身份证后6位+XXXX，，尝试去登录发现全都是失败的?这些人的安全意识真不错?，现阶段知道的就是只要登录过的用户就一定修改了密码。
后面让备注自己单位和名字，没有备注就给我踢了?
#### 0x05js审计（获取大量接口）
通过前端代码审计发现存在大量接口，尝试几个发现都需要权限才能访问，又回到了登录问题
![img](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/07/attach-6a4018bd52abe085163f0373aeb1de290881fd67.png)
#### 0x06通过google大法获取登录账号（登录）
因为是教育平台可以通过google语法对学校资产进行收集获取教师电话，然后再根据密码格式进行登录尝试
经过一顿FUZZ之后成功的登上了平台。但是！除了完善资料外，没有其余功能点，且必须修改默认密码后才能获取功能和内容。
![img](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/07/attach-a536124f02461a0ac2ccb2ca64eaa12beacc96ff.png)
#### 0x07越权（获取账号敏感信息）
通过对完善资料处进行抓包发现可通过输入用户名获取用户敏感信息ID、姓名、电话、身份证等信息（但很局限，因为前提需要知道用户名是什么）
![img](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/07/attach-affea7239968310d08c24155a6902c5ba11e0908.png)
#### 0x08修改默认密码获取正常功能
默认密码修改处需获取手机验证码，无法绕过，该怎么办呢？?
对js源码进行审计发现与修改密码相关的接口有三个，其中一个为当前修改默认密码需要获取短信验证码直接忽略，一个提示只可以修改自己的账号密码，第三个提示权限不足
![img](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/07/attach-4be093ffab8bd468afa194bf73570182ffb3fb39.png)
![img](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/07/attach-0b323951675114506c132dce3f2eadc39346dee6.png)
![img](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/07/attach-54696db4d315709c4da296f4a64fed97d26bd40f.png)
![img](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/07/attach-2d50a5e09801ef289849aaa389a97b988294381c.png)
很明显现阶段第二个接口可以尝试用户名密码修改，只是不知道需要哪些具体参数。继续翻看js发现请求参数名
![img](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/07/attach-3055474e56f04745521185ebddd99a4c5d235e1e.png)
输入密码后仍然提示只允许修改自己密码，那么推断缺少一个确认用户的参数，根据前面的越权可以发现存在确认用户的参数可能是id，也可能是username这两个值
![img](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/07/attach-5a0523aa7922c7360320edad8f56398eb2f50d10.png)
通过验证为username参数，并修改密码成功
![img](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/07/attach-5ca460755ab69d05e9409d8792a3851870afb85d.png)
重新登录后获取正常功能点
![img](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/07/attach-cb4e28642f12aa3e00a61622743de047cd5358ee.png)
#### 0x09信息泄露
由于网站接口较多，对部分接口进行测试发现存在需要可以越权访问的接口和部分权限不足，以及不知道正确路径的接口
其中存在有接口存在大量信息泄露，泄露该域所有教师人员信息，
需先通过接口获取学校key值之后再通过另一个user接口获取当前在校职工信息
![img](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/07/attach-7051a5857dc221929a6ae8ba3cef9eb14d09fb4e.png)
![img](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/07/attach-d85027229eccc37368b9685ca1a6897c15338772.png)
mysql数据库账号密码等信息，但未在互联网上开放端口。
![img](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/07/attach-c08fce0272fdb4cbbcf88fa3ffda85eb94dca709.png)
#### 0x10提权=&gt;任意密码重置
通过某接口查看可获取当前在线用户列表，包含token、用户名等信息
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/07/attach-b776ae92af40104e9fe9ffc0c5ac3dd432d1b5fb.png)
之前密码修改中不是存在一个权限不够的接口吗？，那么如果我获取到管理员的token或其他高权限token是不是就能重置了呢?
答案是yes。不过此处因为任意密码重置，判定要素是用户ID。
![img](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/07/attach-0e1675c2f387ba469decebb45755343370a60af6.png)
#### 0x11获取管理员页面
通过现阶段已获取sysadmin权限的token，如何获取管理员页面呢
一、可以通过用户创建接口直接创建一个管理员用户
二、通过用户编辑接口使普通用户获取管理员权限
三、使用管理员token获取管理员页面和功能
使用第三种方案获取管理员页面
在登录管理中心时会通过Permission接口通过当前token判断用户所拥有的功能并返回，（如果提前替换token会导致账号掉线，从而使token失效）然后通过替换Permission接口的返回值来获取管理员页面和功能点。
普通用户返回包大小为几千
![img](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/07/attach-abca32948dee56c6b3c40c90d254b007e1f1aa46.png)
管理员返回包大小为上万，
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/07/attach-4bd7d2dec27176db5bc74ef42a977ec6a05fd831.png)
替换内容
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/07/attach-d9e001940b2ad8e00c1a8e19ffa8c1ee8a4d9d00.png)
查询内容时需每次都替换token很麻烦,且需较快手速，否则会响应超时，可使用插件modheader替换token即可
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/07/attach-f2247fdaebe9c1e1ca9839bb8918fecd09ec0478.png)
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/07/attach-9835d2b253bae830e7409be2baa42a14efe88bbf.png)
#### 0x12总结
渗透思路往往不要太局限了。当我们对某一个登录框站点没有思路时，可以尝试找找是否存在一些说明手册，因为功能点繁多，面向大量的不同单位人群，可能会存在qq群等，好对一些用户问题进行处理，那么就可以通过谷歌语法，对网站名 + 群等关键字搜索，也可以直接在qq群搜索网站名称，或开发商名称进行查找，当你进入他们内部的群时，就可以获取很多敏感信息了，甚至可以直接向运维人员申请修改密码等操作。
最后的最后白嫖10rank
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/07/attach-9777ab9779f0cba8dd595c4653201f1478e00c39.png)

* 发表于 2024-07-26 09:00:00
* 阅读 ( 6507 )
* 分类：[渗透测试](https://forum.butian.net/community/Pen_Testing)

7 推荐
 收藏

## 2 条评论

[![](https://forum.butian.net/static/images/default_avatar.jpg)](https://forum.butian.net/people/33312)

**[凌000](https://forum.butian.net/people/33312)**
2024-07-27 14:26

厉害

* [0 条评论](#comment-2034)
* 0

请先 [登录](https://forum.butian.net/login) 后评论

[![](https://forum.butian.net/static/images/default_avatar.jpg)](https://forum.butian.net/people/33970)

**[12121289](https://forum.butian.net/people/33970)**
2024-08-08 11:14

厉害

* [0 条评论](#comment-2055)
* 0

请先 [登录](https://forum.butian.net/login) 后评论

请先 [登录](https://forum.butian.net/login) 后评论

[![n3ewlit](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/b3418eb089d4603468282f985b8a59a1a1272a4.png)](https://forum.butian.net/people/24985)

[n3ewlit](https://forum.butian.net/people/24985)

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

#### ![n3ewlit](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/b3418eb089d4603468282f985b8a59a1a1272a4.png)

如果觉得我的文章对您有用，请随意打赏。你的支持将鼓励我继续创作！

![]()

---