---
title: 如何通过利用源 IP、IDOR 和信息泄露漏洞绕过 WAF 来发现 SQL 注入漏洞（翻译转载）
url: https://forum.butian.net/share/4149
source: 奇安信攻防社区
date: 2025-02-22
fetch_date: 2025-10-06T20:32:31.594003
---

# 如何通过利用源 IP、IDOR 和信息泄露漏洞绕过 WAF 来发现 SQL 注入漏洞（翻译转载）

#

[问答](https://forum.butian.net/questions)

*发起*

* [提问](https://forum.butian.net/question/create)
* [文章](https://forum.butian.net/share/create)

[攻防](https://forum.butian.net/community)
[活动](https://forum.butian.net/movable)

Toggle navigation

* [首页 (current)](https://forum.butian.net)
* [问答](https://forum.butian.net/questions)
* [商城](https://forum.butian.net/shop)
* [实战攻防技术](https://forum.butian.net/community)
* [漏洞分析与复现](https://forum.butian.net/articles)
  NEW
* [活动](https://forum.butian.net/movable)
* [摸鱼办](https://forum.butian.net/questions/Play)

搜索

* [登录](https://forum.butian.net/login)
* [注册](https://user.skyeye.qianxin.com/user/register?next=http://forum.butian.net/btlogin)

### 如何通过利用源 IP、IDOR 和信息泄露漏洞绕过 WAF 来发现 SQL 注入漏洞（翻译转载）

* [漏洞分析](https://forum.butian.net/topic/48)

在本文中，我将通过一次对斯里兰卡当地最大的供电局网站中的实战SQL注入挖掘分享如何通过利用源IP、IDOR和信息泄露漏洞绕过WAF来发现SQL注入漏洞

原文地址：<https://infosecwriteups.com/sql-injection-in-largest-electricity-board-of-sri-lanka-1a55c12104bd>
前言：
SQL 注入是一种攻击者利用网站数据库漏洞的技术，通过将恶意 SQL 代码插入表单或搜索字段等输入中，致使攻击者可以访问、修改或删除敏感信息。该漏洞可导致未经授权的访问、数据泄露甚至完全控制服务器，这也使 SQL注入漏洞成为高危害且普遍存在的网络安全威胁之一。
事情起因：
某天我的一位订阅粉丝联系到我，他询问我能否测试他们国家电力局的网站中是否存在 SQL 注入漏洞，该网站受到 Cloudflare WAF 的保护。由于我平时经常分享识别 SQL 注入漏洞的技术和方法，因此我决定接受这个挑战！那么就先从我是如何发现这个漏洞开始吧！
漏洞的发现过程：
首先我访问了该网站并使用Chrome的 Wappalyzer 插件检查该网站所使用到的的技术栈。插件显示该网站是由 PHP编程语言构建的，众所周知，PHP最容易受到 SQL 注入漏洞的影响。此外插件中还显示该网站是由Cloudflare WAF保护。
![26418DC5-4175-40F1-A78B-C97751E96E86.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/01/attach-6396079fec42d76ac239eac000a3263dde378384.png)
接下来我的渗透测试将先从这条单行命令开始：
subfinder -d &lt;REDACTED&gt; -all -silent | httpx-toolkit -sc -td -title -silent |grep-Ei'asp|php|jsp|jspx|aspx'
此命令用于查找收集 ceb.ik 的所有子域名并验证哪些是还存活的，同时还会收集有关其状态、标题和技术的相关信息，随后筛选结果，仅保留了使用 PHP、ASP、JSP 或类似的子域名，因为这些语言更容易受到 SQL 注入攻击。
如下图所示，我发现有几个子域名网站使用了PHP语言并受到 Cloudflare WAF 的保护。但其中的一个子域名：payment.ceb.ik 并没有受到 Cloudflare WAF 的保护，这成功引起了我的注意，于是我将这个子域名作为我进一步渗透的主要目标。
![49A0FE02-DF32-44E4-AC3F-1D69B57DC931.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/01/attach-f63bc0367b02058b59a782067344527848eaaab2.png)
首先在访问该子域名后，我发现了一个选择支付类型的功能点。当我点击它时，系统提示让我输入一个账号，我尝试了输入了几个随机值，但都没有奏效。
![EDBA6EF1-476D-4D93-AEDF-EFD2FFCD4343.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/01/attach-7d36f91d2ca7796fad8e5a85220db9e8ed3613f0.png)
接下来，我使用 GAU 工具收集了该子域名相关的所有URL路径，希望能发现一些有趣的东西。在收集过程中，我发现其中一个 URL 居然泄露了一个账号。
![0A4A7994-ED23-4D8D-BF5C-C6EF33B414BD.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/01/attach-60a6829400729823ff2e1c34f18c1dc8e58813fb.png)
于是我把被泄露的账号输入到输入框中。令人惊讶的是居然返回了该账号的支付信息，如账号名称、账单、手机号等敏感信息，并允许我使用该账号直接进行支付。更细思极恐的是，我意识到只需要拿到其他用户的账号，就可以对网站上的任何其他用户进行同样的操作。
![079BC445-482E-4921-A662-5C2D7FAFA8AF.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/01/attach-9d33f3ca92a4e2aaa9be251419deb8e0d0cdda74.png)
在检查 URL 路径后，我决定通过输入单引号（‘）来测试是否可能存在 SQL 注入。随即触发了一个“正在维护”的报错，该报错再次引起了我的注意，于是我决定继续深入测试该路径。
![4AF69803-AB5E-4BD4-897A-52E20D14F8FB.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/01/attach-0ba46644037100cecb3ba94b90d5f442925cb798.png)
我立刻打开了 Burp Suite，拦截了发包请求并发送到 Intruder 模块进行近一步测试。我添加了一批包含大量基于 XOR 盲注的 payload 列表，这些 payload 旨在绕过 URL 路径中的账号定位，在一系列的发包攻击后，我把返回包进行了过滤后发现有几个延迟注入的payloa返回了响应，说明这里存在延时类型的SQL注入漏洞。
![189901A8-E952-4F20-94A9-DB42FE9F1CD7.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/01/attach-158c56f164aa1ec6061242c9f3c09f8971144bcd.png)
为了近一步验证，我将其中一个有效 payload 的请求包转发到 Repeater 模块并发送了 GET 请求。经过10 秒的延迟才收到返回包内容并返回了 500 状态码，再次确信该站点确实存在延时类型的SQL注入漏洞。
![52527D00-05C3-49F4-916E-12E0693CEF35.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/01/attach-3dae2b41fdfb3792403b35e5034ab0e148d3167e.png)
出于严谨，我又使用了CURL工具来测试延迟响应，从结果来看，清一色完全一致的延迟响应无疑证实了该站点的延时注入漏洞是100%存在的。
![DACD0522-B440-45FA-AB05-FF8C98D6B80B.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/01/attach-308bd23a018404da40ea9f67f570209f2cb6e197.png)
接着来到了最后一步，我使用了 Ghauri 工具来利用这个 SQL 注入漏洞。我选择 Ghauri 是因为它是检测和利用基于 XOR 的 SQL 注入的最佳工具之一，与 SQLmap 相比，这个工具提供了更可靠的结果，而 SQLmap 在基于 XOR 的 SQL 测试方面目前还有所欠缺。
ghauri -u'<https://payment>.&lt;REDACTED&gt;/instantpay/payment/\\*'--dbs --batch --level 3 --tech=T
![516EDFB6-1977-4633-9F31-77E804795B38.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/01/attach-0f22c967a9ed6239e0864d74955a2bf9aec3fd87.png)
如上图所示，我成功检索到了数据库。我在 Ghauri 中使用了—tech=T 指令是因为我知道这是一个基于延时的 SQL 注入，并且我使用了(\\*)自定义匹配，以便 Ghauri 仅在该路径上进行测试，确保工具在利用过程中更加准确和可靠。
提交漏洞报告：
发现漏洞后，我立刻就向他们的技术团队提交了报告并敦促他们应该立即修复，以防止任何潜在的被利用。然而事与愿违，他们的回应速度极其缓慢，居然花了几周得时间才确认了我的报告。
与此同时，我决定继续测试该网站看看是否还存在其他的漏洞，于是我的渗透测试再次展开。
网站路径的Fuzz测试：
Fuzz(模糊测试)一种非常有效的测试方法，可以让你发现网站中隐藏的目录和文件，有助于挖掘到潜在的漏洞。这里我使用了 Dirsearch，当然你也可以使用 FFUF 工具作为替代方案。
dirsearch-u https://&lt;REDACTED\]\]&gt;/-w payloads/all\\_attacks.txt-e php,asp,aspx,jsp,py,txt,conf,config,bak,backup,swp,old,db,sqlasp,aspx,aspx,asp,py,py,rb,rb,php,php,bak,bkp,cache,cgi,conf,csv,html,inc,jar,js,json,jsp,jsp,lock,log,rar,old,sql,sql.gz,sql.zip,sql.tar.gz,sql,swp,swp,tar,tar.bz2,tar.gz,txt,wadl,zip-i200--full-url
![2766A7DA-1E50-4EB9-A77C-FC6AD91698CF.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/01/attach-bf17e9a986799f4d3e930ded92598b6ae375db52.png)
在上图中，你可以看到我发现了一些敏感目录和文件，其中 .env 和 .git 文件最为关键，因为它们可能存在重大的安全隐患。
接着当我读取.env 文件后，成功获取到了网站数据库的用户凭证和密钥！这种级别的敏感信息泄露在漏洞赏金计划中通常都会被归类为 P1（严重）漏洞。
随后，我利用 Git Dumper 工具检索了所有已删除的提交，并从 Git 仓库的披露中发现了更多细节...
![D6BA0997-12E5-4803-8270-AC67DD878330.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/01/attach-401f7a348a2f044597a10238d6d1ba2c44b2abda.png)
与此同时，该网站的技术团队已经着手解决并修补了漏洞，然而我决定再次尝试渗透，试图找到该网站的原始 IP 并再次利用它。于是我的探索之旅重新开始了。
通过源 IP 绕过WAF：
首先，WAF（Web 应用防火墙）存在的目的旨在保护网站免受恶意流量的侵害，但有时攻击者可以通过伪造或操纵源 IP 地址绕过WAF，攻击者通过模仿受信任的 IP 地址或利用配置错误，可以避开 WAF的 检测对网站进行未授权的访问。
我使用了一个简单的单行命令与 Shodan CLI 命令，迅速的揭秘了该网站的原始 IP 地址及其标题和服务器信息
shodansearch[Ssl.cert.subject.CN](http://Ssl.cert.subject.CN):"&lt;REDACTED&gt;"200--fields ip\\_str | httpx-toolkit -sc -title -server -td
![6C10D72B-7261-491F-9C89-6795E3010E54.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/01/attach-b0ac3f237f6df325999357b7277f5f72d275b437.png)
如上图所示，我发现了两个域名的原始 IP 地址，其中一个就属于之前发现 SQL 漏洞的站点，而另一个则是主网站的。当我尝试在浏览器中直接访问这些 IP 地址时，发现目标完全可访问且未受到 WAF 的保护。于是我再次在同一端点上利用了 SQL 漏洞，尽管技术团队已经修补了，但我仍然能够检索到相同的数据库。通过针对原始 IP，我绕过了他们的修复补丁并成功执行了漏洞利用。
接着我又使用 Burp Suite 检查了主网站的源 IP，经过爬取网站后，我发现了一个 POST 端点，该端点给我提供了一个用于进一步测试的参数。
POST /contactus/load\\_area\\_office HTTP/1.1
Host: 124.43.162.71
Cookie:&lt;REDACTED\]\]&gt;
Content-Length: 16
Sec-Ch-Ua-Platform: "Windows"
X-Requested-With: XMLHttpRequest
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36 Edg/131.0.0.0
Accept: \*/\*
Sec-Ch-Ua: "Microsoft Edge";v="131", "Chromium";v="131", "Not\\_A Brand";v="24"
Content-Type: application/x-www-form-urlencoded; charset=UTF-8
Sec-Ch-Ua-Mobile: ?0
Origin: <https://124.43.162.71>
Sec-Fetch-Site: same-origin
Sec-Fetch-Mode: cors
Sec-Fetch-Dest: empty
Referer: <https://124.43.162.71/contactus/en>
Accept-Encoding: gzip, deflate, br
Accept-Language: it,it-IT;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6
Priority: u=1, i
Connection: keep-alive
iMainOfficeID=11
在这个 POST 请求包的请求体中，我注意到了参数 iMainOfficeID=11。于是我在该参数插入了一个单引号（‘）并发包，这个操作立刻返回了 SQL 报错。接着我复制了原始请求包并将其保存为 request.txt 到我的 Kali 虚拟机上做进一步的测试。
ghauri -r request.txt--dbs --batch --level 3 --tech=t
经过近一步的测试后，我再次成功利用了 SQL 注入，这次是通过主网站的原始 IP 完全绕过了 Cloudflare WAF 的保护。
![7B77C99B-30A4-414F-AF1C-4D049C147FC8.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/01/attach-bf49df25cf354c2bfe6281d5daaa3669586ec109.png)
事实证明，尽管开发者们认为通过部署 WAF（Web 应用防火墙）就能确保他们的网站安全无忧，但是攻击者仍可利用源 IP 绕过保护措施，轻松入侵他们的网站。
本次渗透测试的关键要点：
1. WAF 并非万无一失：尽管 WAF 提供了一层保护，但通过源 IP 欺骗或利用配置错误等技术仍可绕过。开发者们不能仅依赖 WAF 来确保网站的安全。
2. 敏感数据泄露：信息泄露漏洞，如泄露的账号和暴露的.env 文件都可能导致严重的后果。对用户进行适当的访问权限控制和安全编码实践对于此类泄露的防范至关重要。
3. 及时修补：对初始漏洞报告的缓慢响应导致了攻击者进一步的利用。技术团队任何时候都应该优先响应及时修补漏洞，以防止网站长期暴露于风险之中。
4. 多层安全：实施包括安全编码实践、定期渗透测试和监控配置错误在内的多层安全方法，对于防范高级攻击至关重要。
最终总结：
本文向大家展示了即使是收到安全防护的网站，如果安全措施不全面且未及时更新，也可能被攻破。通过从中学习，技术团队可以加强防御，减少未来类似漏洞被利用的风险。
最后，该团队在第二次报告后修补了该网站上的所有漏洞，希望你喜欢这篇文章
免责声明：
本文提供的内容仅用于教育科普和技术交流。在...