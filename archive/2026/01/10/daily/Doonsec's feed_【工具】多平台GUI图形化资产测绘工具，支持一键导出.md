---
title: 【工具】多平台GUI图形化资产测绘工具，支持一键导出
url: https://mp.weixin.qq.com/s/J2OSg_jkFW876efv-dtY1Q
source: Doonsec's feed
date: 2026-01-10
fetch_date: 2026-01-11T03:36:06.925703
---

# 【工具】多平台GUI图形化资产测绘工具，支持一键导出

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/YxCBEqEyrw0vWfA2cKpVhIxMsRpLiaeyrMvAfPibCdf4gMPoEpmAzVv3AoZUpYu9w1MdJVibico40B5O4ibB7RQlF9g/0?wx_fmt=jpeg)

# 【工具】多平台GUI图形化资产测绘工具，支持一键导出

原创

track

泷羽Sec-track

![]()

在小说阅读器中沉浸阅读

> 声明！本文章所有的工具分享仅仅只是供大家学习交流为主，切勿用于非法用途，如有任何触犯法律的行为，均与本人及团队无关！！！

**往期推荐：**

**[【SRC】金融场景挖掘技巧](https://mp.weixin.qq.com/s?__biz=MzkzNzg4MTI0NQ==&mid=2247488878&idx=1&sn=2bffe97dce5fc3ceedafee8e9b9bbe31&scene=21#wechat_redirect)**

**[【工具】红队集成工具箱-One-Fox-T00ls](https://mp.weixin.qq.com/s?__biz=MzkzNzg4MTI0NQ==&mid=2247488782&idx=1&sn=0405e0d683d472b783d14b76446ddb1b&scene=21#wechat_redirect)**

**[Jsmoke-一款强大的js检测工具，浏览器部署即用,使用方便且高效](https://mp.weixin.qq.com/s?__biz=MzkzNzg4MTI0NQ==&mid=2247486275&idx=1&sn=5b2fe19dc5b5e9f4261fbe1997435e36&scene=21#wechat_redirect)**

**[一款功能强大的红蓝对抗工具Potato Tool-具备免杀,提权,漏扫,内存马生成,ai分析,溯源等高效的网络安全综合工具](https://mp.weixin.qq.com/s?__biz=MzkzNzg4MTI0NQ==&mid=2247485262&idx=1&sn=18ac6ffb1e0bd3a02f80116938ec03e4&scene=21#wechat_redirect)**

**公众号：**

工具获取在公众号后台回复**26110**即可

## 前言

该工具是一款**多源网络空间测绘平台集成化查询工具**，基于 Python（低版本）/QT C++（v4.0+）开发，核心目标是整合主流网络空间测绘平台的查询能力，提供统一的可视化操作界面，降低多平台资产查询的操作成本，提升网络空间资产探测效率

项目地址

```
https://github.com/G3et/Search_Viewer?tab=readme-ov-file
```

## 工具核心功能

**多平台统一配置**：支持 FOFA / 鹰图 / Shodan/Quake/Zoomeye/Censys 的 API / 密钥配置（保存 / 修改），无需逐个平台配置，统一管理凭证。

**可视化操作**：基于 QT 开发图形界面，所有查询结果以表格形式展示，表头加粗、支持翻页，解决命令行查询的碎片化问题。

**效率优化**：

* 多线程处理 GUI 假死问题，提升查询响应速度；
* 支持 iconhash 自动计算（针对 FOFA），输入图标 URL 即可生成可直接查询的 icon\_hash 语句；
* 历史查询记录、自定义窗口管理（如 CTRL+W 关闭 FOFA 页面）。

**数据导出**：支持各平台查询结果一键导出（可自选路径），解决多平台结果单独导出的繁琐问题。

**跨系统兼容**：低版本（v3.0 以下）基于 Python PySide2 实现，支持 Windows（Win7+）、macOS；v4.0+ 重构为 QT C++，保留核心功能的同时优化性能。

## FOFA

* 1.默认展示10000条数据
* 2.支持iconhash查询，输出的iconhash复制到输入框点击查询即可
* 3.点击查询会覆盖已查询的内容

![image-20260110223249407](https://mmbiz.qpic.cn/sz_mmbiz_png/YxCBEqEyrw0vWfA2cKpVhIxMsRpLiaeyrY4tApcF0avTgicHzNibicRErEJSeWiaXQpwNW1DOxU2dG9Ietr3qxZriaibg/640?wx_fmt=png&from=appmsg)

image-20260110223249407

数据导出

![image-20260110223316456](https://mmbiz.qpic.cn/sz_mmbiz_png/YxCBEqEyrw0vWfA2cKpVhIxMsRpLiaeyrrMaMdzX7LtiaOW9N2BzfL8yb1D3IMmXDt7dDib6Gk4webu2VAXJNzsMA/640?wx_fmt=png&from=appmsg)

image-20260110223316456

## 鹰图

* 1.默认展示10条数据，可翻页
* 2.每次查询可以看到消耗积分和剩余积分
* 3.当日重复查询的语句，不会累计扣积分
* 4.点击查询会覆盖已查询的内容
* 5.暂不支持查询iconhash，之后版本可能会新增

![image-20260110223329367](https://mmbiz.qpic.cn/sz_mmbiz_png/YxCBEqEyrw0vWfA2cKpVhIxMsRpLiaeyrMDT6c0WPjiblS1dOOWjX6E5ibjeZqXictcKjB1d9lPo1ibTzqQdYruJ7bg/640?wx_fmt=png&from=appmsg)

image-20260110223329367

数据导出

![image-20260110223341278](https://mmbiz.qpic.cn/sz_mmbiz_png/YxCBEqEyrw0vWfA2cKpVhIxMsRpLiaeyrykGib5ymkZRiakpetzgqQ3M9ohJciatBXNcex6ZSkj4iaZjhB4qDcYZbcA/640?wx_fmt=png&from=appmsg)

image-20260110223341278

## shodan

* 1.默认展示100条，可翻页
* 2.shodan搜索速度可能比其他的空间测绘慢一些，点击查询后没必要再次点击查询，请耐心等待即可
* 3.搜索方法：如果需要搜索shodan语句选择Search方法，如果需要搜索IP选择IP即可，选错可能会影响到搜索结果
* 4.点击查询不会覆盖已查询的内容
* 5.只能导出已查询出来的内容，可能之后版本会解决

![image-20260110223348900](https://mmbiz.qpic.cn/sz_mmbiz_png/YxCBEqEyrw0vWfA2cKpVhIxMsRpLiaeyricFIiaichjibQkVP9Wia7micic6U72dSibLCWE46NfTvgWUexSBd3u7BOt1TiaQ/640?wx_fmt=png&from=appmsg)

image-20260110223348900

数据导出

![image-20260110223400117](https://mmbiz.qpic.cn/sz_mmbiz_png/YxCBEqEyrw0vWfA2cKpVhIxMsRpLiaeyrgRicTnKoO2UZxVWYVe67hiakbta5iafnRN61dAZOD6LWblKU9ibvW3bK4w/640?wx_fmt=png&from=appmsg)

image-20260110223400117

## 360 Quake

* 1.支持360 Quake语法
* 2.默认查询10条，最大500条，可翻页

![image-20260110223406795](https://mmbiz.qpic.cn/sz_mmbiz_png/YxCBEqEyrw0vWfA2cKpVhIxMsRpLiaeyrnjAZzYo2mYbrKWhic4SjQ6lmOgUH46IyJqGJRwjlhk3CicRdbApjnRrg/640?wx_fmt=png&from=appmsg)

image-20260110223406795

数据导出

![image-20260110223424894](https://mmbiz.qpic.cn/sz_mmbiz_png/YxCBEqEyrw0vWfA2cKpVhIxMsRpLiaeyrpCYKYIdb4hblzH5OwEdQDSWd4DNlkOkwboLc07t6nvrYuLBCTIiaUIw/640?wx_fmt=png&from=appmsg)

image-20260110223424894

## Zoomeye 钟馗之眼

* 1.提供三个资产类型，分别是主机设备、关联域名、子域名，默认关联域名查询
* 2.关联域名、子域名默认查询30条，主机设备默认查询20条，可翻页

![image-20260110223430841](https://mmbiz.qpic.cn/sz_mmbiz_png/YxCBEqEyrw0vWfA2cKpVhIxMsRpLiaeyrMiaQTNCmia9NpXSWw4dB9ia9MLowRQLN5S0DiaPzvaaVleXUMtUG6FgdKQ/640?wx_fmt=png&from=appmsg)

image-20260110223430841

数据导出

![image-20260110223438883](https://mmbiz.qpic.cn/sz_mmbiz_png/YxCBEqEyrw0vWfA2cKpVhIxMsRpLiaeyrcMEaZlibSvYWBvyzibm4BzhfMiaketIStKnEWcO6spwCPkSdgJkyyBkDA/640?wx_fmt=png&from=appmsg)

image-20260110223438883

## 语法

包含各大资产测绘搜索语法

![image-20260110223521347](https://mmbiz.qpic.cn/sz_mmbiz_png/YxCBEqEyrw0vWfA2cKpVhIxMsRpLiaeyrkdTtdaicibfz8lfrJSAia0s3HxGNibdMeODTDf9cMC4QOjcavicWgapjicTw/640?wx_fmt=png&from=appmsg)

image-20260110223521347

## 配置

用来配置key信息，从而调用查询

![image-20260110223550015](https://mmbiz.qpic.cn/sz_mmbiz_png/YxCBEqEyrw0vWfA2cKpVhIxMsRpLiaeyrcibTe8zMEXMn7H7LOSVpx3LarZPgVQW7FT1UAuJRiabvBM9zUC36jzSA/640?wx_fmt=png&from=appmsg)

image-20260110223550015

## 知识星球

**可以加入我们的知识星球，包含cs二开，甲壳虫，渗透工具，SRC案例分享，POC工具等，还有很多src挖掘资料包**

![](https://mmbiz.qpic.cn/sz_mmbiz_png/YxCBEqEyrw0vWfA2cKpVhIxMsRpLiaeyrqgAkicKkWiaCwuOY1JwNqZXkBKMPL552ClHlQPaiaqsssgMejz5TpubTg/640?wx_fmt=png&from=appmsg)![](https://mmbiz.qpic.cn/sz_mmbiz_png/YxCBEqEyrw0vWfA2cKpVhIxMsRpLiaeyrOIDK2HcNJuiaQo3ibYCVyXsEQPI71QSOQRGS1ZHMa1VgsAO9PMfNs6kw/640?wx_fmt=png&from=appmsg)![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/YxCBEqEyrw0vWfA2cKpVhIxMsRpLiaeyriauzNOLfqCVRdabumBMjJ8EFcQPCiav56ibiaCicdcDWsS6IHD0OFe4rueg/640?wx_fmt=jpeg&from=appmsg)

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/sz_mmbiz_png/YxCBEqEyrw2ob06EicM7DDKBlMjOVw0mmNOVKLafx8sRvQbcCQ91ACGG0DWnFb85TOIUSQBgWWmibMSa9KiaEfQXA/0?wx_fmt=png)

泷羽Sec-track

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/YxCBEqEyrw2ob06EicM7DDKBlMjOVw0mmNOVKLafx8sRvQbcCQ91ACGG0DWnFb85TOIUSQBgWWmibMSa9KiaEfQXA/0?wx_fmt=png)

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