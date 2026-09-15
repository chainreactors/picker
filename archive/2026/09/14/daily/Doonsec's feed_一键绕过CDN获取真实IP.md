---
title: 一键绕过CDN获取真实IP
url: https://mp.weixin.qq.com/s/YO8IEgpleGAbIw0rTX4kug
source: Doonsec's feed
date: 2026-09-14
fetch_date: 2026-09-15T06:56:56.793391
---

# 一键绕过CDN获取真实IP

# 一键绕过CDN获取真实IP

点击关注👉
点击关注👉

马哥网络安全

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

### 工具介绍

**穷尽一切手段，扒光 CDN 的底裤，找到真实 IP。**

一个为 Claude Code 打造的自动化 CDN 源站溯源技能（Skill）。输入目标域名，自动按优先级执行 40+ 种 OSINT 方法，构建证据链，输出最终判定。

```
╔══════════════════════════════════════════════════╗║  真实 IP:  103.***.**.32                        ║║  置信度:  确定 (95%+)                            ║║  归属地:  中国广东深圳 · 电信                     ║║  证据链:  [S] SSL证书精确匹配                    ║║          [A] 历史DNS记录确认                     ║║          [A] HTTP行为差异验证                     ║╚══════════════════════════════════════════════════╝
```

![](https://mmbiz.qpic.cn/mmbiz_png/5yYXmGfnscR64bDkoNNHfTpdvuSoDibdN9VYh6RV7obLvVBMmsEY38AbxfvULbRSekkyPE0D4QpCicOnoYpOnxRjk7NSZhyWp1TFAKIU67S1k/640?wx_fmt=png&from=appmsg&watermark=1#imgIndex=0)

### 它能做什么

无论目标藏在哪家 CDN 后面——Cloudflare、腾讯 EdgeOne、阿里云、AWS CloudFront、Akamai、Fastly、Azure、Imperva、Sucuri、华为云、网宿、百度云，**乃至任何不在名单里的未知 CDN**——FUCK-CDN 都会按成本从低到高依次尝试：

| 优先级 | 方法 | Token 成本 |
| --- | --- | --- |
| **P0** | SPF/MX/TXT 记录泄露、IPv6 直连、历史 DNS 回溯 | 极低 |
| **P1** | SSL 证书序列号精确比对、子域名枚举、HTTP Server 头行为差异分析 | 中 |
| **P2** | Shodan / FOFA / Censys / ZoomEye / Quake / Hunter 空间搜索、Favicon Hash、全端口扫描 | 较高 |
| **P3** | 邮件头溯源、JS 源码审计、同组织域名关联、GA/AdSense ID 反查、CDN 特定绕过 | 高 |
| **P4** | 深度挖掘：Web Archive 考古、源码配置审计、被动情报、云厂商元数据、WAF 穿透、时间维度攻击、社工辅助、网络拓扑推断 | 极高 |

**P0 命中就收工，不浪费一个 Token。** 没命中才升级到下一级。P0-P3 + CDN 特定/通用绕过全部失败？P4 会穷尽一切非常规手段死磕到底。找到候选 IP 后自动进入验证阶段——SSL 证书比对 + HTTP 行为对比 + IP 反查——三重交叉验证，给出置信度评级。

### 安装

### 方式一：克隆整个项目（推荐）

```
git clone <repo_url> FUCK-CDNcd FUCK-CDNclaude
```

克隆后直接在项目目录启动 Claude Code，技能自动加载。

### 方式二：只装技能文件

如果你已有自己的项目，只需把技能文件复制进去：

```
# 在你的项目根目录执行mkdir -p .claude/skillscurl -o .claude/skills/fuck-cdn.md \  <repo_raw_url>/.claude/skills/fuck-cdn.md
```

或者手动操作：

1. 下载 `.claude/skills/fuck-cdn.md`
2. 放到你项目的 `.claude/skills/` 目录下（没有就新建）
3. 在项目目录启动 Claude Code

### 方式三：全局安装（所有项目可用）

```
# 放到用户级 skills 目录，所有项目共享mkdir -p ~/.claude/skillscp .claude/skills/fuck-cdn.md ~/.claude/skills/
```

### 验证安装

启动 Claude Code 后输入 `/` 查看可用技能列表，应能看到 `fuck-cdn`。

## 使用

### 基本用法

在 Claude Code 中直接调用：

```
/fuck-cdn example.com
```

或者用自然语言：

```
帮我查 example.com 的真实IP
```

### API Key 配置

有两种方式配置 API Key：

#### 方式一：直接编辑 Skill 文件（推荐，一劳永逸）

#### 打开 `.claude/skills/fuck-cdn.md`，找到顶部的 API Key 配置区，把你的 Key 填进去：

```
SHODAN_API_KEY     = "你的Key"FOFA_EMAIL         = "你的邮箱"FOFA_API_KEY       = "你的Key"CENSYS_API_ID      = "你的ID"CENSYS_API_SECRET  = "你的Secret"SECURITYTRAILS_KEY = "你的Key"ZOOMEYE_API_KEY    = "你的Key"QUAKE_API_KEY      = "你的Key"HUNTER_API_KEY     = "你的Key"VIRUSTOTAL_KEY     = "你的Key"
```

填好后每次调用自动使用，无需重复输入。

**安全提示**：如果你的项目是公开仓库，**不要提交含 Key 的 skill 文件**。建议将 `.claude/skills/fuck-cdn.md` 加入 `.gitignore`，或只在本地 / 全局安装（`~/.claude/skills/`）中填写 Key。

#### 方式二：对话中临时提供

在对话中直接告诉 Claude 你的 Key，仅在当前会话内存中使用，不写入任何文件：

```
我的 Shodan key 是 xxxx，FOFA 邮箱是 xxx key 是 xxx帮我查 example.com 的真实IP
```

#### 支持的平台

| 平台 | Key 格式 | 免费额度 | 用途 |
| --- | --- | --- | --- |
| Shodan | `SHODAN_API_KEY` | 注册即有 | 按证书/favicon/标题搜索持有相同特征的 IP |
| FOFA | `FOFA_EMAIL` + `FOFA_API_KEY` | 注册即有 | icon\_hash、证书、body 关键字搜索 |
| Censys | `CENSYS_API_ID` + `CENSYS_API_SECRET` | 注册即有 | 证书指纹 SHA256 精确搜索 |
| SecurityTrails | `SECURITYTRAILS_KEY` | 免费 50次/月 | 历史 DNS 记录、子域名枚举 |
| ZoomEye | `ZOOMEYE_API_KEY` | 注册即有 | 证书、标题搜索 |
| 360 Quake | `QUAKE_API_KEY` | 注册即有 | 证书搜索 |
| 鹰图 Hunter | `HUNTER_API_KEY` | 注册即有 | 证书搜索 |
| VirusTotal | `VIRUSTOTAL_KEY` | 免费 500次/天 | 解析历史、子域名枚举 |

**没有任何 Key 也能用。** P0 和 P1 阶段的所有方法（历史 DNS、证书比对、子域名枚举、HTTP 行为分析）不需要 Key，命中率已经很高。Key 的价值在 P2 阶段——空间搜索引擎能大幅提升对高防目标的命中率。

## 实战截图

### 案例一

### ![](https://mmbiz.qpic.cn/mmbiz_png/5yYXmGfnscTQibEDPMxSpqFicujaBUGicLVaEAfJIjuqWeIxbdXibRhhOZEe1yK1LBAPvUazCpRVXWlsdgY3hF52jqXeFsAXO7jgE7U8icnUltic0/640?wx_fmt=png&from=appmsg&watermark=1#imgIndex=1) ![](https://mmbiz.qpic.cn/mmbiz_png/5yYXmGfnscTW6DmLL6yAknLJ4hvq3IOFvRaX5wYTH55pSIgvJrVqeZZkJRmGNDGMfCEeLESYAyobvp4yjLzf67At9sy6VygrnOvpYPYibe2A/640?wx_fmt=png&from=appmsg&watermark=1#imgIndex=2)

### 项目地址

### https://github.com/0xShe/FUCK-CDN

### 内容转自乌雲安全，侵删

![图片](https://mmbiz.qpic.cn/mmbiz_png/uGzSjYYxdSzgPJXtHHtAcEwtWoDRo59hpSV8MMeXoGvdPXyPMIQa7mZJtqXj7yquVBibyKl2rbgbk6Wby4Dh5tfhOwibg5mh51N0ajbIZf6uw/640?from=appmsg&wxfrom=5&wx_lazy=1&tp=webp#imgIndex=40)

文末公开课分享

【免费公开课】

从GPU到AI-SRE：100分钟搭建、监控并智能诊断大模型服务

⏰ 9月16日晚20:00 | 创始人马哥亲授

零基础想入行Linux运维、有基础想进阶K8s/SRE、

对AI感兴趣但没算法背景的宝子，都适合听

想学的宝子，扫码预约听课🔥

![](https://mmbiz.qpic.cn/mmbiz_png/2I159AwKj56GWlFpAuJBpDq9xgZp8de9R91BMgAgGaf5D4gwsyWl1FR9RN64BiaJqzxqDicCAgoKtwb9LPrZm4c15qTds6Ux29Cda2avFL0mY/640?wx_fmt=png&from=appmsg)

![图片](https://mmbiz.qpic.cn/mmbiz_jpg/2I159AwKj55NicqiaJ3E3PG15UhbwTkJIibKq06Tic19PW9WDsOuWdwHluv2t5GLJbtHZ56NIhOpZPKpQpTZgZ6NLMJ2Et8vFAZLI3MdIEmu2icU/640?wx_fmt=jpeg&from=appmsg&wxfrom=5&wx_lazy=1&tp=webp#imgIndex=42)

###

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/UkV8WB2qYAnOoZBIicAo3zEb7I6rU7bM6SZGvLjU26JzsajoMuu3oLacM4XPJ9O91942IelPRTHSQFso09IxvVg/0?wx_fmt=png)

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