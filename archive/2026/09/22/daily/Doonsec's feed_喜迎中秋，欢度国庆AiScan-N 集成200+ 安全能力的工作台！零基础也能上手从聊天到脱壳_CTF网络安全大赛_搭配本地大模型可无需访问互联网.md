---
title: 喜迎中秋，欢度国庆AiScan-N 集成200+ 安全能力的工作台！零基础也能上手从聊天到脱壳|CTF网络安全大赛|搭配本地大模型可无需访问互联网
url: https://mp.weixin.qq.com/s/JcQEi6H-G8r_0dT_Ue2bVw
source: Doonsec's feed
date: 2026-09-22
fetch_date: 2026-09-23T06:53:15.192116
---

# 喜迎中秋，欢度国庆AiScan-N 集成200+ 安全能力的工作台！零基础也能上手从聊天到脱壳|CTF网络安全大赛|搭配本地大模型可无需访问互联网

# 喜迎中秋，欢度国庆AiScan-N 集成200+ 安全能力的工作台！零基础也能上手从聊天到脱壳|CTF网络安全大赛|搭配本地大模型可无需访问互联网

原创

渗透测试
渗透测试

渗透测试

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/z3TOtprWtZicsu6bga7V3SVVpfUvMe0icicfJ0a5bQbVAcWNs4GJH0tFic0AWdE6KQZyEvngWoK2szjLlcftOFczXQ/640?wx_fmt=other&wxfrom=5&wx_lazy=1&wx_co=1&randomid=d3ftoiiz&watermark=1&tp=webp#imgIndex=0)

**点击上方蓝字******关注【渗透测试】不迷路****

>       AiScan-N 是一款人工智能驱动的 AI 自动化网络安全（运维）工具，把「AI 对话」和「安全工具链」装进同一个网页工作台：你只需要用中文说出目标，它自己调用工具、执行任务、输出结果与报告——支持 Windows / Linux / macOS / 统信 UOS / WSL 运行，手机浏览器也能用。

**适合谁：安全初学者与零基础入门者、企业安全与运维人员、渗透测试与应急响应从业者、CTF 与逆向爱好者、需要做 App 安全评估的移动端开发者。**

本篇文章介绍了AiScan-N的相关功能介绍：AI 对话与任务、记忆与能力扩展、Skills技能中心、POC&EXP管理、MCP管理、工具Tools、APP逆向、Android 控制中心、流量与抓包、子域名收集、Webshell管理、指纹识别、消息频道、定时任务、实时监控 GitHub、资产与风险、状态与安全等能力。

    严正声明：本工具仅供合法合规的安全研究、教学培训、接口调试、自有系统测试及已获得明确授权的安全评估使用。用户必须对自身行为负责，严格遵守法律。任何将工具用于违法犯罪的行为均被严格禁止，由此工具产生的全部法律责任问题均由用户自行承担一切后果，开发者概不负责。

## 项目地址：

```
https://github.com/SecNN/AiScan-N
```

## **Stars：** 451+　|　**语言：中文** 跨平台（Windows / Linux / macOS / WSL / UOS）　|　定位： Ai 自动化网络安全工具【CLI Agent】

一、AI 对话与任务

说一句话就能下达任务，AI 自己把需求拆成步骤执行。 怎么用：输入「对已授权的站点做一次信息收集」，它自己决定先做什么、后做什么。**自动调用工具、**全过程可见、**随时暂停继续** 、**生成中插话、**多任务并行、**消息管理、**会话归档、**对话备注等操作。**************

