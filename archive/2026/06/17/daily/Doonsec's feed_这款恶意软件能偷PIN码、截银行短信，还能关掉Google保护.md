---
title: 这款恶意软件能偷PIN码、截银行短信，还能关掉Google保护
url: https://mp.weixin.qq.com/s/8dSmK05AbYxKVHBVMOyTew
source: Doonsec's feed
date: 2026-06-17
fetch_date: 2026-06-18T06:48:53.425488
---

# 这款恶意软件能偷PIN码、截银行短信，还能关掉Google保护

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/Cpo2XCpI7K03Sq3kCT1AJ73ddQxnsb9Ch1bY6XeFs5fbXCQicJUEEfFvLOkP8DkenQTCqYy8ib7ouXkEFiaicoROSZfWgnk2Spv45DjUhrhiaGLI/0?wx_fmt=jpeg)

# 这款恶意软件能偷PIN码、截银行短信，还能关掉Google保护

看雪学苑
看雪学苑

看雪学苑

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

如果你的安卓手机最近安装过来路不明的“Chrome更新”或“TikTok破解版”，请立刻检查一下辅助功能权限——因为一款名为 Rokarolla 的新型银行木马，正在通过伪造热门App的钓鱼网站大规模传播。它不是普通的病毒，而是一套完整的“手机控制面板”，让黑客几乎可以为所欲为。

**第一步：披着“谷歌保护”外衣的骗局**

![](https://mmbiz.qpic.cn/mmbiz_png/Cpo2XCpI7K2VATkty1mrHnQia2mErPHp5iaK7dvWavjgWcAMGEckyadTsoWXPSrfW8lLUUULtSSKyIXJH6ayVgicxhnicIbUKaibTfbuIaeA6Cu8/640?wx_fmt=png&from=appmsg)

Rokarolla的入侵从一款投放器（Dropper）开始。这款投放器伪装成谷歌官方的Play Protect安全组件，诱导用户安装。一旦得手，它会立即申请**无障碍服务（Accessibility）权限**——这是安卓系统给予残障人士的辅助功能，但也是木马最爱的“万能钥匙”。

拿到这个权限后，Rokarolla做的第一件事，就是**远程关闭真正的Google Play Protect**，让手机彻底失去官方实时扫描保护。此时，恶意负载已经稳稳扎根在系统里。

**第二步：覆盖层劫持——你输的每一笔账，都进了黑客口袋**

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Cpo2XCpI7K2ZibDPhNlPYp9oyHHM3IoQn6BDvku5bCFTVibYMhkzhfT0ZLbDeyQhuTaydAfkl9gd62UMatT6sBtrR0qEuEcl0icxHD5ibGDicyds/640?wx_fmt=png&from=appmsg)

这款木马最“高明”的手法，是**动态HTML覆盖攻击**。它会从服务器拉取一份包含217个银行和加密钱包App的名单，并针对每个活跃App下载对应的伪造登录页面，存储在本地数据库中。

当你正常打开银行或钱包App时，Rokarolla会**在真页面之上弹出一个一模一样的假页面。**你输入的卡号、密码、支付验证码，全部实时回传。更隐蔽的是，它还会额外覆盖一个**仿冒的安卓锁屏界面**，骗你输入PIN码或图案锁——这样即使手机锁着，黑客也能远程解锁操作。

**第三步：短信、通话、剪贴板——全线失守**

