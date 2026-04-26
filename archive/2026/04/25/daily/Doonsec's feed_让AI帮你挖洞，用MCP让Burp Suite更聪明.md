---
title: 让AI帮你挖洞，用MCP让Burp Suite更聪明
url: https://mp.weixin.qq.com/s/j1ZvM_4OQsE06QUyPx9ykw
source: Doonsec's feed
date: 2026-04-25
fetch_date: 2026-04-26T04:59:18.123550
---

# 让AI帮你挖洞，用MCP让Burp Suite更聪明

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/6fnkZFq8xebV3GZQ6QkROZOQVmkadKqXoiabcgNLmzZTnaqSGoVrPKRma65dTicEjqH5LPciafgoiawDEl4zdw4RpXe9KIj5n5mhmibVEEY1NWlY/0?wx_fmt=jpeg)

# 让AI帮你挖洞，用MCP让Burp Suite更聪明

C4安全

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

以下文章来源于有恒安全
，作者有恒

![](http://wx.qlogo.cn/mmhead/Q3auHgzwzM4P2gbKZcItyLUXAbDPIo3k3pnwpOxcoibDho6RTsh2Z7A/0)

**有恒安全**
.

安全技术知识分享

在渗透测试的时候，遇到了一个注入，该注入点有点奇怪，if(1=1),if(1=2)都恒为真，都会延时

![](https://mmbiz.qpic.cn/mmbiz_png/6fnkZFq8xeaUKEyXLnFrkUuHucZAJ4IWqAJic3K4s08ckDr5jKTGORBKxvhrXGpTC42jhRMVwuuuhT0aWZrlb6qTBh3JT9XKQxDPQiaSXz46s/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/6fnkZFq8xeZYoxhiaHynV1S2rHNdodaSZJ9pCVFMHnGKSwgUBL5VADWPKDOriaTJafeGopn5eFicqeAcPZOXTZVQWh1Vjf17icC6aHbwx9tXxBQ/640?wx_fmt=png&from=appmsg)

无法进行条件判断，使用case when，exp等函数也被过滤了，该网站有黑名单过滤，耗了大量时间也找不到能证明危害的办法。使用了sqlmap也跑不出结果。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/6fnkZFq8xeYEy0DpZYPqWJtHZFrb9icMcfQqN1NRzsicPjkrMAcbIQG8jJVZDmFvHXLkMr9bE8BeI5atN2Whiczx2V1eM1zYUh6lqJzNcnGp24/640?wx_fmt=png&from=appmsg)

不然就试试Burpsuite-MCP与Claude Code联动。

配置教程我让ai总结了一下

```
Burp Suite 与 Claude Code MCP 联动配置教程本文详细介绍 Burp Suite 与 Claude Code MCP 联动的完整配置流程，包含环境准备、两端配置、联动验证及故障排查，步骤清晰、操作简单，新手可快速上手完成配置。一、前置准备（统一操作步骤）1. 安装必备软件Burp Suite：安装专业版或社区版（推荐 2024.6 及以上版本），确保软件可正常启动。Python 环境：安装 Python 3.9~3.12 版本（避免 3.14 及以上版本的兼容问题），安装时务必勾选「Add Python to PATH」。Claude Code：确保已安装并可正常启动（终端输入 claude 可进入 Claude 终端）。2. 安装 mcp-proxy 工具打开 CMD 终端，执行以下命令安装核心依赖：pip install mcp-proxy安装完成后，执行 where mcp-proxy 查看安装路径（默认路径格式：C:\Users\用户名\AppData\Local\Programs\Python\Python3xx\Scripts\mcp-proxy.exe），记录该路径备用。二、Burp Suite 端配置（关键步骤）打开 Burp Suite，进入「扩展」→「BApp Store」，搜索「MCP Server」扩展，点击「安装」。安装完成后，切换到「扩展」→「已安装」，找到「MCP Server」扩展，确认其状态为「已加载」。点击 Burp 顶部菜单栏新增的「MCP」标签页，进行如下设置：
勾选「Enabled」，启用 MCP 服务器；监听地址默认为 http://127.0.0.1:9876（若端口被占用，可修改为其他端口，如 9877，记录修改后的端口备用）；确认「Server status」显示为「Running」（运行中），即完成 Burp 端配置。三、Claude Code 端配置（核心步骤）1. 找到配置文件Claude 的 MCP 配置文件路径为：C:\Users\用户名\.claude.json（若该文件不存在，新建文本文件并将其重命名为 .claude.json 即可）。2. 写入标准配置将以下内容复制到 .claude.json 中，替换「用户名」为实际电脑用户名，替换 mcp-proxy 路径为前文记录的实际安装路径：{  "mcpServers": {    "burp": {      "type": "stdio",      "command": "C:\\Users\\用户名\\AppData\\Local\\Programs\\Python\\Python312\\Scripts\\mcp-proxy.exe",      "args": [        "--transport",        "sse",        "http://127.0.0.1:9876"      ],      "disabled": false    }  }}3. 配置说明command：替换为实际的 mcp-proxy.exe 完整路径；args 中的 URL：需与 Burp 中 MCP 监听地址保持一致（若 Burp 修改了端口，此处同步修改）；无需额外添加 env 或 --named-server 参数，避免导致启动失败。4. 验证配置文件格式打开 CMD 终端，执行以下命令检查 JSON 格式是否正确（无报错即格式正常）：python -m json.tool C:\Users\用户名\.claude.json四、启动联动并验证完全关闭 Claude Code：退出当前所有 Claude 终端，重新打开 CMD 终端。启动 Claude Code：在新终端中输入 claude 并回车，进入 Claude 终端。检查 MCP 配置：输入 /mcp 并回车，查看配置列表：
若 burp 显示 √ connected，说明联动配置成功；若显示 × failed，可参考下方故障排查步骤处理。五、常见故障排查1. Burp MCP 未运行检查 Burp 的 MCP 标签页是否勾选「Enabled」；重启 Burp 后，重新启用 MCP 扩展；端口被占用：修改 Burp 监听端口，同步修改 .claude.json 中的 URL 端口。2. mcp-proxy 启动失败重新安装依赖：执行 pip uninstall mcp-proxy && pip install mcp-proxy；检查路径：确认 command 中的 mcp-proxy.exe 路径正确，可直接在 CMD 中输入该路径，测试是否能正常启动。3. Claude 显示 burp 连接失败关闭所有 Claude 终端，重新启动后再次尝试；检查 .claude.json 格式，确保无多余逗号、引号等语法错误；查看详细日志：终端输入claude --debug，搜索 burp 相关报错（如路径错误、端口拒绝），针对性修改。4. Python 版本兼容问题若使用 Python 3.14 及以上版本出现异常，卸载当前版本后，安装 Python 3.12 版本，重新安装 mcp-proxy 即可。六、最终验证步骤Burp MCP 状态：显示 Running ✅mcp-proxy 手动运行：输入 mcp-proxy.exe --transport sse http://127.0.0.1:9876，无报错 ✅Claude Code 终端输入 /mcp：burp 显示 connected ✅完成以上所有步骤，Burp Suite 与 Claude Code 即可正常联动。
```

**配置好后连接成功**

![](https://mmbiz.qpic.cn/mmbiz_png/6fnkZFq8xeYADL64iaFoNo4t7xDRbuUlYVXVG1KXmJ56ogbKMhMFrYEzVSDrVibYVCEs59sbKfAGR07KHkdXrsNrMcuDZllcEXxctWlPGh3nY/640?wx_fmt=png&from=appmsg)

数据包也能正常读取

![](https://mmbiz.qpic.cn/mmbiz_png/6fnkZFq8xeYwlQpQ8TuNfcIeRoSwu8fnJMjDxQAznXGkugutW0JTvknfcS4MVS06Qv4FKEX6Qfuy7Gz3phuGBVksPkhYV41f1SJMxRLjQQU/640?wx_fmt=png&from=appmsg)

让它试试刚才的那个sql注入，再加上自己的skill。

![](https://mmbiz.qpic.cn/mmbiz_png/6fnkZFq8xeYQ0rZGvjseM6HWyljnsdHXibeBjLOVia14ibD8KOicvbUYvaicibduuMs1G6dicoicq8fL3GK1wriar7l3giaPZIFbHHk3XXcoC4Nu1axia4/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/6fnkZFq8xeaDnfsKbiareHFWxiaYTl5ia9yTspsxnMlWO5sfl2JibwESH5kgu3ahlA8e4GJ3q0TmvgNhHJS5lsXAc1jcymqy9TJkDkPjkFcdElo/640?wx_fmt=png&from=appmsg)

接着让它开始注入

![](https://mmbiz.qpic.cn/mmbiz_png/6fnkZFq8xeaAIzVwg4oogebFfmsrZJOvYFiajO1JFh8qrT7JCN7fYIYSWqQPTxtiazysNnxicyJLOUf92TLeYhqxNzlsYiaYDSrYgB02iaWjsgZU/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/6fnkZFq8xebsnImwJnU011YqbO7nOu9xYWJ8r7s2Ckf0nmBpemNqsvYuQCZAYrCblfy6ZsvcyRb4UaXbVn7jxzHLKGf71WqMueMBqDP8iakU/640?wx_fmt=png&from=appmsg)

最后成功注入出数据库名，原来是=被过滤了，所以导致刚才的1=1，1=2恒为真

![](https://mmbiz.qpic.cn/sz_mmbiz_png/6fnkZFq8xeY0HqObSw4bFt79GZ794hNKuricQwEic23xkiarUUHLmquFLQSvzugOkZibWkaXIYET521sLnGicnaw0F6VjaEZGo3MvicJ7UIgLqhHI/640?wx_fmt=png&from=appmsg)

这个网站还有swagger接口泄露，让它访问swagger接口，根据burp历史数据包来构造参数试试

![](https://mmbiz.qpic.cn/sz_mmbiz_png/6fnkZFq8xeaU6l1ee9CKt14pQd2v9bibY6WqO3W6uAuPxh1QIu4KqavCr62p0rW3ZSic7nib88iaqiaSkMur1zSaPDQXtx8icneAOpIBiaQUxicPcOE/640?wx_fmt=png&from=appmsg)

效果也是不错的

![](https://mmbiz.qpic.cn/sz_mmbiz_png/6fnkZFq8xeZzmtty23knaM4bwbafmxbsPBXpibuJgZQmE5Iiaku5RhEAckCy9NBqH5JMsKPyPPQb8z9NOpFbicZpUfmD9FaliadBgvccpVF4FSE/640?wx_fmt=png&from=appmsg)

---

内部CTF课程上线，总课程30+小时，火热报名中！

点击跳转⬇️

[![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/niasx7fyic9COGdPzfuwpDmqhCazI2icnGkWNsdOAS83HB1uibYosTYfriaibkcSlkWR0dicjZ4e8k64BJiaXdUNEnWgVhK6h70ewMQROibFHgfb9pqc/640?wx_fmt=png&from=appmsg&tp=wxpic&wxfrom=5&wx_lazy=1#imgIndex=15)](https://mp.weixin.qq.com/s?__biz=MzkzMzE5OTQzMA==&mid=2247490264&idx=1&sn=2b7c98ba64b1d79946dcb8e6644ee741&scene=21#wechat_redirect)

---

内部帮会简介

《安全渗透感知》是FreeBuf知识大陆的重量级帮会，帮会致力于漏洞POC/EXP、红队攻防实战，是系统化从基础入门到实战漏洞挖掘的教程社区，包含团队自整的挖掘注意点和案例，还包含分享的渗透经验、SRC漏洞案例、代码审计、挖洞思路等高价值资源。

内容框架（持续新增中）

![图片](https://mmbiz.qpic.cn/mmbiz_png/niasx7fyic9CMSSZhDGfvZc4bj1RfTy0brHiaqCQ9SNmWkwPPK049MibiajUwxNZib1fMibV5ibcxtDdibRzvPvApuhNzLQhSLZpes5Z3j0LtaaWPoFw/640?from=appmsg&tp=wxpic&wxfrom=5&wx_lazy=1#imgIndex=16)

目前已有「630+」小伙伴加入了帮会

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/niasx7fyic9CNYjFsibugJ3icU3qmswbwicibxiaDe1895jCibfR6sK2qqVaunJGPxJjNfMwDhzb3XLGpKkTSHvQBribdibj7QtIJe3dTxMDlSkticax9o/640?from=appmsg&tp=wxpic&wxfrom=5&wx_lazy=1#imgIndex=17)

加入方式目前帮会成员630+人，永久会员优惠后只需69.9元。

随着人数的增加及资源的积累，之后永久会员将涨价至99元。

有意向的师傅们可以扫码加入我们，共同进步。

如何加入帮会？→ 安卓/苹果用户可扫码使用优惠券↓↓

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/niasx7fyic9COfAib7mAjiaRIWdLqlqllrWQdmEoE9ANFyh4s0AqhQhcz65iaqa4xgjYW1XM6AB4Q9rYSSubO9fcwcliaxHulE3GViaBw9M2LCHKZ0/640?from=appmsg&tp=wxpic&wxfrom=5&wx_lazy=1#imgIndex=18)

→ PC端用户可复制此链接到浏览器↓↓

https://wiki.freebuf.com/societyDetail?society\_id=184

已加入帮会的小伙伴

可以加帮主进帮会内部交流群

请备注：帮会

![图片](https://mmbiz.qpic.cn/mmbiz_jpg/niasx7fyic9CO1tQCbVMRK5624szvMVs8ZWwjGIyAPQeSftlTDJaAmA13HXUiciciatHgPf0NcOguIcXP7tQhqohxN1lhjYcOwpKZVEtVHFBflIw/640?from=appmsg&tp=wxpic&wxfrom=5&wx_lazy=1#imgIndex=19)

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/EXTCGqBpVJQiaZKk16p8ASnxuOUZiaJWeVzm5jndulrhBy63D46ic8H6lq8tpJfXTCNEhUeq9LckNiaObB9Auiaicp2Q/0?wx_fmt=png)

C4安全

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/EXTCGqBpVJQiaZKk16p8ASnxuOUZiaJWeVzm5jndulrhBy63D46ic8H6lq8tpJfXTCNEhUeq9LckNiaObB9Auiaicp2Q/0?wx_fmt=png)

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