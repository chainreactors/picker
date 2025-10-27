---
title: Tellyouthepass结合高危漏洞实施攻击：产品联动保护用户数据安全！
url: https://www.secpulse.com/archives/200779.html
source: 安全脉搏
date: 2023-05-23
fetch_date: 2025-10-04T11:36:48.151131
---

# Tellyouthepass结合高危漏洞实施攻击：产品联动保护用户数据安全！

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

# Tellyouthepass结合高危漏洞实施攻击：产品联动保护用户数据安全！

[漏洞](https://www.secpulse.com/archives/category/vul)

[Further\_eye](https://www.secpulse.com/newpage/author?author_id=9241)
![]( https://www.secpulse.com/wp-content/themes/secpulse2017/img/renzheng2.png)

2023-05-22

12,219

**恶意文件名称：**

Tellyouthepass

**威胁类型：**

勒索病毒

**简单描述：**

Tellyouthepass 勒索病毒从 2020 年 7 月开始在国内活跃，早期利用永恒之蓝漏洞攻击套件扩散传播，之后通过 Log4j2 漏洞、Shiro 反序列化漏洞等执行任意代码，从而控制受害主机。该家族针对 Windows 和 Linux 实现双平台勒索，多次活跃直接导致国内多个企业大面积业务停摆。

**恶意文件分析**

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-200779-16847273481.gif)

**事件描述**

**自 5 月 7 日起，深信服深盾终端实验室****收到了多家单位的勒索应急求助，****网络与应用安全能力部、深瞳漏洞实验室、深盾终端实验室及时对该类事件进行响应，**发现国内大量主机遭受到了不定向的勒索攻击。通过排查发现该恶意事件为Tellyouthepass勒索家族利用了某友NC反序列化、某某通电子文档安全管理系统等多个高危漏洞上传webshell并执行勒索病毒。

针对出现的多起勒索攻击事件，**深信服AF通过联动SAAS XDR，成功检测出黑客在后渗透阶段利用了冰蝎WebShell通信。虽然通信过程加密、行为隐蔽，但仍被AF+SAAS XDR成功联动检出，并且深信服EDR勒索防护AI引擎在终端侧成功拦截了多起勒索攻击事件，失陷外联检测引擎成功检测到webshell加密通信行为。**

**本月出现两大类tellyouthepass结合漏洞出现的勒索攻击：**

1、针对NC的勒索攻击与去年12月在国内流行的勒索攻击基本一致，参考链接如下：

https://mp.weixin.qq.com/s/1-H\_LDOeLQkxVP1TZsdEWA

2、本文主要针对结合高危漏洞实施的攻击进行详细分析

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-200779-1684727349.gif)

**勒索家族介绍**

一旦勒索软件完成对系统文件的加密的操作后，加密后的文件默认添加后缀名“.locked1”，勒索信文件名为“README2.html”，受害者可以通过唯一 ID 和邮箱与攻击者取得联系，赎金为 0.12btc。

**README2.html 勒索信文件内容如下所示：**

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-200779-1684727349.png)

**被加密后的文件系统如下所示：**

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-200779-1684727350.png)

**Tellyouthepass历史活动事件合集**

2020年7月借助永恒之蓝进行内网横向；

2021年12月借助OA软件的反序列化漏洞实施攻击；

2022年8月借助畅某某T+文件上传漏洞发动攻击；

2022年12月借助某友NC反序列化漏洞卷土重来，大量服务器已失陷；

2023年5月借助某友NC反序列化漏洞及某某通高危漏洞扩大攻击。

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-200779-1684727350.gif)

**事件排查**

**XDR日志排查**

通过AF接入SaaS XDR，云端检测到文件名为teccxaa.jsp的webshell执行成功，发现攻击IP：23.95.218.244

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-200779-1684727351.png)

通过XDR日志发现，存在内网主机爆破，但是并未成功。

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-200779-1684727355.png)

**排查**

通过查看排查，发现该IP为恶意。

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-200779-1684727358.png)

**智能运营平台排查**

通过对该攻击者的源 IP 分析，在智能运营平台同时发现了10+以上的客户被攻击，均检出了 webshell 加密通信。基本确定该攻击团伙要针对制造业、科技类攻击进行无差别攻击。

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-200779-1684727362.png)

**态势感知日志排查**

