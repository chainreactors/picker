---
title: ATT&amp;CK框架更新跟踪——Invisible Unicode
url: https://mp.weixin.qq.com/s/lamwM212U9Is8lYnuZmPdw
source: Doonsec's feed
date: 2026-05-07
fetch_date: 2026-05-08T04:50:32.098924
---

# ATT&amp;CK框架更新跟踪——Invisible Unicode

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/SxWiaVqD6Jsmhav9iak87G6h3DFdA5xG2rnom2omibWv6eMpaw0yVibDUCibvib85IKKiahKb4E7Pusk9HAF7k5e9SCkvJml08n9tjXwEoxS7DibgyE/0?wx_fmt=jpeg)

# ATT&CK框架更新跟踪——Invisible Unicode

原创

网络保安29
网络保安29

红蓝攻防研究实验室

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

# 0x00 前言

MITRE ATT&CK 框架在2026年4月将利用 Unicode 不可见字符隐藏恶意内容的技术收录为 T1027.018 子技术 Invisible Unicode，归属在 Obfuscated Files or Information（T1027），属于防御规避战术。当文本中嵌入人眼完全无法感知的字符时，一些安全机制可能会失效。

官方描述：

Adversaries may abuse invisible or non-printing Unicode characters to conceal malicious content within files, scripts, or text. By inserting characters that do not visibly render, adversaries may hide data, alter how content is interpreted, or make malicious code appear as benign text or whitespace. Adversaries may encode these malicious payloads, using binary, Base64, or custom schemes, to be reconstructed at runtime through scripting features such as JavaScript Proxy traps, eval(), or other dynamic execution methods. This technique enables adversaries to evade visual inspection and basic static analysis by hiding malicious encoded content in innocuous text.

Unicode is a standardized character encoding model that assigns a unique numerical value, known as a code point, to every character across writing systems, enabling consistent text representation across platforms, applications, and languages. Code points are represented as U+ followed by a hexadecimal value and may be encoded using formats such as UTF-8 or UTF-16. Adversaries may abuse the valid code points in Unicode that are not visibly rendered but still take up bytes, such as zero-width spaces, variation selectors, or bidirectional formatting controls, to conceal malicious payloads.

Adversaries may additionally exploit Private Use Area (PUA) characters, a range of code points reserved for custom assignment. PUA characters that are not defined by a font or application are typically rendered blank.

Unicode characters may also be leveraged in support of other techniques such as Phishing, Right-to-Left Override, or User Execution. For example, some adversaries may embed artificial intelligence (AI) prompt injections using invisible Unicode characters in emails or documents that appear benign when processed by AI systems.

本文主要是对一些公开资料的整理和研究，包含了不可见 Unicode 字符的各种利用方式、实际案例和防御思路。

0x01 Unicode不可见字符的类型谱系

Unicode是一种标准化的字符编码模型，它为世界上所有书写系统中的每个字符分配一个唯一的数值标识——码点（code point），以"U+"后跟十六进制值的形式表示。Unicode的设计初衷是实现跨平台文本一致性表示，但其庞大的字符空间导致了常常被滥用。Unicode中存在大量合法码点，它们对应的字符在渲染时不会产生任何可见的视觉输出，但仍然占据字节空间，可以被程序读取和解析。

## 1.1 零宽字符

零宽字符是一类在显示时不占任何宽度的Unicode字符。常见的有零宽空格（U+200B）、零宽非连接符（U+200C）、零宽连接符（U+200D）和零宽词连接符（U+FEFF）。它们用来处理复杂文字系统的排版问题，例如阿拉伯文和印度文中的连字行为。但攻击者可以将零宽字符作为隐蔽的数据载体，在一串看似正常的文本中插入零宽字符来传递额外的信息，而所有这些字符的视觉呈现都是空白。

## 1.2 变体选择符

变体选择符（Variation Selectors，U+FE00至U+FE0F，以及扩展变体选择符U+E0100至U+E01EF）原本用于指定某个字符应使用哪种视觉变体呈现，比如给同一个emoji选不同肤色。但攻击者可以将恶意数据编码在变体选择符的序列中，使其紧跟在某个正常字符之后而不改变该字符的显示外观。变体选择符可以编码0到15的值，扩展变体选择符可以编码16到255的值，合起来恰好覆盖了0至255，即一个完整字节的所有可能值。这意味着攻击者可以用变体选择符编码任意的二进制数据。GlassWorm蠕虫正是利用了这种特性来将完整的JavaScript代码隐藏在看似空白的代码区域中。

## 1.3 双向格式控制符

