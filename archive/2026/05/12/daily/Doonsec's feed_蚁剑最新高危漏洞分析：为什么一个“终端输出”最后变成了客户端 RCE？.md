---
title: 蚁剑最新高危漏洞分析：为什么一个“终端输出”最后变成了客户端 RCE？
url: https://mp.weixin.qq.com/s/6lAzHpefcbFDM3s6a2R0gA
source: Doonsec's feed
date: 2026-05-12
fetch_date: 2026-05-13T05:44:16.579920
---

# 蚁剑最新高危漏洞分析：为什么一个“终端输出”最后变成了客户端 RCE？

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/FaZFJ7xrqJbibibkHV7uJF1PQMl1LjWeT7IPknjjePLFDtm6lhIdh5XPLSGGGDaJEbzrffQ1jwjIYSjicjxEEOa76ZdUe3X18ROx6wsM3Nsyeo/0?wx_fmt=jpeg)

# 蚁剑最新高危漏洞分析：为什么一个“终端输出”最后变成了客户端 RCE？

原创

MarkSec
MarkSec

六边形攻防安全

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

最近，AntSword 官方 Issue #370 披露了一个非常有意思的漏洞。

很多人第一眼会觉得：

```
“不就是个 XSS 吗？”
```

但实际上，它最后能升级成：

```
客户端本地命令执行（RCE）
```

官方已经在 v2.1.16 中修复。

---

# 一、漏洞核心是什么？

问题出在：

```
终端模块会对服务端返回内容进行二次解析
```

而过滤函数：

```
antSword.noxss()
```

没有完全过滤特殊格式。

攻击者可以构造：

```
[[!;;;;javascript:xxx]{http://test}]
```

最终被终端组件解析成：

```
<a href="javascript:xxx">
```

于是：

```
服务端输出→ 客户端终端渲染→ javascript: 链接→ Electron 执行→ 本地命令执行
```

整个链路本质上是：

```
“远程内容被客户端当成可信代码处理”
```

---

# 二、真正危险的是 Electron

普通 Web XSS 危害其实有限。

但 AntSword 使用的是：

```
Electron
```

并且开启了：

```
nodeIntegration
```

这意味着渲染层可以直接调用：

```
require()child_processfs
```

于是：

```
require('child_process').exec(...)
```

就能直接执行本地系统命令。

所以这个漏洞最关键的地方其实是：

```
Electron 环境下的 XSS ≈ 本地 RCE
```

---

# 三、最容易被忽略的一点：恶意服务端反打客户端

很多人默认：

```
客户端攻击 WebShell
```

但这个漏洞刚好反过来了：

```
恶意 WebShell 反向攻击 AntSword 客户端
```

也就是说：

```
你连接的 Shell 本身可能就是陷阱
```

尤其是：

* 来路不明的 WebShell
* 共享测试环境
* CTF 环境
* 红队钓鱼环境

都可能利用这种思路。

---

# 四、为什么很多复现都用了 auto\_prepend\_file？

因为：

```
auto_prepend_file
```

可以让 PHP：

```
在每次执行前自动加载一个文件
```

这样就能：

```
统一污染所有响应
```

而且：

* 不需要修改已有 WebShell
* 不需要改客户端 Payload
* 隐蔽性很高

所以它经常出现在：

* WebShell 持久化
* PHP 后门
* 流量劫持
* 长驻型木马

等场景里。

---

# 五、测试

这里搭建测试环境，本地蚁剑去连接远程的shell在虚拟终端中执行命令点击构造的链接造成本地代码执行。

本地mac 蚁剑版本V2.1.15

![](https://mmbiz.qpic.cn/sz_mmbiz_png/FaZFJ7xrqJZWQicf2aA5PMnTc9g4Ly15FD7HVb7etoJsd3awdnk28tIgVlibic1J4ZibZ1gewYHxKU6W5NmECQVXyGmVfrXtZndCrMLovibE91JI/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/FaZFJ7xrqJb35x8WWLvSX8OFmHzb8DPJwZn9BgYeQ0v1JyoHsUNxqMRkUaGvklpaYdLLmUGicCO26kbOAV5CjEYspBbFZ3ic155rHJAu5YMb4/640?wx_fmt=png&from=appmsg)

同样笔者测试windows版本v2.1.15同样存在漏洞

![](https://mmbiz.qpic.cn/sz_mmbiz_png/FaZFJ7xrqJZpNj3csmpSpVOUkdrGz5A6wlDvlPeQEFqv3GJEiajUkdEvicatSgfjOGKqYwtYNKcnz6iaiaprGrMicuCF3icA88wuVnkoCGfibMbjI0/640?wx_fmt=png&from=appmsg)

利用代码

![](https://mmbiz.qpic.cn/sz_mmbiz_png/FaZFJ7xrqJYMlJ2gcnicSXI7QmkcgXWvJkpWTEyHJiaK4WTT5oG54lQxSEn7yOU0via9pQKQyIZVQp0bcu8x2iag09ic7QqvBHicfhqStGN1u2JzQ/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/FaZFJ7xrqJaw4gZ1hLdgIx2qDuTwl9Ltovf3jM1nYliaARiaNyibLGLScxicIRfPJ4wjbXAkdSzUPV2OEibqozwM1H8ZiaSzIVXqTY8DzyWhKvav4/640?wx_fmt=png&from=appmsg)

# 六、这个漏洞真正值得学习的地方

以前安全有个核心的安全思想"永远不要相信用户输入的内容"，但今天在这里却是：

```
永远不要相信远程服务器返回的内容
```

哪怕它只是：

```
“一个终端输出”
```

因为：

```
只要客户端会“再次解释”这些内容就可能出问题
```

类似问题其实大量存在于：

* Markdown 渲染
* 富文本编辑器
* 聊天系统
* 日志平台
* AI Agent
* MCP 工具链

---

# 七、最后

这个漏洞虽然已经修复。且这个漏洞其实还是需要用户主动点击终端中的链接（1-click 交互）影响面有限。

但它暴露出来的问题，其实远不止 AntSword。

而是：

```
Electron + 富文本 + Node.js 权限
```

这个组合，本身就天然高危。

未来随着：AI Agent、MCP、桌面化安全工具越来越多。

类似：

```
“远程内容 → 本地执行”
```

的问题，大概率还会继续出现。

---

# 参考链接

* https://github.com/AntSwordProject/antSword/issues/370
* https://github.com/AntSwordProject/antSword/releases
* https://github.com/AntSwordProject/antSword

公众号回复【蚁剑漏洞】获取完整漏洞利用代码及线上测试环境。

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/9qM7NQ3lGkBM9HNjOYhrvc9CNKbbd8pAl3cpffjDBworJnpCOkbD3Flx1XxRPlQbBAicglpPl0ZEGWVzdtCHsdA/0?wx_fmt=png)

六边形攻防安全

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/9qM7NQ3lGkBM9HNjOYhrvc9CNKbbd8pAl3cpffjDBworJnpCOkbD3Flx1XxRPlQbBAicglpPl0ZEGWVzdtCHsdA/0?wx_fmt=png)

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