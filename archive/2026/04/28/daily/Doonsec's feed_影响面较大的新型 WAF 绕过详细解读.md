---
title: 影响面较大的新型 WAF 绕过详细解读
url: https://mp.weixin.qq.com/s/Utx64ue7Phs44pCHrpJbrQ
source: Doonsec's feed
date: 2026-04-28
fetch_date: 2026-04-29T05:08:10.540246
---

# 影响面较大的新型 WAF 绕过详细解读

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/IicMcDFtTOlPVhoqdwWxZDmJ8fGoAMMFx2XaK6jRlLcrHcYOicrxiaGeWchPefByXcrkHXsShSEHs0n9QTFpT1nGibSzwD3ibiaa4VicpssFY8pqRI/0?wx_fmt=jpeg)

# 影响面较大的新型 WAF 绕过详细解读

原创

棉花糖糖糖
棉花糖糖糖

棉花糖fans

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

![图片](https://mmbiz.qpic.cn/mmbiz_gif/1mtwZURvGTkCK3ZFyqYEyTwmaLo2YSMeibz3eeShkewiadS4oh0RBl1U7BTVeEscGQrEbjWKcQzGpJEFLwr4cFQw/640?wx_fmt=gif&wxfrom=5&wx_lazy=1&tp=webp#imgIndex=0)![]()

本文解读使用GPT5.5基于 原PPT 的 56 页内容整理

原文PDF文件：`Asia-26-Bai-Cast-Attack-Ghost-Bits-4.23.pdf`公众号后台回复0428获取

## 0. 先说清楚

可以这样理解这个幽灵比特位的问题：

Java 里的字符 `char` 通常是 16 位，网络协议、文件名、HTTP 头、SMTP 命令这些东西最终却经常要落到 8 位字节上。正常代码应该明确用 UTF-8、ASCII 等编码来转换；但一些老 API 或实现为了方便，直接把 `char` 强行塞进 `byte`。

问题来了：16 位塞进 8 位，塞不下的高 8 位就被丢掉了。

举个最直观的例子：

```
陪 = U+966A
低 8 位 = 0x6A
0x6A = 字母 j
```

所以攻击者给系统的是：

```
1.陪sp
```

安全检查可能觉得这不是 JSP 文件，因为它看到的是 `陪`。但如果后面某个组件把字符按低 8 位写成字节，它就可能变成：

```
1.jsp
```

这就是 Ghost Bits 的味道：高位信息像“幽灵”一样在检查时还存在，到了真正执行时却消失了。上层看到的是一个样子，底层执行的是另一个样子。

整篇 PDF 讲的就是这件事会带来多少连锁反应：

| 场景 | 白话解释 |
| --- | --- |
| WAF 绕过 | WAF 看到乱码或中文，后端看到 SQL、RCE、`@type` |
| 文件上传绕过 | 检查时不是 `.jsp`，保存时变成 `.jsp` |
| 路径穿越 | 检查时没有 `../`，解析后变成 `../` |
| SMTP 注入 | 邮箱地址里藏的 Unicode 变成换行，SMTP 命令被插入 |
| 请求走私 / XSS | Header 里的字符变成 CRLF，请求或响应结构被改写 |
| Redis / XML / 路径污染 | 字符串写到底层协议后，字段、标签、路径含义变了 |

用一句人话总结：

> ❝
>
> Ghost Bits 的危险点不是“中文字符危险”，而是“检查时看到的字符串”和“执行时使用的字节”不是同一个东西。

## 1. PDF 内容总览

先把这份 PDF 放到一张地图里看。它是一份安全议题幻灯片，题目是：

> ❝
>
> Cast Attack: A New Threat Posed by Ghost Bits in Java

演讲者与贡献者：

| 角色 | 人员 | 信息 |
| --- | --- | --- |
| Speaker | Xinyu Bai / B1u3r / 浅蓝 | Web 与应用漏洞研究 |
| Speaker | Zhihui Chen / 1ue | Alibaba Cloud Security Engineer |
| Contributor | Zongzheng Zheng / SpringKill | 贡献者 |

整体结构大致是这样：

| 页码 | 内容 |
| --- | --- |
| 1-2 | 标题、作者介绍 |
| 3-6 | Ghost Bits 概念、Java 字符到字节截断的根因 |
| 7-18 | WAF Bypass：BCEL、Jackson、Fastjson、Tomcat、URL、Base64、GeoServer、Spring4Shell |
| 19-47 | 真实漏洞案例：Openfire、Spring、SMTP、Jira、Confluence、Apache HttpClient、JDK HttpServer |
| 48-56 | 总结、自动化发现、ActiveJ、Lettuce、XMLWriter、Jodd、未来攻击面 |

如果再压缩成一句话：

Ghost Bits 不是单一 CVE，而是一类由“字符视图”和“字节视图”不一致引发的攻击模式。安全检查看到的是 Unicode 字符串，底层协议、解码器或 I/O 写入看到的却是被截断、折叠或宽松解析后的危险字节。

## 2. Ghost Bits 到底是什么

### 2.1 Java 的 `char` 不是 1 字节字符

先从一个很容易被忽略的事实说起：Java 的 `char` 不是 1 字节。它是 16 位 UTF-16 code unit。很多中文、全角字符、其他语种字符都可以放进一个 `char`，例如：

| 字符 | Unicode | 二进制低 8 位 | 低 8 位对应 ASCII |
| --- | --- | --- | --- |
| 陪 | U+966A | 0x6A | `j` |
| 阮 | U+962E | 0x2E | `.` |
| 严 | U+4E25 | 0x25 | `%` |
| 灵 | U+7075 | 0x75 | `u` |
| 丰 | U+4E30 | 0x30 | `0` |
| 甲 | U+7532 | 0x32 | `2` |
| 来 | U+6765 | 0x65 | `e` |
| 瘍 | U+760D | 0x0D | `\r` |
| 瘊 | U+760A | 0x0A | `\n` |

如果代码错误地把这些 `char` 当成单字节写出去，例如 `(byte) ch` 或 `out.write(ch)`，Java 不会帮你保留完整字符。高 8 位会被丢弃，只剩低 8 位。

例如：

```
陪 = U+966A
0x966A & 0xff = 0x6A
0x6A = ASCII 'j'
```

所以在字符串层面，人和 WAF 看到的是 `陪`；但在某些底层字节写入之后，真正落下去的可能是 `j`。

### 2.2 “幽灵比特”的含义

所谓 Ghost Bits，就是输入字符中“高 8 位那部分信息”。这些高位在上层字符串检查时还在，所以 WAF、业务校验、日志、人工审计看到的是一个完整的 Unicode 字符；但到了错误的字节化过程里，它们被静默丢掉，于是执行层只剩低 8 位。

可以把它抽象成：

```
输入字符 c       = 高 8 位 + 低 8 位
安全检查看到    = c 的完整 Unicode 形态
危险 sink 写出  = c & 0xff
协议解析看到    = 低 8 位对应的 ASCII/控制字符
```

利用者可以挑选满足这个条件的字符：

```
c = (k << 8) + target_byte
```

其中 `target_byte` 是希望底层最终看到的字节，例如 `.`, `/`, `%`, `@`, `\r`, `\n`。

### 2.3 这类攻击的本质

所以这类问题的本质不是“中文字符危险”，也不是“Unicode 本身危险”，而是：

```
安全检查使用的语义 != 最终执行使用的语义
```

把攻击链展开看，就是下面这个过程：

```
flowchart LR
    A["攻击者提交 Unicode 字符"] --> B["WAF / 业务校验"]
    B --> C["看起来不是 SQL / 路径 / CRLF / @type"]
    C --> D["进入 Java 组件或协议库"]
    D --> E["char 被截断或宽松折叠成 byte"]
    E --> F["低 8 位变成危险 ASCII / 控制字符"]
    F --> G["协议、路径、JSON、SMTP、Redis 等执行真实含义"]
```

这就是 Cast Attack 的核心：借助类型转换、位运算或宽松解码，让上层看起来无害的字符，在底层变成有语法意义的危险字节。

## 3. 容易出问题的代码模式

议题里反复出现的风险模式包括：

| 模式 | 风险点 |
| --- | --- |
| `(byte) ch` | 直接把 16 位 `char` 缩窄成 8 位 |
| `ch & 0xff` / `ch & 255` | 只保留低 8 位 |
| `baos.write(ch)` | `ByteArrayOutputStream.write(int)` 只写低 8 位 |
| `OutputStream.write(int)` | 参数是 `int`，但写出的仍是低 8 位 |
| `DataOutputStream.writeBytes(String)` | 逐字符写低 8 位，高 8 位丢弃 |
| `StringBufferInputStream.read` | 老旧 API，以低 8 位方式处理字符 |
| `String.getBytes(int, int, byte[], int)` | 已废弃，按低 8 位拷贝 |
| `RandomAccessFile.writeBytes` | 字符串写字节时丢高位 |
| 宽松 Hex / URL 解码 | 非法字符被算成合法 hex |
| 宽松 Base64 解码 | 用 `& 255` 从映射表取值 |

这些 API 并不是一出现就必然等于漏洞。如果输入不可控，或者转换结果不会进入安全敏感语法，风险可能很低。真正需要警惕的是下面这种组合：

```
用户可控输入
+ 字符串层安全校验
+ 后续 char -> byte 截断/折叠
+ 结果进入协议、路径、反序列化、文件名、Header、SMTP、Redis 等语法边界
```

## 4. Ghost Bits、宽松解析、归一化绕过的关系

这份 PPT 把这些现象放在 Ghost Bits 这个大框架下讨论。为了更好理解，建议把案例先分成三类，因为它们的底层触发方式并不完全一样，防御侧的重点也会略有不同。

| 类型 | 典型根因 | PDF 中的例子 |
| --- | --- | --- |
| 真正的高位截断 | `char` 低 8 位被写入 byte | `DataOutputStream.writeBytes` 、Tomcat `fromHex`、Spring `uriDecode`、SMTP、Lettuce、XMLWriter、Jodd |
| 位运算折叠 | 非 hex 字符被算法“压缩”为合法 hex | Jetty `%2>` 变 `%2E`，Openfire、GeoServer |
| 宽松 Unicode 解析/归一化 | 非 ASCII 数字、全角字符被当作 ASCII 语义 | Fastjson `Character.digit`、全角 URL 编码 |

它们共同点是：安全检查和真实执行对同一段输入产生了不同解释。

## 5. WAF Bypass 类案例

### 5.1 BCEL Ghost Bits 绕过

PDF 第 8 页讨论 BCEL 的解码逻辑。核心代码形态是：

```
ByteArrayOutputStream bos = new ByteArrayOutputStream();
CharArrayReader car = new CharArrayReader(chars);
JavaReader jr = new JavaReader(car);

while ((ch = jr.read()) >= 0) {
    bos.write(ch);
}
```

关键点：

`ByteArrayOutputStream.write(int)` 写出的不是完整 `int`，而是低 8 位。因此如果 BCEL 编码字符串里混入高位 Unicode 字符，WAF 看到的是一串异常字符；BCEL 解码时却还原成攻击者想要的字节流。

攻击视图差异：

| 层级 | 看到的内容 |
| --- | --- |
| WAF | `$$BCEL$$` 后面跟大量 Unicode 字符，特征弱 |
| BCEL 解码器 | 低 8 位字节流 |
| 类加载逻辑 | 可执行的字节码 |

本质是“字节码编码字符串”的安全检查没有模拟 BCEL 最终的低字节写入行为。

### 5.2 Jackson `charToHex` 绕过

PDF 第 9 页展示 Jackson 场景：输入看起来像一串 Unicode，例如 `\u丰丰耳失...`，但 `charToHex` 逻辑里存在类似：

```
return sHexValues[ch & 0xff];
```

示例映射：

| 字符 | Unicode | `& 255` 后 | 结果 |
| --- | --- | --- | --- |
| 丰 | U+4E30 | 0x30 | `0` |
| 耳 | U+8033 | 0x33 | `3` |
| 失 | U+5931 | 0x31 | `1` |

所以 `丰丰耳失` 在低 8 位视角中变成 `0031`，再经过字符/转义处理后可能成为 `1`。

PDF 中的完整效果是：

| 阶段 | 语义 |
| --- | --- |
| 攻击者输入 | Unicode 字符串 |
| WAF | 未发现 `union select` |
| Jackson 映射字段 | 还原出 `1 union select 1,2,3--` |
| 后续 SQL | 注入 payload 被执行 |

这里的关键不是 SQL 本身，而是 WAF 没有按照 Jackson 的最终转义解析逻辑还原字符串。

### 5.3 Fastjson `\u` escape 绕过

PDF 第 10 页讲的是 Fastjson 的 `\u` escape 场景。这里不完全是高 8 位截断，而是 Java 的 `Character.digit()` 过于宽松。

`Character.digit(c, 16)` 不只接受 ASCII 的 `0-9a-fA-F`，还可能接受其他文字系统里的数字字符，例如泰文数字、旁遮普数字、Vai 字符等。

结果是：

| WAF 视图 | Fastjson 视图 |
| --- | --- |
| 看不到普通 ASCII `@type` | Unicode 数字被当作 hex digit |
| 认为 payload 不匹配反序列化特征 | 解析后仍得到 `@type` |

所以这个案例的原理应归类为“宽松 Unicode 数字解析导致的语义差异”。防御时不能只找 `(byte) ch`，还要审计协议解析中是否用了宽松字符分类 API。

### 5.4 Fastjson `\x` escape 绕过

PDF 第 11 页展示 `\x` escape：

```
{"\x4_type": ...}
```

解析逻辑类似：

```
int x_val = digits[x1] * 16 + digits[x2];
char x_char = (char) x_val;
```

其中：

```
x1 = '4'  -> 4
x2 = '_'  -> 0
4 * 16 + 0 = 64
64 = '@'
```

于是 `\x4_` 被解析成 `@`，最终键名变成 `@type`。

这个案例说明：如果解码表对非法字符没有严格拒绝，而是给了默认值，就可能把“非法输入”转成“攻击者想要的合法字符”。

### 5.5 Tomcat `filename*` 文件上传绕过

PDF 第 12 页展示 Tomcat 文件上传场景：

```
filename*="UTF-8''1.陪sp"
```

WAF 检查文件名时看到：

```
1.陪sp
```

它不像 `.jsp`，因此可能放行。但 Tomcat 的 RFC2231 解析逻辑中存在如下形态：

```
if (c == '%') {
    ...
    out.write((b1 << shift) | b2);
} else {
    out.write((byte) c);
}
```

`陪 = U+966A`，低 8 位是 `0x6A`，也就是 `j`。因此后端保存时可能得到：

```
1.jsp
```

攻击视图：

| 阶段 | 文件名 |
| --- | --- |
| WAF / 上传扩展名检查 | `1.陪sp` |
| RFC2231 低字节写入后 | `1.jsp` |
| 文件系统落地 | JSP 文件 |

核心问题是：文件名作为安全边界被检查了一次，但真正落盘前发生了另一次不同语义的转换。

### 5.6 全角 URL 编码绕过

PDF 第 13 页讲全角 URL 编码：

```
%２ｅ%２ｅ%２ｆ
```

其中：

| 全角 | ASCII |
| --- | --- |
| `２` | `2` |
| `ｅ` | `e` |
| `ｆ` | `f` |

在某些 URL、URI、文件 URL 处理链中，全角字符经过归一化后会接近：

```
%2e%2e%2f -> ../
```

这个案例不是典型的高 8 位截断，而是“全角/半角归一化 + 多阶段解码”的语义差异。它与 Ghost Bits 一样，利用的是检查阶段和执行阶段的解释不一致。

### 5.7 Ghost-Bit URL Encoding：`%2>` 变成 `.`

PDF 第 14 页和后面的 Openfire、GeoServer 案例都围绕 `%2>` 展开。

正常 URL 百分号编码要求 `%` 后面跟两个十六进制字符，例如：

```
%2e = .
```

但某些 Jetty 相关的十六进制转换逻辑对非法 hex 字符不严格拒绝，而是通过位运算把它折叠成一个 0-15 的值。字符 `>` 被折叠成 `E`，于是：

```
%2> -> %2E -> .
```

这个点非常危险，因为 WAF 通常会认为 `%2>` 是非法编码或噪声，不会把它当作 `.`。

### 5.8 Base64 解码绕过

PDF 第 15...