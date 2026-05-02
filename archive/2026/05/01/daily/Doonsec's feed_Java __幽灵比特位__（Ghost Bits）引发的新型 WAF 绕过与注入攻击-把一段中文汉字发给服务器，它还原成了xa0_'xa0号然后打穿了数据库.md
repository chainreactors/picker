---
title: Java \"幽灵比特位\"（Ghost Bits）引发的新型 WAF 绕过与注入攻击-把一段中文汉字发给服务器，它还原成了xa0\'xa0号然后打穿了数据库
url: https://mp.weixin.qq.com/s/-qNd5Go9a2Ce-Q6iWtewHw
source: Doonsec's feed
date: 2026-05-01
fetch_date: 2026-05-02T04:56:18.135223
---

# Java \"幽灵比特位\"（Ghost Bits）引发的新型 WAF 绕过与注入攻击-把一段中文汉字发给服务器，它还原成了xa0\'xa0号然后打穿了数据库

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/P8tspoQj3VqJx3S4iaX4bCnG3wia2DJ8RYVAXphmqn8Eus3blSqZUp7ByyXJcibvOrKJTibhxrPCzI3oVYiaxd21TZpEzMez1BibVMbsowyAoolk0/0?wx_fmt=jpeg)

# Java "幽灵比特位"（Ghost Bits）引发的新型 WAF 绕过与注入攻击-把一段中文汉字发给服务器，它还原成了 ' 号然后打穿了数据库

原创

IceByte
IceByte

Zner sec

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

> 你的 WAF 拦住了 `' OR 1=1`，却没拦住\*\*「逧 OR 亱=亱」\*\*。

因为对于 WAF 来说，它看到的是汉字——无害； 但对于 Java 的底层字节处理来说，那串汉字在执行时悄悄变成了 `' OR 1=1`。

这是因为 **Java char 强转 byte 时高位被静默丢弃**的底层机制，被研究员包装成了一套完整的攻击体系，在今年4月 **Black Hat Asia 2026** 正式公开。

名字叫：**Ghost Bits（幽灵比特位）**。

---

![](https://mmbiz.qpic.cn/mmbiz_png/P8tspoQj3VqmEgE0ia6sKjaJ9V8vvHO48TL2ozvZXVN1Phib7MlDvz3DpwNoejOUK7fHB8qepYu2gAIKTwHgnibRH03diaMygCIScSickftZ0ees/640?wx_fmt=png&from=appmsg)

---

## 一、先讲清楚这个"缺陷"到底是什么

研究员 **Xinyu Bai（浅蓝）** 最初发现这个问题，是在用 BurpSuite 测试时往请求 URI 里输入中文字符，结果数据包发出去以后——字变了。

他输入的是 `大黑阔`（`\u5927\u9ED1\u9614`）， 发出去的变成了`\x27\xd1\x14`。

`\x27`就是单引号 `'`。

---

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/P8tspoQj3VoAxsmApQQUBGXPuVqqekOAOx0thcGzo6w8mCq5H7Cu7mkTibRfqDGUjUm91ozno4OFtkXHyahJqBwk7ibmr6vxOcau7NWUJnDQY/640?wx_fmt=jpeg)

---

原因是 Java 标准库方法 `DataOutputStream#writeBytes(String s)` 的文档里清楚写着：

> "Each character in the string is written out, by discarding its high eight bits."

这不是 bug，是**有意为之的设计**——只是在当年设计时没人考虑到它会成为攻击向量。

Java 的 `char` 是16位（UTF-16），`byte` 是8位。 当代码执行以下任意一种操作时，**高8位会被抹掉，不报错，不抛异常，静默完成**：

```
(byte) ch             // 强制类型转换ch & 0xFF             // 位掩码截断baos.write(ch)        // ByteArrayOutputStream 写入DataOutputStream.writeBytes(str)
```

那些被抹掉的高8位，就是研究员命名的 **"Ghost Bits（幽灵比特位）"**。

说白了就一句话：**字符在 WAF 眼里是 Unicode 汉字，在 Java 底层执行里是另一个 ASCII 字符。两层视角，同一个输入，完全不同的解读。**

---

## 二、一段汉字如何变成路径穿越攻击