![](https://mmbiz.qpic.cn/sz_mmbiz_png/EZicQGyMXoOkURlWHYZNS4xKGJYOh6X22aUsIuGOPkHlnV6foX8lF7MoiaBXM8ibcWribic0oHjibpMBBLdV6QsFoQic7gkQD4GfIibYN2RRkIzT4OY/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/EZicQGyMXoOl6wRf2Sz3KvZ3Yp27ia4FChJpy3riaNqlwwLfDOF2giaCGXFOQiaiaNJ1vg6kibDCfSrMByGMwzXe8aicHawq0wUBnhaamSTmExAg9ibM/640?wx_fmt=gif&from=appmsg)

****场景模板：** 内置 20 + 个常用任务模板，一键套用。 怎么用：想不起怎么写提示词，直接点模板（如「Web 日志应急」）就能跑。**

![](https://mmbiz.qpic.cn/sz_mmbiz_png/EZicQGyMXoOlXOQzLKk6nlyc2JoerHSDicXQfyicFWdLOXV8x3803XsicCmor2DiblsFwGa3pFA9676aQQgoUYqps7ZKTy4fiaTabB21J1kv9nnmc/640?wx_fmt=png&from=appmsg)

## 对话流程示意图

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/EZicQGyMXoOntGl1RcbII18icGYKQzxQTuxOJAHict8ZS7NXwibc3YnUwzP7KXjTA5oU6ucz5s1VffmZYtic0GpLDUG4oc0rPuEqL8yibsibdibeCqs/640?wx_fmt=gif&from=appmsg)

🌐 HTTP(S) 访问流量

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/EZicQGyMXoOmekYpczr6ib44oywkwhTfuVmWUFXVa5MknXEwJxhfS4RSfHAVMIRA5ASlic0D25ib0BTSpuvAS2rq5wiaBYib9d910wvofh3ic9IpC4/640?wx_fmt=gif&from=appmsg)

态势感知： 实时任务态势、登录风险 IP、渗透测试态势、终端统计集中展示。

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/EZicQGyMXoOk3qCF7KQhGYGJfb3nTB1D8XVGogQBKDSdnHR1YzPaYhBEicYkxYwOVW3VQUdr8fno1G5wWQH0AZ7TRPtJ0vDrcj5QV79h2ic2pw/640?wx_fmt=gif&from=appmsg)

访问智能安全分析工作台【登录页面】

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/EZicQGyMXoOmm2MaTDVOJ2HdbeJz3BV2iaqpglpy1RTVJhzE8uEAHysxBYLlV4oYtCNVGD3j5cicHru1cUxB6XNS6vU2jia9REMVWMgU0jicUHTk/640?wx_fmt=gif&from=appmsg)

二、手机 App 逆向&抓包

**设备连接**：****支持 USB、无线调试、常见模拟器MuMu、夜神、雷电等模拟器一键自动连接，镜像模式、非 Root 重打包、**密钥线索扫描、**静态脱壳、**注入脚本、一键安装APP、**产物管理** 、**APK 分析报告、**历史报告。**********

一键脱壳**：**自动完成部署、JS脚本注入、采集、产物分析、生成报告，不连接手机也能脱壳，直接提取 APK 里的 DEX 和 so等文件。

