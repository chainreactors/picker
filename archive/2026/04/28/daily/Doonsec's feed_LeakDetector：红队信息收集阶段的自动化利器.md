---
title: LeakDetector：红队信息收集阶段的自动化利器
url: https://mp.weixin.qq.com/s/qvriWz37hqIzwYKQMpL9FA
source: Doonsec's feed
date: 2026-04-28
fetch_date: 2026-04-29T05:06:25.276019
---

# LeakDetector：红队信息收集阶段的自动化利器

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/4T1PVwJicwkicksprYep1TtCKCfrDiah43ySa9CNU49UxTrC4JU3zHaN7sI4eHp2GrFT6MwibyfRia8icpIwT988s7pr1XeZqFGjDXLXckbGyusZE/0?wx_fmt=jpeg)

# LeakDetector：红队信息收集阶段的自动化利器

原创

cbbzx12
cbbzx12

泷羽Sec-Norsea

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

# LeakDetector (Bing Dork Automation Tool)

**LeakDetector** 是一款专为红队渗透测试人员打造的信息泄露猎手，它将 `Bing` 搜索引擎的高级 `Dork` 语法与 `Playwright` 浏览器自动化技术深度融合，能快速在互联网上搜寻那些因配置错误、运维疏忽或系统漏洞而意外暴露的敏感信息。

和传统简单脚本不同，它内置了智能抗反爬机制和深度内容分析引擎，可以从海量搜索结果中自动筛选出真正高价值的目标，

比如客户通讯录 Excel、身份证批量数据、API 密钥、数据库配置等，最后还能一键生成带截图和风险等级的可视化审计报告，让原本需要人工刷几个小时甚至几天的脏活累活，几分钟就能跑完。

```
免责声明 / Legal Disclaimer本工具仅供授权的安全测试、漏洞挖掘和企业内部安全审计使用。严禁用于非法入侵、数据窃取或任何未经授权的恶意攻击活动。使用者应自行承担因使用本工具而产生的一切法律责任。
```

## 核心特性 (Key Features)

### 1. 多维度 Dork 侦察策略

* `LeakDetector` 内置了经过大量实战打磨的六层递进式侦察策略（P1-P6），从基础设施到敏感数据实现全覆盖式扫描：

+ API 与配置泄露：精准识别 `Swagger UI、Spring Boot Actuator、.env、 application.yml` 等常见配置泄露点。
+ 敏感文件挖掘：重点锁定 xlsx、docx、pdf 等办公文档，智能识别包含身份证、手机号、工资表、客户名单等敏感关键词的文件。
+ 后台与运维平台：快速发现 OA 系统（泛微、致远）、各类后台管理入口、Jenkins、GitLab 等内部平台。
+ 高危漏洞特征：自动探测 SQL 注入报错页面、文件上传接口、Webshell 残留等危险信号。

### 2.智能浏览器引擎 ( Browser Engine)

* 集成业界领先的 `Playwright` 浏览器内核，彻底告别传统爬虫的各种顽疾：

+ 智能反检测与验证码绕过：支持自动识别 Bing 的 Turnstile 和 ReCAPTCHA，可在图形界面中暂停并引导手动验证，有效解决 IP 被封导致无结果的难题。
+ 动态页面渲染：完美处理依赖 JavaScript 加载的内容，抓取到的搜索结果远比纯 HTTP 请求更完整、更真实。

### 3.深度内容分析与提取 (Deep Analysis)

* LeakDetector 不仅会收集链接，更会对目标文件进行深度解析和价值提炼：

+ 文档智能解析：自动下载并读取 Excel、CSV、PDF 等文件，支持多 Sheet 识别。
+ 敏感信息精准提取：内置中国大陆身份证、手机号、邮箱等多种高精度正则，能从海量文本中快速捞出 PII（个人隐私信息）。
+ 智能风险评分：根据泄露数据的类型和数量自动打分，并在最终报告中用颜色直观标记高危条目。

### 4.高性能并发架构

* 采用 ThreadPoolExecutor 线程池，支持 10-50 线程并发运行。
* Pipeline 流水线设计：搜索、下载、分析三阶段并行处理，实现“边搜索边分析”，大幅提升整体扫描效率。

## 快速开始 Guide (EXE 版本)

本工具已打包为独立的 `LeakDetector.exe`，无需安装 Python 或依赖库。

### 1. 启动

直接双击 `LeakDetector.exe` 即可启动图形化界面。

### 2. 基础配置

1. **输入目标**: 在主界面的文本框中输入**根域名**，支持批量导入。

   > ❝
   >
   > *示例*: `example.com``university.edu.cn`
2. **选择模式**:

* **Standard (EDU/Gov)**: 适合教育、政府目标，侧重文档泄露和 PII 提取。
* **企业**: 适合企业目标，侧重后台、OA、DevOps 暴露。
* **All**: 执行所有 P1-P6 策略（耗时较长）。

3. **开始运行**: 点击 `▶ 开始扫描` 按钮。