来看一个最典型的真实漏洞：**CVE-2025-41242（Spring Framework 任意文件读取）**。

研究员设计了一串中文：`阮严灵丰丰甲来`。 看起来毫无意义，但每一个字都经过精心挑选：

| 字符 | Unicode | 低8位（byte） | 对应 ASCII |
| --- | --- | --- | --- |
| 阮 | U+962E | 0x2E | `.` |
| 严 | U+4E25 | 0x25 | `%` |
| 灵 | U+7075 | 0x75 | `u` |
| 丰 | U+4E30 | 0x30 | `0` |
| 丰 | U+4E30 | 0x30 | `0` |
| 甲 | U+7532 | 0x32 | `2` |
| 来 | U+6765 | 0x65 | `e` |

这七个汉字拼在一起，经过 Ghost Bits 截断，变成了：`.%u002e`

`.%u002e` 是什么？是点号 `.` 加上 `..` 的 Unicode 编码形式。

也就是说，`阮严灵丰丰甲来/阮严灵丰丰甲来` = `./..` = `../`

**路径穿越就这样发生了。**

---

![](https://mmbiz.qpic.cn/mmbiz_png/P8tspoQj3VoHeWsXDkgsv3pWib6pcKR8d2vQFCPmZJHsDmYu7fib34GKKvqSA3iaJpFZIe1RYh47pibaRnrXcP2aDfHI81kjTxNtXO5wYpoc7eY/640?wx_fmt=png&from=appmsg)

---

### 这个漏洞厉害在哪？

Spring 有安全检查：`isInvalidPath`，会拦截包含 `../` 的路径。 但它**只认识字面量 `../`**，对 `/.阮严灵丰丰甲来/` 完全无感，判定放行。

路径随后进入 Jetty 的 `PathResource``#resolve`，Jetty 会识别 `%u002e` 并将其解码为 `.`，最终在文件系统层面还原成 `../../`。

一句话总结：**Spring 说"这段路径安全"，但 Jetty 执行时已经穿越了。**

受影响范围：`spring-boot-starter-jetty ≤ 3.2.4`，无需认证，直接读取服务器任意文件。

---

## 三、这套手法的攻击图谱

Ghost Bits 不是一个漏洞，是一种**攻击范式**。研究员演示了至少六个不同的攻击方向：

---

### 3.1 让 WAF 看不到 SQL 注入

Jackson 处理 JSON 字段时，内部有个 `charToHex` 方法用 `ch & 255` 截断字符：

```
"name": "1 union select 1,2,3--"
```

↑ 这个 WAF 会拦。

```
"name": "\u丰丰耳失\u丰丰甲丰..."
```

↑ 这个 WAF 不认识，放行——但 Jackson 解码后得到的结果和上面完全一样。

---

![](https://mmbiz.qpic.cn/mmbiz_png/P8tspoQj3Vrkw7mHqBcsLlffYuezcdlb3LHtPQA0Jw7nwKiaEWkMGSYRMqIicFS6kPz2ban6OFFbg3TRBOEgVyyaxt4UwibpiahvUDeQEgpVeuU/640?wx_fmt=png&from=appmsg)

---

### 3.2 Tomcat 文件上传，jsp 伪装成汉字发过去

上传文件时，`Content-Disposition` 里的文件名写成 `filename*="UTF-8''1.陪sp"`。

WAF 看到的是 `1.陪sp`——不是 `.jsp`，规则不触发，放行。

Tomcat 的 `RFC2231Utility.java` 内部执行 `(byte) c`，字符 `陪`（U+966A）高位 `0x96` 被丢弃，低位 `0x4A` = `'j'`，文件最终以 `1.jsp` 保存。

Webshell 就这样传上去了。

---

![](https://mmbiz.qpic.cn/mmbiz_png/P8tspoQj3Vo03Mb6icrjmyY9jcyzHAYBkOvcmZOI1Eo3eFiaU0MIJ79iaqggChtslxhEzJHKZcWUNwbEhSwTvrOyicicmGefGhHHV5kjdITUrIrc/640?wx_fmt=png&from=appmsg)

---

### 3.3 让 Jira 给你发钓鱼邮件（而且绕过 DKIM）

这是本次研究中**社会危害最大**的攻击方向。

Jakarta Mail（angus.mail）的 `ASCIIUtility.java` 在序列化邮件地址时，对每个字符执行强制 `(byte)` 转换。攻击者在"收件人"字段中夹入特定 Unicode 字符，经 Ghost Bits 截断后还原为 `\r\n`（回车换行），从而注入任意 SMTP 命令。

**具体场景：**

攻击者在 Jira 注册时，邮箱地址填入精心构造的 Ghost Bits 载荷。Jira 后端发送"注册确认邮件"时，触发 SMTP 注入——邮件被劫持，实际发送的是攻击者自定义内容：

```
RCPT TO: <2336485988@qq.com>DATASubject: You are Hacked!Malicious Link...
```

但**发件人依然是 Jira 的官方邮件地址**，而且 SPF / DKIM / DMARC 全部校验通过——因为邮件本来就是从 Jira 服务器发出去的，没有伪造发件服务器。

---

> * ![](https://mmbiz.qpic.cn/sz_mmbiz_png/P8tspoQj3VrD4002eudwNzhcFJGdvk3nUohn3xx7cx8eGS9Jt0T9llmKVhR1rPDcbR3QBCFCCHm00yunjLN9EmKqKs4W3GHfE7iaYbG1UzcU/640?wx_fmt=png&from=appmsg)
> * ![](https://mmbiz.qpic.cn/sz_mmbiz_png/P8tspoQj3VpdYnV10AuBmglq3zIb8J7ASibdwYOhHHtWibPODbbxkwCricfAibrCMWr6HqbBTj0gRIzQGdT0iaU76JAhROicmfhT1Kc1TNfZQRSlE/640?wx_fmt=png&from=appmsg)

---

### 3.4 Confluence 域名白名单？直接绕过

Confluence 可以配置"只允许 `@company.com` 邮箱注册"。 攻击者注册时填：`hacker[Ghost\r\n]@company.com`

* **Confluence 的验证逻辑**

  ：检查字符串末尾，确实是 `@company.com` → 验证通过
* **底层 SMTP 执行**

  ：Ghost Bits 将特定字符还原为 `\r\n`，SMTP 在 `hacker@qq.com` 处提前结束 RCPT TO 命令，确认邮件被发送到攻击者的 QQ 邮箱

攻击者拿到邮件里的激活链接，完成注册，获得内部系统账号权限。

---

> ![](https://mmbiz.qpic.cn/sz_mmbiz_png/P8tspoQj3VoTL5MBvk6cXK6FKF03dJibUjKbibJdibf47VBkzbAYkwicUSkAk5N9RuIQLzN4ibB2ERqSxqvSYEiaLOG94DsFwU8vXAS7j4ublYbbg/640?wx_fmt=png&from=appmsg)
>
> ![](https://mmbiz.qpic.cn/mmbiz_png/P8tspoQj3VqlqcqdvwbUm9Ax7P2oI96ZQ4jKIt6VicU0BBwZUTxZL5RMyAVicNoorKYwtrZSq1Vof74iacAzxd0IYOfoEq9YjAJJ2WzfQMAjsY/640?wx_fmt=png&from=appmsg)
>
> ![](https://mmbiz.qpic.cn/mmbiz_png/P8tspoQj3VqmictcqLPrqicApbBH16NAEOZHwRrwRAgPewbcADhUKhZM2Ngeq6z1eBVoeTWxvQDXCrtYbrBtX6FKnQUszEGKLQ3KtbibwcYvsc/640?wx_fmt=png&from=appmsg)

---

### 3.5 供应链污染：一个库，倒下一片

这个 SMTP 注入问题的根源——`angus.mail`——不是某个小众库，它是整个 Java 邮件生态的底座：

* Confluence、Jira、Bitbucket（Atlassian 全家桶）
* Keycloak
* YouTrack
* TeamCity（CVE-2025-57733）
* Liferay
* OpenMeetings

只要应用允许用户输入邮箱并从后端发信，就可能中招。这是典型的**供应链级攻击**。

---

> ![](https://mmbiz.qpic.cn/mmbiz_png/P8tspoQj3VoiavicpSCVr9jKD64nuUIlxc2v46wicsCkwI77YtJs2VxG9uUOibpiaDvhf6fhHolKgAdMfa5y5DB3Ar0INCleia6WAibib0aia0cxfsOE/640?wx_fmt=png&from=appmsg)

---

### 3.6 还有 HTTP 请求走私和 XSS

* **Apache HttpClient ≤ 4.5.9**

  （HTTPCLIENT-1974）：`ByteArrayBuffer#append` 在构建请求头时盲目 cast，如果应用把用户可控 token 拼进请求头，攻击者可注入 `\r\n` 实现请求走私
* **JDK 原生 HttpServer**

  （CVE-2026-21933）：若将用户输入反射到响应头，Ghost Bits 可注入 `\r\n`，将响应头变成新的响应体，导致 XSS

---

## 四、真的到处都是

研究员用自动化工具 **Secrux** 在 GitHub 搜索相关高危写法：

```
lang:Java AND ("(byte)ch" OR "(byte) ch" OR "ch & 0xff" OR "baos.write(ch")
```

**结果：8100+ 条匹配，Display limit hit（超出展示上限）。**

---

> ![](https://mmbiz.qpic.cn/mmbiz_png/P8tspoQj3VpM9EYmibJd6PVfVpsxCULXMiayYxq30B0iacMSibUPlkUXuEYWicW3OcKnIBgViaSWeowf0uNeIyGoEMVVFk7HTSuUiaZJ20R7xk42NU/640?wx_fmt=png&from=appmsg)

---

这意味着什么？意味着 Ghost Bits 不是某一个组件的问题，而是**渗透在整个 Java 生态底部的一类编码哲学缺陷**，还有大量未被发现的利用路径。

研究员在演讲结尾说的那句话：

> **"We have only scratched the surface."**（我们才刚触及表面。）

不是谦虚，是字面意思。

---

## 五、系统自查

## poc脚本自查

```
https://github.com/shiyeshu/GBitsTools
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/P8tspoQj3VoSB7hdg1KP5uW2cVJtemCz6InBuMVInhlBaCAumUXgznfiaSw6qcVxwPGmCaH20JNTycTuugZ3fvcACgciaVVQwasZFAvibPFx2M/640?wx_fmt=png&from=appmsg)

测试环境搭建：

```
https://github.com/vulhub/vulhub/blob/master/spring/CVE-2025-41242/README.zh-cn.md
```

![](https://mmbiz.qpic.cn/mmbiz_png/P8tspoQj3VptrTIYrmp5Zia2YBicCj1InL1ImUbRCCD8qWpHaDzc1icyFOxLwauOtOuD59RddPbca4oLbgic4W1wVxEBibfhdHQDnNnhTR5trRfo/640?wx_fmt=png&from=appmsg)

快速自查清单：

| 使用框架 | 排查范围 |
| --- | --- |
| Spring Boot + Jetty（≤ 3.2.4） | CVE-2025-41242，路径穿越 |
| Tomcat 处理文件上传 | Ghost Bits 文件名绕过 |
| Jackson / fastjson 解析用户输入 | WAF 绕过，SQL 注入 / RCE |
| 使用 jakarta.mail / angus.mail 发邮件 | CVE-2025-7962，SMTP 注入 |
| Apache HttpClient ≤ 4.5.9 | 请求走私 |
| Openfire（未打补丁） | CVE-2023-32315 新型绕过 |
| GeoServer（未打补丁） | CVE-2024-36401 WAF 绕过 |

---

## 六、如何防御

**第一步，打补丁（优先级最高）**

| 组件 | 升级目标 |
| --- | --- |
| Spring Framework 6.2.x | → 6.2.10 |
| Spring Framework 6.1.x | → 6.1.22 |
| Spring Framework 6.0.x | → 6.0.30 |
| Spring Framework 5.3.x | → 5.3.44 |
| Apache Commons BCEL | → 6.12.0+ |
| Apache HttpClient | → 4.5.10+ |
| GeoServer | → 2.28.3+ |
| Openfire | → 5.0.4+ |

**第二步，代码层面排查**

搜索代码库中的以下高危模式，逐一评估是否接收了外部输入：

```
(byte) chch & 0xFFbaos.write(ch)DataOutputStream.writeBytes(...)
```

替换方式：...