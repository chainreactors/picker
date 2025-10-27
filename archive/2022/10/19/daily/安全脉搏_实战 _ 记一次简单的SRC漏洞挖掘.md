---
title: 实战 | 记一次简单的SRC漏洞挖掘
url: https://www.secpulse.com/archives/189303.html
source: 安全脉搏
date: 2022-10-19
fetch_date: 2025-10-03T20:13:03.481424
---

# 实战 | 记一次简单的SRC漏洞挖掘

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

# 实战 | 记一次简单的SRC漏洞挖掘

[脉搏文库](https://www.secpulse.com/archives/category/category/secdocs)

[HACK\_Learn](https://www.secpulse.com/newpage/author?author_id=8971)
![]( https://www.secpulse.com/wp-content/themes/secpulse2017/img/renzheng0.png)

2022-10-18

10,493

## 一.起

开局一个登录框，简单测试了几个弱口令无果后

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-189303-1666071667.png)

注意力转到找回密码处

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-189303-1666071669.png)

先输入两个非法的参数

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-189303-16660716691.png)

点击获取验证码，抓包，查看响应代码返回0，前端显示未查询到账户信息

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-189303-1666071670.png)

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-189303-1666071671.png)

再来一次，抓包并修改响应包，将0改为1，放包后成功来到第二步，前端自动请求了一个后端接口发送验证码

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-189303-1666071672.png)

查看该接口的响应，发现验证码作为响应体被返回了

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-189303-1666071674.png)

填入验证码，直接跳转到第三步修改新密码，填入新密码后，点击提交

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-189303-1666071675.png)

发现请求体里只有userIds和password两个参数，前者是要修改密码用户的uid，后者是新密码的值，猜测这里可能存在任意账户密码重置，而后又意识到我们传入的用户不存在，所以前端存储的userid变量为0，于是我们将请求包中userIds字段修改为1，尝试重置管理员密码。
后端响应为1，证明密码重置成功了，走到这里只觉喜出望外，赶紧拿着新密码去登录管理员账户

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-189303-1666071676.png)

结果

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-189303-16660716761.png)

想不通，难道是管理员的账户名不是admin？接连试了几个常见管理员用户名都失败后，想到还有个注册点，兴许可以爆破出管理员账号呢？
结果还是不行：

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-189303-1666071677.png)

## 二.承

无奈，此路不通另寻他路，注意到有个APP下载的二维码，解析之，而后下载到apk

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-189303-16660716771.png)

用工具快速扫描一下，发现两个移动端的接口地址有点不同寻常

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-189303-1666071678.png)

访问之，好家伙，竟然返回了所有用户的uid和电话号码

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-189303-16660716781.png)

## 三.转

惊喜之余突然回过神来，马上到接口中去检索uid为1的用户

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-189303-1666071679.png)

结果证明uid=1的用户不是管理员权限，而是一个普普通通的员工id，之前由于太过笃定管理员的uid就是1，导致我们在这个点上浪费了太多时间。

## 四.合

随后也是通过这个未授权的接口找到了管理员的id

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-189303-16660716791.png)

但是为了不对业务系统造成严重破坏，我们仅重置了一个普通用户的密码，随后成功登录以验证漏洞的存在：

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-189303-1666071680.png)

工具地址：

```
https://github.com/kelvinBen/AppInfoScanner
```

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-189303-16660716801.png)

作者：Alpaca

原文地址：https://xz.aliyun.com/t/11757

如有侵权，请联系删除

**本文作者：[HACK\_Learn](newpage/author?author_id=8971)**

**本文为安全脉搏专栏作者发布，转载请注明：**[**https://www.secpulse.com/archives/189303.html**](https://www.secpulse.com/archives/189303.html)

Tags: [src漏洞](https://www.secpulse.com/archives/tag/src%E6%BC%8F%E6%B4%9E)、[抓包](https://www.secpulse.com/archives/tag/%E6%8A%93%E5%8C%85)、[漏洞挖掘](https://www.secpulse.com/archives/tag/%E6%BC%8F%E6%B4%9E%E6%8C%96%E6%8E%98)

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
* [![记一次springboot项目漏洞挖掘](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-200022-1683537351-300x173.png)

  记一次springboot项目漏洞挖掘](https://www.secpulse.com/archives/200022.html "详细阅读 记一次springboot项目漏洞挖掘")

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
| [![]( https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1ca91da9312f04fadf4ab539bb3cb881.png)](https://www.secpulse.com/newpage/author?author_id=8971aaa) | [HACK\_Learn ![]( https://www.secpulse.com/wp-content/themes/secpulse2017/img/renzheng0.png)](https://www.secpulse.com/newpage/author?author_id=8971) | |
| 文章数：142 | 积分： 323 |
| 微信公众号：HACK学习呀 | |

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

#### 202...