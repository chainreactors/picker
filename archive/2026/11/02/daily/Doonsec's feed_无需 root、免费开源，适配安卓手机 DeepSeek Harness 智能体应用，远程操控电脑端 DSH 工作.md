---
title: 无需 root、免费开源，适配安卓手机 DeepSeek Harness 智能体应用，远程操控电脑端 DSH 工作
url: https://mp.weixin.qq.com/s/MF19DEnSQj03Cl_m0wrrHg
source: Doonsec's feed
date: 2026-11-02
fetch_date: 2026-11-03T08:45:48.331508
---

# 无需 root、免费开源，适配安卓手机 DeepSeek Harness 智能体应用，远程操控电脑端 DSH 工作

# 无需 root、免费开源，适配安卓手机 DeepSeek Harness 智能体应用，远程操控电脑端 DSH 工作

原创

~
~

IoT物联网技术

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

![](https://mmbiz.qpic.cn/mmbiz_jpg/0VE9kDxicLUj8VrEq5JBFpEbkBXZf5nL9Rj797VxTpiaicyqU00ZgYVAS1KKza5eFQ4eNcvn2EgUUia1HDJxSLKlnyJU716ibgGLE4nHCw0icW6Dc/640?wx_fmt=other&from=appmsg)

> 适配Android手机、无需 Root、内置 Linux 环境

DSH Go 是基于 DeepSeek Harness 的免费开源第三方 DSH 引擎应用，适配 Android 8.0 及以上安卓手机，提供聊天界面、本机运行环境和远程连接，DSH Remote 当前只支持图片附件，不能在 App 内打开网页版，插件管理限于开关，且不支持 DS Bot 和对话日志导出。

本地运行：在 App 内安装 Ubuntu、Node.js 与 DSH 运行环境，无需 Root 权限。

远程连接：通过 SSH 或 DSH Remote 使用电脑、服务器上的 DSH。

聊天与工具：切换模型，发送图片、使用语音输入，处理工具审批和提问；支持聊天界面与网页模式。

插件界面：使用适配 DSH Go 的原生工具卡、表单和面板；仓库提供 SDK、教程和示例。

手机操控：在你开启权限后，让本机引擎读取屏幕、点按和输入，并可随时停止。

分享与外观：分享、导出和回放对话，调整主题、图标和桌宠。

数据与权限：模型请求会发送给你配置的提供方。开启手机操控后，任务需要的屏幕文字可能发送给模型，支持看图的模型也可能收到截图。

**01**

**DSH Go 功能演示**

![本机对话、切换主机、电脑上的对话](https://mmbiz.qpic.cn/mmbiz_jpg/0VE9kDxicLUjVnDmrrcXu9iaiasE0NDRKQwrIPYibB2YtG8w2RmqicUVoQVWyyI0a1IE6ROJRiasaEDcQXYicn6hXN8HLqKfe7NALTr2AK0I2BUukc/640?wx_fmt=other&from=appmsg)

内置 Linux 环境，免 Root、免 Termux，本机运行，也能遥控电脑。

![生成中排队一条消息；完成后过程折叠](https://mmbiz.qpic.cn/mmbiz_jpg/0VE9kDxicLUgH6EAvMm9augv0W0CPe6EK2W3T5Pzpo2bJ5XpBLqAXEykGlgR44Bibibdrl8aNaiaE5C7pVnq90mtvZcH9rBL2uNEpto1pepiciaGw/640?wx_fmt=other&from=appmsg)

回复中途也能插话，排队的消息随时「立即发送」。插话、打断，过程自动收好，折叠成一行。

![同一段对话的原生界面与网页版](https://mmbiz.qpic.cn/mmbiz_jpg/0VE9kDxicLUgnicic7P5vfotuYVfDQscmftH7QxXIYgiaUCaX3Mx6CySibW7zIoyNwskfN8Ca7hobEJRCPPravDT2WBACVJbobMt1oyhy4IIeb7o/640?wx_fmt=other&from=appmsg)

原生界面，也有网页版和官方网页版一键切换，停在同一段对话，下次打开还是你上次用的那个。

![分享卡、对话回放、我的分享链接](https://mmbiz.qpic.cn/mmbiz_jpg/0VE9kDxicLUjpzjgXziaKkBUx2gaHgIibwYWZCrseva7RnK9VI8jrw8trgDObMOLfEdQ1vZamBDo5YD42yphf4fFg4sZRLDX74gh2GtdVYNKVw/640?wx_fmt=other&from=appmsg)

回复一键做成分享卡。整段对话生成链接，对方在浏览器里回放，链接端到端加密。

![主题设置与两种主题色](https://mmbiz.qpic.cn/mmbiz_jpg/0VE9kDxicLUhf1S3eWkGlTvib28X7OgyII1T79ncrRDutbISsnXo12PdW6iblibERVrw6HJpZFARFfnbiciaALrmuicibtiaUnVg1V3w3uOZfKWmScNQ/640?wx_fmt=other&from=appmsg)

六套主题色，也能跟随壁纸或自选颜色。四款桌面图标，三种功能图标风格。

![手机操控与确认方式](https://mmbiz.qpic.cn/sz_mmbiz_jpg/0VE9kDxicLUjntKmr1TichCjeJg0lprggGXgxkFibM66NiaQO8ohkYicmXlItnqHvGNlg3RGbJVHFxd8PNg7iaCNDBN0Iofg3WB67m5727tkIsB90/640?wx_fmt=other&from=appmsg)

手机操控严把安全关，看屏幕、帮你点，三档确认随你选。付款、密码和验证码，永远交还给你。

**02**

**快速开始**

![](https://mmbiz.qpic.cn/mmbiz_png/0VE9kDxicLUiaAtzOdg2sPLnuxXoibGtuicAGtdFiaYBBCz0h1T3Ias8u274hImwibVMViciclyMSibUc0ZMsG6W4Hibn9fcc3nQI1mBtSIQy7EfIPS0Q/640?wx_fmt=png&from=appmsg)

你可以从 GitHub Releases 或官网下载页获取最新版 APK，常见手机选 arm64 包，也可以从源码构建：

```
git clone https://github.com/ccch1mneyyy/dsh-go.git
cd dsh-go

bash tooling/setup-toolchain.sh
source tooling/env.sh
flutter --version
java -version

bash runtime/build-runtime.sh arm64-v8a
DSH_BETA_TOKEN_FILE= bash tooling/build-apk.sh -f arm64 --keep-daemon
```

工具链脚本会下载 SDK/NDK 与模拟器镜像，并执行 Android SDK 许可接受步骤。默认安装到 ~/dev；可通过 DEV\_ROOT 指定独立目录。脚本会复用已有安装，构建前请核对版本。

| 路径 | 内容 |
| --- | --- |
| `app/` | Flutter 界面与 Android Kotlin 平台实现 |
| `packages/dsh_client/` | DSH Web API 的 Dart 客户端 |
| `packages/dsh_remote/` | DSH Remote 的 Dart 客户端 |
| `runtime/` | Linux 运行时打包、引擎补丁与 App 桥接 |
| `sdk/plugin-kit/` | 原生插件作者工具包；在仓库中使用，未发布到 npm |
| `examples/plugins/` | 插件示例 |
| `docs/guide/` 、`docs/plugins/` | 用户指南与插件开发文档 |
| `docs/assets/` | 本页用到的展示图、桌宠动图和社群二维码 |
| `tooling/` | 工具链、APK 构建与诊断脚本 |
| `services/` 、`site/`、`infra/` | 配套分享服务、网站和部署材料 |

如果你想手机远程操控电脑上的 DSH，随时随地处理电脑里的文件和任务，就切到远程模式。

![](https://mmbiz.qpic.cn/mmbiz_png/0VE9kDxicLUgHQfxSiaMiaDJfnd4NGPH4gN9KOkAzabdVsJI8j1eHvzdPQhMRECSy44XNiaR5LSHVg4XiaDia1vjjphXu3b16Zg1Dhib4GSe1TViaYc/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/0VE9kDxicLUjeheiapk9j5t8fkZWZvibmTlDH52MGAPkUWhAaSUiciaCzfBWBxib2G7mbZwh0c13d8RicichtaMXhnSFm0IdUtWP8qSfIE6YAHdIWq0/640?wx_fmt=png&from=appmsg)

首先，在电脑端安装 ds-harness-remote 插件 ，然后在手机，点开左上角的菜单，再点左下角的“本机”，选择“连接电脑或服务器”，和电脑端登录同一个账号即可。

如果你想让DSH Go 自动操作你的手机，需要先切回本机，进入设置、手机操控，打开手机操控开关，就可以开始读屏幕内容了。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/0VE9kDxicLUjiaemx22AKAWvKRriaI5rjxMdroByNl7FphlJFEwwOfzVzvnMcicJACc49ic1BH7CrDzc3g0TAS4wTCN6iaicLG0JPX1rQBokSa2w0A/640?wx_fmt=png&from=appmsg)

你就可以通过对话让DSH Go操作手机App了，比如打开淘宝，找到搜索框，输入AI 录音卡，再进店选商品，加入购物车，下单。

**03**

**写在最后**

![平板与横屏手机](https://mmbiz.qpic.cn/mmbiz_jpg/0VE9kDxicLUhia6BXtLaaNrrGF1FPPordUQxesk8GyBedYOtGLIkPUbXtU3lp9ZLIr5wU39KYMQVxbXvmbXiayfLDtEyOEtx7mGQwbIibE4ByicQ/640?wx_fmt=other&from=appmsg)

有了 DSH Go 当你离开电脑以后，也能接着在手机App上跟进状态，不用换手机，也能免费获得类似豆包 AI 手机 自动操作体验。

那么，你安装 DSH Go 了吗？

Github 项目：chinaywx/dsh-Go

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