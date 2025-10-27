---
title: 靶场攻略 | vulhub_DC6
url: https://www.secpulse.com/archives/191716.html
source: 安全脉搏
date: 2022-11-19
fetch_date: 2025-10-03T23:11:48.439917
---

# 靶场攻略 | vulhub_DC6

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

# 靶场攻略 | vulhub\_DC6

[资讯](https://www.secpulse.com/archives/category/news)

[贝塔安全实验室](https://www.secpulse.com/newpage/author?author_id=9525)
![]( https://www.secpulse.com/wp-content/themes/secpulse2017/img/renzheng0.png)

2022-11-18

10,594

DC-6是一个易受攻击的实验环境，最终目的是让入侵者获得root权限，并读取flag。通过tweet可以联系到作者@DCAU7。DC\_6使用的操作系统为Debian 64位，可以在VirtualBox、VMware上直接运行。

> **靶场下载链接：**

```
Download：http://www.five86.com/downloads/DC-6.zip
Download (Mirror)：https://download.vulnhub.com/dc/DC-6.zip
Download (Torrent)：https://download.vulnhub.com/dc/DC-6.zip.torrent (Magnet)
```

**注：**该靶机作者在后面给出了相关提示：

```
cat /usr/share/wordlists/rockyou.txt | grep k01 > passwords.txt
```

**(1) 环境搭建**

根据作者的安装说明，将压缩文件下载后，通过vm或者virtualbox打开即可，注意由于作者设置为桥接模式，为了试验方便此处可以改为NAT模式。

**(2) 主机发现**

通过arp(地址解析协议)进行局域网内主机发现，arp是根据IP地址获取物理地址的一个TCP/IP协议。主机发送信息时将包含目标IP地址的ARP请求广播到网络上的所有主机，并接收返回消息，以此确定目标的物理地址；收到返回消息后将该IP地址和物理地址存入本机ARP缓存中并保留一定时间，下次请求时直接查询ARP缓存以节约资源。**此处利用metasploit工具下auxiliary模块，通过arp协议发现内网主机的ip地址为192.168.71.132。**

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-191716-1668677173.jpg)

**(3) 端口探测**

利用nmap工具进行端口探测，相信大家对于nmap已经相当熟悉了，下面列举了一些nmap常见参数：

-A：一次扫描包含系统探测、版本探测、脚本扫描和跟踪扫描 ......作者太懒了0.0！

往端口扫描结果可知系统开放了两个端口：22端口(ssh)，80端口(http)。此处有两个利用思路，第一种是通过hydra对ssh服务进行爆破，第二种思路则是通过web进行渗透。可以进一步发现http服务被重定向到了http://wordy/

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-191716-16686771731.jpg)

**(4) 访问web服务**

由于web服务被重定向到了 http://wordy/ 此时可以本地添加域名到主机文件，这样以后我们访问 http://wordy/ 就相当于访问对应的ip地址。添加完域名及对应ip后，可以发现已经能够访问http://wordy/ 。

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-191716-1668677174.jpg)

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-191716-16686771741.jpg)

**(5) 利用工具对wordpress网站信息搜集**

查看打开的页面为wordpress搭建的web环境，利用工具wpscan对该web环境进黑盒扫描（WPScan是一个扫描WordPress漏洞的黑盒子扫描器），可以获取到wordpress的版本，主题，插件，后台用户以及后台用户密码等，执行过程如下：

```
wpscan --url http://wordy --enumerate vp --enumerate vt --enumerate t --enumerate u
```

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-191716-1668677175.jpg)

获取到的可用信息如下：

```
url链接：
http://wordy/xmlrpc.php
http://wordy/readme.html
http://wordy/wp-cron.php
wordpress版本为：5.1.1
Author: the WordPress team
枚举出的用户姓名如下：
admin
graham
mark
sarah
jens
```

**(6) 利用已知提示登录系统**

