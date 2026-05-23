---
title: 【安全事件】Apifox桌面客户端遭供应链投毒分析
url: https://blog.nsfocus.net/%e3%80%90%e5%ae%89%e5%85%a8%e4%ba%8b%e4%bb%b6%e3%80%91apifox%e6%a1%8c%e9%9d%a2%e5%ae%a2%e6%88%b7%e7%ab%af%e9%81%ad%e4%be%9b%e5%ba%94%e9%93%be%e6%8a%95%e6%af%92%e5%88%86%e6%9e%90/
source: 绿盟科技技术博客
date: 2026-05-22
fetch_date: 2026-05-23T05:40:56.882580
---

# 【安全事件】Apifox桌面客户端遭供应链投毒分析

* [登录](http://blog.nsfocus.net/wp-login.php)
* [注册](http://blog.nsfocus.net/wp-login.php?action=register)

[![Logo](http://blog.nsfocus.net/wp-content/uploads/2020/07/blog-logo.png)](https://blog.nsfocus.net/)

* [技术产品](https://blog.nsfocus.net/category/technology-product/)
* [数智安全](https://blog.nsfocus.net/category/digital-intelligence-secuirty/)
* [威胁通告](https://blog.nsfocus.net/category/threat-alert/)
* [研究调研](https://blog.nsfocus.net/category/security-research/)
* [洞见RSA](https://blog.nsfocus.net/category/rsac/)
* [公益译文](https://blog.nsfocus.net/category/translation/)
* [安全分享](https://blog.nsfocus.net/category/security-sharing/)

[![Logo](http://blog.nsfocus.net/wp-content/uploads/2020/07/blog-logo.png)](https://blog.nsfocus.net/)

* [技术产品](https://blog.nsfocus.net/category/technology-product/)
* [数智安全](https://blog.nsfocus.net/category/digital-intelligence-secuirty/)
* [威胁通告](https://blog.nsfocus.net/category/threat-alert/)
* [研究调研](https://blog.nsfocus.net/category/security-research/)
* [洞见RSA](https://blog.nsfocus.net/category/rsac/)
* [公益译文](https://blog.nsfocus.net/category/translation/)
* [安全分享](https://blog.nsfocus.net/category/security-sharing/)

# 【安全事件】Apifox桌面客户端遭供应链投毒分析

### 【安全事件】Apifox桌面客户端遭供应链投毒分析

[2026-05-22](https://blog.nsfocus.net/%E3%80%90%E5%AE%89%E5%85%A8%E4%BA%8B%E4%BB%B6%E3%80%91apifox%E6%A1%8C%E9%9D%A2%E5%AE%A2%E6%88%B7%E7%AB%AF%E9%81%AD%E4%BE%9B%E5%BA%94%E9%93%BE%E6%8A%95%E6%AF%92%E5%88%86%E6%9E%90/ "【安全事件】Apifox桌面客户端遭供应链投毒分析")[NSFOCUS](https://blog.nsfocus.net/author/zhengfangying/ "View all posts by NSFOCUS")

阅读： 35

### **通告编号:NS-2026-0007**

|  |  |
| --- | --- |
| **TA****G：** | **Apifox、供应链攻击、CDN投毒** |
| **危害程度：** | **高** |
| **版本：** | **1.0** |

### **1** **事件概述**

近日，绿盟科技CERT监测到Apifox官方CDN托管的前端JS文件遭受了供应链投毒，恶意脚本被植入经过多重混淆的JavaScript代码，Apifox桌面客户端启动后会自动加载，可窃取用户主机系统信息和SSH密钥、用户凭证等敏感数据，攻击者后续可控制主机执行后门程序实现远程命令执行。影响范围较大，请相关用户尽快采取措施进行排查与防护。

Apifox是一款功能强大的 API 协作开发平台，它将 API 文档、调试、Mock（模拟）、自动化测试等多个核心功能集成，为前端、后端、测试人员提供一个统一的工作平台。

参考链接：

https://mp.weixin.qq.com/s/GpACQdnhVNsMn51cm4hZig

### **2** **影响范围**

**受影响版本**

* Apifox公网SaaS版桌面客户端（Windows/macOS/Linux）<= 2.8.14

  注：在2026年3月4日至2026年3月22日期间使用了上述版本可能受影响。

**不受影响版本**

* Apifox客户端 >= 2.8.19
  注：SaaS Web版与私有化部署版不受此次事件影响

**3****事件时间线**

2026年3月4日：apifox.it.com DNS解析上线(Cloudflare托管)，CDN的JS文件被投毒

2026年3月22日：apifox.it.com DNS记录下线，域名停止解析

2026年3月23日：Apifox官方发布新版本修复此问题

2026年3月25日：Apifox官方针对事件发布安全公告

2026年3月26日：绿盟科技CERT发布分析文章

### **4** **漏洞防护事件分析**

**Apifox官方CDN托管的资源被恶意篡改**

Apifox在启动过程中会加载正常资源：

hxxps://cdn.apifox.com/www/assets/js/apifox-app-event-tracking.min.js

因未严格启用sandbox参数，且暴露了Node.js的API接口，导致攻击者可通过JavaScript控制Apifox的终端。

投毒恶意文件（Web Archive 还原）：

hxxps://web.archive.org/web/20260305051418/hxxps://cdn.apifox.com/www/assets/js/apifox-app-event-tracking.min.js

2026年3月4日至2026年3月22日期间（18天），攻击者通过 Cloudflare CDN向Apifox桌面客户端分发恶意载荷；恶意文件在原本正常的事件统计功能上，嵌入了可窃取信息和进行远程控制的代码。

**4.1 样本分析**

投毒的恶意文件为apifox-app-event-tracking.min.js，文件大小约77KB；

该文件由两部分组成：第一部分约34KB，为合法的Apifox事件追踪SDK，采用Webpack打包，包含GA4、百度统计、阿里云 SLS、PostHog等多平台事件追踪模块，本身无恶意行为；第二部分约42KB，为攻击者追加的恶意后门代码，经过严重混淆处理。利用Apifox客户端对事件追踪脚本的信任机制实现隐蔽植入。

恶意代码采用了多重混淆技术，使用javascript-obfuscator对恶意代码段进行字符串数组旋转，所有字符串通过RC4算法加密存储，再进行Base64编码，并通过代理函数增加间接调用层次；所有关键数字常量均使用多步运算表达，规避静态扫描；注入无效代码分支，增加分析干扰；具备反调试机制，检测到调试器则触发死循环。

完整还原后的恶意代码为Node.js脚本，具备远程代码执行能力，主要功能特点如下：

**RSA-2048私钥硬编码：**恶意代码中硬编码了一个RSA-2048私钥，采用PKCS#8格式，共1703字符。该私钥用于两个核心用途：一是加密上报，从私钥中提取公钥，使用publicEncrypt配合OAEP 填充加密敏感信息后附加到HTTP请求头；二是解密指令，使用privateDecrypt配合OAEP和SHA-256解密C2服务器下发的Stage-1 payload。攻击者将私钥嵌入客户端代码属于设计失误，使研究人员能够解密全部C2通信，还原完整攻击链。

**机器指纹采集：**恶意代码通过MAC地址、CPU 型号、主机名、用户主目录和操作系统平台五个字段构造机器唯一标识，将拼接字符串进行SHA-256哈希，得到64字符的十六进制指纹，存储在localStorage的\_rl\_mc 键中。

**Apifox用户凭证窃取：**恶意代码从localStorage读取 common.accessToken，即 Apifox 登录令牌，利用该令牌调用官方API获取用户信息，从响应中提取用户邮箱和姓名，经RSA加密后附加到后续请求头中。

**C2 通信协议：**恶意代码向C2服务器发送带有自定义HTTP头的请求，包含以下字段：

af\_uuid 为机器指纹SHA-256，明文传输；

af\_os 为操作系统类型与版本号，明文传输；

af\_user 为用户主目录路径，使用RSA-2048 OAEP加密；

af\_name为主机名，使用RSA-2048 OAEP加密；

af\_apifox\_user为 Apifox账户邮箱，使用RSA-2048 OAEP加密；

af\_apifox\_name为 Apifox账户姓名，使用RSA-2048 OAEP加密。

**远程代码执行：**恶意代码从C2获取 RSA 加密的payload，经私钥解密后使用 eval() 直接执行，实现完全的远程代码执行。这意味着攻击者每次轮询C2可下发不同载荷，后续攻击行为未知。

**持久化机制：**恶意代码执行完毕后，在30分钟至3小时的随机间隔后会重新执行整个流程。只要Apifox应用保持运行，恶意代码就会持续活跃。

**4.2 攻击流程**

1. Apifox启动，加载被投毒的event-tracking.min.js文件 (77KB)

2. 恶意代码执行：

   – 采集机器指纹（MAC地址、CPU信息及主机名，使用SHA-256处理）

   – 窃取Apifox访问令牌（accessToken），通过调用官方API获取用户邮箱

   – 使用RSA-2048算法加密敏感数据

3. 向C2服务器进行请求：GET /public/apifox-event.js

请求头包含af\_uuid、af\_os、af\_user、af\_name等字段

返回内容为经RSA加密的Stage-1加载程序（344字节）

4. 对Stage-1进行RSA解密并执行eval函数：

   – 动态创建<script>标签加载Stage-2

   – 加载路径为/<随机8位十六进制字符>.js（该URL为一次性链接，使用后返回404）

   – 加载完成后自动删除<script>标签

5. Stage-2执行(明文Node.js代码）：

v1版本功能collectPreInformations：

– 获取~/.ssh/目录下全部密钥文件

– 获取~/.zsh\_history与~/.bash\_history文件

– 获取~/.git-credentials文件

– 执行系统命令（ps aux或tasklist）

v2版本功能collectAddInformations：

– 获取~/.kube/目录下的K8s配置文件

– 获取~/.zshrc与~/.npmrc文件

– 获取~/.subversion/目录下的文件

– 执行目录树遍历操作

6. 数据外泄：

数据经JSON序列化→Gzip压缩→AES-256-GCM加密（密钥为apifox/foxapi）→Base64编码

POST /event/0/log (v1 数据)

POST /event/2/log (v2 数据)

请求头中af\_uuid字段值为代码中硬编码的机器指纹

7. 持久化机制：

以30分钟至3小时的随机间隔循环执行步骤3，重新向C2请求指令

每次轮询C2可返回完全不同的载荷内容

8. 后续阶段：未知

攻击者可根据信息筛选特定目标，定制攻击脚本与定向入侵，包括但不限于横向移动、K8s集群接管、二次投毒等。

### **5** **风险排查**

检查2026年3月4日至2026年3月22日期间是否使用了Apifox桌面客户端，可使用Apifox后门扫描工具（可通过邮箱或后台留言获取）进行检测：

![](https://blog.nsfocus.net/wp-content/uploads/2026/05/水水水水水水水水水水水水-300x166.png)

    若在受影响范围，请采取下列措施进行处理：

1、立即停用当前Apifox桌面端应用，下载安装安全版本或替代工具

2、吊销历史 accessToken，并轮换所有密钥和用户凭证

3、检查Apifox账户是否存在异常登录，并修改账户密码

4、清除Apifox客户端的localStorage，删除\_rl\_headers和\_rl\_mc键：

|  |
| --- |
| localStorage.removeItem(‘\_rl\_headers’);localStorage.removeItem(‘\_rl\_mc’); |

5、阻断攻击者恶意域名，在host文件中增加配置：127.0.0.1 apifox.it.com

6、审查服务器登录日志与敏感文件，检查是否有异常登录和后门遗留

### **6** **总结与建议**

目前Apifox官方已发布新版本修复了此问题，请受影响的用户尽快更新进行防护，下载链接：https://docs.apifox.com/download

此次事件凸显了软件供应链安全的严峻挑战，攻击者利用CDN基础设施的信任机制，实现了对下游用户的大规模影响，单位需建立完善的供应链安全监控体系应对此类风险。

**安全加固建议：**

1、Apifox启用Electron sandbox 模式，限制渲染进程的 Node.js API 访问；

2、对远程加载的JS文件实施 Subresource Integrity (SRI) 校验；

3、建立CDN资源的文件完整性监控机制；

4、对开发工具类软件的网络通信进行审计；

**7****IOCs**

相关用户可根据以下IoC进行排查与封禁：

**恶意文件**

文件名: apifox-app-event-tracking.min.js

SHA256: 91d48ee33a92acef02d8c8153d1de7e7fe8ffa0f3b6e5cebfcb80b3eeebc94f1

**恶意域名**

apifox.it.com

\*.apifox.it.com

**恶意URL**

hxxp[:]//cdn.apifox.com/www/assets/js/apifox-app-event-tracking.min.js

hxxp[:]//cdn.apifox.com/www/assets/js/user-tracking.min.js

### **最后的宣传彩蛋：**

**安全情报通告服务：**

绿盟科技CERT日常监控国内外上百家主流软件厂商、数十家安全论坛与漏洞社区，结合每日应急安全事件和私域运营进行情报生产，并根据情报评级、PoC披露情况、产品使用流行度、实际利用价值、网空资产测绘数据等多个维度进行综合评估，及时推送最新重大安全漏洞情况及安全事件给客户，整合公司的研究、产品、服务等能力，针对突发性威胁制定可落地的安全防护方案，在威胁事件爆发之前协助客户及时发现问题，采取相关防护措施，保护用户信息系统安全，提升企业应对威胁的能力。

**凭据泄露监测服务：**

近年来，攻击者经常会通过购买或各种手段获取目标用户的登录凭据，进而突破系统入口开展后续攻击，目前主要被用于加密勒索等高威胁场景。为帮助客户能够快速识别自身敏感凭据的泄露风险，绿盟科技特此推出凭据泄露监测服务。此服务以SaaS方式提供，通过7×24小时持续监测数十万数据泄露渠道，结合AI驱动的数据关联分析，当检测到与客户相关的凭据泄露风险后，及时向客户进行预警。

注：对上述服务感兴趣的客户可通过联系绿盟当地区域同事或发送邮件至cert@nsfocus.com咨询交流。

**绿盟科技应急响应中心（NSFOCUS CERT）致力于为客户提供及时、专业、高效的情报预警与应急服务，针对高危漏洞与安全事件进行快速响应，提供可落地的解决方案。**

**END**

**声明**

本安全公告仅用来描述可能存在的安全问题，绿盟科技不为此安全公告提供任何保证或承诺。由于传播、利用此安全公告所提供的信息而造成的任何直接或者间接的后果及损失，均由使用者本人负责，绿盟科技以及安全公告作者不为此承担任何责任。

绿盟科技拥有对此安全公告的修改和解释权。如欲转载或传播此安全公告，必须保证此安全公告的完整性，包括版权声明等全部内容。未经绿盟科技允许，不得任意修改或者增减此安全公告内容，不得以任何方式将其用于商业目的。

Spread the word. Share this post!

[Previous](https://blog.nsfocus.net/%E3%80%90%E5%AE%89%E5%85%A8%E4%BA%8B%E4%BB%B6%E3%80%91ai%E5%9F%BA%E7%A1%80%E8%AE%BE%E6%96%BDlitellm%E4%BE%9B%E5%BA%94%E9%93%BE%E6%8A%95%E6%AF%92%E9%A2%84%E8%AD%A6%E9%80%9A%E5%91%8A/)

[Next](https://blog.nsfocus.net/%E3%80%90%E5%AE%89%E5%85%A8%E6%9B%B4%E6%96%B0%E3%80%91%E5%BE%AE%E8%BD%AF3%E6%9C%88%E5%AE%89%E5%85%A8%E6%9B%B4%E6%96%B0%E5%A4%9A%E4%B8%AA%E4%BA%A7%E5%93%81%E9%AB%98%E5%8D%B1%E6%BC%8F%E6%B4%9E%E9%80%9A/)

### Meet The Author

NSFOCUS

咨询与合作：nsmagazine@nsfocus.com

* [绿盟科技官网](https://www.nsfocus.com.cn)
* [绿盟威胁情报中心（NTI）](https://nti.nsfocus.com)
* [绿盟云](https://cloud.nsfocus.com)