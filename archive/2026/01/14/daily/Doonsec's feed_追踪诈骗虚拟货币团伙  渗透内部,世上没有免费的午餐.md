---
title: 追踪诈骗虚拟货币团伙  渗透内部,世上没有免费的午餐
url: https://mp.weixin.qq.com/s/TqjqSF5fqWuRWW0UDXnxNA
source: Doonsec's feed
date: 2026-01-14
fetch_date: 2026-01-15T03:28:57.679484
---

# 追踪诈骗虚拟货币团伙  渗透内部,世上没有免费的午餐

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/cm9mPvQVqibGIFFDR9y64HwDGGrAJ04XXY11swT55oyYoXD0txylQKySgl4u3cF6np8x0OSRB4QzavUibz6ib5aAQ/0?wx_fmt=jpeg)

# 追踪诈骗虚拟货币团伙 渗透内部,世上没有免费的午餐

原创

原来我还在你身边

网安守护

![]()

在小说阅读器中沉浸阅读

##

## 阅读须知

文章仅供参考，未经授权请勿利用文章中的技术资料对任何计算机系统进行入侵操作。利用此文所提供的信息而造成的直接或间接后果和损失，均由使用者本人负责。本文所提供的工具仅用于学习，禁止用于其他！！！

## 圈套诱因

近年来，虚拟币市场异常火爆，各类相关平台纷纷涌现。然而，随之而来的是层出不穷的诈骗。最近，接到了一个电话，对方声称能帮我一夜致富。出于好奇，我决定亲自调查这个机会。

