---
title: 一次隐藏页面泄露导致的未授权
url: https://mp.weixin.qq.com/s/8L86SpB4XrZVJcxsfx5SXw
source: Doonsec's feed
date: 2026-03-21
fetch_date: 2026-03-22T04:13:31.892889
---

# 一次隐藏页面泄露导致的未授权

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/oQ0sWhcqsVn8ZNHHQyQT0Qqrreiazfr9VaylVm7onvJ07LPQo4eMoMuM3xTEp7qVx0NIXy8sKVSzia6zpevRtPY3om5bvPvvB13Ku9uwK5CLQ/0?wx_fmt=jpeg)

# 一次隐藏页面泄露导致的未授权

原创

进击的HACK
进击的HACK

进击的HACK

![]()

在小说阅读器中沉浸阅读

> 字数 471，阅读大约需 3 分钟

## 测试流程

近期做的一个渗透测试项目，客户只提供的资产里仅包含域名，让我们自己信息收集做测试。

其中有一个 Tomcat 搭建的网站，直接访问 http://demo.com:8889/ 显示 403
![7ea496f8ac163cca11d0fd8f962e075d.png](https://mmbiz.qpic.cn/sz_mmbiz_png/oQ0sWhcqsVnPYtfD4RpCsOZSRNCxUvySkR6JOroT5RZI1KFVUKvvDESeDKoSBKTY8RMUlUWcsuTJUGjp5eAIDvBX6d6Mj0G9kaZI4e7EZdk/640?from=appmsg "null")

7ea496f8ac163cca11d0fd8f962e075d.png

随意添加一个子路径，显示 404
![88f3c8dc720e2edc0dcdf43b8c46b8c4.png](https://mmbiz.qpic.cn/mmbiz_png/oQ0sWhcqsVmQYliaQBbCLibOSRq6yOgkZicbVb0NQ4w05w3uKy3oD48du0Rz8wIljzmSeiawiaH7c2NiaBgns6Tc5CW6Xf31YYLPzJeGQLvxHttHk/640?from=appmsg "null")

88f3c8dc720e2edc0dcdf43b8c46b8c4.png

先整理一个常用的子路径字典，用 dirsearch 跑子路径，当子路径存在的时候，虽然也显示 404，但是为 Tomcat 的 404

![2cf1c2e4705c6a4054e2d5afb35c1e80.png](https://mmbiz.qpic.cn/mmbiz_png/oQ0sWhcqsVn0lKf0ZWLGUHXkco7ialvFLMx0LYibMdVQKnD76E3vcbphUa5ANL7HeFuiatXF3qYfoqleQwe6Mhr1jh1kZfCbo9U1QibQHxDYxXM/640?from=appmsg "null")

2cf1c2e4705c6a4054e2d5afb35c1e80.png

说明这个子路径下面的有东西的，继续跑常见的路径字典。

当跑到 swagger-ui.html 的时候，页面 200。
![0bedb179f82fc103e4e14df2dd3ecfa3.png](https://mmbiz.qpic.cn/sz_mmbiz_png/oQ0sWhcqsVk74J89kiblAnXeAmW0spaibw6tkvSy9ADQibFhXtlUajtia7KFMFfxibM4vCGgFYR1RmJIPic2OWlbZWFGg4fpOrP9ytOsHhj53eeSg/640?from=appmsg "null")

0bedb179f82fc103e4e14df2dd3ecfa3.png

但下面先生的并非 swagger 文档以及 api-docs，而是这个系统的首页。

爆破的其他常见路径都显示 404，唯独 swagger-ui.html 报的是 200，返回的主页面。

找了一下规律，发现服务器是匹配到 **-ui.html** 后，判断页面不存在就返回首页，如果页面存在就返回当前页面。

如果不是按照惯例跑 springboot 相关接口字典，还未必能找到。

> 后续提交漏洞时候，和客户沟通。客户说这个系统是门户系统，分对客的页面和管理系统，但他们只用了管理系统，对客的那部分没用。
> 他们以为代码已经删除，但还保留着。

在隐藏的 HTML 页面的 JS 当中，保存着可以未授权访问的 API 接口。

简单跑了点端口，就可以未授权的获取管理系统的用户以及敏感信息。还可以进行任意用户密码重置，从而登录系统。

这个已经废弃的面客网站的 JS 代码里，还有后台的登录地址。拿着跑 API 接口获取的用户，重置密码后成功登录。

## 小结

这次测试运气成分比较大。但结果是好的。

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/a1BOUvqnbrhOdQiaFvupNflYqfzCq5nzdjQF1j9ib5wTPYG8g3txOmd7mu8icbHfWCHTLibYzSOMlRrlLD9EicEESzA/0?wx_fmt=png)

进击的HACK

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/a1BOUvqnbrhOdQiaFvupNflYqfzCq5nzdjQF1j9ib5wTPYG8g3txOmd7mu8icbHfWCHTLibYzSOMlRrlLD9EicEESzA/0?wx_fmt=png)

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