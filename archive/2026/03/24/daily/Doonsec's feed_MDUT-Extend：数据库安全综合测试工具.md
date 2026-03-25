---
title: MDUT-Extend：数据库安全综合测试工具
url: https://mp.weixin.qq.com/s/3jxxsEeJtmaAmGt-nU3-Ow
source: Doonsec's feed
date: 2026-03-24
fetch_date: 2026-03-25T04:12:45.238766
---

# MDUT-Extend：数据库安全综合测试工具

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/x2ibBTFXYHicJqfMHqrOW4uzvHXPfDZx65lC49I5315BDYricObPInn4vYPP7sovlzXWpWKyBveKVS3nubsPibHVx75fYO13yPArgicXZegNribTw/0?wx_fmt=jpeg)

# MDUT-Extend：数据库安全综合测试工具

原创

网安工具库
网安工具库

网安工具库

![]()

在小说阅读器中沉浸阅读

**更多干货  点击蓝字 关注我们**

**注：本文仅供学习，坚决反对一切危害网络安全的行为。造成法律后果自行负责！**

**往期回顾**

·[RzWeb（Rizin）：浏览器端的在线逆向工程平台](https://mp.weixin.qq.com/s?__biz=MzYzNTExNDYwMg==&mid=2247486826&idx=1&sn=7c205514b78c3002d22e12cbafd913a0&scene=21#wechat_redirect)

·[Glato：GitLab CI/CD 流水线的渗透测试框架](https://mp.weixin.qq.com/s?__biz=MzYzNTExNDYwMg==&mid=2247486813&idx=1&sn=7d6a9888840f5a5c20abcec44152c09e&scene=21#wechat_redirect)

·[内网网络审计工具箱（大牛蛙版）](https://mp.weixin.qq.com/s?__biz=MzYzNTExNDYwMg==&mid=2247486807&idx=1&sn=1b567845a716975b6e522377016aa681&scene=21#wechat_redirect)

·[ADPulse：开源的内网渗透和内网安全审计工具](https://mp.weixin.qq.com/s?__biz=MzYzNTExNDYwMg==&mid=2247486788&idx=1&sn=4d49ca2e3b06488b80efb6f9e3c1bed9&scene=21#wechat_redirect)

·[近期你还有这些CTF比赛可以参加](https://mp.weixin.qq.com/s?__biz=MzYzNTExNDYwMg==&mid=2247486793&idx=1&sn=cdb32a1bebeda8c4f670d3528be22d1d&scene=21#wechat_redirect)

·[HackerMind：三AI架构自集成MCP的链上对话智能渗透系统工具](https://mp.weixin.qq.com/s?__biz=MzYzNTExNDYwMg==&mid=2247486640&idx=1&sn=19052c6dd7b1d73d9b8395857276042f&scene=21#wechat_redirect)

**背景分析**

![](https://mmbiz.qpic.cn/sz_mmbiz_png/x2ibBTFXYHicKvAKDKoRZJjJvMog6EO0Cmyic0Js0WFwhsBnVVaHUibLyYicZjjzqy9LlGT4kyiaH4GI8u3Hmfd1KkvQvgqdmVTzRA8WztMtNGB0s/640?wx_fmt=png&from=appmsg)

当前各类数据库广泛应用于业务系统，`MongoDB`、`Redis`、`Oracle`、`Mssql`、`Postgresql`等主流数据库均存在不同类型的安全漏洞与配置风险，针对数据库的安全测试需求持续提升，单一功能的测试工具难以满足多样化的检测需求。`MDUT-Extend`作为`MDUT`的扩展增强版数据库安全测试工具，针对主流数据库的漏洞与配置问题进行功能开发，新增多项数据库利用与检测能力，修复原有版本存在的功能缺陷，优化工具运行依赖与交互界面，能够为授权安全测试场景提供全面的数据库安全检测支持，有效辅助安全人员验证漏洞与排查风险。

**安装介绍**

```
地址：https://github.com/DeEpinGh0st/MDUT-Extend-Release
```

工具依赖相关运行环境，使用前需配置`java`依赖配置，直接`java -jar`文件名`.jar`启动

工具具备图形化交互界面，完成环境配置与文件部署后，可直接启动运行，原文未提供具体的终端启动命令。

工具开发过程中借助`AI`辅助完成代码编写，V1.3.0版本优化了整体代码结构与`UI`界面，提升了工具运行稳定性。

工具启动后，图形界面正常加载即为安装与配置成功，原文未提及具体的验证命令与异常解决方案。

功能介绍

`MDUT-Extend V1.3.0`版本为数据库安全测试工具，所有功能仅限授权合法的安全测试场景使用，禁止用于非法入侵与未授权检测，工具无明确公开的使用代码说明。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/x2ibBTFXYHicLqibzKJUpkLmticty9Oh7nia7C6Tb8GUcSSafNe4k9icibBmdllxaYhGmvbicoQUSUaHPgrNFoUdwLRlnlibTah79oVq1e1BJY69qYPA/640?wx_fmt=png&from=appmsg)

工具新增`MongoDB`数据库利用功能，支持针对`MongoDB`的安全测试与漏洞验证，同时新增数据库存活扫描功能，可快速检测目标数据库的运行状态。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/x2ibBTFXYHicK36laycnV9H5kQwADoBr2wKHYfkHPobdcv2h8rmfS7D141gtCpG29ibWDojsHe8KX2zibXIGZLkSNLUp6hDxJWFe8REG1POCmXY/640?wx_fmt=png&from=appmsg)

工具完成`Redis`漏洞利用功能增强，适配更多`Redis`相关安全测试场景，新增`Oracle`数据库大文件传输功能，满足`Oracle`数据库的文件操作测试需求。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/x2ibBTFXYHicJHcGFg5KVLP8HtfB1icDehE2sc1UVKcyqIdmOJWYSSCibZicXHyX6UtmpR6ibuj2N30JZoOKecPyBj4AhXZRyXjTkSL3k8wvZ4B2s/640?wx_fmt=png&from=appmsg)

工具新增`Mssql`数据库提权与综合利用功能，可针对`Mssql`数据库进行权限提升与综合安全测试，覆盖主流商用与开源数据库的测试需求。

工具修复了`Oracle`、`Redis`、`Postgresql`数据库相关功能的多项漏洞问题，解决了原有版本的运行缺陷，优化了工具依赖包，减少了环境配置的复杂度。

工具优化了核心代码逻辑与图形化`UI`界面，提升了操作便捷性与运行效率，V1.3.0版本部分新增功能未完成完全测试，使用过程中可能存在未知问题。

工具整体作用为实现一站式的主流数据库安全测试，涵盖漏洞利用、存活检测、文件传输、权限提升等能力，可辅助安全人员验证数据库漏洞、排查配置风险，为企业数据库安全加固提供测试依据。

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