---
title: Ghost Bits 自动化提效：让WAF绕过告别重复劳作
url: https://mp.weixin.qq.com/s/WMD3MQ-8QM8hZXtTpbxFnA
source: Doonsec's feed
date: 2026-04-29
fetch_date: 2026-04-30T05:27:08.720076
---

# Ghost Bits 自动化提效：让WAF绕过告别重复劳作

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/jibGAup6p72FoujKVuxr0NYSX6utpHbvzQXibpXOxJ5kVe9rlt7dTIXlYgia6JlyBE9oJwLAyqDZ8KvS9EO7Zwq51eU9uBuQXDvSz0j92FJuw4/0?wx_fmt=jpeg)

# Ghost Bits 自动化提效：让WAF绕过告别重复劳作

原创

YAK
YAK

Yak Project

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

![](https://mmbiz.qpic.cn/mmbiz_gif/f7AtEgJhMZc5BYI1O7qwYC876L6gkbkACCZMJOIAPQmNqT0uZojjJZcfPsNJk6EjcbicXiaaSZ6j4APvocaxlI1w/640?wx_fmt=gif)

![](https://mmbiz.qpic.cn/mmbiz_jpg/f7AtEgJhMZd0VthLJpzgmAAibgKmOtuudYEwKgrTRWKUKeuACA9RLaqk2MUIXHibxa7kicVPMHHT6ibIUsWCPUryRA/640?wx_fmt=webp&from=appmsg)

前言

Ghost Bits 是近期安全社区热度很高的 WAF 绕过技术，Blackhat 相关议题以及多个 CVE（如 CVE-2025-41242）都涉及到这一手法。在实际渗透测试中，Ghost Bits 编码本身不难——写几行脚本就能实现。但每次都是"打开编辑器 → 改代码 → 跑脚本 → 复制结果 → 粘贴到工具里"，步骤一多就容易打断思路。为此我们写了一个 Yak Codec 插件，选中 payload 右键直接输出编码结果，省去来回切换窗口的麻烦。

除了编码，批量探测靶点是否受 Ghost Bits 影响也是个重复活动。针对这个场景我们还写了一个 **Yak Fuzz插件**，内置了 CVE-2025-41242、Jackson、fastjson 等常见场景的 preset，跑一遍就能快速判断目标是否存在截断风险。

本文在梳理核心原理的基础上，分别介绍这两个插件的设计思路和使用方式：Codec 负责"一键编码"，Fuzz 负责"批量探测"。希望能帮师傅们在检测这类漏洞时少做一些重复劳动、提高效率。

如果你也厌倦了手动复制粘贴 Unicode 字符，或者想快速批量验证一批目标是否受 Ghost Bits 影响，这篇文章适合你。这些插件目前你可以在Yakit插件商城下载。

前这些插件你可以在在线商店下载：

![](https://mmbiz.qpic.cn/mmbiz_png/jibGAup6p72GiaDibhIib4VAraOiap4pXzicSRbhY7Upr3wEMZxDFWQR7QKq6tHxUMoTGoFKLhuILd6QOPibvichOf9BibiaWuGZZf1cUXCHMx4r6BpKc/640?wx_fmt=png&from=appmsg)

一、Ghost Bits 漏洞原理

Ghost Bits（幽灵位）是一种利用 Java 字符截断特性的 WAF 绕过技术。其核心原理在于：**Java 在处理****Unicode****字符时，某些方法会静默丢弃高 8 位，只保留低 8 位**。

例如，`String.getBytes()`、`ByteArrayOutputStream.write(ch)`、`DataOutputStream.writeBytes()` 等方法，本质上都执行了如下操作：

```
截断结果 = unicodeChar & 0xFF
```

这意味着，只要构造一个 Unicode 字符，使其低 8 位等于目标 ASCII 值，就能在服务端"伪装"成该 ASCII 字符：

```
阮 = U+962E → 0x962E & 0xFF = 0x2E = .严 = U+4E25 → 0x4E25 & 0xFF = 0x25 = %灵 = U+7075 → 0x7075 & 0xFF = 0x75 = u
```

攻击者利用这一点，将 WAF 能识别的敏感字符串（如 `../`、`union select`）编码成"无害"的中文 Unicode，从而绕过检测。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/jibGAup6p72G4H83Cp4yWCRNhQOLG22DNoYjYDUhz0V996Cz7x5xiaYqjuiciczL5fhbibicibxOHGTav0EMjSYcIkpEMVjWw1d3l91WppxnplrFxE/640?wx_fmt=png&from=appmsg)

***YAK***

**以 CVE-2025-41242 为例**

在 Spring Framework CVE-2025-41242 中，攻击链如下：

1. **WAF****放行**：WAF 看到 `阮严灵丰丰甲来` 等 Unicode 字符，没有敏感关键词，直接放行

2. **Spring 防御层**：`ResourceHttpRequestHandler#getResource` 调用 `isInvalidPath(path)` 检查字面量 `../`，路径中没有 `../`，判定安全

3. **截断发生**：`StringUtils.uriDecode()` 内部的 `baos.write(ch)` 丢弃高 8 位，`阮`(U+962E) → `.`(0x2E)

4. **路径折叠**：Jetty/Servlet 容器将 `%u002e` 解码为 `.`，最终 `.%u002e` → `..`，形成目录穿越

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/jibGAup6p72FDqpiajj2LJOwI2aGKJBIfyuxOR2xZibl8xiaKv0NSkfplU36F29JWTa2FxjfRJrbyAb5wA60KBU7FnA88A8U11cNZhY2Uicbw7icU/640?wx_fmt=jpeg&from=appmsg)

## **二、利用流程中，哪个环节适合工具提效**

Ghost Bits 漏洞的完整利用流程包括：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/jibGAup6p72HW85VCXJ2xCyFNjSDBSZlcENx65xuAWo8DNCR9P1A1ovyquCEdQhiaj2QprbO2n2XqZaAkGKLicq7KgJrsn8658bE8Bd8sicTHXE/640?wx_fmt=png&from=appmsg)

