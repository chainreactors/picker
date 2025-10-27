---
title: 深入User-Agent的生成、校验以及安全风险
url: https://saucer-man.com/information_security/982.html
source: SAUCERMAN
date: 2022-11-19
fetch_date: 2025-10-03T23:12:46.393717
---

# 深入User-Agent的生成、校验以及安全风险

* [Home](https://saucer-man.com/)
* [Archives](https://saucer-man.com/archives.html)
* [About](https://saucer-man.com/about.html)
* [Github](https://github.com/saucer-man)

Previous post
Next post
Back to top
Share post

* [1. UA生成](#cl-1)* [1.1 android端](#cl-2)
  * [1.2 pc端](#cl-3)
  * [1.3 随机UA实现](#cl-4)
* [2. UA解析](#cl-5)
* [3. 安全威胁](#cl-6)* [3.1 web漏洞](#cl-7)
  * [3.2 在风控对抗中的妙用](#cl-8)

# 深入User-Agent的生成、校验以及安全风险

2022-11-18

10529

[信息安全](https://saucer-man.com/category/information_security/)

> 文章最后更新时间为：2025年02月26日 23:26:16

User-Agent是http协议中请求头的一个字段，在设计之初，其作用是用来向服务端表明客户端的版本，方便服务端根据不同的客户端，对响应内容作出适当的调整。对于大部分人来说，UA并不陌生，稍微大点公司通常会对UA进行数据分析，从而刻画用户画像，更好的调整业务增长方向。

对于做安全和爬虫的同学，经常需要伪造UA，避免特征聚集，绕过风控策略。下面就来分析下从攻击者角度，如何生成真实的UA，从防守者角度，如何对UA进行正确的解析。如有错误，欢迎指正。

## 1. UA生成

UA的生成规则其实是没有一个统一的标准的，换言之，你可以随便生成UA，任意字符串都可以，但是为了抵抗风控策略，我们需要伪装真人流量，那么就需要了解常见的UA生成方式。

### 1.1 android端

下面来看 android 端小米 8 利用原生 webview 生成的UA

```
Mozilla/5.0 (Linux; Android 10; MI 8 Build/QKQ1.190828.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/83.0.4103.101 Mobile Safari/537.36

# 生成规则
mWebView = findViewById(R.id.web_view);
WebSettings settings = mWebView.getSettings();
String userAgent = settings.getUserAgentString();
```

其中里面包含了三部分信息：

* 浏览器：Chrome 83.0.4103.101
* 设备：MI 8 Build/QKQ1.190828.002 Mobile
* 操作系统：Android 10

实际上任何的UA也只包含了这三部分信息，其他的字段通常是固定的，下面简单解释下他们的由来：

* `Mozilla/5.0`: Mozillia 是公益社区（后来开发了 firefox ），开发了Gecko引擎，在浏览器大战时，由于性能吊打 IE ，于是其他浏览器都假装自己是 Mozilla ，并且使用了 Gecko。Mozilla/5.0 是表示该浏览器与 Mozilla 兼容的通用标记，如今几乎所有浏览器都通用。
* `KHTML, like Gecko`: KHTML 是由 KDE 项目开发的浏览器引擎，它是 Konqueror 浏览器的默认引擎，但是 Gecko 引擎的性能更好，于是开发出 Konqueror 浏览器的开发者，在 UA 中加入 like Gecko，来获得更好的响应。
* `AppleWebKit/537.36`: Apple后来开发了Safari浏览器，并基于KHTML开发了WebKit引擎，于是在UA中嵌入此部分。537.36是AppleWebKit的版本号，2013年后，chrome使用了blink引擎，从而 UA 中的 AppleWebKit 版本永远停留在了537.36版本。
* `Safari/537.36`: Chrome浏览器使用Webkit引擎，想要像Safari一样构建页面，所以假装自己是Safari，在UA中添加了此部分。

综上：Chrome使用了WebKit，并伪装成Safari，WebKit伪装成KHTML，KHTML伪装成Gecko，所有浏览器都伪装成Mozilla，于是这么混乱的UA头就这么沿用下来了。这部分有意思的解释来自于<https://webaim.org/blog/user-agent-string-history/> ，有兴趣的可以去看看原文。

接下来我们还是回到如何构建真实的UA，固定的部分我们不用管，只要随机生成如下三部分信息即可：

* 浏览器：从chrome历史版本列表中随机挑选一个版本：<https://en.wikipedia.org/wiki/Google_Chrome_version_history>
* 设备：从众多手机型号中随机挑选一个，其中生成规则是ro.product.model + ro.build.id
* 操作系统：目前android平台主流的版本有：12, 11, 10, 9, 8.1.0, 8, 7.1.2, 7.1.1, 7.1.0, 7

在android端的webview ua生成规则我们知道了，但是安卓上一般都有不同的浏览器，比如uc浏览器、qq浏览器，也会存在像微信内置webview这种特殊的客户端存在，那么他们的规则是怎么生成的呢？

以UC浏览器为例，先来看下uc浏览器的UA和系统webview默认的UA有什么区别：

```
Mozilla/5.0 (Linux; U; Android 9; zh-CN; LON-AL00 Build/HUAWEILON-AL00) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/12.9.0.1070 Mobile Safari/537.36
```

可以看到相比较于原生UA，增加了`UCBrowser/12.9.0.1070`字段，这个也就是UC浏览器的名字和版本，所以想要构造随机的UC浏览器UA，我们只需要增加这个字段即可，其中uc浏览器的历史版本列表可以从豌豆荚找到：<https://www.wandoujia.com/apps/36557/history>

同理qq浏览器是增加了`MQQBrowser/{mqq_version}`，微信内置weiview是增加了`MicroMessenger/{wechat_version}`，百度浏览器是增加了`baiduboxapp/{baidu_browser_version}`。

综上想要生成一个随机的android ua，我们只需要生成Weiview默认的UA，再加上一些浏览器标识即可，具体的实现代码在下面会给出。

### 1.2 pc端

pc又分为windows、mac和linux，但是pc端的UA生成比较简单，所以可以合并在一起来看，先来看下chrome浏览器的UA

```
# windows10上
Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36

# linux上
Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36

# mac上
Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36
```

可以看出，相比较于android端，在pc端生成ua简单的多，只有chrome版本是不断变化的，我们只需要生成随机的chrome版本即可，对于firefox也是同理：

```
# windows10上
Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:107.0) Gecko/20100101 Firefox/107.0

# linux上
Mozilla/5.0 (X11; Linux x86_64; rv:107.0) Gecko/20100101 Firefox/107.0

# mac上
Mozilla/5.0 (Macintosh; Intel Mac OS X 13.0; rv:107.0) Gecko/20100101 Firefox/107.0
```

对于特殊的edge、safira等浏览器，我们也只是需要找到其浏览器版本历史列表，即可生成比较真实的UA。

### 1.3 随机UA实现

在日常工作中，生成随机UA这个需求其实比较多，相关的实现代码也比较多，但是大部分的代码都比较老，看了几个都是 android 8 以下的 UA，同时针对android端的UA生成也比较少，大部分都是PC端的，所以这里我写了一个pypi库，主要针对android和pc端的UA，争取更加贴近真人实际UA，项目主页为：<https://pypi.org/project/r-useragent/>

安装如下：

```
python3 -m pip install r-useragent
```

使用样例

```
from random_useragent import UserAgent

u = UserAgent()

# generate android user-agent
print(u.android())  # random
print(u.android(app="app"))
print(u.android(app="webview"))
print(u.android(app="uc"))
print(u.android(app="baidu"))
print(u.android(app="qq"))
print(u.android(app="wechat"))

# generate windows user-agent from chrome,firefox,edge...
print(u.windows())  # random
print(u.windows(app="chrome"))
print(u.windows(app="firefox"))
print(u.windows(app="edge"))

# generate linux user-agent
print(u.linux())
print(u.linux(app="chrome"))
print(u.linux(app="firefox"))

# generate mac user-agent
print(u.mac())
print(u.mac(app="chrome"))
print(u.mac(app="firefox"))
print(u.mac(app="safari"))

# and if you want, you can just generate random ua
print(u.random())

# or designated platform
print(u.pc())
```

## 2. UA解析

ua既然没有一个固定的格式，那么怎么去解析UA呢？目前的常见UA解析方式，都是用了正则表达式去匹配。比如python ua解析库：<https://github.com/ua-parser/uap-python>

查看其源码，发现是通过定义了一套正则规则来实现解析。

![2022-11-17T12:14:48.png](https:////saucer-man.com/usr/uploads/2022/11/4241507544.png "2022-11-17T12:14:48.png")

所以UA解析的准确率主要也是依赖于规则库的更新速度。

## 3. 安全威胁

### 3.1 web漏洞

user-agent是http header的一个字段，自然也会存在一些常见的web漏洞，比如常见的有sql注入和xss等，分享几个案例，这里就不必多说了。

* [挖洞经验 | 构造User-Agent请求头内容实现LFI到RCE提权](https://www.freebuf.com/articles/web/253102.html)
* [HackerOne | HTTP头注入之User-Agent注入](https://zhuanlan.zhihu.com/p/161688195)
* [Blind XSS through User-Agent header on Vaccination Management portal affecting admins](https://www.bugbountyhunter.com/hackevents/report?id=726)

### 3.2 在风控对抗中的妙用

UA在风控中是很重要的一个参数，比如反爬会利用短时间内ua的聚集性做封禁，也会利用UA来生成用户画像，比如用户常用设备就是用UA判断的。

下面分享一个前段时间遇到的案例，在红蓝对抗的盗号演练中，经常会使用钓鱼的方式去盗号，但是即使你拿到了用户的用户名和密码还是会登录不上去，因为账户风控策略中，如果登录环境是非历史环境，会有二次验证，比如短信验证码等。

经过测试我发现历史环境的校验是根据UA字段中的信息来判断的，进一步排查，发现UA无论怎么变化，只要带上合适的ro.product.model信息(比如`Mi 8`这样的关键词)即可成功登录。那么也就意味着只要伪造这个字段变成用户的手机即可。于是钓鱼要变两次，第一次获取用户的手机型号，第二次钓鱼拿到用户名密码之类的凭证。

事情看似解决了，但是获取手机型号的行为很怪异。在研究UA的生成和解析规则后，我想起一个问题，既然UA只能用正则表达式去解析，我推测后端是使用了类似于下面的函数来验证是否是历史环境：

```
def is_history(ua)
    ......
    history_model = "xiaomi 8"
    ......
    if re.match(history_model, ua):
        return true
    else:
        return false
```

那么我是不是可以把常见的手机机型杂糅在一块，生成一个包含很多手机型号的UA，于是我测试了下面的UA

```
JLN-A00JLN-LX1M2012K10CM2006J10CK6PGLA-AL00CDL-AN50YAL-AL50YAL-TL002106118CM2102K1ACRedmi K30 Pro.....
```

发现其不仅可以匹配JLN-A00机型，也可以匹配M2006C3LC机型，成功绕过了该登录风控策略。

1 + 6 =

 回复

4  评论

![](https://sdn.geekzu.org/avatar/0c28fe7dce7cc9a74b1cbf9d027b72f4?s=50&r=G&d=mm)

ccc
Chrome 109
Windows 10

2024年11月16日
[回复](https://saucer-man.com/information_security/982.html?replyTo=429#respond-post-982)[取消](https://saucer-man.com/information_security/982.html#respond-post-982)

太棒了，顺带提个小错误，使用样例的print(u.mac(app="safiri"))这个safari打错了，直接调试会错误

![](https://sdn.geekzu.org/avatar/aad83b0e2d88e8fdbda07ef31210122b?s=50&r=G&d=mm)

yanq
Chrome 132
Windows 10

2月26日
[回复](https://saucer-man.com/information_security/982.html?replyTo=433#respond-post-982)[取消](https://saucer-man.com/information_security/982.html#respond-post-982)

[@ccc](#comment-429) 感谢提醒

![](https://sdn.geekzu.org/avatar/004c4d14b51d0118578e2efc1c6c83a1?s=50&r=G&d=mm)

bbb
Chrome 121
Windows 10

2024年02月28日
[回复](https://saucer-man.com/information_security/982.html?replyTo=405#respond-post-982)[取消](https://saucer-man.com/information_security/982.html#respond-post-982)

棒

![](https://sdn.geekzu.org/avatar/b4efac1f46f683131f806af4ea8feb52?s=50&r=G&d=mm)

aaaaa
Chrome 109
Windows 10

2023年01月23日
[回复](https://saucer-man.com/information_security/982.html?replyTo=322#respond-post-982)[取消](https://saucer-man.com/information_security/982.html#respond-post-982)

牛皮

Copyright © 2025 By [Typecho](https://www.typecho.org) & [saucerman](https://saucer-man.com)

* [Home](https://saucer-man.com/)
* [Archives](https://...