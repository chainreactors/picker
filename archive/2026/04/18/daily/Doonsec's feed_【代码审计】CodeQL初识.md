---
title: 【代码审计】CodeQL初识
url: https://mp.weixin.qq.com/s/406DYM0f4HHo_st1XK2bQQ
source: Doonsec's feed
date: 2026-04-18
fetch_date: 2026-04-19T04:48:19.618137
---

# 【代码审计】CodeQL初识

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/ocg1gpicEs1ufS1aMrEF4QMqmQWlEoTeIyhV6AUoQyJUsFGD0cicfsVsib8BklQwYcQBibdqPEY7YoBPf1ZJbUeCGZVuic3zUibVqDWiaMcay7ib3as/0?wx_fmt=jpeg)

# 【代码审计】CodeQL初识

原创

十月的进阶之路
十月的进阶之路

十月的进阶之路

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

> 与其精神内耗，不如出门瞎跑。

## 目录

1. 背景
2. CodeQL 检测示例
3. 结果总览
4. 结果抽样分析
5. 使用 VSCode 的 CodeQL 插件

## 一、背景

微软开发的`SAST`工具，将代码转化成一种关系型数据库，可用`QL`查询语句来查找符合特定模式的代码片段，通过这种方式查找漏洞。`QL`语言作为一种面向对象的逻辑编程语言，语法类似于`SQL`，但引入了类 (`Class`) 和谓词 (`Predicate`) 等概念。

`CodeQL`组成部分：解析引擎+`SDK`。

* 解析引擎地址：

```
https://github.com/github/codeql-cli-binaries/releases
```

* 规则库地址：

```
https://github.com/github/codeql
```

**解析引擎**：不开源，解析编写的规则，但是可以直接在官网下载二进制文件直接使用。

**SDK(规则库)**：完全开源，里面包含大部分现成的漏洞规则，**可编写自定义规则**。

## 二、CodeQL 检测示例

### 注意：本小结的示例代码依旧以WebGoat作为案例

### 1. 创建数据库

```
codeql database create webgoat --language=java --command="mvn clean package -DskipTests" --source-root=D:\code-audit\codeQL\WebGoat-2025.3
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ocg1gpicEs1t9ZRicD948KyibtWeprcU8ia9gwQbcjwashQmSD5qnE2qKQGUxcKkPtsQOdlN9EypTBSkPcS5IicIZwOzfbjib23jnx5OEFxdt4Me8/640?wx_fmt=png&from=appmsg)

### 2. 升级数据库格式

升级`CodeQL`数据库的格式，让旧数据库适配最新版的`CodeQL`工具/扫描规则。

```
codeql database upgrade webgoat
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ocg1gpicEs1v9UCkgMxBaOATIdbKk1qLBIicxuw9YMia0OLVmPEDE4SWjO8L1yXKWKFH0V9DSx2z3BS5PPhm2vpGiabZxACkFX6rMG6ibsnOpibUM/640?wx_fmt=png&from=appmsg)

### 3. 全量规则扫描（基础版）

调用`CodeQL`官方规则库，对数据库进行代码扫描，输出漏洞/缺陷报告。默认的检测命令太慢了，加入如下的参数稍微快一点。

```
codeql database analyze D:\code-audit\codeQL\data\webgoat D:\code-audit\codeQL\codeql-main\java\ql\src\Security --format=csv --output=webgoat_result.csv --threads 0 --ram 16 --no-debug --no-save-cache
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ocg1gpicEs1unooz06Pf80vJHcp1PiafQLckfRiabGcNEoC8nC5LJKoXbAU5GRfZY8cAiaeAotzcaBEK3cLLUBhsFSRjWURVSWGsKWtPxo3QTaw/640?wx_fmt=png&from=appmsg)

当然如果您执行上述的命令，会出现如下的情况，内存不足。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ocg1gpicEs1twElKBpo0p2DKO8WLytDx5UYLrMXDibfUTjh5w0iblicRYtZicWQ7icjv4GrMy770STxjR03SLA86qZha9E8Skt4d6WKep7aoTTgZk/640?wx_fmt=png&from=appmsg)

### 4. 精简规则加速扫描

针对这种情况精简下规则，将不需要的规则去除掉。在`codeql-main\java\ql\src\Security`目录下编写`fast-web-security.qls`文件，加入如下规则。

```
- description: fast-web-security

