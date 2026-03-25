---
title: 让 AI 帮你逆向 JS：js-reverse-mcp
url: https://mp.weixin.qq.com/s/KFB4g3ZIGLxYQsIiZrK4kQ
source: Doonsec's feed
date: 2026-03-24
fetch_date: 2026-03-25T04:14:33.176632
---

# 让 AI 帮你逆向 JS：js-reverse-mcp

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/0zk3Ye7cp0309ed7jp36RZoUBLeJ9qL4EicLAfQHFvunUhn6MU2EEx7Habws5mgWRricKszNDp8XsibtcQXOgl20EgUEgTPHibqOZ5s9KzGsxqg/0?wx_fmt=jpeg)

# 让 AI 帮你逆向 JS：js-reverse-mcp

原创

攻防路
攻防路

攻防录

![]()

在小说阅读器中沉浸阅读

#

js-reverse-mcp 是一个 JS 逆向用的 MCP Server。装上之后，Claude Code、Cursor、Copilot 这些 AI 编辑器可以直接操作 Chrome DevTools——搜脚本、设断点、查调用栈，用自然语言就行。

比如你跟 AI 说"打开这个页面，搜所有包含 encrypt 的代码，在加密函数入口设个断点"，它真的会帮你做完。底层基于 Patchright 反检测引擎，知乎、Google 这种有反爬的站也能用。

截至 2026 年 3 月，这个项目在 GitHub 上约 417 颗 star。

---

## 它能做什么

一共 23 个工具，按功能分成六大类：

**页面与导航**

| 工具 | 作用 |
| --- | --- |
| select\_page | 列出所有打开的页面，按索引切换调试目标 |
| new\_page | 创建新页面并导航到 URL |
| navigate\_page | 导航、后退、前进、刷新 |
| select\_frame | 切换 iframe 执行上下文 |
| take\_screenshot | 截图 |

**脚本分析**

| 工具 | 作用 |
| --- | --- |
| list\_scripts | 列出页面加载的所有 JS 脚本 |
| get\_script\_source | 获取脚本源码片段（支持行范围/字符偏移） |
| save\_script\_source | 把完整脚本存到本地文件 |
| search\_in\_sources | 在所有脚本里搜字符串或正则 |

**断点与执行控制**

| 工具 | 作用 |
| --- | --- |
| set\_breakpoint\_on\_text | 通过搜索代码文本自动设断点，对压缩代码特别有用 |
| break\_on\_xhr | 按 URL 模式设 XHR/Fetch 断点 |
| remove\_breakpoint | 移除断点，支持按 ID、URL 或全部移除 |
| list\_breakpoints | 列出所有活动断点 |
| get\_paused\_info | 获取暂停位置、调用栈、作用域变量 |
| pause\_or\_resume | 暂停/恢复执行 |
| step | 单步调试（step over / into / out） |

**函数追踪与注入**

| 工具 | 作用 |
| --- | --- |
| trace\_function | 追踪任意函数调用（包括 webpack 打包的内部函数），无需设断点 |
| inject\_before\_load | 在页面加载前注入脚本，用于拦截和插桩 |

**网络与 WebSocket**

| 工具 | 作用 |
| --- | --- |
| list\_network\_requests | 列出网络请求 |
| get\_request\_initiator | 获取网络请求的 JS 调用栈——就是找到是哪段 JS 发起了这个请求 |
| get\_websocket\_messages | 列出 WebSocket 连接，查看消息内容和模式 |

**检查工具**

| 工具 | 作用 |
| --- | --- |
| evaluate\_script | 在页面中执行 JavaScript，支持在断点上下文中运行 |
| list\_console\_messages | 查看控制台输出 |

---

## 安装和使用

最简单的方式是用 npx，不需要手动安装。

**前置条件：**

* Node.js v20.19 或以上
* Chrome 浏览器

**配置 MCP 客户端：**

在你的 MCP 客户端配置文件里加上：

```
{
  "mcpServers": {
    "js-reverse": {
      "command": "npx",
      "args": ["js-reverse-mcp"]
    }
  }
}
```

各客户端的快捷方式：

Claude Code：

```
claude mcp add js-reverse npx js-reverse-mcp
```

Codex：

```
codex mcp add js-reverse -- npx js-reverse-mcp
```

VS Code Copilot：

```
code --add-mcp '{"name":"js-reverse","command":"npx","args":["js-reverse-mcp"]}'
```

Cursor 的话，在 Cursor Settings → MCP → New MCP Server 里粘贴上面的 JSON 配置就行。

