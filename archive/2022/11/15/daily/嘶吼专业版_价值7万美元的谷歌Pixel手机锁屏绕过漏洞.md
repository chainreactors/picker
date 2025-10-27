---
title: 价值7万美元的谷歌Pixel手机锁屏绕过漏洞
url: https://mp.weixin.qq.com/s?__biz=MzI0MDY1MDU4MQ==&mid=2247553752&idx=2&sn=e4018f4129fcb9921f469dbfdf73aa2e&chksm=e915c2e2de624bf47c59126095f4069443a6f3e108b982d3733600818e678de4101e9d2812e9&scene=58&subscene=0#rd
source: 嘶吼专业版
date: 2022-11-15
fetch_date: 2025-10-03T22:46:21.566172
---

# 价值7万美元的谷歌Pixel手机锁屏绕过漏洞

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/wpkib3J60o2952zbOiaalibgKkVlibj2MAns2hpJCfQN0T1j950qpuw6siajshIryHoRvRo9icr0VKcsvkILy1Nv996w/0?wx_fmt=jpeg)

# 价值7万美元的谷歌Pixel手机锁屏绕过漏洞

ang010ela

嘶吼专业版

![](https://mmbiz.qpic.cn/mmbiz_gif/wpkib3J60o297rwgIksvLibPOwR24tqI8dGRUah80YoBLjTBJgws2n0ibdvfvv3CCm0MIOHTAgKicmOB4UHUJ1hH5g/640?wx_fmt=gif)

研究人员发现一种可绕过谷歌Pixel手机锁屏的方法。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o2952zbOiaalibgKkVlibj2MAnsaHIvicemhicQNyscRVNicXz9iaskEsI4BDLc9FnN3ZSPO6ZeO2ulfuIYbA/640?wx_fmt=png)

近日，谷歌修复了一个影响所有Pixel 智能手机的高危安全漏洞，漏洞CVE编号CVE-2022-20465。该漏洞是一个锁屏绕过漏洞，攻击者利用该漏洞可以解锁Pixel 智能手机。

从谷歌官方发布的修复代码分析，该漏洞是由错误翻译SIM改变事件引发的不准确系统状态导致的漏洞，会使得锁屏保护无效。

研究人员称，通过以下步骤可以完全绕过Pixel的锁屏保护：

在锁屏的设备上输入3次错误指纹以禁用生物认证；

在不关机的情况下将手机的SIM卡替换为攻击者控制的SIM卡，并事先设置PIN码；

输入错误的SIM PIN码锁定SIM卡；

设备会要求用户输入SIM卡的PUK码以解锁SIM卡，PUK码是一个8位的数字；为攻击者控制的SIM卡输入新的PIN码；

设定自动解锁。

也就是说，攻击者将自己持有PIN锁定的SIM卡和该卡的PUK码就可以解锁Pixel手机。

攻击者利用该漏洞可以在物理接触受害者手机的情况下绕过手机的锁屏保护，包括指纹、PIN码等。

该漏洞是安全研究人员David Schütz在2022年6月发现的，谷歌于2022年11月安卓月度安全更新中修复了该漏洞。谷歌通过漏洞奖励计划向该漏洞的提交者Schütz奖励7万美元。

完整技术分析参见：https://bugs.xdavidhu.me/google/2022/11/10/accidental-70k-google-pixel-lock-screen-bypass/

参考及来源：https://thehackernews.com/2022/11/hacker-rewarded-70000-for-finding-way.html

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o2952zbOiaalibgKkVlibj2MAnsDJUzqJbEHry5c7R8H7rHamCyH3oiak4vKia8R1FTCe2hTFOMVTHYOPfQ/640?wx_fmt=png)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o2952zbOiaalibgKkVlibj2MAnsm02PyxJCDrQ0mficD0NRMNqPwWvLjM0AFoUP38dHzEyyibKGtXxfGprQ/640?wx_fmt=png)

预览时标签不可点

阅读原文

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o29QZSgjKMjM7j822AuVv1iaicmoBhDlvJq1s41w5yIxoicDK9AsOGHLnQYkqq95ibWgq3OqvvXEO1qBVg/0?wx_fmt=png)

嘶吼专业版

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o29QZSgjKMjM7j822AuVv1iaicmoBhDlvJq1s41w5yIxoicDK9AsOGHLnQYkqq95ibWgq3OqvvXEO1qBVg/0?wx_fmt=png)

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