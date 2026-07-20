---
title: JavaScript 逆向 &amp;&amp;渗透测试辅助工具&amp;&amp;AntiDebug_Breaker_mcp
url: https://mp.weixin.qq.com/s/itztvjkR88LosymeRo4bRA
source: Doonsec's feed
date: 2026-07-19
fetch_date: 2026-07-20T05:30:49.136090
---

# JavaScript 逆向 &amp;&amp;渗透测试辅助工具&amp;&amp;AntiDebug_Breaker_mcp

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/MSDUaqtwboTP0XP25JFE8KMJMcGV8FmQkMZbjOHDKJvAtRmmg08nP83MnHSVm9YFtVbENvuOSmTKZDpCSe8pTHs5ERKZdKvXWznx0sUyF7U/0?wx_fmt=jpeg)

# JavaScript 逆向 &&渗透测试辅助工具&&AntiDebug\_Breaker\_mcp

vs-olitus
vs-olitus

陌笙不太懂安全

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

免责声明

```
由于传播、利用本公众号所提供的信息而造成的任何直接或者间接的后果及损失，均由使用者本人负责，公众号陌笙不太懂安全及作者不为此承担任何责任，一旦造成后果请自行承担！如有侵权烦请告知，我们会立即删除并致歉，谢谢！
```

## 🌍工具简介

AntiDebug Breaker MCP 是一款专为前端 JavaScript 逆向工程和渗透测试设计的 Chrome 浏览器扩展，基于 Hook\_JS 库开发，提供强大的反调试绕过、API Hook、Vue 路由获取等功能。

### 🔓 反调试绕过 —— 扫清分析障碍

前端页面常通过无限`debugger`、时间差检测、窗口尺寸嗅探、控制台清空等手段干扰调试。本模块针对这些防护逐一击破：

* **代码层绕过**：拦截`eval`、`Function`构造器等代码执行入口，从源头化解无限循环断点
* **行为层对抗**：阻止页面强行关闭标签页或操作历史记录，避免调试过程中断
* **环境层伪装**：固定窗口尺寸与时间相关API（如`Date.now`），消除基于环境特征的反调试判断
* **加密库Hook**：对CryptoJS、JSEncrypt等主流加密库进行底层拦截，加解密过程尽在掌握
* **跳转定位**：快速追溯页面跳转的触发源头，不再被路由逻辑牵着鼻子走

### 🪝 API拦截 —— 洞察数据流向

业务逻辑往往藏匿于浏览器API的调用链中，通过精准拦截可快速定位关键节点：

* **存储层监控**：全面跟踪`localStorage`与`sessionStorage`的增删改查，捕获所有持久化数据变更
* **网络层捕获**：拦截`XMLHttpRequest`与`fetch`请求，实时查看请求头、参数及响应内容
* **数据流追踪**：监控`JSON.parse/stringify`，观察数据在序列化前后的形态变化
* **异步定位**：Hook Promise的`resolve`方法，让异步回调的触发点不再神秘
* **环境固化**：固定`Math.random`返回值，消除随机变量对分析过程的干扰

### 🌐Vue - 路由分析

针对 Vue.js 框架的专属功能，快速获取和分析路由信息。

![](https://mmbiz.qpic.cn/mmbiz_png/MSDUaqtwboQibJmnyJEasPAkPzbyXs5WE1dJpsWobbPfglIoazzOG4psQ98Y1FPonJTiaic33icPFRR4H0xJtMGia3jeibiaUNp3mIiaC9Qnza5Dwbo/640?wx_fmt=png&from=appmsg)

| 脚本名称 | 功能描述 |
| --- | --- |
| **获取路由** | 获取 Vue Router 中所有已加载的路由 |
| **清除跳转** | 清除 Vue Router 的跳转方法 |
| **清除路由守卫** | 清除 beforeEach 和 beforeResolve 守卫 |
| **激活 Vue Devtools** | 强制激活 Vue Devtools 调试工具 |

**Vue 板块特性：**

* 📋 **路由列表**：一键查看所有路由，支持搜索过滤
* 🔗 **快速操作**：复制路由、直接打开页面
* 📦 **批量导出**：一键复制所有路径或完整 URL
* 🎯 **自定义前置路由**：灵活配置路由前缀

### 📝 Headers - 请求头管理

全局请求头注入功能，类似 ModHeader 扩展，支持分组管理。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/MSDUaqtwboS7ebS7RQAN1YrC28VcuXOaewOvqPNQQc5hkhkp4uY45KpHufRRHfMXWCCSic1zPom8x1BSl3cL1AbMF6zsTyFWc35fo7uZEGyc/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/MSDUaqtwboSECqdVonnaOx9uaYgQcKO4bicYrG8d8vfjpGvibf4icyHmuTVxaQpAZQfHrpWFNNV3s8gQghxiaXibc3PTO7BVRamapm57wR4k8880/640?wx_fmt=png&from=appmsg)

