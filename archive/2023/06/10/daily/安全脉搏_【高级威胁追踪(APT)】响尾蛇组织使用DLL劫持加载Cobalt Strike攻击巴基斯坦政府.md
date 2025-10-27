---
title: 【高级威胁追踪(APT)】响尾蛇组织使用DLL劫持加载Cobalt Strike攻击巴基斯坦政府
url: https://www.secpulse.com/archives/201630.html
source: 安全脉搏
date: 2023-06-10
fetch_date: 2025-10-04T11:44:16.967631
---

# 【高级威胁追踪(APT)】响尾蛇组织使用DLL劫持加载Cobalt Strike攻击巴基斯坦政府

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

# 【高级威胁追踪(APT)】响尾蛇组织使用DLL劫持加载Cobalt Strike攻击巴基斯坦政府

[资讯](https://www.secpulse.com/archives/category/news)

[Further\_eye](https://www.secpulse.com/newpage/author?author_id=9241)
![]( https://www.secpulse.com/wp-content/themes/secpulse2017/img/renzheng2.png)

2023-06-09

12,115

***![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-201630-1686282003.gif)***

***![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-201630-16862820031.gif)*****![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-201630-1686282004.gif)****

**概述**

**近期，深信服深瞻情报实验室监测到响尾蛇组织对巴基斯坦政府单位的最新攻击动态。**响尾蛇组织， 又称Sidewinder、APT-C-17、T-APT-04，是一个来自于南亚地区的境外APT组织。该组织主要针对中国、巴基斯坦等亚洲地区国家进行网络间谍活动，其中以窃取敏感信息为主。相关攻击活动最早可以追溯到2012年，至今还非常活跃。在针对巴基斯坦地区的攻击中，该组织主要针对政府机构、军事单位进行攻击。

在本次攻击活动中，我们监测到响尾蛇组织使用钓鱼邮件攻击政府单位的事件，本次事件相关的邮件附件名称为“ Adv-16-2023”，是关于巴基斯坦内阁部门发布的网络安全咨询16号文件。

钓鱼文件内容以文档被微软Azure云安全保护为由，引诱用户下载带有密码的压缩包文件，压缩包中包含一个恶意lnk文件，用于下载第二阶段HTA下载脚本，最后劫持本地Onedrive客户端程序及其更新程序实现DLL侧加载，最终上线Cobalt Strike载荷，用户机器中Onedrive定时更新的计划任务也会成为响尾蛇组织的持久化计划任务，整个攻击过程与之前披露的攻击大相径庭，攻击过程更为简单，样本制作成本更低。

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-201630-1686282004.png)

**分析**

在本次攻击活动中，我们捕获响尾蛇组织的钓鱼文件，以Adv-16-2023.pdf命名，诱导用户下载RAR压缩包文件，并提供解压密码。

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-201630-1686282005.png)

下载的RAR压缩文件包含一个lnk文件，文件名后缀为.pdf.lnk来伪装成pdf文件，引诱用户打开文件，该lnk文件信息如下。

|  |  |
| --- | --- |
| 描述 | 详细信息 |
| 名称 | Advisory-16-2023.pdf.lnk |
| 文件大小 | 2300 bytes |
| 文件类型 | LNK |
| 文件功能 | Downloader |
| 编译时间 | / |
| 开发平台及语言 | / |
| 是否加壳 | 否 |
| VT首次上传时间 | / |
| md5 | AAA784E212C4F65E95B43F56B81E4AB4 |
| Sha256 | C1BFF4A3E396EBABC8ABBA92AF92B5345ED5E044366A346480E141E847B47BF9 |

打开文件后，会使用mshta下载执行远程something.hta文件。

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-201630-1686282006.png)

下载的hta文件中会执行VBScript脚本，继续下载后续组件。

|  |  |
| --- | --- |
| 描述 | 详细信息 |
| 名称 | something.hta |
| 文件大小 | 680 bytes |
| 文件类型 | HTA |
| 文件功能 | Downloader |
| 编译时间 | / |
| 开发平台及语言 | / |
| 是否加壳 | 否 |
| VT首次上传时间 | / |
| md5 | 2BCE7A8E34E4751C8E421BAA4C4A0ADA |
| Sha256 | F0CB23D26AF39BBFAE450F37BC7642B59D30EE346020485FECC5CD8C33D2190A |

