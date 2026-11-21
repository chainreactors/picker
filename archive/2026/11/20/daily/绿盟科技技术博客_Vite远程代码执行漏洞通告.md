---
title: Vite远程代码执行漏洞通告
url: https://blog.nsfocus.net/vite%e8%bf%9c%e7%a8%8b%e4%bb%a3%e7%a0%81%e6%89%a7%e8%a1%8c%e6%bc%8f%e6%b4%9e%e9%80%9a%e5%91%8a/
source: 绿盟科技技术博客
date: 2026-11-20
fetch_date: 2026-11-21T09:00:43.673067
---

# Vite远程代码执行漏洞通告

* [技术产品](https://blog.nsfocus.net/category/technology-product/)
* [数智安全](https://blog.nsfocus.net/category/digital-intelligence-secuirty/)
* [威胁通告](https://blog.nsfocus.net/category/threat-alert/)
* [研究调研](https://blog.nsfocus.net/category/security-research/)
* [洞见RSA](https://blog.nsfocus.net/category/rsac/)
* [公益译文](https://blog.nsfocus.net/category/translation/)
* [安全分享](https://blog.nsfocus.net/category/security-sharing/)
* [登录](https://blog.nsfocus.net/wp-login.php)

* [首页](https://blog.nsfocus.net)
* [威胁通告](https://blog.nsfocus.net/category/threat-alert/)
* Vite远程代码执行漏洞通告

# Vite远程代码执行漏洞通告

[0](https://blog.nsfocus.net/vite%E8%BF%9C%E7%A8%8B%E4%BB%A3%E7%A0%81%E6%89%A7%E8%A1%8C%E6%BC%8F%E6%B4%9E%E9%80%9A%E5%91%8A/#comments)

![](https://secure.gravatar.com/avatar/99bcec439a2a5078218073d2459e8069eb89b5ce5cbf840afef1c3ed7395d75c?s=40&d=identicon&r=g) [NSFOCUS](https://blog.nsfocus.net/author/zhengfangying/ "written 2026-11-2015:40") 发布于 1 天前

![](https://blog.nsfocus.net/wp-content/uploads/2026/05/mmm.jpg)

阅读： 55

|  |  |  |  |
| --- | --- | --- | --- |
| Vite远程代码执行漏洞通告 | | | |
| ■ 通告编号 | **NS-2026-0034** | ■ 发布日期 | **2026-11-19** |
| ■ 漏洞危害 | **攻击者利用此漏洞，可造成任意文件读取和远程代码执行。** | | |
| ■ TAG | **Vite、远程代码执行** | | |

# 漏洞概述

近日，绿盟科技CERT监测到Vite发布安全公告，修复了Vite远程代码执行漏洞；由于Vite的\_\_vite-browser-external和\_\_vite-optional-peer-dep虚拟模块未对来源于URL的模块ID进行转义，未经身份验证的攻击者可通过发送特制的HTTP请求注入恶意JavaScript代码进行任意文件读取，并利用new Worker和import.meta.glob相关模块代码的eval处理绕过变量限制在目标服务器上执行任意代码。CVSS评分9.1，目前漏洞细节与PoC已公开，请相关用户尽快采取措施进行防护。

Vite是一款现代化的前端开发与构建工具，提供极速的开发服务器启动速度和高效的热更新机制，支持多框架开发，如Vue、React等。其开发服务器默认仅绑定`localhost`，但可通过配置显式开放至局域网或公网。

参考链接：

https://github.com/vitejs/vite/security/advisories/GHSA-p4f5-76q4-ffq7

# 影响范围

**受影响版本**

* 4.0.0 <= Vite <= 6.4.5
* 7.0.0 <= Vite <= 7.3.7
* 8.0.0 <= Vite <= 8.1.6
* 8.2.0 <= Vite <= 8.2.4
* 8.3.0 <= Vite <= 8.3.6
* Vite-plus <= 1.5.0

注：影响将Vite开发服务器暴露到网络（启用–host或配置server.host）的应用。

**不受影响版本**

* Vite 6.x >= 6.4.6
* Vite 7.x >= 7.3.8
* Vite 8.1.x >= 8.1.7
* Vite 8.2.x >= 8.2.5
* Vite 8.3.x >= 8.3.7
* Vite-plus >= 1.5.1

# 漏洞检测

人工检测

相关用户可以通过检查项目依赖版本及开发服务器网络配置，判断当前Vite或Vite-plus是否在受影响范围内：

1、查看项目安装的Vite版本

在项目根目录使用下列命令查看当前使用的版本，也可直接查看package.json及锁文件中的版本号。

|  |
| --- |
| npm ls vite –all npm ls vite-plus –all |

1. 检查开发服务器网络配置

查看项目中的Vite配置文件、package.json脚本及其他启动脚本：

|  |
| --- |
| find . -name ‘vite.config.’ -not -path ‘/node\_modules/\*’  grep -RInE –exclude-dir=node\_modules –exclude-dir=.git — ‘–host([ =]|$)|host[[:space:]]\*:’ . |

3、检查运行进程及是否使用–host参数启动

使用命令查看正在运行的相关进程及启动参数：

|  |
| --- |
| ps -ef | grep -iE ‘vite|vite-plus|vp’ | grep -v grep |

若当前使用的Vite或Vite-plus版本在受影响范围内，且开发服务器通过–host参数或server.host配置等方式暴露到非本机网络，则可能存在安全风险。

# 漏洞防护

官方升级

目前官方已发布新版本修复此漏洞，请受影响的用户尽快升级版本进行防护。Vite下载链接：https://github.com/vitejs/vite/releases；vite-plus下载链接：https://www.npmjs.com/package/vite-plus

其他防护措施

在不影响业务的情况下，相关用户可通过对Vite开发服务器进行访问限制来临时缓解：

1、禁止将开发服务器绑定到对外网络地址

删除配置server.host或将其显式设为localhost，使其仅允许本机访问。

|  |
| --- |
| // vite.config.js export default {  server: {  host: ‘localhost’  }  } |

2、启动Vite开发服务器时避免添加–host参数，检查package.json中的启动脚本及其他实际启动命令，确保其中未包含–host参数。

# 声明

本安全公告仅用来描述可能存在的安全问题，绿盟科技不为此安全公告提供任何保证或承诺。由于传播、利用此安全公告所提供的信息而造成的任何直接或者间接的后果及损失，均由使用者本人负责，绿盟科技以及安全公告作者不为此承担任何责任。

绿盟科技拥有对此安全公告的修改和解释权。如欲转载或传播此安全公告，必须保证此安全公告的完整性，包括版权声明等全部内容。未经绿盟科技允许，不得任意修改或者增减此安全公告内容，不得以任何方式将其用于商业目的。

最后修改日期: 2026-11-20

### 作者

![](https://secure.gravatar.com/avatar/99bcec439a2a5078218073d2459e8069eb89b5ce5cbf840afef1c3ed7395d75c?s=96&d=identicon&r=g)

[NSFOCUS](https://blog.nsfocus.net/author/zhengfangying/)

## 最新发布

* [绿盟科技受邀出席首届交通运输数智化发展大会，以“AI对抗AI”筑牢行业网络安全防线](https://blog.nsfocus.net/%E7%BB%BF%E7%9B%9F%E7%A7%91%E6%8A%80%E5%8F%97%E9%82%80%E5%87%BA%E5%B8%AD%E9%A6%96%E5%B1%8A%E4%BA%A4%E9%80%9A%E8%BF%90%E8%BE%93%E6%95%B0%E6%99%BA%E5%8C%96%E5%8F%91%E5%B1%95%E5%A4%A7%E4%BC%9A%EF%BC%8C/)
* [VMware vCenter身份验证绕过漏洞（CVE-2026-123890）通告](https://blog.nsfocus.net/vmware-vcenter%E8%BA%AB%E4%BB%BD%E9%AA%8C%E8%AF%81%E7%BB%95%E8%BF%87%E6%BC%8F%E6%B4%9E%EF%BC%88cve-2026-123890%EF%BC%89%E9%80%9A%E5%91%8A/)
* [Ruby远程代码执行漏洞（CVE-2026-132825）通告](https://blog.nsfocus.net/ruby%E8%BF%9C%E7%A8%8B%E4%BB%A3%E7%A0%81%E6%89%A7%E8%A1%8C%E6%BC%8F%E6%B4%9E%EF%BC%88cve-2026-132825%EF%BC%89%E9%80%9A%E5%91%8A/)
* [PHP远程代码执行漏洞（CVE-2026-126714）通告](https://blog.nsfocus.net/php%E8%BF%9C%E7%A8%8B%E4%BB%A3%E7%A0%81%E6%89%A7%E8%A1%8C%E6%BC%8F%E6%B4%9E%EF%BC%88cve-2026-126714%EF%BC%89%E9%80%9A%E5%91%8A/)
* [Vite远程代码执行漏洞通告](https://blog.nsfocus.net/vite%E8%BF%9C%E7%A8%8B%E4%BB%A3%E7%A0%81%E6%89%A7%E8%A1%8C%E6%BC%8F%E6%B4%9E%E9%80%9A%E5%91%8A/)

## 文章导航

[上一篇文章 Nginx多个远程代码执行漏洞（CVE-2026-123007/CVE-2026-123634/CVE-2026-123633/CVE-2026-121810/CVE-2026-113425）通告](https://blog.nsfocus.net/nginx%E5%A4%9A%E4%B8%AA%E8%BF%9C%E7%A8%8B%E4%BB%A3%E7%A0%81%E6%89%A7%E8%A1%8C%E6%BC%8F%E6%B4%9E%EF%BC%88cve-2026-123007-cve-2026-123634-cve-2026-123633-cve-2026-121810-cve-2026-113425%EF%BC%89/)

[下一篇文章 PHP远程代码执行漏洞（CVE-2026-126714）通告](https://blog.nsfocus.net/php%E8%BF%9C%E7%A8%8B%E4%BB%A3%E7%A0%81%E6%89%A7%E8%A1%8C%E6%BC%8F%E6%B4%9E%EF%BC%88cve-2026-126714%EF%BC%89%E9%80%9A%E5%91%8A/)

著作权 © 2026 **[绿盟科技技术博客](https://blog.nsfocus.net/)**. 保留一切权利。 本站采用的布景主题为 [Mynote](https://terryl.in/).