| 功能 | 说明 |
| --- | --- |
| **请求头分组** | 创建多个请求头组，快速切换不同环境配置 |
| **全局注入** | 请求头自动添加到所有 HTTP 请求 |
| **启用/禁用** | 单独控制每个请求头的启用状态 |
| **MCP 集成** | 通过 AI 工具管理请求头配置 |

**使用场景：**

* 🔐 添加认证 Token（Authorization、X-Token 等）
* 🏢 切换租户 ID（tenant-id）
* 🧪 测试不同环境的请求头配置
* 🔧 调试 API 接口

### 🤖 MCP - AI 集成

🔗 支持 Model Context Protocol (MCP)，可通过 Cursor AI 直接控制浏览器。

**MCP 功能：**

* 🔌 与 Cursor AI / Claude / Trae 等编辑器无缝集成
* 🌍 全局操作模式：通过页面标题匹配操作任意标签页
* 🛠️ 60+ 专用工具：页面分析、网络监控、加密捕获、请求头管理等

## 📖 使用说明

### ⚡ 基本操作

1. **开启脚本**：点击对应脚本的开关按钮
2. **刷新页面**：脚本生效需要刷新目标页面
3. **查看结果**：打开 F12 控制台查看 Hook 输出

### 🔄 模式切换

* **标准模式**（默认）：脚本仅注入到当前网站
* **全局模式**：脚本注入到所有网站

> ⚠️ 对于 `file://` 协议或 `localhost` 页面，必须开启全局模式

### 🪝 Hook 板块使用

1. **基础使用**：开启脚本后，所有相关操作都会打印到控制台
2. **关键字过滤**：开启「检索关键字」，添加关键字后只捕获匹配内容
3. **断点调试**：开启 `debugger` 按钮，捕获时自动断点
4. **堆栈追踪**：开启 `stack` 按钮，打印完整调用堆栈

### 🌐 Vue 路由获取

1. 开启「获取路由」脚本
2. 刷新目标 Vue 网站
3. 返回插件查看「路由列表」标签页
4. 点击「复制」或「打开」操作路由

### 📝 请求头管理

1. 点击左侧「Headers」菜单进入请求头管理
2. 点击「新建分组」创建请求头组
3. 在分组中添加请求头（名称和值）
4. 点击分组右侧的「启用」按钮激活该组请求头
5. 所有 HTTP 请求都会自动携带已启用的请求头

**使用技巧：**

* 🔄 **快速切换**：创建多个分组（如"开发环境"、"测试环境"），一键切换
* ✅ **单独控制**：每个请求头可单独启用/禁用
* 🤖 **MCP 管理**：通过 AI 工具快速配置请求头

## 🤖 MCP 提示词与案例

### 💬 常用提示词

> 📝 **使用说明：** 将 `{网站title}` 替换为目标网站的实际标题

#### 🔍 一键分析页面

```
请帮我调用 AntiDebug_Breaker_mcp 分析 {网站title} 页面，检测反调试机制、前端框架、加密方式和认证机制
```

#### 🔐 加密算法逆向

```
请帮我调用 AntiDebug_Breaker_mcp 分析 {网站title} 输入内容"你好啊"后会触发 API 接口：https://xxxx.com/translate/key?mysticTime=xxx&token=xxx&sign=xxx帮我还原出 sign 的加密算法，并进行发包验证
```

#### 🔥 综合渗透测试

