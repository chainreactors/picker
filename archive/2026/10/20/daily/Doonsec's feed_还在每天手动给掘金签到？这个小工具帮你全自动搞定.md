---
title: 还在每天手动给掘金签到？这个小工具帮你全自动搞定
url: https://mp.weixin.qq.com/s/I9FJ54pRhj3-t9i9lbZJpw
source: Doonsec's feed
date: 2026-10-20
fetch_date: 2026-10-21T06:48:26.098337
---

# 还在每天手动给掘金签到？这个小工具帮你全自动搞定

# 还在每天手动给掘金签到？这个小工具帮你全自动搞定

原创

didiplus
didiplus

攻城狮成长日记

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

开源工具预计阅读 6 分钟 · 共 2175 字

还在每天手动给掘金签到？这个小工具帮你全自动搞定

一次配置，永久托管，矿石天天涨

#掘金#Playwright#自动化#Python

READING PATH

阅读路线

8 个章节

01

先说痛点，看你中招没

-

02

它能干什么

-

03

技术上的小聪明：不逆向，借 SDK 的手

-

04

三步上手，真的不复杂

-

05

邮件通知：每天一封战报，仪式感拉满

-

06

部署方式任你挑

-

07

几点风控提醒

-

08

写在最后

每天打开掘金第一件事就是签到、抽奖、查矿石……一天不落，生怕断签。但说实话，谁记得住啊？今天给大家安利一个折腾出来的小项目——掘金每日签到 + 抽奖自动化工具，挂上去就忘掉它，矿石天天涨。

![](https://mmbiz.qpic.cn/mmbiz_jpg/kztGyHFwmfxgRb1GU8NBFd57tncffwK2CAAO0aE5Nv9EZp2PrdbEiawKXOmd18Xm9L3GfXeyYYtzMDUVhaQEqBECNqmpibuDQbUW8gkGKaSu4/640?wx_fmt=jpeg&from=appmsg)

CHAPTER 01

**01****先说痛点，看你中招没**

用掘金的朋友应该都懂那套日常仪式感：打开掘金 → 点签到 → 领矿石，顺手再抽个免费奖，偶尔看一眼矿石攒到多少了。

听起来不复杂，但问题在于：

●**容易忘** —— 周末一放松，断签三天，欲哭无泪

●**多账号更惨** —— 小号也要签，切来切去烦死人

●**手动太低效** —— 每天花五分钟做重复劳动，程序员不能忍

于是就有了这个项目。**一次配置，永久托管，签到抽奖矿石查询一条龙，完事还发封邮件告诉你今天战果如何。**

CHAPTER 02

**02****它能干什么**

一句话概括：**把掘金成长体系的每日任务全自动化。**

自动签到免费抽奖矿石查询多账号邮件通知灵活调度扫码登录

具体来说：

●✅ **自动签到** —— 每天定时签到，失败自动重试 3 次，稳得一批

●🎁 **免费抽奖** —— 签到完顺手把免费抽奖次数用掉，不浪费每一次机会

●💎 **矿石查询** —— 实时查当前矿石余额，心里有数

●👥 **多账号托管** —— 一个配置文件管所有账号，账号间随机抖动，不扎堆

●📧 **邮件通知** —— 每次跑完发一封漂亮的 HTML 邮件，躺床上看战报

●⏰ **灵活调度** —— 单次跑、常驻进程、crontab、systemd、Windows 任务计划

●🔐 **扫码登录** —— 内置交互式登录导出 cookie，不用手动抠 F12

CHAPTER 03

**03****技术上的小聪明：不逆向，借 SDK 的手**

这块是整个项目最值得说道的地方，懂行的朋友往下看。

掘金的签到接口带签名校验，请求里必须带上 `a_bogus`、`msToken`、`X-Bogus` 这几个参数，而且是动态生成的。常规思路是硬啃 `webmssdk.js` 把签名算法逆出来——**费时费力，而且掘金一更新算法就全废。**

这个项目换了个思路：

不逆向算法，直接借 SDK 的手

用`Playwright`起一个无头浏览器，加载掘金页面让 `webmssdk.js` 正常注入。然后在页面环境内发起 `fetch` 请求——SDK 会自动给请求加上签名参数，我们啥都不用算。

打个比方：

常规思路

硬逆向

把锁拆了研究内部结构，自己配一把钥匙。费时费力，锁一换就废。

本方案

最小化签名

找到锁的主人，让他帮你开。省时省力，锁换了也不怕。

好处显而易见：

1.不怕掘金更新签名算法——SDK 自己会适配

2.代码量极小——核心逻辑就几十行

3.维护成本几乎为零

这是最小化签名方案的精髓：**与其对抗风控，不如顺着它的生态走。**

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/kztGyHFwmfzLWqbzicOT7JFfKicg2QicEZYUygbiamardnbH4t1rtZ1bdRSsFia2gEen9tkT1YxOGDDQSmJP97aGwuaJpdR3bogesdkms3raZz6g/640?wx_fmt=jpeg&from=appmsg)

