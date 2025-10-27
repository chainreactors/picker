---
title: 【勒索防护】MSI 等多个企业已遭受攻击！MoneyMessage 勒索软件突现
url: https://www.secpulse.com/archives/199280.html
source: 安全脉搏
date: 2023-04-21
fetch_date: 2025-10-04T11:31:26.318541
---

# 【勒索防护】MSI 等多个企业已遭受攻击！MoneyMessage 勒索软件突现

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

# 【勒索防护】MSI 等多个企业已遭受攻击！MoneyMessage 勒索软件突现

[系统安全](https://www.secpulse.com/archives/category/articles/system)

[Further\_eye](https://www.secpulse.com/newpage/author?author_id=9241)
![]( https://www.secpulse.com/wp-content/themes/secpulse2017/img/renzheng2.png)

2023-04-20

32,310

**恶意文件名称：**

MoneyMessage

**威胁类型：**

勒索软件

**简单描述：**

MoneyMessage是一款横跨Linux和Windows的双平台勒索软件。该组织在部署勒索软件前，会窃取用户的私人数据，MSI 等多个企业的数据也已遭泄露。

**恶意文件分析**

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-199280-16819783171.gif)

**事件描述**

深信服深盾终端实验室在近期的运营工作中捕获了 MoneyMessage 勒索病毒，通过关联分析发现该样本最早出现于2023年3 月。**截至发文，从全球范围来看，已有多个受害者公开披露其遭受了MoneyMessage勒索病毒的攻击，其中不乏大型公司。**

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-199280-1681978318.png)

援引 Bleeping Computer 2023年4月7日的消息，MSI 已确认其遭受勒索软件攻击：

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-199280-16819783181.png)

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-199280-1681978319.gif)

**恶意文件分析**

选取SHA256为dc563953f845fb88c6375b3e9311ebed49ce4bcd613f7044989304c8de384dac的样本进行分析，其基本信息如下所示。

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-199280-1681978319.png)

勒索软件开始执行后，其会从文件的末尾读取攻击者留存的配置文件，配置文件具体如下所示：

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-199280-1681978320.png)

读取配置文件命令行如下图所示：

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-199280-1681978323.png)

提取出的参数如下所示：

info\_text\_message

mutex\_name

extensions

skip\_directories

network\_public\_key

network\_private\_key

processes\_to\_kill

services\_to\_stop

logging

domain\_login

domain\_password

crypt\_only\_these\_directories

temporary\_extension

从配置文件读取出的信息将用于后续的加密过程。

1. 创建 Mutex 避免重复运行。

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-199280-16819783231.png)

2. 通过以下 API 组合枚举当用户系统中的所有服务及其状态：OpenSCManagerW、EnumServicesStatusExW、CloseServiceHandle。

若服务名称符合以下名称集合中的任意一个元素，则关闭该服务。

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-199280-1681978324.png)

3. 通过 API 组合关闭配置文件中提到的进程。

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-199280-1681978325.png)

4. 删除 VSS 备份文件。

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-199280-1681978329.png)

5. 横向移动。使用存储在配置文件中的账号和密码，尝试连接当前计算机所在网络的其它机器，连接成功则再次进行加密操作。

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-199280-16819783291.png)

配置文件中的字符串解密后对应的账户名和密码如下所示，在此处攻击者并未使用密码字典进行 RDP 爆破来传播勒索病毒，而是使用有限数量且特殊的用户名和密码，具有较强的指向性。

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-199280-1681978331.png)

此勒索样本和传统的勒索病毒不同的点在于，此勒索样本并不会修改加密文件的后缀。加密后的文件如下图所示：

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-199280-16819783311.png)

加密操作完成后，攻击者留存的勒索信如下图所示：

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-199280-1681978333.png)

在此勒索样本的分析过程中，并未发现其有明显的外连行为。根据 hackread 于 2023年4月8日的一篇文章，MSI 对外声称遭受到 MoneyMessage 勒索病毒的攻击，MoneyMessage 要求 MSI 支付 4 百万美元，否则将窃取的 MSI 信息公之于众。MSI 于2023年4月7日发表了一篇声明，其修复了位于固件平台上的一个漏洞。MoneyMessage 很可能利用了该固件漏洞获取了MSI内部计算机的控制权，并部署相应的勒索软件。

国外某社交软件平台上一位用户声称，MoneyMessage 团伙使用 RClone 将窃取的信息传输至云存储服务中。

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-199280-1681978334.png)

该组织窃取的信息在如下网站公布：

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-199280-1681978335.png)

MSI  泄露的信息如下所示：

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-199280-1681978339.png)

**IOC**

**Sha256：**

dc563953f845fb88c6375b3e9311ebed49ce4bcd613f7044989304c8de384dac

4f8bd37851b772ee91ba54b8fd48304a6520d49ea4a81d751570ea67ef0a9904

97abcf01deea74eb3771ddcef8bfc0906b46a55172588de8e2ad20f8d92b2de7

bbdac308d2b15a4724de7919bf8e9ffa713dea60ae3a482417c44c60012a654b

**解决方案**

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-199280-1681978341.gif)

**处置建议**

**预防勒索攻击措施：**

Ø 避免打开可疑或来历不明的邮件中的链接和附件。

Ø 进行定期备份，并将这些备份保存在离线状态或单独的网络中。

Ø 安装知名的防病毒和 Internet 安全软件包。

当遭遇勒索攻击后：

Ø 对受感染设备进行断网。

Ø 断开外部存储设备（如果已连接）。

Ø 检查系统日志中是否存在可疑事件。

**本文作者：[Further\_eye](newpage/author?author_id=9241)**

**本文为安全脉搏专栏作者发布，转载请注明：**[**https://www.secpulse.com/archives/199280.html**](https://www.secpulse.com/archives/199280.html)

Tags: [Linux](https://www.secpulse.com/archives/tag/linux)、[MoneyMessage](https://www.secpulse.com/archives/tag/moneymessage)、[MSI](https://www.secpulse.com/archives/tag/msi)、[windows](https://www.secpulse.com/archives/tag/windows)、[勒索病毒](https://www.secpulse.com/archives/tag/%E5%8B%92%E7%B4%A2%E7%97%85%E6%AF%92)、[勒索软件](https://www.secpulse.com/archives/tag/%E5%8B%92%E7%B4%A2%E8%BD%AF%E4%BB%B6)

点赞：
1
[评论：0](#goComment)
收藏：
0

*新浪微博
QQ空间
微信扫一扫*

### 相关文章

* [![Responder与evil-winRM配合远程登录Windows](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/2023/08/16872431395792-300x192.png)

  Responder与evil-winRM…](https://www.secpulse.com/archives/203051.html "详细阅读 Responder与evil-winRM配合远程登录Windows")
* [![某次演练复盘总结](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/2023/06/1687313516203-300x202.png)

  某次演练复盘总结](https://www.secpulse.com/archives/202339.html "详细阅读 某次演练复盘总结")
* [![Windows版宝塔bypass到RDP登录](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/2023/06/1686117734105-300x189.png)

  Windows版宝塔bypass到RDP…](https://www.secpul...