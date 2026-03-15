---
title: JsRouteScan：渗透测试中的路由发现利器
url: https://mp.weixin.qq.com/s/8cEbgFDYgmz9Waqd65LQog
source: Doonsec's feed
date: 2026-03-14
fetch_date: 2026-03-15T04:25:17.974195
---

# JsRouteScan：渗透测试中的路由发现利器

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/IjKZbibec2gAwn1SYTcRmdOSA2whwQLib2LHU7JuoQMraZtmZlKB578bsUkvbzRE2g3mMJeakD3etNGyWw0vyR3u3BXxdDmHaXqAmjLr12iajI/0?wx_fmt=jpeg)

# JsRouteScan：渗透测试中的路由发现利器

原创

Zacarx
Zacarx

Zacarx随笔

![]()

在小说阅读器中沉浸阅读

> 一款让你在 JS 文件中挖掘隐藏路由的 Burp Suite 插件

---

## 写在前面

在 Web 渗透测试中，信息收集是最关键的一环。而 JavaScript 文件往往是被忽视的宝藏——前端路由、API 接口、隐藏页面，这些信息都可能藏在 JS 代码里。今天要介绍的 **JsRouteScan**，就是一款专门从 JS 响应中提取路由并自动探测的 Burp Suite 插件。

**项目地址：**https://github.com/F6JO/JsRouteScan
**Star 数：** 366+
**开发语言：** Java
**适用场景：** Web 渗透测试、漏洞挖掘、资产收集

---

## 核心功能

### 1. 被动路由提取

JsRouteScan 通过 Burp Suite 的被动扫描机制，自动监听所有 HTTP 响应。当响应中包含 JavaScript 代码时，插件会使用预定义的正则表达式列表匹配疑似路由的字符串。

**默认正则规则：**

