---
title: Nuclei 漏洞扫描图形化工具 | POC 管理、FOFA/Hunter/Shodan 资产测绘、AI 辅助分析、漏洞报告生成
url: https://mp.weixin.qq.com/s/hRQs9wtmkgSWhGPSubHwkw
source: Doonsec's feed
date: 2026-06-26
fetch_date: 2026-06-27T05:48:33.487899
---

# Nuclei 漏洞扫描图形化工具 | POC 管理、FOFA/Hunter/Shodan 资产测绘、AI 辅助分析、漏洞报告生成

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/2I159AwKj57JTPEmvaJ3JJgnlKMsckArajsYibJicUiaJ4ibPGCB4GDnzyBID48wM1ASAHhnRBZknTDbZRvakLaibsZibXgyrRLbIPpsEycaNSTiaU/0?wx_fmt=jpeg)

# Nuclei 漏洞扫描图形化工具 | POC 管理、FOFA/Hunter/Shodan 资产测绘、AI 辅助分析、漏洞报告生成

点击关注👉
点击关注👉

马哥网络安全

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

![](https://mmbiz.qpic.cn/mmbiz_png/2I159AwKj54Cxc1qqWxICcv9ibpuMHgDibbSDtBGdnliaje38YicNKZBlfBEPsLSWyF3fttdAtqicp2TwQpaV0Q0vXG0aLXJnHIsVuYFuoiaVib2tM/640?wx_fmt=png&from=appmsg)

## 工具介绍

**Nuclei GUI Scanner**基于 PyQt5 开发的 Nuclei 漏洞扫描图形化工具，提供友好的可视化界面，支持 POC 管理、资产搜索、AI 辅助分析等功能。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/WibL3bOeESMKByBFniciafIDgM82PEKYAeYBl96a6kfEUicdiaobEeAiboRrjx5cmlE5GkYsoOKgsMNaHsYick9RVhDo4CzeNvrp80UH2YBXaP9nm4/640?wx_fmt=png&from=appmsg&wxfrom=13&tp=wxpic&watermark=1#imgIndex=1)

## 功能截图

![](https://mmbiz.qpic.cn/sz_mmbiz_png/WibL3bOeESMLpETzTru5U2YKaadrZaiaEQhoOoSk93ljxCX9NqXgicRCQxnPGicO2NhiabnIjM6oFVpdV3dKZErtKcjVrSaKXU0tdoCuFAs4zAjM/640?wx_fmt=png&from=appmsg&watermark=1&tp=wxpic&wxfrom=5&wx_lazy=1#imgIndex=2)![](https://mmbiz.qpic.cn/sz_mmbiz_png/WibL3bOeESMJdWbFSzDRe9RiaxrSoUPHruferuZqMALOlb3FqY6p74n0afHADzP0K7eFiazDhlhglFr5fKK6wHmCX7ictibOibAOEQeHPyKjRdpEA/640?wx_fmt=png&from=appmsg&watermark=1&tp=wxpic&wxfrom=5&wx_lazy=1#imgIndex=3)![](https://mmbiz.qpic.cn/mmbiz_png/WibL3bOeESMJ1nIoZv8UFdOT8EJicRX0Gkwiabwp8nAxL0SnYR8EKUiclJhUo4ltiaWz1KooWFBgh4LAaO4VJpiaxsKHEyq7ZqkRZIcicLct79jUAg/640?wx_fmt=png&from=appmsg&watermark=1&tp=wxpic&wxfrom=5&wx_lazy=1#imgIndex=4)![](https://mmbiz.qpic.cn/mmbiz_png/WibL3bOeESMJqCic16xRpmK6nc9Ea9Mz1ZXdXZ393iafDGvUiccVc0dlEthsaWhPtGwrm0LBEtABBVn4TNcQV1j1d57WAanfFXicPR8TyvB6D3HI/640?wx_fmt=png&from=appmsg&watermark=1&tp=wxpic&wxfrom=5&wx_lazy=1#imgIndex=5)

## 功能介绍

### 1. 仪表盘

* 扫描统计概览 (总扫描次数、发现漏洞数、POC 数量)
* 漏洞趋势图表
* 最近扫描历史
* 漏洞严重程度分布

### 2. 漏洞扫描

* 支持单目标/批量目标扫描
* 可选择多个 POC 模板
* 实时显示扫描进度和结果
* 支持暂停/恢复/取消扫描
* 扫描结果可导出为 CSV/HTML

### 3. 任务队列管理

* 多任务排队执行
* 任务优先级设置 (紧急/高/普通/低/后台)
* 断点续扫支持
* 任务状态实时监控
* 显示创建时间、开始时间、耗时

### 4. POC 管理

* POC 列表浏览和搜索
* 按严重程度/标签筛选
* POC 导入 (文件/目录)
* POC 在线同步 (从 nuclei-templates 官方仓库)
* POC 编辑器 (语法高亮)
* POC 快速测试
* POC 收藏管理

### 5. 资产搜索

支持多个资产搜索引擎：

| 引擎 | 说明 |
| --- | --- |
| FOFA | 国内主流资产搜索引擎 |
| Hunter | 奇安信鹰图平台 |
| Quake | 360 网络空间测绘 |
| Shodan | 国际知名搜索引擎 |

* 搜索结果可直接导入为扫描目标
* 搜索历史记录

### 6. AI 助手

支持 OpenAI 兼容接口 (DeepSeek、通义千问、GPT 等)：

| 功能 | 说明 |
| --- | --- |
| FOFA 语法生成 | 根据漏洞描述生成 FOFA 搜索语法 |
| POC 生成 | 根据漏洞描述生成 Nuclei YAML POC |
| 漏洞分析 | 深入分析漏洞原理和修复建议 |
| 智能推荐 | 根据目标特征推荐适用的 POC |
| 漏洞报告生成 | 生成 SRC 提交格式的漏洞报告 |

### 7. 漏洞报告生成

扫描结果支持一键生成 AI 漏洞报告：

* 补天/SRC 提交报告格式
* 详细技术分析报告
* 简要漏洞说明
* 修复建议报告

### 8. 设置

* **扫描参数**: 超时、并发数、重试次数、代理设置
* **FOFA 配置**: API URL、Email、API Key
* **AI 配置**: 多预设支持、模型选择、API 测试
* **主题设置**: 经典蓝、深邃蓝、清新绿、优雅紫

## 快捷键

| 快捷键 | 功能 |
| --- | --- |
| Ctrl+N | 新建扫描 |
| Ctrl+S | 保存设置 |
| Ctrl+E | 导出结果 |
| Ctrl+F | 聚焦搜索框 |
| Ctrl+L | 显示日志 |
| F5 | 刷新 POC 列表 |
| Escape | 停止扫描 |
| Ctrl+1~6 | 快速切换页面 |

## 配置说明

### Nuclei配置

```
将官方Nuclei放入bin目录下
在程序设置中将扫描参数设置选择"跳过探测"和"详细日志"进行打勾
```

### AI 配置

支持任何 OpenAI 兼容接口：

```
API URL: https://api.deepseek.com (或其他兼容接口)
API Key: 你的 API Key
模型: deepseek-chat / gpt-4o / qwen-turbo 等
```

### FOFA 配置

```
API URL: https://fofa.info
Email: 你的 FOFA 邮箱
API Key: 你的 FOFA API Key
```

### 代理设置

支持 HTTP/SOCKS5 代理：

```
http://127.0.0.1:7890
socks5://127.0.0.1:1080
```

## 工具获取

https://github.com/ChenChen753/Nuclei\_Gui

文章来源：夜组安全

![](https://mmbiz.qpic.cn/mmbiz_png/INa3lxHH4I2aV3zCmfiaj4cXeQ2HQd6s53wJS36HYI65ib48fujDK8najfWiahicsljzsdT3dfVS8HHyxaviaSd8g2g/640?wxfrom=5&wx_lazy=1&wx_fmt=png&wx_co=1)

**今日福利**

为了帮助大家早日习得网络安全核心知识，快速入行网络安全圈，给大家整理了一套***【2026最新网安资料】***网络安全工程师必备技能资料包（文末一键领取），内容有多详实丰富看下图！

Web安全👇

![](https://mmbiz.qpic.cn/mmbiz_png/UkV8WB2qYAkcvc41LgmeFn1B18QpgBZFBODrmsTGnPTOibdIT9B5eFLTHVIgWzYafxGAesmYnfzrz52xwV3Bjhw/640?wx_fmt=other&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

渗透测试👇

![](https://mmbiz.qpic.cn/mmbiz_png/UkV8WB2qYAkcvc41LgmeFn1B18QpgBZFVKWl2cLRTq7x9haKJerUZNO0YMhiaO8ibN1jjV0qxNLEvRKMfR90eNjQ/640?wx_fmt=other&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

安全面试题👇

![](https://mmbiz.qpic.cn/mmbiz_png/UkV8WB2qYAkcvc41LgmeFn1B18QpgBZFgrmaDLaYT1yV5lst9tKC72QrYjd5I8IN7kcOZIZSfQJJz8MdX6a1uA/640?wx_fmt=other&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

代码审计👇

![](https://mmbiz.qpic.cn/mmbiz_png/UkV8WB2qYAkcvc41LgmeFn1B18QpgBZFxmUkTNP1iagssZL5zkjID8hibpZsRCj1OnEb4x7ZYWqpiaymSjc8O7vSQ/640?wx_fmt=other&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

红队笔记👇

![](https://mmbiz.qpic.cn/mmbiz_png/UkV8WB2qYAkcvc41LgmeFn1B18QpgBZFVZS1mB4MKAo4FoMBGyVSzq38ZXEKJCjZVaTsFtLE7tIJ3zbRWF5xeA/640?wx_fmt=other&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

入门视频👇

![](https://mmbiz.qpic.cn/sz_mmbiz_png/O9D0kmTL9EgxtiaXGtk7loXV41e8AXiaORJMhqFbrtcfHvJWTia6ME2oSI9msVYJu79uCicb7foufuibEHaVg32XnWw/640?wx_fmt=other&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

![](https://mmbiz.qpic.cn/mmbiz_gif/NUwbCdTuQQxsJibSZGyA8akP9TVyJfPcpJ4uIZJDj3akRUfv6cNbnksGJQsibq1aH8iaGDic7TvOaSwNGXLdQ8PC9A/640?wx_fmt=gif&wxfrom=5&wx_lazy=1&tp=webp)

以上所有资料获取请扫码

![](https://mmbiz.qpic.cn/mmbiz_png/2I159AwKj57dqicaIYBvqCk0ZmUMCRAPvdvFhqTClxu4OCe19NETpdebica4ficVvXHBNjgPiapribMoO7hyFoibJlQ2H8PX531QicicsY5wZb6YpLg/640?wx_fmt=png&from=appmsg)

识别上方二维码

备注：***2026安全合集***

100%免费领取

（是扫码领取，不是在公众号后台回复，别看错了哦）

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