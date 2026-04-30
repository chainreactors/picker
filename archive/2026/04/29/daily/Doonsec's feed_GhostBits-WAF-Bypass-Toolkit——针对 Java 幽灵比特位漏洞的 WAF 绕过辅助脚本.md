---
title: GhostBits-WAF-Bypass-Toolkit——针对 Java 幽灵比特位漏洞的 WAF 绕过辅助脚本
url: https://mp.weixin.qq.com/s/Q6SqplB6NUzs2_lc5WuQww
source: Doonsec's feed
date: 2026-04-29
fetch_date: 2026-04-30T05:25:24.380926
---

# GhostBits-WAF-Bypass-Toolkit——针对 Java 幽灵比特位漏洞的 WAF 绕过辅助脚本

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/qqiaD4wiajgFyXLNhQibPJgRrhK1beJZStMJ4Q32huSGthyaEyhgdJskmBTsLu4vg8rVo0tMWC1tUMeQ4HZq4ZIJaY1MEn4JJTCeQib2X1aFMZo/0?wx_fmt=jpeg)

# GhostBits-WAF-Bypass-Toolkit——针对 Java 幽灵比特位漏洞的 WAF 绕过辅助脚本

一个人挺好
一个人挺好

一个人挺好 wa

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

项目地址

https://github.com/lxqwind/GhostBits-WAF-Bypass-Toolkit

GhostBits WAF Bypass Toolkit Java char→byte 高位截断漏洞（幽灵比特位/Ghost Bits）WAF 绕过工具，专为文件读取/路径穿越场景设计。

✨ 功能特性 ● Bypass 生成：一键替换敏感字符（如 . / ' 等）为 Ghost Bits 替换体，生成绕过 payload ● 多格式输出：支持原始字符、URL 编码、curl 命令三种格式，直接适配 Burp/curl 场景 ● Ghost 字符查询：输入目标 ASCII 字符，快速获取所有低位匹配的 Unicode 替换体 ● 原理说明：内置漏洞原理与攻击链说明，帮助理解绕过逻辑

