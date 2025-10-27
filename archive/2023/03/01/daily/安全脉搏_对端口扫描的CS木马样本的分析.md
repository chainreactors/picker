---
title: 对端口扫描的CS木马样本的分析
url: https://www.secpulse.com/archives/196811.html
source: 安全脉搏
date: 2023-03-01
fetch_date: 2025-10-04T08:18:07.899159
---

# 对端口扫描的CS木马样本的分析

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

# 对端口扫描的CS木马样本的分析

[Web安全](https://www.secpulse.com/archives/category/articles/web)

[小道安全](https://www.secpulse.com/newpage/author?author_id=11697)
![]( https://www.secpulse.com/wp-content/themes/secpulse2017/img/renzheng3.png)

2023-02-28

15,195

序言

病毒、木马是黑客实施网络攻击的常用兵器，有些木马、病毒可以通过免杀技术的加持躲过主流杀毒软件的查杀，从而实现在受害者机器上长期驻留并传播。

CobaltStrike基础

**Cobalt Strike简称CS**，它是一款非常好用的渗透测试工具，它允许攻击者在受害机器上部署名为“Beacon”的代理，Beacon 为攻击者提供了丰富的功能。它可以快速地生成后门并通过其控制目标主机。

CS拥有多种协议主机上线方式，集成了提权，凭据导出，端口转发，服务扫描，自动化溢出，多模式端口监听，木马生成，木马捆绑，socket代理，office攻击，文件捆绑，钓鱼等多种功能。但它也通常被利用于恶意木马后门、被利用于远程控制。

它支持通过 shellcode方式，创建自定义的C2二进制可执行文件，还支持通过修改代码来隐藏恶意程序。

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-196811-1677573620.png)

**基于CobaltStrike生成恶意 payload， 共分为5种：**

1、HTML Application 生成 hta 形式的恶意 payload

2、 MS Office Macro 生成宏文档的 payload

3、 Payload Generator 生成各种语言的 payload

4、Windows Executable 生成可执行的分段 payload

5、 **Windows Executable(S) 生成可执行的不分段 payload**

**Windows平台的 payload 有分段和不分段两种模式：**

**1、选择分段:** 它生成的原始文件会很小，原始文件就是一个download，用于从C2下载并加载后续的 payload;

**2、不分段模式:** 它生成的原始文件跟普通软件大小差不多，原始文件是一个loader加载器，可以直接将 shellcode 加载执行。

样本基础分析

下图是本次分析样本的基本属性，这个样本的图标通过伪装成中国移动的图标，通过上文的理论基础，我们可以直接猜测出它是采用不分段的摸索，这个样本就是一个loader，它直接执行shellcode的功能。

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-196811-1677573622.png)

下面通过PE的查壳工具Detect IT Easy对样本进行基本构成属性的分析，它首先是PE64的程序，并且是通过PyInstaller工具进行打包的(也就是说这个程序是通过python语言开发的)，并且没有做任何保护的功能。

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-196811-1677573624.png)

下图通过CFF工具可以分析出，该样本的依赖模块都是系统模块，没有依赖自定义或者第三方的模块。

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-196811-1677573627.png)

行为数据分析

通过进程监控工具进行对样本启动过程进行文件监控**(在虚拟机环境上测试)**

下图可以清晰的看到该样本在启动的时候会创建很多文件(也就是依赖释放文件)：

1、这里面有个python38.dll模块，表示该样本采用python3.8版本进行编译的。

2、还有释放了好几个的pyd的文件(pyd文件时由python编译生成的 Python 扩展模块，为啥要打包成pyd文件呢？因为pyd文件可以更好的防止反编译，只能反汇编。要分析pyd文件就得借助ida静态反汇编工具进行分析。)。

3、还有个base\_library.zip文件(这个就是python工具打包成exe后，运行所需要的依赖模块)。

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-196811-1677573629.png)

下图是od中进行释放文件的功能实现部分。

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-196811-1677573631.png)

通过CreateFileMapping方式操作文件。

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-196811-1677573635.png)

通过网络**抓包工具Fiddler**对样本的网络行为分析

