---
title: 如何使用AI辅助构建最合适渗透的爬虫系统？
url: https://mp.weixin.qq.com/s/84QEmrxIow6vuk1xKuYo7Q
source: Doonsec's feed
date: 2026-10-16
fetch_date: 2026-10-17T06:29:51.884304
---

# 如何使用AI辅助构建最合适渗透的爬虫系统？

# 如何使用AI辅助构建最合适渗透的爬虫系统？

原创

Yak
Yak

Yak Project

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

![](https://mmbiz.qpic.cn/mmbiz_gif/f7AtEgJhMZfCSs0zKcMmDXyJt76PDpGiataSbajd3BpbZnPXBCqFaA3icu2mY1LGqAmJHIiaCq5N9qCBv47ktQEYA/640?wx_fmt=gif&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_jpg/f7AtEgJhMZd0VthLJpzgmAAibgKmOtuudBzo08KsWzzBtEzpIf5l8zyaU3uqV4GA4USxXeyfnPuQa0ibK1Kr9fibQ/640?wx_fmt=webp&from=appmsg)

一、背景

即使 AI 技术持续演进，经典的漏洞挖掘与渗透测试方法仍然有效。实际工作通常仍围绕 Recon（信息收集）、分析规划和验证测试展开。其中，信息收集阶段能够覆盖的资产与接口范围，会直接影响后续分析和验证的完整性。

AI 可以用于增强传统工作流中的具体环节。本文以渗透测试场景中的 Web 爬虫为切入点，讨论如何利用 AI 分析页面、JavaScript 与构建产物，从已有材料中恢复更多接口、路由及关联资产。

二、爬虫基础演进

为了说明 AI 适合介入的位置，下面按照爬虫的主要观测对象和执行方式，对其能力演进进行划分。

***YAK***

**2.1 爬虫1.0：以 HTTP 和 HTML 为中心**

爬虫 1.0 主要面向传统的多页面 Web 应用。在这类应用中，服务端返回的 HTML 通常已经包含主要页面结构和导航信息。爬虫可以从 `<a href>` 中提取页面链接，从 `<form action>` 中识别表单提交地址，再按照设定的作用域和深度递归访问。

这一阶段的 JavaScript 多用于表单校验、局部交互或页面效果，通常不会决定主要页面和接口的发现过程。因此，仅使用 HTTP 客户端和 HTML 链接提取器，就可以完成基础的网站路径遍历。

一个最小可复现的实现

下面的 `webtree` 函数使用 GNU Wget 实现了一个基础爬虫。它将访问范围限制在起始域名内，按照指定深度递归跟随页面链接，并排除 JavaScript、样式表、图片、字体、压缩包等非 HTML 资源。随后，脚本从 Wget 的访问记录中提取 URL，去重后按照路径层级输出网站树。

该示例适用于 macOS 环境或者常见 Linux 发行版。

Bash

```
 1  webtree() { 2    local start_url="$1" 3    local depth="${2:-3}" 4    local host="${start_url#*://}" 5    host="${host%%/*}" 6   7    if [[ -z "$start_url" ]]; then 8      echo "用法: webtree <URL> [递归深度]" 9      return 110    fi11  12    LC_ALL=C wget \13      --recursive \14      --level="$depth" \15      --delete-after \16      --no-parent \17      --domains="$host" \18      --follow-tags=a,area,frame,iframe \19      --ignore-case \20      --reject='css,js,mjs,map,jpg,jpeg,png,gif,webp,svg,ico,bmp,avif,woff,woff2,ttf,eot,otf,mp3,wav,ogg,mp4,webm,avi,mov,pdf,zip,tar,gz,7z,rar' \21      --wait=1 \22      --timeout=15 \23      --tries=1 \24      "$start_url" 2>&1 |25    awk '/^--[0-9][0-9][0-9][0-9]-.*--  https?:\/\// {print $NF}' |26    sed -E 's/#.*$//; s#^https?://[^/]+##' |27    grep -v '^/robots\.txt$' |28    sort -u |29    awk -F/ -v root="$host" '30      BEGIN {31        print root32      }33      {34        prefix = ""35        level = 036  37        for (i = 2; i <= NF; i++) {38          if ($i == "")39            continue40  41          prefix = prefix "/" $i42          level++43  44          if (!seen[prefix]++)45            printf "%*s%s\n", level * 2, "", $i46        }47      }48    '49  }
```

执行以下命令，对目标进行一层递归：

Bash

```
1  webtree https://public-firing-range.appspot.com/ 1
```

示例输出如下：

Bash

```
 1  public-firing-range.appspot.com 2    address 3      index.html 4    angular 5      index.html 6    badscriptimport 7      index.html 8    clickjacking 9      index.html10    cors11      index.html12    dom13      index.html14    escape15      index.html16    flashinjection17      index.html18    insecurethirdpartyscripts19      index.html20    leakedcookie21      index.html22    mixedcontent23      index.html24    redirect25      index.html26    reflected27      index.html28    remoteinclude29      index.html30    reverseclickjacking31    stricttransportsecurity32      index.html33    tags34      index.html35    urldom36      index.html37    vulnerablelibraries38      index.html
```

对于服务端直接输出完整导航结构的传统 Web 应用，基于 HTTP 和 HTML 的递归遍历已经能够恢复主要页面路径。这种方法实现简单、资源开销较低，可以作为后续方案的基础能力。

它的能力边界也比较明确：不会执行 JavaScript，也无法观察运行时网络请求、客户端路由和动态加载的模块。当应用逐渐转向 React、Vue、Angular 等单页应用架构时，爬虫的观测对象需要从静态 HTML 进一步扩展到浏览器执行状态。

***YAK***

**2.2 爬虫2.0: 以浏览器执行为中心**

随着 React、Vue 和 Angular 等单页应用框架普及，服务端返回的 HTML 往往只包含应用入口和少量静态资源，例如：

XML

```
1  <div id="app"></div>2  <script src="/assets/index-a82f3c.js"></script>
```

此时，`curl` 获取到的通常是一份内容较少的初始 HTML、一个或多个带有内容哈希的 JavaScript Bundle，以及相关静态资源。页面结构、客户端路由和业务数据需要在 JavaScript 执行后，通过 Fetch、XHR 或 GraphQL 等请求进一步加载。

因此，爬虫 2.0 的观测对象从静态 URL 扩展到了浏览器中的应用状态：

Go

```
1  应用状态 = URL + DOM + Cookie/Storage + 已执行操作2  3  状态转换 = 点击 + 输入 + 提交 + 滚动 + 路由跳转
```

即使 URL 和初始 HTML 相同，不同的认证信息、浏览器存储和操作序列，也可能产生不同的 DOM、网络请求和页面数据。爬虫的任务由遍历 URL，进一步扩展为对应用状态及其转换关系的探索。

浏览器爬虫的观测面与实现

浏览器执行 JavaScript 后，可以从以下几个观测面补充静态 HTTP 爬虫的结果：

|  |  |  |
| --- | --- | --- |
| 观测面 | 主要内容 | 对渗透测试的价值 |
| 渲染后 DOM | 链接、按钮、表单、iframe、动态文本 | 发现运行后才出现的入口 |
| 路由状态 | Hash、History API、前端路由变化 | 发现 SPA 内部页面 |
| 网络请求 | XHR、Fetch、GraphQL、WebSocket 握手 | 获得真实接口、方法和参数 |
| 浏览器状态 | Cookie、LocalStorage、SessionStorage | 保持登录态和业务上下文 |

浏览器爬虫通常分为两个阶段。首先加载种子 URL，等待页面达到相对稳定状态，收集渲染后的链接、表单、事件元素和网络请求；随后执行点击、输入或提交等动作，观察 URL、DOM 和网络状态的变化，并对已经访问的状态进行规范化和去重。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/jibGAup6p72H7ib6tPmgXT5T8bQajDd1kKh9DGJJmvJ7RSlTO0Iu7d510ybjThRkIREKX2mOQ2UQa5oHo0Gfz6iclS9A3Cickf68b5yTd3icKYPw/640?wx_fmt=png&from=appmsg)

