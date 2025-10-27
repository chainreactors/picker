---
title: 苹果、特斯拉均受影响，新型漏洞迫使GPU无限循环，直至系统崩溃
url: https://www.freebuf.com/news/413576.html
source: FreeBuf网络安全行业门户
date: 2024-10-25
fetch_date: 2025-10-06T18:51:40.768232
---

# 苹果、特斯拉均受影响，新型漏洞迫使GPU无限循环，直至系统崩溃

[![freeBuf](/images/logoMax.png)](/)

主站

分类

云安全

AI安全

开发安全

终端安全

数据安全

Web安全

基础安全

企业安全

关基安全

移动安全

系统安全

其他安全

特色

热点

工具

漏洞

人物志

活动

安全招聘

攻防演练

政策法规

[报告](https://www.freebuf.com/report)[专辑](/column)

* ···
* [公开课](https://live.freebuf.com)
* ···
* [商城](https://shop.freebuf.com)
* ···
* 用户服务
* ···

行业服务

政 府

CNCERT
CNNVD

会员体系（甲方）
会员体系（厂商）
产品名录
企业空间

[知识大陆](https://wiki.freebuf.com/page)

搜索

![](/freebuf/img/7aa3bf7.svg) ![](/freebuf/img/181d733.svg)

创作中心

[登录](https://www.freebuf.com/oauth)[注册](https://www.freebuf.com/oauth)

官方公众号企业安全新浪微博

![](/images/gzh_code.jpg)

FreeBuf.COM网络安全行业门户，每日发布专业的安全资讯、技术剖析。

![FreeBuf+小程序](/images/xcx-code.jpg)

FreeBuf+小程序把安全装进口袋

[![](https://image.3001.net/images/20231020/1697804527_653270ef7570cc7356ba8.png)](https://wiki.freebuf.com)

苹果、特斯拉均受影响，新型漏洞迫使GPU无限循环，直至系统崩溃

* ![]()
* 关注

* [资讯](https://www.freebuf.com/news)

苹果、特斯拉均受影响，新型漏洞迫使GPU无限循环，直至系统崩溃

2024-10-24 10:15:47

所属地 上海

![1729740070_6719bd263c662098eb23a.png!small?1729740071759](https://image.3001.net/images/20241024/1729740070_6719bd263c662098eb23a.png!small?1729740071759)

近日，Imperva 研究人员发现了一个名为 ShadyShader 的漏洞。该漏洞允许攻击者反复冻结苹果设备的 GPU，最终可能导致系统崩溃。

研究人员认为，主要问题在于现代 GPU 如何检测和停止无限循环，即如果不终止就会无休止运行的指令序列。虽然 GPU 能够熟练地检测并阻止明显的循环，但研究人员展示了一种方法，即制作一个嵌套循环，并在未被发现的情况下执行。

Imperva 公司的安全研究员罗恩-马萨斯（Ron Masas）尝试制作了一个简单的着色器代码，该代码只迭代大量循环，迫使 GPU 执行大量计算。这种代码可以添加到网站上，使用户系统崩溃。它还可以通过信息、电子邮件和带有恶意链接的 QR 码扫描器发送。如果用户点击链接，浏览器就会加载带有恶意着色器的 WebGL 内容，设备就会进入数字迷宫。这些操作往往都无需用户许可，因为在执行许多常见任务时，GPU 访问都是悄无声息地进行的。

马萨斯表示，驱动程序无法识别着色器不必要地垄断了资源。这使 GPU 不堪重负，无法再管理其他任务，最终导致系统崩溃。

苹果的显示管理服务（macOS 上的 WindowServer 或 iOS 上的 SpringBoard）会等待 GPU 完成任务。当受到 ShadyShader 的攻击时，这个负责管理屏幕的服务就无法获得任何更新，整个系统就会变得很迟钝。

苹果设备内置的计时器可以监控关键进程，确保它们不会耗时过长。120 秒后，该计时器会触发内核恐慌，迫使系统崩溃并重启。在 iPhone 和 iPad 上，计时器的反应速度更快，只需 30 秒。

研究人员指出：在我们的测试中，Macbook 会在 1-2 分钟内完全重启，而 iOS 设备则会在显示锁屏之前的 3-6 分钟内保持无响应状态，在大多数情况下都不会完全重启。

## 尽管打了补丁，问题依然存在

苹果公司早在 2023 年就更新了 GPU 驱动程序来解决这个漏洞，因此运行最新 iOS 和 macOS 版本的用户应该没有问题。但根本问题似乎具有更广泛的影响。

Imperva 警告说：在我们看来，GPU 资源耗尽问题依然存在，并可能在未来的攻击中被利用。我们在其他设备上也观察到了有趣的行为，尤其是在谷歌 Pixel 手机上。

一些机会主义测试显示，Pixel 手机上的浏览器应用会变得无法使用，直到用户重启手机，尽管设备并未崩溃。

甚至在特斯拉汽车上，Imperva 的研究人员也观察到主屏幕在遭遇 ShadyShader 漏洞攻击后暂时无法响应的情况，不过其关键的驾驶功能没有受到影响。

研究人员表示，虽然目前没有测试该漏洞可能带来的全部影响，但所有带有 GPU 和浏览器的系统都可能受到类似的影响。

如果用户发现自己的设备因这种攻击而陷入崩溃循环，可以尝试在打开浏览器之前在设置中禁用 JavaScript，然后关闭有问题的标签页。

> 参考来源：[Flaw crashes Apple devices with a single click, Tesla also vulnerable | Cybernews](https://cybernews.com/security/flaw-crashes-apple-devices-tesla-also-vulnerable/)

# 安全漏洞 # 苹果 # 特斯拉

本文为 独立观点，未经授权禁止转载。
如需授权、对文章有疑问或需删除稿件，请联系 FreeBuf
客服小蜜蜂（微信：freebee1024）

被以下专辑收录，发现更多精彩内容

+ 收入我的专辑

+ 加入我的收藏

展开更多

相关推荐

![]()

关 注

* 0 文章数
* 0 关注者

文章目录

尽管打了补丁，问题依然存在

![](/images/logo_b.png)

本站由阿里云 提供计算与安全服务

### 用户服务

* [有奖投稿](https://www.freebuf.com/write)
* [提交漏洞](https://www.vulbox.com/bounties/detail-72)
* [参与众测](https://www.vulbox.com/projects/list)
* [商城](https://shop.freebuf.com)

### 企业服务

* [安全咨询](https://company.freebuf.com)
* [产业全景图](https://www.freebuf.com/news/307349.html)
* [企业SRC](https://www.vulbox.com/service/src)
* [安全众测](https://www.vulbox.com/)

### 合作信息

* [斗象官网](https://www.tophant.com/)
* [广告投放](https://www.freebuf.com/articles/444331.html)
* [联系我们](https://www.freebuf.com/articles/444332.html)

### 关于我们

* [关于我们](https://www.freebuf.com/news/others/864.html)
* 微信公众号
* [新浪微博](http://weibo.com/freebuf)

### 战略伙伴

* [![](https://image.3001.net/images/20191017/1571306518_5da83c1686dd9.png)](http://www.aliyun.com/?freebuf)

### FreeBuf知识大陆

![](https://image.3001.net/images/20250703/1751535036_68664dbcae34ac40bb9e7.png)

扫码把安全装进口袋

* [斗象科技](https://www.tophant.com/)
* [FreeBuf](https://www.freebuf.com)
* [漏洞盒子](https://www.vulbox.com/)
* [斗象智能安全](https://ai.tophant.com/)
* [免责条款](https://www.freebuf.com/dis)
* [协议条款](https://my.freebuf.com/AgreeProtocol/duty)

Copyright © 2025 WWW.FREEBUF.COM All Rights Reserved
[沪ICP备2024099014号](https://beian.miit.gov.cn/#/Integrated/index) | [沪公安网备
![](https://image.3001.net/images/20200106/1578291342_5e12d08ec2379.png)](http://www.beian.gov.cn/portal/registerSystemInfo?recordcode=31011502009321)