双向格式控制符（如U+202A至U+202E）用于控制文本的显示方向，让阿拉伯文等从右向左书写的文字与英文在同一行中混合排列。攻击者可以利用这些控制符来解耦代码的视觉顺序和逻辑顺序，这种技术在2021年被Cambridge大学的研究团队以"Trojan Source"的名字首次系统化披露。

比如下面这段代码，里面插入了一些不可见字符，编译器读到的是：

```
var accessLevel = "user";if (accessLevel != "user[U+202E][U+2066]// Check if admin[U+2069][U+2066]"){  console.log("You are an admin.");}
```

而人眼看到的是：

```
var accessLevel = "user";if (accessLevel != "user") { // Check if admin  console.log("You are an admin.");}
```

代码中有三个控制符：

U+202E (RLO)：从这之后，所有字符按RTL（从右到左）方向渲染。

U+2066 (LRI) + U+2069 (PDI)：这是一对"隔离气泡"。LRI在RTL的大环境中挖出一个LTR（从左到右）的小区域，PDI关上这个气泡回到RTL。// Check if admin 就在这个气泡里面，被保护在了RTL规则之外。如果没有这个LRI/PDI对，RLO会把 // Check if admin 显示成 nimda fi kcehC //，导致暴露。

最后的 U+2066 (LRI)：在闭合引号 " 前面再开一个LTR气泡。这个气泡配合RLO的效果，让闭合引号 " 在视觉上被"推"到紧挨着 user 后面出现，完成欺骗。

看起来accessLevel不等于"user"时才输出管理员消息，逻辑上不应该执行，因为accessLevel就是"user"。但RLO字符（U+202E，hexdump中为e2 80 ae）让"// Check if admin"这个看似注释的文字被藏在了字符串引号内部，代码运行时，"user"不等于那个包含不可见字符的长字符串，条件为真，代码授予了管理员权限。

GitHub后来在检测到这种双向Unicode文本时会显示黄色警告："This file contains bidirectional Unicode text that may be interpreted or compiled differently than what appears below."

## 1.4 私有使用区字符

私有使用区（Private Use Area, PUA）是Unicode中保留给私人或组织自定义使用的码点空间，范围包括U+E000至U+F8FF以及若干补充平面中的区域。PUA字符没有由Unicode标准赋予任何默认含义，如果某个字体或应用程序没有为它们定义对应的符号，它们在渲染时就表现为空白。这种"天生隐形"的特性使PUA字符成为攻击者隐藏数据的理想容器。比如一个看起来完全正常的空字符串const key = ""; 在hexdump中只有干净的ASCII字节，但一个PUA字符U+FFF80的hexdump是f3 bf be 80，4个字节占据磁盘空间，渲染0像素宽度。

## 1.5 Unicode标签字符

Unicode标签字符集（Unicode Tag set，码点范围E0000至E007F）原本设计用于语言标注和方言标记，但已被Unicode标准废弃。这些字符在几乎所有现代浏览器、文本编辑器和应用中都不渲染，是真正的隐藏字符。标签字符从U+E0020到U+E007E恰好与可见ASCII字符集直接对应：任何英文字母、数字或常见标点符号只需给原始码点加上0xE0000就能得到对应的不可见标签版本，这个极其方便的映射关系使得标签字符被经常用于攻击大语言模型。

# 0x02 利用方式一：不可见字符编码隐藏恶意代码

将恶意代码转换为不可见Unicode字符序列是最直接的利用方式。核心原理是将恶意代码序列化为二进制数据，再用特定不可见字符的码点值来承载这些数据，使得整个payload在视觉上完全消失，但可以被运行时的解码逻辑完整还原并执行。不同攻击者会选择不同的不可见字符和编码方案，但本质都是同一个模式：编码→隐藏→解码→执行。

## 2.1 二进制编码

将恶意代码转换为二进制数据，然后用两个特定的不可见Unicode字符分别代表0和1。每一个字节由8个不可见字符组成，在视觉上完全不可感知，但在逻辑上完整地承载了原始数据。

例如Tycoon2FA钓鱼套件是采用二进制编码方式的典型案例。根据LevelBlue SpiderLabs的分析，Tycoon2FA在其钓鱼着陆页中使用了半宽韩文填充符（U+FFA0）代表二进制0，韩文填充符（U+3164）代表二进制1。攻击者将想要执行的JavaScript代码转换为二进制表示，然后用这两个不可见字符替换每一个二进制位。解码过程将编码字符拼接为二进制字符串，再按8位一组分割为字节，还原出原始JavaScript脚本。

