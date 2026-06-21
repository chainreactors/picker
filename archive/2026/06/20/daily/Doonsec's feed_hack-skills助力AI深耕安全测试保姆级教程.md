---
title: hack-skills助力AI深耕安全测试保姆级教程
url: https://mp.weixin.qq.com/s/gPxm7q-beih_xFlDi-kAaQ
source: Doonsec's feed
date: 2026-06-20
fetch_date: 2026-06-21T06:45:16.792997
---

# hack-skills助力AI深耕安全测试保姆级教程

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/xY9ZTT0gDw7DiageW0R8wlAhQfWkPfDASB95iaHicibX4iaJBcaYZ65Sh3j8MRgWVjjhMh2IQWLmL6Vo3Fnmk7o9ib0N4Jciacu2zqK7ZLngJ0un5A/0?wx_fmt=jpeg)

# hack-skills助力AI深耕安全测试保姆级教程

原创

huan666
huan666

huan666

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

一、前言

这是一个面向 Agent 的安全技能知识库，覆盖 Web 安全、API 安全、认证与授权、操作系统提权（Linux/Windows/macOS）、Active Directory 攻击、移动安全、二进制漏洞利用（Pwn）、逆向工程、密码学攻击、区块链与智能合约安全、AI/ML 与 LLM 安全、网络协议与横向移动、数字取证——服务于漏洞赏金、渗透测试、CTF 竞赛和授权安全研究。

二、配套工具

```
trae：https://www.trae.cn/hack-skills：https://github.com/yaklang/hack-skills/
```

三、工具配置

下载并安装trae，详细安装步骤参考之前文章

