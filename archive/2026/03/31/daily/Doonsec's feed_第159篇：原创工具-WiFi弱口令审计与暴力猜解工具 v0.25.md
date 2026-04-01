---
title: 第159篇：原创工具-WiFi弱口令审计与暴力猜解工具 v0.25
url: https://mp.weixin.qq.com/s/8yRanj6Hg1qglX81-PJ3rg
source: Doonsec's feed
date: 2026-03-31
fetch_date: 2026-04-01T04:44:34.628796
---

# 第159篇：原创工具-WiFi弱口令审计与暴力猜解工具 v0.25

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/uPOMOKjLe2Yibz8N12OiaFdQoMvYZuPBNEE0YMibxruibJfgxc5ibuial6FpiaOMynARkNNaMYJibpNrUvIrRd24KdY13hJ2HiacEdcH6MHVakgD6aHM/0?wx_fmt=jpeg)

# 第159篇：原创工具-WiFi弱口令审计与暴力猜解工具 v0.25

原创

abc123info
abc123info

希潭实验室

![]()

在小说阅读器中沉浸阅读

![](https://mmbiz.qpic.cn/mmbiz_png/OAz0RNU450ATcz6jUJnFNeOxRzVZ9LbcCCMJ6Af2WYicgMPA32IwibF8mI2ibC9h8jaHkhxnZzZuqctMLRTxDudicA/640?wx_fmt=png)

## **Part1 前言**

大家好，我是 ABC\_123。近年来红队评估项目越来越难打了，近源渗透逐渐成为常见切入点。很多项目都会安排到目标单位的总部或分支网点，通过物理接近的方式寻找可利用的无线网络。发现周边 WiFi 热点后，尝试获取其WiFi密码，一旦成功接入，有机会直接进入内网环境，从而发现新的攻击面，甚至取得突破性进展。在多次的近源攻击中，ABC\_123也创作了一个WiFi密码暴力猜解工具，加载字典不断枚举弱口令，可在现场直接使用。文末有知识星球二维码，欢迎大家扫码加入，一起学习进步。

![](https://mmbiz.qpic.cn/mmbiz_jpg/OAz0RNU450Dq1Q8s4COc7InkMO0jIGjiaGho1fcJicpibWB4vzvIM1wAib9TiakVECbIM5S0mHCTTeGJJibWtCe25vXw/640?wx_fmt=jpeg&from=appmsg)

## **Part2 技术研究过程**

双击运行“无线 WiFi 密码枚举工具”这个工具后，会弹出图形界面。点击“搜索附近 WiFi”即可扫描周边无线网络，并在列表中展示 SSID、BSSID、信号强度、频段及加密类型等信息。用户可双击目标 WiFi 自动填入名称，便于后续进行密码枚举测试。

![](https://mmbiz.qpic.cn/mmbiz_png/uPOMOKjLe2Y0PO8ibb2NxgjQe2laL4jqialE5Vd47Q3zcerLjHmdtV3ibrclsaVFnJhI01gic9Zfs88lWrsPzH2ATJyeGNvhwQRSZ6G2qWP3EXY/640?wx_fmt=png&from=appmsg)

选择目标WiFi（若出现同名，一般对应 2.4G 和 5G 频段），点击“开始破解密码”后，程序会按字典逐条尝试连接，自动进行密码枚举；一旦连接成功，即判定密码正确并自动停止。

![](https://mmbiz.qpic.cn/mmbiz_png/uPOMOKjLe2ZKv11YMTrVbOtFZtBEbyWl24qj267wSwNvhHiaDhZQQtraWXc7gOfPxXhWIKMrfjx6bV0Bd5zkrCGH2xnSakiaGV8Uribp5LJnks/640?wx_fmt=png&from=appmsg)

工具编写原理：

1.  使用 pywifi 扫描周边 WiFi，获取并展示 SSID、BSSID、信号强度、频段及加密类型等信息。

2.  用户选择目标 WiFi，并导入密码字典文件作为候选密码来源。

3.  程序逐行读取字典中的密码，进行顺序枚举。

4.  对每个候选密码构造连接配置（基于 WPA2-PSK + CCMP），并尝试连接目标 WiFi。

5.  等待约 1.5 秒检测连接状态：若连接成功则判定密码正确并停止，否则继续尝试下一个密码。

 Part3 总结

1.  修复了文本框在多线程环境下的安全问题，解决了输出错行等异常。

2.  点击“开始”后按钮自动置灰，避免重复触发；破解过程中支持随时点击“停止”进行中断。

3.  当密码猜解成功后，程序会自动在界面中填充对应的 WiFi 账号及密码信息。

4.  可通过加入知识星球「希水涵信安知识库-原创工具板块」获取，相关资料已系统整理，并持续更新，欢迎大家扫码加入。

![图片](https://mmbiz.qpic.cn/sz_mmbiz_jpg/uPOMOKjLe2YywU547copFHJL8xFRZjXnTxnC7GH7RHPZPdXkeGR545mibDpDO1MNU5GBZaEKAPo2ickgS6Ir2673hILujK7bSMrhfeSg6MSJ8/640?wx_fmt=jpeg&from=appmsg&watermark=1&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=8)

知识星球分为以下几个板块：

![图片](https://mmbiz.qpic.cn/sz_mmbiz_jpg/uPOMOKjLe2ZfOc4cib9XiaMpQW60ibhScZWItO5GU9UxkDAUDk1wx0abmj7TWgPr2riaNAwpz5skw3bBr5PLPOibG0hspJnhVz58mhwkIUFFkIvs/640?wx_fmt=jpeg&from=appmsg&watermark=1&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=9)

知识星球的每一篇PDF文档、PPT文档都细心整理，配有3到9张关键截图。

![](https://mmbiz.qpic.cn/mmbiz_jpg/uPOMOKjLe2bicNb95URAZRXXzwbCM3mTicHl3IlvnsiaAzaibVtibhj93YiaCLf0qHTMhspxGKk1ZLyeozMjEBop5h3s6oOe0vQ07rZGqkP3JLO4A/640?wx_fmt=jpeg&from=appmsg)

知识星球的每一个工具都是精心筛选，都附带有实测评价及使用说明。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/uPOMOKjLe2axPkYrOibDpJDloxpBYpIG0398Fjv6PI7DCJwtflV1GCDic2lzGC64U0LDG3kZbupxb4mrTzRZ3zrAxs6ciazdpXeMppfdCUjGmQ/640?wx_fmt=jpeg&from=appmsg)

欢迎大家扫码加入知识星球，一起学习进步！

![](https://mmbiz.qpic.cn/mmbiz_jpg/uPOMOKjLe2a8Qn5A6V1riav1lusWYBmiaq1dBZR7XNqf30uIDHwiciaibEvjhVRjIwjx2ibtXeSoXJnnrb9J0xFNSjRfNSnumRb7FbmxPN8Csk1NU/640?wx_fmt=jpeg&from=appmsg)

![图片](https://mmbiz.qpic.cn/mmbiz_png/OAz0RNU450A5qqg2iaK6KIYYR8y6pF5Rh3JHDibOKOop204nXz618iawdRb8dABicMPtHb2PkJE8x6koJO5HyuwZJQ/640?wx_fmt=png&wxfrom=5&wx_lazy=1&tp=webp#imgIndex=18)

**公众号专注于网络安全技术分享，包括APT事件分析、红队攻防、蓝队分析、渗透测试、代码审计等，每周一篇，99%原创，敬请关注。**

**Contact me: 0day123abc#gmail.com**

**OR 2332887682#qq.com**

**(replace # with @)**

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/OAz0RNU450BdnvpJibA3tSJeDb0OXXOT6kIw73PgKhWOibfMUWNHQrU1khmjEj6WmWUBLTzIurHUxfJScUyEcTicQ/0?wx_fmt=png)

希潭实验室

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/OAz0RNU450BdnvpJibA3tSJeDb0OXXOT6kIw73PgKhWOibfMUWNHQrU1khmjEj6WmWUBLTzIurHUxfJScUyEcTicQ/0?wx_fmt=png)

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