![](https://mmbiz.qpic.cn/mmbiz_png/EZicQGyMXoOlPsnR0OT9TtVsawazZ6sfG3ibyfLPYxbSb72PWS65ic1pibWQJOlicC8E3rEwnNvZhmBcw3FwNic7R7u7cRiabDjoX1obicW5VIHpVx4/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/EZicQGyMXoOm39n75sk9dQrZHb9fibgibb5o1Ya9lflIA0IswZahnVFz2aoJkicKSYplOtkZjdnn0GmSC1MpgsgaoeZb265fEtx081YnIGoDZicw/640?wx_fmt=png&from=appmsg)

**投屏控制：**镜像模式把手机画面投到电脑，用鼠标直接操作。

![](https://mmbiz.qpic.cn/mmbiz_png/EZicQGyMXoOncK2xW4vY3PicK5tQbsibdMrMGT98T5lHbvrMbgYNFaEQnibl9YVnMevibicQaSPQRBFJ6ER8gXfVILQicnicotmdlQcPH3pnGOOiauwI/640?wx_fmt=png&from=appmsg)

## 三、流量与抓包

**代理抓包：** 一键启动本地代理，手机流量实时可见。 怎么用：手机设好代理后，请求和响应在电脑上实时刷新。**敏感信息识别、**会话流量、**抓包文件分析、证书******

* **代理抓包**

  ：本地 HTTP/HTTPS 代理（CA 生成/下载 `.crt`、导出 `.p12`、一键安装信任）、实时流量与历史抓包、搜索过滤、**自定义敏感信息规则（正则）**、Host 白/黑名单、**AI 分析抓包流量**
* 注入/越权/上传/敏感信息泄露等风险通过内置技能与模型协同验证（低影响、留存证据）

![](https://mmbiz.qpic.cn/sz_mmbiz_png/EZicQGyMXoOmzVcn0M0HbGPAeyp35oOg79ZFc9vkrNxJe96EetwHRQ4hyicW7qqMmWF6MXLVmxhXfdnePiccyKarYYM5V68gLH7tWSwubtW1mI/640?wx_fmt=png&from=appmsg)

微信小程序抓包

![](https://mmbiz.qpic.cn/mmbiz_gif/EZicQGyMXoOkNFkuGBXwy8ZHHJRhkPBYlCRQfYOUsmO2NyUKuYicKxsvGlPnzvNqsr2ibibibCx5hdVpamBY1pD4NHnkXtOBYXUdFibk5L5xkkiaOo/640?wx_fmt=gif&from=appmsg)

设置【下游代理】把流量转发到BurpSuite

![](https://mmbiz.qpic.cn/mmbiz_png/EZicQGyMXoOlSIlRicibn7GNKFz01BtXBBylZC0Xm1ADgGnmEGawThv1MTntzGx1QmuylgktkHArvVjs1afXeXlFJRYTQqJMQIqibqXXoxnyxEM/640?wx_fmt=png&from=appmsg)

Android APP 抓包

![](https://mmbiz.qpic.cn/mmbiz_png/EZicQGyMXoOnicFRayDaWdr9ZJVk94HgNdmYiaLe79kvM0NKtQ9nOH15B4hr7JyQlnbT8x75ABHRsdc9d6V5gMUqczP0XjmOst9hz7CxjwDPBM/640?wx_fmt=png&from=appmsg)

抓电\*报（T\*G）小程序数据包

![](https://mmbiz.qpic.cn/mmbiz_png/EZicQGyMXoOkgTJbfIqJq5iaWia19j2XHc5x2Rx9mRkJAxO6JrCpmiabokmEqVYhicbMmO4IeK5glYKfx8FvDfGUmpOvZPRqzibTWwk0jux5rr5LY/640?wx_fmt=png&from=appmsg)

四、漏洞与交付

* **渗透测试任务中心：案例/漏洞/证据三库联动，严重性、置信度（confirmed/pending/误报）、CVSS/CWE、flag 提取、任务状态（进行中/已完成/暂停）**
* **派发任务：指定目标与范围，一键派发 AI 执行**
* **报告导出：Markdown / DOCX 安全报告（执行摘要、攻击链、漏洞详情、修复建议、加固方案）**
* 对话报告也可导出 PDF/Markdown/DOCX（reportlab / python-docx）
* **POC&EXP 管理：知识库管理，沉淀已验证的验证过程**
* 对话内生成 **PPT / Word**、**图片**、单文件 **HTML 报告**（示例提示词已内置）

![](https://mmbiz.qpic.cn/mmbiz_png/EZicQGyMXoOl83qeb9fhgZ3AuvXHroPaJJicFUHRbbgmaYOCPtkwKKKMbMqY6r48nYvNkLrXMia9y5vAiaNGJ4rGVIexQ7mz55o9T7OsdalRoIw/640?wx_fmt=png&from=appmsg)

## 五、资产与风险

* **子域收集：被动数据源（crt.sh / OTX / HackerTarget / RapidDNS / Wayback / Common Crawl）+ 常规检查（AXFR、证书 SAN、robots/sitemap/crossdomain、CSP、NSEC）+ 字典爆破（内置字典 / 自定义 / 文件导入 / 多文件拖拽，检测到 massdns自动启用加速）+ 爬取/置换 + 子域验证（DNS+HTTP、泛解析过滤）+ 递归爆破**
* **网络资产测绘源：FOFA / Shodan / ZoomEye / Quake / Hunter（各自 API Key）**
* **Host 碰撞：随收集实时碰撞 + 独立「碰撞所填内容」入口；自动分批（每批 ≤8000 组）、可停止、并发可调（1–500）；命中结果并入结果列表并红色告警**
* **CDN/源站判定：Cloudflare/CDN 标记徽章 + 仅存活/CDN/源站/Host 碰撞筛选**
* 结果管理：历史主域名数据、删除主域历史、**导出 6 种格式**（TXT / 仅域名 / CSV / Excel / JSON / Markdown）、**下发 Ai 任务**（一键送 AI 分析并创建渗透测试任务）
* **指纹识别：CMS、框架、中间件、语言、WAF/CDN、蜜罐等特征识别（内置规则库 + 结果检索/分页）**

![](https://mmbiz.qpic.cn/sz_mmbiz_png/EZicQGyMXoOlplCYeg45lW9UeLeDUAANZskEia7cGDxbFpficU3Fsib2Q4DxB7HkP6Jhh5lm407iao722jib97ocOapc3VZmaHzic6T6gcfWR9ibrwU/640?wx_fmt=png&from=appmsg)

**记忆管理** ： Ai 会自动记住对话里值得记录的信息。 怎么用：告诉过它的资产、习惯和偏好，下次不用重复交代，把常用方法和流程沉淀成「技能」，Ai 干活时自动调用。 怎么用：把公司的检查清单写成技能，Ai 每次按你的规范执行。

## ![](https://mmbiz.qpic.cn/sz_mmbiz_png/EZicQGyMXoOkk6icpbnF8lLgA9R75ibeg1ibsqyr1EMIHqVibym6BO9Gu0WJ3UyqEhiaWXmvocOkQf1o36ZPm2Vv7lUTW5I3S3Sv1SiaFL8H4CWbVk/640?wx_fmt=png&from=appmsg)

## MCP 管理：MCP 是一种「外部能力服务」，接上它，Ai 就能使用更多本机以外的能力。 怎么用：比如接上搜索服务、数据库服务、公司内部平台，Ai 都能直接调用。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/EZicQGyMXoOnIfo9q73Wqzb5g1y3Qkl0vLAVaPaJKVzIiac97iaicCJNfDomFQrq8UZwpcIffkr2jEXP9hsujV6I2hUc6mWUHhnMA4qZwbk7GKc/640?wx_fmt=png&from=appmsg)

## Skills 技能中心：技能就是一份「怎么做」的方法、流程或规范文档。 怎么用：把公司的检查清单、处置流程写成技能，AI 每次按你的规范执行。

![](https://mmbiz.qpic.cn/mmbiz_png/EZicQGyMXoOlGjeuCcLEU8eNqolmjOZR7L8IUPrQPVJEJqZ6yPATfLmn2FiahkOiciaLYYDhypYXx6NbHGf2ATC83ZneKKslP58o019bkHgrf2M/640?wx_fmt=png&from=appmsg)

## 工具 Tools 中心：把可执行程序或 ZIP 工具包直接导入，Ai 就能调用它。 怎么用：点「文件 / ZIP」选中工具包，导入后在对话里勾选即可使用。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/EZicQGyMXoOlyicwUlzsllGIL5M20gxGPxBPS6nf33U28J9Jvccf95wGAoYAAfCF4GSaxJBTcUqXdgXJv0MNHjeCnAPoeH1XabzVllR9TT0Ac/640?wx_fmt=png&from=appmsg)

POC&EXP 管理

![](https://mmbiz.qpic.cn/sz_mmbiz_png/EZicQGyMXoOlAtKiaYQnXsGy2ItMIfwuick8NiaSpmG2ZNjZTocI7IdUlqBHN9xRwY2ibMeKibC2vS8BBVx8zMc1MuicryXJyExm867icjync5kZiaicE/640?wx_fmt=png&from=appmsg)

六、远程与移动端

* **SSH 远程：面板连接主机后，模型可用ssh\_run 执行非交互命令（含只读/低影响约束）**

* **Android 控制：adb 设备发现与授权、USB/无线调试scrcpy 镜像、受限工具（读界面 XML、截图、点击/滑动、输入、启动普通应用；支付/银行/认证类应用禁止）**
* **iOS 控制：通过本机 WDA 服务，同样为受限操作工具集**
* **终端管理（Agent）：生成/连接 Agent、授权续期、TCP 监听端口管理、遥测（CPU/内存/磁盘）、只读诊断任务（系统信息/进程/网络/日志）、AI 生成只读排查命令（需确认后下发）、AI 诊断结论、运行日志检索**
* **Webshell 管理：生成多语言"无害代码执行验证文件"用于授权验证**

七、自动化与通知

* **定时任务：按计划让模型对指定授权资产做巡检/检查，结果可推送到通知渠道**
* **通知渠道：微信 ClawBot、Telegram、钉钉 Stream（可与会话绑定，支持独立频道会话直接对话）**
* **GitHub 监控：关键词监控，发现新内容推送通知**
* **一键复制全部 URL、结果分页、空对话示例提示词（18 条，覆盖渗透测试、CTF、流量/日志应急、SSH 运维、报告与 PPT 生成等）**

![](https://mmbiz.qpic.cn/sz_mmbiz_png/EZicQGyMXoOmmbjUvxaU0iaaTs8kPZZSx197FXhQibHpondWD9A8jTMjdl8ibSdM9VQMzCo9y...