![](https://mmbiz.qpic.cn/mmbiz_png/Cpo2XCpI7K3SX3wpCnwq4h9YthDonXBIgJZyvtD2zZVLnCtvVlV0ynyn9675PjNayCJuaxENkHkaDQyiaiaB6zJAJMeHxib9s54w3IbUkn42Jc/640?wx_fmt=png&from=appmsg)

银行交易往往依赖短信验证码，Rokarolla对此早有对策：

* 读取并发送短信：能截获所有一次性验证码，甚至主动发短信；
* 设为默认短信/电话应用：拦截银行打来的风险警告电话，让你完全不知情；
* 键盘记录+屏幕截图：通过无障碍服务定时截屏（避开会弹出提示的录屏API），压缩成PNG图传走，相当于“无声直播”你的每一步操作；
* 剪贴板劫持：当你复制加密货币钱包地址时，它悄悄替换成黑客的地址，一笔转账就可能血本无归。

**137条指令，比知名木马HOOK更强大**

![](https://mmbiz.qpic.cn/mmbiz_png/Cpo2XCpI7K0xWXH2E3Fjxl4oxHQsmQkstfX6AWOvZn3IOWvxeibYquLjm7M54zx5YcAQjFazhWfsNriaq7raPicPShbxIyFXicNkRGp24Pl5neQ/640?wx_fmt=png&from=appmsg)

安全公司Zimperium的zLabs团队统计，Rokarolla内置了多达137条远程控制命令，超过之前肆虐的HOOK木马（107条）。从开关Wi-Fi、拨打电话、安装应用，到清除数据、上传文件，几乎覆盖了手机的所有功能。

而且它的**C2（命令控制）服务器采用多备用域名机制**，即使封掉一个，也能实时切换到新地址，传统“断网”式拦截效果有限。

**为什么没有“补丁”可打？**

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Cpo2XCpI7K3DEq1S1T4CiaicgqeWPiccIMSOFR9p69PmozluQ38yy6QIfP3xQxQqAYpJDlyQlnGTfsVqNuA0QduQJlKBrtMsOU0aqZntiafAef0/640?wx_fmt=png&from=appmsg)

这是纯粹的恶意软件，谷歌无法通过系统更新来清除它。唯一的防御方式，仍是老生常谈却最有效的几条：

* 只从Google Play官方商店下载应用，拒绝任何第三方网站诱惑；
* 始终保持Play Protect开启，不要因为弹窗提醒就手动关闭；
* 对任何索取“无障碍服务”权限的App保持最高警惕——哪怕是伪装成安全工具，也要立刻拒绝并卸载。

Zimperium表示，其安全产品已能检测该家族，相关入侵指标（IoC）已公开在GitHub仓库中。目前尚未确认Rokarolla归属于哪个黑客组织，但其代码设计明确针对用户最依赖的几道防线——从Play Protect到锁屏密码，全部被逐一击破。

*资讯来源：Zimperium zLabs安全研究报告（2026年6月）*

![](https://mmbiz.qpic.cn/mmbiz_jpg/Cpo2XCpI7K1qZhGltOHQoUJuU5OytkOyIcUcy1foJETda4InjicQMclLndAxEFjwt6EFjBIet3qQEXicjDmxDyicIFZic1IheXzSyMe3aXUX9dc/640?wx_fmt=jpeg&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_gif/Cpo2XCpI7K1UZ4RwLOkCme5UsBF9cNKpHaWeo6Lj3Y3mjFNKlkRQJibvBywJhiaJCNsAHGSC8176ic6KFHtBRPpeqc3QYHSJPJVZ0ficlmnAQI4/640?wx_fmt=gif&from=appmsg)

**球分享**

![](https://mmbiz.qpic.cn/mmbiz_gif/Cpo2XCpI7K399wnqf26BOoFGRpTNhhQXC32lkY6gZqfcx5XPhXpxM8PT8grehQGkuhMd73eiaHERa7x0icv0dQIng3QRUpu0lIe53pBxcWSQ4/640?wx_fmt=gif&from=appmsg)

**球点赞**

![](https://mmbiz.qpic.cn/mmbiz_gif/Cpo2XCpI7K1gIgMdZF9gwTjzvZY0S1py9ics1bUgvM9nYzicSuAgXYtCaiaVsC5DDuqGkAJ5EQm6bDfZzHiavrITqyD1aCOKZQLAbopsjGY3QiaY/640?wx_fmt=gif&from=appmsg)

**球在看**

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/1UG7KPNHN8EGLfh77kFmnicd9WOic2ibvhCibFdB4bL4srJCgo2wnvdoXLxpIvAkfCmmcptXZB0qKWMoIP8iaibYN2FA/0?wx_fmt=png)

看雪学苑

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/1UG7KPNHN8EGLfh77kFmnicd9WOic2ibvhCibFdB4bL4srJCgo2wnvdoXLxpIvAkfCmmcptXZB0qKWMoIP8iaibYN2FA/0?wx_fmt=png)

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