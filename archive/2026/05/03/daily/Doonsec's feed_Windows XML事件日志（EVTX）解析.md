---
title: Windows XML事件日志（EVTX）解析
url: https://mp.weixin.qq.com/s/O9lk_NbcmxpWaC8YcUoyBg
source: Doonsec's feed
date: 2026-05-03
fetch_date: 2026-05-04T05:31:28.825926
---

# Windows XML事件日志（EVTX）解析

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/FT3A8r9icDymY09avDFrXTRoKlalEnx1FH1h60W22KQZjz34n2MwpfGe8VibOibU1wbw7j6iaX8Q5RypGSpIrM3Z1624KErbVaUKO0mW18UZ7ZU/0?wx_fmt=jpeg)

# Windows XML事件日志（EVTX）解析

原创

凉城
凉城

ListSec

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

# Windows XML 事件日志（EVTX）解析

## Evtx 日志描述

windows 下的 evtx 日志存放位置

```
%SystemRoot%\System32\Winevt\Logs\
```

![image.png](https://mmbiz.qpic.cn/sz_mmbiz_png/FT3A8r9icDynGTunshE2H6LgibUxITRFGx0FxiaxBVr8tMPq0NRbHwmqcYAEbwU1T3dBxuVEt2DNZwogQU1zbXFpvWYy01Y5fyKzNuac5BkPibA/640?wx_fmt=png&from=appmsg)

主要日志包括应用程序、安全、系统日志等，日志默认大小 20484K（20M），超出的部分将覆盖过期的日志。

通过 windows 自带的事件查看器可以查看对应的日志。

![image.png](https://mmbiz.qpic.cn/mmbiz_png/FT3A8r9icDyniaSyOS3LJn4w4nUyNC0saMFSPbRE91nsib1sMpRAp9YeqQ1ttHd9BiaLNKcicGdaXq5xCickUdpLlGuA4Go9kBHJHJibY2cyYMibeqE/640?wx_fmt=png&from=appmsg)

随机点击一个事件 ID 为 4624 的事件，大体内容如下，切换到 xml 视图，可以查看 xml 格式日志。

![image.png](https://mmbiz.qpic.cn/sz_mmbiz_png/FT3A8r9icDykUlgiayLS2JbRnsLt62PwMlRQvQH4icewByt1pHdpG1H3jVoqmuON28RfIyibkGuzs1uYF2AaYnBvr1INf9Q1psfqf9nKj8jwcIE/640?wx_fmt=png&from=appmsg)

## evtx\_dump

通过工具去解析 evtx 的日志

https://github.com/omerbenamram/evtx

下载对应版本：

https://github.com/omerbenamram/evtx/releases

```
evtx_dump <evtx_file> 以xml形式转储

evtx_dump -o json <evtx_file> 以json格式转储

evtx_dump -f <output_file> -o json <input_file> 输出到指定文件
```

配合 fd（https://github.com/cha0ran/fd-zh）使用，便于批量处理

```
fd -e evtx -x evtx_dump -o jsonl #将所有evtx后缀结尾的文件转储到单独的json文件中

fd -e evtx -x evtx_dump '{}' -f '{.}.xml #创建一个与evtx对应的xml文件，然后内容到对应的xml文件中

fd -a -e evtx | xargs -I input sh -c "evtx_dump -o jsonl input | jq --arg path"input"'. + {path: \$path}'"

-e：文件后缀
-a：搜索隐藏文件或目录
xargs -I input sh -c "command"：传入input变量，并将其交给command执行
jq --arg path "input" ‘. + {path: \$path}’：将path变量追加至输出的json文件中
```

### 提取

**从 evtx 文件中提取 EventID**

```
evtx_dump temp_scheduled_task_4698_4699.evtx -o jsonl | jq '.Event.System.EventID'
```

对 EventID 进行排序并统计个数

```
evtx_dump Security.evtx -o jsonl | jq '.Event.System.EventID' | sort | uniq
```

![image.png](https://mmbiz.qpic.cn/sz_mmbiz_png/FT3A8r9icDymykjg6tU0ufPShqC4hhKzNEI8yxJWy8tKD006gwLgtYYpeSxTTyfgxT3nUxcUPTcia06FUbowUTcVlQNX6wRMksREdcibbkmJ1o/640?wx_fmt=png&from=appmsg)

查看事件 ID 可以知道当前日志中大部分日志的状态。如上 5379 表示 Microsoft Windows Defender 防病毒软件有关的事件，该事件记录了 Windows Defender 的相应策略信息，指示 Defender 定期扫描或更新情况。4625 表示登录失败，且只有一条日志，那说明不存在登录暴力破解的尝试。4672 代表管理员登录，同时以管理员的身份进行操作的日志也会记录成 4672，类似于 linux 下面的 sudo，一次 sudo 记录一条日志。

可以和事件 ID 进行一一对比，判断相关事件的影响。

**提取多个字段**

```
evtx_dump temp_scheduled_task_4698_4699.evtx -o jsonl | jq '.Event.System.EventID','.Event.System.Computer'
```

## EvtxECmd

EvtxECmd 是事件记录文件（evtx）的解析工具（windows 下），能够生成符合标准的 CSV、XML 和 json 格式的输出！它还支持自定义映射功能，能够处理被锁定的文件，以及提供更多其他功能！

### 用法

导出内容至 json 文件

```
EvtxECmd.exe -f C:\Users\lca\Desktop\Security.evtx --json .
```

![](https://mmbiz.qpic.cn/mmbiz_png/FT3A8r9icDym5OTFvOaXEAo1axMTNsYhnDcDoWPZkHz7etggr2TMhQ1qUyUJ2Fhy86hG124Uup4X50CFVDiaRbNKgUXsEsqAOpyL8HGpDyRFY/640?wx_fmt=png&from=appmsg)

如上图所示，对 Security.evtx 进行解析，输出的末尾还统计了事件 ID 的数量。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/FT3A8r9icDyn1XTwBucsFRYZxdHSsO9Ue7ia0HM7mOxcNnodCmUMRZEhUkO5ddibICO5bVV8fftWKC5JXukrhPXBs6H9utVXzAUqVazEnwUVdc/640?wx_fmt=png&from=appmsg)

在当前目录下生成了 json 文件，接下来就可以通过 jq 工具去解析 json 文件的内容了。

```
cat 20240813012115_EvtxECmd_Output.json | jq . -c | jq '. | select(.EventId==4624)'

# . -c : . 是一个jq过滤器，表示输出输入的全部内容。-c将内容压缩为紧凑的 JSON 字符串格式。
# . | : . 代表前面传入的整个 JSON 对象
```

提取指定字段，如下，假如从 4624 的日志中提取 MapDescription 字段的内容

```
cat 20240813012115_EvtxECmd_Output.json | jq . -c | jq '. | select(.EventId==4624) | "\(.MapDescription)"'

# \(.MapDescription)：表示从筛选出的JSON对象中提取MapDescription字段的值，并将其作为字符串输出。
```

像这种 jq 过滤更多的是熟悉 jq 的语法。

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/GPsT7FaPGw5uQIpWOXmtw3tpIcv79XQaeOzFgThibkpMw28zSicDFgOumVJfHnfM533DBb7ibM1KnqkShD3Wtt3BA/0?wx_fmt=png)

ListSec

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/GPsT7FaPGw5uQIpWOXmtw3tpIcv79XQaeOzFgThibkpMw28zSicDFgOumVJfHnfM533DBb7ibM1KnqkShD3Wtt3BA/0?wx_fmt=png)

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