---
title: 实战钓鱼之url魔改
url: https://mp.weixin.qq.com/s?__biz=MzkyMTI0NjA3OA==&mid=2247490656&idx=1&sn=0d98bc095f34ecfb53f0c0d5d835ba32&chksm=c187dc71f6f0556707214ade4ebd207f2a6aeba469f5641f15d96892c13a37a8856c67421f1c&scene=58&subscene=0#rd
source: M01NTeam
date: 2023-02-09
fetch_date: 2025-10-04T06:09:28.049108
---

# 实战钓鱼之url魔改

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/TPGibEO8KBwbPoko3y1oG4oweW75rEu3IMwKwKycuhRwnk3ica8hOOvibBX69oaicziaHsHKmQ1XCM6q65Lh4LMvNng/0?wx_fmt=jpeg)

# 实战钓鱼之url魔改

原创

天元实验室

M01N Team

![](https://mmbiz.qpic.cn/mmbiz_gif/TPGibEO8KBwbPoko3y1oG4oweW75rEu3I7QmcHWGwicnfk7Rr3tyek8HufbuyC990sYfiaAbOAWrEdvouV7lLKgkQ/640?wx_fmt=gif)

**背景**

在实战钓鱼演练中通常会注册近似域名来博取信任，比如：googlle.com、g00gle.com等，又或者会利用url跳转漏洞将恶意url伪装成官方域名，比如：https://google.com?check=hack.com，本文将介绍如何在不利用漏洞的情况下，将恶意域名伪装成任意官方域名。

第一式：url语法格式利用

众所周知，url由几个主要部分组成：协议、主机、端口、路径，即：

```
<scheme>://<host>:<port>/<path>?<query>
```

事实上，url的语法格式可以细分为九个部分：

```
<scheme>://<user>:<password>@<host>:<port>/<path>;<params>?<query>#<frag>
```

params常通过";key=value"的形式被某些协议用来指定输入参数，frag常通过"#flag"的形式用来跳转到一个网页的指定位置。这里的重点是，url语法允许host前面添加"user:password@"形式的用户名密码对，拿http协议的url举例，我们通常不会在host前加用户名密码对，这是因为请求的资源匿名即可访问，但是在host前加上用户名密码对也并不会影响资源的访问，借此我们可以在url中构造任意的用户名密码对。

比如，将url伪造成任意官方域名：

```
https://www.bing.com&action=login@ikun.org
```

第二式：浏览器域名解码利用

上述操作，我们对url进行了一番伪造，但是隐藏在url后面的真实域名ikun.org仍会引起警觉。于是想办法让后面的ikun.org看起来不像个域名，由于DNS服务器的解析是由英文代码所构成，所以浏览器会在访问资源前会对域名进行解码，而多个ascii字符会被解码成同一个英文字母，我们可以编写简单的JavaScript脚本进行fuzz。

```
for (let i=0;i<=65535;i++){    var a = 'https://'+ String.fromCharCode(i) +'kun.org';    try{        let url = new URL(a);         if (url.hostname && url.hostname == "ikun.org")            {                console.log(i,String.fromCharCode(i));            }    }catch{        // console.log("error");    }}
```

通过脚本我们找出域名所对应的ascii字符，比如英文字母i同时对应：

```
I i ᴵ ᵢ ⁱ ℐ ℑ ℹ ⅈ Ⅰ ⅰ Ⓘ ⓘ Ｉ ｉ
```

url进一步伪造成了

```
https://www.bing.com&action=login@ℐⓀⓊⁿ.ºʳℊ
```

第三式：IP整数形式利用

除了可以用其他ascii字符代替真实的域名外，还可以使用ikun.org的ip地址来指向真实的域名，比如

```
https://www.bing.com&action=login@127.0.0.1
```

为了更好的隐藏ip地址，我们可以将ip地址的点分十进制表示方式转换为整数表示，转换原理的简单解释：IP 地址（IPv4）由32 位的 8 位二进制文件的组合组成。由于输入实际的二进制组合（例如：11000000）非常不方便，因此使用与二进制对应的十进制（例如：192），浏览器在解析整数形式的ip地址时，会将URL中的十进制转换为二进制并分割成8位，然后从将8位的二进制数字转换为对应的十进制。

拿127.0.0.1举例，对应的二进制应该是01111111 00000000 00000000 00000001，二进制进一步转换成得到整数形式的IP 2130706433，于是url进一步伪造成

```
https://www.bing.com&action=login@2130706433
```

末尾可以使用frag稍加修饰，最终我们将ikun.org 魔改成

```
https://www.bing.com&action=login@2130706433#3.docx
```

写在最后

本文介绍了如何在不利用漏洞的情况下对恶意url进行魔改，最终达到逼真的url伪造效果，在实战攻防中逼真的url伪造往往能让攻击效果事半功倍，同时希望企业能重视人员安全意识培养，认识到人员就是企业的边界。

![](https://mmbiz.qpic.cn/mmbiz_png/TPGibEO8KBwbPoko3y1oG4oweW75rEu3IoiczHicRpSMbMMnqNUuLnH0TWynNvPOsD6BP2ibujO7KNJibjsB854cXcA/640?wx_fmt=png)

**绿盟科技天元实验室**专注于新型实战化攻防对抗技术研究。

研究目标包括：漏洞利用技术、防御绕过技术、攻击隐匿技术、攻击持久化技术等蓝军技术，以及攻击技战术、攻击框架的研究。涵盖Web安全、终端安全、AD安全、云安全等多个技术领域的攻击技术研究，以及工业互联网、车联网等业务场景的攻击技术研究。通过研究攻击对抗技术，从攻击视角提供识别风险的方法和手段，为威胁对抗提供决策支撑。

![](https://mmbiz.qpic.cn/mmbiz_jpg/TPGibEO8KBwbPoko3y1oG4oweW75rEu3IxkaDuZ6c2lmHjVkRpFibyiaZZKD3lzvntoQLYBSQwuy341VnbaLlPUHg/640?wx_fmt=jpeg)

**M01N Team公众号**

聚焦高级攻防对抗热点技术

绿盟科技蓝军技术研究战队

![](https://mmbiz.qpic.cn/mmbiz_jpg/TPGibEO8KBwbPoko3y1oG4oweW75rEu3Iw5f88UeTibCmFLL0ACHt45bibZaTh0pLAbibJXLEpptjShibxRBJGicRyhQ/640?wx_fmt=jpeg)

**官方攻防交流群**

网络安全一手资讯

攻防技术答疑解惑

扫码加好友即可拉群

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/TPGibEO8KBwa3nTcsDs91X6JY6LnXNhPLatIoU1PEVBLzWXTcnyiahhYUB9hcwX2MJkOmo9NEM2jVO8ib8yutnJxw/0?wx_fmt=png)

M01N Team

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/TPGibEO8KBwa3nTcsDs91X6JY6LnXNhPLatIoU1PEVBLzWXTcnyiahhYUB9hcwX2MJkOmo9NEM2jVO8ib8yutnJxw/0?wx_fmt=png)

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