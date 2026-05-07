---
title: Milesight IP 摄像头漏洞：5 个关键 CVE 导致全球 14,706 台监控设备暴露于风险之中
url: https://mp.weixin.qq.com/s/cUHeCo207MEqWbuWEQQvfQ
source: Doonsec's feed
date: 2026-05-06
fetch_date: 2026-05-07T05:31:26.349738
---

# Milesight IP 摄像头漏洞：5 个关键 CVE 导致全球 14,706 台监控设备暴露于风险之中

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/R98u9GTbBnv0np2Dk8ic0R6icTxnpc3eC2VPpY1VtmPEhEH216tGQicAOgbtu1ybUzEyHs4LN3vhh5cdoZqUBhjLt0tI4jxAYNdeTZBl1zEMyg/0?wx_fmt=jpeg)

# Milesight IP 摄像头漏洞：5 个关键 CVE 导致全球 14,706 台监控设备暴露于风险之中

haidragon
haidragon

安全狗的自我修养

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

# 官网：http://securitytech.cc

安装监控摄像头是为了保障场所安全——但如果摄像头本身成为安全漏洞呢？在82个国家，共有14,706台运行Milesight固件的IP摄像头被发现存在五个严重安全漏洞，这些摄像头由全球各地的OEM厂商和贴牌厂商以各种品牌名称销售，其CVSS评分最高达到9.8分。这些并非隐藏在服务器机房中的不起眼工业设备——它们正守护着全球各地的酒店、仓库、办公室和商业设施，而这项研究揭示了它们究竟存在多大的安全隐患。

