---
title: Ghost Bits 幽灵比特绕过攻击爆发！你的IPS可能已失效
url: https://blog.nsfocus.net/ghost-bits-%e5%b9%bd%e7%81%b5%e6%af%94%e7%89%b9%e7%bb%95%e8%bf%87%e6%94%bb%e5%87%bb%e7%88%86%e5%8f%91%ef%bc%81%e4%bd%a0%e7%9a%84ips%e5%8f%af%e8%83%bd%e5%b7%b2%e5%a4%b1%e6%95%88/
source: 绿盟科技技术博客
date: 2026-05-15
fetch_date: 2026-05-16T05:14:20.935180
---

# Ghost Bits 幽灵比特绕过攻击爆发！你的IPS可能已失效

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

# Ghost Bits 幽灵比特绕过攻击爆发！你的IPS可能已失效

### Ghost Bits 幽灵比特绕过攻击爆发！你的IPS可能已失效

[2026-05-15](https://blog.nsfocus.net/ghost-bits-%E5%B9%BD%E7%81%B5%E6%AF%94%E7%89%B9%E7%BB%95%E8%BF%87%E6%94%BB%E5%87%BB%E7%88%86%E5%8F%91%EF%BC%81%E4%BD%A0%E7%9A%84ips%E5%8F%AF%E8%83%BD%E5%B7%B2%E5%A4%B1%E6%95%88/ "Ghost Bits 幽灵比特绕过攻击爆发！你的IPS可能已失效")[NSFOCUS](https://blog.nsfocus.net/author/zhengfangying/ "View all posts by NSFOCUS")

阅读： 31

### 网安圈最新高危风险：Ghost Bits（幽灵比特）编码绕过

安全检测环节判定为正常字符，后端执行却变为攻击 Payload。这样语义不一致问题，正成为 Web 防护致命缺口，对各类网络应用及核心资产构成严重威胁。

近期，业内披露了与 Ghost Bits相关的输入语义偏差风险。该风险的核心在于：安全检测链路与应用执行链路对同一输入的编码解释不一致，可能导致前置防护判定为无害，而后端执行阶段恢复为高风险语义。该问题本质属于“端到端语义不一致”而非单一组件缺陷。

### 什么是 Ghost Bits？

Ghost Bits（幽灵比特）可理解为：在字符到字节的收窄转换中，被静默丢弃但影响安全语义的高位比特。

以 Java 为例：

– char 是 16 位（UTF-16 code unit）

– byte 是 8 位

– 当代码出现 (byte) ch、ch & 0xFF、write(int) 仅写低 8 位等行为时，高 8 位会被丢弃

这意味着一个 Unicode 字符在某些链路里会“退化”为另一个字节值。攻击者可利用这种差异构造“前后语义不一致”的输入：前置检测看到A，后端执行却是B。

### 攻击者怎么绕过？

攻击者利用“高位静默丢弃”这一特性，将攻击的payload中关键ASCII字符经过精心构造的Unicode字符替换(低8位与payload保持一致)，IPS看到的Unicode字符是无害的字符，而到后端Java服务器解码时高位截断只选取低位从而还原成攻击载荷，从而绕过IPS检测，并能真正执行命令。

### 能触发哪些高危漏洞？

![](https://p3-sign.toutiaoimg.com/tos-cn-i-6w9my0ksvp/0bfe0b6ca43f45d3b11476d2d148b308~tplv-tt-shrink:640:0.image?lk3s=06827d14&traceid=202605151730126B7DFA500B3A79CFE84B&x-expires=2147483647&x-signature=XdM0HA%2BGI4QtOx2GriMXBI69qI8%3D)

### 绿盟 IPS 解决方案

绿盟IPS 引擎版本V5.6R11F08（支持编解码功能的设备）及以上支持Unicode类型的Ghost Bits编码绕过检测；默认配置下关闭，可按照下面配置后**重启检测引擎**生效（开启解码功能对性能有5-10%左右影响，与流量强相关）：

![](https://p26-sign.toutiaoimg.com/tos-cn-i-6w9my0ksvp/d14ac3d4e44a4850957da2d46394cdb3~tplv-tt-shrink:640:0.image?lk3s=06827d14&traceid=202605151730126B7DFA500B3A79CFE84B&x-expires=2147483647&x-signature=GRYLWBQ1YNQ0RhgwnAskGQKhsXk%3D)

以SQL注入检测为例

Unicode编码类型:

Payload: 1 or 1=1

Unicode编码后payload: %u0031%u0020%u006F%u0072%u0020%u0031%u003D%u0031

Ghost Bits编码后

payload: %u0131%u0120%u016F%u0172%u0120%u0131%u013D%u0131

pcap包：

![](https://p26-sign.toutiaoimg.com/tos-cn-i-6w9my0ksvp/9f83eb4d4c8a43bd9042d99117455957~tplv-tt-shrink:640:0.image?lk3s=06827d14&traceid=202605151730126B7DFA500B3A79CFE84B&x-expires=2147483647&x-signature=LubUyIJEfWryx%2BDj3w%2BVTDeq%2Be4%3D)

产品侧告警：

![](https://p3-sign.toutiaoimg.com/tos-cn-i-6w9my0ksvp/4b61718e61e448e9bccb116d3691d03d~tplv-tt-shrink:640:0.image?lk3s=06827d14&traceid=202605151730126B7DFA500B3A79CFE84B&x-expires=2147483647&x-signature=CKM8u5xGiQoKas9XQRtlt8eS%2BVw%3D)

### 业务 / 服务器必做加固

**统一编码：**全链路 UTF-8，禁止自动猜编码

**输入规范化：**Unicode 标准化，对高风险字段（用户名、文件名、SQL相关参数、路径）做 字符集白名单；明确拒绝“不可见控制字符”“异常混淆字符”“超预期字符集”。

**数据库兜底：**强制参数化查询，防注入最后防线

**代码审计：**删掉(byte)ch、ch & 0xFF、baos.write(ch)、DataOutputStream#writeBytes()等危险写法。应使用指定编码方式的写法处理文件。

**收敛访问：**公网服务限制访问源

Ghost Bits攻击的核心是检测与执行链路的端到端语义不一致，并非单一设备漏洞。绿盟科技建议各用户通过“设备升级+业务加固”双管齐下，彻底封堵安全缺口，保障企业网络与核心业务安全。绿盟科技也将持续跟进风险态势，优化防护方案，提供专业安全支撑。

Spread the word. Share this post!

[Previous](https://blog.nsfocus.net/%E5%9B%BD%E9%99%85%E8%AE%A4%E5%8F%AF-%E7%BB%BF%E7%9B%9F%E7%A7%91%E6%8A%80%E5%85%A5%E9%80%89gartner%E3%80%8A%E7%BD%91%E7%BB%9C%E5%A8%81%E8%83%81%E6%83%85%E6%8A%A5%E6%8A%80%E6%9C%AF%E9%AD%94/)

[Next](https://blog.nsfocus.net/%E6%97%A0%E9%9C%80%E4%B8%8B%E8%BD%BD%EF%BC%81%E9%92%89%E9%92%89%E5%8A%A0%E5%AF%86%E6%96%87%E4%BB%B6%E5%8F%AF%E5%9C%A8%E7%BA%BF%E8%A7%A3%E5%AF%86%E9%A2%84%E8%A7%88/)

### Meet The Author

NSFOCUS

咨询与合作：nsmagazine@nsfocus.com

* [绿盟科技官网](https://www.nsfocus.com.cn)
* [绿盟威胁情报中心（NTI）](https://nti.nsfocus.com)
* [绿盟云](https://cloud.nsfocus.com)