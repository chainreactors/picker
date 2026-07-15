---
title: Src捡钱12，AI一键自动挖掘小程序漏洞
url: https://mp.weixin.qq.com/s/g88J0mJZXAp59Xj5beZKgw
source: Doonsec's feed
date: 2026-07-14
fetch_date: 2026-07-15T04:46:13.227203
---

# Src捡钱12，AI一键自动挖掘小程序漏洞

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/2BCHXx7iavkTZS2bx3tdFvGAZuW7I7BV7icLx5iaT2rAkZEprEXY5OHKia7XgcffIQhPcuRvAzxk9n4p9wbjUEmkjks9FChVq5WYM0cMFNvYQLU/0?wx_fmt=jpeg)

# Src捡钱12，AI一键自动挖掘小程序漏洞

an7ln
an7ln

山河学安全

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

**免责声明**

本公众号山河学安全旨在分享网络安全领域的相关知识和工具，仅限于学习和研究之用。由于传播、利用本公众号山河学安全所提供的信息而造成的任何直接或者间接的后果及损失，由使用者承担全部法律及连带责任，公众号山河学安全及作者不为此承担任何责任。如有侵权烦请告知，我们会立即删除并致歉，谢谢。**工具安全性自测！**

![](https://mmbiz.qpic.cn/sz_mmbiz_png/2BCHXx7iavkTeD7TNYmuA54EfmkQzaFJtx9YChJGYjb7v6xQZkNicV0G7a53zQGJVRZUnE0BnExCiat37mg5YxBiafZcPnR2g6ENW6As5vpXSXM/640?from=appmsg)

**PART**

**01**

**工具概述**

本项目是一个本地 Streamable HTTP MCP Server，用于把 WMPFDebugger 暴露的裸 Chrome DevTools Protocol WebSocket 包装成 MCP 工具，辅助 Codex / Cursor / VS Code Agent 对已授权调试的微信小程序进行安全评估、证据采集和报告整理。

**PART**

**02**

**使用方法**

**使用边界**

• 仅用于已获得授权的小程序、本机调试环境和当前 WMPFDebugger 会话。

• MCP HTTP 服务只监听 127.0.0.1。

• 默认只连接 ws://127.0.0.1:62000，CDP URL 只允许 127.0.0.1 或 localhost。

• /mcp 必须携带启动时输出的 token。

• 主动请求修改/重放能力未实现；当前工具只做被动采集、单次页面交互观察和人工验证计划生成。

• 点击类工具会拦截支付、提交订单、删除、注销、退款、提现、确认支付等危险文本，默认不执行，必须显式 requireConfirm=true。

**安装与启动**

npm install
npm run dev

也可以指定固定 token：

$env:MCP\_TOKEN="your-local-token"
npm run dev

启动后访问根路径查看当前 MCP URL：

http://127.0.0.1:43827/

默认 MCP URL：

http://127.0.0.1:43827/mcp?token=wmpf-local-token

**Codex 配置**

[mcp\_servers.wmpf]
enabled = true
url = "http://127.0.0.1:43827/mcp?token=wmpf-local-token"
startup\_timeout\_sec = 20
tool\_timeout\_sec = 60

**建议测试提示词**

使用 wmpf MCP，先调用 status，然后 connect\_wmpf 连接 ws://127.0.0.1:62000。
随后调用 hook\_wx\_request 和 hook\_fetch\_and\_xhr，打开当前小程序页面并操作关键业务流程。
再调用 dump\_runtime\_snapshot、get\_all\_requests、get\_api\_inventory、analyze\_auth\_surface、find\_idor\_candidates、find\_sensitive\_data\_exposure、find\_upload\_surfaces、find\_payment\_and\_order\_surfaces、find\_sign\_related\_requests。
请基于证据生成 generate\_security\_notes，只输出发现线索和人工验证建议，不直接下漏洞结论。

**工具列表**

**基础连接与 CDP**

• status：查看 MCP 和 CDP 连接状态。

• connect\_wmpf：连接本机 WMPFDebugger CDP WebSocket，并启用 Runtime/Network。

• select\_appservice\_context：自动枚举 Target、flatten attach，并选择包含 wx.request / require / getCurrentPages 的 appservice Runtime context。

• cdp\_call：调用任意 CDP 方法，支持传入 flatten sessionId。

• cdp\_call\_target：对指定 targetId 自动 Target.attachToTarget({ flatten: true }) 后在子 session 中调用 CDP。

• runtime\_eval：在当前 Runtime 执行 JS。

• runtime\_eval\_appservice：在自动选择的 appservice Runtime context 中执行 JS。

• network\_enable：启用 CDP Network。

• get\_recent\_requests：读取最近 CDP Network 请求，支持 domain、pathPrefix、keyword、excludeStatic、compact 过滤。

• get\_response\_body：尝试读取 CDP 响应体。

• get\_recent\_console：读取 console 和 exception 事件。

**运行时与页面探索**

• dump\_runtime\_snapshot：采集页面运行时快照、storage 摘要、可见文本、可交互元素、疑似框架对象。

• get\_basic\_page\_info：兼容旧版页面信息工具。

• get\_document\_html：读取 document HTML 前缀。

• query\_selector\_text：读取指定元素文本和 HTML。

• list\_interactive\_elements：列出按钮、输入框、链接及高风险关键词元素。

• safe\_click\_and\_observe：单次点击并观察 URL、文本、storage、请求和 console 变化。

• input\_text\_and\_observe：输入文本并观察变化。

• inspect\_window\_keys：检索 window keys。

• search\_global\_string：搜索页面、脚本、window keys 中的单个关键词。

**网络采集与接口资产**

• hook\_wx\_request：自动选择 appservice context 后注入非破坏性 wx.request hook。

• hook\_fetch\_and\_xhr：注入非破坏性 fetch/XHR hook，记录响应和调用栈。

• get\_hooked\_requests：读取 fetch/XHR hook 记录。

• get\_all\_requests：汇总 CDP、wx.request、fetch/XHR 请求，并统一格式。

• get\_request\_detail：查询单个请求详情，CDP 请求会尝试读取响应体。

• get\_api\_inventory：按 method + path 生成接口资产清单。

**漏洞线索识别**

• analyze\_auth\_surface：分析认证字段、token 位置、query token、缺失认证和重放线索。

• find\_idor\_candidates：查找越权候选接口，只给人工验证建议。

• find\_sensitive\_data\_exposure：查找敏感字段并默认脱敏。

• find\_upload\_surfaces：识别上传、文件、图片、头像、媒体接口。

• find\_payment\_and\_order\_surfaces：识别支付、订单、优惠券、钱包、积分接口。

• find\_debug\_admin\_surfaces：识别 debug/test/admin/internal/dev/staging/mock 线索。

• find\_sign\_related\_requests：识别 sign/signature/timestamp/nonce 请求。

**主动验证辅助但默认安全**

• build\_replay\_plan：根据请求生成 Burp Repeater 人工重放计划，不发送请求。

• compare\_two\_requests：对比两个请求的 URL、header、body、auth 和 response 差异。

• passive\_param\_fuzz\_suggestions：生成参数 fuzz 建议，不发送请求，并标注需要授权环境人工验证。

**源码与签名逻辑分析**

• inspect\_wx\_config：读取 \_\_wxConfig、\_\_wxAppCode\_\_、\_\_wxRoute、\_\_wxAppData\_\_ 摘要和关键词命中。

• search\_runtime\_keywords：搜索 window keys、document HTML、script 文本、storage 和已抓请求。

• trace\_request\_callstack：从 hook 记录中提取发起请求的 JS 调用栈。

**状态篡改/复原辅助**

• inspect\_vuex\_store：在 appservice context 中查找 Vuex-like store，保存原始 state 快照，并返回 state/mutations/actions 摘要。

• patch\_vuex\_state：按 path 修改 state 或调用 mutation。默认 dryRun=true，只有 dryRun=false 且 requireConfirm=true 才会修改本地 Runtime 状态。

• restore\_vuex\_state：从 inspect\_vuex\_store 保存的快照恢复 state。默认 dryRun=true，只有 dryRun=false 且 requireConfirm=true 才会恢复。

**报告与证据**

• export\_session：导出当前会话 JSON 到 reports/session-\*.json。

• generate\_security\_notes：生成 Markdown 安全评估笔记，只写发现线索和验证建议。

• generate\_api\_table\_markdown：生成接口清单 Markdown 表格。

**推荐工作流**

1. 启动 WMPFDebugger 并确认 DevTools 可连接 ws=127.0.0.1:62000。

2. 启动本项目并把启动输出的 MCP URL 配入 Codex。

3. 调用 connect\_wmpf。

4. 调用 select\_appservice\_context，确认选中的 context 包含 wx.request / require。

5. 调用 hook\_wx\_request 和 hook\_fetch\_and\_xhr。

6. 在小程序中人工操作登录、搜索、下单前流程、个人中心、地址、优惠券、上传等页面。

7. 使用 get\_recent\_requests 的 excludeStatic=true、domain、pathPrefix 过滤图片、字体、data URI 等噪声。

8. 调用 get\_api\_inventory 和各类 find\_\* 工具生成线索。

9. 对候选接口使用 build\_replay\_plan、compare\_two\_requests、passive\_param\_fuzz\_suggestions 制定人工验证步骤。

10. 如需验证前端状态授权绕过，先调用 inspect\_vuex\_store 保存快照，再用 patch\_vuex\_state dry-run 预览；确认后才设置 dryRun=false 和 requireConfirm=true。结束后用 restore\_vuex\_state 复原。

11. 调用 export\_session 和 generate\_security\_notes 保存证据与笔记。

**构建**

npm run build
npm start

**PART**

**03**

**工具下载**

**关注名片进入公众号**

**回复关键字【260714】获取下载链接**

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/0sjvG0TycCrkwqc9NOyXnxJdd3Sx952ibuNc9JbaRIwgribBX5MRFHecGVwgntRMicphmT55OA24qTJdzwXhegujQ/0?wx_fmt=png)

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