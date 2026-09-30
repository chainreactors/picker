---
title: Fastjson 2.x远程代码执行漏洞通告
url: https://blog.nsfocus.net/fastjson-2-x%e8%bf%9c%e7%a8%8b%e4%bb%a3%e7%a0%81%e6%89%a7%e8%a1%8c%e6%bc%8f%e6%b4%9e%e9%80%9a%e5%91%8a/
source: 绿盟科技技术博客
date: 2026-09-29
fetch_date: 2026-09-30T07:42:38.300529
---

# Fastjson 2.x远程代码执行漏洞通告

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
* Fastjson 2.x远程代码执行漏洞通告

# Fastjson 2.x远程代码执行漏洞通告

[0](https://blog.nsfocus.net/fastjson-2-x%E8%BF%9C%E7%A8%8B%E4%BB%A3%E7%A0%81%E6%89%A7%E8%A1%8C%E6%BC%8F%E6%B4%9E%E9%80%9A%E5%91%8A/#comments)

![](https://secure.gravatar.com/avatar/99bcec439a2a5078218073d2459e8069eb89b5ce5cbf840afef1c3ed7395d75c?s=40&d=identicon&r=g) [NSFOCUS](https://blog.nsfocus.net/author/zhengfangying/ "written 2026-09-2914:51") 发布于 1 天前

![](https://blog.nsfocus.net/wp-content/uploads/2026/06/7.png)

阅读： 31

|  |  |  |  |
| --- | --- | --- | --- |
| **■ 通告编号** | **NS-20****2****6****-00****20** | ■ 发布日期 | **202****6****–****07****–****27** |
| **■ 漏洞危害** | **攻击者利用此漏洞，****可实现远程代码执行****。** | | |
| **■ TAG** | **Fastjson****、反序列化、****autoType****绕过** | | |

### ****一********.********漏洞概述****

近日，绿盟科技CERT监测到网上披露了Fastjson 2.x远程代码执行漏洞；由于Fastjson2.x在默认配置未启用SupportAutoType时仍可能通过内置白名单处理JSON中的@type，未经身份验证的攻击者可构造特制的恶意JSON数据，无需目标服务存在任何第三方危险类即可实现远程代码执行。CVSS评分9.8，目前已有漏洞细节披露，请相关用户尽快采取措施进行防护。

Fastjson是阿里巴巴开源的JSON解析库，它可以解析JSON格式的字符串，支持将Java Bean序列化为JSON字符串，也可以从JSON字符串反序列化到JavaBean；具有执行效率高的特点，应用范围广泛。

参考链接：

https://github.com/alibaba/fastjson2/issues/7702

###

### ****二********.********影响范围****

**受影响版本**

* Fastjson2.x <= 2.0.62

**注：**官方在Fastjson 1.2.68及之后的版本中添加了SafeMode功能，可完全禁用autoType。

**不受影响版本**

* Fastjson2.x >0.62

### ****三********.********漏洞检测****

****3.1********人工排查****

相关用户可使用以下命令检测当前使用的 Fastjson 版本：

|  |
| --- |
| lsof | grep fastjson |

或查找项目目录中的文件是否存在 fastjson-[version].jar 文件。

使用 maven 打包的项目可通过 pom.xml 查看当前使用的 fastjson 版本：

若当前版本在受影响范围内，且未开启 SafeMode 则存在安全风险。

### ****四********.********漏洞防护****

****4.1********官方升级****

目前官方已发布安全补丁修复此漏洞，建议受影响用户尽快更新进行防护，下载链接：https://github.com/alibaba/fastjson2/pull/7695/changes

****4.2********其他防护措施****

若相关用户暂时无法进行升级操作，也可使用下列措施进行临时缓解：

1、Fastjson 在 1.2.68 及之后的版本中引入了 safeMode 安全模式，配置 safeMode 后无论白名单和黑名单都不支持 autoType ，可杜绝反序列化漏洞攻击；三种开启 SafeMode 的方式如下：

1. 在代码中配置：

|  |
| --- |
| ParserConfig.getGlobalInstance().setSafeMode(true); |

2. 加上JVM启动参数：

|  |
| --- |
| -Dfastjson.parser.safeMode=true |

如果有多个包名前缀，可用逗号隔开。

3. 通过<fastjson.properties>文件配置：

通过类路径的 <fastjson.properties> 文件来配置，配置方式如下：

|  |
| --- |
| fastjson.parser.safeMode=true |

参考官方文档：[https://github.com/alibaba/fastjson/wiki/fastjson\_safemode](https://github.com/alibaba/fastjson/wiki/fastjson_safemode2)

[2](https://github.com/alibaba/fastjson/wiki/fastjson_safemode2)、使用WAF 等安全设备拦截请求体中 key 包含@type 字段的 JSON 数据，需同时覆盖URL 参数和请求体并注意编码绕过。

****4.3********产品防护****

绿盟科技 WEB应用防护系统（WAF）、网络入侵防护系统（IPS）与绿盟综合威胁探针（UTS）历史规则支持此漏洞防护，请相关用户升级规则包至最新版，以形成安全产品防护能力。

### ****声明****

本安全公告仅用来描述可能存在的安全问题，绿盟科技不为此安全公告提供任何保证或承诺。由于传播、利用此安全公告所提供的信息而造成的任何直接或者间接的后果及损失，均由使用者本人负责，绿盟科技以及安全公告作者不为此承担任何责任。

绿盟科技拥有对此安全公告的修改和解释权。如欲转载或传播此安全公告，必须保证此安全公告的完整性，包括版权声明等全部内容。未经绿盟科技允许，不得任意修改或者增减此安全公告内容，不得以任何方式将其用于商业目的。

最后修改日期: 2026-09-29

### 作者

![](https://secure.gravatar.com/avatar/99bcec439a2a5078218073d2459e8069eb89b5ce5cbf840afef1c3ed7395d75c?s=96&d=identicon&r=g)

[NSFOCUS](https://blog.nsfocus.net/author/zhengfangying/)

## 最新发布

* [四次进化，绿盟科技将开拓怎样的安全新境？](https://blog.nsfocus.net/%E5%9B%9B%E6%AC%A1%E8%BF%9B%E5%8C%96%EF%BC%8C%E7%BB%BF%E7%9B%9F%E7%A7%91%E6%8A%80%E5%B0%86%E5%BC%80%E6%8B%93%E6%80%8E%E6%A0%B7%E7%9A%84%E5%AE%89%E5%85%A8%E6%96%B0%E5%A2%83%EF%BC%9F/)
* [微软9月安全更新多个产品高危漏洞通告](https://blog.nsfocus.net/%E5%BE%AE%E8%BD%AF9%E6%9C%88%E5%AE%89%E5%85%A8%E6%9B%B4%E6%96%B0%E5%A4%9A%E4%B8%AA%E4%BA%A7%E5%93%81%E9%AB%98%E5%8D%B1%E6%BC%8F%E6%B4%9E%E9%80%9A%E5%91%8A/)
* [微软8月安全更新多个产品高危漏洞通告](https://blog.nsfocus.net/%E5%BE%AE%E8%BD%AF8%E6%9C%88%E5%AE%89%E5%85%A8%E6%9B%B4%E6%96%B0%E5%A4%9A%E4%B8%AA%E4%BA%A7%E5%93%81%E9%AB%98%E5%8D%B1%E6%BC%8F%E6%B4%9E%E9%80%9A%E5%91%8A/)
* [Fastjson 2.x远程代码执行漏洞通告](https://blog.nsfocus.net/fastjson-2-x%E8%BF%9C%E7%A8%8B%E4%BB%A3%E7%A0%81%E6%89%A7%E8%A1%8C%E6%BC%8F%E6%B4%9E%E9%80%9A%E5%91%8A/)
* [Fastjson 1.2.x无需gadget远程代码执行漏洞通告](https://blog.nsfocus.net/fastjson-1-2-x%E6%97%A0%E9%9C%80gadget%E8%BF%9C%E7%A8%8B%E4%BB%A3%E7%A0%81%E6%89%A7%E8%A1%8C%E6%BC%8F%E6%B4%9E%E9%80%9A%E5%91%8A/)

## 文章导航

[上一篇文章 Fastjson 1.2.x无需gadget远程代码执行漏洞通告](https://blog.nsfocus.net/fastjson-1-2-x%E6%97%A0%E9%9C%80gadget%E8%BF%9C%E7%A8%8B%E4%BB%A3%E7%A0%81%E6%89%A7%E8%A1%8C%E6%BC%8F%E6%B4%9E%E9%80%9A%E5%91%8A/)

[下一篇文章 微软8月安全更新多个产品高危漏洞通告](https://blog.nsfocus.net/%E5%BE%AE%E8%BD%AF8%E6%9C%88%E5%AE%89%E5%85%A8%E6%9B%B4%E6%96%B0%E5%A4%9A%E4%B8%AA%E4%BA%A7%E5%93%81%E9%AB%98%E5%8D%B1%E6%BC%8F%E6%B4%9E%E9%80%9A%E5%91%8A/)

著作权 © 2026 **[绿盟科技技术博客](https://blog.nsfocus.net/)**. 保留一切权利。 本站采用的布景主题为 [Mynote](https://terryl.in/).