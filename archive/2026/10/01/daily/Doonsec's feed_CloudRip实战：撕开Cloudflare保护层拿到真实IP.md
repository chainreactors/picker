---
title: CloudRip实战：撕开Cloudflare保护层拿到真实IP
url: https://mp.weixin.qq.com/s/A8ileb526axsFdXqGcinGQ
source: Doonsec's feed
date: 2026-10-01
fetch_date: 2026-10-02T07:48:04.493658
---

# CloudRip实战：撕开Cloudflare保护层拿到真实IP

# CloudRip实战：撕开Cloudflare保护层拿到真实IP

原创

Red Hunter
Red Hunter

黑白之道

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

![](https://mmbiz.qpic.cn/mmbiz_png/nGzNudUIJ6PdBlHj3sXtqMkhKpR9qdPpGFRS4BedPozd16cxZxYGkIJ1mclZzz782ptGNhsGuVOaeUZaCgecYJuEbtFfNZL3Lkes5LIibicXk/640?from=appmsg)
> **导语**：Cloudflare（CDN即内容分发网络与安全防护服务商）靠挡DDoS（分布式拒绝服务攻击）和藏IP攒下800亿美元的身家，但挡得住主站挡不住所有子域名。CloudRip就是盯着这个缝——把子域名解析到的非Cloudflare IP全捞出来。本文手把手装、跑、实战，并讲清楚这工具能干什么、不能干什么。

## 一、背景

很多组织主站套了Cloudflare全套保护，但子域名常常被遗忘。开发服务器、预发布环境、管理后台这些资产大多跑在Cloudflare保护圈外，真实IP就这么裸奔在外网。CloudRip专门干这事：扫子域名，把不属Cloudflare的IP筛出来摆到台面上。

下面装上、跑一遍，再总结它的好处和短板。

## 二、第一步：下载安装

先克隆GitHub仓库：

```
kali> git clone https://github.com/staxsum/CloudRip.git
kali> cd CloudRip
```

![克隆CloudRip仓库](https://mmbiz.qpic.cn/mmbiz_jpg/nGzNudUIJ6PnKrz0Cu3TYPyz4lxlHk6Ro3nPLLKaOSjgFSDfwepfTrs2bAL5UlSPITq8icmibiabfeCgzicofu9VZDr8I5GqqOuITYZADy6yA4w/640?from=appmsg "克隆CloudRip仓库")

装依赖。只需要两个Python库：`colorama`（彩色终端输出）和`pyfiglet`（ASCII艺术字横幅）。

```
kali> pip3 install colorama pyfiglet --break-system-packages
```

![安装CloudRip依赖](https://mmbiz.qpic.cn/mmbiz_jpg/nGzNudUIJ6Mvav82KI1SrzdgDoYqmp2H7EtyXHjZ4iafnAIFx4DHos8Ed73fTNQcp85aSjZD1jlTTsSOg2OKbyiaicuP4oz3zmKwwOjCPYEP74/640?from=appmsg "安装CloudRip依赖")

装完就能开扫了。工具自带默认词表（`dom.txt`），不用额外准备。

![CloudRip文件结构](https://mmbiz.qpic.cn/sz_mmbiz_jpg/nGzNudUIJ6PVibuzIic886P6pF8jqPYeq6Nno0b2pWibRUH7DWiar2BDdzgEhicBxVrxcHc26S74dOad9WXxNpLLlQL1zPC9eYOpHia2Z3FWJVchw/640?from=appmsg "CloudRip文件结构")

> **红队视角**：能 git clone + pip install 一步到位，对侦察工具来说门槛算很友好。脚本小子（Script Kiddie）也能上手，但能不能用好还是看词表质量。

## 三、第二步：基础使用

先跑最简单的命令看一眼效果。原文里用BuildWith找了一批挂了Cloudflare的俄罗斯站点做靶子。

![BuildWith找Cloudflare站点](https://mmbiz.qpic.cn/sz_mmbiz_jpg/nGzNudUIJ6P3I88WD5KVqiaObYtIXialzE2sOnicTtJ84PF1ibBus4g5xI1AlDzGBnAKNztvLY1NTuWEB5dHzZibd9WuCjSK0W14uKD0kibV4bONw/640?from=appmsg "BuildWith找Cloudflare站点")

扫之前先用`whois`确认一下站点归属：

```
kali> whois esetnod32.ru
```

![whois查询esetnod32.ru](https://mmbiz.qpic.cn/sz_mmbiz_jpg/nGzNudUIJ6OibOJBEAvPo7ksGo5BZTG5TCp6MtRibGZpMcjncmu5NgGBUKLPpDUwHn7OdydPNEylfzT6QSGDrecSdDmlqh3V4qNMOkHxV3Oz8/640?from=appmsg "whois查询esetnod32.ru")

NS记录（域名服务器记录）来自CloudFlare，注册商是俄罗斯。用`dig`看看A记录（域名到IPv4地址的映射记录）里CloudFlare代理是不是把真IP藏了。

```
kali> dig esetnod32.ru
```

![dig查询esetnod32.ru的A记录](https://mmbiz.qpic.cn/mmbiz_jpg/nGzNudUIJ6MlSlVLY8EIroKyicHvibibv3ew9S9YbUh96TjKrBpVY3kz7hrkOKlf2BF8lm5ooIqBZib1yMQib4QxBHBbxuSGZ7RhxI8yCuEqIy1U/640?from=appmsg "dig查询esetnod32.ru的A记录")

返回的IP都属CloudFlare。CloudRip上场。

```
kali> python3 cloudrip.py esetnod32.ru
```

工具按词表挨个测常见子域名（www、mail、dev 这些），解析出它们的IP，再判断是不是Cloudflare的。

![CloudRip扫描esetnod32.ru运行截图](https://mmbiz.qpic.cn/sz_mmbiz_jpg/nGzNudUIJ6OzfZL5hiciceaDIgUD9lbLA5bAibNCIhjfUFiaX9oRmLUtsNdDibyNTMFhTSyWLKY7zfhbnzKyHY1fkrZ4MlmUzicXlpOZuR9WvM0Go/640?from=appmsg "CloudRip扫描esetnod32.ru运行截图")

结果一目了然：主站IP是CloudFlare的，但子域名的IP都不属CloudFlare。

> **红队视角**：这一手太常见了。主站套盾、子站裸奔。运维视角下是失误，攻击者视角下就是直球——绕开Cloudflare直接打真IP，老DDoS、老定向扫描都能打上。

## 四、第三步：进阶选项

CloudRip提供几个命令行参数，让你对侦察节奏有更多控制。

完整语法：

```
kali> python3 cloudrip.py example.com -w custom_wordlist.txt -t 20 -o results.txt
```

逐个拆解：

* **`-w`（wordlist，词表）**：指定自定义子域名词表。默认的`dom.txt`已经不错，但老手一般会按行业或目标类型维护自己的定制词表。
* **`-t`（threads，线程数）**：控制扫描线程数。默认10够用大多数场景。如果词表特别大想跑快点，可以调到20甚至更高。注意线程太多可能触发限流（Rate Limiting）或显得可疑。
* **`-o`（output file，输出文件）**：把所有非Cloudflare的IP存到文本文件。

## 五、第四步：实战示例

走一个完整场景看CloudRip怎么嵌入真实行动。

### 场景一：自定义词表打特定目标

先用subfinder（另一款流行的子域名枚举工具）跑一遍，发现了一批独特的子域名：

```
kali> subfinder -d rp-wow.ru -o rp-wow.ru.txt
```

![subfinder枚举rp-wow.ru子域名](https://mmbiz.qpic.cn/sz_mmbiz_jpg/nGzNudUIJ6OgPSbAicaoxRpPz0scaWL7I7z13yeFfNkNsibzicbQteteLEGIjDEMDyLR3TDERiaD6Cf31LpUjwQxOETqlnlEiauSZ15b9k0ibQqW8/640?from=appmsg "subfinder枚举rp-wow.ru子域名")

过滤掉根域名，只留子域名：

```
kali> grep -v "^rp-wow.ru$" rp-wow.ru.txt | sed 's/.rp-wow.ru$//' > subdomains_only.txt
```

![grep sed过滤子域名](https://mmbiz.qpic.cn/sz_mmbiz_jpg/nGzNudUIJ6OfgHicVTtNC8z9z7nbticzIzNZQCKFIvVavWMcnbYYtMZa5EGYbWKBic62phEhXR12UialCLp4SicowAFicu3FLdia2ZXcicb3h6BjZKE/640?from=appmsg "grep sed过滤子域名")

接着拿这个自定义词表跑CloudRip：

```
kali> python3 cloudrip.py rp-wow.ru -w subdomains_only.txt -t 20 -o findings.txt
```

![CloudRip自定义词表扫描rp-wow.ru](https://mmbiz.qpic.cn/mmbiz_jpg/nGzNudUIJ6NPSrTicdUHU5nDF0GeQ74NvgicibleiaiaXqaurEjtnStwsvNb5ZyFK7Ssc9JQd7HcFVqoFLPsILy49v14O5vUibnh0CZdLLYvImrN4/640?from=appmsg "CloudRip自定义词表扫描rp-wow.ru")

> **红队视角**：`subfinder`（子域名枚举）+ `grep/sed`（过滤纯子域名）+ `CloudRip`（筛选非Cloudflare IP）这个三件套是子域名侦察的标配。CloudRip 自己没枚举能力，它只负责"筛"，前面得有枚举器喂数据。

## 六、工具优点

CloudRip把一件事做到极致。不搞瑞士军刀路线，只把侦察的一个环节做精。

多线程架构在速度和资源消耗之间取得平衡。线程数能调，但默认值已经覆盖大部分场景，不用天天调参。

## 七、工具短板

跟所有工具一样，CloudRip有局限，靠它之前得先认清。

**第一，效果完全看词表**。目标组织用奇怪的命名规范，最全的词表也会漏。

**第二，安全意识强的组织把所有子域名都纳进Cloudflare保护**——这种情况下CloudRip基本没活干。

**第三，CloudRip只看DNS解析**。它不上历史DNS记录分析，不查SSL证书里挂的额外域名这些进阶手法。它该是侦察工具箱里的一件，不是唯一一件。

> **红队视角**：这三条短板其实就是侦察链上要接别的工具的原因。CloudRip 处理"已知子域名筛选"，SecurityTrails / ViewDNS 处理历史 DNS，Censys / Shodan 处理证书和被动 DNS。多工具组合才是完整侦察。

## 八、总结

CloudRip是个简单有效的工具，帮你在Cloudflare保护下找出真实源站。原理就是批量扫可能的子域名，看哪些解析出来的IP不属Cloudflare——这些就是可能的真实服务器位置。

工具好上手，几乎不用准备，自动筛结果省时间。新手老兵都用得上。

跑起来试试——可能就成你工具箱里的又一件。

---

**原文地址**：https://hackers-arise.com/web-app-hackingtearing-back-the-cloudflare-veil-to-reveal-ips/

**工具仓库**：https://github.com/staxsum/CloudRip

---

![](https://mmbiz.qpic.cn/mmbiz_jpg/nGzNudUIJ6NicW9ibGLUvuuvVxdHnD93Seuk110kKso5DRxBD7NO7CsLuVTzSKZuGiaLwIfYJiaOSxpfPCibCVtpwfEeNmicUGtu2ia9bDicyqfK2lg/640?from=appmsg)

[![](https://mmbiz.qpic.cn/mmbiz_jpg/nGzNudUIJ6Omib0yeIGW13FxYIkBbGiaWChhtGQAG2uQiau9ZSa6Hy3rDicgJVO4UBiaysdsgst9nqtWPsyROnJb7VWEDbmDBXNuRvJlAuy72Kiac/640?from=appmsg)](https://mp.weixin.qq.com/s?__biz=MzAxMjE3ODU3MQ==&mid=2650621549&idx=1&sn=21c4b072726d2387d562109ada6b9bbb&scene=21#wechat_redirect)

[![](https://mmbiz.qpic.cn/mmbiz_jpg/nGzNudUIJ6MtDlhrwXLGFpGb1qSDLYS7Nf1iasS39icAM4XwNdKscvwkGLxICGvIMKxLRXsqYxrw9t0FsTuDS5qR5Vucic8FEwv8esf5OYMky0/640?from=appmsg)](https://mp.weixin.qq.com/s?__biz=MzAxMjE3ODU3MQ==&mid=2650621944&idx=1&sn=3cc6dc9876a20466d4ec3634deb80220&scene=21#wechat_redirect)

[![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/nGzNudUIJ6MpMyyicc2Jn9xxBV2QmOeDba8aXZDe76hia04rFdAZB4RqtweChzpGiahNhSZ8132Rh9CXCLV7g4GKKJPmcpibibLiaF3sNyQeWo29k/640?from=appmsg)](https://mp.weixin.qq.com/s?__biz=MzAxMjE3ODU3MQ==&mid=2650622065&idx=1&sn=09f8ae84c06d4331e71c277b177ae701&scene=21#wechat_redirect)

> 👇 点击**阅读原文**，访问我的网站

---

预览时标签不可点

阅读原文

不喜欢

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/3xxicXNlTXLicpdp8GZxicJpcFIZglvakzYRZiaqt6W61hfgibjeymOgiaGqRsgNvgWIacMj7Gk4PIZ4o2NtW1zb9P6Q/0?wx_fmt=png)

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