### 3. 进阶功能：浏览器模式 (强烈推荐)

默认情况下工具使用 HTTP 请求模式（速度快但易被封）。建议开启 **"显示浏览器 (手动绕过验证)"**:

1. 勾选界面上的 `显示浏览器` 复选框。
2. 工具会自动启动一个 Chrome / Edge 窗口。
3. **不要关闭该窗口**。当遇到 Bing 验证码时，工具会暂停并弹窗提示。
4. 您只需在浏览器中手动完成滑块验证，然后点击工具弹窗的 `确定`，扫描将自动继续。

## 配置文件说明 (`config.json`)

工具首次运行后会在同级目录生成 `config.json`，可修改高级选项：

```
{
    "proxy_enabled": true,            // 是否默认启用代理
    "proxy_url": "127.0.0.1:7890",    // 代理地址 (HTTP/Socks5)
    "use_browser": false,             // 默认是否开启浏览器模式
    "max_threads": 10,                // 扫描并发线程数 (建议 5-20)
    "time_range": "不限时间",          // 默认时间过滤 (过去24h/1周/1月等)
    "auto_organize": false            // 扫描结束后是否自动整理结果文件夹
}
```

## 运行截图 (Screenshots)

### 1. 主界面与配置

![](https://mmbiz.qpic.cn/mmbiz_png/4T1PVwJicwk8k5ROPEh0wibzVNFwVOicngic90zfpjrgCOZqzEOLgRIfPfxJCTGd1WbZB20Gh5Jm1b63icKic3whH2Ys1AwqY25icica5zcpI1iaFdk8/640?wx_fmt=png&from=appmsg)

*简洁直观的操作界面，支持批量目标导入与策略选择*

### 2. 自动化扫描

![](https://mmbiz.qpic.cn/sz_mmbiz_png/4T1PVwJicwk9llZibPSbFJut8OFE5P7R44L5t4ZqgMlE6tdM59rpdO78DjWfic8cVhbDNpz5yCBG187wuic0viaUp3jMUdDCPc76cv5MJJWRKO90/640?wx_fmt=png&from=appmsg)

*实时显示扫描进度与发现的高危目标*

### 3. 结果分析

![](https://mmbiz.qpic.cn/mmbiz_png/4T1PVwJicwkic1v9mwZxibVDC0mt9GBTlZ7CHIiciasESHOOMqtP7l9qTQItkQGAAMTm9HgwRJtjx4IaCYvLYu7b9bRibYpibgKnMnZ4ibCHLS6JeHc/640?wx_fmt=png&from=appmsg)

*自动提取 Excel/PDF 中的敏感信息，并进行风险分级*

### 4. 浏览器模式 (Bypass CAPTCHA)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/4T1PVwJicwkibhPqYfpFS3TJmiahZ4obVS0R4n98ZIicBBxF0sd5QBLiclHHGxF55vCCxfjduR1jsjGoe7pqzhibeibg1pYBOwA83Wckjs1HbhbxkU/640?wx_fmt=png&from=appmsg)

*直观的浏览器视图，辅助通过复杂的人机验证*

## 输出报告解读

扫描结果保存在 `results/Scan_YYYYMMDD_HHMMSS/` 目录下：

+ **汇总详情页**: 包含所有发现的高危条目，按风险评分排序。
+ **扫描概览页**: 各类风险的数量统计、高危域名 Top20 分布。
+ **风险评分**: 红色背景为极高危（身份证/密码），黄色为中危（邮箱/手机）。
+ `信息泄露扫描报告_xxx.xlsx`
+ 核心产出物。

* **下载的文件**: 扫描过程中自动下载的 `.xlsx`， `.pdf` 等原始文件会保存在对应文件夹中，供人工取证。

```
工具地址：https://github.com/cbbzx12/LeakDetector
```

## 学习交流群

刚加入网络安全行业的小白，可以加入学习交流群，大家一起互相学习，互相进步，不会的难题大家一起学习，一起攻克。

想要进学习交流群的师傅们，可以扫描下方二维码添加好友，我再拉你进群（Ps：防止广告进群）。

![](https://mmbiz.qpic.cn/mmbiz_jpg/IkpoxULsr9dEclFnKnAAurt1AlnO1HBLiaRymULG1ibJJhXlNjMH1rd1SgQQWIyFBVTRMteWWfiby3FCWfpB7n2oA/640?wx_fmt=jpeg&from=appmsg)

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/IkpoxULsr9fbWSl52zKqe5AN711UM8IFNbS9rZLM7reGeUZs0XqdtM8X5L5mdRibicHpxmu3iaPGct9UztVKAT6AA/0?wx_fmt=png)

泷羽Sec-Norsea

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/IkpoxULsr9fbWSl52zKqe5AN711UM8IFNbS9rZLM7reGeUZs0XqdtM8X5L5mdRibicHpxmu3iaPGct9UztVKAT6AA/0?wx_fmt=png)

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