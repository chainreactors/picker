---
title: 认输
url: https://h4ck.org.cn/2025/05/20784
source: obaby@mars
date: 2025-05-22
fetch_date: 2025-10-06T22:27:17.737152
---

# 认输

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

[个人日记『Diary』](https://h4ck.org.cn/cats/dddd/grrj)

# 认输

2025年5月21日
[33 条评论](https://h4ck.org.cn/2025/05/20784#comments)

[![](https://h4ck.org.cn/wp-content/uploads/2025/05/WechatIMG1554.jpg)](https://h4ck.org.cn/wp-content/uploads/2025/05/WechatIMG1554.jpg)

这几天在调整一个项目的 mqtt 上报的数据时发现一个诡异的问题，那就是同样的服务器，如果使用 mqtt 客户端连上去一切都是正常的，上报频率也确实是看起来跟客户说的一样一分钟 1 条。

然而，在代码里获取的时候就完全变了，有时候看起来一切正常有时候时间就变得异常不稳定。

```
[*] Time: 2025-05-20 15:09:13
[*] Time interval from last message: 240.51 seconds
[*] Topic: canteen/third/second/valve1
[*] Message: {"switch1":1,"switch2":0,"switch3":0,"switch4":0}
[A] Updated device status: canteen/third/second/valve1_switch1
[W] Device not found: canteen/third/second/valve1_switch3
```

甚至有时候时间能到十来分钟都没数据。这个就很诡异了。

输出错误日志会发现系统在一直尝试断线重连：

[![](https://h4ck.org.cn/wp-content/uploads/2025/05/WechatIMG3871111.png)](https://h4ck.org.cn/wp-content/uploads/2025/05/WechatIMG3871111.png)

但是在不断重连之后又能间歇性 的收到消息，这就很神奇了。7: “Connection refused – not authorized (no credentials needed)”

在尝试调整 qos 以及优化连接代码之后，依然无果。没有任何的改进，不得已只能放弃原有的链接库paho，转投更先进的gmqtt。

### gmqtt: Python async MQTT client implementation.

https://pypi.org/project/gmqtt/

看示例代码也比较简洁：

```
import asyncio
import os
import signal
import time

from gmqtt import Client as MQTTClient

# gmqtt also compatibility with uvloop
import uvloop
asyncio.set_event_loop_policy(uvloop.EventLoopPolicy())

STOP = asyncio.Event()

def on_connect(client, flags, rc, properties):
    print('Connected')
    client.subscribe('TEST/#', qos=0)

def on_message(client, topic, payload, qos, properties):
    print('RECV MSG:', payload)

def on_disconnect(client, packet, exc=None):
    print('Disconnected')

def on_subscribe(client, mid, qos, properties):
    print('SUBSCRIBED')

def ask_exit(*args):
    STOP.set()

async def main(broker_host, token):
    client = MQTTClient("client-id")

    client.on_connect = on_connect
    client.on_message = on_message
    client.on_disconnect = on_disconnect
    client.on_subscribe = on_subscribe

    client.set_auth_credentials(token, None)
    await client.connect(broker_host)

    client.publish('TEST/TIME', str(time.time()), qos=1)

    await STOP.wait()
    await client.disconnect()

if __name__ == '__main__':
    loop = asyncio.get_event_loop()

    host = 'mqtt.flespi.io'
    token = os.environ.get('FLESPI_TOKEN')

    loop.add_signal_handler(signal.SIGINT, ask_exit)
    loop.add_signal_handler(signal.SIGTERM, ask_exit)

    loop.run_until_complete(main(host, token))
```

[![](https://h4ck.org.cn/wp-content/uploads/2025/05/Jietu20250521-100822.jpg)](https://h4ck.org.cn/wp-content/uploads/2025/05/Jietu20250521-100822.jpg)

其实，各种方式或者库对我来说没什么特殊的喜好，只要能解决自己的问题就好，作为一个实用主义住，该认输就认输，毕竟要解决这个异常问题可能得从框架本身入手了，这也非我所愿。有这点时间干点别的不好吗？

白天又又又又收到了整改通知，现在看到这种整改通知，的确是有点沮丧，改不完，根本改不完。

[![](https://h4ck.org.cn/wp-content/uploads/2025/05/Jietu20250521-100937.jpg)](https://h4ck.org.cn/wp-content/uploads/2025/05/Jietu20250521-100937.jpg)

不过这次反馈的是功能问题，该修复还是要修复的。不过白天也确实没时间了，晚上还要带宝子去石老人看沙滩音乐会。

下班还是果断先带宝子出去玩啊：

[![](https://h4ck.org.cn/wp-content/uploads/2025/05/15461747792211_.pic_-1024x768.jpg "15461747792211_.pic")](https://h4ck.org.cn/wp-content/uploads/2025/05/15461747792211_.pic_.jpg "15461747792211_.pic")

[![](https://h4ck.org.cn/wp-content/uploads/2025/05/15471747792212_.pic_-1024x768.jpg "15471747792212_.pic")](https://h4ck.org.cn/wp-content/uploads/2025/05/15471747792212_.pic_.jpg "15471747792212_.pic")

[![](https://h4ck.org.cn/wp-content/uploads/2025/05/15481747792213_.pic_-1024x768.jpg "15481747792213_.pic")](https://h4ck.org.cn/wp-content/uploads/2025/05/15481747792213_.pic_.jpg "15481747792213_.pic")

[![](https://h4ck.org.cn/wp-content/uploads/2025/05/15491747792214_.pic_-1024x768.jpg "15491747792214_.pic")](https://h4ck.org.cn/wp-content/uploads/2025/05/15491747792214_.pic_.jpg "15491747792214_.pic")

[![](https://h4ck.org.cn/wp-content/uploads/2025/05/15501747792215_.pic_-1024x768.jpg "15501747792215_.pic")](https://h4ck.org.cn/wp-content/uploads/2025/05/15501747792215_.pic_.jpg "15501747792215_.pic")

[![](https://h4ck.org.cn/wp-content/uploads/2025/05/15511747792216_.pic_-1024x768.jpg "15511747792216_.pic")](https://h4ck.org.cn/wp-content/uploads/2025/05/15511747792216_.pic_.jpg "15511747792216_.pic")

[![](https://h4ck.org.cn/wp-content/uploads/2025/05/15521747792217_.pic_-1024x768.jpg "15521747792217_.pic")](https://h4ck.org.cn/wp-content/uploads/2025/05/15521747792217_.pic_.jpg "15521747792217_.pic")

[![](https://h4ck.org.cn/wp-content/uploads/2025/05/15531747792218_.pic_-1024x768.jpg "15531747792218_.pic")](https://h4ck.org.cn/wp-content/uploads/2025/05/15531747792218_.pic_.jpg "15531747792218_.pic")

![](https://h4ck.org.cn/wp-content/uploads/2025/05/15461747792211_.pic_.jpg)![](https://h4ck.org.cn/wp-content/uploads/2025/05/15471747792212_.pic_.jpg)![](https://h4ck.org.cn/wp-content/uploads/2025/05/15481747792213_.pic_.jpg)![](https://h4ck.org.cn/wp-content/uploads/2025/05/15491747792214_.pic_.jpg)![](https://h4ck.org.cn/wp-content/uploads/2025/05/15501747792215_.pic_.jpg)![](https://h4ck.org.cn/wp-content/uploads/2025/05/15511747792216_.pic_.jpg)![](https://h4ck.org.cn/wp-content/uploads/2025/05/15521747792217_.pic_.jpg)![](https://h4ck.org.cn/wp-content/uploads/2025/05/15531747792218_.pic_.jpg)

舞台比较小，毕竟是海尔组织的小型活动，所以也没多大的舞台。据说主要目的还是为了今天的集体婚礼，宝子一直在边上的游乐设施玩，等玩够了却发现连舞台边都看不到，什么也看不着，好在无人机表演倒是不需要往前挤。

早上送宝子上学，宝子嚷嚷着要听收音机的 青紫堂的广告，非得听那个念电话号码的 57813377。不得不说，这个广告没白听，我都记住了。

学校外面看到有卖小樱桃的，问了下十三一斤，回家的路上买了点，说要两三节，结果一下子来了四斤多。

到家之后打开袋子发现是上当了，篮子底下的基本都是坏的。也就是说给我装的就没几个好的，连表面一层好的想找也找不出来了。

对象说，你洗洗看看吧，不行就不要了。

那和樱桃放到水盆里，倒上水，挑的时候的确是绝望了，不单软软的，还有很多烂的，挑了几个长了一下，也不好吃。最后放弃了，连袋子一起扔到了垃圾桶里。

这的确是上了老当了，被骗了，只能认输。

☆版权☆

\* 网站名称：**[obaby@mars](https://h4ck.org.cn/)**
\* 网址：<https://h4ck.org.cn/>
\* 个性：<https://oba.by/>
\* 本文标题： [《认输》](https://h4ck.org.cn/2025/05/20784)
\* 本文链接：<https://h4ck.org.cn/2025/05/20784>
\* 短链接：<https://oba.by/?p=20784>
\* 转载文章请标明文章来源，原文标题以及原文链接。请遵从 [《署名-非商业性使用-相同方式共享 2.5 中国大陆 (CC BY-NC-SA 2.5 CN) 》](https://creativecommons.org/licenses/by-nc-sa/2.5/cn/)许可协议。

---

[上当](https://h4ck.org.cn/tags/%E4%B8%8A%E5%BD%93)[樱桃](https://h4ck.org.cn/tags/%E6%A8%B1%E6%A1%83)

[Previous Post](https://h4ck.org.cn/2025/05/20800)
[Next Post](https://h4ck.org.cn/2025/05/20774)

![obaby](https://gg.lang.bi/avatar/d6ebc088df916bcc9e8b94a09f9b0f604e57be54b04bd520c6db2492740fc563?s=90&d=identicon&r=r)

#### obaby

爱好广泛的火星小妖精，有问题欢迎留言交流啊~(✪ω✪)
爬虫类工具请先点击这个链接查看用法https://oba.by/?p=12240
闺蜜圈APP下载 https://guimiquan.cn

#### 猜你喜欢：

2024年7月23日

#### [夏日游记 — episode 2 多伦湖国家湿地公园](https://h4ck.org.cn/2024/07/17651)

2023年7月28日

#### [北京欢迎你（2）–展演](https://h4ck.org.cn/2023/07/12679)

2025年8月8日

#### [挣得太少](https://h4ck.org.cn/2025/08/21207)

### 33 comments

1. ![](https://gg.lang.bi/avatar/d838166f05390e17979f10c8e0fcc3b1d719369e6450e9eb30f218d8579263ee?s=64&d=identicon&r=r) **[dujun](https://dujun.io/)**说道：

   [2025年5月21日 10:55](https://h4ck.org.cn/2025/05/20784#comment-126587)

   ![](https://badgen.net/badge/用户/已认证/CCFF33?icon=rss) ![](https://badgen.net/badge/友链/集美们/blue?icon=chrome) ![Level 7](https://badgen.net/badge/亲密度/Level 7/pink?icon=codebeat)

   ![Google Chrome 136](https://h4ck.org.cn/wp-content/plugins/wp-useragent/img/16/net/chrome.png "Google Chrome 136") Google Chrome 136 ![Mac OS X 1...