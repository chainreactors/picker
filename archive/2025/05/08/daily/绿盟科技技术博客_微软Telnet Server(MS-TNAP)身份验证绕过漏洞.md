---
title: 微软Telnet Server(MS-TNAP)身份验证绕过漏洞
url: https://blog.nsfocus.net/telnet-serverms-tnap/
source: 绿盟科技技术博客
date: 2025-05-08
fetch_date: 2025-10-06T22:28:30.149321
---

# 微软Telnet Server(MS-TNAP)身份验证绕过漏洞

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

# 微软Telnet Server(MS-TNAP)身份验证绕过漏洞

### 微软Telnet Server(MS-TNAP)身份验证绕过漏洞

[2025-05-07](https://blog.nsfocus.net/telnet-serverms-tnap/ "微软Telnet Server(MS-TNAP)身份验证绕过漏洞")[NSFOCUS](https://blog.nsfocus.net/author/zhengfangying/ "View all posts by NSFOCUS")

阅读： 1,595

****一、漏洞概述****

近日，绿盟科技CERT监测到网上披露了微软Telnet Server(MS-TNAP)身份验证绕过漏洞，由于Telnet Server在处理NTLM（NT LAN Manager）认证流程时配置错误，在认证握手阶段设置了存在缺陷的SSPI（安全支持提供程序接口）标志；未经身份验证的攻击者可利用Guest账户绕过登录限制，获取包括管理员在内的任意用户访问权限。目前漏洞PoC已公开，请相关用户尽快采取措施进行防护。

漏洞利用：

* 使用特定标志请求双向认证
* 在客户端使用管理员账户的NULL空密码
* 设置特定SSPI标志触发服务器NTLM认证逻辑缺陷
* 发送经过篡改的NTLM Type 3类型消息欺骗服务器
* 绕过身份验证，开启具有管理员权限的Telnet会话

****影响范围****

**受影响版本**

* Windows 2000
* Windows XP
* Windows Vista
* Windows 7
* Windows Server 2003
* Windows Server 2008
* Windows Server 2008 R2

****三、暴露面排查****

绿盟科技自动化渗透测试工具（EZ）即将支持Telnet Server(MS-TNAP)的识别检测（注：企业版请联系绿盟销售人员获取）。

工具下载链接：https://github.com/m-sec-org/EZ/releases

新用户请注册M-SEC社区（https://msec.nsfocus.com）申请证书进行使用：

****四、漏洞防护****

* + **临时防护措施**

目前微软官方暂未发布修复措施与补丁，建议相关用户尽快采取下列措施进行临时防护：

* 禁用Telnet服务器系统上的Guest账户；
* 在Telnet服务器上禁用NTLM认证协议；
* 禁用受影响系统上的Telnet Server服务，用SSH等替代；
* 实施网络层过滤，仅允许可信IP和网络访问Telnet服务；
* 应用控制策略阻止未经授权的Telnet客户端连接；

****声明****

本安全公告仅用来描述可能存在的安全问题，绿盟科技不为此安全公告提供任何保证或承诺。由于传播、利用此安全公告所提供的信息而造成的任何直接或者间接的后果及损失，均由使用者本人负责，绿盟科技以及安全公告作者不为此承担任何责任。

绿盟科技拥有对此安全公告的修改和解释权。如欲转载或传播此安全公告，必须保证此安全公告的完整性，包括版权声明等全部内容。未经绿盟科技允许，不得任意修改或者增减此安全公告内容，不得以任何方式将其用于商业目的。&nbsp

Spread the word. Share this post!

[Previous](https://blog.nsfocus.net/11-2/)

[Next](https://blog.nsfocus.net/elastic-kibana/)

### Meet The Author

NSFOCUS

咨询与合作：nsmagazine@nsfocus.com

* [绿盟科技官网](https://www.nsfocus.com.cn)
* [绿盟威胁情报中心（NTI）](https://nti.nsfocus.com)
* [绿盟云](https://cloud.nsfocus.com)