[基于Trae的AI自动化安全测试实战总结](https://mp.weixin.qq.com/s?__biz=MzkzMjk5MDU3Nw==&mid=2247484740&idx=1&sn=3a62e0cc4905d77278ea557791c2c20e&scene=21#wechat_redirect)

安装hack-skills目录下的所有skills，下载然后进入到hack-skills目录，执行命令进行安装

hack-skills目录结构

![](https://mmbiz.qpic.cn/sz_mmbiz_png/xY9ZTT0gDw5sa2lRdiaM2T8YIriaWNKNpibN2M4Fjkma24AbDVibZPicLdFP3V5SDkBrhRFyuElSDcTJtvWkx0voicLQiac7V5Kmk8rzeGtWjZa4go/640?wx_fmt=png&from=appmsg)

```
npx skills add ./skills --agent trae trae-cn -g -y
```

安装hack-skills

![](https://mmbiz.qpic.cn/sz_mmbiz_png/xY9ZTT0gDw5VKj8WkKsxNQXbU05WvtEjC1zVg2Mbm4YhaI2Udj3yh3bib3aaKoqIqolFpWpkXibjpibUsBJW91jL687Jzogvry4YFA5FfV1vv4/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/xY9ZTT0gDw5lgeAiaMWqrmViaMmXX3r1a3YyvNr5AUrHozaibzL5TUNjzXeylicHZZSicSIj8bFQsSiama7N78ibGv4hic8icEpXKlRVr8SUSH5xBibicA/640?wx_fmt=png&from=appmsg)

四、hack-skills主要入口

| 类型 | Skill | 用途 | 何时优先使用 |
| --- | --- | --- | --- |
| 总入口 | hack | 全局路由、阶段判断、跨类别切换 | 新目标、未知攻击面 |
| 分类入口 | recon-for-sec | 资产发现、技术识别 | 刚接目标、信息不足 |
| 分类入口 | api-sec | REST、GraphQL、移动端后端路由 | 看到 API 接口 |
| 分类入口 | auth-sec | 认证、会话、OAuth、JWT、授权 | 看到登录、令牌、对象 ID |
| 分类入口 | injection-checking | XSS、SQLi、SSRF、XXE、SSTI、CMDi、NoSQL 路由 | 输入进入解释器 |
| 分类入口 | file-access-vuln | 上传、下载、LFI、路径控制 | 文件操作 |
| 分类入口 | business-logic-vuln | 竞态、价格、流程、状态机 | 业务流程测试 |

官方文档介绍

```
https://github.com/yaklang/hack-skills/blob/main/README_CN.md
```

五、调用hack-skills

输入“/”符号调用skills

![](https://mmbiz.qpic.cn/sz_mmbiz_png/xY9ZTT0gDw5QMdUJ30dYjKJJPzJ6vzRib4BEmGkrlmEwq9l6Hstsghnopnt1icjvCPcNVFrfQiaN6oPM7PunJPp2HMzB4picrYtKeNMQjGg1yRg/640?wx_fmt=png&from=appmsg)

调用总入口

![](https://mmbiz.qpic.cn/mmbiz_png/xY9ZTT0gDw5OHf5eQx2SttRf52NiaRP6l6JEyXCeVKUb94oEjP4QZVpFp5HMYqNQImBzoAsQ2BAQ3cJxJGDtOliamFhr8lbWT8dH0NTekyR84/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/xY9ZTT0gDw7nb0cWUkueaugjWCCfHhzMgKlqlQzOTYRZiaUqgvB4LfjACWYyWszmjibeFMYLN0iaf8MSPxwjicSItEe0WgrsxJTQsnAKLz6zYr4/640?wx_fmt=png&from=appmsg)

调用分类入口

![](https://mmbiz.qpic.cn/sz_mmbiz_png/xY9ZTT0gDw7DregXsQ0H4LPib5E4MzDhcah66Wf4DQFics7Uy80vH4mU5rzaNCd9KsIdKhpmwibl7SDzC64QroiaK1UbWcW1CCm15j0l8s18j2o/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/xY9ZTT0gDw550og0tg0cMxIZStOtSTy7qvSt9FzuHlbGxBY25YRK5yb5zibaUFibWI5G6ZrVJsxNYwwcqPThuz3q1NEAU9rS3y1YFnHW1Mrx8/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/xY9ZTT0gDw4cg7K7drCNqPlMvrVrEPWeNX4FHownQ29oe90bTiaWldsIDqryCANblDQiaktxf3ZDGufb1C2ibl3evaNAWz5iaVOMloFhZvpy7r0/640?wx_fmt=png&from=appmsg)

六、案例演示

利用yakit启动靶场服务

![](https://mmbiz.qpic.cn/mmbiz_png/xY9ZTT0gDw4leoTTZuRibBzbgicTubegra2vLqkHRow9DXfGqkfvxxTmcGSvVcysQNnfaJTTiccbahD6hFZsW4CyeY1eM6nrZibAJDk9TpnybjY/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/xY9ZTT0gDw6ic2SjP8XVU6DX3aYHpBpOB3PexYF8HjnBXMq1SXbZnT8UGDUDpQtmibfJtdJNeN6mY6YQwOvCQSDZGGGNmdfGSIsAsutibH5n3o/640?wx_fmt=png&from=appmsg)

自动化安全测试

![](https://mmbiz.qpic.cn/sz_mmbiz_png/xY9ZTT0gDw4Q2LazUNOKkFib5JJZJMjsPokRusR9kMyaLfpaRc6xrUldBemQhDJV8lB2oZONrrYjxWxHnygMZHFic4MjIUT0pibibRJq9JnFia1s/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/xY9ZTT0gDw7Pon37LAHhF0ILrTUdWvibxfIv6gyxibOHLrez9YVcU1PuBZd9gKFesC5oyiamibibfkhSiaFLIlpoFfAyrOUAO0qzGpQUxkoWtTp5M/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/xY9ZTT0gDw68KdlhSQQzhSR0gdAcnLoDspick3HKNUSIpmpZhL2iaEgDPl5co4UGuS0KMudmH0zjD7XQsu4o1eRrFDn35qJEU1wlo332ET1k8/640?wx_fmt=png&from=appmsg)

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/sz_mmbiz_png/xY9ZTT0gDw6icA95A0DazyibBuBlgxdu0I7Uur9m9tX1sdyI3HkB0MSnTicBxt0hWuSGAm7f3bVUWzO1xGDMlWcNSGYJaqrWJefgrlYtJFCpDY/0?wx_fmt=png)

huan666

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/xY9ZTT0gDw6icA95A0DazyibBuBlgxdu0I7Uur9m9tX1sdyI3HkB0MSnTicBxt0hWuSGAm7f3bVUWzO1xGDMlWcNSGYJaqrWJefgrlYtJFCpDY/0?wx_fmt=png)

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