**加强反检测的配置**（推荐对抗风控严格的站点）：

```
{
  "mcpServers": {
    "js-reverse": {
      "command": "npx",
      "args": [
        "js-reverse-mcp",
        "--hideCanvas",
        "--blockWebrtc"
      ]
    }
  }
}
```

**连接已运行的 Chrome**（适合用已登录的浏览器）：

先启动带调试端口的 Chrome：

```
# macOS
/Applications/Google\ Chrome.app/Contents/MacOS/Google\ Chrome --remote-debugging-port=9222 --user-data-dir=/tmp/chrome-debug

# Windows
"C:\Program Files\Google\Chrome\Application\chrome.exe" --remote-debugging-port=9222 --user-data-dir="%TEMP%\chrome-debug"
```

然后配置 MCP 连接：

```
{
  "mcpServers": {
    "js-reverse": {
      "command": "npx",
      "args": [
        "js-reverse-mcp",
        "--browser-url=http://127.0.0.1:9222"
      ]
    }
  }
}
```

---

## 实战场景

### 场景一：分析网页加密参数

你在抓包时发现某个接口的请求参数有加密字段，想找到加密逻辑。

跟 AI 说：

```
打开 https://target.com 并列出所有加载的 JS 脚本
```

```
在所有脚本中搜索包含 "encrypt" 的代码
```

```
在加密函数入口处设置断点
```

然后在页面上触发操作（比如点个按钮），断点命中后 AI 会自动帮你查看参数值、调用栈和作用域变量。整个流程不需要手动打开 DevTools。

### 场景二：追踪 webpack 打包的内部函数

现代网站基本都是 webpack 打包的，代码被压缩混淆到一个巨大文件里。传统方式要在压缩代码里手动找函数入口，非常痛苦。

`trace_function` 工具可以直接按函数名追踪调用，连 webpack 打包的内部函数都能追。比如：

```
使用 trace_function 追踪 webpack 打包的内部函数 "encryptData"，
无需设置断点即可查看每次调用的参数
```

原理是通过 logpoint（日志断点）实现的——在函数入口自动插入日志点，记录每次调用的参数，但不会暂停执行。

### 场景三：WebSocket 协议分析

有些站点用 WebSocket 传数据，在 Network 面板里看 WS 消息比较麻烦，尤其是消息量大的时候。

```
列出 WebSocket 连接，分析消息模式，查看特定类型的消息内容
```

AI 会帮你归类消息类型、分析数据格式，比手动翻 WS 帧高效不少。

### 场景四：逆向登录流程

想分析一个网站的登录请求是怎么构造的，密码是怎么加密传输的。

1. 用 `inject_before_load` 在页面加载前注入拦截脚本，hook 关键 API
2. 打开登录页面
3. 让 AI 搜索 "password"、"sign"、"token" 相关的代码
4. 在关键函数设断点，执行登录操作
5. 断点命中后检查参数传递过程

整个过程用自然语言指挥 AI 完成，连 DevTools 都不用打开。

---

## 和直接用 DevTools 比

| 维度 | 手动 DevTools | js-reverse-mcp |
| --- | --- | --- |
| 操作方式 | 鼠标点击 + 快捷键 | 自然语言指令 |
| 搜索效率 | 一个文件一个文件翻 | AI 批量搜索所有脚本 |
| 设断点 | 得先找到代码位置 | 按代码文本搜索自动定位 |
| 分析能力 | 纯人工 | AI 辅助理解代码逻辑 |
| 反爬绕过 | 手动配置 | 内置多层反检测 |
| 适合对象 | 经验丰富的逆向工程师 | 有 AI 编辑器的开发者 |

手动 DevTools 在灵活性和精细控制上仍然无可替代。但对于"搜代码、设断点、查参数"这类重复性劳动，交给 AI 省时间。

---

项目地址：https://github.com/zhizhuodemao/js-reverse-mcp

欢迎关注“攻防录”✨

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/7vAmdAO11X4lmHfibkjicia7MkfgkmAZCoKicD7poPsfAkjB9o6vqFNE8stLqAYa4gaHHLSmU42FMuYrNiab6mWBWTg/0?wx_fmt=png)

攻防录

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/7vAmdAO11X4lmHfibkjicia7MkfgkmAZCoKicD7poPsfAkjB9o6vqFNE8stLqAYa4gaHHLSmU42FMuYrNiab6mWBWTg/0?wx_fmt=png)

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