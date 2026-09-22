---
title: 每天学一个 Kali 工具 · Day21 nikto：Web 服务器的老牌\"体检医生\"
url: https://mp.weixin.qq.com/s/27cnlKglnLF1SNhL-ZP9xQ
source: Doonsec's feed
date: 2026-09-21
fetch_date: 2026-09-22T07:01:38.313543
---

# 每天学一个 Kali 工具 · Day21 nikto：Web 服务器的老牌\"体检医生\"

# 每天学一个 Kali 工具 · Day21 nikto：Web 服务器的老牌"体检医生"

原创

0day收割机
0day收割机

0day收割机

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

每天学一个 Kali 工具 · Day21

# nikto：Web 服务器的老牌"体检医生"

摘要：「每天学一个 Kali 工具」第二十一天。昨天 davtest 敲开了进攻篇的大门，今天请出 Web 漏洞扫描界的元老——nikto：Perl 编写的 Web 服务器扫描器，七千多项检查，专治过时版本、危险文件、错误配置和缺失安全头。它还能把全部流量喂给 Burp Suite 联动分析。文末附完整参数速查和 Tuning 代码表，建议收藏。

![](https://mmbiz.qpic.cn/mmbiz_jpg/ZrTsB3aQgWBgh54UthKMEw3AO44ntNu59ULsIobYzD7PUU1vXvBR6B4ESWhTCAKSFOFQnzgI4Pic0fXkXMhk2LSqwFsK05ne0YtNsPSnQGec/640?wx_fmt=jpeg)

## 写在前面

Day02 到 Day05，我们学了四件目录爆破兵器（dirb、feroxbuster、ffuf、gobuster），它们回答的问题是：**"这个服务器上有什么路径？"**

Day19 的 Burp Suite 回答的是：**"这个请求的每个字节能不能做手脚？"**

今天的 **nikto** 回答的问题更进一步：**"这台 Web 服务器本身，病了吗？"**

软件版本过时吗？有没有不该存在的默认文件？管理后台暴露了吗？安全响应头配齐了吗？CGI 目录能被利用吗？——nikto 拿着七千多项检查清单，把 Web 服务器从头到脚体检一遍，直接出病历。

它是渗透测试流程里雷打不动的一环：**nmap 发现 80 端口 → nikto 体检 → Burp 精细手术**。OffSec 的 WEB-200 课程专门给它开了章节。

## 一、nikto 是什么？

Kali 官网的定义：Nikto 是一款 **Web 服务器扫描器**（Perl 编写），通过 CSV 格式的**检查数据库**对 Web 服务器执行全面的漏洞测试，支持文本/HTML 等多种输出格式，支持 SSL、代理和 Cookie。

三个身份标签：

| 标签 | 说明 |
| --- | --- |
| **元老资历** | 2001 年诞生，比大多数读者的安全生涯都长，至今仍在维护更新 |
| **数据库驱动** | 检查项存在 CSV 数据库里（7000+ 项），更新数据库就是更新"病历知识库" |
| **轻量敏捷** | 2.15 MB，依赖只有 Perl 和几个库——和 Burp 的 344MB 形成鲜明对比 |

**nikto 检查什么？** 官方归纳的核心类别：

* 过时/存在漏洞的服务器软件版本
* 危险的默认文件和 CGI 脚本
* 服务器配置错误（目录列表开启、可写目录等）
* 缺失的安全响应头（X-Frame-Options、CSP 等）
* 信息泄露（版本号、内部路径、注释里的敏感信息）
* 管理后台、安装脚本等敏感入口暴露

![](https://mmbiz.qpic.cn/mmbiz_jpg/ZrTsB3aQgWCpA2BcqJjboib9bODgdfZnyFsKwE1ibwXvhrrJWF6y6EGhrmznbUnKwHgFZlJwC60ZX9YibnlW0gEVgdNJmRlCtRLicwicicFibVPcJs/640?wx_fmt=jpeg)

## 二、快速上手：官网示例精讲

官网给的示例：对 192.168.0.102 做扫描，显示等级 1234EP，只跑 1/2/3/b/d/e 六类检查，HTML 报告输出：

```
nikto -Display 1234EP -o report.html -Format htm -Tuning 123bde -host 192.168.0.102
```

官网输出（节选）：

```
+ Target IP:          192.168.0.102
+ Server: Apache/2.2.22 (Ubuntu)
+ The X-XSS-Protection header is not defined...
+ Apache/2.2.22 appears to be outdated...
+ End Time:           2018-03-23 10:50:44
```

**逐段解读：**

1. `Server: Apache/2.2.22 (Ubuntu)`

   ：nikto 第一件事就是抓服务器 Banner——2.2.22 是 2012 年的版本，早已停止维护；
2. `X-XSS-Protection header is not defined`

   ：缺失安全响应头，一条典型的"配置病"；
3. `Apache/2.2.22 appears to be outdated`

   ：直接判定软件过时——这就是 nikto 的看家本领，对着版本数据库比年龄；
4. `End Time`

   ：扫描耗时统计，报告收尾。

**参数拆解：**

| 片段 | 含义 |
| --- | --- |
| `-host 192.168.0.102` | 目标主机（也可用 `-url`） |
| `-Display 1234EP` | 显示控制：1 重定向、2 Cookie、3 所有 200/OK 响应、4 需认证的 URL、E 错误、P 进度 |
| `-Tuning 123bde` | 只跑指定类别的检查（代码表见第四节） |
| `-o report.html -Format htm` | 输出 HTML 报告 |

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/ZrTsB3aQgWB1jcpVNAIUx8aLmYSibx25mr1zQrLCsWIKcmGaAAMicrynqsB9bojkYiaYuY1JaKoziawa5Pgx83ZBHSJNnD8twF95j2zse7S8gCY/640?wx_fmt=jpeg)

## 三、和 Burp Suite 联动：流量全进航母

Day19 学的 Burp，今天就能和 nikto 打配合——nikto 支持走代理：

```
# 1. 编辑 nikto.conf，把代理指向 Burp
PROXYHOST=127.0.0.1
PROXYPORT=8080

# 2. nikto 挂代理扫描（Burp 要先开且关闭拦截，免得流量卡住）
nikto -host http://target -useproxy
```

这样 nikto 打出的**每一个请求**都会进 Burp 的 Proxy History 和 Site Map：nikto 负责地毯式体检，Burp 负责把可疑请求捞出来 Send to Repeater 精细手术。**老兵 + 航母，Web 测试的标准双打。**

## 四、参数速查表

### ▍目标指定

|  |  |
| --- | --- |
| `-host <主机/URL>` | 目标主机或 URL |
| `-url <主机/URL>` | -host 的别名 |
| `-port <端口>` | 目标端口，默认 80 |
| `-ssl` | 强制对端口使用 SSL |
| `-nossl` | 禁用 SSL |
| `-ipv4 / -ipv6` | 只用 IPv4 / IPv6 |
| `-check6` | 检查 IPv6 是否可用 |
| `-vhost <主机名>` | 虚拟主机（用于 Host 头） |

### ▍扫描控制（精华所在）

|  |  |
| --- | --- |
| `-Tuning <代码>` | **扫描调优** ：只跑指定类别的检查（代码表见下） |
| `-Plugins <列表>` | 只运行指定插件 |
| `-list-plugins` | 列出所有可用插件 |
| `-evasion <编号>` | **编码规避技术** ：改变请求形态躲避 IDS/过滤 |
| `-mutate <编号>` | 猜测额外文件名（对发现的目录做变体扩展） |
| `-mutate-options` | 为 mutate 提供附加信息 |
| `-maxtime <秒>` | 单主机最大测试时长 |
| `-timeout <秒>` | 单请求超时，默认 10 秒 |
| `-Pause <秒>` | 每个测试之间的暂停（放慢节奏） |
| `-Cgidirs <目录>` | 指定要扫描的 CGI 目录 |
| `-Platform <平台>` | 指定目标平台 |
| `-followredirects` | 跟随 3xx 重定向 |
| `-root <路径>` | 给所有请求加统一前缀路径 |

### ▍-Tuning 代码表（背下来，扫描效率翻倍）

| 代码 | 类别 | 代码 | 类别 |
| --- | --- | --- | --- |
| **0** | 文件上传 | **8** | 命令执行/远程 Shell |
| **1** | 日志中见过的有趣文件 | **9** | SQL 注入 |
| **2** | 错误配置/默认文件 | **a** | 认证绕过 |
| **3** | 信息泄露 | **b** | 软件识别 |
| **4** | 注入（XSS/脚本） | **c** | 远程源码包含 |
| **5** | 远程文件获取（Web 根内） | **d** | Web 服务 |
| **6** | 拒绝服务（DoS） | **e** | 管理控制台 |
| **7** | 远程文件获取（全服务器） | **x** | **反向排除** （跑除了它以外的所有） |

组合直接连写：`-Tuning 123bde`（官网示例同款）；排除某类用 x：`-Tuning 9x` 表示"除了 SQL 注入都跑"。

### ▍认证与代理

|  |  |
| --- | --- |
| `-id <user:pass>` | HTTP 认证 |
| `-key <文件>` | 客户端证书私钥 |
| `-RSAcert <文件>` | 客户端证书 |
| `-useproxy` | 使用 nikto.conf 里定义的代理（**接 Burp 就靠它**） |
| `-nocookies` | 不使用响应里的 Cookie |
| `-useragent <UA>` | 强制 User-Agent |
| `-Add-header <头>` | 给请求附加 HTTP 头 |

### ▍输出与报告

|  |  |
| --- | --- |
| `-o / -output <文件>` | 输出到文件 |
| `-Format <格式>` | 输出格式（txt/htm/csv/xml/json 等） |
| `-Display <代码>` | 终端显示控制：1 重定向、2 Cookie、3 全部 200/OK、4 认证 URL、E 错误、P 进度、V 详细 |
| `-Save <目录>` | 把阳性响应保存到目录——**可回放** |
| `-nointeractive` | 禁用交互特性 |
| `-noslash` | 去掉 URL 末尾斜杠 |

### ▍数据库与配置

|  |  |
| --- | --- |
| `-dbcheck` | 检查数据库和关键文件完整性 |
| `-update` | 更新检查数据库（老手扫前必跑） |
| `-nocheck` | 启动时不检查更新 |
| `-config <文件>` | 使用指定配置文件 |
| `-Option <选项>` | 覆盖 nikto.conf 里的某个选项 |
| `-Version` | 打印插件和数据库版本 |
| `-404code <代码>` | 把这些 HTTP 状态码当作"不存在"忽略 |
| `-404string <字符串>` | 响应体里出现该字符串就当作 404 |
| `-no404` | 禁用 nikto 的 404 页面猜测 |
| `-nolookup` | 禁用 DNS 反查 |

## 五、实战速查

```
# 1. 最简扫描：一条命令体检
nikto -host http://192.168.0.102

# 2. 官网同款：调优扫描 + HTML 报告
nikto -Display 1234EP -o report.html -Format htm -Tuning 123bde -host 192.168.0.102

# 3. 扫前先更新数据库（病历知识库要最新）
nikto -update

# 4. HTTPS 站点强制 SSL
nikto -host target.com -ssl -port 443

# 5. 非标准端口的管理后台体检
nikto -host http://192.168.0.102:8080

# 6. 只测高危类别：命令执行 + SQL 注入 + 认证绕过
nikto -host http://target -Tuning 89a

# 7. 挂 Burp 代理联动扫描
nikto -host http://target -useproxy

# 8. 带认证扫描内部系统
nikto -host http://target -id admin:pass123

# 9. 温柔模式：每个测试间隔 2 秒 + 限时 10 分钟
nikto -host http://target -Pause 2 -maxtime 600s

# 10. 阳性响应存档，供后续回放分析
nikto -host http://target -Save ./nikto_results

# 11. 多格式报告一次出齐
nikto -host http://target -o report.csv -Format csv
nikto -host http://target -o report.xml -Format xml

# 12. IDS 规避：改变请求编码形态（仅限授权评估）
nikto -host http://target -evasion 1
```

## 六、合规提醒

nikto 是主动漏洞扫描器，动静比目录爆破更大：

1. **书面授权**

   ：nikto 会对目标发起数千个探测请求（含注入类、DoS 类测试项），未授权扫描可能直接触发对方告警甚至法律责任；
2. **生产环境限速**

   ：默认速度对老旧系统可能过载，`-Pause` 放慢、`-maxtime` 限时、避开业务高峰；
3. **Tuning 排除危险项**

   ：给客户生产系统体检时用 `-Tuning x6`（排除 DoS 类）更稳妥；
4. **报告保管**

   ：HTML/CSV 报告含完整漏洞清单，等同攻击地图，加密保管按项目流程流转；
5. **误报要人工复核**

   ：nikto 是老牌扫描器，发现项要结合 Burp/手工验证再写进报告，直接照搬输出容易闹笑话。

---

## 今日小结

1. **nikto**

   = Web 服务器体检医生：2001 年出道至今仍在更新，7000+ 项检查存在 CSV 数据库里，`-update` 保持病历最新；
2. 检查重心和目录爆破不同：**版本过时、危险文件、配置错误、缺失安全头**——是"服务器本身病没病"，不是"有什么路径"；
3. **-Tuning 代码表是效率灵魂**

   ：只跑关心的类别，官网示例 `123bde` 值得当默认起手式；
4. `-useproxy`

   挂 Burp 联动：nikto 地毯式体检 + Burp 精细手术，Web 测试标准双打；
5. 输出格式全家福（txt/htm/csv/xml/json）+ `-Save` 阳性响应存档回放，报告链路完整。

觉得有用的话，**点赞 + 在看 + 转发** 给一起学安全的朋友
关注「每天学一个 Kali 工具」，明天见！

---

**参考资料**

· Kali 官方工具页：https://www.kali.org/tools/nikto/

· 项目主页：https://cirt.net/Nikto2

· GitHub：https://github.com/sullo/nikto

· OffSec WEB-200 课程：Introduction to Nikto

预览时标签不可点

![]()

微信扫一扫
关注该公众号

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/MtjOicQLUtFg3CRl5wFA4loxN8krcYMpuzNjcVibkricNCB4GC9k3ib6UQLsf2RIuOcJFHT568lSjAqz8ze0oMAgxw/0?wx_fmt=png)

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