在现有工具中，ProjectDiscovery Katana 同时提供 Standard 和 Headless 两种模式。Headless 模式能够在浏览器环境中执行 JavaScript，并结合原始响应和渲染后的页面发现端点；启用 XHR 提取后，还可以记录页面运行期间产生的异步请求。Yaklang 的 CrawlerX 则基于 Chromium 浏览器执行页面，通过事件探索和请求拦截收集运行时流量。两者都能处理 SPA，但在动作生成、请求记录和结果组织方式上有所不同。

浏览器爬虫的能力边界

浏览器执行扩大了爬虫的运行时观测面，但发现结果仍然取决于页面是否实际加载了相关资源，以及自动化流程是否触发了对应状态。以下几类资产仍可能被遗漏：

1. 1.**非标准位置中的资源描述：**路由和接口可能出现在 `routes.json`、Runtime Config、Asset Manifest、Source Map 或其他构建文件中。浏览器即使下载了这些文件，也不一定会继续解析其中包含的地址。

1. 2.**未执行或难以执行的 JavaScript：**部分接口只存在于尚未加载的 Chunk、未点击按钮、异常分支、历史代码或混淆后的表达式中。由于相关代码没有实际运行，网络监听无法观察到对应请求。

1. 3.**需要专门解析的接口与协议：**Service Worker、GraphQL、SSE、Socket.IO、WebSocket，以及泄露的 OpenAPI YAML，具有不同的描述形式和交互方式。仅依赖 DOM 遍历或通用网络捕获，通常不足以还原其完整接口关系。

