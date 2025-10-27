---
title: 3CXDesktopApp供应链攻击分析
url: https://www.secpulse.com/archives/200404.html
source: 安全脉搏
date: 2023-05-17
fetch_date: 2025-10-04T11:37:11.022464
---

# 3CXDesktopApp供应链攻击分析

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

# 3CXDesktopApp供应链攻击分析

[Web安全](https://www.secpulse.com/archives/category/articles/web)

[洞源实验室](https://www.secpulse.com/newpage/author?author_id=49765)

2023-05-16

24,455

**一、事件背景**

3CX是一家软件公司，该公司为客户提供基于软件的电话系统，用于企业或组织内部的通讯。

3CX电话系统可以在Windows或Linux服务器上部署，并提供包括VoIP、PSTN和移动电话在内的多种通讯方式。此外，3CX还提供一系列的通讯软件，包括用于电脑、移动设备及浏览器的应用程序，可以让用户通过各种方式与他人通讯。据3CX称，其提供的软件服务了600,000多个客户，遍布全球190多个国家。

2023年3月29日，CrowdStrike发出告警，指出具备合法签名的二进制程序3CXDesktopApp存在恶意行为。

**二、事件过程**

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-200404-1684201247.jpeg)

**2023年3月22日**

凌晨一点，部分用户反馈3CXDesktopApp自动更新的版本被杀毒软件告警。此时部分用户还将其定性为误报。

SentinelOne的告警信息显示软件存在shellcode或代码攻击能力。

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-200404-1684201248.png)

**2023年3月29日**

上午十一点，安全公司CrowdStrike发出告警，确定具备合法签名的二进制程序3CXDesktopApp存在恶意行为，危害Windows和macOS。

CrowdStrike怀疑其攻击行为源于LABYRINTH CHOLLIMA，这是一个具有有朝鲜相关背景的专业APT组织。

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-200404-1684201249.png)

**2023年3月30日**

上午六点，3CX的CEO Nike Galea发出安全警告，确认3CX的Windows Electron client遭受攻击，并建议用户卸载该应用程序改而选择基于WEB的PWA客户端。

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-200404-1684201253.png)

**2023年4月6日**

3CX发布未被攻击的18.12.425版本软件，但仍然建议用户使用基于WEB的PWA客户端。

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-200404-1684201254.png)

**三、技术分析**

* **受影响版本**

?Windows versions 18.12.407 and 18.12.416

?Mac OS versions 18.11.1213, 18.12.402, 18.12.407, and 18.12.416.

部分文件及对应hash如下?

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-200404-1684201258.png)

* **攻击分析**

安装程序具有合法签名，安装后的3CXDesktopApp启动时会主动加载安装目录下没有签名的ffmpeg.dll。

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-200404-1684201259.png)

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-200404-1684201260.png)

ffmpeg.dll被加载的时候会进行以下行为：

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-200404-1684201263.png)

首先打开安装路径下的d3dcompiler\_47.dll文件，并读入内存。

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-200404-1684201265.png)

对比读入内存数据与磁盘数据发现一致，且读入数据大小为0x4EDCD8。

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-200404-1684201269.png)

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-200404-1684201271.png)

随后定位shellcode，shellcode使用RC4算法进行了加密，密钥为3jB(2bsG#@c7。

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-200404-1684201277.png)

如下图所示，shellcode由8字节xFExEDxFAxCExFExEDxFAxCE定位，后续0x43B08字节为其shellcode。

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-200404-1684201279.png)

然后跳转到shellcode执行。

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-200404-1684201285.png)

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-200404-1684201290.png)

此时0x000001C7B90D3FA0为shellcode地址。

随后使用反射dll注入技术加载了放在shellcode中的dll文件，这里获取了一些dll函数用来后续修复导入表。

shellcode偏移0x65D处为dll文件开始处。

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-200404-1684201293.png)

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-200404-1684201298.png)

对该dll进行分析，发现其行为如下：

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-200404-1684201302.png)

如果首次执行，写入manifest当前时间，后续执行判断是否过了604800s（七天），如果已经过了七天则向https://raw.githubusercontent.com/IconStorages/images/main/icon%d.ico发送请求，加载后续的payload。

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-200404-1684201305.png)

七天正好与3月22号的首次更新至3月29日首次确定攻击行为的间隔一样。

在本文章所写的2023年5月9日，由于其Github仓库已关闭，无法获取后续payload。但是通过静态分析可以得出，后续会使用AES-GCM算法进行解密从icon中获取的数据。解密结果为C2服务器域名，域名如下?

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-200404-1684201308.png)

**四、相关反应**

**2023年3月30日**，3CXDesktopApp的提供商在官网上发出安全警告。

**2023年3月31日**，ffmpeg声明，其只提供源代码，编译的”ffmpeg.dll“**由供应商提供**。

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-200404-1684201310.png)

**2023年4月6日**，3CX发布未被攻击的18.12.425版本软件。

**五、事件启示**

本次事件，确定是一起**供应链攻击事件**，攻击者以3CX公司作为攻击对象。

最初的攻击定位在2022年4月，一名员工在其个人计算机上安装了受感染的X\_TRADER软件，该软件于2020年停用，但其软件签名有效期持续到了2022年10月。

随后攻击者通过该恶意软件获取了管理员级别的权限并且使用frp工具在3CX网络中横向移动，最终破坏了Windows和macOS的构建环境。

具体的破坏手法没有公布，据笔者猜测，可能是类似SolarWinds事件(被攻击者破坏了产品的构建系统)，也可能是篡改了构建的基础源码。

两次攻击的过程极为类似，都是使用已签名的安装包安装了软件，安装过程释放了恶意文件，最后通过反射dll注入，外联C2服务器。3CX的攻击过程如下图?

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-200404-1684201312.jpeg)

在3月22日3CXesktopApp首次被杀毒软件告警的时候，部分用户认为是杀毒软件的误报，可以看出由于应用更新的时候已经经过了签名和认证，所以用户对该应用保持了一定的信任，然而这种信任会导致供应链上游环节的安全问题在下游环节被放大。并且在更上游，从3CX员工因为下载X\_TRADER软件导致构建环境被破坏可以看出，互联网从业者与普通用户对带有合法签名的软件均无防范。

因此，供应链安全的保证不仅在于供应商对安全的重视，客户也应加强对供应链安全的重视，定期对其使用的组件、软件等进行安全检测。

**本文作者：[洞源实验室](newpage/author?author_id=49765)**

**本文为安全脉搏专栏作者发布，转载请注明：**[**https://www.secpulse.com/archives/200404.html**](https://www.secpulse.com/archives/200404.html)

Tags: [3CX](https://www.secpulse.com/archives/tag/3cx)、[PSTN](https://www.secpulse.com/archives/tag/pstn)、[Voip](https://www.secpulse.com/archives/tag/voip)、[移动电话](https://www.secpulse.com/archives/tag/%E7%A7%BB%E5%8A%A8%E7%94%B5%E8%AF%9D)

点赞：
2
[评论：0](#goComment)
收藏：
0

*新浪微博
QQ空间
微信扫一扫*

### 相关文章

* [![Advanced Penetration Testing第九章—北国...