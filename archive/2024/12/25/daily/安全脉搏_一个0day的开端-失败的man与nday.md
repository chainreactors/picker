---
title: 一个0day的开端-失败的man与nday
url: https://www.secpulse.com/archives/205498.html
source: 安全脉搏
date: 2024-12-25
fetch_date: 2025-10-06T19:36:04.438173
---

# 一个0day的开端-失败的man与nday

[![](https://www.secpulse.com/wp-content/themes/secpulse2017/img/logo-header.png)](https://www.secpulse.com "安全脉搏")

* [首页](https://www.secpulse.com/)
* [分类阅读](https://www.secpulse.com/archives/category/category)

  #### 脉搏文库

  - [内网渗透](https://www.secpulse.com/archives/category/articles/intranet-penetration)
  - |
  - [代码审计](https://www.secpulse.com/archives/category/articles/code-audit)
  - |
  - [安全文献](https://www.secpulse.com/archives/category/articles/sec-doc)
  - |
  - [Web安全](https://www.secpulse.com/archives/category/articles/web)
  - |
  - [移动安全](https://www.secpulse.com/archives/category/articles/mobile-security)
  - |
  - [系统安全](https://www.secpulse.com/archives/category/articles/system)
  - |
  - [工控安全](https://www.secpulse.com/archives/category/articles/industrial-safety)
  - |
  - [CTF](https://www.secpulse.com/archives/category/exclusive/ctf-writeup)
  - |
  - [IOT安全](https://www.secpulse.com/archives/category/iot-security)
  - |

#### 安全建设

+ [业务安全](https://www.secpulse.com/archives/category/construction/businesssecurity)
+ |
+ [安全管理](https://www.secpulse.com/archives/category/construction/securityissue)
+ |
+ [数据分析](https://www.secpulse.com/archives/category/construction/bigdata)
+ |

#### 其他

+ [资讯](https://www.secpulse.com/archives/category/news)
+ |
+ [漏洞](https://www.secpulse.com/archives/category/vul)
+ |
+ [工具](https://www.secpulse.com/archives/category/tools)
+ |
+ [人物志](https://www.secpulse.com/archives/category/people)
+ |
+ [区块链安全](https://www.secpulse.com/archives/category/exclusive/block_chain_security)
+ |
+ [安全招聘](https://www.secpulse.com/archives/category/hiring)
+ |

- [安全问答](https://www.secpulse.com/newpage/question_list)
- [金币商城](https://www.secpulse.com/shop?donotcachepage=c010349fd98847cb9d6e07d3cbc19288)
- [安全招聘](https://www.secpulse.com/archives/category/hiring)
- [活动日程](https://www.secpulse.com/newpage/activity)
- [live课程](https://www.secpulse.com/live)
- [企业服务](https://duoyinsu.com/service.html)
- [插件社区](https://x.secpulse.com/)

小程序

![脉搏小程序](https://www.secpulse.com/wp-content/themes/secpulse2017/img/wxchat.jpg)
[登录](https://www.secpulse.com/user_login)
|
[注册](https://www.secpulse.com/user-register)

# 一个0day的开端-失败的man与nday

[漏洞](https://www.secpulse.com/archives/category/vul)

[蚁景网安实验室](https://www.secpulse.com/newpage/author?author_id=37244)
![]( https://www.secpulse.com/wp-content/themes/secpulse2017/img/renzheng2.png)

2024-12-24

8,169

最近在审计java的CMS，跟着文章进行nday审计，找准目标newbee-mall Version1.0.0（新蜂商城系统），并跟着网上文章进行审计：

<https://blog.csdn.net/m0_46317063/article/details/131538307>

![](https://m-1254331109.cos.ap-guangzhou.myqcloud.com/202410101641859.png)

下载唯一的版本，且源码README中版本也对的上，但没想到nday全部复现失败，但在一番审计后找到了一个新的漏洞点：ssrf，且在前台可以被用户触发。

失败的man与nday：

失败的sql注入漏洞：

（此漏洞原本可以在前台与后台进行sql注入攻击）

分析文章中有两sql注入漏洞，是由于引入mybatis依赖导致，但在我下的版本中根据关键字符${找不到任何的注入点，经过与分析文章对比发现所有注入点全部由${改成了#{由此完成修复。

![](https://m-1254331109.cos.ap-guangzhou.myqcloud.com/202410101641860.png)

失败的权限绕过：

（此漏洞原本可以在admin登录后台通过/;/admin/test完成权限绕过）

复现文章写到以request.getRequestURI()获取路径获取路径后再进入if判断：

![](https://m-1254331109.cos.ap-guangzhou.myqcloud.com/202410101641862.png)

但我下载的版本进行了修复：将获取前端传输的路径方法改为了：getServletPath()从而完成修复。

两种方法的不同具体分析可以参考如下文章：

<https://forum.butian.net/share/3730>

失败的越权漏洞：

（此漏洞原本可以根据传入的id参数越权修改他人信息。）

定位到具体代码：

![](https://m-1254331109.cos.ap-guangzhou.myqcloud.com/202410101641863.png)

此处代码与复现文章一样，都是先创建一个NewBeeMallUserVO对象，再通过是否为空判断信息修改是否成功。

真正修改信息的代码在updateUserInfo方法里面，于是跟进该方法实现处：

![屏幕截图 2024-09-18<br />222508](https://m-1254331109.cos.ap-guangzhou.myqcloud.com/202410101641864.png)

![](https://m-1254331109.cos.ap-guangzhou.myqcloud.com/202410101641865.png)

发现跟到了接口，于是我们继续跟进，找该接口的实现类：

![](https://m-1254331109.cos.ap-guangzhou.myqcloud.com/202410101641866.png)

跟进到如下类，找到具体实现的代码块：

![](https://m-1254331109.cos.ap-guangzhou.myqcloud.com/202410101641867.png)

复现文章代码在进入if判断前只有一行代码，并且代码逻辑是从前端传入的id值进行信息修改，但可以看到我下载的代码有两行：

NewBeeMallUserVO userTemp = (NewBeeMallUserVO)httpSession.getAttribute(Constants.MALL\_USER\_SESSION\_KEY);

首先通过http.Session获取当前用户，再赋给创建的userTemp对象。

MallUser userFromDB =mallUserMapper.selectByPrimaryKey(userTemp.getUserId());

再从userTemp对象中获取id值进行信息修改，而非从前端请求中获取参数id的值，来完成漏洞修复。

0day的发现：

登录后台，点击修改或者添加商品：

![屏幕截图 2024-09-18<br />204816](https://m-1254331109.cos.ap-guangzhou.myqcloud.com/202410101641868.png)

随意传入图片后点击保存并抓包。

![屏幕截图 2024-09-18<br />204915](https://m-1254331109.cos.ap-guangzhou.myqcloud.com/202410101641869.png)

将POST数据包如上两个参数修改为dnslog地址，放包，在商城前台搜索该商品名称。

![屏幕截图 2024-09-18<br />204953](https://m-1254331109.cos.ap-guangzhou.myqcloud.com/202410101641871.png)

点击访问，dns平台出现记录。

![屏幕截图 2024-09-18<br />205059](https://m-1254331109.cos.ap-guangzhou.myqcloud.com/202410101641872.png)

漏洞代码分析：

先看看商品信息存储过程：

根据接口定位代码块：

![](https://m-1254331109.cos.ap-guangzhou.myqcloud.com/202410101641873.png)

可以发现在接受参数后进行是否为空判断后进入了核心方法updateNewBeeMallGoods，跟进：

![](https://m-1254331109.cos.ap-guangzhou.myqcloud.com/202410101641874.png)

跟到接口后再找到接口实现类，最后定位到更新信息代码块。

可以看到，仅仅对传入参数值进行为空判断和相同判断后，便调用set方法进行存储。

接下来再看看商品信息调用代码链。

根据触发漏洞的数据包接口定位代码块：

![](https://m-1254331109.cos.ap-guangzhou.myqcloud.com/202410101641875.png)

此处代码根据传入goodsid参数，将商品渲染到前端，也就是搜索商品后，见到商品那刻触发漏洞。

对接受goodsid参数是否<1判断后进入取商品信息代码。

跟进getNewBeeMallGoodsById方法，找到方法接口后再找接口实现类，再找方法：

![](https://m-1254331109.cos.ap-guangzhou.myqcloud.com/202410101641876.png)

发现goodsid参数传入selectByPrimaryKey方法。

![](https://m-1254331109.cos.ap-guangzhou.myqcloud.com/202410101641877.png)

该方法通过数据访问对象（DAO）goodMapper调用，且在方法最前处由NewBeeMallGoodsMapper对其定义：

![屏幕截图 2024-09-18<br />225627](https://m-1254331109.cos.ap-guangzhou.myqcloud.com/202410101641877.png)

全局搜索，找到对应xml文件：

![](https://m-1254331109.cos.ap-guangzhou.myqcloud.com/202410101641878.png)

发现通过id参数对数据库操作，取出goodsCoverImg与goodsCarousel参数。

回到最先前的类：

![](https://m-1254331109.cos.ap-guangzhou.myqcloud.com/202410101641879.png)

此时goods对象已经获取商品相关参数值。

再进入if判断商品是否上架，上架则进入下一轮代码，将商品信息封装为视图模型，找到NewBeeMallGoodsDetailVO类，发现只接受了goodsCoverImg参数，也就是先前抓包修改处只用修改该参数即可：

![](https://m-1254331109.cos.ap-guangzhou.myqcloud.com/202410101641880.png)

最后返回视图名称"mall/detail"，表示渲染商品详情页面：

![](https://m-1254331109.cos.ap-guangzhou.myqcloud.com/202410101641881.png)

由于存储时未做任何过滤，进行视图层渲染时直接拿出goodsCoverImg参数放到前端，导致用户一旦访问商品便触发该漏洞。

**本文作者：[蚁景网安实验室](newpage/author?author_id=37244)**

**本文为安全脉搏专栏作者发布，转载请注明：**[**https://www.secpulse.com/archives/205498.html**](https://www.secpulse.com/archives/205498.html)

点赞：
0
[评论：0](#goComment)
收藏：
0

*新浪微博
QQ空间
微信扫一扫*

### 相关文章

* [![Solon框架模板漏洞深度剖析与修复实战](https://www.yijinglab.com/guide-img/d9634e2f-3b66-42e7-8279-c0877cdd70e5/7266edd7-a4cc-444d-bacb-7ee802487ac4.png)

  Solon框架模板漏洞深度剖析与修复实战](https://www.secpulse.com/archives/206316.html "详细阅读 Solon框架模板漏洞深度剖析与修复实战")
* [![路由器安全研究：D-Link DIR-823G v1.02 B05 复现与利用思路](https://m-1254331109.cos.ap-guangzhou.myqcloud.com/202503171628715.png)

  路由器安全研究：D-Link DIR-8](https://www.secpulse.com/archives/206007.html "详细阅读 路由器安全研究：D-Link DIR-823G v1.02 B05 复现与利用思路")
* [![DedeBIZ系统审计小结](https://m-1254331109.cos.ap-guangzhou.myqcloud.com/202502121526395.png)

  DedeBIZ系统审计小结](https://www.secpulse.com/archives/205891.html "详细阅读 DedeBIZ系统审计小结")

评论  (0)

昵称

必填
您当前尚未登录。
[登录？](https://www.secpulse.com/user_login "登录")
[注册](https://www.secpulse.com/user-register)

邮箱

必填（保密）

快来写下你的想法吧！

upload

|  |  |  |
| --- | --- | --- |
| [![]( https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/2024/12/logo-white.png)](https://www.secpulse.com/newpage/author?author_id=37244aaa) | [蚁景网安实验室 ![]( https://www.secpulse.com/wp-content/themes/secpulse2017/img/renzheng2.png)](https://www.secpulse.com/newpage/author?author_id=37244) | |
| 文章数：402 | 积分： 877 |
| 蚁景网安实验室（www.yijinglab.com）网络安全靶场练习平台，涉及CTF赛前指导、职业技能训练、网安专项技能提升等。 | |

* [![阿波罗主机安全管理](/wp-content/themes/secpulse2017/img/product-agent.png)](https://linkage.duoyinsu.com)
* [![伏特漏洞扫描云平台](/wp-content/themes/secpulse2017/img/product-fute.png)](https://v.duoyinsu.com)

### 安全问答社区

![安全问答社区](https://www.secpulse.com/wp-content/themes/secpul...