1. 4.**【最难】依赖外部状态的业务流程：**登录、二次核身、扫码确认、移动端支付和跨设备授权等流程需要浏览器之外的状态参与。自动点击和表单填写无法独立完成这类状态转换。

工程实现中通常会结合静态正则、浏览器网络事件或 MITM 代理补充请求记录。这些方法能够观察已经发生的流量，但对未触发代码和非运行时材料的解释能力仍然有限。

这一限制构成了爬虫 3.0 的切入点：在 HTTP 采集和浏览器执行之外，引入一个受限的语义分析层，对已经获得的 JavaScript、配置文件和构建材料继续推导尚未进入请求队列的候选资产。

三、爬虫3.0：AI 驱动的攻击面发现

浏览器爬虫扩展了运行时观测能力，但其发现范围仍然依赖页面实际执行的代码和已经触发的交互。某项资源即使被浏览器加载，也不代表爬虫会继续理解其中描述的接口和关联资产。

例如，浏览器爬虫可能发现 `runtime-config.json`、Asset Manifest 或动态 JavaScript Chunk，却不会自动将其中的路由、服务目录和实时通信地址继续加入请求队列。此时，限制来自对材料语义的理解，而不仅是资源获取能力。

爬虫 3.0 将 AI 引入分析与调度层，使系统能够围绕现有证据回答三个问题：

1. 1.当前材料中包含哪些可以确认的技术线索？

1. 2.哪些高价值线索尚未被展开或验证？

1. 3.下一步应该访问哪些资源，以获得新的接口和资产信息？

AI 在这里承担的是受约束的语义分析任务。它可以分析 Runtime Config、Asset Manifest、Source Map、OpenAPI 文档和复杂 JavaScript，生成带有来源依据的候选 URL，再由普通爬虫完成范围校验和实际请求。

***YAK***

**3.1 基础 MVP：从配置文件生成候选 URL**

先从一个规模较小、结构明确的材料开始。爬虫访问以下地址：

Bash

```
1  https://coldchain.redhaze.top/assets/coldchain/runtime-config.json
```

访问获得的 JSON 内容如下：

JSON

```
 1  { 2    "api_base": "/api/coldchain", 3    "asset_manifest": "/assets/coldchain/asset-manifest.json", 4    "business_unit": "hub", 5    "environment": "production", 6    "integration_spec": "/files/integration/coldchain-partner-api.yaml", 7    "interfaces": { 8      "events": "/events/v1/shipments/stream", 9      "graphql": "/gateway/graphql",10      "legacy": "/api/legacy/v1/regions?callback=ColdChain.regions",11      "socket": "/realtime/socket.io/?EIO=4&transport=polling"12    },13    "release": "v0.6.12+6953643",14    "route_catalog": "/assets/coldchain/routes.json",15    "service_catalog": "/api/catalog/v2/services",16    "service_worker": "/service-worker.js"17  }
```

仅围绕 HTML 标签和 JavaScript 字面量工作的爬虫，通常不会把 JSON 中的任意字符串都视为可访问资源。这样可以减少误报，但也可能遗漏 `asset_manifest`、`route_catalog`、`graphql` 和 `socket` 等具有明确技术语义的字段。

浏览器执行同样不能保证这些资源全部被访问。页面可能读取配置文件，但只使用当前业务状态需要的部分字段。其余地址虽然已经存在于响应中，却不会出现在本轮网络请求里。

为了验证 AI 是否能够补充这一过程，可以将当前 URL、响应内容和输出约束一并提交给模型：

SQL

```
 1  prompt = `作为一个爬虫调度器 2   3  我现在访问 https://coldchain.redhaze.top/assets/coldchain/runtime-config.json 4   5  得到的结果为： 6   7  { 8    "api_base": "/api/coldchain", 9    "asset_manifest": "/assets/coldchain/asset-manifest.json",10    "business_unit": "hub",11    "environment": "production",12    "integration_spec": "/files/integration/coldchain-partner-api.yaml",13    "interfaces": {14      "events": "/events/v1/shipments/stream",15      "graphql": "/gateway/graphql",16      "legacy": "/api/legacy/v1/regions?callback=ColdChain.regions",17      "socket": "/realtime/socket.io/?EIO=4&transport=polling"18    },19    "release": "v0.6.12+6953643",20    "route_catalog": "/assets/coldchain/routes.json",21    "service_catalog": "/api/catalog/v2/services",22    "service_worker": "/service-worker.js"2...