```
请帮我调用 AntiDebug_Breaker_mcp 对 {网站title} 进行完整的前端安全分析：1. 检测并绕过反调试2. 获取所有 Vue 路由3. 批量访问路由收集 API4. 扫描敏感数据泄露5. 分析加密和认证机制
```

#### 🛡️ 后台系统测试

```
请帮我调用 AntiDebug_Breaker_mcp 对 {网站title} 测试后台系统的前端安全：1. 获取所有路由2. 检测未授权访问3. 扫描敏感信息泄露4. 分析接口签名
```

工具链接

```
https://github.com/vs-olitus/AntiDebug_Breaker_mcp
```

**后台回复加群加入交流群**

**广告：****cisp pte/pts &nisp1级2级低价报考**

**陌笙安全纷传圈子+陌笙src挖掘知识库+陌笙安全漏洞库+陌笙安全面试题库****简单介绍****（****加入纷传圈子****送****知识库+漏洞库+面试题库****）**

如果觉得合适可以加入,圈子目前价格39.9元，价格只会根据圈子内容和圈子人数进行上调，不会下跌。。。

**圈子福利**

**edu漏洞挖掘1v1指导出洞**

![](https://mmbiz.qpic.cn/mmbiz_png/MSDUaqtwboRKQWHxLsRrPqpqdiceX76d7yExQIyOqFmmJAfHQh7qzKvPc2V5z6iaa0RY6Ib8AsGvgS5MKkAk5aaHnJBaSnI10LDKQYMLcQMmg/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/MSDUaqtwboR8pnPeapLBK4Jsa4ufCvFoGL66t7PKeZyA3AjNxsObjtnCibN2gzGX7NMS7Wo5sj3YYL2iboeRuQDcWqiapc8xuo5fticoBG4DsyY/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/MSDUaqtwboRKIBNIQIVicRWJLbyGRmg92vPzc8375PJpcYVvfywzwqnaeBicZuEbfvuic9KRdjwkahSDic5VqrH2Mb4NkqtkADl5HLIh8gPex60/640?wx_fmt=png&from=appmsg)

**陌笙src挖掘知识库介绍（内容持续更新中!!!)**

```
信息收集(主域名信息收集,子域名信息收集等&会永久提供fofa-key助力)弱口令漏洞&未授权访问漏洞挖掘任意文件读取&删除&下载&上传漏洞sql注入漏洞url重定向漏洞csrf&ssrf漏洞挖掘XSS&XXE漏洞挖掘等等常见漏洞cors&目录遍历&越权漏洞挖掘EDUSRC(证书站挖掘案例分享&edusrc挖掘技巧分享)CNVD挖掘技巧分享&实战案例报告编写公益漏洞挖掘（公益src挖掘漏洞分享&提供补天1权重资产）SRC挖掘实战(针对各种常见功能总结的常见测试思路等快速提升)经典常见Nday漏洞(常见中间件&以及各种常见框架)复现云安全相关漏洞挖掘（云key扫盲&云存储桶&快速识别云环境&云攻防）AI相关学习（AI基础&AI代码审计实战测试&webLLM攻击等）APP&小程序漏洞挖掘等各模块不在一一介绍
```

信息收集

