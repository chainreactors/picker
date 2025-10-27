---
title: 200小时黑客挑战：如何在BugCrowd上赚取2万美元？
url: https://mp.weixin.qq.com/s?__biz=MzU2NzcwNTY3Mg==&mid=2247485353&idx=1&sn=aa2044a30cc9dd73ceb51a58bde65afe&chksm=fc986e8ecbefe7987e15c22353288d0a1b7bc22f0ee6ee8a29edc795fc82367f74bccee82fc6&scene=58&subscene=0#rd
source: Hacking就是好玩
date: 2025-02-24
fetch_date: 2025-10-06T20:36:39.153225
---

# 200小时黑客挑战：如何在BugCrowd上赚取2万美元？

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/eLgL5R4W3Fgo2cRfQjkqFgZffibFh4BLXll1MP3Dyqew2OHCUSh3XIxpyF3xsaZDb3InhsLAbqHmR6XP15SyK6A/0?wx_fmt=jpeg)

# 200小时黑客挑战：如何在BugCrowd上赚取2万美元？

w8ay

Hacking就是好玩

在网络安全的世界里，漏洞赏金（Bug Bounty）项目就像一场高手云集的“擂台赛”，吸引着全球的白帽黑客们一显身手。

今天分享一个真实的故事：一位安全研究者和他的朋友Mohammad Nikouei决定在BugCrowd上挑战一个公开的漏洞赏金项目。这是已被众多白帽高手打过的项目，目标公司知名度较高，他们也并非全职挖洞，但他们选择投入每人100小时，总计200小时，来完成这次挑战。最终获得了20,300美元的赏金。

这篇文章将详细介绍他们的方法、技术细节和经验总结。

文本转自：https://blog.voorivex.team/20300-bounties-from-a-200-hour-hacking-challenge#heading-reconnaissance

## 选择赏金项目

俩兄弟没把钱当成唯一目标，而是想好好玩一把“挖洞”。他们给自己定了个规矩：每人100小时，总共200小时，纯当挑战。他们觉得，盯着过程而不是光想着赏金，能让自己更有动力，哪怕遇到坑也能坚持下去。

如何选择一个赏金项目？这个项目的技术栈应该和你的技能匹配，作者两兄弟倾向于选择赏金范围多，架构广泛新旧技术都有，并且有专业的应急响应团队的项目。

最主要的是 todayisnew在这个项目排行榜上名列第一。如果他能够发现许多漏洞，为什么我们不能呢？不要低估自己，因为每个赏金猎人都有自己独特的思维方式来测试网站。

## 信息收集

信息收集是漏洞赏金项目的起点，作者团队在这部分采用了多种技术手段。

* **利用证书发现资产**

* **利用 IP 进行发现**

* **利用 CSP 响应头**

* **Google Dorks**

* **利用Google Analytics id**

* **DNS爆破**

* **OSINT**

### 证书

常见的证书搜索方法是搜索 `Common Name` ；然而，证书有不同的部分，如 `Organization` 字段等。有一些网站在网络上搜索并保存证书，例如 shodan 或 censys。可能有其他替代方案。以苹果公司为例：