# 只保留你关心的 Web 安全类 CWE 目录
- queries: Security/CWE/CWE-022
- queries: Security/CWE/CWE-023
- queries: Security/CWE/CWE-074
- queries: Security/CWE/CWE-079
- queries: Security/CWE/CWE-089
- queries: Security/CWE/CWE-094
- queries: Security/CWE/CWE-113
- queries: Security/CWE/CWE-134
- queries: Security/CWE/CWE-200
- queries: Security/CWE/CWE-209
- queries: Security/CWE/CWE-352
- queries: Security/CWE/CWE-601
- queries: Security/CWE/CWE-611
- queries: Security/CWE/CWE-918

# 再做一次“收口”：只保留 security 且高精度的查询
- include:
    tags contain: security
    precision:
      - high
      - very-high
```

执行验证命令`resolve queries`，将`suite`展开成最终会执行的查询列表。

![](https://mmbiz.qpic.cn/mmbiz_png/ocg1gpicEs1v0xnsHa5WLeSYZU4lwzjzmD5cmR8g44k1R2jDAw8Wf3BeWS1QNjs5mtbIxXCAcBcicrLj9hogNj0EibaLjTGoiaeSt5z4SSvS6Gw/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/ocg1gpicEs1uMQOn2BwhYMic2hhHeXXZ7ha6gibDJKwAzqO2HEGGQEfEQrKcTxM95AhSYOdCEQudAwKhORBWx9dk75nA6qrs4xVcKeno38v0eU/640?wx_fmt=png&from=appmsg)

重新执行命令扫描。

```
codeql database analyze D:\code-audit\codeQL\data\webgoat D:\code-audit\codeQL\codeql-main\java\ql\src\Security\fast-web-security.qls --format=csv --output=webgoat_fast_result.csv --threads 0 --ram 16 --no-debug
```

![](https://mmbiz.qpic.cn/mmbiz_png/ocg1gpicEs1sydSwHjTmM36ib5tb833IflIG93ZvqXYGZMKiaoXWvbqXuScl0KvJVO4pFPBicnTLHO6Rmd10xeB4uht7LggxLSDhRpEvWVQv5TQ/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ocg1gpicEs1sydDbEpbn5qAwM6CPffaoDcUjx1e5HEIO7Lmt9DzvialUQYVCibicQUF1TxySyzxWon5VWMHoefsu4PPkbVgorGZY6WuN732tuLM/640?wx_fmt=png&from=appmsg)

这次很快就扫描完成。

## 三、结果总览

先来看看扫描的漏洞整体状态，如下。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ocg1gpicEs1vlEGlJoGMN2iaMn8oGCoTB2YtRChoyJaaia6GicrgRpQkrNl4A1aDiatWUBcJWqjE1Yqa1u0Z8GyfOD82WI3vTLupHNA4icYr7pGoM/640?wx_fmt=png&from=appmsg)

### （一）漏洞总体统计

* **总计漏洞数量**：35个实例
* **漏洞类型**：5种不同类型
* **高危漏洞占比**：94.3%（33/35个）
* **主要影响范围**：SQL安全、文件操作安全、Web安全配置

### （二）漏洞类型分布

| 漏洞类型 | 危险级别 | 数量 | 主要风险 |
| --- | --- | --- | --- |
| SQL注入漏洞 | 高危 | 16个 | 数据泄露、篡改、服务器接管 |
| 路径遍历漏洞 | 高危 | 15个 | 敏感文件泄露、服务器文件访问 |
| CSRF防护漏洞 | 中危 | 2个 | 跨站请求伪造、未授权操作 |
| Zip Slip漏洞 | 高危 | 1个 | 文件覆盖、恶意文件上传 |
| XXE漏洞 | 高危 | 1个 | 内部信息泄露、端口扫描 |

## 四、结果抽样分析

本小结随机抽取一个`sql`注入进行结果分析，首先介绍下`codeql`结果中各列的含义，当然为了表格的美观，我建议将`csv`转换为`xlsx`视觉上更舒服。

| Excel列号 | 完整列名 | 核心作用 |
| --- | --- | --- |
| A | 漏洞类型（Vulnerability Type） | 快速识别漏洞属于哪一类安全问题 |
| B | 漏洞描述（Vulnerability Description） | 一句话说明漏洞的原理和基本危害 |
| C | 严重级别（Severity Level） | 评估漏洞的紧急程度 |
| D | 输入源追踪（Source Trace） | 找到**用户输入从哪里进入**漏洞代码（最关键的溯源列） |
| E | 漏洞所在文件（Vulnerable File） | 漏洞代码实际存在的Java文件路径 |
| F | 起始行号（Start Line） | 漏洞代码片段的第一行行号 |
| G | 起始列号（Start Column） | 漏洞代码片段的第一个字符位置 |
| H | 结束行号（End Line） | 漏洞代码片段的最后一行行号 |
| I | 结束列号（End Column） | 漏洞代码片段的最后一个字符位置 |

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ocg1gpicEs1sEyCYVWrqkswREibOMv95hOD1qDsm9joo1GAM3b8SXk7Lj9A6fR2K5Nkia0C6Ic7t4icNq7rEykicETHooMhMWcBOjoG3b65hCavU/640?wx_fmt=png&from=appmsg)

根据列表的内容定位代码中的漏洞点，经过发现这正是`jwt`存在`sql`注入的漏洞点。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ocg1gpicEs1srWpsicqiamGw10dG9BGklN1QtWxjQw0AibU1l84v0PsGRCtbvogm7HvAEWNRVerLRH55drQVPKQW7iaaFmiaR2G7o8DDMnibPbLBy8/640?wx_fmt=png&from=appmsg)

## 五、使用 VSCode 的 CodeQL 插件

从`csv`文件去定位代码，终究是比较繁琐，那么我们考虑使用`codeql`插件，可以免去手动定位这个步骤。

![](https://mmbiz.qpic.cn/mmbiz_png/ocg1gpicEs1v3PaO88nltyC4TxGvq30Svoa47TOWNf2aAttZ9YW9vf5cUQGseYpkbRvsNt5AsrNP9vP1okbpwLtn9sKWiaicpjuVQrrTDtGicSc/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/ocg1gpicEs1u2DEH84y3BFdHrIicIJXp1xy6db2RiaJxDYmqicX8vlIXGTwTVNEMZfavxH6TZgYqyVdibOlC5pfomIgsGNb4VnjYUaw98BVFliaEk/640?wx_fmt=png&from=appmsg)

当然你可以参考内置的检测规则撰写自己的检测规则，充分发挥你的能力。

![](https://mmbiz.qpic.cn/mmbiz_png/ocg1gpicEs1uMBoHy013CNzf51kl5fiaCrCCWodzXX6OVfGOGnNQTqwNMV029t5VcGGYQCJRiceFia8LXxs8W6EJZ2YV7rAZHNzr3U0fUibn3iaQo/640?wx_fmt=png&from=appmsg)

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/GFPic2iaAJQw9icmAfmmEej0faflh5tB82cUK35MTVuw42wOQtcxfYUV0AXBEgJCSan9OhFhdMXuUpjtyUB8cxwVA/0?wx_fmt=png)

十月的进阶之路

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/GFPic2iaAJQw9icmAfmmEej0faflh5tB82cUK35MTVuw42wOQtcxfYUV0AXBEgJCSan9OhFhdMXuUpjtyUB8cxwVA/0?wx_fmt=png)

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