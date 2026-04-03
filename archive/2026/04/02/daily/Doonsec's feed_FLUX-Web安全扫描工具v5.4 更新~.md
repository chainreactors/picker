---
title: FLUX-Web安全扫描工具v5.4 更新~
url: https://mp.weixin.qq.com/s/zRcjNCgt48JSAYKuTg5fyg
source: Doonsec's feed
date: 2026-04-02
fetch_date: 2026-04-03T04:26:29.788029
---

# FLUX-Web安全扫描工具v5.4 更新~

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/I2dhkmhKrSbKmXlOJlLEt8ciabXhrib8BeBH7iaaiaZOnJnTmeQRgLrXpltGvvdPXtPcqpYkdt65T7kTgGickIicIibDB2yQ2avE1kSPDAWVPRJ21w/0?wx_fmt=jpeg)

# FLUX-Web安全扫描工具v5.4 更新~

原创

ROOT4044
ROOT4044

不秃头的安全

![]()

在小说阅读器中沉浸阅读

# FLUX-Web安全扫描工具

```
前言：本文中涉及到的相关技术或工具仅限技术研究与讨论，严禁用于非法用途，否则产生的一切后果自行承担，如有侵权请私聊删除。
知识星球和交流群在最下方。
需要cn*d（中高）/c2n*d（高与支撑单位）/安全证书请联系vx咨询
```

