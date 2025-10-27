---
title: InfluxDB 诡异的时间窗口对齐(是我太傻逼)
url: https://h4ck.org.cn/2025/05/20827
source: obaby@mars
date: 2025-05-28
fetch_date: 2025-10-06T22:25:43.520448
---

# InfluxDB 诡异的时间窗口对齐(是我太傻逼)

[![obaby@mars](/wp-content/uploads/2023/08/logo-pink-small.png)](https://h4ck.org.cn)

Artificial Intelligence / Reverse Engineering / Internet of Things / Full Stack Developer

* [※说说/Talk※](https://h4ck.org.cn/talk)
* [※留言/Msg※](https://h4ck.org.cn/guestbook)
* [※归档/File※](https://h4ck.org.cn/myarchive)
* [※资源/Res※](https://h4ck.org.cn/res-page)
* [※我是谁/Me※](https://h4ck.org.cn/whoami)
* [※集美们/Besties※](https://h4ck.org.cn/besties)

 [Menu](#mobilemenu)

* [※说说/Talk※](https://h4ck.org.cn/talk)
* [※留言/Msg※](https://h4ck.org.cn/guestbook)
* [※归档/File※](https://h4ck.org.cn/myarchive)
* [※资源/Res※](https://h4ck.org.cn/res-page)
* [※我是谁/Me※](https://h4ck.org.cn/whoami)
* [※集美们/Besties※](https://h4ck.org.cn/besties)

[后台开发『BackEnd』](https://h4ck.org.cn/cats/cxsj/backend)

# InfluxDB 诡异的时间窗口对齐(是我太傻逼)

2025年5月27日
[30 条评论](https://h4ck.org.cn/2025/05/20827#comments)

[![](https://h4ck.org.cn/wp-content/uploads/2025/05/WechatIMG1571.jpg)](https://h4ck.org.cn/wp-content/uploads/2025/05/WechatIMG1571.jpg)

之前的项目，将部分数据迁移到了InfluxDB v2 数据库。但是，在查询数据的时候发生了一件很诡异的事情，就是使用不同的时间间隔，返回的数据却完全不一样。

感谢 [**ymz316**](https://hollowman.cn/) 帮我找到了 bug，还是数据处理逻辑的问题。我把 ai 给唬住了，他没分析代码，我也没分析代码。**另外一个问题就是上报数据的时间间隔太长了，在时间为 1m 的时候表现出了诡异的行为，根本原因在于 1m 中采样的时候，后面四分钟都没数据（上报频率正好也是 5 分钟）于是采样到了 06 分钟的数据。就成了 01 06 11 的样子，这 tmd 把数据上报频率也给忽略了。**

[![](https://h4ck.org.cn/wp-content/uploads/2025/05/Jietu20250527-145919.jpg)](https://h4ck.org.cn/wp-content/uploads/2025/05/Jietu20250527-145919.jpg)

查询代码如下：

```
def query_data_with_5min_sampling(device_id, start_time, end_time, interval='05m'):
    """
    查询指定设备在时间范围内的数据，支持不同的采样间隔
    :param device_id: 设备ID
    :param start_time: 开始时间
    :param end_time: 结束时间
    :param interval: 采样间隔，支持 '10s', '30s', '01m', '05m', '10m', '30m', '01h'，默认为 '05m'
    :return: 采样后的数据列表
    """
    if interval is None or interval == '':
        interval = '05m'
    if 'm' not in interval and 's' not in interval:
        interval = f"0{interval}m" if int(interval) < 10 else f"{interval}m"
    # 验证时间范围，如果大于一天，强制使用5分钟采样
    if end_time - start_time > timedelta(days=1):
        interval = '05m'
    # 如果小于等于一天且没有指定间隔，使用1分钟采样
    elif interval == '5m' and end_time - start_time <= timedelta(days=1):
        interval = '01m'

    query = f"""
    from(bucket: "ts")
        |> range(start: {datetime_to_tz_time_string(datetime_to_utc_time(start_time))},
                stop: {datetime_to_tz_time_string(datetime_to_utc_time(end_time))})
        |> filter(fn: (r) => r._measurement == "TSSourceData")
        |> filter(fn: (r) => r.device_id_string == "{device_id}")
        |> filter(fn: (r) => r._field =~ /^(temperature|humidity|health_level)$/)
        |> aggregateWindow(
            every: {interval},
            fn: mean,
            createEmpty: false
        )
        |> pivot(rowKey:["_time"], columnKey: ["_field"], valueColumn: "_value")
    """

    tables = client.query_api().query(org="power", query=query)

    lines = []
    for table in tables:
        for record in table.records:
            lines.append(record.values)
    return lines
```

数据支持： ’10s’, ’30s’, ’01m’, ’05m’, ’10m’, ’30m’, ’01h’，默认为 ’05m’

然而，当使用 5 分钟为间隔查询的时候，返回的第一条数据时间竟然是 01 分，不是整点，查询代码：

```
nt = current_time = get_rounded_time_before_time(8)
    # # print(nt)
    lines = query_data_with_5min_sampling('mddt6825050023_1', nt, datetime.now(), interval='5m')
    # print(lines)
    for data_point in lines:
        # print(data_point)
        utc_time = data_point.get('_time')
        tz = pytz.timezone('Asia/Shanghai')
        local_time = utc_time.astimezone(tz)
        print(local_time.strftime('%Y-%m-%d %H:%M:%S'))
```

执行结果：

```
2025-05-27 01:01:00
2025-05-27 01:06:00
2025-05-27 01:11:00
2025-05-27 01:16:00
2025-05-27 01:21:00
2025-05-27 01:26:00
2025-05-27 01:31:00
2025-05-27 01:36:00
2025-05-27 01:41:00
```

然而，当时间改成 15 分钟或者其他时间，就完全是按照整点以及时间间隔来的：

```
lines = query_data_with_5min_sampling('mddt6825050023_1', nt, datetime.now(), interval='15m')
```

执行结果：

```
2025-05-27 01:15:00
2025-05-27 01:30:00
2025-05-27 01:45:00
2025-05-27 02:00:00
2025-05-27 02:15:00
2025-05-27 02:30:00
2025-05-27 02:45:00
2025-05-27 03:00:00
2025-05-27 03:15:00
2025-05-27 03:30:00
2025-05-27 03:45:00
2025-05-27 04:00:00
2025-05-27 04:15:00
2025-05-27 04:30:00
2025-05-27 04:45:00
2025-05-27 05:00:00
2025-05-27 05:15:00
2025-05-27 05:30:00
2025-05-27 05:45:00
2025-05-27 06:00:00
2025-05-27 06:15:00
```

我勒个豆，这么神奇吗？对于这种错误其实猜测可能是返回数据的对齐粒度问题，但是在尝试了使用 offset 等各种参数之后，对于 5 分钟的数据还是返回了 01。直接崩溃，让 cursor 来回改，最后代码改的面目全非了依然没达到效果。只能回滚代码。

这时候鬼使神差想到，这个参数既然是个字符串，那么传个 05m 呢？

```
lines = query_data_with_5min_sampling('mddt6825050023_1', nt, datetime.now(), interval='05m')
```

执行结果：

```
2025-05-27 01:05:00
2025-05-27 01:10:00
2025-05-27 01:15:00
2025-05-27 01:20:00
2025-05-27 01:25:00
2025-05-27 01:30:00
2025-05-27 01:35:00
2025-05-27 01:40:00
2025-05-27 01:45:00
2025-05-27 01:50:00
2025-05-27 01:55:00
2025-05-27 02:00:00
2025-05-27 02:05:00
2025-05-27 02:10:00
2025-05-27 02:15:00
2025-05-27 02:20:00
```

竟然神奇的治愈了，这尼玛不得不说竟然这么神奇。所以最开始的代码其实是修复之后的代码，对于没有 0 开头的分钟进行填充。

问了下 cursor，给出了下面的答复：

[![](https://h4ck.org.cn/wp-content/uploads/2025/05/Jietu20250526-155837-scaled.jpg)](https://h4ck.org.cn/wp-content/uploads/2025/05/Jietu20250526-155837.jpg)

这特性，真是服了，问题是 cursor，为什么不是你发现了告诉我？而是我发现了告诉你呢？

果然是高级 quirk！

☆版权☆

\* 网站名称：**[obaby@mars](https://h4ck.org.cn/)**
\* 网址：<https://h4ck.org.cn/>
\* 个性：<https://oba.by/>
\* 本文标题： [《InfluxDB 诡异的时间窗口对齐(是我太傻逼)》](https://h4ck.org.cn/2025/05/20827)
\* 本文链接：<https://h4ck.org.cn/2025/05/20827>
\* 短链接：<https://oba.by/?p=20827>
\* 转载文章请标明文章来源，原文标题以及原文链接。请遵从 [《署名-非商业性使用-相同方式共享 2.5 中国大陆 (CC BY-NC-SA 2.5 CN) 》](https://creativecommons.org/licenses/by-nc-sa/2.5/cn/)许可协议。

---

[InfluxDB](https://h4ck.org.cn/tags/influxdb)[Python3](https://h4ck.org.cn/tags/python3)[时序数据库](https://h4ck.org.cn/tags/%E6%97%B6%E5%BA%8F%E6%95%B0%E6%8D%AE%E5%BA%93)

[Previous Post](https://h4ck.org.cn/2025/05/20843)
[Next Post](https://h4ck.org.cn/2025/05/20810)

![obaby](https://gg.lang.bi/avatar/d6ebc088df916bcc9e8b94a09f9b0f604e57be54b04bd520c6db2492740fc563?s=90&d=identicon&r=r)

#### obaby

爱好广泛的火星小妖精，有问题欢迎留言交流啊~(✪ω✪)
爬虫类工具请先点击这个链接查看用法https://oba.by/?p=12240
闺蜜圈APP下载 https://guimiquan.cn

#### 猜你喜欢：

2024年4月25日

#### [umami 升级记 — 能跑千万别折腾](https://h4ck.org.cn/2024/04/16742)

2025年9月18日

#### [Baby WP 评论强化拦截插件 — 再战 WP 垃圾评论](https://h4ck.org.cn/2025/09/21609)

2025年3月20日

#### [418 I’m a teapot](https://h4ck.org.cn/2025/03/19860)

### 30 comments

1. ![](https://gg.lang.bi/avatar/19a53855a6616e2ead18670b736d1917a8b5dbe3f22d629e637d9e3f384e451f?s=64&d=identicon&r=r) **[小彦](https://note-star.cn/)**说道：

   [2025年5月27日 09:59](https://h4ck.org.cn/2025/05/20827#comment-126757)

   ![](https://badgen.net/badge/用户/已认证/CCFF33?icon=rss) ![Level 6](https://badgen.net/badge/亲密度/Level 6/red?icon=codebeat)

   ![Microsoft Edge 136](https://h4ck.org.cn/wp-content/plugins/wp-useragent/img/16/net/edge-2.png "Microsoft Edge 136") Microsoft Edge 136 ![Windows 11](https://h4ck.org.cn/wp-content/plugins/wp-useragent/img/16/os/win-6.png "Windows 11") Windows 11 ![cn](https://h4ck.org.cn/wp-content/plugins/wp-useragent/show-useragent/flags_svg/cn.svg "cn")

   05m和5m有这么大区别吗，查死人哦，你们的业务要用到时间间隔采样，像是物联网监测的项目

   [回复](#comment-126757)

   1. ![](https://gg.lang.bi/avatar/d6ebc088df916bcc9e8b94a09f9b0f604e57be54b04bd520c6db2492740fc563?s=64&d=identicon&r=r)

      [2025年5月27日 10:15](https://h4ck.org.cn/2025/05/20827#comment-126758)

      ![公主](https://badgen.net/badge/管理员/小妖精/ff91a4?icon=terminal) ![Queen](https://badgen.net/badge/角色/女王/red?icon=matrix)

      ![Google Chrome 134](https://h4ck.org.cn/wp-content/plugins/wp-useragent/img/16/net/chrome.png "Google Chrome 134") Google Chrome 134 ![Mac OS X 10.15](https://h4ck.org.cn/wp-content/plugins/wp-useragent/img/16/os/mac-3.png "Mac OS X 10.15") Mac OS X 10.15 ![cn](https://h4ck.org.cn/wp-content/plugins/wp-useragent/show-useragent/flags_svg/cn.svg "cn")

      是的，问题是这 tm 谁知道一个 0 引起的查询结果出现的问题。

      [回复](#comment-1...