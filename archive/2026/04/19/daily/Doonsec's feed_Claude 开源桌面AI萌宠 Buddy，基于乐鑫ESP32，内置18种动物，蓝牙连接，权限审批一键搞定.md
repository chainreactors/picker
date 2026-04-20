---
title: Claude 开源桌面AI萌宠 Buddy，基于乐鑫ESP32，内置18种动物，蓝牙连接，权限审批一键搞定
url: https://mp.weixin.qq.com/s/NLg70N7hhdcimb3wEdgNfQ
source: Doonsec's feed
date: 2026-04-19
fetch_date: 2026-04-20T04:53:21.960643
---

# Claude 开源桌面AI萌宠 Buddy，基于乐鑫ESP32，内置18种动物，蓝牙连接，权限审批一键搞定

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/0VE9kDxicLUiagzOPSr9m9BJ1aPDXo5l8Y4zeVXztP4fmg6tTaibh8xicZlpXt3oqZJYhNWgcA9bjMVIjZdvpZicKo9hhsVuyWv0pM68r0ib8qd90/0?wx_fmt=jpeg)

# Claude 开源桌面AI萌宠 Buddy，基于乐鑫ESP32，内置18种动物，蓝牙连接，权限审批一键搞定

原创

~
~

IoT物联网技术

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

![](https://mmbiz.qpic.cn/sz_mmbiz_png/0VE9kDxicLUjvdRTkrGRhlWSC7iap5ymwqOTUQUicEgNUibFUyh39LL4n3avYO7ialhZIc1DUmkLtpiapKFmezEJQDNTKpGFfq26ib8BL8EQIldgDw/640?wx_fmt=png&from=appmsg)

> 文末联系小编，获取项目源码

Claude Buddy是一款基于乐鑫 ESP32 的开源物联网桌面AI电子宠物，通过 BLE 蓝牙连接 Claude Cowork 与 Claude Code，它不占地方、安安静静待在桌面，却能实时同步 Claude 状态，充当权限审批小助手，成为你的一位能互动、有情绪的实体小搭档，让你彻底告别只盯着软件窗口的枯燥体验。

Claude Buddy 桌面萌宠内置 18 种 ASCII 小动物形象，每种都有完整动画：睡觉、待机、忙碌、提醒、庆祝、眩晕、心动，循环不重样。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/0VE9kDxicLUg6mCHKFwTRRbD8l7Wvalz7PV8wqw6Cpnt2jLh3sxAXiaiatdj39MmTriaK7RUDBqN0Xv77nlyY5licgJ6BDzja4P4e5rWMqToTPXU/640?wx_fmt=png&from=appmsg)

Claude 桌面萌宠Buddy 会跟着 Claude 的状态自动切换情绪，七种状态覆盖全场景：

* 未连接：闭眼睡觉，安静省电
* 连接等待：轻轻眨眼，四处张望
* 干活中：忙碌流汗，认真工作
* 待审批：LED 闪烁，提醒你处理
* 达成目标：撒花庆祝，超有仪式感
* 摇晃设备：晕乎乎卖萌
* 快速审批：飘出小爱心，治愈拉满不用频繁切窗口，看一眼小硬件就知道 AI 进度，专注不被打断。

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/0VE9kDxicLUjExEfLAdFZH1Do8m6EwjCDaQFC0N5zMSLxebCquuvDmWMA76BJOnerZyq70aicSkWbScmicTLibHzW5yJVtX7Lq1Owl4wQHlIZFc/640?wx_fmt=gif&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/0VE9kDxicLUiaiaAicUde7tJDCdpIOz1XLt0QWYZNicgvOFic4twwk0vgdzr73icYMbciagmeMbZTUrj8fp1a9qic6KPKp39zC2ZVwEJEspVYAQOG6BE/640?wx_fmt=png&from=appmsg)

考虑到续航问题，Claude 桌面萌宠Buddy 屏幕 30 秒无操作自动熄屏，有审批时保持常亮；按键唤醒、翻转休眠、摇晃互动，小细节拉满生活感，放桌面一整天也不耗电。

![](https://mmbiz.qpic.cn/mmbiz_png/0VE9kDxicLUjxbITbLsIibOfclflWBDb2oX77nMZVbibEDfjgs4zjwcqYuvicGAqOz57mDicSXotXqyQDicuG4CJkWURicVj89dwyk17FsxmibrwnLg/640?wx_fmt=png&from=appmsg)

### 通信协议：蓝牙 BLE + Nordic UART Service

### NUS 是嵌入式世界里非常通用的串口转蓝牙方案，Arduino、ESP32、nRF52、树莓派都支持，入门门槛很低。

###

### 通信格式：换行分隔的 JSON

### Claude Desktop 持续往设备推送心跳包，长这样：

```
{"total":3,"running":1,"waiting":1,"msg":"approve: Bash","entries":["10:42 git push","10:41 yarn test"],"tokens":184502,"tokens_today":31200,"prompt":{"id":"req_abc123","tool":"Bash","hint":"rm -rf /tmp/foo"}}
```

字段含义也很清晰：

* `total`：几个 session 在跑
* `running`：正在运行的数量
* `waiting`：等待审批的数量
* `msg`：当前消息
* `entries`：最近操作列表
* `tokens`：总 token 消耗
* `tokens_today`：今日 token 消耗
* `prompt`：有待审批的操作（这个字段出现就代表需要审批）

设备往回发一条 JSON 就能批准或拒绝：

```
{"cmd":"permission","id":"req_abc123","decision":"once"}
```

除了审批流程，还支持把本地文件夹拖拽推送到硬件（比如更新固件资源），以及每次对话完成时的事件推送。协议文档（REFERENCE.md）全部公开，任何能跑蓝牙的设备都可以接入。

值得注意的一个细节：**API 只在开发者模式下开启**，官方明确说这是给创客和开发者用的实验性功能。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/0VE9kDxicLUh9R9cfmSViaaPicmTnz5PzkicrGLFNCiaQvZtib2WPbPOU9JjcXEaeesFQkyDicItAq66vdeBZEnYo5Aq2HSicpUicMmX7rM5hdRN4EIk/640?wx_fmt=png&from=appmsg)