在kali系统执行以下命令，生成一个带有k01的新密码字典passwords.txt，rockyou.txt.gz文件需要自己解压缩，gunzip rockyou.txt.gz。

```
cat /usr/share/wordlists/rockyou.txt | grep k01 > passwords.txt
```

```

```

根据枚举出的用户名和密码进行登录（http://wordy/wp-login.php），可以看到如下图所示界面，通过wordspress管理后台分析，并没有发现可以利用的漏洞。此时尝试寻找是否存在插件漏洞：**activity monitor**

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-191716-16686771752.jpg)

**(7) activity monitor漏洞利用**

将exploits/php/webapps/45274.html中的内容根据如下格式进行修改：

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-191716-1668677176.jpg)

nc -l -v -p 9999 在本机进行监听，通过web访问45274.html文件，点击运行后。可以看到nc成功反弹，效果如下图所示：

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-191716-1668677177.jpg)

进一步执行如下指令获取完整的shell：

```
python -c 'import pty; pty.spawn("/bin/bash")'
```

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-191716-1668677177.png)

通过目录查看，发现在/home/mark/stuff目录下存在thing-to-do.txt文件，其内容为：

```
Things to do:
- Restore full functionality for the hyperdrive (need to speak to Jens)
- Buy present for Sarah's farewell party
- Add new user: graham - GSo7isUM1D4 - done
- Apply for the OSCP course
- Buy new laptop for Sarah's replacement
```

添加了一个用户graham 口令为 GSo7isUM1D4 ，因为系统开放了22端口，此时可以通过ssh登录该用户。

**(8) 漏洞利用与提权**

```
ssh graham@192.168.1.103
输入登录口令：GSo7isUM1D4
```

ssh成功进行了登录，此时登录用户为graham。

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-191716-16686771771.jpg)

继续输入 sudo -l 查看可执行的操作。发现能够以jens用户，不使用口令执行情况下执行backups.sh。打开文件backups.sh为一个文件减压的命令行，可将减压指令删除，换成/bin/bash 以jens用户去执行操作。

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-191716-1668677178.png)

此时用户为jens，进一步，继续执行sudo -l 查询可执行的操作，发现能够以root用户，在不使用口令的的情况下执行nmap。故可通过nmap指令调用自己设定好的脚本如执行/bin/bash，新建一个nmap可执行的脚本 root.nse，输入如下内容：

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-191716-1668677178.jpg)

通过nmap运行该root.nse脚本，进入root用户。

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-191716-1668677179.jpg)

**本文作者：[贝塔安全实验室](newpage/author?author_id=9525)**

**本文为安全脉搏专栏作者发布，转载请注明：**[**https://www.secpulse.com/archives/191716.html**](https://www.secpulse.com/archives/191716.html)

Tags: [metasploit](https://www.secpulse.com/archives/tag/metasploit)、[vulhub](https://www.secpulse.com/archives/tag/vulhub)、[靶场](https://www.secpulse.com/archives/tag/%E9%9D%B6%E5%9C%BA)

点赞：
1
[评论：0](#goComment)
收藏：
0

*新浪微博
QQ空间
微信扫一扫*

### 相关文章

* [![代码审计 | Wavsep靶场审计防御](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/2023/06/1686638778312.png)

  代码审计 | Wavsep靶场审计防御](https://www.secpulse.com/archives/201916.html "详细阅读 代码审计 | Wavsep靶场审计防御")
* [![如何复现网传微信csv注入漏洞？](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/2023/05/1683601873856-300x176.png)

  如何复现网传微信csv注入漏洞？](https://www.secpulse.com/archives/200060.html "详细阅读 如何复现网传微信csv注入漏洞？")
* [![Privilege Escalation 权限提升](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/2023/04/16811117785231-300x227.png)

  Privilege Escalation…](https://www.secpulse.com/archives/198765.html "详细阅读 Privilege Escalation 权限提升")

评论  (0)

昵称

必填
您当前尚未登录。
[登录？](https://www.secpulse.com/user_...