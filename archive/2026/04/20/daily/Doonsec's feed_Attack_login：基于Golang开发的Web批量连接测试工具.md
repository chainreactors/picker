---
title: Attack_login：基于Golang开发的Web批量连接测试工具
url: https://mp.weixin.qq.com/s/_Wqrc5xtgY3onWwWnvmbwg
source: Doonsec's feed
date: 2026-04-20
fetch_date: 2026-04-21T04:43:33.960898
---

# Attack_login：基于Golang开发的Web批量连接测试工具

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/x2ibBTFXYHicJBhp3phljJwTa2vYLqJFibHAe2L0Dr6P8Cm1vRbuCffK3dN72pMicC2HDTJ7VAG13ZQHQQ9yqiceD2MSen1V824AvK9uIibLHrLQQ/0?wx_fmt=jpeg)

# Attack\_login：基于Golang开发的Web批量连接测试工具

原创

网安工具库
网安工具库

网安工具库

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

**更多干货  点击蓝字 关注我们**

**注：本文仅供学习，坚决反对一切危害网络安全的行为。造成法律后果自行负责！**

**往期回顾**

·[PyGlimmer：Python逆向集成工具](https://mp.weixin.qq.com/s?__biz=MzYzNTExNDYwMg==&mid=2247487068&idx=1&sn=c7e31db8644a1a56beb932b40ef5cd95&scene=21#wechat_redirect)

·[ClarityJS：一款轻量级JavaScript解混淆工具](https://mp.weixin.qq.com/s?__biz=MzYzNTExNDYwMg==&mid=2247487053&idx=1&sn=1eba92a83267ab8c8a2ef8db834a4586&scene=21#wechat_redirect)

·[Burp AI Agent：集成AI能力的Burp Suite安全测试扩展](https://mp.weixin.qq.com/s?__biz=MzYzNTExNDYwMg==&mid=2247487028&idx=1&sn=03f00c9e9169d54f5d4de1187726cc98&scene=21#wechat_redirect)

·[Ai工具辅助CTF小白 自动化做Web题目 Windows可用](https://mp.weixin.qq.com/s?__biz=MzYzNTExNDYwMg==&mid=2247487021&idx=1&sn=1733aea27dba4cf495a521590eb18e42&scene=21#wechat_redirect)

·[Auto-SSRF+SSRFmap：构建SSRF自动化利用链](https://mp.weixin.qq.com/s?__biz=MzYzNTExNDYwMg==&mid=2247487017&idx=1&sn=f5b69619acc08b55db5609767690e077&scene=21#wechat_redirect)

·[蓝队应急响应工具箱](https://mp.weixin.qq.com/s?__biz=MzYzNTExNDYwMg==&mid=2247486994&idx=1&sn=2a9a0e9377d8a6360721c67977ef070e&scene=21#wechat_redirect)

**背景分析**

![](https://mmbiz.qpic.cn/sz_mmbiz_png/x2ibBTFXYHicJ3viciaA2vKuD9gNpuF1KXDibjobyAU9C601AUSvIJVRMJsJ9gn6JE4DYX8gSTegPHotqOXhYbplAgHibJh3mn4LbHPlwuVYhicVEA/640?wx_fmt=png&from=appmsg)

在企业内网安全测试与红队攻防演练场景中，内网资产服务弱口令、未授权访问是高频安全风险，传统手工检测方式效率低下，难以实现批量服务验证，且缺乏统一的可视化管理界面。`Attack_login`工具基于`Golang`开发，专注解决内网多类型服务批量连接测试难题，支持十四种常见服务的批量连接与未授权访问检测，可快速验证内网资产服务可达性与弱口令问题，适配`Windows`、`Linux`、`macOS`多平台环境，为授权安全测试提供高效便捷的技术支撑。

**安装介绍**

```
●●●

地址：https://github.com/ChinaRan0/Attack_login
```

源码编译运行步骤：

```
●●●

git clone https://github.com/ChinaRan0/Attack_login.git
cd attack_login
go mod download
go run main.go
```

工具运行依赖配置文件`config.json`，可修改其中的`password`与`port`参数，默认登录密码为`admin123`，默认服务端口为18921，支持在前端界面配置`SOCKS5`代理参数。

工具启动成功后，在浏览器中访问`http`:`//localhost`:18921即可进入`Web`管理界面，输入配置的登录密码完成验证。

功能介绍

![](https://mmbiz.qpic.cn/mmbiz_png/x2ibBTFXYHicJZzb7BicOpNoqa9O31zR3MlibVgYiamB4OibmiaMTNhX2bAhGmEkjhGw0XoWT3XCaEAHIic1dFzyicgxibiaM8P7aacH7nazJ5hyPePiass/640?wx_fmt=png&from=appmsg)

`Attack_login`具备十四种常见服务批量连接测试功能，同时支持服务未授权访问检测，可满足内网资产安全测试的核心需求。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/x2ibBTFXYHicLVh6fg2pqqKvUyHibBXXicnkIvmfibaooSCAv2KvbGlNfVzyBVP4QqiazT12kqxhHGv6iajSjYerk4NTA2ibAdqy0uaY34l1RYLaews/640?wx_fmt=png&from=appmsg)

工具支持`CSV`文件批量导入目标资产信息，无需手动逐个添加目标，大幅提升大规模资产测试的操作效率。

![](https://mmbiz.qpic.cn/mmbiz_png/x2ibBTFXYHicJylC0ZhPLIkNrs8Iq1LxqPC4TzC0Gibm6cvCib3yKjNIvsoDeC8qnKMs0B0g4R6vibYJsauYLoTkwiaRibDQAylMl1xvkZJFSJ9XAc/640?wx_fmt=png&from=appmsg)

工具提供可视化`Web`管理界面，所有操作均可通过前端界面完成，降低使用门槛，方便测试人员进行操作与结果查看。

工具集成全局`SOCKS5`代理功能，可适配内网穿透等复杂网络环境，满足多样化的内网测试场景需求。

工具针对`SSH`服务支持连接后自动执行命令，可快速获取目标主机的核心信息，提升测试效率。

更多资源欢迎加群讨论

![](https://mmbiz.qpic.cn/sz_mmbiz_png/x2ibBTFXYHicKlShic0cpYzgnOheB3nCvpkx8BfmxFgngjWYiaPW3H9NPbSpzr0WRtJ2DXtUR1YIC0cs1dxPDRIdFEh0lXa5IibE8uiaZlVjLYpBk/640?wx_fmt=png&from=appmsg)

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/x2ibBTFXYHicJVRBMdib7K3ZtqZv8Yl8uRmgwoJjcDRPibW9TfdiaaibJnTboUxTXo5C0iacxMHS0JnjVbGextpYnIfUquG9E3icJmibOWcPSVNJOOIk/0?wx_fmt=png)

网安工具库

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/x2ibBTFXYHicJVRBMdib7K3ZtqZv8Yl8uRmgwoJjcDRPibW9TfdiaaibJnTboUxTXo5C0iacxMHS0JnjVbGextpYnIfUquG9E3icJmibOWcPSVNJOOIk/0?wx_fmt=png)

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