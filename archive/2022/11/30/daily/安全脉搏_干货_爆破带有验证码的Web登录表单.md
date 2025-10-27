---
title: 干货|爆破带有验证码的Web登录表单
url: https://www.secpulse.com/archives/192531.html
source: 安全脉搏
date: 2022-11-30
fetch_date: 2025-10-04T00:03:39.832865
---

# 干货|爆破带有验证码的Web登录表单

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

# 干货|爆破带有验证码的Web登录表单

[资讯](https://www.secpulse.com/archives/category/news)

[hackctf](https://www.secpulse.com/newpage/author?author_id=34005)

2022-11-29

10,452

> 转载于ybdt.me博客

**吐槽**

逛github看到一个项目，讲述如何爆破带有验证码的Web登录表单，作者是基于c0ny1师傅的captcha-killer项目修改了一下，过程叙述稍微有点简陋，自己折腾了好一会，想了想还是记录一下使用过程，方便自己也方便他人（耗时约3小时）

连续2篇图文记录真是太累人了，以后还是多文字描述吧。。

本文定位教程类文章，共包括step1-step5

# **step1-安装插件**

下载并安装插件
下载地址：https://github.com/f0ng/captcha-killer-modified/releases

# **step2-插件获取图片验证码**

burp抓包会发现某个请求是获取图片验证码的，将这个请求发送到插件中的captcha panel

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-192531-1669701541.png)

点击captcha-killer-modified界面中的获取，发现可以正常获取验证码

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-192531-1669701546.png)

# **step3-本地启动验证码识别接口**

此处我们使用github上的一个开源验证码识别项目，没有次数限制，识别率在80%左右

```
pip3.exe install ddddocr

python3.exe .codereg.py
```

codereg.py位于：https://github.com/ybdt/dict-hub/blob/master/2022\_03\_22\_%E7%88%86%E7%A0%B4%E5%B8%A6%E6%9C%89%E9%AA%8C%E8%AF%81%E7%A0%81%E7%9A%84Web%E7%99%BB%E5%BD%95%E8%A1%A8%E5%8D%95/codereg.py

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-192531-1669701548.png)

# **step4-识别验证码**

点击captcha-killer-modified界面，接口URL填上步中启动后的监听地址

```
http://127.0.0.1:8888
```

请求模板填如下

|  |  |
| --- | --- |
| ``` POST /reg HTTP/1.1Host: 127.0.0.1:8888Connection: closeCache-Control: max-age=0Upgrade-Insecure-Requests: 1User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36Sec-Fetch-Mode: navigateSec-Fetch-User: ?1Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3Sec-Fetch-Site: noneAccept-Encoding: gzip, deflateAccept-Language: zh-CN,zh;q=0.9Content-Type: application/x-www-form-urlencodedContent-Length: 55 <@BASE64><@IMG_RAW></@IMG_RAW></@BASE64> ``` | ```  ``` |

点击识别，可以看到能够识别到验证码

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-192531-16697015481.png)

点击锁定

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-192531-1669701550.png)

**step5-暴力破解**

burp拦截登录数据包

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-192531-1669701560.png)

发送到intruder，选择Pitchfork

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-192531-1669701567.png)

payload1正常选择字典，payload2选择如下

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-192531-1669701570.png)

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-192531-1669701573.png)

线程选择1，发送延时为500ms

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-192531-1669701577.png)

可看到能够成功爆破带有验证码的Web表单，识别率在80%左右

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-192531-1669701581.png)

# **参考链接**

https://mp.weixin.qq.com/s/\_P6OlL1xQaYSY1bvZJL4Uw
https://github.com/f0ng/captcha-killer-modified
https://github.com/c0ny1/captcha-killer
https://gv7.me/articles/2019/burp-captcha-killer-usage/
https://github.com/sml2h3/ddddocr

文章转自https://ybdt.me/

**本文作者：[hackctf](newpage/author?author_id=34005)**

**本文为安全脉搏专栏作者发布，转载请注明：**[**https://www.secpulse.com/archives/192531.html**](https://www.secpulse.com/archives/192531.html)

Tags: [Burp](https://www.secpulse.com/archives/tag/Burp)、[Web登录表单](https://www.secpulse.com/archives/tag/web%E7%99%BB%E5%BD%95%E8%A1%A8%E5%8D%95)、[抓包](https://www.secpulse.com/archives/tag/%E6%8A%93%E5%8C%85)、[爆破](https://www.secpulse.com/archives/tag/%E7%88%86%E7%A0%B4)

点赞：
4
[评论：0](#goComment)
收藏：
0

*新浪微博
QQ空间
微信扫一扫*

### 相关文章

* [![实战|记一次校内站点的渗透测试](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/2023/05/1684822359737-300x175.png)

  实战|记一次校内站点的渗透测试](https://www.secpulse.com/archives/200867.html "详细阅读 实战|记一次校内站点的渗透测试")
* [![实战 | 记一次X站逻辑漏洞到到管理员后台](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/2023/05/1684478703453-300x241.png)

  实战 | 记一次X站逻辑漏洞到到管理员后…](https://www.secpulse.com/archives/200723.html "详细阅读 实战 | 记一次X站逻辑漏洞到到管理员后台")
* [![MySQL数据库安全测试](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/2023/05/1684133717094-300x188.png)

  MySQL数据库安全测试](https://www.secpulse.com/archives/200243.html "详细阅读 MySQL数据库安全测试")

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
| [![]( https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/2020/06/04/6bfc834beda6e9debb9f6b48a215b4bc-290x290.jpeg)](https://www.secpulse.com/newpage/author?author_id=34005aaa) | [hackctf](https://www.secpulse.com/newpage/author?author_id=34005) | |
| 文章数：40 | 积分： 80 |
| 微信公众号：hackctf | |

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

[2021中国国际网络安全博览会暨高峰论坛](http...