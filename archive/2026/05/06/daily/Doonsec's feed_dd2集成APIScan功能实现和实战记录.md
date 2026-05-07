---
title: dd2集成APIScan功能实现和实战记录
url: https://mp.weixin.qq.com/s/3dyxG4YlqPqfN8clsNEk8g
source: Doonsec's feed
date: 2026-05-06
fetch_date: 2026-05-07T05:31:08.280467
---

# dd2集成APIScan功能实现和实战记录

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/6mEJuibtxKvOib4MRFeibJ9gSJKzWr71StQnHxyHjM5qfQzVJFPgmYmEyU5SyTHSOvhdyh42otgSf6z9axyfwIl9sQRyfPjNF3xyPlrVIaq6tg/0?wx_fmt=jpeg)

# dd2集成APIScan功能实现和实战记录

原创

安全艺术
安全艺术

安全艺术

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

# APIScan 功能实现

## 一、核心能力

## 1. 自动收集扫描目标

APIScan 会从全局 URL 资产中提取待扫描目标，并自动去重，避免对同类路径反复扫描。
对云厂商公共域名、策略明确要求跳过的目标也会自动过滤，减少无效流量。

## 2. 页面与 JS 递归采集

APIScan 会围绕目标站点做受控递归采集，包括：

* 页面链接
* HTML 中引用的 JS
* 动态 import 的 JS
* Vite / Webpack 等前端构建产物中的 chunk 依赖
* 脚本中显式或隐式拼接出来的资源路径

这意味着它不仅能发现首屏页面能看到的接口，还能继续向构建后的前端资源深挖，把隐藏在 chunk、依赖映射和延迟加载模块中的接口线索一并挖出来。

## 3. 多策略接口候选提取

APIScan 对接口候选的提取不是单规则，而是组合多种模式：

* `fetch`、`axios`、`$.ajax` 等调用特征
* `url`、`api`、`endpoint`、`baseURL` 等对象字段
* 相对路径、绝对路径、拼接路径
* 关键字路径，如 `api`、`graphql`、`gateway`、`openapi`、`auth`、`admin`、`service`
* 基础 API 前缀 + suffix 组合推导

这使它对现代前端项目更友好，尤其适合：

* Vue / React / Vite 项目
* Webpack 分包项目
* 管理后台
* 中后台 API 网关型应用

## 4. 根路径推导与接口扩展

这是 APIScan 很有价值的一点。

它不仅抽取接口，还会分析目标站点的 **根路径 / 部署前缀**，例如：

* `/app`
* `/admin`
* `/gateway`
* `/foo/v2`

在拿到这些根路径后，APIScan 会对接口候选做二次扩展，例如把页面里看到的相对接口路径自动映射到不同部署前缀下，补出更多更接近真实可访问面的 URL。

对于多层目录部署、反向代理子路径部署、前后端统一前缀部署的系统，这个能力能显著提高命中率。

## 5. 同站点 / 子域名范围内联动发现

APIScan 在处理 JS 时，会识别同站点或子域名下的新目标，并将它们继续纳入发现链路。
这意味着它不仅扫“当前 URL”，而是在合理边界内把关联 Web 面串起来，形成更完整的接口视图。

适合发现：

* 主站引用的子系统
* 子域 API 网关
* 前端静态资源落在不同二级域名的场景

## 6. 接口响应分析

APIScan 会对候选接口逐个发起请求，并对返回内容进行判断：

* HTTP 状态码
* Content-Type
* 响应长度
* 是否为可分析文本 / JSON / XML / HTML / JS

对于命中的结果，会进一步保存请求包、响应包和命中规则，便于后续人工复核。

## 7. 敏感信息泄露识别

除了“找接口”，APIScan 还会直接识别前端和接口响应中的高价值泄露内容，包括：

* AK / SK 类凭据
* JWT
* 大模型 API Key（如 `sk-`、`sk-proj-`、`sk-ant-` 形式）
* 密码类字段
* 身份证号
* 手机号
* Email
* URL
* Webhook 地址

其中对大模型 Key、密码、邮箱、URL 等做了专门的误报过滤，不是简单正则命中就报，尽量压低“看起来像、其实不是”的噪声。

---

## 二、典型输出成果

运行后通常会在 `results/` 目录下生成：

* `apiscan-时间戳.html`
  用于汇总展示所有命中结果，支持按规则筛选查看。
* `apiscan-url-时间戳.txt`
  保存扫描过程中发现的 URL / 线索，便于二次利用。
* 单目标或命中详情 HTML
  保存具体请求包、响应包、命中规则和提取出的数据。

---

# APIScan 实战记录

进入apiscan，目录扫描，指纹识别和漏洞扫描前需要加一层判断过滤无效扫描，比如：

```
阿里云 Web应用防火墙
503 Service Temporarily Unavailable
502 Bad Gateway
```

加入-api参数，先提取js并匹配js中存在的敏感信息。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/6mEJuibtxKvOHVwnG6YLjRllYvHZ1ru8d2j2VYwnQLfxgx1zeu3chMrUu0ZEiaxGeLiaQDvLaptWEL73f6icQdowa2YgiaIYtkGTU0NIqCxAmEFo/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/6mEJuibtxKvPyaDsNwia2tGEu12VazYwMPW29YqsNlbI3SbHicJybsjNX3bib69yedIhqnGuuvNN0SoUv6vofRIbQD9r8ppOdttIhnPxPN7QcNU/640?wx_fmt=png&from=appmsg)

再提取js中接口，批量请求匹配响应中存在的手机号、密码等敏感信息。

![](https://mmbiz.qpic.cn/mmbiz_png/6mEJuibtxKvONKJsOCvQ2iaBibZcAAufY3vLD3sZ6TCmuIjMN4CJZOibnfibEF5h2Yf9XD1jeMemSg14oVA93icenzS8sPR61M1XLLkmQg8CMFc8Y/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/6mEJuibtxKvO34OVebdegcQtrLkAHB3AFFGlDaKbHPKnM78bruFb2rp51LCkquOOBkJ2Aum7JyZ089N6xSlUzw6lBMqc4kJ0ZfnJoOJ9OQnM/640?wx_fmt=png&from=appmsg)

提取的URL接口会加入扫描队列进入目录扫描和POC扫描。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/6mEJuibtxKvNKctwMt9e61PI6icicicDrq7dZEJtPicRln6cge6HNAgyQlribS5Via2A7y3WwnZJHXmU1BpeOEiaJPcQu815JiauEKD9s6dp7Eo06jy4/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/6mEJuibtxKvOGbjtUC4NLxq2hlzZYR6nZrbDiaYDrSdnDDGYbx03R4adPt83yKRs3g6P5qdruWVwuSQ4m1NkiaEbeko1stcBy6qgk3ib94wYibTA/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/6mEJuibtxKvPs5gAERTcC9w66k8BAmsWib2xaN8ncXOll9ia6wxj79XWJdmt50NQMEwYmI6tPop22ogiaO4uYcrDThX6oZqaesXBNgeBichjWeww/640?wx_fmt=png&from=appmsg)

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/sz_mmbiz_png/X5epWh2K2Oo4NY9fLLoomQgld6ia6hfpRbrvGyVibgUgzOauMBthcywVUOU2bSRtSyjunLPVQNqRAO2YKH85bPMg/0?wx_fmt=png)

安全艺术

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/X5epWh2K2Oo4NY9fLLoomQgld6ia6hfpRbrvGyVibgUgzOauMBthcywVUOU2bSRtSyjunLPVQNqRAO2YKH85bPMg/0?wx_fmt=png)

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