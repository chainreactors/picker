---
title: DAY 26 · 每天学一个 Kali 工具wpscan：WordPress 站点的\"专属体检医生\"
url: https://mp.weixin.qq.com/s/OxDiR6c5S_5KHjg9ZP2zGA
source: Doonsec's feed
date: 2026-09-26
fetch_date: 2026-09-27T07:20:39.560941
---

# DAY 26 · 每天学一个 Kali 工具wpscan：WordPress 站点的\"专属体检医生\"

# DAY 26 · 每天学一个 Kali 工具wpscan：WordPress 站点的"专属体检医生"

原创

0day收割机
0day收割机

0day收割机

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

DAY 26 · 每天学一个 Kali 工具

# wpscan：WordPress 站点的"专属体检医生"

**🩺 一句话认识 wpscan：**专门给 WordPress 做"全身体检"的黑盒漏洞扫描器——枚举插件、主题、用户、版本，比对漏洞数据库，还能爆破后台密码。全球 40%+ 网站用 WordPress，这把"专科手术刀"你必须有。Ruby 编写，仅 695KB。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ZrTsB3aQgWDbeZw6vicuf5KmmaDOWWJpxCfnia2mZedgpUPBVkAcdDv6Fdgxj98RXRLofOfmX4A6VbOsrUNTku55KnqPic3yuLCe5lLuoWLIfg/640?wx_fmt=png&from=appmsg)

## 写在前面：为什么需要"专科医生"

昨天我们学了 whatweb——它能识别出"这是个 WordPress 站"。但识别出来之后呢？WordPress 有**数万个插件和主题**，每一个都可能藏着漏洞。这时候，通用扫描器（wapiti、nuclei）就不够用了，你需要一把**专打 WordPress 的手术刀**。

| 维度 | whatweb (Day25) | wapiti (Day24) | wpscan (Day26) |
| --- | --- | --- | --- |
| 定位 | 通用指纹识别 | 通用漏洞扫描 | WordPress 专用 |
| 深度 | 识别是什么 | 通用注入探测 | 枚举插件/主题/用户/漏洞 |
| 数据库 | 900+ 指纹插件 | 12 类攻击模块 | WP 专属漏洞库 + API |

**💡 为什么 WordPress 值得一个专用工具？**WordPress 驱动了全球 **40% 以上**的网站。它的插件/主题生态极其庞大，第三方代码质量参差不齐，是黑客眼中的"肥肉"。wpscan 就是针对这个庞然大物量身定做的专科扫描器。

## 一、wpscan 是什么

**WPScan** 是一个**黑盒 WordPress 漏洞扫描器**，它扫描远程 WordPress 站点，找出其中的安全问题：过时的核心版本、有漏洞的插件和主题、暴露的用户名、危险配置、备份文件泄露等。

|  |  |
| --- | --- |
| 版本 | 4.1.0 |
| 体积 | 695 KB（极致轻量） |
| 语言 | Ruby（依赖 ruby-cms-scanner、typhoeus 等） |
| 背书 | 由 Sucuri 赞助，Automattic（WordPress 母公司）项目 |
| 理念 | 黑盒扫描——从外部枚举与探测，不需要源码 |

## 二、官网示例精讲

一条命令，枚举目标站的所有插件：

```
root@kali:~# wpscan --url http://wordpress.local --enumerate p
```

| 参数 | 含义 |
| --- | --- |
| --url | 目标 WordPress 站点 URL |
| --enumerate p | 枚举热门插件（p = popular plugins） |

**输出结果解读：**

```
        WordPress Security Scanner by the WPScan Team

[+] URL: http://wordpress.local/
[+] Started: Mon Jan 12 14:07:40 2015

[+] robots.txt available under: 'http://wordpress.local/robots.txt'
[+] Interesting entry from robots.txt: http://wordpress.local/search
[+] Interesting header: SERVER: nginx
[+] Interesting header: X-FRAME-OPTIONS: SAMEORIGIN
[+] XML-RPC Interface available under: http://wordpress.local/xmlrpc.php

[+] WordPress version 4.2-alpha-31168 identified
    from rss generator

[+] Enumerating installed plugins  ...
    Time: 00:00:35 (2166 / 2166) 100.00%

[+] We found 2166 plugins:
[...]
```