![](https://mmbiz.qpic.cn/mmbiz_png/qqiaD4wiajgFwfCTEM8KOLRf0Y2nf1XlK9fibKbU87kBlqKod99nzyHdkLde6HyJww1iaBmxy3mOHwwBicNeoCp5cAdy21dx1WRdgx85H5jNPWWY/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/qqiaD4wiajgFwbA1MYqYYepOVqseZpmficQVeKw6sRVtp988zMJgVrtGsB7VCI1ZAFqLdBN7X3TT4yCiaZZW1iaiaBHEdLlALwpvgibPZpUp8qebeg/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/qqiaD4wiajgFxTKbTBjEg8icxJ9K1wMqicXg62NMDpyCHayQBsuzD2uPmfUoSBCqAllicxKtb5eZIdsWFWjexzn9JfrUnWmmMf9qJpBT4oibXTChc/640?wx_fmt=png&from=appmsg)

2026 年 4 月，在 **Black Hat Asia 2026** 大会上，安全研究员 Xinyu Bai（浅蓝）与 Zhihui Chen（1ue）发表了题为 **《Cast Attack: A New Threat Posed by Ghost Bits in Java》** 的研究成果，首次系统性地揭示了 Java 生态中一个长期被忽视的底层编码缺陷 —— **"幽灵比特位（Ghost Bits）"**。

该漏洞源于 Java 中 `char`（16 位）与 `byte`（8 位）之间强制类型转换时的高位静默丢弃问题。攻击者利用这一特性，可将攻击 Payload 中的关键 ASCII 字符替换为精心构造的 Unicode 字符，使 **WAF/IDS** 看到的是无害的中文或乱码，而**后端 Java 服务**在解码时高位截断还原为原始危险字符，从而实现"瞒天过海"式的绕过。

> **核心公式**:
> `Java 16位 char → 被错误当成 8位 byte → 高位静默丢失 → 低位变成危险语法字符 → 安全检查与真实执行不一致`

---

## 漏洞原理

### 根本原因

Java 中 `char` 类型为 **16 位（2 字节）**，而 `byte` 类型仅为 **8 位（1 字节）**。当 Java 代码通过以下方式将 `char` 转换为 `byte` 时：

* `(byte) ch`
* `ch & 0xFF`
* `baos.write(ch)`
* `DataOutputStream#writeBytes()`

**高 8 位会被静默丢弃，只保留低 8 位**。这些被丢弃的高位比特即被称为"幽灵比特位"。

### 2.2 字符转换示例

以汉字「爻」（U+2F58）为例：

```
爻 → U+2F58 → 二进制：00101111 | 00111010
(byte) 转换后：高 8 位 0x2F 丢弃，低 8 位 0x3A → 'X'
```

### 2.3 典型字符映射表

| Unicode 字符 | Unicode 编码 | 低 8 位 | 还原为 ASCII |
| --- | --- | --- | --- |
| 陪 | U+966A | 0x6A | `j` |
| 阮 | U+962E | 0x2E | `.` |
| 瘍 | U+760D | 0x0D | `\r` (回车) |
| 瘊 | U+760A | 0x0A | `\n` (换行) |
| 爻 | U+2F58 | 0x3A | `:` |
| 㹣 | U+3E63 | 0x63 | `c` |
| ౬ | U+0C6C | 0x6C | `l` |
| ᙡ | U+1661 | 0x61 | `a` |
| ⑳ | U+2473 | 0x73 | `s` |

### 2.4 攻击链流程

```
攻击者提交 Unicode 字符
        ↓
WAF / 业务校验 → 看到无害中文/乱码，放行
        ↓
进入 Java 组件或协议库
        ↓
char 被截断或宽松折叠成 byte
        ↓
低 8 位变成危险 ASCII / 控制字符
        ↓
协议、路径、JSON、SMTP、Redis 等执行真实含义
```

---

## 3. 攻击场景分类

### WAF/IDS 全面绕过

现有基于字符串特征的 WAF 规则对 Ghost Bits 变形 Payload 防护效果有限。攻击者通过高位 Unicode 字符隐写攻击载荷，可绕过绝大多数特征检测规则。

### SQL 注入绕过

**受影响组件**: Jackson Databind
**漏洞点**: `charToHex()` 方法中 `ch & 255` 截断
**利用方式**: 将 SQL 注入 Payload 隐写于 Unicode 字符中，WAF 无告警，后端还原并执行

### 反序列化 RCE 绕过

**受影响组件**: Apache Commons BCEL、Fastjson
**漏洞点**:

* BCEL ClassLoader 解码时 `ByteArrayOutputStream.write(int)` 仅保留低 8 位
* Fastjson `\u` / `\x` 转义存在 Ghost Bits
  **利用方式**: 绕过 WAF 触发反序列化远程代码执行

### 文件上传绕过

**受影响组件**: Apache Tomcat
**漏洞点**: `RFC2231Utility` 处理文件名时截断高位
**利用方式**: 将 `.jsp` 伪装为非敏感 Unicode 字符（如 `1.陪sp`），绕过 WAF 上传 Webshell

### 路径穿越 / 认证绕过

**受影响组件**: Spring Framework、Jetty、Undertow、Vert.x
**漏洞点**: URL 解码路径存在 Ghost Bits
**利用方式**: 绕过 WAF 实现目录穿越；Openfire CVE-2023-32315 可借此绕过 WAF 防护直接利用

### SMTP 注入

**受影响组件**: Angus Mail 等邮件库
**漏洞点**: 隐写 CRLF 序列还原为换行符
**利用方式**: 触发 SMTP 注入，实现邮件劫持或业务逻辑绕过（已在 Jira、Confluence 上复现）

### HTTP 请求走私 / XSS

**受影响组件**: Apache HttpClient（≤ 4.5.9）、JDK 原生 HttpServer
**漏洞点**: Ghost Bits CRLF 注入
**利用方式**: Header 中的字符变成 CRLF，请求或响应结构被改写

---

## 实战利用案例

### BCEL Ghost Bits 绕过

**核心代码形态**:

```
ByteArrayOutputStream bos =newByteArrayOutputStream();
CharArrayReader car =newCharArrayReader(chars);
JavaReader jr =newJavaReader(car);

while((ch = jr.read())>=0){
    bos.write(ch);// 仅写入低 8 位
}
```

**攻击视图差异**:

| 层级 | 看到的内容 |
| --- | --- |
| WAF | `$$BCEL$$` 后面跟大量 Unicode 字符，特征弱 |
| BCEL 解码器 | 低 8 位字节流 |
| 类加载逻辑 | 可执行的字节码 |

### Tomcat 文件上传绕过

**Payload 构造**:

```
文件名: 1.陪sp
        ↓
WAF 看到: "陪" → 非敏感字符，放行
        ↓
Tomcat RFC2231Utility 处理:
        陪 (U+966A) → 低 8 位 0x6A → 'j'
        ↓
最终文件名: 1.jsp
```

### Spring4Shell WAF 绕过

**传统 Payload**:

```
class.module.classLoader.resources.context.parent.pipeline.first.directory
```

**Ghost Bits 变形**:

```
㹣౬ᙡ⑳⑳.module.classLoader...
```

**映射关系**:

| 字符 | 低 8 位 | ASCII |
| --- | --- | --- |
| 㹣 | 0x63 | `c` |
| ౬ | 0x6C | `l` |
| ᙡ | 0x61 | `a` |
| ⑳ | 0x73 | `s` |
| ⑳ | 0x73 | `s` |

### 4.4 Openfire CVE-2023-32315 认证绕过

**传统 Payload**:

```
/setup/setup-s/%u002e%u002e/%u002e%u002e/log.jsp
```

**Ghost Bits 进阶 Payload**:

```
/setup/setup-s/%2>%2>/%2>%2>/log.jsp
```

**原理**: Jetty 的宽松 hex 转换将 `>` 折叠为 `E`，使 `%2>` 变为 `%2E`（即 `.`），WAF 将其视为非法编码而放行。

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/AGUhPQZ04zyTvSBegohhPkdl4ZiaID39hGjT55M6GNVWWYfpt8Q146OaDEU4xQ0E4VtxLO4zfGia16VE6qHb001g/0?wx_fmt=png)

一个人挺好 wa

向上滑动看下一个

知道了

![]()
微信扫一扫
使用小程序

取消
允许

取消
允许

取消
允许

×
分析

![跳转二维码]()

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/AGUhPQZ04zyTvSBegohhPkdl4ZiaID39hGjT55M6GNVWWYfpt8Q146OaDEU4xQ0E4VtxLO4zfGia16VE6qHb001g/0?wx_fmt=png)

微信扫一扫可打开此内容，
使用完整服务

：
，
，
，
，
，
，
，
，
，
，
，
，
。

视频
小程序
赞
，轻点两下取消赞
在看
，轻点两下取消在看
分享
留言
收藏
听过