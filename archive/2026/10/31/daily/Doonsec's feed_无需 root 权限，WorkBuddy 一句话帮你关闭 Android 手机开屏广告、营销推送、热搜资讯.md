---
title: 无需 root 权限，WorkBuddy 一句话帮你关闭 Android 手机开屏广告、营销推送、热搜资讯
url: https://mp.weixin.qq.com/s/9Ppuyjy8hnam9l_xQjBr1w
source: Doonsec's feed
date: 2026-10-31
fetch_date: 2026-11-01T08:19:10.033703
---

# 无需 root 权限，WorkBuddy 一句话帮你关闭 Android 手机开屏广告、营销推送、热搜资讯

# 无需 root 权限，WorkBuddy 一句话帮你关闭 Android 手机开屏广告、营销推送、热搜资讯

原创

~
~

IoT物联网技术

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

![](https://mmbiz.qpic.cn/sz_mmbiz_png/0VE9kDxicLUjgajLkFZ9kHCHYCrFJZPHWgKhChz82If0GpicTgoPlQ8LlribNR6bGnvibVbomppVN1bcLd8ibYcltZRMvPiagiaXJoR3hF0ZMYcCwQ/640?wx_fmt=png&from=appmsg)

> 一句话去除开屏广告、营销推送、热搜资讯

前两天，飞哥给大家介绍过 [WorkBuddy 拯救小米电视，接管 HOME 键，去除开屏广告](https://mp.weixin.qq.com/s?__biz=MjM5OTA4MzA0MA==&mid=2454949607&idx=1&sn=2b853bd47885f901d2c397d879c774a9&scene=21#wechat_redirect)的操作方法，收到了许多读者朋友发来自家电视刷机照片。

手机满屏的广告如何关闭呢？

今天，飞哥给大家介绍使用WorkBuddy 去除国产 Android 手机开屏广告、营销推送、个性化广告跟踪、下拉热搜榜单、负一屏资讯推荐、浏览器开屏广告、摇一摇广告、活动优惠等的方法，无需 root 权限，可以一键还原，安全无风险。

| 类别 | 例子 | 怎么处理 |
| --- | --- | --- |
| 系统广告 | 个性化广告、广告跟踪（OAID）、智能推荐服务 | 系统设置里的开关 |
| 热搜和资讯 | 下拉搜索的热榜、负一屏资讯、浏览器信息流 | 各 App 设置里的开关，浏览器切到简洁首页 |
| 推广位 | 商店的轮播、开屏、悬浮活动、签到福利 | 商店「服务管理」里的开关 |
| 营销推送 | 各 App 的「内容与营销」「活动优惠」通知 | 按渠道关，同一个 App 的订单、快递、更新通知保留 |
| 广告组件 | `com.opos.ads` 、`com.miui.systemAdSolution` 等 | `pm suspend` 挂起，要机主同意 |
| 快应用 | 广告里一点就跳进去的「免安装小程序」 | `quickapp` 检测，`quickapp off` 关闭，见 docs/07-快应用.md |

WorkBuddy 指令

![](https://mmbiz.qpic.cn/sz_mmbiz_png/0VE9kDxicLUhiaQe94iaCx5ya3XpWvqfubYEnoddicXJrB3hxZd9dhuNvJWRpGbhgwvTXscx5s2TrfhxfMxWZ0e8ciaF7nArVCWyyZajU4AsysjU/640?wx_fmt=png&from=appmsg)

打开WorkBuddy，输入指令：请克隆 https://github.com/rddmwmddr/android-ad-cleaner ，读仓库里的 AGENTS.md，然后帮我给连着电脑的这台手机去广告。每一步改之前告诉我要改什么。

**操作过程**

连接手机：打开开发者模式和 USB 调试，用数据线连电脑。客户端里有五个品牌的图文教程。

检测：读取型号、系统版本、机型脚本、快应用和广告组件的状态。只读。

选择：营销通知按渠道列出，服务类渠道默认不勾。快应用和广告组件由你决定。

执行：开始前存一份改动前的快照。执行中显示进度和日志，手机放在一边。

完成：列出每一步的结果。关闭开发者模式，改动保留。「还原改动」可以恢复。

**常见问题**

会影响系统更新和保修吗？

不会。不 root，不解锁，不改系统分区。用到的是开发者选项和系统自带的设置项。

关完还会有广告吗？

会剩一些：浏览器搜索框的轮播热词没有开关；新装的 App 带着广告跟踪和营销通知，装新 App 后跑一次客户端。第三方 App 自己的开屏广告不在范围内。

怎么恢复？

客户端左下角「还原改动」：恢复快应用、恢复挂起的广告组件、重新打开关掉的营销通知。App 里的开关按清单路径打开。

**软件演示**

![](https://mmbiz.qpic.cn/sz_mmbiz_png/0VE9kDxicLUh2c8pekawciaMcHmNEtHETVVaaSGVRBMfEgFLY4I67mOkxge5PWIbfLFEoSMqjp1IwMAwtD3ys7jf0K4VTJVXOhRkWEgKR8icGU/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/0VE9kDxicLUgoYHbI8ICE98PeceIQiamxulapCh67xRa5h7F8yLvibWyN1sunyw0jHBiaj7WesJ5RPOgrGlXVG6EwBThYfvdBWck6gLcfyWR9Q0/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/0VE9kDxicLUh3z8OQnmYzibgGlKpmzM9L3vgk5SY9ErHDLibOcAjTZe6QjiavEQ7iaiadM4GrZiaD8Y8SD2hGial70rRBI6MlS4m71vNa9paTCVQIEk/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/0VE9kDxicLUjsVulDlsRrSsA9fHJtuU0wHkX3gNryyC0c4VRyYibkJibjibwSSqQyjR3C1qVrRicYH7JbFBgvt5ciazoKf3xiaGIClNJXCRoySFXW0/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/0VE9kDxicLUgCibCqvwaXRfLvat4qCiclmHqZsMX9rCDklOZ1licjW1vEMNdvQicEvmnNkjtiaObTRdj9T5NrDGPPX6AvUnwmYUY33PYogOlkEx00/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/0VE9kDxicLUiaGQRE5wmD2XccooFeG6CibZ9LXRFql4hVPJ5E6foxVpXcQwh6fRFBRtqONrB5Xsj1ibt8A5E61nhyc4DnFqNEuheSt0G021KaMI/640?wx_fmt=png&from=appmsg)

**机型适配情况**

![](https://mmbiz.qpic.cn/sz_mmbiz_png/0VE9kDxicLUiaw6wHXNichPa4ib5iap0DLrfRBv5ADRngB0icxMKu6A74aNh6dqTJkrMegZNEJuGOgLxvny0KLfdcyYViaJY6wfoqryfmsMossm7gE/640?wx_fmt=png&from=appmsg)

**开放源码**

![](https://mmbiz.qpic.cn/sz_mmbiz_png/0VE9kDxicLUjGL5vFeOvQmOicT4IpT2ic3ek42A50icz3fNiaBua5cFBiamQgTgLZtJSxdpUuBJibNehF22ebuRxLxEBCwN3TsSKZac2GibkrdQE128/640?wx_fmt=png&from=appmsg)

```
AGENTS.md            给 AI 智能体读的操作规范
CHANGELOG.md         源码更新、验证结果与安装包发布状态
docs/
  00-打开开发者模式.md 带截图的分步教程
  01-准备工作.md      装 adb、连电脑、无线调试
  02-用AI智能体.md    WorkBuddy、Claude Code、Codex、Trae、Cursor
  03-用聊天AI.md      DeepSeek、豆包、ChatGPT
  04-给新机型写脚本.md
  05-还原.md
  06-常见问题.md
  07-快应用.md        什么是快应用、怎么检测和关闭
  08-桌面客户端.md     Mac / Windows 客户端的用法、数据位置、打包
  09-社区问题处理.md   Issue / PR 处理范围及待验证项
  清单/               各品牌的手动清单
prompts/             复制给聊天 AI 的提示词
tool/
  run.py             总入口
  fast.py            读屏、找入口、拨开关的引擎（uiautomator2）
  chan_fast.py       营销通知渠道
  explore.py         新机型探路（实验）
gui/                 桌面客户端（pywebview 界面 + PyInstaller 打包）
recipes/<品牌>-<型号>/recipe.py   各机型的机型脚本
images/              文档配图
tests/               不连接手机的引擎回归测试
```

Github项目：rddmwmddr/android-ad-cleaner

---

点个关注 **🌟，精彩不迷路 ❤️**

**往期推荐**

☞[小赚3万元！全靠这套开源AIoT 企业物联网平台](https://mp.weixin.qq.com/s?__biz=MjM5OTA4MzA0MA==&mid=2454946282&idx=1&sn=ad676c8d5c0785c5915e5c96ba318d82&scene=21#wechat_redirect)

☞[开箱即用！国产开源30+AI视觉算法IoT智能物联网云平台](https://mp.weixin.qq.com/s?__biz=MjM5OTA4MzA0MA==&mid=2454941969&idx=1&sn=bd91e2bdae181e82774c394c0e709f4b&scene=21#wechat_redirect)

☞[国产开源Web 工业IoT组态软件，支持Modbus、OPC，支持拖拉拽](https://mp.weixin.qq.com/s?__biz=MjM5OTA4MzA0MA==&mid=2454941531&idx=1&sn=dce5163565601e80d153821745715745&scene=21#wechat_redirect)

☞[源码交付，7天完成国产信创部署智慧工地方案](https://mp.weixin.qq.com/s?__biz=MjM5OTA4MzA0MA==&mid=2454940216&idx=1&sn=316b42125f746e16289fe04031496b10&scene=21#wechat_redirect)

☞[5万元斩杀线！ 一网统飞无人机AI巡检平台](https://mp.weixin.qq.com/s?__biz=MjM5OTA4MzA0MA==&mid=2454945550&idx=1&sn=403e8d5bad8c53ff1b7514a5e1146255&scene=21#wechat_redirect)

☞[上班摸鱼， 树莓派DIY智能 AI 视频算法监控老板行踪](https://mp.weixin.qq.com/s?__biz=MjM5OTA4MzA0MA==&mid=2454932745&idx=1&sn=532fc401409718148a07b35002c40b98&scene=21#wechat_redirect)

☞[免费开源，千知AI知识图谱平台，支持DeepSeek、Qwen](https://mp.weixin.qq.com/s?__biz=MjM5OTA4MzA0MA==&mid=2454944463&idx=1&sn=879157ebcc69d371ad87aa3816db7bc7&scene=21#wechat_redirect)

☞[信创部署，源码交付！县域低空经济无人机 AI 巡检平台](https://mp.weixin.qq.com/s?__biz=MjM5OTA4MzA0MA==&mid=2454944340&idx=1&sn=0bd578639500191483b4c76cc9083052&scene=21#wechat_redirect)

☞[智慧农业大爆发：AI+物联网+区块链重构“天空地”一体化监测](https://mp.weixin.qq.com/s?__biz=MjM5OTA4MzA0MA==&mid=2454944207&idx=1&sn=27aba015734707013b311674825c37cc&scene=21#wechat_redirect)

☞[一站式AIoT视频聚合平台，适配国标28181和国密35114协议](https://mp.weixin.qq.com/s?__biz=MjM5OTA4MzA0MA==&mid=2454946211&idx=1&sn=0072cf454ac83d98adb64c5767e58901&scene=21#wechat_redirect)

☞[“空中奇兵”无人机多光谱罂粟巡查平台，识别出苗期、花期、果期](https://mp.weixin.qq.com/s?__biz=MjM5OTA4MzA0MA==&mid=2454946024&idx=1&sn=6b7d30937351bcce27a0d930c5727726&scene=21#wechat_redirect)

**免责声明：**本公众号所发布的内容来源于互联网，我们会尊重并维护原作者的权益。由于信息来源众多，若文章内容出现版权问题，或文中使用的图片、资料、下载链接等，如涉及侵权，请及时告知，我们将尽快处理。

预览时标签不可点

阅读原文

不喜欢

![]()

微信扫一扫
关注该公众号

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/tnMEWNbfO5dAnL0wnu7VicnmWCziaZr42icK2RbNCTV6KezOBgYPIZc7hiaZiaTaUnPZzwShBn7FXicr96iamdc0kKPYw/0?wx_fmt=png)

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