***YAK***

**最适合工具提效的环节**

整个流程里，真正值得插件化的是**编码和验证**这两个环节。发现截断点虽然也可以写 Fuzzer 辅助批量探测，但更多依赖对目标架构的理解；构造 payload 和发送测试本身不复杂。真正消耗时间的是把每个 ASCII 字符逐个查表转换成 Unicode 替换体，以及编码完成后验证截断结果是否还原成了原始 ASCII——这两个步骤重复性高、容易出错，最适合交给工具处理。我们的 Codec 插件解决"一键编码"的问题，Fuzzer 插件解决"批量探测截断点"的问题，验证脚本则用来确保编码结果正确。

## **三、Ghost Bits编码插件**

基于上述痛点，我们编写了一个 Yak Codec 插件，将 Ghost Bits 编码过程完全自动化。

***YAK***

工具原理

**插件内置两个 Unicode 候选池：**

![](https://mmbiz.qpic.cn/mmbiz_jpg/jibGAup6p72HbIM4XAGgfgY4wr7mET7nrCrQ09CJBVh0KfzoljnJyY01RJoH9rtO6xpubCNFONibxxbL77ZicYdquEibxCiaiccjkfvGlcJgfichEw/640?wx_fmt=jpeg&from=appmsg)

**候选池设计：**

![](https://mmbiz.qpic.cn/mmbiz_png/jibGAup6p72Gmxiccw6ibyEd839peMFLMktd4x0yeXgplEicV3kLhxETHo402D4GFMqCX9R3Wicag4AibaY88fCnpfATOlUHJ11YICAG0eFUJibanI/640?wx_fmt=png&from=appmsg)

默认使用**中文优先池**，编码结果可读性强，便于在 WebFuzzer 中辨认和调试。

***YAK***

### **核心代码**

```
// 保留空白和斜杠，其余 ASCII 全部编码shouldEncode = func(asciiCode) {    if asciiCode < 0 || asciiCode > 127 { return false }    if asciiCode in [9, 10, 13, 32] { return false }  // 空白    if asciiCode == 47 { return false }                 // /    return true}// 从中文优先池随机选 highBytepickGhostChar = func(asciiCode, fixedHighByte) {    selectedHighByte = fixedHighByte    if selectedHighByte <= 0 || selectedHighByte > 255 {        selectedHighByte = chinesePreferredHighBytes[randn(0, len(candidatePool))]    }    return chr(selectedHighByte*256 + asciiCode)}
```

***YAK***

### **靶场实战：vulhub/CVE-2025-41242**

以 vulhub 的 `spring/CVE-2025-41242` 靶场为例，演示 Codec 插件的实际用法。

靶场环境

```
```
docker-compose 启动后，目标地址：http://127.0.0.1:8080漏洞点：Spring 的 StringUtils.uriDecode() 在特定路径下会丢弃 Unicode 高 8 位
```
```

**构造****Payload**

这个漏洞的利用需要把路径中的 ASCII 字符替换成 Ghost Bits 编码的 Unicode。比如目标 payload 是 `.%u002e`（经过 Spring 内部解码后变成 `..` 实现目录穿越）。在 WebFuzzer 中选中 `.%u002e`，右键执行 GhostBits Payload Codec，插件直接输出对应的 Unicode 替换结果：

```
输入：  .%u002e输出： 蔮蔥蕵蔰锰進蕥
```

此处payload不是“阮严灵丰丰甲来”，原因是 Ghost Bits 的编码本身就不唯一。只要满足"截断后低 8 位等于目标 ASCII"这个条件，任何一个 Unicode 字符都可以作为替换体。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/jibGAup6p72ECLvbKgSjL8lllHrf8qGY463KtTcrUeJP1uibE9K4Nia89MvJXEeSA5wpQJqIhC6NLlTTO0AfeS2Qbj3IlBefdia4ia8du4jDIzaw/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/jibGAup6p72H6ChiaOXicjfUYNbLOkL5N56jgE18o08GUZRqgaZnYbBicpWmYtFwD7DhnyEgfrarZ3DVUVD7FVYjeFgPciclkfxn0sjTUB56cvIY/640?wx_fmt=png&from=appmsg)

**验证结果**

发送后观察响应。如果截断生效，服务端会将 Unicode 高 8 位丢弃，实际处理的路径变成 `../../etc/passwd`，从而读取到系统文件内容。响应中若出现 `root:x:0:0:` 等 `/etc/passwd` 特征，即可确认漏洞存在。

![](https://mmbiz.qpic.cn/mmbiz_png/jibGAup6p72GmibFAW7V0EICRnJnROnoTMwSkxWWnnLPL7c2j9Dw9dd1u4NHfpRE66eIH0EuXzXxJRicgw94B8rKq22feqKpgKFn7tYLf54nGA/640?wx_fmt=png&from=appmsg)

## **四、Ghost Bits Cast Fuzz插件**

Codec 插件解决的是"如何快速编码 payload"的问题，但在实战中，你还需要回答另一个问题：**目标是否存在 Ghost Bits 漏洞？**

为此我们编写了 **GhostBits Cast Fuzzer**——一个主动扫描插件，内置多个常见场景的预设 payload，一键发送到目标并自动分析响应。

***YAK***

### **集成的场景**

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/jibGAup6p72HodBhhicMictOUo4ZK06JWUVeFmpn7iaXDa76LW8MBvgGSKJMxrSQ86AVGibPy4BOYIcCBEa50LkSiagA0DlFmXgoP2cEHgZnzKelc/640?wx_fmt=jpeg&from=appmsg)

***YAK***

### **快速验证流程**

```
```
输入目标 URL → 选择场景 → 一键发送 → 自动分析响应
```

Fuzzer 会自动检测响应中是否包含 WAF 拦截关键词、异常状态码、或成

功读取的文件内容，并在 Yakit 数据库中记录风险发现。

![](https://mmbiz.qpic.cn/mmbiz_png/jibGAup6p72Enh1HiaZdEWnBbIOv7yUmL3dI7OGibKjBds3kGL12sOMElRiab3RI83fMVeyLZia2RZGLezh0YKtAEvYXwl5Hpe7UwOiciaJJSM2d7I/640?wx_fmt=png&from=appmsg)
```

## **五、Ghost Bits编码字符串验证脚本**

## **编码后的 payload 必须验证每个 Unicode 字符能否正确截断回原始 ASCII。我们编写了一个独立的 Yak 验证脚本：**

```
// verify_ghostbits.yak// 验证 Ghost Bits 编码结果：每个 Unicode 字符截断后是否等于原始 ASCIItruncateVerify = func(encoded, original) {    ok = true    encRunes = []    for _, r = range encoded { encRunes = append(encRunes, r) }    origBytes = []byte(original)
    for i = 0; i < len(origBytes) && i < len(encRunes); i++ {        truncated = ord(encRunes[i]) & 0xFF        if truncated != int(origBytes[i]) {            println("FAIL at", i, "orig=", origBytes[i], "truncated=", truncated)            ok = false        }    }    return ok}// 测试示例encoded = "阮严灵丰丰甲来"original = ".%u002e"if truncateVerify(encoded, original) {    println("验证通过：所有字符截断后还原正确")}
```

该脚本的核心逻辑就是模拟服务端的截断行为：`ord(unicodeChar) & 0xFF == ord(originalChar)`。

![](https://mmbiz.qpic.cn/mmbiz_png/jibGAup6p72EaxxDViaN9Ar58RicJSGZiaPcsrV4x4HQVCDCTyS18baoztuicJj5XWrkGgO5h8WZUzlV2iaZkhptHY0NlicxZPCl4nRfmRHEHiccSU8/640?wx_fmt=png&from=appmsg)

**六、总结**

**Ghost Bits 漏洞的本质是****编码层与解析层的语义差异**：WAF 在编码层看到无害的 Unicode，服务端在解析层截断还原成恶意的 ASCII。

本文分享的 Codec、Fuzzer 和验证脚本三个工具，希望能帮师傅们在检测这类漏洞时少做一些重复劳动、提高测试效率。Codec 插件把 Ghost Bits 编码压缩成"选中 → 右键 → 输出"的三步操作；截断验证脚本则自动确认编码结果的正确性，避免人眼比对出错。

需要说明的是，Fuzzer 插件中内置的场景（CVE-2025-41242、Jackson、fastjson 等）并不通用——它们借鉴了 AsiaCCS 2026 相关议题和论文中对 Ghost Bits 利用路径的分析，但每个目标的业务场景、框架版本、WAF 规则都不相同。师傅们可以参考其中的 payload 构造思路和场景分类方法，根据自己的实际目标修改测试脚本，而不是直接照搬运行。

**END**

**YAK官方资源**

Yak 语言官方教程：
*https://yaklang.com/docs/intro/*
Yakit 视频教程：
*https://space.bilibili.com/437503777*
Github下载地址：
*https://github.com/yaklang/yakit*
Yakit官网下载地址：
*https://yaklang.com/*
Yakit安装文档：
*https://yaklang.com/products/download\_and\_install*
Yakit使用文档：
*https://yaklang.com/products/intro/...