![](https://mmbiz.qpic.cn/mmbiz_png/R98u9GTbBnszXaWubWhKKo6ciaIXCX4j8RficA44nE3ldwy7Gib4Eqy9bLYqJ77Oync1zmPVwwmsr8oYOJd5k2JGLxNTH0mVMCicjWp0cwdwWRU/640?wx_fmt=png&from=appmsg)

*首先是****CVE-2026-32644****（CVSS 9.8 — 严重）——所有 82 个受影响产品系列的固件中都存在硬编码的加密密钥漏洞。其次是****CVE-2026-27785****（CVSS 8.8 — 高危）——同样是固件中硬编码的凭据漏洞，影响范围同样广泛。第三是****CVE-2026-20766****（CVSS 8.8 — 高危）——基于堆的缓冲区溢出漏洞，可能导致设备崩溃甚至更严重的后果。第四是****CVE-2026-32649****（CVSS 6.8 — 高危）——通过 Web 界面注入操作系统命令漏洞。最后是****CVE-2026-28747****（CVSS 7.1 — 高危）——通过固件中生成的弱密钥绕过授权漏洞。所有这些问题都会影响同一个庞大的产品系列——MS-C、MS-N、TS、PMC 系列等等——从子弹型摄像机到可视对讲机，涵盖数十条产品线的固件版本。*

**现在到了有趣的部分**——找出究竟有多少此类易受攻击的设备暴露在开放的互联网上。这一切始于一段**YouTube 视频**。在分析 Milesight 摄像头登录页面演示时（没错，有时候最有用的研究就发生在 YouTube 上），

![](https://mmbiz.qpic.cn/sz_mmbiz_png/R98u9GTbBnsNq6iaNWuRicHWdHkse0j8TVXJNkKqsUNkU4E1MLuPITUGjQG7hefjvRU37DNvjHXb9t2P7gR3l4mKdV9D89U0ibNxwoljfcichQg/640?wx_fmt=png&from=appmsg)

页面标题为“Milesight 网络摄像头”——一个简单但实用的起点。将其作为 Modat Magnify 签名运行：

```
web.html~"Milesight 网络摄像头"
```

![](https://mmbiz.qpic.cn/mmbiz_png/R98u9GTbBnuZBvORlsGVVwcakzkRUcv4tfRS8dzWaYQibmEI7CQwtdkqb0ywZicWVYAGjNLicsstJY1KazIJ0y8rEc52oN4g5zxZTjA9ibLbZick/640?wx_fmt=png&from=appmsg)

全球共回收了 2912 台设备。数量不错，但这并非全貌，因为这仅涵盖了仍然带有 Milesight 标识的设备。深入分析相机网页界面的 HTML 源代码，我们发现了一些更有趣的东西——页面代码中存在两个结构标识符 activeDiv 和 activeMask，无论外部显示的品牌名称是什么。这些字符串属于固件的网页界面框架，而非品牌层，这意味着贴牌版本也带有这些标识符。将此改进后的特征码导入 Modat Magnify 后：

```
web.html~"activeDiv" 和 web.html~"activeMask"
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/R98u9GTbBnsI4Nlo0t6IawvibNXQumRKW48iaWXzmykw9Veqm6Otrsuvhg8aRIKibjR5icnSkSPAX5kL7MvBJBhsOnkMoTaficJNBpyIVcZibH7Sc/640?wx_fmt=png&from=appmsg)

调查结果显示，在 82 个国家/地区共有 14,706 台设备被发现存在漏洞——几乎是最初统计数字的五倍。2,912 台和 14,706 台之间的巨大差距本身就说明了问题，而 Modat Magnify 的分析结果更是令人无法忽视——大多数暴露的设备都是 Milesight 的白标产品，经过重新包装，完全不在那些专门搜索 Milesight 漏洞的人员的视野范围内。

**在分析 Modat Magnify 返回的 14,706 个结果时，一个显而易见的问题浮出水面**——其中相当一部分设备根本没有以 Milesight 摄像头的名义出现。不同的品牌名称、不同的徽标、不同的登录页面设计——但底层却运行着相同的 Milesight 固件，并存在相同的五个关键漏洞。这些贴牌产品或许是整个研究中最令人担忧的部分，因为它们的拥有者没有任何理由将自己的设备与 Milesight 的安全公告联系起来。他们不会去搜索，也不会找到相关信息，他们的设备将一直处于未修复状态——并非出于疏忽，而是因为没有人告诉他们自己的摄像头受到影响。

**影响：**监控摄像头一旦遭到入侵，损失的不仅仅是设备本身，还有它所保护的物理空间。在82个国家，有14706台运行存在漏洞的Milesight固件的摄像头可能面临风险，其中许多摄像头还使用了贴牌品牌。全球各地的酒店、办公室、仓库和重要商业设施都处于威胁之下——而且并非以他们预期的方式。

*在一个摄像头应该能看到一切的世界里，五起 CVE 事件证明，最大的盲点就是摄像头本身。*

* ![图片](https://mmbiz.qpic.cn/mmbiz_png/R98u9GTbBnusOGAxd6evbwvXlVKWmd9neea0QmJulVu6mkeoP2gU1e8s4Al8oKtKD7RARVO1rKg4RFv6o8icOr3hkfibQ7TmlWtfKNRUy5Xtc/640?wx_fmt=png&from=appmsg&watermark=1&wxfrom=5&wx_lazy=1&tp=webp#imgIndex=5)

  ![图片](https://mmbiz.qpic.cn/mmbiz_png/R98u9GTbBnvd0WeSicQwuR6MDL9T63icEyMAoTqeBPhfENrYl95nVHXAGue7VYJvSRTaAUb18f1yD59r7OeB9IyoHFpWpicZ04bBibibTkm7nPtE/640?wx_fmt=png&from=appmsg&watermark=1&wxfrom=5&wx_lazy=1&tp=webp#imgIndex=7)

  ![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/vBZcZNVQERHYgfyicoHWcBVxH85UOBNaPZeRlpCaIfwnM0IM4vnVugkAyDFJlhe1Rkalbz0a282U9iaVU12iaEiahw/640?wx_fmt=other&wxfrom=5&wx_lazy=1&wx_co=1&randomid=z84f6pb5&tp=webp#imgIndex=5)

+ 公众号:安全狗的自我修养
+ vx:2207344074
+ http://gitee.com/haidragon
+ http://github.com/haidragon
+ bilibili:haidragonx

+ ![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/vBZcZNVQERHYgfyicoHWcBVxH85UOBNaPMJPjIWnCTP3EjrhOXhJsryIkR34mCwqetPF7aRmbhnxBbiaicS0rwu6w/640?wx_fmt=other&wxfrom=5&wx_lazy=1&wx_co=1&randomid=omk5zkfc&tp=webp#imgIndex=5)

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/sz_mmbiz_png/vBZcZNVQERH8N8KjDo7DwKbNkHbLeSV917gqKcuKHWeINcgDQYWVq7WaRpFQCc3TvfLLJrrjaiaLCElA7oflv0A/0?wx_fmt=png)

安全狗的自我修养

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/vBZcZNVQERH8N8KjDo7DwKbNkHbLeSV917gqKcuKHWeINcgDQYWVq7WaRpFQCc3TvfLLJrrjaiaLCElA7oflv0A/0?wx_fmt=png)

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