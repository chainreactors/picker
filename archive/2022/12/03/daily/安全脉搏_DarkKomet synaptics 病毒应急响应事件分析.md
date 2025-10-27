---
title: DarkKomet synaptics 病毒应急响应事件分析
url: https://www.secpulse.com/archives/192714.html
source: 安全脉搏
date: 2022-12-03
fetch_date: 2025-10-04T00:23:03.691260
---

# DarkKomet synaptics 病毒应急响应事件分析

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

# DarkKomet synaptics 病毒应急响应事件分析

[系统安全](https://www.secpulse.com/archives/category/articles/system)

[货拉拉安全](https://www.secpulse.com/newpage/author?author_id=40552)

2022-12-02

44,901

# 一、准备阶段

## 1.1 基本情况

**DarkComet （暗黑彗星）**是由 Jean-Pierre Lesueur（称为 DarkCoderSc）开发的远程访问木马（称为 RAT），在 2012 年初开始扩散，它用于许多有针对性的攻击，能够通过网络摄像头拍照，通过连接到 PC 的麦克风窃听对话，并获得对受感染机器的完全控制。该 RAT 还以其键盘记录和文件传输功能而闻名，因此，任何远程攻击者都可以将任何文件加载到受感染的机器上，甚至窃取管理员权限、计算机/用户名、语言/国家、操作系统信息、使用的内存、网络摄像头信息、文档等。它会禁用任务管理器、注册表编辑器和文件夹选项，修改注册表项以禁用 Windows 防火墙设置，此操作允许此恶意进程执行而不会被 Windows 防火墙检测到。别名有：Fynloski、Krademok、DarkKomet 等。

## 1.2 功能

DarkKomet 主要功能：远控，对用户行为进行监控并为攻击者开启 SYSTEM 后门，窃取用户信息并回传窃取的信息发送给攻击者，同时还可以下载其他恶意软件。

## 1.3 传播方式

DarkKomet 将自身伪装成笔记本电脑触控板的驱动程序 Synaptics Pointing Device Driver，启动后，会全盘遍历 exe 文件、xlsx 文件，并将目标文件更新到病毒资源中，将 shellcode 注入的图标资源替换为目标文件图标，然后用病毒文件覆盖目标文件，完成感染，实现不死及复生能力。并可通过U盘插入、xlsx 文件分享、远控软件捆绑实现横向扩散，具有极强传播能力。

##

# 二、检测阶段

![1.jpeg](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/2022/12/1-1024x682.jpeg "1-1024x682.jpeg")

货拉拉终端应急响应检测机制基于**TTP驱动**、**离群数据驱动**、**杀毒事件驱动**、**威胁情报驱动**混合。该次事件由EDR收集终端全量启动项数据，结合威胁情报接口，实现终端权限维持数据基线的分钟级扫描。高危事件通过webhook 实现IM告警，方便安全运营人员实时接入处置，并通过工单记录汇总。

聚合N day内 该病毒感染的终端量及感染者的账号、用户名、部门等信息，最终由多条alert形成单条完整incident。

![2.jpeg](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/2022/12/2-1024x897.jpeg "2-1024x897.jpeg")

通过 webhook/工单形式将消息推送给终端安全运营人员对事件进行下钻，IOC/TTP加入EDR实时检测阻断规则，完成由**单次事件检测** —— **一类事件阻断**的事件闭环。

# 三、抑制阶段

## 3.1 事件的处置

1、拦截回连c2域名、IP，中断连接。

2、远程接入应急溯源，获取TTP。

# 四、根除阶段

## 4.1 删维权

该病毒通过 Run 键实现到权限维持（开机自启动），删除启动项

![3.jpeg](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/2022/12/3-1024x318.jpeg "3-1024x318.jpeg")

## 4.2 清进程

结束 2 个Synaptics.exe进程

![4.jpeg](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/2022/12/4.jpeg "4.jpeg")

## 4.3 删文件

进入 DarkKomet 文件目录，只有WS文件夹，却找不到相关可执行文件

![5.jpeg](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/2022/12/5.jpeg "5.jpeg")

怀疑DarkKomet隐藏自身，取消勾选【隐藏受保护的操作系统文件】并选中【显示隐藏文件】

![6.jpeg](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/2022/12/6.jpeg "6.jpeg")

被隐藏的病毒文件 Synaptics.exe显形，

![7.jpeg](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/2022/12/7.jpeg "7.jpeg")

删除文件，提示需要SYSTEM权限（高于Administrator），病毒文件通过修改文件属主及文件权限实现强行驻留

![8.jpeg](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/2022/12/8.jpeg "8.jpeg")

修改文件属主为administrator并继承权限后，删除病毒文件

![9.png](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/2022/12/9.png "9.png")

## 4.4 溯源头

清除威胁后，溯源入口点，从取证角度获取 2022-05-17 16:29:30 运行软件信息，发现可疑文件路径

F:\柯美黑白机64位系统\

![10.jpeg](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/2022/12/10-1024x365.jpeg "10-1024x365.jpeg")

可疑点：该文件位于F盘，且运行时间与病毒创建时间密切相关，但用户终端上却只有C、D、E盘。

![12.jpeg](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/2022/12/12.jpeg "12.jpeg")

猜测该盘为第三方便携插入式U盘，咨询用户后得到【安装打印机】细节。

由此推测：该病毒原本位于U盘中，安装打印机时插入U盘，U盘内的病毒自动感染终端位于C盘的文件，实现横向扩散。

由于该病毒具有感染性，推测还感染了其他文件。通过遍历NTFS文件系统 MFT-TIME，获取 2022-05-17 16:29:30 - 2022 - 05 -17 16:29:40 创建及修改的所有文件，获取被感染文件信息

![13.jpeg](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/2022/12/13-1024x543.jpeg "13-1024x543.jpeg")

通过日志回溯取证，发现 f:\京瓷复印机\Kx6111118\_en\setup.exe入驻Run键，创建病毒文件 C:\ProgramData\Synaptics\Synaptics.exe，并将Synatics.exe添加启动项 。由此映证猜测，C2病毒感染源头为安装打印机时插入U盘。

# 五、恢复阶段

1、清除被感染的"\_cache\_"文件

2、IOC / TTP 加入EDR、杀毒，复验攻击能被实时阻断。

3、受损用户更改密码

# 六、总结阶段

IOC：

DNS：xred.mooo.com

IP：69.42.215.252

TTP：

![14.jpeg](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/2022/12/14-1024x312.jpeg "14-1024x312.jpeg")

## 6.1 历史事件

某用户请第三方安装师傅安装打印机，插入 U 盘后，U 盘中已存在的 DarkKomet 组织 synaptics 病毒自动运行，进而感染终端位于 C 盘下的十余个进程及文件。

某员工下载被投毒的 todesk 进行远程办公【具有 todesk 功能，实为 synaptics 远控病毒新变种】，导致感染 synaptics 病毒。

某员工下载 CAD 破解软件，其中夹杂最新版 synaptics 病毒。

...

本轮 synaptics 应急响应，终端产生的威胁主要来自：U 盘扩散、软件投毒捆绑这两种形式。病毒最明显特征为：未签名进程 **C:\ProgramData\Synaptics\Synaptics.exe** 入驻Run键以权限维持。

当下阶段，利用人性弱点进行投毒的事件层出不穷。针对员工高频安装的浏览器类、IM类、运维工具类、远程控制类软件，需做好软件与对应签名的映射验证，并针对高危场景离群数据进行威胁狩猎。辅以外部/内生威胁情报，构建滤网机制，对启动项软件流水加以管控。实现启动项快照机制，对未知/离群/高危/权限维持数据定时清理，在提升攻击者成本的同时，也增加检测/阻断未知攻击的可能。

**本文作者：[货拉拉安全](newpage/author?author_id=40552)**

**本文为安全脉搏专栏作者发布，转载请注明：**[**https://www.secpulse.com/archives/192714.html**](https://www.secpulse.com/archives/192714.html)

Tags: [DarkComet](https://www.secpulse.com/archives/tag/darkcomet)、[DarkKomet](https://www.secpulse.com/archives/tag/darkkomet)、[DarkKomet synaptics](https://www.secpulse.com/archives/tag/darkkomet-synaptics)、[Fynloski](https://www.secpulse.com/archives/tag/fynloski)、[Krademok](https://www.secpulse.com/archives/tag/krademok)、[暗黑彗星](https://www.secpulse.com/archives/tag/%E6%9A%97%E9%BB%91%E5%BD%97%E6%98%9F)、[木马](https://www.secpulse.com/archives/tag/%E6%9C%A8%E9%A9%AC)、[远控](https://www.secpulse.com/archives/tag/%E8%BF%9C%E6%8E%A7)

点赞：
1
[评论：0](#goComment)
收藏：
0

*新浪微博
QQ空间
微信扫一扫*

### 相关文章

* [![某查询和短信轰炸样本的分析](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/2023/08/6cd475e953cba46a99ac1b9196993cc-300x239.png)

  某查询和短信轰炸样本的分析](https://www.secpulse.com/archives/203338.html "详细阅读 某查询和短信轰炸样本的分析")
* [![从JS到内网横向](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/2023/04/1682065936883-300x267.png)

  从JS到内网横向](https://www.secpulse.com/archives/199384.html "详细阅读 从JS到内网横向")
* [![【恶意文件】沉寂之后，Emotet木马再次来袭](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/2023/04/1681724018362-300x186.png)

  【恶意文件】沉寂之后，Emotet木马再…](https://www.secpulse.com/archives/199128.html "详细阅读 【恶意文件】沉寂之后，Emotet木马再次来袭")

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
| ...