```
.{10}["'`]([a-zA-Z0-9/=_{}\.\?&!-]+/[a-zA-Z0-9/=_{}\.\?&!-]+(\.jspx|\.jsp|\.html|\.php|\.do|\.aspx|\.action|\.json)*)["'`].{160}
```

这个正则可以匹配类似这样的路由：

```
"/api/user/info"
'/admin/dashboard.php'
`/system/config.json`
```

### 2. 智能过滤机制

为了避免误报和无效请求，插件提供了两层过滤：

**排除路由正则（ExRouteRegexs）：**

* 过滤静态资源（.css, .js, .png 等）
* 过滤特定 Content-Type（image/\*, application/pdf 等）
* 过滤已知的无效路径模式

**排除后缀列表（ExSuffix）：**

```
[.jpg, .png, .css, .jpeg, .gif, .zip, .tar, .mp3, .wav,
 .flac, .mp4, .mov, .avi, .mkv, .bmp, .tiff, .pdf, .doc,
 .docx, .xls, .xlsx, .ppt, .pptx, ...]
```

这样可以大幅减少无效请求，提高扫描效率。

### 3. 被动探测模式

开启被动探测后，所有匹配到的路由都会自动发起请求。你可以配置：

* **Passive Scan Path：** 探测的根目录（默认 `/`）
* **Request Method：** GET 或 POST
* **CarryHead：** 是否携带原始请求头
* **Thread Pools Number：** 线程池大小

**工作流程：**

```
1. 监听响应 → 2. 正则匹配路由 → 3. 过滤无效路由 → 4. 自动发起探测请求
```

### 4. 主动扫描模式

在 ReqDisplay 面板中，你可以看到每个网站提取到的所有路由。然后可以：

**普通扫描（Scan）：**

* 对指定根目录下的所有路由发起请求
* 适合探测特定目录下的资源

**递归扫描（Recursion-Scan）：**

* 对每一层路径进行递归探测
* 例如路由 `/api/user/info`，会探测：

+ `/api/`
+ `/api/user/`
+ `/api/user/info`

**注意：** 递归扫描的请求数量 = 目录层级 × 路由数量，使用前务必清理无用路由！

### 5. 自定义请求头

可以为每个网站单独设置请求头，这在需要特定 Token 或 Cookie 的场景下非常有用。

---

## 实战场景

### 场景 1：前端路由泄露

某 SPA 应用的 `app.js` 中包含了所有前端路由配置：

```
const routes = [
  { path: '/admin/dashboard', component: AdminDashboard },
  { path: '/api/internal/config', component: ConfigPage },
  { path: '/debug/console', component: DebugConsole }
]
```

JsRouteScan 会自动提取这些路由并探测，可能发现：

* `/admin/dashboard` 存在权限绕过
* `/api/internal/config` 泄露敏感配置
* `/debug/console` 未授权访问

### 场景 2：API 接口发现

前端代码中的 API 调用：

```
axios.get('/api/v2/users/list')
fetch('/internal/system/backup')
$.ajax({ url: '/admin/export/data.json' })
```

这些接口可能：

* 未在公开文档中列出
* 缺少权限验证
* 存在越权漏洞

### 场景 3：隐藏功能页面

开发者可能在 JS 中硬编码了一些测试页面或管理页面：

```
if (isDev) {
  window.location = '/test/upload.php'
}
// 或者
const adminUrl = '/secret/admin/panel.html'
```

即使这些页面没有链接入口，JsRouteScan 也能发现它们。

---

## 优势分析

### 1. 自动化程度高

* 无需手动分析 JS 文件
* 被动扫描，不影响正常测试流程
* 自动去重和过滤

### 2. 配置灵活

* 支持自定义正则规则
* 可针对不同网站设置不同策略
* 线程数可调，适应不同网络环境

### 3. 深度探测

* 递归扫描功能可以发现深层路径
* 支持携带原始请求头，绕过简单的防护

### 4. 集成度好

* 原生 Burp Suite 插件
* 结果直接显示在 Burp 中
* 可与其他 Burp 功能联动

---

## 局限性与注意事项

### 1. 正则匹配的局限

**问题：** 正则表达式无法覆盖所有路由格式

**示例：**

```
// 可能无法匹配的情况
const path = base + '/api/' + version + '/user'
const url = `${domain}${endpoint}`
const route = buildPath(['admin', 'users', id])
```

**解决方案：**

* 根据目标网站特点自定义正则
* 结合其他工具（如 LinkFinder）
* 手动分析关键 JS 文件

### 2. 递归扫描的风险

**问题：** 请求数量爆炸

假设有 100 个路由，平均 3 层目录：

```
请求数 = 100 × 3 = 300 次
```

如果路由更多或层级更深，可能产生数千次请求。

**建议：**

* 扫描前清理无用路由
* 分批次扫描
* 控制线程数
* 注意目标网站的 WAF/限流

### 3. 误报问题

**常见误报：**

* 注释中的路径
* 示例代码中的 URL
* 第三方库的内部路径

**示例：**

```
// 这是一个示例：'/example/path'
/*
 * API 文档：https://api.example.com/v1/users
 */
```

**解决方案：**

* 完善 ExRouteRegexs 规则
* 手动审查提取结果
* 结合响应状态码判断

### 4. 动态路由的挑战

**问题：** 无法处理参数化路由

```
// 实际路由
'/api/user/:id'
'/product/{category}/{id}'

// 提取到的可能是
'/api/user/123'
'/product/electronics/456'
```

这些路由需要手动泛化处理。

### 5. 性能影响

**问题：**

* 大量请求可能影响 Burp 性能
* 被动扫描会增加内存占用
* 递归扫描可能导致 Burp 卡顿

**优化建议：**

* 合理设置线程数（建议 5-10）
* 定期清理扫描结果
* 针对性扫描，避免全站递归

---

## 使用技巧

### 1. 正则规则优化

根据目标网站的技术栈调整正则：

**针对 Vue/React 项目：**

```
["'`]([a-zA-Z0-9/_-]+)["'`]\s*:\s*\{?\s*component
```

**针对 API 接口：**

```
["'`](/api/[a-zA-Z0-9/_-]+)["'`]
```

### 2. 分阶段扫描策略

**第一阶段：被动收集**

* 开启被动探测
* 正常浏览网站
* 收集所有路由

**第二阶段：筛选清理**

* 查看 PATH 列表
* 删除明显无用的路由
* 保留可疑路径

**第三阶段：主动探测**

* 先用普通扫描测试
* 确认无问题后使用递归扫描
* 关注 200/403/401 响应

### 3. 结合其他工具

**推荐组合：**

* **JSFinder：** 提取 JS 中的敏感信息
* **Packer Fuzzer：** 解密混淆的 JS 代码
* **Intruder：** 对提取的路由进行参数爆破
* **Logger++：** 记录所有扫描请求

### 4. 针对性配置

**高价值目标：**

* 开启 CarryHead
* 设置完整的 Cookie 和 Token
* 使用较小的线程数（避免触发 WAF）

**快速扫描：**

* 关闭 CarryHead
* 增大线程数
* 只扫描根目录

---

## 与同类工具对比

| 工具 | 类型 | 优势 | 劣势 |
| --- | --- | --- | --- |
| **JsRouteScan** | Burp 插件 | 自动化高、集成度好、递归扫描 | 依赖正则、可能误报 |
| **LinkFinder** | Python 脚本 | 轻量级、正则灵活 | 需手动运行、无自动探测 |
| **JSFinder** | Python 脚本 | 功能全面、提取敏感信息 | 不集成 Burp、需额外处理 |
| **Packer Fuzzer** | Burp 插件 | 解密混淆代码 | 不提取路由 |
| **JS Miner** | Burp 插件 | 可视化好 | 功能相对简单 |

**结论：** JsRouteScan 在自动化和深度探测方面表现突出，适合作为主力工具，配合其他工具使用效果更佳。

---

## 进阶玩法

### 1. 自定义正则库

针对不同框架建立正则库：

```
# Vue Router
VueRegex: ["'`]path\s*:\s*["'`]([^"'`]+)["'`]

# React Router
ReactRegex: ["'`]<Route\s+path=["'`]([^"'`]+)["'`]

# Express.js
ExpressRegex: app\.(get|post|put|delete)\(["'`]([^"'`]+)["'`]
```

### 2. 结合被动扫描器

将 JsRouteScan 提取的路由导出，配合：

* **Nuclei：** 批量漏洞扫描
* **FFUF：** 目录爆破
* **Sqlmap：** SQL 注入测试

### 3. 自动化工作流

```
# 1. 使用 JsRouteScan 提取路由
# 2. 导出路由列表
# 3. 批量测试
cat routes.txt | httpx -status-code -title -tech-detect
cat routes.txt | nuclei -t vulnerabilities/
```

### 4. 监控新增路由

定期扫描目标网站，对比路由变化：

* 发现新增接口
* 监控功能更新
* 及时发现新漏洞

---

## 总结

### 适合使用 JsRouteScan 的场景：

* SPA 单页应用渗透测试
* API 接口发现与测试
* 隐藏功能页面挖掘
* 前端路由权限测试
* 资产收集与信息泄露检测

### 不适合的场景：

* 纯静态网站（没有 JS 路由）
* 严格限流的目标（递归扫描会被封）
* 需要深度 JS 代码分析的场景
* 完全混淆加密的 JS 文件

### 最佳实践：

1. **先被动后主动：** 充分利用被动扫描收集信息
2. **精准过滤：** 根据目标调整正则和过滤规则
3. **分批扫描：** 避免一次性递归扫描所有路由
4. **结合工具：** 与其他工具配合使用，形成完整工作流
5. **持续优化：** 根据实战经验不断完善配置

---

## 写给渗透测试新手

如果你是刚入门的渗透测试工程师，JsRouteScan 是一个很好的学习工具：

1. **理解前端路由：** 通过观察提取的路由，了解现代 Web 应用的架构
2. **学习正则表达式：** 自定义正则规则可以提升你的正则能力
3. **掌握自动化思维：** 体会自动化工具如何提升测试效率
4. **培养安全意识：** 发现开发者容易忽视的安全问题

---

## 相关资源

* **项目地址：**https://github.com/F6JO/JsRouteScan
* **参考项目：**https://github.com/fKzhangsa/FilterJs
* **Burp Suite 官方文档：**https://portswigger.net/burp/documentation
* **正则表达式学习：**https://regexr.com/

---

## 最后

JsRouteScan 是一款实用的渗透测试辅助工具，它不能替代手工测试，但可以大幅提升信息收集的效率。在实际使用中，需要根据目标特点灵活调整配置，结合其他工具形成完整的测试流程。

如果你在使用过程中发现 Bug 或有新的需求，欢迎到 GitHub 提 Issue。开源工具的进步离不开社区的贡献！

**记住：工具只是辅助，思路才是核心。**

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/sz_mmbiz_png/XLoEenAE7ASIz4RAJ9pnvqWIDRXiaT978JAnY7UCQIc9RLgib4WyMKAvN5sJQJq9MlibUyPBJNR5wjvCCrPvcOWQQ/0?wx_fmt=png)

Zacarx随笔

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/XLoEenAE7ASIz4RAJ9pnvqWIDRXiaT978JAnY7UCQIc9RLgib4WyMKAvN5sJQJq9MlibUyPBJNR5wjvCCrPvcOWQQ/0?wx_fmt=png)

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