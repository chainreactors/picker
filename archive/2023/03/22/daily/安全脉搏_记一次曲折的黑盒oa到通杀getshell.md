---
title: 记一次曲折的黑盒oa到通杀getshell
url: https://www.secpulse.com/archives/198028.html
source: 安全脉搏
date: 2023-03-22
fetch_date: 2025-10-04T10:14:23.214838
---

# 记一次曲折的黑盒oa到通杀getshell

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

# 记一次曲折的黑盒oa到通杀getshell

[Web安全](https://www.secpulse.com/archives/category/articles/web)

[潇湘信安](https://www.secpulse.com/newpage/author?author_id=37983)
![]( https://www.secpulse.com/wp-content/themes/secpulse2017/img/renzheng3.png)

2023-03-21

11,986

|  |
| --- |
| **声明：**该公众号大部分文章来自作者日常学习笔记，也有部分文章是经过作者授权和其他公众号白名单转载，未经授权，严禁转载，如需转载，联系开白。  请勿利用文章内的相关技术从事非法测试，如因此产生的一切不良后果与文章作者和本公众号无关。 |

周末闲来没事干，分享下周末挖的一个垃圾0day

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-198028-1679388265.png)

直接弱口令进去

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-198028-1679388266.png)

目的明确，找找上传点

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-198028-1679388269.png)

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-198028-1679388272.png)

原来是小黑子（黑名单）

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-198028-1679388276.png)

直接jspx上传看看

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-198028-1679388278.png)

上传成功，但你到是给我返回路径啊，复制上面的看看

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-198028-1679388280.png)

我干，直接下载出来了，直接f12看看找找jpg路径

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-198028-1679388281.png)

发现还是有相同时间命名的文件，Fuzz路径看看，应该2015是时间，logo是上传参数，最后是时间命名文件

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-198028-1679388282.png)

全是400

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-198028-1679388283.png)

真是多看一眼就爆炸，再近一点靠近点快被融化

再找找别的图片路径看看有没有发现，翻着翻着看见一个小喇叭，出于好奇点开看看

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-198028-1679388284.png)

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-198028-16793882841.png)

点开看看，开启f12大法

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-198028-1679388285.png)

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-198028-1679388286.png)

突然这个时候想到，找个人设置瞅瞅，说出来不怕笑话，找个人设置找了半小时，Tm的藏这么深

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-198028-1679388288.png)

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-198028-16793882881.png)

你大爷的

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-198028-1679388289.png)

不急，咱们获取下路径就行，上传jpg看看（上传的照片是他之前的）

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-198028-1679388291.png)

然后拼接看看

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-198028-1679388293.png)

可行，我以为前段只是js校验的时候是我想多了。

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-198028-1679388296.png)

啥也不返回，然后我对比前面上传的包，一个path参数=cooperate，一个是=peopleinfo，原来path参数就是文件夹命名

那还说啥，直接拼接下机

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-198028-1679388300.png)

我真的会谢，我以为是我搞错的时候，上传个txt看看

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-198028-1679388302.png)

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-198028-1679388304.png)

没毛病啊，难道是这个目录不解析jspx

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-198028-1679388305.png)

根目录是解析jspx的，所以尝试下path参数跨目录

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-198028-1679388306.png)

报500,不支持跨目录？，尝试下用/

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-198028-1679388310.png)

上传成功

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-198028-1679388313.png)

也不行，上传txt确可以跨了个目录

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-198028-1679388314.png)

也试了编码这些，正当准备提桶跑路的时候，想到../不行试下..

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-198028-1679388315.png)

梭哈的艺术

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-198028-1679388318.png)

正当准备复制连接的时候，不小心点快了，吧页面删了，直接重新传个命令马

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-198028-1679388319.png)

愉快的周末，现在终于能下机了

```
文章来源：先知社区（呱呱yyy啊）
原文地址：https://xz.aliyun.com/t/12282
```

**本文作者：[潇湘信安](newpage/author?author_id=37983)**

**本文为安全脉搏专栏作者发布，转载请注明：**[**https://www.secpulse.com/archives/198028.html**](https://www.secpulse.com/archives/198028.html)

Tags: [0day](https://www.secpulse.com/archives/tag/0day)、[Fuzz](https://www.secpulse.com/archives/tag/fuzz)、[jspx](https://www.secpulse.com/archives/tag/jspx)、[path参数](https://www.secpulse.com/archives/tag/path%E5%8F%82%E6%95%B0)、[弱口令](https://www.secpulse.com/archives/tag/%E5%BC%B1%E5%8F%A3%E4%BB%A4)、[黑盒](https://www.secpulse.com/archives/tag/%E9%BB%91%E7%9B%92)

点赞：
1
[评论：0](#goComment)
收藏：
0

*新浪微博
QQ空间
微信扫一扫*

### 相关文章

* [![某应用虚拟化系统远程代码执行](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-199708-1682584786-300x200.png)

  某应用虚拟化系统远程代码执行](https://www.secpulse.com/archives/199708.html "详细阅读 某应用虚拟化系统远程代码执行")
* [![实战|记两起挖矿木马排查](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-199667-1682566759-300x156.png)

  实战|记两起挖矿木马排查](https:/...