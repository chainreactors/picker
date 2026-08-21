---
title: Web漏洞扫描工具 -- Webscanner
url: https://mp.weixin.qq.com/s/cEWF0XVx5NW4qTzkIFoy2g
source: Doonsec's feed
date: 2026-08-20
fetch_date: 2026-08-21T03:01:52.230229
---

# Web漏洞扫描工具 -- Webscanner

# Web漏洞扫描工具 -- Webscanner

huocai250
huocai250

Web安全工具库

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

===================================

**免责声明**

请勿利用文章内的相关技术从事非法测试，由于传播、利用此文所提供的信息而造成的任何直接或者间接的后果及损失，均由使用者本人负责，作者不为此承担任何责任。工具来自网络，安全性自测，大家都要把工具当做病毒对待，在虚拟机运行。如有侵权请联系删除。个人微信：ivu123ivu

**0x01 工具介绍**

WebVulnScanner 是一款检测 / 评估型安全扫描器（与 OWASP ZAP、Nikto、Nuclei 同类）： 它探测目标是否存在常见漏洞、梳理攻击面并给出整改建议，不包含利用、提权、 数据窃取或持久化功能（详见「关于漏洞利用」）。请仅在已获得书面授权的目标上使用。v9 亮点：新增 YAML 模板签名引擎（可无代码扩展规则）、内置 1000+ 检测规则/签名、 35 个检测模块，并新增 JS 密钥、敏感路径暴露、API 发现、缓存投毒、版本漏洞、 前端安全、子域名接管等模块。

```
信息收集与指纹：爬虫、信息收集、指纹识别（60+ 规则）、版本漏洞提示、 robots/sitemap/well-known 情报、子域名枚举、子域名接管指纹。配置与传输：安全头（9 项）、SSL/TLS、配置错误/点击劫持、前端安全（SRI/混合内容/CSP）、 HTTP 方法、Host 头注入、CORS、CSRF。信息泄露：敏感信息、JS 密钥/端点、敏感路径暴露（600+ 路径）、 模板签名库（YAML，可扩展）、API 文档发现、CMS 专项。注入与漏洞：SQL 注入、XSS/SSTI、LFI/命令注入、路径穿越、XXE、SSRF、 CRLF 注入、开放重定向、缓存投毒、Log4Shell、JWT 安全。主动扫描：端口扫描（60+ 高危端口）、目录枚举。
```

**0x02 安装与使用**

常用命令：

```
pip install -r requirements.txtpip install flask        # 仅使用 Web UI 时需要
# 基本扫描（启动时显示已加载规则总量）python main.py https://example.com
# 快速模式（跳过端口/目录/暴露/子域名等重型模块）python main.py https://example.com --fast --html report.html
# 被动模式（仅非侵入式检测）python main.py https://example.com --passive
# 追加自定义模板 + 插件python main.py https://example.com --templates my_templates --plugins plugins
# 带外探测（Log4Shell/SSRF）指定你自己的 collaboratorpython main.py https://example.com --canary your.collaborator.net
# 批量扫描python main.py -f targets.txt --concurrency 5 --html out.html
# Web UIpython main.py --web        # http://127.0.0.1:5000
# 作为模块运行python -m webscanner https://example.com
```

网盘下载链接（一定要在虚拟机运行）：

```
后台回复：20260820获取下载链接，仅一天有效
```

**·****今 日 推 荐****·**

|  |  |
| --- | --- |
| ![](https://mmbiz.qpic.cn/mmbiz_jpg/U7LDNXUGXQvRM7omc2ES2NSLMZ2Nbib7VftC67uHpXxKTZqyibjeicgibLRzg0Xiao8B2x6JB25gOIdKTSwHD3F28Ek94lQmlM9E8xkAHvRjrLHw/640?wx_fmt=jpeg) | ![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/8H1dCzib3UibsC4yYFwgTnJrN0q57DearHJhaWSE6XQllpkUviaibg5MqTYgdUQYDNt8ysfV2v6o4jsN34pmq3DAOg/640?wx_fmt=jpeg&from=appmsg) |

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