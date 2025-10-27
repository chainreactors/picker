---
title: HW 中如何利用 WAF 缺陷进行绕过
url: https://forum.butian.net/share/3639
source: 奇安信攻防社区
date: 2024-07-27
fetch_date: 2025-10-06T17:38:27.559285
---

# HW 中如何利用 WAF 缺陷进行绕过

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

### HW 中如何利用 WAF 缺陷进行绕过

* [渗透测试](https://forum.butian.net/topic/47)

在挖洞过程中，往往会遇到各种攻击利用被waf拦截的情况，本文浅析总结了常见的一些绕过思路以及具体实现

浅析waf绕过
=======
在挖洞过程中，往往会遇到各种攻击利用被waf拦截的情况，本文浅析总结了常见的一些绕过思路以及具体实现
利用waf的缺陷绕过
----------
#### 1.1利用waf性能缺陷-垃圾字符填充
对于通用性较强的软WAF来说，不得不考虑到各种机器和系统的性能，故对于一些超大数据包、超长数据可能会跳过不检测
因此可以填充大量垃圾字符来逃避waf对数据包的检测如下
![image-20240526154113932](https://oss-yg-cztt.yun.qianxin.com/butian-public/f150172a1e6cbec89f2dc5fd4dc5bf7f404757b2f85bd.jpg)
![image-20240526154349390](https://oss-yg-cztt.yun.qianxin.com/butian-public/f9057463b4bd7e81f6cb050db6a2c1174c4f33c556f77.jpg)
#### 1.2利用waf性能缺陷-发送大量请求包
可以采取高并发的攻击手段，waf同样出于性能考虑可能会直接放行部分数据包。
### 2.利用waf适配组件的缺陷
由于后端web容器、中间件、数据库、脚本语言的多样性，waf很难覆盖全，容易导致waf解析不了而后端可以正常解析读取导致的绕过
##### IIS+asp
在IIS+ASP的环境中，如果url中出现了百分号，但后面邻接的字符拼起来后又不在url编码表之内的话，ASP脚本处理时会将其忽略
例如假设有如下请求xxx.asp?id=1 union se%lect 1,2,3,4 fro%m adm%in
waf规则不严放行后，后端由于该特性成功处理执行了xxx.asp?id=1 union select 1,2,3,4 from admin导致绕过
##### TOMCAT
tomcat的特性也可以构造出许多绕过的方式，可以参考https://y4tacker.github.io/2022/06/19/year/2022/6/%E6%8E%A2%E5%AF%BBTomcat%E6%96%87%E4%BB%B6%E4%B8%8A%E4%BC%A0%E6%B5%81%E9%87%8F%E5%B1%82%E9%9D%A2%E7%BB%95waf%E6%96%B0%E5%A7%BF%E5%8A%BF/这篇文章
1.参数前后添加空白字符绕过
`filename="1.jsp"`的filename字符左右可以加上一些空白字符`%20 %09 %0a %0b %0c %0d %1c %1d %1e %1f`，比如`%20filename%0a="1.jsp"`这样导致waf匹配不到我们上传⽂件
2.utf-16、cp037等各种编码绕过
utf-16
![image-20240526170229544](https://oss-yg-cztt.yun.qianxin.com/butian-public/f540634c7b31344476ba545be386ce8320137a04cfe61.jpg)
cp037（原始payload为' and (7=len(db\\_name())) and 'a' = 'a）
![image-20240526165744271](https://oss-yg-cztt.yun.qianxin.com/butian-public/f98547866797cf9b081ca4dd0d25f95d8d4413ad7caef.jpg)
##### json下的unicode编码
![image-20240526173506645](https://oss-yg-cztt.yun.qianxin.com/butian-public/f2971352b4b74bcd51a8d9f311019a17483c6924aea44.jpg)
### 3.利用waf适配协议的缺陷
##### 3.1畸形请求（与Web应用所处的中间件有关，在部分中间件下不适用）
将HTTP请求头变为随机字符串例如\*\*xxxxT\*\*
![image-20240526171614450](https://oss-yg-cztt.yun.qianxin.com/butian-public/f78430671e32968ca3123950b60895178a40b20f71798.jpg)
请求方法后加一个table等空字符
![image-20240526172126984](https://oss-yg-cztt.yun.qianxin.com/butian-public/f8560208146f9320d62eddb35ffdd07a008facb234cff.jpg)
使用get请求方法但带上post体（需要服务端能正常接受）
![image-20240624152546175](https://oss-yg-cztt.yun.qianxin.com/butian-public/f1856403689e8ea779d3cd433954cf749977b7596c992.jpg)
##### 3.2分块传输
仅仅适用于post传输方法
![image-20240526172521876](https://oss-yg-cztt.yun.qianxin.com/butian-public/f6118296d5cc73cf836ce5e2eb04176077824551badb6.jpg)
分块传输不少waf现在也都可以识别了，可以结合waf性能缺陷的思路综合利用-\*\*延时分块传输\*\*
具体使用可以参考该项目 <http://github.com/c0ny1/chunked-coding-converter>
![image-20240624152546175](https://oss-yg-cztt.yun.qianxin.com/butian-public/f1856403689e8ea779d3cd433954cf749977b7596c992.jpg)
##### 3.3非预期请求方式
get改为post、Content-Type: application/x-www-form-urlencoded改为multipart/form-data等
跳过waf直接访问服务器
------------
### 寻找真实ip绕过云waf
云waf通过配置NS或者CNAME记录，使得对网站的请求报文优先经过WAF主机，经过WAF主机过滤之后，将被认为无害的请求报文再送给实际的网站服务器进行请求,此时只要找到服务器的真实ip,修改host为服务器真是ip即可绕过云waf
常见寻找真实ip的方式有如下几种
1.证书信息查询 <https://myssl.com/>
2.dns历史解析记录
3.搜集子域名ip c段(考虑到费用问题，一些子域名并不会部署)
4.超级ping
......
### 寻找没有部署waf的nginx反代机器
当waf在nginx服务器上部署，且存在nginx集群时，可以试试尝试寻找能反代服务却又没用部署waf的机器访问进行绕过
以下面这个为例，测试某接口发现被拦截
![image-20240526175155960](https://oss-yg-cztt.yun.qianxin.com/butian-public/f34706506274374aa48d48ef2682e07eeaceee63939b5.jpg)
搜集ip信息为xxx.xxx.200.1xx
![image-20240526175323108](https://oss-yg-cztt.yun.qianxin.com/butian-public/f594909448d221b5f03fea5e94d807f464d60045d7a2d.jpg)
查找c段服务，一个个访问尝试
![image-20240526175455156](https://oss-yg-cztt.yun.qianxin.com/butian-public/f754634bdfae2033de6bcb19e9a1f4cc3bc80ca53f2f5.jpg)
利用成功
![image-20240526175618342](https://oss-yg-cztt.yun.qianxin.com/butian-public/f951797199d8b6a691977127c21498fb5f1fc9fa0fb6b.jpg)
### 利用waf白名单
WAF存在某些机制，不处理和拦截白名单中的请求数据
例如特定的ip,来自于搜索引擎爬虫的访问数据等
特定ip
可以使用https://github.com/TheKingOfDuck/burpFakeIP插件将xff等头部设置为127.0.0.1等进行绕过尝试
![image-20240526180922628](https://oss-yg-cztt.yun.qianxin.com/butian-public/f159457bfdd55ee5d8c120a3e6822d90b6ddf8a7cc82f.jpg)
搜索引擎爬虫的访问数据
User-Agent修改为谷歌搜索引擎等

* 发表于 2024-07-26 10:00:02
* 阅读 ( 34486 )
* 分类：[漏洞分析](https://forum.butian.net/community/Vul_analysis)

7 推荐
 收藏

## 1 条评论

[![](https://forum.butian.net/static/images/default_avatar.jpg)](https://forum.butian.net/people/7409)

**[ybdt](https://forum.butian.net/people/7409)**
2024-07-28 12:07

不错~

* [0 条评论](#comment-2035)
* 1

请先 [登录](https://forum.butian.net/login) 后评论

请先 [登录](https://forum.butian.net/login) 后评论

[![中铁13层打工人](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/bd481171367dd9c7aac272bf517c972393f08b4.jpg)](https://forum.butian.net/people/77)

[中铁13层打工人](https://forum.butian.net/people/77)

79 篇文章

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

#### ![中铁13层打工人](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/bd481171367dd9c7aac272bf517c972393f08b4.jpg)

如果觉得我的文章对您有用，请随意打赏。你的支持将鼓励我继续创作！

![]()

---