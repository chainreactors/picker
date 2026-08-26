---
title: 若依专项漏洞扫描工具 -- Ruoyi-Scan
url: https://mp.weixin.qq.com/s/VAqE3rnRNnz8s0a1Zth6ig
source: Doonsec's feed
date: 2026-08-25
fetch_date: 2026-08-26T03:04:03.619588
---

# 若依专项漏洞扫描工具 -- Ruoyi-Scan

# 若依专项漏洞扫描工具 -- Ruoyi-Scan

xiabai2008
xiabai2008

Web安全工具库

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

===================================

**免责声明**

请勿利用文章内的相关技术从事非法测试，由于传播、利用此文所提供的信息而造成的任何直接或者间接的后果及损失，均由使用者本人负责，作者不为此承担任何责任。工具来自网络，安全性自测，大家都要把工具当做病毒对待，在虚拟机运行。如有侵权请联系删除。个人微信：ivu123ivu

**0x01 工具介绍**

若依（RuoYi）专项漏洞扫描器 — 插件化 / 三态判定 / WAF绕过 / 利用链 / AI生成POC / nuclei模板兼容 / 组件版本检测 / Web API

**0x02 安装与使用**

常用命令：

```
# 单目标漏洞扫描python main.py -p http://target:8080/
# 批量扫描python main.py -f targets.txt -p --report ./reports
# 手动指定 CMS（跳过指纹识别）python main.py -p http://target:8080/ --cms ruoyi
# 综合扫描（目录扫描 + 漏洞检测 + 登录爆破）python main.py -u http://target:8080/
# 生成全格式报告（HTML/JSON/CSV/PDF/Word/Excel）python main.py -p http://target:8080/ --report ./reports --report-format all
# WAF 绕过（检测到 WAF 自动启用）python main.py -p http://target:8080/ --bypass-waf auto
# 执行漏洞利用链python main.py --chain ruoyi_sql_to_rce -u http://target:8080/python main.py --chain list  # 列出可用链
# 组件版本检测（fastjson/SpringBoot/Shiro/Nacos/Log4j → CVE 比对）python main.py -p http://target:8080/ --components
# 执行 nuclei 模板（nuclei-templates 生态直接复用）python main.py -p http://target:8080/ --nuclei examples/nuclei/python main.py --nuclei-validate examples/nuclei/  # 模板校验（不扫描）
# AI 生成插件（LLM 自验证回灌；无 Key 时降级规则模板）python main.py --ai "检测若依任意文件读取漏洞" --category ruoyi
# 插件模板仓库（社区分发）python main.py --plugin-export ./ruoyi-scan-templatespython main.py --plugin-manifest ./ruoyi-scan-templates  # 生成/校验 manifest（Ed25519 签名）python main.py --plugin-update  # 从官方仓库更新插件
# Web API 服务python main.py --serve# 访问 http://localhost:8000/ (Web 控制台)# 访问 http://localhost:8000/docs (OpenAPI 文档)
# 端口扫描 + 漏洞检测python main.py -p http://target:8080/ --portscan
# 被动代理模式python main.py --passive --passive-port 8080
# Docker 部署（见下方「Docker 部署」章节）# docker-compose up -d
```

网盘下载链接（一定要在虚拟机运行）：

```
后台回复：20260825获取下载链接，仅一天有效
```

**·****今 日 推 荐****·**

|  |  |
| --- | --- |
| ![](https://mmbiz.qpic.cn/mmbiz_jpg/U7LDNXUGXQuibiciaRzwfw5QtjwDHvtwKHBLVriaD1picuNUblTthG4Tk5T547z2glCmTFXcVNtTcMmwiavVcbtgLuy4kZKEEPG6QjHYkkEJCGtSU/640?wx_fmt=jpeg&from=appmsg) | ![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/8H1dCzib3UibsC4yYFwgTnJrN0q57DearHJhaWSE6XQllpkUviaibg5MqTYgdUQYDNt8ysfV2v6o4jsN34pmq3DAOg/640?wx_fmt=jpeg&from=appmsg) |

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/8H1dCzib3UibvAJDLSoAcyS63uxfNryXVibVJx8MiaiaibYmLj4Zk1fPdTYCsDjIEEoiaF1BPQydFZornyvv10iarEPCkg/0?wx_fmt=png)

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