![](https://mmbiz.qpic.cn/mmbiz_png/WTOrX1w0s54XMawBBGogicB32mB1SmFJ0LZLW1mxW6TeL3uxazrk5sMaOQia4nyvFCcicibVibHbSy1SsnnrlPqskibA/640?wx_fmt=png)

按照电话中的指引，一位自称是客服的人添加了我的微信，并将我拉入了一个微信群。群里人数众多，至于有多少人被卷入这个局，我无从得知。

![](https://mmbiz.qpic.cn/mmbiz_png/WTOrX1w0s54XMawBBGogicB32mB1SmFJ0dibPkqr06TZicGfgTHiaPzJcbptMiayviaKdebFv1rJRPick35QcGxvq44Cg/640?wx_fmt=png)

进入群后，许多自称是币圈大佬和资深玩家的人在里面非常活跃。我对这些人的真实身份存疑，也不便询问。不久，群主自称是某平台的客服开始活跃，并推广一种看似非常有吸引力的虚拟币玩法，这激起了我的兴趣。

![](https://mmbiz.qpic.cn/mmbiz_png/WTOrX1w0s54XMawBBGogicB32mB1SmFJ0tlvJvuU7LB750FibPOSjhtQdE5BRqicm80ExplF5QMMDSwAq2E3O4OIQ/640?wx_fmt=png)![](https://mmbiz.qpic.cn/mmbiz_png/WTOrX1w0s54XMawBBGogicB32mB1SmFJ0qTGY4icX1rSqK0jU78hf08uLibJicY9NNDibUtADVb76QQ0FoTWg3jhicpw/640?wx_fmt=png)

这个群的鲜明标题和诱人的回报让我心动不已。然而，这些夸张的宣传也透露出平台的不可靠之处。因此，为了彻底揭露这一套路，我开始了一场探索之旅。

## 踩点圈套

我首先进行了一系列的框架、端口、目录和子域名扫描，动作迅速而彻底。扫描结果显示，有三个端口开放，基本可以确定目标是一台Linux机器。

![](https://mmbiz.qpic.cn/mmbiz_png/WTOrX1w0s54XMawBBGogicB32mB1SmFJ03eUIHMPSxe0EXK3h71qGWDnOCuiaFcXiapM5IHIz1xE3lNA4QdKUr8sw/640?wx_fmt=png)

遗憾的是，我未能识别出任何框架，这可能意味着平台是定制开发的或者是完全自主编写的。

![](https://mmbiz.qpic.cn/mmbiz_png/WTOrX1w0s54XMawBBGogicB32mB1SmFJ0hrKbWXz0AAdhGkUgnLr5AgiaXicfYqqfzWkU3EczzSr2RJybiblZ4c5hA/640?wx_fmt=png)

对子域名的扫描也未能带来任何发现。

![](https://mmbiz.qpic.cn/mmbiz_png/WTOrX1w0s54XMawBBGogicB32mB1SmFJ0SibNjQ6NKqxuZgL8RQPR01SW42XyQllTbSJhNVV3M9EnNIAjW9icdU2w/640?wx_fmt=png)

目录扫描未能成功，可能是因为存在WAF拦截或者目录路径被开发者特别定制过。这使得直接获取shell的可能性不大。因此，决定暂时搁置这条线索，有时候细节会决定整个行动的成败。

![](https://mmbiz.qpic.cn/mmbiz_png/WTOrX1w0s54XMawBBGogicB32mB1SmFJ0wMM5DrazHPfiaVBSp1yEiaSicU7HXhLIgUWoED58vKicfia7vzGJjV0OibrA/640?wx_fmt=png)

## 艺术控权

完成了初步的侦查后，我开始深入探索这个号称能带人暴富的平台。由于平台没有提供注册账户的功能，我决定试试运气，看看是否有未删除的测试账号。

最初尝试的手机号`13888888888`提示账号不存在。记得之前在做SRC（安全响应中心）任务时，曾经凭直觉成功猜测过手机号，所以这次也采用相同的方法。通过Burp Suite设置两个参数进行扫描，竟然真的找到了一个测试账号：`13100000000`，密码`123456`。

![](https://mmbiz.qpic.cn/mmbiz_png/WTOrX1w0s54XMawBBGogicB32mB1SmFJ0X5iaOyO0HPibbnqb9Kz6l1am4Q2tkicvxFRceeaVk1hicHJ5CD6uuzPa4Q/640?wx_fmt=png)![](https://mmbiz.qpic.cn/mmbiz_png/WTOrX1w0s54XMawBBGogicB32mB1SmFJ0yp76UyF5sXHjzQZCk3E6VP1ibdOZvViclKn6LfbcibicXfugdA1OzVSLqQ/640?wx_fmt=png)![](https://mmbiz.qpic.cn/mmbiz_png/WTOrX1w0s54XMawBBGogicB32mB1SmFJ0oOYLsPCP630xfc8XicZPpfkUIwz6ftf8ficPMtDrziaAWrS64NEqicic3WA/640?wx_fmt=png)

登录后，我发现账户似乎具有代理权限，但并没有找到可以上传文件的功能，因此继续寻找潜在的漏洞点。

经过深入探索，我在交易中心的买入和卖出记录部分发现了潜在的漏洞。当点击某条记录的详情时，我尝试抓包分析，发现POST请求中包含一个`id`参数。进一步测试表明，这个`id`参数存在SQL注入的问题。

![](https://mmbiz.qpic.cn/mmbiz_png/WTOrX1w0s54XMawBBGogicB32mB1SmFJ0VXWDQb92VQibzTBGNOgrGl7nnpT1L6IkfhBPlf16yFtOlrpccjibwP6Q/640?wx_fmt=png)

通过分析，确定这是一个时间盲注SQL注入漏洞。通常的响应时间为60秒左右。

![](https://mmbiz.qpic.cn/mmbiz_png/WTOrX1w0s54XMawBBGogicB32mB1SmFJ0MicSV3VFbicpFbcTuem4M7IdMzyBObbRmVucZGMoXrQf10oc3ib9HeY9A/640?wx_fmt=png)

为了验证是否存在时间盲注，我尝试在`id`参数中添加了`sleep()`函数。结果，响应时间明显增加，直接飙升到了5000多毫秒，这进一步确认了漏洞的存在。

![](https://mmbiz.qpic.cn/mmbiz_png/WTOrX1w0s54XMawBBGogicB32mB1SmFJ0fV2IIlm2JicVd4mf0uO2Mb6mN1NDZby5I4p7h5chK6uJUweocTVHazA/640?wx_fmt=png)

本来打算直接使用sqlmap工具进行自动化的SQL注入攻击，但是出现了一些意外情况，无法进行。

![](https://mmbiz.qpic.cn/mmbiz_png/WTOrX1w0s54XMawBBGogicB32mB1SmFJ05cDWx7p8XqoWOnygPvIcSictgNba3ADfaBicJ0tO5tuL8y1oGlL53zkQ/640?wx_fmt=png)

这个操作涉及到的是下面这个页面。

![](https://mmbiz.qpic.cn/mmbiz_png/WTOrX1w0s54XMawBBGogicB32mB1SmFJ0DfdVqrhu8rxBicU8DmagtkQjiaXHcIre0NSB72Xc6iccW1w0IDs1mNAXg/640?wx_fmt=png)我在先知社区找到了一篇相关的文章，并尝试了里面的方法，结果确实有效，运气真好。你可以查看文章以及参考其中的payload形式，文章链接如下：先知社区文章。

```
and if(ascii(substr((/\*!50000%53elect\*/column_name frominformation_schema.columns where table_schema=database/\*\*/() andtable_name='xxxx' limit 0,1),1,1))\>96,1,sleep/\*\*/(5))
```

通过细致的SQL注入操作，我逐步获取了数据库名、表名、字段名以及管理员的用户名和MD5加密的密码。

虽然费了好大劲寻找后台入口却一直未果，最后意外发现可以通过前台登录进入。原来，普通用户或代理账户仅有访问个人中心的权限，而只有拥有超级管理员权限的用户账户才能访问一个名为“管理中心”的区域，从那里可以直接跳转至后台。

![](https://mmbiz.qpic.cn/mmbiz_png/WTOrX1w0s54XMawBBGogicB32mB1SmFJ0NqEa2E4G8oVDXSVbzwmUdNlFwITVvORBdE4iaaHEfAZkHRNVicdgTriaQ/640?wx_fmt=png)

在后台，我发现虽然功能众多，但真正有用的并不多，大部分都与金钱相关。不过，我找到了一个可以上传图片的功能。![](https://mmbiz.qpic.cn/mmbiz_png/WTOrX1w0s54XMawBBGogicB32mB1SmFJ0P5EwdriaXyyz4ktficBBp0vCDj8ay5S5LiamlCyCOia9ibvO8lkcQQrhbpA/640?wx_fmt=png)

利用上传功能变得相对简单，主要有两个原因：一是网站后端编写较为粗糙，二是似乎没有部署WAF或其他文件上传防护措施。

我通过绕过前端的JavaScript验证，直接在网络请求中修改文件后缀，成功上传了文件。上传完成后，系统返回了文件的存储路径。这为进一步操作提供了便利。

## 权限提升

获取webshell后，我尝试进一步深入系统，但发现仅具有列出网站目录的权限，并且无法执行任何命令。这限制了我进一步探索和操作的能力。![](https://mmbiz.qpic.cn/mmbiz_png/WTOrX1w0s54XMawBBGogicB32mB1SmFJ0PeRuOuxezc1JPm1rMQmn2aLVfglSwsqSlb829e17SK43dhvoicJibzmw/640?wx_fmt=png)

从phpinfo的信息来看，服务器过滤了许多关键的PHP函数，这为直接执行命令带来了挑战。

![](https://mmbiz.qpic.cn/mmbiz_png/WTOrX1w0s54XMawBBGogicB32mB1SmFJ0BoIYSErlZF8tBqtNzBr3BaolR9IavQm9xeGuhJglP1qjIm3wHEKiaRQ/640?wx_fmt=png)

为了绕过这些限制，我决定尝试使用蚁剑的bypass插件，特别是针对禁用函数的bypass功能。这个插件可以在GitHub上找到，链接如下：
https://github.com/Medicean/as\_bypass\_php\_disable\_functions

使用蚁剑插件的GC模式后，成功绕过了禁用的函数限制，从而恢复了执行命令的能力。这一步骤为进一步探索和操控服务器提供了更大的自由度。

![](https://mmbiz.qpic.cn/mmbiz_png/WTOrX1w0s54XMawBBGogicB32mB1SmFJ08ic1OXB9wMIPMwOiasyhKcxyWN9q9hpGicfHQoVy22OmEODmvpXPOz7kw/640?wx_fmt=png)

## 追溯黑手

既然已经控制了服务器，接下来的步骤是获取更多关于这台机器的信息。通常，查看 `/var/log/lastlog` 和 `/var/log/wtmp` 文件是一个好方法，因为这些日志文件记录了登录IP地址，可以提供有关系统访问模式的重要信息。

不过，当我尝试查看这些文件时，发现它们竟然全是空的。这一发现确实令人失望，因为这意味着无法通过这种方式追踪到其他可能的入侵者或合法用户的活动，对进一步了解系统安全状态构成了障碍。这种情况可能导致心态有所波动，因为缺乏预期中的信息通常会增加分析的复杂度。

![](https://mmbiz.qpic.cn/mmbiz_png/WTOrX1w0s54XMawBBGogicB32mB1SmFJ0ZqicA8pHI2Wiap3UjbC0Qf47jibXDwOQHKyicFxhNRIN3u2LRpeRr1VzHg/640?wx_fmt=png)

平台的管理似乎非常谨慎，很可能有脚本定期清理日志文件。

接下来，我打算尝试SUID提权。一些常见的可用于SUID提权的命令包括Nmap、Vim、Find、Bash、More、Less、Nano和Cp。推荐访问GTFOBins网站，这里有关于如何利用具有SUID权限的程序的详细信息。

虽然绕过了disable\_function的限制，但出于某种原因，用find命令搜寻具有SUID权限的文件未果，因此我决定手动一一尝试这些命令。尝试多次后，意外发现find命令本身就具有SUID权限，这真是出乎意料。![](https://mmbiz.qpic.cn/mmbiz_png/WTOrX1w0s54XMawBBGogicB32mB1SmFJ03UUlA0CQIY05b1ZH5myDOmctFKyVJlliaiavSq5ek9Urw5mydmIFicjiaQ/640?wx_fmt=png)

提权成功后，虽然我获得了更高的系统权限，但我的主要目标是追溯这台机器所有者的真实信息。以root身份重新检查系统后，依然未能找到有价值的线索。确认在root目录下确实有一个脚本文件正在运行，我决定先终止这个进程，希望有人因此上线来处理问题，从而留下线索。

然而，等待有人上线可能需要很长时间，于是我不得不将注意力再次转回到后台的一些信息上，继续寻找可能的线索。

## 钓鱼黑手

由于通过机器溯源未能取得成果，我决定转向使用钓鱼手段。

在前台的公告和后台设置中，我发现了三个疑似属于开发和运营人员的邮箱地址，决定将它们作为钓鱼攻击的目标。

![](https://mmbiz.qpic.cn/mmbiz_png/WTOrX1w0s54XMawBBGogicB32mB1SmFJ0YCvGd6wGnSzBrjD9oy5N8NXtrltX32cfzeibAp2Qhj7JmXdbibsdHFCQ/640?wx_fmt=png)![](https://mmbiz.qpic.cn/mmbiz_png/WTOrX1w0s54XMawBBGogicB32mB1SmFJ0g3a7ov0AicLDMuwHJy7fwibrnzreUgv9q0m99IfwZcgNWV4qxIicll6YQ/640?wx_fmt=png)![](https://mmbiz.qpic.cn/mmbiz_png/WTOrX1w0s54XMawBBGogicB32mB1SmFJ0FfYxNsiacowib8gVqMMqsSnSehbZBw54T01y2KLLPeZvxsCUr5261dJQ/640?wx_fmt=png)

## 狙击黑手的准备（一）

由于直接从机器追踪未果，我转向制作Word宏进行钓鱼攻击。虽然CobaltStrike简化了宏病毒的制作过程，但它生成宏的方式固定，难以自定义恶意代码，导致恶意代码特征值容易被防护设备如发件服务器、收件邮件网关和本地杀毒软件识别和拦截。

为了确保邮件能顺利送达收件箱，我开始研究免杀技术。了解到常见的邮件处理流程包括：邮件发送到邮件服务器，经过静态查杀、云查杀、行为查杀，最后到达收件箱。邮件服务器通常只进行静态查杀，因此只需绕过这一步骤。

为了规避静态查杀，我选择了自行编写恶意代码的替代方案，使用了名为“EvilClippy”的开源免杀工具，可以在以下链接下载：

EvilClippy

接着，我使用CobaltStrike来生成Office宏病毒。操作如下：打开CobaltStrike，选择“监听器”，点击“Add”添加新的监听器，命名（例如“Office”），设置HTTPHosts为CobaltStrike服务端的IP，并架设在公网上，设置监听端口（例如“8888”）。![](https://mmbiz.qpic.cn/mmbiz_png/WTOrX1w0s54XMawBBGogicB32mB1SmFJ0bNZfhvc7j7xMicOnI1OS45Y4qtianObY07r7UHkZamTUfIAMicmCSxGsg/640?wx_fmt=png)

要在CobaltStrike中生成Office宏代码，请按照以下步骤操作：

1. 打开“攻击”菜单。
2. 选择“生成后门”。
3. 从选项中选择“MS Office Macro”开始生成宏代码。
4. 在随后出现的窗口中，选择你之前创建并激活的监听器。

执行这些步骤后，CobaltStrike将利用选定的监听器配置生成Office宏代码，目的是在目标打开并启用宏的文档时，建立与服务器的连接。

![](https://mmbiz.qpic.cn/mmbiz_png/WTOrX1w0s54XMawBBGogicB32mB1SmFJ0aiboaSWQjT6rh9qLQG6DZFqpQIvFDppj8armPiaLdvSbWETrhdh4Rljg/640?wx_fmt=png)

选择监听器后，单击“Generate”。

![](https://mmbiz.qpic.cn/mmbiz_png/WTOrX1w0s54XMawBBGogicB32mB1SmFJ0COvP56mTbliaDBH9W0BwXxFbTm7yntOIKQz55llw4vDLf...