通过下图的监控工具截图中可以看到，该样本在启动后通过http方式的网络通信行为，**所指向的服务器：124.70.22.50:8090**

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-196811-1677573639.png)

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-196811-1677573643.png)

下图通过威胁情报的数据中心分析，该ip是华为云的，并且这个ip所指向的都已被标识为病毒相关信息。

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-196811-1677573646.png)

代码功能分析

从前面的分析这个样本是python基于python3.8开发的，通过python打包的应用可以通过解包还原出python的源代码，下面就对样本进行解包，分析解包后的源代码

1、通过基于pyinstxtractor.py进行解包，只要用pytho pyinstxtractor.py cs(样本名称)

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-196811-16775736461.png)

执行命令后，在目录中会出现解包后文件夹，这个文件夹就是解包后的数据

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-196811-1677573647.png)

通过下图可以看出这个样了里面主要由pyc文件、pyd文件、dll文件、zip文件构成的，其中高危端口检测.pyc就是样本的主程序。pyc文件无法直接查看需要将pyc文件转换为py文件。

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-196811-1677573648.png)

2、通过使用 uncompyle6 可以将.pyc文件反编译成.py文件

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-196811-1677573651.png)

执行完上面命令后，下图就是反编译转换后的py文件了，这时候就可以查看py的源代码。

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-196811-1677573654.png)

下图是反编译转换后高危端口扫描.py的源代码，这代码里面主要的功能实通过base64去加解密，通过开启一个线程去执行自定义的shellcode代码(shellcode代码可以用于对抗病毒查杀软件的查杀，也就是免杀功能)

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-196811-1677573657.png)

通过采用urllib方式的http通信（它是一个内置在Python标准库中的模块），使用http.client来实现HTTP和协议的客户端。基于Request方式进行http通信。

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-196811-1677573658.png)

防护思考

目前Cobalt Strike所有的后门都比较活跃，在红蓝对抗中占据很重要的地位，建议提前部署具备高级威胁检测能力的安全产品进行及时监控、防范。

个人降低和防范中木马病毒建议方式：

1、主机环境安装主流的病毒查杀软件并及时更新病毒库;

2、规范上网行为，不下载安装未知的软件;

3、不点开来历不明的文档、图片、音频视频等;

4、及时安装系统补丁，修复漏洞;

5、加强密码复杂度，定期更改密码;

6、进行严格的隔离，有关系统、服务尽量不开放到互联网上，内网中的系统也要通过防火墙、VLAN或网匣等进行隔离。

阅读结束

**本文作者：[小道安全](newpage/author?author_id=11697)**

**本文为安全脉搏专栏作者发布，转载请注明：**[**https://www.secpulse.com/archives/196811.html**](https://www.secpulse.com/archives/196811.html)

Tags: [cobalt strike](https://www.secpulse.com/archives/tag/cobalt-strike)、[CS](https://www.secpulse.com/archives/tag/cs)、[fiddler](https://www.secpulse.com/archives/tag/fiddler)、[Python](https://www.secpulse.com/archives/tag/python)、[反编译](https://www.secpulse.com/archives/tag/%E5%8F%8D%E7%BC%96%E8%AF%91)、[木马](https://www.secpulse.com/archives/tag/%E6%9C%A8%E9%A9%AC)、[渗透测试](https://www.secpulse.com/archives/tag/%E6%B8%97%E9%80%8F%E6%B5%8B%E8%AF%95)、[病毒](https://www.secpulse.com/archives/tag/%E7%97%85%E6%AF%92)、[端口](https://www.secpulse.com/archives/tag/%E7%AB%AF%E5%8F%A3)、[进程监控工具](https://www.secpulse.com/archives/tag/%E8%BF%9B%E7%A8%8B%E7%9B%91%E6%8E%A7%E5%B7%A5%E5%85%B7)

点赞：
0
[评论：0](#goComment)
收藏：
0

*新浪微博
QQ空间
微信扫一扫*

### 相关文章

* [![《内网安全攻防》姊妹篇《红队之路》重磅上市！（文末赠书）](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-204824-1711610670-300x300.png)

  《内网安全攻防》姊妹篇《红队之路》重磅上…](https://www.secpulse.com/ar...