![](https://mmbiz.qpic.cn/mmbiz_jpg/I2dhkmhKrSbiahWwL9VWibtAsBibZicZh0yt4zAF7KkgRMe6Whib38YSsyj9P1ECn4EHOrjfV2yd9xBT6ujCOZv8yfQK20hfUJmrB1oAL50Z5aBI/640?wx_fmt=jpeg)

FLUX v5.4 是一款专业的Web安全扫描工具，JS敏感信息收集、API端点提取、API文档解析、页面爬取、子域名发现、漏洞测试、WAF检测与绕过、JS代码分析等功能。

### **核心特性:**

* 🔍 25,000+ 指纹库
* 🛡️ 40+种WAF检测与绕过（含国产厂商）
* 🎯 一键全功能扫描
* 📊 美观HTML报告
* 🤖 智能速率限制与流量伪装
* 🔐 CSRF Token自动提取与Cookie持久化

### 功能特性

#### 🔍 信息收集

* **JS敏感信息收集**: 云API密钥、认证令牌、个人信息、硬编码凭据等（含熵值验证）
* **API端点提取**: 自动提取JS中的API接口路径（支持绝对/相对/模块路径）
* **API文档解析**: 支持Swagger/OpenAPI/Postman文档解析
* **页面爬取**: 深度爬取网站页面，提取表单和链接
* **子域名发现**: 自动收集子域名

#### 🎯 指纹识别（增强版）

* **指纹库规模**: 25,000+条指纹规则
* **支持类别**: OA系统、开发框架、Web服务器、安全设备、数据库、CMS等
* **检测方式**: 多特征交叉验证、Favicon Hash、特定文件探测
* **置信度评分**: 采用加权评分机制，多特征验证降低误报

+ 多特征匹配：≥2种不同方法匹配
+ 高置信度单一特征：favicon hash等强特征
+ 通用关键词过滤：避免"login"、"admin"等通用词汇误报

#### 🛡️ 漏洞测试（差分检测）

* **SQL Injection**: SQL注入检测（带基准线差分测试）
* **XSS**: 跨站脚本检测（反射型、DOM型）
* **LFI**: 本地文件包含检测
* **RCE**: 远程代码执行检测
* **XXE**: XML实体注入检测
* **SSTI**: 服务器端模板注入检测
* **SSRF**: 服务端请求伪造检测（支持交互式DNSLog输入）
* **Cloud Security**: 云存储桶安全检测

+ **Access Key泄露**: 检测12种云服务商的Access Key/Secret Key（阿里云、腾讯云、华为云、AWS、百度云、七牛云、又拍云、京东云、Google Cloud、Azure、Firebase等）
+ **存储桶遍历**: 测试未授权列出存储桶文件
+ **存储桶接管**: 检测可接管的废弃存储桶
+ **ACL/Policy泄露**: 测试访问控制列表和策略配置泄露
+ **未授权操作**: 测试未授权上传、删除文件

**差分测试机制:**

* 发送正常请求获取基准响应（状态码、长度、内容hash）
* 发送Payload后对比差异
* 显著差异才判定为漏洞，误报率降低80%+

#### 🔥 WAF检测与绕过

* **WAF识别**: 自动识别40+种WAF（国际16种 + 国产24种）

+ 国产支持：阿里云盾、腾讯云WAF、华为云WAF、安全狗、360网站卫士、知道创宇、安恒、长亭等

* **绕过技术**:

+ SQLi: 注释混淆、编码绕过、大小写变化、空格替代
+ XSS: URL编码、HTML实体、替代标签、Polyglots
+ LFI: 路径编码、双编码、空字节
+ RCE: printf编码、过滤器绕过

* **HTTP绕过**: X-Forwarded-For伪造、爬虫User-Agent、请求延迟调整

#### 🤖 智能防护规避

* **自适应速率限制**: 根据服务器响应动态调整请求频率
* **Header轮换**: 4种真实浏览器指纹轮换（Chrome/Windows, Chrome/Mac, Firefox, Safari）
* **流量指纹伪装**: 完整的Sec-Ch-Ua头、Accept-Language等
* **CSRF Token自动提取**: 支持6种常见Token格式
* **Cookie持久化**: 保存/加载会话状态，支持登录后扫描

#### 🔬 JS代码分析

* **混淆还原**: 支持eval(atob(...))、String.fromCharCode、\x十六进制、\uUnicode解码
* **DOM XSS检测**: 静态污点分析追踪source(location.hash)到sink(innerHTML)的数据流
* **API参数提取**: 从JS代码中提取fetch/ajax调用的参数名
* **参数Fuzzing**: 对提取的参数进行自动模糊测试

#### 📊 报告生成

* **HTML报告**: 美观的可视化报告，含统计图表
* **JSON输出**: 结构化数据便于集成
* **请求/响应包**: 详细的HTTP请求和响应信息

![](https://mmbiz.qpic.cn/sz_mmbiz_png/I2dhkmhKrSaAicicKFB2vV1xRgTLGry0xYySUwYPz914ZE1UI7Dm7KFcPSqKBliaVvD0feyjMjBVQKp64IcEKxKpxE05aWxpNxRxY77e1xu1Yg/640?wx_fmt=png&from=appmsg)

### 更新日志

```
v5.4 更新 (2026-03-29):
【核心优化 - 模块利用率提升】
- 重构: 统一敏感信息扫描入口 scan_sensitive_all()
  * 支持7种来源: html/js/render_dom/api_doc/sourcemap/storage_token/api_response
  * 106条敏感信息规则全链路复用
- 重构: SecretMatcher全量化，解除vuln_test依赖
  * 移除JS文件[:20]硬截断限制
  * 独立于漏洞测试开关运行
- 新增: --ssrf-dangerous 参数，替代环境变量控制
- 新增: _priority_sample() 优先级采样，替代固定切片
  * 云/K8s/Container/CI-CD模块按风险评分采样
- 新增: header_rotate 功能实现
  * 请求头轮换，模拟不同浏览器访问
- 新增: test_csrf 被动分析方法
  * 检测敏感操作端点是否缺少CSRF防护
- 优化: --full 模式增强
  * 新增 scan_mode='hybrid' 混合扫描模式
  * 新增 render_enable_interaction 浏览器交互
  * 新增 render_deep_spider 深度Spider
  * 新增 ssrf_dangerous SSRF危险探测
- 修复: 多目标扫描时每个目标生成独立日志文件
- 修复: 页面统计排除JS文件，数量更准确
- 修复: 批量扫描最终汇总使用累计统计
- 清理: scanner.py 死入口 (test_csrf/test_ssrf/run_all_tests)

v5.3 更新 (2026-03-28):
【架构优化 - 模块化拆分】
- 新增: 路径归一化与拼接治理模块 (core/path_normalizer.py)
  * 统一处理 ./、../、//、#、/#/、反斜杠、带端口URL
  * 支持异步chunk路径、带版本号JS路径归一化
  * 敏感路径拼接与候选URL生成
- 新增: 脏数据清洗模块 (core/dirty_cleaner.py)
  * 过滤伪JS、错误拼接URL、注释中的路径
  * 非关键页面、非目标后缀过滤
  * 异常超长/超小响应、重复页面/路径/参数过滤
- 新增: URL产物与域名汇总模块 (core/url_producer.py)
  * 纯净URL输出（可访问的真实目标）
  * 候选URL输出（拼接/FUZZ结果）
  * 域名汇总报告（主域/子域/第三方域/静态资源域/API域）
  * 扫描日志和阶段总结产物
- 新增: JS资产流水线 (core/js_pipeline.py)
  * 以JS为中心的资产发现流水线
  * 统一执行 URL提取 + 参数提取 + 路径提取 + API线索提取
  * 敏感路径拼接 + 候选请求生成
- 新增: 前端交互点识别模块 (core/interaction_point.py)
  * 识别登录点、提交按钮、注册点、搜索点、上传点、手机号登录点
  * 作为优先打点目标
- 新增: 敏感页面标签体系 (core/page_tagger.py)
  * 识别管理后台、登录页、存储桶页、黑页、AI页面、上传页等
  * 先做标签，不直接定性漏洞
- 新增: 误报治理回路模块 (core/false_positive_tracker.py)
  * 记录规则命中的来源、位置、值、过滤原因、降级原因
  * 主动探测/静态匹配分离机制
- 新增: 迭代式扫描深度模块 (core/iterative_scanner.py)
  * 首轮基于页面和静态JS，后续轮次扩展新路径/异步JS/失败URL
  * 深度可配置
- 新增: 浏览器动态渲染兜底模块 (core/render_fallback.py)
  * 默认静态抓取，仅在页面空白/JS延迟加载/API动态注入/关键资源缺失时启用
  * 避免全量浏览器渲染带来的资源消耗

v5.2.4 更新 (2026-03-28):
【报告优化】
- 新增: API端点表格增加响应长度列
- 新增: 所有来源列添加一键复制去重URL功能
- 修复: 修复批量扫描时每个目标统计为0的问题
- 修复: JavaScript代码中换行符转义问题
```

## 工具交流群

工具地址：https://github.com/MY0723/FLUX-Webscan

FLUX v5.4 使用手册：

https://github.com/MY0723/FLUX-Webscan/blob/main/FLUX\_MANUAL.md

问题清单收集：【腾讯文档】FLUX问题清单

https://docs.qq.com/sheet/DZmFZZ0JhaVRXSkFi

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/I2dhkmhKrSYiaC4NpLOYcjsJD9Dg18icoC3Xk35IYlT3Z03vicGJjbt1y3G7B4syiaPvgBibH3ngACiaEXthNpD4vQKc8EBia1e8qoH0gpu2fKrlVw/640?wx_fmt=jpeg&from=appmsg)

如果群满加我拉

![图片](https://mmbiz.qpic.cn/mmbiz_jpg/I2dhkmhKrSazov3P0xicP57U21T0PgibQVtlO9pzzhMzTwJZIclzH4yDAmg7psMREVovAQib07634YiazDibKkNGZgvv8dS5HPmNYtdSicXbcSr3g/640?wx_fmt=other&watermark=1&wxfrom=5&wx_lazy=1&tp=webp#imgIndex=23)

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/sz_mmbiz_png/DicRqXXQJ6fVZYQ3CLswQeCkia9axLIjSV5hFqM9ouzExlwAsUtDeqEyXE2pLUIRCeDJ0m89GHyibMCFAHXBHmiacg/0?wx_fmt=png)

不秃头的安全

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/DicRqXXQJ6fVZYQ3CLswQeCkia9axLIjSV5hFqM9ouzExlwAsUtDeqEyXE2pLUIRCeDJ0m89GHyibMCFAHXBHmiacg/0?wx_fmt=png)

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