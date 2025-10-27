---
title: 逆向分析010 editor
url: https://www.secpulse.com/archives/192246.html
source: 安全脉搏
date: 2022-11-26
fetch_date: 2025-10-03T23:48:26.189331
---

# 逆向分析010 editor

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

# 逆向分析010 editor

[工具](https://www.secpulse.com/archives/category/tools)

[TideSec](https://www.secpulse.com/newpage/author?author_id=26366)
![]( https://www.secpulse.com/wp-content/themes/secpulse2017/img/renzheng0.png)

2022-11-25

13,086

# 逆向分析010 editor

## 0x01 什么是010 editor

010 Editor 是一款专业的文本编辑器和十六进制编辑器，旨在快速轻松地编辑计算机上任何文件的内容。该软件可以编辑文本文件，包括 Unicode 文件、批处理文件、C/C++、XML 等，但 010 Editor 擅长的地方在于编辑二进制文件。二进制文件是计算机可读但人类不可读的文件（如果在文本编辑器中打开，二进制文件将显示为乱码）。十六进制编辑器是一个程序，允许您查看和编辑二进制文件的各个字节，包括 010 编辑器在内的高级十六进制编辑器还允许您编辑硬盘驱动器、软盘驱动器、内存密钥、闪存驱动器、CD-ROM、 流程等。

官网地址：https://www.sweetscape.com/010editor/

## 0x02 OD暴力破解

在软件逆向破解的过程中，OD暴力破解是比较有效的方式，通过修改jcc指令或者nop掉一些跳转让程序按照正确的流程走下去。

主要流程大概是：1、寻找关键函数；2、分析整体流程；3、修改程序验证逻辑。

本次测试的010 editor版本为v13.0

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-192246-1669347478.png)

首先查壳

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-192246-1669347483.png)

既然无壳那就直接上OD

首先我们要找到注册的函数，首次下载010 editor可以试用30天，点击注册按钮

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-192246-1669347485.png)

程序会让输入用户名和注册码，随便输入试试

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-192246-1669347489.png)

程序会提示无效的用户名和密码，可以根据程序提示的内容来找到对应的函数

通过OD的中文搜索引擎-智能搜索功能查找对应字符串

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-192246-1669347491.png "null")

找到对应的字符串，跟进函数

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-192246-1669347493.png "null")

跟进后可以看到，程序执行到输出无效的用户名和密码处，是通过一个跳转到该位置的，继续往上跟看看是那个地方跳转

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-192246-1669347496.png "null")

发现是从`0x0144B62A`位置处跳转过来的，这样的话是否可以直接修改jcc执行来让程序不跳转呢

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-192246-1669347498.png)

改成je试下，改成je后发现不对，程序会执行到`0x0144B6C6`的位置，提示 `Password accepted but the trial period is already over`，那么就继续往上跟踪

在跳转前边有三个cmp指令，其中`0x0144B60D`是从`0x0144B4E2` 处跳转来的

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-192246-1669347500.png "null")

在`0x0144B4E2`处下断点调试一下

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-192246-1669347503.png "null")

在这里发现`0x0144B51D`的位置会输出`Password accepted`，所以这里把jnz改成je或者nop掉就可以了

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-192246-1669347505.png "null")

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-192246-1669347509.png)

保存出来看一下

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-192246-1669347512.png)

可以看到输入任意的内容已经激活成功，但是这样的话每次打开都需要点击一下check license，那么继续看看能不能让程序直接打开。

首先来梳理一下正常的逻辑程序是怎么运行的：首先在`0x0030B3FC`的位置处EAX和0xE7进行比较，此时EAX的值为0xE7，所以je跳转成立，程序运行到`0x0030B4DC` 处，`cmp ebx,0xDB`，这时候EBX的值为0x177，jnz不等于则跳转，所以此时跳转成立，跳转到`0x0030B60D`的位置处，这个时候程序已经跳过了验证成功的地方，继续执行，有三个cmp语句后跟jcc跳转指令，`cmp ebx,0xED`和`cmp ebx,0x20C`，这时EBX的值还是0x177，所以两个je都没有跳转，运行到第三个cmp指令`cmp eax,0x93`的位置，EAX此时的值为0xE7，这里是jnz指令所以跳转成功，跳转到`0x0030B6E8`的位置，输出无效的用户名密码，验证函数到此结束。

通过上面的分析当EBX等于0xDB的时候程序才会走到验证成功的位置，也就是说想要程序不每次运行都弹验证框，需要直接将0xDB赋给EBX

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-192246-1669347517.png)

返回到`0x0030B3FC`的位置继续往上跟踪可以看到EBX的值就是EAX的值，所以需要将0xDB赋给EAX，那么需要继续跟踪看看EAX的值是谁赋给的，在`0x0030B3E9`的位置处下断点，F8执行，发现在执行`call 0x0013808A`的时候EAX的值发生了变化，所以直接跟进call里面

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-192246-1669347519.png "null")

在开头直接给EAX赋值，`mov eax,0x2d retn 0x8`

最后把程序dump出来，发现程序直接打开就能使用了也不用每次都点击验证了。

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-192246-1669347522.png "null")

## 0x03 总结

其实010 editor对于新手逆向来说还是挺友好的，没有加壳，然后整个函数的逻辑也算比较清晰，更改起来也很简单，以后有时间的还是要研究一下注册验证的算法，然后写个注册机出来。

参考文章：逆向分析商业软件 010 Editor 及注册机编写

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-192246-1669347523.gif)

E

N

D

**本文作者：[TideSec](newpage/author?author_id=26366)**

**本文为安全脉搏专栏作者发布，转载请注明：**[**https://www.secpulse.com/archives/192246.html**](https://www.secpulse.com/archives/192246.html)

Tags: [010 editor](https://www.secpulse.com/archives/tag/010-editor)、[C&C](https://www.secpulse.com/archives/tag/cc)、[Editor](https://www.secpulse.com/archives/tag/editor)、[Unicode 文件](https://www.secpulse.com/archives/tag/unicode-%E6%96%87%E4%BB%B6)、[xml](https://www.secpulse.com/archives/tag/xml)、[批处理文件](https://www.secpulse.com/archives/tag/%E6%89%B9%E5%A4%84%E7%90%86%E6%96%87%E4%BB%B6)、[逆向分析](https://www.secpulse.com/archives/tag/%E9%80%86%E5%90%91%E5%88%86%E6%9E%90)

点赞：
6
[评论：0](#goComment)
收藏：
0

*新浪微博
QQ空间
微信扫一扫*

### 相关文章

* [![探究SMC局部代码加密技术以及在CTF中的运用](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/2023/03/1678429569077-300x190.png)

  探究SMC局部代码加密技术以及在CTF中…](https://www.secpulse.com/archives/197285.html "详细阅读 探究SMC局部代码加密技术以及在CTF中的运用")
* [![浅谈android端的字符串加密](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/2022/12/1670318227218-300x208.png)

  浅谈android端的字符串加密](https://www.secpulse.com/archives/193005.html "详细阅读 浅谈android端的字符串加密")
* [![图形化红队渗透辅助工具 V3.4](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/2022/12/16702288173571-300x200.png)

  图形化红队渗透辅助工具 V3.4](https://www.secpulse.com/archives/192770.html "详细阅读 图形化红队渗透辅助工具 V3.4")

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
| [![]( https://secpulseoss.oss-...