![](https://mmbiz.qpic.cn/sz_mmbiz_png/MSDUaqtwboTu9DGyTubluhYicFynwVBKa4V06sDfEVKOyk5Q4ghZzLMDAuLb1M1oR4RJumGWrADPapFjTrOjpksKQ8q0YYCnl3ZWLof8Knzg/640?wx_fmt=png&from=appmsg)

src挖掘基础

![](https://mmbiz.qpic.cn/sz_mmbiz_png/MSDUaqtwboR45bibbJEb28a1gS5yth3r5HyOsgPiaOUHHYriahZyIyrk0LMOsHW4VoDibyBRibTNzptGiaLWX62UwykicwvbxCJPopvklqiaxML8lS8/640?wx_fmt=png&from=appmsg)

src挖掘实战

![](https://mmbiz.qpic.cn/sz_mmbiz_png/MSDUaqtwboTKWnTsN6CXf3djhXIlMKNRjVmJn3g5b23ur9E6Cx3O68f0hXVjCiaj8J4RYeTGBecqf1k99phG0ice2wtd5lKgR46OeqeLQfMpk/640?wx_fmt=png&from=appmsg)

edusrc

![](https://mmbiz.qpic.cn/mmbiz_png/MSDUaqtwboQVVlTXhibjR8UiakZBQicXRZrQ7hdoOz5G8MQrcuDBGbqJdO0kIz6R9IU4ObAeOiabT8pr6lc7jibdIkKoTjiaXNHPLAwAB3BV2UvLM/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/MSDUaqtwboSCrvarBbzP4L9kS6P0LVH9JMdmcbFDKiaicHqMFgTxq3x4iatjDJQicmc7NPC14C9Fk3icFjrouSgNVaN8Byuf0C0Iq9O6D1XPvFvY/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/MSDUaqtwboRALwXmgZ4mh2LW0RdicrKjBCP7P1iaF14G0Eq2v3KRnTJORpwXZlF58WEz6QicxLJpyJaA5iah5CF2rHjBz4JzOELFRaZTAKOQ2tQ/640?wx_fmt=png&from=appmsg)

经典nday复现

![](https://mmbiz.qpic.cn/sz_mmbiz_png/MSDUaqtwboRu8Gf849iaCkSBxLL8IlzJTRs185QicEe9l5UGI1dEVKISt2IGGveZynXBW9tIUsxNsz4adSTib7rib50uSJdjNfTvVRFrbPJhzL4/640?wx_fmt=png&from=appmsg)

云安全&AI安全

![](https://mmbiz.qpic.cn/mmbiz_png/MSDUaqtwboQ9qiavETNjaaX162czpNCqpw3uJqVpicbI15AXzhf5x8icmHxBdTGOgRgzNPGF3Aw2gglT4Fx09JGXYibQC6U7CQKVmoH08l3meia4/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/MSDUaqtwboQgcsjiaZ4S26TWowHfpBkhSeHf2pjrcDyicJuia3uqvRBauLEOicibibEMqibnBMtjopFL8No7UXNibbURvzeJ3dQHTibvGxRQGnorb4co/640?wx_fmt=png&from=appmsg)

**陌笙安全漏洞库介绍**

```
最新漏洞查看1day&0day分享EDU学校相关漏洞Web应用漏洞CMS漏洞OA产品漏洞中间件漏洞云安全漏洞人工智能漏洞其他漏洞
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/MSDUaqtwboTFBRMa8XwYxfcZMyXicx94xSKxawPcqFia2rJKOL7fSLYXiccwHc868XxNGIQ5z7ibiaI1MNAGRrK7U6wXJTsZOCAu2I5XV1boTAL4/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/MSDUaqtwboSBzdakI9XI33ReAm2dxO8vgzw3JicQmUuWCb5ayBlKR1PoQHEHFETteBnicyupwU0mXvXibfrDoyg8nSWBGoK1p2YXY3ElhcvOQ0/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/MSDUaqtwboSajCclDhuRpaLic9Ld915CHU7RqSC1LCrPGfNZiavdPEVeDedDWOPBhtMLCicTp3RNd1lT0Pmfo3mx5B0hUxbQg3ic6Via90NMtZVk/640?wx_fmt=png&from=appmsg)

**陌笙安全面试库**

```
渗透测试基本问题一汇总渗透测试基本问题二汇总渗透测试基本问题三汇总微步护网面试题目长亭科技面试深信服护网面试启明星辰渗透测试面试题目安恒面试题目绿盟笔试题目360面试奇安信护网面试运维面试题目运维面试题库网安面试相关文档大全相关面试文章推荐等等
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/MSDUaqtwboSoLqEzH0a3A4LQrvTIkGx81Sh5pf6fCoEQJhYg715vrJicSkfBuCoAmV2Kp4uOMe5jcUZutPwicibFibtJ1ZmyiaAibCg0XicWnsNcicE/640?wx_fmt=png&from=appmsg)

**POC库****&&更新适配afrog&&nuclei&&dddd的POC&1day/Nday等&&******dddd二开******工具[助力渗透测试&&红蓝攻防]**

**工具截图**

**![](https://mmbiz.qpic.cn/mmbiz_png/MSDUaqtwboRLmmY4kF0AaQjAJUQzH1sAExGoE7AmDJZXcEgdnKuRkpgZ9xYflY0UxtVkrP4HicDfvCW...