下载version.dll放置在本地Onedrive目录，当本地64位的Onedrive.exe和OneDriveStandaloneUpdater.exe执行时会被劫持以加载恶意version.dll，定时执行OneDriveStandaloneUpdater.exe更新Onedrive的计划任务也会变成响尾蛇组织的常驻项。

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-201630-1686282008.png)

另外从巴基斯坦的内阁部门官方网站（cabinet.gov.pk）下载“Advisory No. 16”网络安全咨询16号文件，对应钓鱼文件中提及的内容。

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-201630-1686282009.png)

下载的version.dll的存放路径为%LOCALAPPDATA%MicrosoftOneDrive，文件为64位，需要同为64位的Onedrive.exe和OneDriveStandaloneUpdater.exe加载，恶意的version.dll相关信息如下。

|  |  |
| --- | --- |
| 描述 | 详细信息 |
| 名称 | version.dll |
| 文件大小 | 275456 bytes |
| 文件类型 | DLL |
| 文件功能 | RAT |
| 编译时间 | / |
| 开发平台及语言 | / |
| 是否加壳 | 否 |
| VT首次上传时间 | / |
| md5 | F2974B8D6B0B2774F49642D53BDEE8A4 |
| Sha256 | 37E3465D6FCCFAE6E1C29526AA015A766F8FC26CC61ED821F3E0B44D794C99EC |

其导出函数GetFileInfoSize和GetFileVersionInfoSizeW指向同一个偏移量，是Onedrive.exe导入dll后会调用的函数。

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-201630-1686282012.png)

GetFileInfoSize和GetFileVersionInfoSizeW函数中会调用函数FUN\_180001120解密执行后续的载荷。

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-201630-16862820121.png)

函数中先读取系统目录下的ntdll中的.text段替换掉当前进程加载的ntdll中的.text，解除函数挂钩，如果有安全软件通过在ntdll中设置钩子实现对进程行为的监控，那么该恶意文件的操作会让这种类型的监控方式失效。

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-201630-1686282014.png)

通过计算硬编码16字节的数据的SHA256值，作为AES-256解密的密钥，解密出shellcode，最后执行。

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-201630-1686282016.png)

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-201630-1686282017.png)

执行的shellcode会反射加载一个Cobalt Strike的beacon，连接攻击者C2：35.175.135.236，实现远程控制。

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-201630-16862820171.png)

**关联分析**

另外通过关联分析找到关联域名finance-govpk.servehttp.com和csd-govpk.servehttp.com

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-201630-1686282018.png)

与csd-govpk.servehttp.com关联的https[:]//csd-govpk.servehttp.com/Advisory-16-2023.rar攻击过程和上诉分析一致。不同的是finance-govpk.servehttp.com关联到一个钓鱼文档，其详细信息如下。

|  |  |
| --- | --- |
| 描述 | 详细信息 |
| 名称 | Elligible- Employee-List.xls |
| 文件大小 | 134656 bytes |
| 文件类型 | XLS |
| 文件功能 | Downloader |
| 编译时间 | / |
| 开发平台及语言 | / |
| 是否加壳 | 否 |
| VT首次上传时间 | 2023-05-19 20:36:03 UTC |
| md5 | d2bebe3912a5700d76635af29f098cfb |
| Sha256 | 135efe01516830bed632b746171c14650f4b0ceb943ea4a6ce91c0fdcb9876c4 |

文档打开后，只有允许宏执行才能看到内容，来诱导用户执行文档中恶意宏代码。

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-201630-1686282019.png)

宏代码将诱导用户打开宏的图片删除显示出诱饵信息，然后使用UrlDownloadFileA下载version.dll放置到Onedrive目录下，进行dll劫持。其功能和上文分析的something.hta相近，但使用不同的钓鱼方式。

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-201630-1686282020.png)

**溯源归因**

**溯源归因-基础设施：**

通过分析ntc-govpk.servehttp.com，finance-govpk.servehttp.com，csd-govpk.servehttp.com的域名构造，符合格式[xxx]govpk.servehttp.com，这是响尾蛇组织常用的域名构造方式，以及钓鱼C2只允许巴基斯坦等攻击目标区域IP才能下载文件的访问控制，都与响尾蛇组织的特征非常相似，此外多个外部情报也将ntc-govpk.servehttp.com等域名归为响尾蛇组织。

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-201630-1686282021.png)

**总结**

响尾...