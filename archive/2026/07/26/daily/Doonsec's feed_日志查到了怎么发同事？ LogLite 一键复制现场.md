---
title: 日志查到了怎么发同事？ LogLite 一键复制现场
url: https://mp.weixin.qq.com/s/LypgGOdM_M4TflnaDu-SNw
source: Doonsec's feed
date: 2026-07-26
fetch_date: 2026-07-27T05:40:32.269230
---

# 日志查到了怎么发同事？ LogLite 一键复制现场

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/yJLbez93fl9f2WFibNic862JtPWXnq17WEz3ibambLUpf68fib1dK4JumFibA9NJvy9WEMG1lsV2B5YoB7go8oWLhbd5UicaxLUjToc0pFMzf1Eh8/0?wx_fmt=jpeg)

# 日志查到了怎么发同事？ LogLite 一键复制现场

宝十八
宝十八

网络安全老宋

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

**导语：** 你好，我是网络安全老宋。安全攻防干货准时送达！

查日志不难，难的是把"现场"完整地发给同事。LogLite 这次补的小功能，正好掐在排查的最后一步。

![](https://mmbiz.qpic.cn/mmbiz_png/yJLbez93flibDqAicW1icf8mxLGlpXKfklXYCQw7g4kW6QoZ2uSibJSiaq02qicKb7LG4UgdYIDNdsjhV8LSIPl5IEn7YAG6ibQDibTUD7bZLUcZNX0/640?wx_fmt=png&from=appmsg)

你肯定遇到过这种场面。

线上报了个错，你 SSH 上去 tail 了半天，终于在 app.log 第 1287 行看到了 `payment failed: invalid signature`。问题定位到了，下一步不是自己闷头查，而是要把这段甩给后端同事，或者贴进工单里："你看一下这个订单为什么失败？大概在这几行。"

⚠️ **痛点：**发日志这件事，比想象中别扭。手动框选右侧日志，容易少复制一行上下文；只复制命中的那一行，别人看不出前面请求进没进来、后面有没有回滚；直接截图最直观，可后面人家想搜 `request_id`、想复制 trace id，又没辙。

LogLite 的作者枫枫知道，在把搜索定位功能做完之后，给自己（也给所有运维）补了这个最容易被忽略、却天天要用的一键动作：**把当前日志片段、搜索命中上下文、多文件搜索结果，一键复制成可以直接发出去的纯文本。**

目录 · Table of Contents

00为什么"发日志"这么别扭

01LogLite 是什么：本地+远程的日志查看器

02复制片段：把"现场"带上下文带走

03三个位置，只复制最像问题的那段

04为什么是复制，不是截图也不是导出

05和 lnav / GoAccess 比，它赢在哪

|  |  |
| --- | --- |
| 00 | 为什么"发日志"这么别扭 |

很多日志工具都会高亮 `ERROR`。但真排查的时候，只看这一行经常不够。

你看到 `payment failed: invalid signature`，下一步通常要看：前面请求参数进没进来、有没有同一个 trace id、是不是刚重试过、后面有没有补偿或者回滚。这些上下文丢一节，同事就没法接手。

LogLite 之前做搜索定位时，就没有只返回命中行，而是把命中行前后几行一起带回来。这次复制功能，是沿同一个思路往下走——把"上下文"当作一等公民。

![](https://mmbiz.qpic.cn/mmbiz_png/yJLbez93fl82CKTwnYxXkzsruB4IOtTXaQIr9tjqiaQRgF6udfbkmibKibFwpaoIh16Foau2LVSouGiaUqjO21CJdVmHYjIZY5SYA635f2IjpC8/640?wx_fmt=png&from=appmsg)

|  |  |
| --- | --- |
| 01 | LogLite 是什么：本地+远程的日志查看器 |

LogLite 是开发者枫枫知道做的一个**本地日志查看器**，用 Wails 3 打包成桌面应用（Go 写后端、前端做界面），主要用来更方便地查看、筛选和定位本地日志内容，适合开发调试和日常排查。

ℹ️ **提示：**Wails 是个把 Go 和前端（Vue/React 之类）捆成一个桌面程序的框架，打出来的包跟 Electron 不同，后端是原生 Go，体积小、启动快。

它现在已经不只是一个"本地 tail 窗口"了：

• 能看本地日志文件，支持搜索定位；

• 能连远程 Agent，把服务器上的日志拉到本地界面里看；

• 这一版又补上了"把现场复制出去"的动作。

换句话说，从"看到"到"发出去"，它把排查的最后一公里也接上了。

|  |  |
| --- | --- |
| 02 | 复制片段：把"现场"带上下文带走 |

![](https://mmbiz.qpic.cn/mmbiz_png/yJLbez93fl8uDAUAmHXoudibo7RVia9ibC3NO3rxZKMwJJ4ol9l4lZsCdUicgegbhds9khgOibKYbVKDEaGGpbKBfCw01d4lDoOoPdiamMn5FnWqI/640?wx_fmt=png&from=appmsg)

点一下复制，出来的不是孤零零的一行 error，而是一段自带元数据的纯文本：

⏺ 复制片段 · LogLite 搜索命中上下文

```
# LogLite 搜索命中上下文来源：远程服务器：test  文件：app.log  关键词：error  命中行：12871285 | 2026-06-11 10:21:31 INFO  request_id=req-7f3c start /api/pay 1286 | 2026-06-11 10:21:31 WARN  request_id=req-7f3c retry payment gateway 1287 | 2026-06-11 10:21:32 ERROR request_id=req-7f3c payment failed: invalid signature 1288 | 2026-06-11 10:21:32 INFO  request_id=req-7f3c rollback order status 1289 | 2026-06-11 10:21:32 INFO  request_id=req-7f3c response 500
```

这段文本直接发到微信、飞书、工单系统都行。别人拿到以后，还能继续复制里面的 `request_id` 或关键字段去查。

注意它带了什么：来源（本地还是远程）、文件名、搜索关键词、命中行号、前后上下文。这几样东西一凑齐，同事不用再问你"这是哪个文件、哪一行"。

|  |  |
| --- | --- |
| 03 | 三个位置，只复制最像问题的那段 |

作者这次没搞一个庞大的"导出中心"——日志工具的操作最好别绕。复制按钮只放在三个地方：

| 位置 | 按钮 | 适用场景 |
| --- | --- | --- |
| 打开日志尾部 | 复制片段 | 正 tail，看到最近一段异常，先把这一屏带走 |
| 搜索当前文件 | 复制现场 | 搜到 error / 订单号 / trace id，点一下命中结果再复制 |
| 多文件搜索 | 复制（每段旁） | app.log / worker.log / gateway.log 都有同一 trace id，只挑最像问题现场的那段 |

💡 **克制：**作者故意没做"复制全部搜索结果"。结果一多，复制出来就是另一片日志海。排查时真正有用的往往是某一个片段，不是几百条命中堆在一起。

|  |  |
| --- | --- |
| 04 | 为什么是复制，不是截图也不是导出 |

一开始作者也纠结过两个方向。

截图对"证明我看到了什么"很直观，但它不好搜索、也不好复制里面的 trace id、订单号、接口路径。

导出文件（.txt 或 .md）也有用，但动作重一点：要选路径、要命名、要再找到文件发出去，对临时排查来说过了。

所以这一版先做复制。它解决的是最短路径：

⏺ 最短路径

```
搜到 → 点中 → 复制 → 发出去
```

等后面真有需要，再考虑导出 Markdown 报告——比如一次事故里复制多个片段，最后生成一个排查记录，那个方向比现在就做文件导出更自然。

⚠️ **技术细节：**复制逻辑主要在前端，因为搜索结果本来就是结构化数据（lineNumber / matchLines / lines），要做的只是把这些整理成可读文本，行号固定宽度左对齐，右边保留原始内容。真正写剪贴板时还加了个兜底：优先用 navigator.clipboard.writeText，不行就退回 textarea + execCommand('copy')——WebView 和权限环境各不相同，这个兜底不优雅但稳。另外 Wails 项目里前端构建产物 hash 变化后，偶尔 go test ./... 会报 embed 旧资源找不到，清一下缓存（go clean -testcache）重跑就正常，这点作者也踩过。

|  |  |
| --- | --- |
| 05 | 和 lnav / GoAccess 比，它赢在哪 |

单说"看日志"，终端里早有一票成熟工具。我顺手对比了一下，方便你判断要不要装：

| 工具 | 形态 | 强项 | 短板 | 和 LogLite 的关系 |
| --- | --- | --- | --- | --- |
| lnav | 终端 TUI | 自动识别格式、多文件按时间合并、支持 SQL 查询，取证级强 | 纯终端，没有"一键发给同事" | 深度分析更强，协作弱 |
| GoAccess | 终端/HTML | Web 日志实时可视化，秒出 PV/UV 报表 | 只吃 access 类日志，不擅长通用排查 | 场景窄，各管一段 |
| MultiTail | 终端 TUI | 多文件并行监控、颜色高亮 | 不解析格式、不生成报告 | 实时监控强，事后协作弱 |
| LogLite | 桌面 GUI | 本地+远程、搜索定位、一键复制带上下文的现场 | 深度分析（SQL 之类）不如 lnav | 赢在"最后一公里协作" |

一句话：lnav 们擅长"自己把日志看透"，LogLite 擅长"看完了顺手发给别人"。如果你的日常是**一个人深挖**，lnav 更顺手；如果是**排障要拉群、要塞工单、要对着后端同事解释现场**，LogLite 这一键复制刚好补上那个缺口。

// **老宋说：**这件事的本质，不是"又多了个日志工具"，而是排查日志的最后一米被补上了——过去我们花大力气做搜索、做高亮，却一直容忍"复制出去"这个动作又脏又漏。我的观察是，运维圈对工具的要求正在从"功能强"转向"协作顺"：一个人能看明白不够，得让同事拿到就能接手。LogLite 这种"小但掐在痛点上的功能"，比堆大功能更讨喜。给你的建议很具体：下次排查完准备发同事前，先想清楚要带哪几行上下文，别再手动框选漏一行；远程日志尽量走 Agent 拉到本地看，敏感服务器的密码、密钥别在截图里露脸。

```
https://github.com/fengfengzhidao/LogLite# 运行 cd wails-log-viewer wails3 dev # 构建 wails3 task build # 构建产物：  bin/LogLite.exe
```

防御，不是在演练期间发现攻击，而是在演练开始前就把攻击面收敛到最小。

end

不想错过文章内容？读完请点一下**“在看**![图片](https://mmbiz.qpic.cn/sz_mmbiz_gif/4hgdCZdc8jUczamtqCrTy0y1qxtj2D4su6J9PETsVrjWFibSzm7JzZEXeaJeovtAiaIWVQiclhQuENTqFwTzwUH8w/640?wx_fmt=gif&wxfrom=5&wx_lazy=1&wx_co=1&randomid=g5u115ni&tp=webp#imgIndex=1)******”**，加个**“****关注”**，您的支持是我创作的动力

期待您的一键三连支持（点赞、在看、分享~）

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/sowcUpcXRY07WiafrWPnt0icqSjEOPqweHgqfN5sMGTgMPP5yciaeNiaPx8oJtcS4I6dCcBUL6q4JOY9jNalwkxmZQ/0?wx_fmt=png)

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