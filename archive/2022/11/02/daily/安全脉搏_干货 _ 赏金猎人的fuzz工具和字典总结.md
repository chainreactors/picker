---
title: 干货 | 赏金猎人的fuzz工具和字典总结
url: https://www.secpulse.com/archives/190198.html
source: 安全脉搏
date: 2022-11-02
fetch_date: 2025-10-03T21:30:56.367342
---

# 干货 | 赏金猎人的fuzz工具和字典总结

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

# 干货 | 赏金猎人的fuzz工具和字典总结

[工具](https://www.secpulse.com/archives/category/tools)

[HACK\_Learn](https://www.secpulse.com/newpage/author?author_id=8971)
![]( https://www.secpulse.com/wp-content/themes/secpulse2017/img/renzheng0.png)

2022-11-01

14,755

# 赏金猎人的fuzz工具和字典总结

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-190198-1667286431.jpeg)

通过手动输入输入来测试漏洞可能会麻烦。

在当今人们时间和耐心水平较低的时代，手动提供输入以查找目标中的错误/漏洞的想法可能会让人不知所措。

为了减少这个压倒性的问题并节省时间，模糊测试可能是一个很大的优势。

Fuzzing 是一个自动化过程，其中所有繁重的工作都由 fuzzing 工具处理。分析师所要做的就是查看流程完成后的响应、时间和状态代码。

考虑一个有许多输入字段来测试 XSS 的站点。在手动方法中，我们所做的只是将 XSS payload一个一个地提供给输入字段，这太麻烦了。

Fuzzing是在一定的时间间隔内向目标网站发送多个请求的过程或技术。换句话说，它也类似于暴力破解。

Fuzzing 是一个可以使用 Wfuzz、ffuf 等工具来实现的过程。你需要为工具提供目标 URL、参数、端点等以及某种输入。

然后 fuzzing 工具制作请求并将它们一个接一个地发送到目标。模糊测试完成后，需要分析响应、时间和状态代码是否存在漏洞。

# 用于模糊测试的工具

业内有数百种工具可用于进行模糊测试。下面列出了一些评价最高的流行模糊测试工具。

# Wfuzz

Wfuzz通过将占位符 `FUZZ` 替换为 wordlist 值来工作。为了更清楚地理解这一点，让我们考虑一个例子：

```
$ wfuzz -w userIDs.txt https://example.com/view_photo?userId=FUZZ
```

在上面的命令中，`userIds.txt` 是一个包含数字 ID 值的 worldlist 文件。在这里，我们告诉 wfuzz 对示例 URL 的请求进行模糊测试。请注意 URL 中的 FUZZ 单词，它将充当 wfuzz 的占位符，以替换单词列表中的值。将插入 `userIDs.txt` 文件的所有数字 ID 值，替换 `FUZZ` 关键字。

# Ffuf

Ffuf是一个用 Go 语言编写的网络模糊测试工具，本质上是非常快速和递归的。它的工作方式类似于 Wfuzz，但相比之下它是递归的。Ffuf 还可以通过用 worldlist 值替换占位符 `FUZZ` 来工作。例如：

```
$ ffuf -w userIDs.txt -u https://example.com/view_photo?userId=FUZZ
```

这里的 `-w` 是 wordlist 的标志，而 `-u` 是目标 URL 的标志。其余工作机制与Wfuzz相同。它用 `userIDs.txt` 值替换了 `FUZZ` 占位符。

# GoBuster

GoBuster是另一种用 Go 语言编写的模糊器，最常用于模糊 URI、目录/路径、DNS 子域、AWS S3 存储桶、虚拟主机名，并支持并发。例如：

```
$ gobuster dir -w endpoints.txt -u https://example.com
```

在上面的命令中，`dir` 指定我们正在对一个目录进行模糊测试，`-u` 是 URL 的标志，`-w` 是 wordlist 的标志，其中 `endpoints.txt` 是将从中获取有效负载的 worldlist 文件。该命令对端点运行并发请求以查找可用目录。

# Fuzz字典和参考资料

在上面的例子中，我们已经看到了为什么我们需要一个字典。仅字典是不够的，必须非常适合你的 fuzzing 场景。如果你没有找到任何符合必要场景的词表，请考虑生成你自己的字典。下面提供了一些流行的字典和参考资料。

```
(XSS) 备忘单
https://portswigger.net/web-security/cross-site-scripting/cheat-sheet

AwesomeXSS
https://github.com/s0md3v/AwesomeXSS

常用的payload
https://github.com/swisskyrepo/PayloadsAllTheThings

https://github.com/minimaxir/big-list-of-naughty-strings

https://github.com/Bo0oM/fuzz.txt

FuzzDB
https://github.com/fuzzdb-project/fuzzdb

bl4de字典
https://github.com/bl4de/dictionaries

重定向相关payload
https://github.com/cujanovic/Open-Redirect-Payloads

EdOverflow 漏洞赏金备忘单
https://github.com/EdOverflow/bugbounty-cheatsheet

SecLists
https://github.com/danielmiessler/SecLists

XssPayloads
https://twitter.com/XssPayloads

XssPayloads列表
https://github.com/payloadbox/xss-payload-list
```

# Tips

声明一下，并不是每个人都使用模糊测试工具。每个人都有不同的习惯和方法。

使用模糊测试工具不是强制性的。根据你的条件和情况，你可以使用模糊测试工具，这将有利于您节省时间。

模糊测试大量的请求可能会导致您的 IP 地址被目标ban掉，有些人同意手动完成所有工作，而不是使用模糊测试工具。因此，由你手动测试漏洞或让模糊测试工具自动为你完成。

**![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-190198-1667286431.png)**

**本文作者：[HACK\_Learn](newpage/author?author_id=8971)**

**本文为安全脉搏专栏作者发布，转载请注明：**[**https://www.secpulse.com/archives/190198.html**](https://www.secpulse.com/archives/190198.html)

Tags: [Ffuf](https://www.secpulse.com/archives/tag/ffuf)、[FUZZ工具](https://www.secpulse.com/archives/tag/fuzz%E5%B7%A5%E5%85%B7)、[gobuster](https://www.secpulse.com/archives/tag/gobuster)、[Wfuzz](https://www.secpulse.com/archives/tag/wfuzz)、[字典总结](https://www.secpulse.com/archives/tag/%E5%AD%97%E5%85%B8%E6%80%BB%E7%BB%93)、[模糊测试](https://www.secpulse.com/archives/tag/%E6%A8%A1%E7%B3%8A%E6%B5%8B%E8%AF%95)

点赞：
0
[评论：0](#goComment)
收藏：
0

*新浪微博
QQ空间
微信扫一扫*

### 相关文章

* [![资产发现之垂直关联](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-199499-1682316427-300x173.png)

  资产发现之垂直关联](https://www.secpulse.com/archives/199499.html "详细阅读 资产发现之垂直关联")
* [![一个文件上传漏洞靶场](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-196724-1677477148-300x253.png)

  一个文件上传漏洞靶场](https://www.secpulse.com/archives/196724.html "详细阅读 一个文件上传漏洞靶场")
* [![AFL源码浅析](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/2022/10/1666752458070-300x204.png)

  AFL源码浅析](https://www.secpulse.com/archives/189852.html "详细阅读 AFL源码浅析")

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

#### 2021-05-27

[The 2nd AutoCS 2021智能汽车信息安全大会](https://artisan-event.com/AutoCS2021/)

#### 2020-12-18

[贝壳找房2020 ICS安全技术峰会](https://www.4hou.com/tickets/bmZO)

#### 2020-12-11

[全球敏捷运维峰会（Gdevops2020）](https://www.bagevent.com/event/6243820?bag_track=AQMB)

#### 2020-12-04

[2020京麒网络安全大会](htt...