---
title: 【恶意文件】AgentTesla 贼心不死，换壳之后卷土重来
url: https://www.secpulse.com/archives/197248.html
source: 安全脉搏
date: 2023-03-10
fetch_date: 2025-10-04T09:06:09.045662
---

# 【恶意文件】AgentTesla 贼心不死，换壳之后卷土重来

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

# 【恶意文件】AgentTesla 贼心不死，换壳之后卷土重来

[Web安全](https://www.secpulse.com/archives/category/articles/web)

[Further\_eye](https://www.secpulse.com/newpage/author?author_id=9241)
![]( https://www.secpulse.com/wp-content/themes/secpulse2017/img/renzheng2.png)

2023-03-09

14,365

**恶意家族名称：**

AgentTesla

**威胁类型：**

间谍软件

**简单描述：**

2023 年 2 月 13 日，深信服 XDR 捕获新型间谍软件。

**恶意文件分析**

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-197248-16783494521.gif)

**恶意事件描述**

2023 年 2 月13 日，深信服 XDR 捕获新型间谍软件，此次事件中的恶意程序通过钓鱼邮件传播，当受害者解压邮件附件并执行其中的恶意程序之后，该程序会通过 PowerShell 添加 Defender 扫描白名单并创建计划任务，之后执行窃密操作。

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-197248-1678349453.gif)

**恶意事件分析**

通过进程执行链可以发现该样本是通过钓鱼邮件投递，受害者解压之后执行。

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-197248-1678349453.png)

该样本是一个 .NET 编写的窃密程序，通过对资源节区的数据进行解密还原出恶意模块，然后使用反射加载的方式执行该模块。

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-197248-1678349456.png)

调试发现该恶意模块名为 B4000。入口函数为Melvin.White。跟进函数，首先使用Sleep 休眠了 44s，在对一段硬编码的数据进行base64解码后再解压缩，还原出一个 PE 文件。

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-197248-1678349457.png)

同样使用反射加载的方式加载还原出来的 PE，名为 Cruiser，在通过加载模块中的函数从图像中提取出另外一个模块 HIVacSim，同样使用反射加载。找到模块入口函数如下：

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-197248-1678349461.png)

进入模块之后会执行一系列恶意操作。

**释放文件**

从资源节区中释放文件至 C:UsersUserNAmeAppDataRoamingNgsWWESFAPv.exe

，释放的文件与当前文件一致。

**创建计划任务**

通过schtasks.exe从XML文件中创建计划任务，二进制文件指向`C:UsersUserNameAppDataingRomaingNgsWWSFAPv.exe。`

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-197248-1678349463.png)

**添加Defender白名单**

通过 Powershell 添加 Defender 白名单。

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-197248-1678349466.png)

**创建傀儡进程**

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-197248-1678349467.png)

**创建傀儡进程步骤大致如下：**

1. 通过 GetThreadContext 获取线程内容

2. 使用 ReadProcessMemory 读取进程内容

3. 使用 VirtualAllocEx 在傀儡进程中分配空间

4. 使用 WriteProcessMemory 往分配的内存中写入数据，

5. 使用 SetThreadContext 设置执行入口。

6. 使用 ResumeThread 恢复傀儡进程的主线程。

在 SetThreadContext 处下一个断点，找到傀儡进程入口点：

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-197248-1678349470.png)

在写完数据并激活傀儡进程之后当前进程就会结束，导出写完数据的傀儡进程继续调试。

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-197248-1678349475.png)

**信息主机收集**

通过 Win32\_BaseBoard 获取主板信息，之后获取主机和用户名信息等。

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-197248-16783494751.png)

**获取公网 IP**

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-197248-1678349476.png)

**收集软件信息**

收集多种浏览器信息。

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-197248-1678349477.png)

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-197248-1678349480.png)

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-197248-1678349482.png)

在多个 try catch 中收集特定安装程序的数据：

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-197248-1678349486.png)

包括 discord、Claws mail、eM Client、FileZilla、Foxmail、FTP Navigator、WinSCP、RealVNC、MySQL 等程序、以及系统凭证等信息。

**发送数据**

将收集到的数据进行处理之后通过邮件发送到特定邮箱。

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-197248-1678349487.png)

**解决方案**

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-197248-1678349492.gif)

**处置建议**

1. 删除计划任务

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-197248-1678349492.png)

2. 取消 Defender 白名单

3. 终结该进程及其子进程并删除对应文件。

**本文作者：[Further\_eye](newpage/author?author_id=9241)**

**本文为安全脉搏专栏作者发布，转载请注明：**[**https://www.secpulse.com/archives/197248.html**](https://www.secpulse.com/archives/197248.html)

Tags: [AgentTesla](https://www.secpulse.com/archives/tag/agenttesla)、[恶意模块](https://www.secpulse.com/archives/tag/%E6%81%B6%E6%84%8F%E6%A8%A1%E5%9D%97)、[白名单](https://www.secpulse.com/archives/tag/%E7%99%BD%E5%90%8D%E5%8D%95)、[钓鱼邮件](https://www.secpulse.com/archives/tag/%E9%92%93%E9%B1%BC%E9%82%AE%E4%BB%B6)、[间谍软件](https://www.secpulse.com/archives/tag/%E9%97%B4%E8%B0%8D%E8%BD%AF%E4%BB%B6)

点赞：
1
[评论：0](#goComment)
收藏：
0

*新浪微博
QQ空间
微信扫一扫*

### 相关文章

* [![钓鱼邮件攻击分析](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/2023/05/1685429063311-300x172.png)

  钓鱼邮件攻击分析](https://www.secpulse.com/archives/201168.html "详细阅读 钓鱼邮件攻击分析")
* [![疑似 Kasablanka 组织针对阿塞拜疆及乌兹别克斯坦地区的攻击行动分析](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-196928-1677832266-300x186.png)

  疑似 Kasablanka 组织针对阿塞…](https://www.secpulse.com/archives/196928.html "详细阅读 疑似 Kasablanka 组织针对阿塞拜疆及乌兹别克斯坦地区的攻击行动分析")
* [![社会工程学 | cobalstrike批量发送钓鱼邮件方法](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/2023/02/1676358686959-300x224.png)

  社会工程学 | cobalstrike批…](https://www.secpulse.com/archives/195833.html "详细阅读 社会工程学 | cobalstrike批量发送钓鱼邮件方法")

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
| [![]( https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/2022/08/16/9f4b1a0a8978eebf651bfe827b4d307a-300x255.jpeg)](https://www.secpulse.com/newpage/author?author_id=924...