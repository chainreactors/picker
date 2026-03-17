---
title: WatchVuln_Web高价值漏洞采集与推送
url: https://mp.weixin.qq.com/s/36x_CgbTO9qJvEG7ZGBKbw
source: Doonsec's feed
date: 2026-03-16
fetch_date: 2026-03-17T04:13:03.236232
---

# WatchVuln_Web高价值漏洞采集与推送

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/105Qt3DpWpib9fksgb0Xbfg3toYHZ9ngrUTorFckPLZib0No9Xjuu3mUs7BkrGlzvDn3RLeM8CCGdqEEkQE1SDa9VXz8Q249tpX5b9PDXuqVs/0?wx_fmt=jpeg)

# WatchVuln\_Web高价值漏洞采集与推送

原创

SXdysq
SXdysq

南街老友

![]()

在小说阅读器中沉浸阅读

# WatchVuln\_Web

WatchVuln 的二开版本，在原版命令行工具的基础上增加了 Web 管理控制台，提供可视化配置界面，方便用户管理漏洞监控和推送设置。

## 功能特性

### Web 管理控制台

* • **可视化配置界面**：通过 Web 页面配置所有功能，无需修改配置文件
* • **实时监控状态**：查看漏洞库数量、最近更新时间、下次检查时间
* • **手动触发检查**：一键触发漏洞检查，无需等待定时任务
* • **操作日志**：记录所有配置变更和推送记录

![](https://mmbiz.qpic.cn/mmbiz_png/105Qt3DpWp9sD0UkqbKiapLMZ7R4rJWCvHSR2lAkBMbqzicfpsoEcydTacc0AjmPXxyYvoHugQib8JzBeqAJicl9Hib1l0DPXE3GBib7n7ukSrjuk/640?wx_fmt=png&from=appmsg)

### 数据源

支持以下漏洞信息源：

| 数据源 | 说明 |
| --- | --- |
| 阿里云漏洞库 (AVD) | 高危/严重漏洞 |
| 长亭漏洞库 | 高危/严重漏洞（中文标题） |
| OSCS 开源安全情报 | 高危/严重漏洞（预警标签） |
| 奇安信威胁情报中心 | 高危漏洞（特定标签） |
| 微步在线 | 高危/严重漏洞 |
| Seebug 漏洞平台 | 高危/严重漏洞 |
| 启明星辰 | 高危/严重漏洞 |
| CISA KEV | 全部漏洞 |
| Apache Struts2 | 高危/严重漏洞 |

![](https://mmbiz.qpic.cn/sz_mmbiz_png/105Qt3DpWpic9XeZiaDb7YGaxw6H4ZpbxPicWe4wmw0qiaacQNc4lwczVhFJjYxvr8tkhQPG6FfQtEiajg5pHcWCG1Uf9BjibLSIlibWxcNyadKuMg/640?wx_fmt=png&from=appmsg)

### 推送渠道

支持多种推送方式：

* • 钉钉群机器人
* • 飞书群机器人
* • 微信企业版
* • Server 酱
* • PushPlus
* • Telegram Bot
* • Slack Webhook
* • Bark
* • 蓝信
* • 自定义 Webhook

![](https://mmbiz.qpic.cn/mmbiz_png/105Qt3DpWpicwz4PDnPbnFaoYjbjBtFbhjNjwxhXX9xgOqZXI8yvWic968rPuX0HpKUc31lwDVloTSozoCvXJYn5PYgDs4dmA9DnT84g5HoOw/640?wx_fmt=png&from=appmsg)

## 快速开始

### 直接运行

```
# 运行（默认监听 0.0.0.0:8080）
./WatchVuln_Web-windows-amd64.exe --console
```

首次启动会生成随机登录密码，请注意查看日志。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/105Qt3DpWpica4e3AG9C0sOqJMHlTRMKDXHicK1my2dcHDfh9LDP7LPyicNB2dD22blYz2PjPSLIIXkMxrKUpJxB0Lp50D2d0gRZO6eqmfmbaM/640?wx_fmt=png&from=appmsg)

## 配置说明

启动后访问 `http://localhost:8080`，使用 admin 账号登录（每次启动密码会随机生成，见日志）。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/105Qt3DpWpibBn3ibcibm6XRicbDSVEYrQ3v1xTPDz8HjIvnLtEVCVpIXdbgMS6NCydxTy1W3tyex1EWaZz6rgw2EDa38OOshjbhNnhOjZ5gQ9o/640?wx_fmt=png&from=appmsg)

### 监控配置

* • **检查间隔**：设置漏洞检查周期（15分钟/30分钟/1小时/2小时/6小时）
* • **数据源选择**：勾选需要监控的漏洞源
* • **关键词过滤**：设置白名单/黑名单关键词过滤
* • **CVE 过滤**：开启后多个源的同一 CVE 只推送一次

![](https://mmbiz.qpic.cn/sz_mmbiz_png/105Qt3DpWpibBtZPJD8lXqRGBND55FJF5ib2YKiaFhHL2MusudS5eI53OevUTGuJibB2oAOic6C8G6vyGfUQLiarPibovpP36FJL8y4QBj2vC1QYPY/640?wx_fmt=png&from=appmsg)

### 推送配置

配置推送渠道的访问凭证，每个渠道可独立开启/关闭。

### 代理配置

支持 HTTP/SOCKS5 代理，用于访问需要代理的数据源。

## 配置数据存储

配置信息存储在 SQLite 数据库中（`vuln_v3.sqlite3`），包括：

* • 登录凭据（bcrypt 加密）
* • 监控配置（数据源、检查间隔等）
* • 推送渠道配置
* • 代理设置

## 相关链接

* • 原版项目：zema1/watchvuln（https://github.com/zema1/watchvuln）
* • 数据来源：阿里云 AVD、长亭漏洞库、OSCS、奇安信、微步、Seebug、启明星辰、CISA KEV、Apache Struts2

## 工具获取

关注公众号

发送WatchVuln\_Web获取下载地址。

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/dfviaLov8RtDh0smUOwWjuqU0hZH5wjOZVv69y5Q3stMXiaXKDgicWX93nJMStS2mqjhGyof1QicoiaLvqmV5RDZ8pQ/0?wx_fmt=png)

南街老友

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/dfviaLov8RtDh0smUOwWjuqU0hZH5wjOZVv69y5Q3stMXiaXKDgicWX93nJMStS2mqjhGyof1QicoiaLvqmV5RDZ8pQ/0?wx_fmt=png)

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