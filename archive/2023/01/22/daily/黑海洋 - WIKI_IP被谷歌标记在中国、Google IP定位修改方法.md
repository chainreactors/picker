---
title: IP被谷歌标记在中国、Google IP定位修改方法
url: https://blog.upx8.com/3196
source: 黑海洋 - WIKI
date: 2023-01-22
fetch_date: 2025-10-04T04:33:37.482663
---

# IP被谷歌标记在中国、Google IP定位修改方法

# [黑海洋 - Wiki](/ "黑海洋 - Wiki - 点击返回首页")

# IP被谷歌标记在中国、Google IP定位修改方法

发布时间:
2023-01-21

分类:
[共享资源/Free](https://blog.upx8.com/Free/)

热度:
59358

最近谷歌大幅更新了 IP 库？Luyee 用的甲骨文美国 IP 被谷歌标记在中国北京，韩国 IP 也被定位识别到中国上海，虽然影响不算大，但还是了解到在这种情况下，使用谷歌产品的时候，会受到 IP 所在地区法律/特殊规定的限制，那么使用起来就不那么好用了。

例如使用谷歌搜索时，搜索语言可能会被修改成当地的，那么相应的语言文章其搜索结果排序可能相对靠前，稍微影响搜索结果的准确性。

谷歌类推送广告或其他服务时会以 IP 被标记所在国家/地区为主。那么 Google IP 定位错误，怎么修改呢？请看下文。

## IP 被谷歌标记在中国的表现

1. 访问谷歌 google.com 被重定向，跳转至 google.com.hk
2. 搜索内容结果默认隐藏敏感内容，即开启了安全搜索
3. 注册谷歌旗下产品账号，默认 +86 区号的手机号码
4. [Youtube Premium](https://blog.upx8.com/go/aHR0cHM6Ly93d3cuZWx1eWVlLmNvbS9waGlsaXBwaW5lcy1zcG90aWZ5Lw)，高级账户功能，画中画、后台播放等受限制
5. Youtube Music 可能无法使用
6. 中国地区 Youtube 无广告。IP 被定位在其他国家/地区，Premium 免除广告政策若不适用，会看到油管广告
7. 访问 google.com/maps/timeline 会返回 400 代码错误
8. 打开 youtube.com/red 网页会提示 Youtube Premium 在您所在的国家/地区尚未推出或不提供此服务
9. 谷歌 Play 商店可浏览，但可能无法更新/下载应用

临时解决方案：

1. 访问 google.com 时，地址后加上 ncr，即 google.com/ncr （ncr = no country redirect = 无国家/地区重定向）
2. 在谷歌搜索设置里，SafeSearch 选项选为 Show explicit results

## Google IP 定位修改方法

1：关闭/取消登录了谷歌账户的 APP 定位权限/授权

2：将常用的一个谷歌账号的位置记录功能打开

![IP 被谷歌标记在中国、Google IP 定位修改方法](https://note.lazzman.com:18084/media/202204/2022-04-30_2138540.7168586998421873.png "IP被谷歌标记在中国、Google IP定位修改方法 1")

3：在电脑上打开 Chrome/谷歌浏览器，登录开了位置记录功能的谷歌账号，安装 [Location Guard 拓展插件](https://blog.upx8.com/go/aHR0cHM6Ly9jaHJvbWUuZ29vZ2xlLmNvbS93ZWJzdG9yZS9kZXRhaWwvbG9jYXRpb24tZ3VhcmQvY2ZvaGVwYWdwbW5vZGZkbWpsaWNjYmJpZ2RrZmNnaWE)（也可在其他支持此插件的浏览器使用）

4：打开 Location Guard 插件，选择 Fixed Location，并在给出的地图上单击，即可标记上你想要 IP 所处的国家/地区

![Google IP 定位错误，使用 Location Guard 修改](https://note.lazzman.com:18084/media/202204/2022-04-30_2138540.533299038615381.png "IP被谷歌标记在中国、Google IP定位修改方法 2")

5：转换到 Options 选项，Default level 默认设置为 Use fixed location

6：打开谷歌地图 [google.com/maps](https://blog.upx8.com/go/aHR0cHM6Ly93d3cuZ29vZ2xlLmNvbS9tYXBzLw)，点击右下角定位授权图标，使 google maps 获取当前“我的 GPS 位置”

![Google IP 定位错误，使用 Location Guard 修改 GPS 位置地址](https://note.lazzman.com:18084/media/202204/2022-04-30_2138540.6404691130981292.png "IP被谷歌标记在中国、Google IP定位修改方法 3")

7：[谷歌搜索 my ip](https://blog.upx8.com/go/aHR0cHM6Ly93d3cuZ29vZ2xlLmNvbS9zZWFyY2g_cT1teStpcA)，即可看到谷歌 IP 定位到了刚才地图上标记的位置

![Google IP 定位到美国凤凰城 Phoenix 成功](https://note.lazzman.com:18084/media/202204/2022-04-30_2138540.5838899103347786.png "IP被谷歌标记在中国、Google IP定位修改方法 4")

![谷歌标记中国 IP 如何修改？](https://note.lazzman.com:18084/media/202204/2022-04-30_2138540.24981113860000526.png "IP被谷歌标记在中国、Google IP定位修改方法 5")

关于 Location Guard 插件，由名称可看出来，这是为保护隐私而开发的位置守卫插件。

Location Guard 是在巴黎综合理工学院、CNRS 和 Inria 进行研究的产物。它基于 Miguel Andrés, Nicolás Bordenabe, Kostas Chatzikokolakis, Catuscia Palamidessi 和 Marco Stronati 的作品开发。

Location Guard 实现了一种基于添加二维拉普拉斯分布的噪声的位置混淆技术。这种方法可以被正式证明为提供了一种隐私保证，是差分隐私的一种变体。更多的细节可以在下面的论文中找到。

地理不可辨。基于位置的系统的差异性隐私。
M. Andres, N. Bordenabe, K. Chatzikokolakis and C. Palamidessi.
Proc. of the ACM Conference on Computer and Communications Security (CCS) ’13, ACM, pp.901-914, 2013. [[报告版本](https://blog.upx8.com/go/aHR0cHM6Ly9hcnhpdi5vcmcvYWJzLzEyMTIuMTk4NA)]

### 其他解决方法

我想你也可以通过手机、平板等移动设备，或其他设备来实现上述定位修改类似的操作：找一个可虚拟 GPS 定位的 APP，打开手机的 GPS 定位，将定位修改到指定位置后，在浏览器上打开谷歌地图，让它获取当前位置。

在此网页向谷歌报告 IP 问题：[https://support.google.com/websearch/workflow/9308722](https://blog.upx8.com/go/aHR0cHM6Ly9zdXBwb3J0Lmdvb2dsZS5jb20vd2Vic2VhcmNoL3dvcmtmbG93LzkzMDg3MjI)

[取消回复](https://blog.upx8.com/3196#respond-post-3196)

### 在下方留下您的评论.[加入TG群](https://t.me/).[打赏🍗](/reward.html)

提交评论

* [Post](/author/1)
* [Link](/links.html)
* [工具](https://tools.upx8.com/)
* [关于](/about.html)
* [文库](/WooyunDrops)

[![](/usr/uploads/ypyun.png)](https://www.upyun.com/?utm_source=lianmeng&utm_medium=referral "赞助商")
Copyright © 2024 黑海洋. All rights reserved.
[看雪赞助](https://www.kanxue.com/ "看雪学院赞助")

[浙ICP备2021040518号](http://beian.miit.gov.cn "浙ICP备2021040518号") [Sitemap](sitemap.xml?type=index "Sitemap")