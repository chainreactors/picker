---
title: 在Django中使用MQTT的方法
url: https://h4ck.org.cn/2022/11/%e5%9c%a8django%e4%b8%ad%e4%bd%bf%e7%94%a8mqtt%e7%9a%84%e6%96%b9%e6%b3%95/
source: obaby@mars
date: 2022-11-10
fetch_date: 2025-10-03T22:13:04.745986
---

# 在Django中使用MQTT的方法

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

# 在Django中使用MQTT的方法

2022年11月9日
[5 条评论](https://h4ck.org.cn/2022/11/10698#comments)

[![](https://image.h4ck.org.cn/wp-content/uploads/2023/10/108a170cf25538ea5bd667600043cb50-scaled.jpg)](https://image.h4ck.org.cn/wp-content/uploads/2023/10/108a170cf25538ea5bd667600043cb50-scaled.jpg)

文章代码源于这里：https://www.zhuxianfei.com/python/47350.html。

就想偷懒而已，于是直接超了代码。结果运行直接bug了：

```
Traceback (most recent call last):
  File "/Users/zhongming/PycharmProjects/django-vue-admin/backend/application/baby_mqtt.py", line 11, in <module>
    django.setup()
  File "/Users/zhongming/PycharmProjects/django-vue-admin/backend/venv/lib/python3.8/site-packages/django/__init__.py", line 19, in setup
    configure_logging(settings.LOGGING_CONFIG, settings.LOGGING)
  File "/Users/zhongming/PycharmProjects/django-vue-admin/backend/venv/lib/python3.8/site-packages/django/conf/__init__.py", line 82, in __getattr__
    self._setup(name)
  File "/Users/zhongming/PycharmProjects/django-vue-admin/backend/venv/lib/python3.8/site-packages/django/conf/__init__.py", line 63, in _setup
    raise ImproperlyConfigured(
django.core.exceptions.ImproperlyConfigured: Requested setting LOGGING_CONFIG, but settings are not configured. You must either define the environment variable DJANGO_SETTINGS_MODULE or call settings.configure() before accessing settings.
```

这个错误提示就很高端，往上搜了一遍又一遍发现都是下面一样的代码：

```
# 为了能在外部脚本中调用Django ORM模型，必须配置脚本环境变量，将脚本注册到Django的环境变量中
import os, sys
import django
# 第一个参数固定，第二个参数是工程名称.settings
os.environ.setdefault('DJANGO_SETTING_MODULE', 'my_django.settings')
django.setup()

# 引入mqtt包
import paho.mqtt.client as mqtt
# 使用独立线程运行
from threading import Thread
from app名 import models
import time
import json

# 建立mqtt连接
def on_connect(client, userdata, flag, rc):
    print("Connect with the result code " + str(rc))
    client.subscribe('test/#', qos=2)

# 接收、处理mqtt消息
def on_message(client, userdata, msg):
    out = str(msg.payload.decode('utf-8'))
    print(msg.topic)
    print(out)
    out = json.loads(out)

    # 收到消息后执行任务
    if msg.topic == 'test/newdata':
        print(out)

# mqtt客户端启动函数
def mqttfunction():
    global client
    # 使用loop_start 可以避免阻塞Django进程，使用loop_forever()可能会阻塞系统进程
    # client.loop_start()
    # client.loop_forever() 有掉线重连功能
    client.loop_forever(retry_first_connection=True)

client = mqtt.Client(client_id="test", clean_session=False)

# 启动函数
def mqtt_run():
    client.on_connect = on_connect
    client.on_message = on_message
    # 绑定 MQTT <a href="http://www.zhuxianfei.com/server/" target="_blank" class="infotextkey">服务器</a>地址
    broker = '192.168.1.88'
    # MQTT服务器的端口号
    client.connect(broker, 1883, 62)
    client.username_pw_set('user', 'user')
    client.reconnect_delay_set(min_delay=1, max_delay=2000)
    # 启动
    mqttthread = Thread(target=mqttfunction)
    mqttthread.start()

# 启动 MQTT
# mqtt_run()

if __name__ == "__main__":
    mqtt_run()
```

一个字母都不带改的，当然这些抄文章的人肯定自己没试过。因为上面的代码就跑不动，那一行有问题呢？当然就是下面这一行了：

```
os.environ.setdefault('DJANGO_SETTING_MODULE', 'my_django.settings')
```

上面的代码应该是：

```
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'application.settings')
```

对比一下发现区别了吗？少了个S对不对？这个陷阱真的是太牛逼了，不是语法问题，所以运行的之后不会报语法错误，直接报的django的错误。想排查都不好排查。直到所又从google的代码抄了一份，发现长度不一致，才发现少了个S。不知道是不是作者有意为之，这就很高端。其他的就没什么问题了，加上S就可以正常运行了。

☆版权☆

\* 网站名称：**[obaby@mars](https://h4ck.org.cn/)**
\* 网址：<https://h4ck.org.cn/>
\* 个性：<https://oba.by/>
\* 本文标题： [《在Django中使用MQTT的方法》](https://h4ck.org.cn/2022/11/10698)
\* 本文链接：<https://h4ck.org.cn/2022/11/10698>
\* 短链接：<https://oba.by/?p=10698>
\* 转载文章请标明文章来源，原文标题以及原文链接。请遵从 [《署名-非商业性使用-相同方式共享 2.5 中国大陆 (CC BY-NC-SA 2.5 CN) 》](https://creativecommons.org/licenses/by-nc-sa/2.5/cn/)许可协议。

---

[Django](https://h4ck.org.cn/tags/django)[mqtt](https://h4ck.org.cn/tags/mqtt)[paho-mqtt](https://h4ck.org.cn/tags/paho-mqtt)[Python3](https://h4ck.org.cn/tags/python3)

[Previous Post](https://h4ck.org.cn/2022/11/10701)
[Next Post](https://h4ck.org.cn/2022/11/10691)

![obaby](https://gg.lang.bi/avatar/d6ebc088df916bcc9e8b94a09f9b0f604e57be54b04bd520c6db2492740fc563?s=90&d=identicon&r=r)

#### obaby

爱好广泛的火星小妖精，有问题欢迎留言交流啊~(✪ω✪)
爬虫类工具请先点击这个链接查看用法https://oba.by/?p=12240
闺蜜圈APP下载 https://guimiquan.cn

#### 猜你喜欢：

2025年2月16日

#### [微博图片拯救 — 妈妈再也不用担心图片被夹看不到啦！🤓](https://h4ck.org.cn/2025/02/19296)

2024年1月26日

#### [django rest framework 多语言支持](https://h4ck.org.cn/2024/01/15185)

2021年10月21日

#### [Freeswitch sip Push notifications](https://h4ck.org.cn/2021/10/9190)

### 5 comments

1. ![](https://gg.lang.bi/avatar/d838166f05390e17979f10c8e0fcc3b1d719369e6450e9eb30f218d8579263ee?s=64&d=identicon&r=r) **[dujun](https://dujun.io)**说道：

   [2022年11月9日 15:27](https://h4ck.org.cn/2022/11/10698#comment-88738)

   ![](https://badgen.net/badge/用户/已认证/CCFF33?icon=rss) ![](https://badgen.net/badge/友链/集美们/blue?icon=chrome) ![Level 7](https://badgen.net/badge/亲密度/Level 7/pink?icon=codebeat)

   ![Google Chrome 107](https://h4ck.org.cn/wp-content/plugins/wp-useragent/img/16/net/chrome.png "Google Chrome 107") Google Chrome 107 ![Mac OS X 10.15](https://h4ck.org.cn/wp-content/plugins/wp-useragent/img/16/os/mac-3.png "Mac OS X 10.15") Mac OS X 10.15 ![cn](https://h4ck.org.cn/wp-content/plugins/wp-useragent/show-useragent/flags_svg/cn.svg "cn")

   抄文章的太多了，很多自己不验证的

   [回复](#comment-88738)

   1. ![](https://gg.lang.bi/avatar/d6ebc088df916bcc9e8b94a09f9b0f604e57be54b04bd520c6db2492740fc563?s=64&d=identicon&r=r)

      [2022年11月9日 15:28](https://h4ck.org.cn/2022/11/10698#comment-88739)

      ![公主](https://badgen.net/badge/管理员/小妖精/ff91a4?icon=terminal) ![Queen](https://badgen.net/badge/角色/女王/red?icon=matrix)

      ![Google Chrome 102](https://h4ck.org.cn/wp-content/plugins/wp-useragent/img/16/net/chrome.png "Google Chrome 102") Google Chrome 102 ![Mac OS X 10.15](https://h4ck.org.cn/wp-content/plugins/wp-useragent/img/16/os/mac-3.png "Mac OS X 10.15") Mac OS X 10.15 ![cn](https://h4ck.org.cn/wp-content/plugins/wp-useragent/show-useragent/flags_svg/cn.svg "cn")

      填下文章一大抄，抄完了也没人验证。不过，这个坑确实留得不错。

      [回复](#comment-88739)
2. ![](https://gg.lang.bi/avatar/1c03767b0691f80231895255661bcf42eceab95dc8b493ee80c835b07f577f49?s=64&d=identicon&r=r)

   [2022年11月9日 21:05](https://h4ck.org.cn/2022/11/10698#comment-88749)

   ![](https://badgen.net/badge/友链/集美们/blue?icon=chrome) ![Level 6](https://badgen.net/badge/亲密度/Level 6/red?icon=codebeat)

   ![Microsoft Edge 107](https://h4ck.org.cn/wp-content/plugins/wp-useragent/img/16/net/edge-2.png "Microsoft Edge 107") Microsoft Edge 107 ![Windows 10](https://h4ck.org.cn/wp-content/plugins/wp-useragent/img/16/os/win-6.png "Windows 10") Windows 10 ![cn](https://h4ck.org.cn/wp-content/plugins/wp-useragent/show-useragent/flags_svg/cn.svg "cn")

   文章头的配图真是……还好我划得快！

   [回复](#comment-88749)

   1. ![](https://gg.lang.bi/avatar/d6ebc088df916bcc9e8b94a09f9b0f604e57be54b04bd520c6db2492740fc563?s=64&d=identicon&r=r)

      [2022年11月9日 21:16](https://h4ck.org.cn/2022/11/10698#comment-88751)

      ![公主](https://badgen.net/badge/管理员/小妖精/ff91a4?icon=terminal) ![Queen](https://badgen.net/badge/角色/女王/red?icon=matrix)

      ![Google Chrome 104](https://h4ck.org.cn/wp-content/plugins/wp-useragent/img/16/net/chrome.png "Google Chrome 104") Google Chrome 104 ![Windows 10...