**📊 一次扫描的收获：**
• 解析 **robots.txt**，挖出隐藏路径（/search、/archive 等）
• 识别 **Web 服务器**（nginx）和安全头（X-FRAME-OPTIONS）
• 发现 **XML-RPC 接口**（常被用于暴力破解和放大攻击）
• 识别 **WordPress 版本**（4.2-alpha-31168）
• 枚举出 **2166 个插件**——每一个都是潜在的漏洞入口

![](https://mmbiz.qpic.cn/mmbiz_jpg/ZrTsB3aQgWA3zQFvhJxZOQDNjgmYWiawWjbJvmCR2ErHTpgTEs3xpD8tjWYu4jWAj6Dqgu8Hic6S29PGIUJqR5hveqY1gl92YQgbBqYqwyQBw/640?wx_fmt=jpeg)

## 三、核心能力：-e 枚举一切

`-e`（--enumerate）是 wpscan 的灵魂，能枚举 WordPress 的方方面面：

| 选项 | 枚举内容 |
| --- | --- |
| vp | 有漏洞的插件（Vulnerable Plugins） |
| ap | 所有插件（All Plugins） |
| p | 热门插件（Popular Plugins） |
| vt | 有漏洞的主题（Vulnerable Themes） |
| at / t | 所有主题 / 热门主题 |
| tt | Timthumb 脚本（易被利用的图片脚本） |
| cb | 配置文件备份（Config Backups） |
| dbe | 数据库导出文件（Db Exports） |
| bf | 备份文件夹（Backup Folders） |
| u | 用户 ID（如 u1-5，枚举用户名） |
| m | 媒体 ID（如 m1-15） |

```
# 枚举所有漏洞插件 + 漏洞主题 + 用户
wpscan --url http://target.com -e vp,vt,u

# 不带参数 = 默认枚举全部
wpscan --url http://target.com -e
```

## 四、漏洞情报：API Token

wpscan 光枚举出插件还不够，关键是**告诉你这些插件有没有已知漏洞**。这背后靠的是 WPScan 官方漏洞数据库（data.wpscan.org）。

注册一个免费的 API Token，就能让扫描结果显示每个插件/主题的 CVE 编号、漏洞详情、修复建议：

```
# 带 API Token，输出漏洞详情
wpscan --url http://target.com -e vp,vt \
  --api-token 你的TOKEN

# Token 申请地址：https://wpscan.com/profile
```

**💡 免费额度：**WPScan API 对个人非商业用途提供免费额度（每天有限次数请求），足够学习和小规模测试。商业批量扫描需要付费订阅。

![](https://mmbiz.qpic.cn/mmbiz_jpg/ZrTsB3aQgWBMO4Zvy5sDJXLwbTuibTyiaTKC9eTeOItPNgDYV77sB1A2DsBRrJb59AVPcKLduCJDz5tW55F1Nz0MJEc1TqaVWBXpmRDIiahLaI/640?wx_fmt=jpeg)

## 五、检测模式与密码爆破

### 三种检测模式

| 模式 | 说明 |
| --- | --- |
| passive | 被动：不额外发请求，最隐蔽 |
| mixed | 混合（默认）：平衡速度与准确性 |
| aggressive | 激进：主动探测，最准但最容易被发现 |

### 后台密码爆破

wpscan 内置 WordPress 密码攻击，支持三种方式（`--password-attack`）：

```
# 用字典爆破 admin 用户
wpscan --url http://target.com \
  -U admin -P /usr/share/wordlists/rockyou.txt

# 三种攻击方式：wp-login / xmlrpc / xmlrpc-multicall
# xmlrpc-multicall 一次请求试多个密码，速度最快（仅 WP < 4.4）
```

## 六、参数速查表

| 参数 | 说明 |
| --- | --- |
| --url URL | 目标站点（必选） |
| -e [OPTS] | 枚举：vp/ap/p/vt/at/t/tt/cb/dbe/bf/u/m |
| --api-token | WPScan API Token，显示漏洞详情 |
| --detection-mode | mixed/passive/aggressive |
| -U / -P | 密码爆破的用户名 / 密码字典 |
| --password-attack | wp-login/xmlrpc/xmlrpc-multicall |
| -t NUM | 并发线程（默认 5） |
| -o FILE / -f FORMAT | 输出文件 / 格式（json/jsonl/sarif/cli） |
| --rua | 随机 User-Agent |
| --stealthy | 隐蔽模式（= --rua + passive 检测） |
| --proxy | 走代理（可挂 Burp） |
| --wp-auth | 用 WP 应用密码登录，读取权威插件/主题清单 |
| --update | 更新漏洞数据库 |

## 七、工具链联动

| 联动工具 | 用法 |
| --- | --- |
| whatweb (Day25) | whatweb 先确认是 WordPress 站 → wpscan 深度体检 |
| nmap (Day01) | nmap 扫全网找 Web 端口 → wpscan 逐个筛 WordPress 站 |
| Burp Suite (Day19) | wpscan 挂 Burp 代理，抓包分析每个请求 |
| nuclei (Day22) | wpscan 查出漏洞插件 → nuclei 验证可利用性 |
| hydra | wpscan 爆破后台，也可导出用户名交给 hydra 继续 |

**🔗 典型流水线：**
`whatweb 识别 WP → wpscan 枚举漏洞 → 带 API Token 出情报 → 针对漏洞插件精准打击`

## 八、实战速查 10 条

```
# 1. 基础扫描
wpscan --url http://target.com

# 2. 枚举漏洞插件和主题（最常用）
wpscan --url http://target.com -e vp,vt

# 3. 带 API Token 输出漏洞详情
wpscan --url http://target.com -e vp,vt \
  --api-token YOUR_TOKEN

# 4. 枚举用户（为爆破做准备）
wpscan --url http://target.com -e u

# 5. 后台密码爆破
wpscan --url http://target.com -U admin \
  -P /usr/share/wordlists/rockyou.txt

# 6. 隐蔽模式（随机 UA + 被动检测）
wpscan --url http://target.com --stealthy

# 7. 输出 JSON 报告
wpscan --url http://target.com -e vp,vt \
  -f json -o report.json

# 8. 挂 Burp 代理
wpscan --url http://target.com --proxy http://127.0.0.1:8080

# 9. 提高并发加速
wpscan --url http://target.com -e ap -t 20

# 10. 更新漏洞数据库
wpscan --update
```

## 九、合规提醒

**⚠️ 安全与法律边界：**
1. wpscan 是**主动扫描 + 密码爆破工具**，**必须获得书面授权**，尤其密码爆破可能触发账户锁定，务必谨慎
2. 未经授权的 WordPress 扫描和爆破可能违反《网络安全法》及计算机犯罪相关法规
3. 枚举和爆破会产生大量请求，用 `--throttle` 或 `-t` 控制速率，避免打崩目标
4. wpscan 是**防御利器**：站长可用它自查自己站点的暴露面和过时插件
5. 漏洞情报和爆破结果含敏感信息，注意保密，切勿公开传播或用于非法入侵

## 今日小结

wpscan 是 WordPress 世界的"专科体检医生"：

|  |  |
| --- | --- |
| 专科专用 | 只做 WordPress，但做到极致深入 |
| 枚举全面 | 插件/主题/用户/版本/备份/数据库导出，一网打尽 |
| 漏洞情报 | API Token 接入官方漏洞库，直出 CVE 和修复建议 |
| 爆破能力 | wp-login/xmlrpc 多种密码攻击方式 |
| 权威背书 | Sucuri 赞助、Automattic 项目，业界标准 |

占全球 40% 网站的 WordPress，是攻击者的头号目标，也是防御者的必守之地。wpscan 用 695KB 的小身材，装下了整个 WordPress 安全生态的"病历本"——无论你是渗透测试者还是 WordPress 站长，它都是不可或缺的利器。

**觉得有用？**点个「在看」👇 让更多人知道
关注本号，每天 5 分钟，学一个 Kali 工具

**参考资料：**
• Kali 官网：https://www.kali.org/tools/wpscan/
• WPScan 官方网站：https://wpscan.com/
• GitHub：https://github.com/wpscanteam/wpscan

预览时标签不可点

不喜欢

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