根据webshell文件名过滤，发现有黑客攻击及后门通信记录。

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-200779-1684727364.png)

根据攻击者 ip 过滤，发现黑客所利用的接口。云端专家通过对软件进行代码分析，发现存在一个高危漏洞，利用此漏洞可以执行任意代码，上传任意文件。在测试环境中完成该漏洞的复现，并报送监管单位。

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-200779-16847273641.png)

**安全人员分析及EDR产品联动**

安全人员根据日志查看webshell路径，发现其位于在某某通站点根目录，随后安全人员对此进行分析，发现类型为jsp，并采用了AES+BASE64加密。

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-200779-1684727365.png)

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-200779-1684727366.png)

应急团队收到客户勒索应急求助，经 EDR 确认，进程为 tomcat8.exe，黑客为了绕过勒索诱饵的防护将勒索程序注入到 tomcat 白进程中进行加密，EDR 的勒索行为AI引擎可针对白进程注入勒索进行防护，该进程对应某某通站点。通过勒索信息内容和加密后缀，确认该勒索病毒为 tellyoutheapss 勒索病毒，暂时没有公开解密工具。

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-200779-1684727368.png)

在受影响系统中同样在某某通根目录发现名称为teccxaa.jsp的webshell，推测该勒索病毒可能是通过该组件漏洞上传webshell，随后将勒索攻击模块注入到 tomcat8.exe 进程中执行加密操作。

为了最大化加密文件，避免文件被占用，确保不中断系统加密过程，该勒索软件在加密系统之前尝试终止特定的进程列表，这些进程大多属于数据库相关产品，需以防在加密文件的文件被如下进程所占用：

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-200779-1684727369.png)

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-200779-1684727370.gif)

**事件梳理与总结**

通过事件排查发现，此次攻击事件主要利用 某某通高危上传webshell，注入白进程tomcat8.exe，随后直接执行勒索加密模块，并无勒索文件“落地”，建议联系厂商打上最新补丁防止类似情况发生。

从确定受害主机到执行加密操作时间间隔较短，且并无明显上传扫描、信息收集等黑客攻击的痕迹，因而猜测此次勒索事件并无敏感数据外发的迹象。

**解决方案**

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-200779-1684727371.gif)

**处置建议**

**预防勒索攻击措施：**

 1、避免打开可疑或来历不明的邮件中的链接和附件；

 2、进行定期备份，并将这些备份保存在离线状态或单独的网络中；

 3、安装知名的防病毒和 Internet 安全软件包。

当遭遇勒索攻击后：

1、对受感染设备进行断网；

2、断开外部存储设备（如果已连接）；

3、检查系统日志中是否存在可疑事件。

**本文作者：[Further\_eye](newpage/author?author_id=9241)**

**本文为安全脉搏专栏作者发布，转载请注明：**[**https://www.secpulse.com/archives/200779.html**](https://www.secpulse.com/archives/200779.html)

Tags: [.locked1](https://www.secpulse.com/archives/tag/locked1)、[Log4j2 漏洞](https://www.secpulse.com/archives/tag/log4j2-%E6%BC%8F%E6%B4%9E)、[README2.html](https://www.secpulse.com/archives/tag/readme2-html)、[Shiro 反序列化漏洞](https://www.secpulse.com/archives/tag/shiro-%E5%8F%8D%E5%BA%8F%E5%88%97%E5%8C%96%E6%BC%8F%E6%B4%9E)、[Tellyouthepass](https://www.secpulse.com/archives/tag/tellyouthepass)、[勒索病毒](https://www.secpulse.com/archives/tag/%E5%8B%92%E7%B4%A2%E7%97%85%E6%AF%92)

点赞：
6
[评论：0](#goComment)
收藏：
0

*新浪微博
QQ空间
微信扫一扫*

### 相关文章

* [![【勒索防护】BabLock，游离于主流杀软之外的新型勒索病毒](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-200456-1684221051-300x175.png)

  【勒索防护】BabLock，游离于主流杀…](https://www.secpulse.com/archives/200456.html "详细阅读 【勒索防护】BabLock，游离于主流杀软之外的新型勒索病毒")
* [![【勒索防护】MSI 等多个企业已遭受攻击！MoneyMessage 勒索软件突现](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-199280-1681978319-300x158.png)

  【勒索防护】MSI 等多个企业已遭受攻击…](https://www.se...