```
// 简化的二进制解码逻辑function decode(binaryEncoded) {    let binaryStr = "";    for (let ch of binaryEncoded) {        let cp = ch.codePointAt(0);        if (cp === 0xFFA0) binaryStr += "0";  // 半宽韩文填充符 → 0        else if (cp === 0x3164) binaryStr += "1"; // 韩文填充符 → 1    }    let decoded = "";    for (let i = 0; i < binaryStr.length; i += 8) {        decoded += String.fromCharCode(parseInt(binaryStr.slice(i, i+8), 2));    }    return decoded;}
```

这种方式使得payload在视觉上完全隐形，能够规避静态分析和简单的模式匹配检测，而且将执行延迟到运行时，只有特定条件满足时才触发。

## 2.2 PUA字符编码与多重解码链

将恶意代码先Base64编码，然后编码后的字符串再以PUA不可见Unicode字符的形式嵌入载体文本中。在运行时，脚本先提取不可见字符还原为Base64字符串，再通过atob()解码，最后用eval()执行。

用代码简单说明一下：

编码：恶意JS → Base64 → PUA不可见字符

```
// 原始恶意代码const payload = 'require("child_process").exec("calc.exe")';// Base64编码const b64 = btoa(payload);// → "cmVxdWlyZSgiY2hpbGRfcHJvY2VzcyIpLmV4ZWMoImNhbGMuZXhlIiki"// 把Base64的每个字符映射到PUA码点// Base64字符是可见ASCII（A-Z, a-z, 0-9, +, /），码点值比如65-122// 给每个码点加上一个固定偏移量，推到PUA区间（U+E000-U+F8FF）const hidden = b64.split('').map(c =>    String.fromCharCode(0xE000 + c.charCodeAt(0))).join('');// 现在hidden是一串不可见字符，嵌入到载体文本中// 比如嵌入到 "|" 后面，视觉上用户只看到一个竖线const carrier = '|' + hidden;
```

解码（恶意代码运行时做的事）：PUA不可见字符 → Base64 → 原始JS

```
function decode(carrier) {    // 过滤出PUA字符（跳过可见的"|"等正常字符）    const puaChars = [...carrier].filter(c => {        const cp = c.codePointAt(0);        return cp >= 0xE000 && cp <= 0xF8FF;    });    // 减去偏移量，还原为Base64字符串    const b64 = puaChars.map(c =>        String.fromCharCode(c.codePointAt(0) - 0xE000)    ).join('');    // Base64解码还原恶意代码    return atob(b64);}eval(decode(carrier)); // 执行恶意代码
```

例如npm恶意包os-info-checker-es6展示了PUA字符作为编码载体的一个攻击链。这个包的preinstall.js文件包含eval(atob(...))调用，输入表面上只是一个竖线符号"|":

![](https://mmbiz.qpic.cn/sz_mmbiz_png/SxWiaVqD6JskGib9XkhUDx1WoEicWvFCiaYESc49ia337WhQIoW5LVngcTJBsJFabTdWz6VClF7YN8vhxbRhQ4cqvULiaJEsvFjIrooKlvC8gLpJM/640?wx_fmt=png&from=appmsg)

```
eval(atob(decode("|"))); // "|"实际是大量不可见PUA字符// Rust原生模块decode()将PUA码点转换为Base64字符串// atob()将Base64解码为JavaScript源码// eval()执行解码后的代码
```

当把代码复制到能显示Unicode码点的编辑器中，才发现竖线后面隐藏着大量PUA字符，这些PUA字符通过一个随包发布的Rust编译的原生Node模块进行解码。

![](https://mmbiz.qpic.cn/mmbiz_png/SxWiaVqD6JsmL9LqVicvFPDgFScwr79DJPShTDjviaia1rm3vSHRaWTW3jKKHtPvNpwicQsUHetayj5LgSxrZcE5syibCVh1sFj637RV6JqV0Z3Rg/640?wx_fmt=png&from=appmsg)

解码后的代码通过访问特定的Google Calendar事件url，获得payload并执行。

## 2.3 变体选择符编码

变体选择符的编码效率远高于二进制编码，每一个变体选择符可以直接承载一个字节值，而不是二进制编码中每个字节需要8个字符。变体选择符（U+FE00-U+FE0F）映射0到15，扩展变体选择符（U+E0100-U+E01EF）映射16到255，合起来覆盖了0-255即一个完整字节的所有可能值。这意味着每个不可见字符携带一个字节的数据，编码密度是二进制方式的8倍。

解码函数非常精简，一行代码就完成了从不可见字符到字节再到字符串的完整还原：

```
const d = s => [...s].map(c => (  c = c.codePointAt(0),  c >= 0xFE00 && c <= 0xFE0F ? c - 0xFE00 :       // VS1-VS16 → 0-15  c >= 0xE010...