![](https://mmbiz.qpic.cn/mmbiz_png/eLgL5R4W3Fgo2cRfQjkqFgZffibFh4BLXfWEIQ142eThkmbAOlBFHcAjpGzkUD0LfwjMLqbnsP7kJlm2o5Fekag/640?wx_fmt=png&from=appmsg)

使用以下命令可以列出苹果公司的根域名：

```
curl -s "https://crt.sh/?O=Apple%20Inc.&output=json" | jq -r ".[].common_name" | tr A-Z a-z | unfurl format %r.%t | sort -u | tee apple.cert.txt
```

![](https://mmbiz.qpic.cn/mmbiz_png/eLgL5R4W3Fgo2cRfQjkqFgZffibFh4BLXhK3BY0fXOibV9VtUgKQwguTmFtnVJ9vMEnGXZcYEXXs3ko9JaKTW0nA/640?wx_fmt=png&from=appmsg)

### **利用 IP 进行资产发现**

每家公司可能拥有一些 CIDR，有时很难找到这些 CIDR，因为所有者的名字模糊不清；然而，带有公司标识的 CDIR（在 ASN 名称中的 Apple）。要找到 IP、CIDR 和 ASN，可以使用很多方法，例如 ipip.net。

![](https://mmbiz.qpic.cn/mmbiz_png/eLgL5R4W3Fgo2cRfQjkqFgZffibFh4BLXvwviauYt3rvTzC8YiawwbBWdGgVcXbopZ4cNZFcHicbHzy7WAtzj95vfA/640?wx_fmt=png&from=appmsg)

扫描了公司所有的 CIDR、ASN 和 IP，提取了证书信息，并发现了一些域名。通过以下命令，可以找到 `alternative names` 和 `common names` ：

```
echo AS714 | tlsx -san -cn -silent -resp-only
```

### OSINT

你可能已经在网上阅读过OSINT技术。然而，作为一名白帽黑客或猎人，你应该不断跳出思维定式。在这个阶段，作者团队在完成基本的信息收集后，转向了 OSINT。

起初只是在网上漫无目的地搜索，只是阅读了一些关于公司的新闻，以找出一些新东西（实际上作者也不知道在寻找什么，只是在浏览）。

在这个时候，一个巨大的里程碑时刻来了。

公司有一个新闻博客，当我偶然看到一篇博客文章时，我发现了一个像这样的域名 `championscompany.com` 。检查信息收集的结果，它不在域名列表中。

之后，作者手动检查了公司所有的 5,000 篇博客文章，并发现了 60 个不在信息收集中的有趣的域名。

## 漏洞

在测试过程中发现了一些有趣的安全漏洞。这里从一些简单的开始，为了避免无聊，作者挑选了几个具有代表性且有趣的案列。

### 通过 Swagger 泄露访问所有用户数据

通过 DNS 暴力破解（就是测试test子域）发现了 `test.target.tld` 子域名。找到了一个在 `5000` 端口上无认证的 Swagger UI。

大约有 100 个 API 看起来需要认证，于是开始逐一测试每个 API（无聊但必要）。

令人惊讶的是，发现了10 个开放的 API，其中 2 个正在泄露 身份信息，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/eLgL5R4W3Fgo2cRfQjkqFgZffibFh4BLXbRxhmgricAjED89goHZaMprdkMzxBvmKAO2ykr3vgz9picaIibyH1kmqw/640?wx_fmt=png&from=appmsg)

### 两个SQL注入

渗透测试过程中最有效的方法之一是威胁建模。一旦我们了解目标的环境，我们就可以准备测试用例和攻击场景。

威胁建模非常关键；你不能随便fuzz，这样很难有结果，而且还要花费很长时间。

系统是基于旧架构的遗留系统，包含从数据库加载的字段（如country），可以对这些字段检测基于时间的SQL注入。

于是发现了 2 个payload是 `1'XOR(SELECT CASE WHEN(1234=1234) THEN SLEEP(7) ELSE 0 END)XOR'Z` 的sql注入。

![](https://mmbiz.qpic.cn/mmbiz_png/eLgL5R4W3Fgo2cRfQjkqFgZffibFh4BLX5own4Xon3fNPBfqZicFU9SbHtBaQbkBmaYQhdKLSLoqukBffDRyCWoA/640?wx_fmt=png&from=appmsg)![](https://mmbiz.qpic.cn/mmbiz_png/eLgL5R4W3Fgo2cRfQjkqFgZffibFh4BLX4jkibpdnxy1taedZR1xk3H0vlZmiaNu8Y6CGBVFInQQOsvmPO4J41Jgw/640?wx_fmt=png&from=appmsg)

### 所有用户信息泄漏

当浏览应用程序时，看到一个类似这样的请求：

```
GET /users/58158 HTTP/2
Host: www.target.com
Cookie: x
Content-Length: 0
Sec-Ch-Ua:
```

尝试通过更改请求中的数字 ID 来获取用户信息，类似于许多渗透测试者所做的那样，但遇到了 403 错误。

然后作者切换了请求方法为 PATCH ，这是一些白帽子使用的策略，但那里也没有奏效。然而，作者的关键策略是添加特定的header头，通过添加 Accept: application/json ，成功收到了 200 OK 响应。

The result:

![](https://mmbiz.qpic.cn/mmbiz_png/eLgL5R4W3Fgo2cRfQjkqFgZffibFh4BLXesu2qUJpoEYXqveOJLlZiayUQibcLLKyjicIOUtIn453CF7DOPGnDygNQ/640?wx_fmt=png&from=appmsg)

### 存储XSS

任何编辑器使用文本的地方都是测试 XSS 的环境。

当我们浏览某个程序时，我们发现一个位置可以写像 Twitter 一样的发布笔记。然而，它使用正则表达式过滤掉危险的标签，所以我们不应该在这里气馁，继续测试并成功绕过了。

但他们有 CSP，所以使用了google的payload来绕过 CSP：

```
xss<script/src="https://www&#x2e;google&#x2e;com/complete/search?client=chrome&q=hello&callback=alert#1"> "></script>
```

![](https://mmbiz.qpic.cn/mmbiz_png/eLgL5R4W3Fgo2cRfQjkqFgZffibFh4BLXTldIV8CoibgQHnLqVibbDASKxdJdCFJ9a0YJTmfJibwvrwlPh8qKHHrwg/640?wx_fmt=png&from=appmsg)

### **员工域访问导致所有交易泄露**

在信息收集过程中，作者团队发现了一个特别有趣的域名，其名称中包含 `demo` ，例如 `companydemonew.com` 。该域名仅提供登录或注册选项。注册时，需要公司电子邮件地址，如 `mamad@company.com` 。

![](https://mmbiz.qpic.cn/mmbiz_png/eLgL5R4W3Fgo2cRfQjkqFgZffibFh4BLXOPmrVqT0fWU6ymor98h6SqTqlQ8k1cFaZMyickQwFRrmj8Ieum9vjPQ/640?wx_fmt=png&from=appmsg)

于是作者注册了 `mamad@company.com.burpcollaborator.com` ，并成功绕过了注册流程，收到了激活邮件！

由于该域名无法公开访问，我们预计在登录后存在许多漏洞。在探索网站功能后不久，我们的预期得到了证实。结果，只需将数字 ID 从 35 更改为 36，我们就发现了一个重大的 IDOR 漏洞。

![](https://mmbiz.qpic.cn/mmbiz_png/eLgL5R4W3Fgo2cRfQjkqFgZffibFh4BLX0ywmzyiaAMex2sbXcAqoqD4vbYBqCjO1Kb0q9reX06I7VplMK61c6ZA/640?wx_fmt=png&from=appmsg)

成果：

![](https://mmbiz.qpic.cn/mmbiz_png/eLgL5R4W3Fgo2cRfQjkqFgZffibFh4BLXSEm0bPKHaBFb2oUbRV3yMdbTt2nwyM3ekSoBibL64TAUby7qrEaOckQ/640?wx_fmt=png&from=appmsg)

### **WPEngine 配置文件**

使用公共字典，你可以找到一些漏洞，但自定义字典可以找到更多。使用我们的私有单词表，我们能够找到 `WPEngine` 配置文件：

```
https://target.com/_wpeprivate/config.json
```

![](https://mmbiz.qpic.cn/mmbiz_png/eLgL5R4W3Fgo2cRfQjkqFgZffibFh4BLXMmxkut8hy37MibRp287zUB2gib5Em86hbK0tv86AO22LsW2906E2LEtg/640?wx_fmt=png&from=appmsg)

### **其他漏洞**

* 数据库凭证泄露\*2

* 账号接管

* 反射XSS\*10

* 信息披露\*2

* 业务逻辑漏洞\*2

* 子域名接管\*2

## 总耗时

作者使用toggltrack程序跟踪时间，以评估旅程结束时的进度。结果如图所示：

![](https://mmbiz.qpic.cn/mmbiz_png/eLgL5R4W3Fgo2cRfQjkqFgZffibFh4BLXN8ItgpUpia6WhqPA28UR6ibJDIJGwxj8MMvK7Jpq7nsC0uEBLxjatHmA/640?wx_fmt=png&from=appmsg)

他们花费了大约 200 小时（每人 100 小时）在这次漏洞赏金活动中。达成 200 小时共同工作的目标后，我们暂停了狩猎，等待开放报告的处理。几乎用了 5 个月的时间收到所有报告的赏金，最后，他们的这次旅程赚了 20,300 美元。

## 总结：怎么学他们？

这200小时挑战，这故事挺带劲儿的，不光是技术牛，心态和协作也真值得夸。200个小时在一个公开被挖过很多次的项目上，从侦察到挖洞，他们靠自动化工具、手动翻博客、OSINT情报，三管齐下，最后搞出成果。给新手白帽子的小建议：巩固基础知识，别光靠工具，多动手试试；中级白帽子可以学学他们的策略，效率还能再上一层楼。

给新手推荐下面几本书，巩固基础知识，对web安全有个全面的认识，形成自己的“威胁建模”，总之，坚持下去，坑再多也能挖出金子。

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/eLgL5R4W3FjHty0EhJ3ohRK5fgibRAto40C8GWzr2qkcQTpsQr3YSmiaWSxJsliaX7qic9zVVpU7YcKrgFuXPzjBDg/0?wx_fmt=png)

Hacking就是好玩

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/eLgL5R4W3FjHty0EhJ3ohRK5fgibRAto40C8GWzr2qkcQTpsQr3YSmiaWSxJsliaX7qic9zVVpU7YcKrgFuXPzjBDg/0?wx_fmt=png)

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