---
title: 签到免费兑换加油卡、超市礼品卡
url: https://mp.weixin.qq.com/s/Jf8_wjZsHHmc2bkjeVRoQg
source: Doonsec's feed
date: 2026-09-11
fetch_date: 2026-09-12T06:42:43.965661
---

# 签到免费兑换加油卡、超市礼品卡

# 签到免费兑换加油卡、超市礼品卡

原创

x1a0q1
x1a0q1

水哥说安全

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

# 薅 Bing 积分不用手点：我开源了个 Microsoft Rewards 油猴脚本

Microsoft Rewards 这玩意儿，积分能换礼品卡、换会员、抽奖，白给的羊毛不少人都在薅。就是每天那点活儿太碎：签到、PC 搜几次、手机搜几次、几个活动、再读篇文章，天天手动点，烦。

![](https://mmbiz.qpic.cn/mmbiz_png/qicyBphRiciaskwK3QGrU4ulMahIiaVG9YiadsLF5osrym6kxvLeIbVT8enfHvSicHmhHvO8bvk0jGDkMtEdmlpFdGeHlg5htwyQUmCAd4OctgBMA/640?wx_fmt=png&from=appmsg)

我实在嫌麻烦，写了个油猴脚本替我点，顺手开源了。

## 它能替你干什么

说白了，就是替你把 Rewards 页面上那些重复动作点完：

* PC 搜索和移动搜索各跑一轮
* 能认出来的活动任务，自动点
* "每日连续打卡"那一排活动，侧边栏和子卡片挨个过
* 阅读任务
* 活动中途跳页了，回来能接着跑；标签页干完自动关
* 单个活动失败最多重试三次，不会一崩就整批废
* 右下角一个悬浮窗，跑到哪一步、日志都在上面

有个细节我比较得意：搜索它不是瞎敲关键词，而是去拉微博、抖音、百度、知乎这些真实热榜，拿上面的词条去搜。一来更像正常人在搜东西，二来那几下搜索你平时也真能搜到点有用的。搜索之间还塞了随机延迟，PC 五到八秒、移动端二十到三十五秒，不整那种一秒十次的机器节奏。

## 装起来五分钟

前提是先有 Tampermonkey 扩展，浏览器应用商店搜就有。然后：

1. 打开 Tampermonkey 管理面板
2. 新建脚本，或者干脆把仓库里那个 `Get_Microsoft_Rewards_fixed.user.js` 直接拖进浏览器
3. 保存，启用
4. 打开 rewards.bing.com，右侧冒出悬浮窗，就成了

## 怎么用

登录好 Rewards，悬浮窗上三个按钮：搜索、活动、一键全部执行。图省事就点最后那个，脚本按它的流程把搜索、活动、阅读挨个走完。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/qicyBphRiciasktO4A0cAFBdehm4hvEYxFCLn0GiaKrNIaIsTOfPFPKr7j3piaLrN95Vhiaqd0xlklWfkV00sCHAUicRPRtLWwaic126obCH4xF4rbk/640?wx_fmt=png&from=appmsg)

想调节奏，改脚本顶部的 `CONFIG`。默认是每搜满十次自动歇一分钟，活动失败重试三次，这些都能改。首次用我建议先盯着跑一遍，看看你这账号的地区、任务类型跟脚本对不对得上，别一上来就丢后台。

## 提醒

丑话说前头，这类脚本不是稳赚的买卖。

它靠 Bing 和 Rewards 的页面结构吃饭，微软哪天改版，脚本说罢工就罢工，得跟着修。更要紧的是，这毕竟是自动化脚本，踩在服务条款的灰区，积分异常、账号被限都有可能，README 里我也写了免责。要不要用、用多狠自己掂量，别拿主力账号上。

还有两件事别忽略：别在好几个标签页同时跑同一批任务，状态会互相盖；脚本只在你浏览器的登录态下活动，不托管账号、也不往外传凭据，但你自己别把 Cookie、Token、日志截图往公开仓库丢。

## 地址

关注公众号后回复“Bing签到”，获取项目地址。

---

觉得有用？点个关注，持续获取优质内容。

---

延伸阅读：

* Microsoft Rewards：https://rewards.bing.com/

预览时标签不可点

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/4o8NpWgPnzvicMQz0Pib3GZ4SaBpfHMrCZdvaXAEmZ6ia1l954OeKMYXvib1huHKuFQtt4ibtibg71RcRy8eUOFicE7nQ/0?wx_fmt=png)

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