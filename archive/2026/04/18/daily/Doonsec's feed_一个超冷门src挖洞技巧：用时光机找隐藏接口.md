---
title: 一个超冷门src挖洞技巧：用时光机找隐藏接口
url: https://mp.weixin.qq.com/s/gy4hkk-JpZhrXdLJ0lWQog
source: Doonsec's feed
date: 2026-04-18
fetch_date: 2026-04-19T04:50:24.420884
---

# 一个超冷门src挖洞技巧：用时光机找隐藏接口

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/gL9yql6ibrhKD7iacVPnCos2BKib0yXKcfciaup7AzibX38N6X1NJk26v3OfodvVBqX1fQS5Frja0lwickmD5KSpS5ia11OeHoEPRqtsQzm4RJmdkg/0?wx_fmt=jpeg)

# 一个超冷门src挖洞技巧：用时光机找隐藏接口

原创

src大湿
src大湿

鹏组安全

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

分享一个寻找隐藏接口的实战思路，很多人不知道。

核心方法：利用**web.archive.org查看目标站****历史 robots.txt、历史页面、旧接口路径**。

很多站点：

* 新版把敏感接口、后台路径删掉了
* 旧版 robots.txt 里还留着大量未下线接口
* 不同年份暴露的路径完全不一样

操作步骤：

1. 打开 web.archive.org
2. 输入目标站 robots.txt
3. 翻 2020–2026 年历史记录
4. 提取旧路径、旧接口、后台地址
5. 直接访问或批量测试漏洞
6. 演示如下：
7. 2025年与2009年的robots.txt文件内容进行对比，所暴露出来的接口是不一样的
8. ![](https://mmbiz.qpic.cn/sz_mmbiz_png/gL9yql6ibrhLAPKia00vP7dicHUWPJ6TTeWXhhRqJQm0AwXg7pSjCRrkXiaRgUVicYlGu55qMb6zhAeWaI2o9picwxb2szYmbeIbzQV71rib6vvQhg/640?wx_fmt=png&from=appmsg)

   ![](https://mmbiz.qpic.cn/mmbiz_png/gL9yql6ibrhI3ko9eliccWOiaC0b3YC5To4XyFblltUpiawxVIpZ9h0LJ1VYo7OiatdbtvzWPwbyLUt1icBCZWnzwmksFboZe3MypVmo0I9gto0qY/640?wx_fmt=png&from=appmsg)
9. 这个技巧在 信息收集、子域名、隐藏接口、未授权访问里特别好用，很多 SRC 漏洞都是这么挖出来的。

[鹏组安全社区站：您身边的安全专家-情报 | 攻防 | 渗透 | 线索 | 资源社区](https://mp.weixin.qq.com/s?__biz=Mzg5NDU3NDA3OQ==&mid=2247491205&idx=1&sn=b212739965f6617c84c89726cc85d50c&scene=21#wechat_redirect)

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/0YvAy5BgkyNHF1CWPJ9XSApBFhIGwF5Jh0zD2ySOcHvBkYgicU4xZsqvR3XEjUEnfGKH7ya8TgqCibHpYZKcibDBQ/640?wx_fmt=other&from=appmsg&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp#imgIndex=28)

**扫码关注**

**社区**

鹏组安全社区：comm.pgpsec.cn

专注网络技术与骇客的一个综合性技术性交流与资源分享社区

老用户续费88折扣![图片](https://mmbiz.qpic.cn/mmbiz_png/gL9yql6ibrhLhc9ic3aExW7y8pcFF4AFHicSNrzOlf9tsLU2Krt1xsSgicTiaZHaCBBnChkx3ibxpPCAu9pLOy6t2nUyegx5iawicmLl6b1eUoEzcibY/640?wx_fmt=png&from=appmsg&watermark=1&wxfrom=5&wx_lazy=1&tp=webp#imgIndex=3)

社区首页

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/0YvAy5BgkyN92OtiagxgUpDAeq8RbcPacH8L82CwLzHtvucDrP1RrgfzeUYY8cS4WHk8niap3jKZzys9wK5oHB9w/640?wx_fmt=other&from=appmsg&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp#imgIndex=29)

免责声明

由于传播、利用本公众号鹏组安全所提供的信息而造成的任何直接或者间接的后果及损失，均由使用者本人负责，公众号鹏组安全及作者不为此承担任何责任，一旦造成后果请自行承担！如有侵权烦请告知，我们会立即删除并致歉。谢谢！

好文分享收藏赞一下最美点在看哦

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/sz_mmbiz_png/0YvAy5BgkyMD7I0zCGRx4cPrP4o4wlMpgZicY0R4ENahs8NIk1GkREYoIic48qMVebUnzHcaBL0Gzib4mvE9VsibFQ/0?wx_fmt=png)

鹏组安全

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/0YvAy5BgkyMD7I0zCGRx4cPrP4o4wlMpgZicY0R4ENahs8NIk1GkREYoIic48qMVebUnzHcaBL0Gzib4mvE9VsibFQ/0?wx_fmt=png)

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