Claude桌面萌宠 Buddy 最戳人的地方，是把冰冷的 AI 交互变得有温度、有画面感。它不复杂、不折腾，却解决了「状态看不见、提醒易遗漏、交互太单调」的小痛点，整个项目全部开源，给创客留足自定义空间。

claude-desktop-buddy 开源项目地址：

https://github.com/anthropics/claude-desktop-buddy

---

如有IoT 源码采购和项目交付需求，请扫码联系小编，微信号: beacon0418

![](https://mmbiz.qpic.cn/mmbiz_png/0VE9kDxicLUiammPZaNSh2HzseQoJ9bNzUSCR9jaK8eBlwD7hS4Qc7LH5ZWOb8IrvxwhaqLcic14VbJIiaWQk4ffEylWbhyeMiaM2q1SaV1EmX40/640?wx_fmt=png&from=appmsg)

[![](https://mmbiz.qpic.cn/mmbiz_png/0VE9kDxicLUgskq8VzxckmN9998ALu5rS2oztQH1K25Dg9soia2ia0gkd7x2AYelfa9HLv70n6ppiaoLbq1n0qSQ6TNoAjof2ibkVoryffJO0gibk/640?wx_fmt=png&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MjM5OTA4MzA0MA==&mid=2454939032&idx=1&sn=5679fa0132dd03f96b7854e02250f5bb&scene=21#wechat_redirect)

[![](https://mmbiz.qpic.cn/sz_mmbiz_png/tnMEWNbfO5cnUxs4P033DlMMqqOLqmN4nJPPZIh6azfSNld68R6DUJneWzEdAm0vHbaGxD8KIQe6hsIV3gRK9Q/640?wx_fmt=png)](https://mp.weixin.qq.com/s?__biz=MjM5OTA4MzA0MA==&mid=2454938828&idx=1&sn=c23447c25873fe4f344373b3b2f5303e&scene=21#wechat_redirect)

**往期推荐**

☞[开箱即用！国产开源30+AI视觉算法IoT智能物联网云平台](https://mp.weixin.qq.com/s?__biz=MjM5OTA4MzA0MA==&mid=2454941969&idx=1&sn=bd91e2bdae181e82774c394c0e709f4b&scene=21#wechat_redirect)

☞[国产开源Web 工业IoT组态软件，支持Modbus、OPC，支持拖拉拽](https://mp.weixin.qq.com/s?__biz=MjM5OTA4MzA0MA==&mid=2454941531&idx=1&sn=dce5163565601e80d153821745715745&scene=21#wechat_redirect)

☞[源码交付，7天完成国产信创部署智慧工地方案](https://mp.weixin.qq.com/s?__biz=MjM5OTA4MzA0MA==&mid=2454940216&idx=1&sn=316b42125f746e16289fe04031496b10&scene=21#wechat_redirect)

☞[4万元，国产信创私有化部署，破解县域无人机AI巡检平台落地难题](https://mp.weixin.qq.com/s?__biz=MjM5OTA4MzA0MA==&mid=2454941157&idx=1&sn=b63f67eb0f573b247f47059347b9e407&scene=21#wechat_redirect)

☞[上班摸鱼， 智能 AI 监控老板行踪](https://mp.weixin.qq.com/s?__biz=MjM5OTA4MzA0MA==&mid=2454932745&idx=1&sn=532fc401409718148a07b35002c40b98&scene=21#wechat_redirect)

☞[免费开源，千知AI知识图谱平台，支持DeepSeek、Qwen](https://mp.weixin.qq.com/s?__biz=MjM5OTA4MzA0MA==&mid=2454944463&idx=1&sn=879157ebcc69d371ad87aa3816db7bc7&scene=21#wechat_redirect)

☞[信创部署，源码交付！县域低空经济无人机 AI 巡检平台](https://mp.weixin.qq.com/s?__biz=MjM5OTA4MzA0MA==&mid=2454944340&idx=1&sn=0bd578639500191483b4c76cc9083052&scene=21#wechat_redirect)

☞[智慧农业大爆发：AI+物联网+区块链重构“天空地”一体化监测](https://mp.weixin.qq.com/s?__biz=MjM5OTA4MzA0MA==&mid=2454944207&idx=1&sn=27aba015734707013b311674825c37cc&scene=21#wechat_redirect)

**免责声明：**本公众号所发布的内容来源于互联网，我们会尊重并维护原作者的权益。由于信息来源众多，若文章内容出现版权问题，或文中使用的图片、资料、下载链接等，如涉及侵权，请告知我们，我们将尽快处理。主理人微信: beacon0418

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/tnMEWNbfO5dAnL0wnu7VicnmWCziaZr42icK2RbNCTV6KezOBgYPIZc7hiaZiaTaUnPZzwShBn7FXicr96iamdc0kKPYw/0?wx_fmt=png)

IoT物联网技术

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