CHAPTER 04

**04****三步上手，真的不复杂**

QUICK START

三步跑起来

1

安装依赖

pip install 依赖 + playwright install chromium

2

填配置

编辑 config.json，填入账号 cookie 和邮件 SMTP

3

跑起来

python main.py once --all 一键签到 + 抽奖

01

安装依赖

bash

pip install -r requirements.txt

playwright install chromium

02

填配置

编辑 `config.json`，把账号 cookie 填进去：

jsonc

{

"accounts": [

{

"name": "我的主号",

"cookie": "sessionid=xxx; ...",

"ua": "Mozilla/5.0 ..."// 用真实 Chrome UA，防风控

}

],

"email": {

"enabled": true,

"smtp": {

"host": "smtp.qq.com",

"port": 465,

"user": "you@qq.com",

"password": "授权码",

"to\_addrs": ["you@qq.com"]

}

}

}

💡 cookie 怎么拿？浏览器 F12 → Application → Cookies，复制掘金域下的那串就行。项目还自带 `login` 命令，扫码登录自动导出 cookie，连复制都省了。

03

跑起来

bash

# 签到 + 抽奖，所有账号

python main.py once --all

# 挂成常驻服务，每天 06:00 自动执行

python main.py schedule --all

![](https://mmbiz.qpic.cn/mmbiz_jpg/kztGyHFwmfxwEdia4aYQK0y3J8L1ZQIl7A2HuuWXU5icfzRPibdnoia1PCC3nBxm5VBxquJiaowM8mw60xlAibufazAib8ksZ2Ej4PHGVJiaSMO0iawY/640?wx_fmt=jpeg&from=appmsg)

完事。去喝杯咖啡，等邮件通知。

CHAPTER 05

**05****邮件通知：每天一封战报，仪式感拉满**

这是我个人最喜欢的一个功能。每次执行完，会收到一封排版精致的 HTML 邮件：

●顶部掘金蓝渐变标题栏

●三栏统计：成功 / 失败 / 总计，一眼看清

●每个账号一张卡片，签到状态、积分变化、抽奖结果、矿石余额，清清楚楚

●抽到奖品还会高亮显示，小小成就感

而且邮件模板是用 Jinja2 渲染的，模板文件单独放在 `templates/` 目录下。想改样式？直接改 HTML 模板就行，不用动 Python 代码。业务逻辑和展示层彻底分离，干净。

![](https://mmbiz.qpic.cn/mmbiz_jpg/kztGyHFwmfyvfS9SMFkImuibWhspVK0rwx1XE2x1WzPlH1TktlFgc3COBE5XXIMXc9HnTU6XXMiaGsTJg4z9dO3xgzibCMiaEKllMBTvqbDKkEY/640?wx_fmt=jpeg&from=appmsg)

CHAPTER 06

**06****部署方式任你挑**

不管你是 Windows、Linux 还是 Mac，都给你照顾到了：

| 平台 | 方式 | 一句话 |
| --- | --- | --- |
| Windows | 任务计划 | 管理员跑 `register_task.bat` |
| Linux | crontab | `./register_cron.sh` 一键注册 |
| Linux | systemd | `sudo ./register_systemd.sh` （推荐，开机自启 + 错过补跑） |
| 全平台 | 常驻进程 | `python main.py schedule --all` |

个人最推荐 systemd timer：**机器重启自动拉起，错过的任务还会补跑**，真正的挂上就不管。

CHAPTER 07

**07****几点风控提醒**

注意

工具好用，但这几句实话要说在前面

#风控#合规

1. **每天跑 1 次就够**，别贪杯短时间反复刷，容易触发风控 2. 多账号之间已加 5~15 秒随机抖动，systemd 还加了 30 分钟抖动，**别自己把抖动去掉**3. cookie 有效期大概 30 天，过期重新弄一下就行 4. 掘金 TOS 其实禁止自动化，**仅供学习交流，使用后果自负**

CHAPTER 08

**08****写在最后**

这个项目说白了就是用最省事的方式解决一个每天都要面对的小麻烦。

技术上的核心思路——不逆向算法、借 SDK 的手完成签名——其实是个挺通用的思路，不止掘金，很多带签名校验的站点都能套这套玩法。感兴趣的同学可以扒一下源码，核心逻辑真的不长。

GET STARTED

准备好告别手动签到了吗？

项目地址关注并私信我

感谢你的阅读与支持！

如果这篇文章对你有帮助，点个「在看」让更多朋友看到～

· 点赞 ·

喜欢就点个赞吧

· 转发 ·

分享给更多朋友

· 推荐 ·

推荐给身边的人

预览时标签不可点

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/OsuOF7sibMYtLPfoEoNn5zJQjy6nMKW0GVf41zsKNsIVKdWJsxm2gSyIToAJOFI8x2wryVm4GqQib0ibno9KzEa9A/0?wx_fmt=png)

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