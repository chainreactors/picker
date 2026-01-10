---
title: 火绒小问答——「企业版」离线升级工具与隔离网升级工具指南
url: https://mp.weixin.qq.com/s/Pb_b3zXSbhydZFoIxqnuYg
source: Doonsec's feed
date: 2026-01-09
fetch_date: 2026-01-10T03:24:19.014408
---

# 火绒小问答——「企业版」离线升级工具与隔离网升级工具指南

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/0icdicRft8tz7xGucUYl8icJicHmKlL1nvMOfll8tksGBuX2omwyI7AXLAezVcjmSrkgRttoOFJpBib6uvUhictZ1SpQ/0?wx_fmt=jpeg)

# 火绒小问答——「企业版」离线升级工具与隔离网升级工具指南

原创

火绒安全

火绒安全

![]()

在小说阅读器中沉浸阅读

![图片](https://mmbiz.qpic.cn/sz_mmbiz_gif/0icdicRft8tz7iato7JibDIQmF8J8iaF0RfnmKMcFNdDNkSK4HiaUeibds86SC50iaLhp9PHZD8vpMUaFQPibBkwl7PcEJg/640?wx_fmt=gif&from=appmsg#imgIndex=0)

点击蓝字，关注+星标⭐精彩内容不迷路~

![图片](https://mmbiz.qpic.cn/sz_mmbiz_gif/0icdicRft8tz67kQibpXXcWMgUOUKpXxjFaMtRMYbClDbKLkgKMf1vdBWn90gmgibZE3hhwREhicHjjS2sagpEvptgg/640?wx_fmt=gif&from=appmsg#imgIndex=0)

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/0icdicRft8tz7xGucUYl8icJicHmKlL1nvMOD1VIU0cQXJ1e93CQZVRIzOibHApq61lNKn3nx1959LbVdTxPOlPH6Bw/640?wx_fmt=gif&from=appmsg)

**尊敬的用户，您好！**

企业内网隔离虽能保障数据安全，却易导致火绒终端安全管理系统升级受阻。火绒企业版针对性推出**离线升级工具与隔离网升级工具**，无需打破网络隔离，即可实现控制中心程序、客户端程序、病毒库、漏洞补丁及授权信息的全量更新，适配不同隔离场景需求，区别在于内网是否允许向外传递信息。

**![](https://mmbiz.qpic.cn/mmbiz_gif/7QRTvkK2qC5GUbQCMws4DwCrakx3FiaDA57CMxiaWcSZKIa65Obg7ePmLUNOn0PHQnicRBmGFJIzxSFu0f9iaicFL0Q/640?wx_fmt=gif)**

**一、**

**离线升级工具：三步完成更新**

**1. 同步中心数据（内网机操作）**

登录火绒控制中心，从「管理工具」下载离线升级工具并运行；

![企业版1.png](https://mmbiz.qpic.cn/sz_mmbiz_png/0icdicRft8tz7xGucUYl8icJicHmKlL1nvMOtE7DkTwJLuN9okJicqcEINqh9qozicDRQnjeDfFdLX8ShrPMfuBU4XCw/640?wx_fmt=png&from=appmsg)

点击「同步中心」，填写控制中心地址（支持IPv4/IPv6/域名，格式如 127.0.0.1:8080），输入管理员账号密码；

![企业版2.png](https://mmbiz.qpic.cn/sz_mmbiz_png/0icdicRft8tz7xGucUYl8icJicHmKlL1nvMOtOibIhpBWRsia6x6Xso786NmibtM1rZ3LH79ib6V4rtibMQyWX3zCib0nPIA/640?wx_fmt=png&from=appmsg)

![企业版3.png](https://mmbiz.qpic.cn/sz_mmbiz_png/0icdicRft8tz7xGucUYl8icJicHmKlL1nvMObeFsQFE3RkrdqEkbr7KIJm6MM709qR37XSBa1EMibFfuJptJpgYdZCA/640?wx_fmt=png&from=appmsg)

成功后生成「conf 文件夹」（含授权状态、版本信息等），需妥善保存。

![企业版4.png](https://mmbiz.qpic.cn/sz_mmbiz_png/0icdicRft8tz7xGucUYl8icJicHmKlL1nvMO2LnpR9AQyPcazEEwMHW1yCd6ias2Y7auQeFsyGYDuRgXjWc0iaWqCPDQ/640?wx_fmt=png&from=appmsg)

**2. 下载升级包（外网机操作）**
将离线升级工具与「conf 文件夹」拷贝至外网机，放置同一目录；

打开离线升级工具，进入【下载升级包】页；

点击「检查更新」，按需勾选升级包、病毒库、补丁等类型；

有特殊补丁需求可点击「添加补丁」，选择对应操作系统补丁；

![企业版5.png](https://mmbiz.qpic.cn/sz_mmbiz_png/0icdicRft8tz7xGucUYl8icJicHmKlL1nvMODyS4KOUKtAtYhmFlgdWS95syeqvlsuSbtfQPvhPKDBWOrhic7z6FAng/640?wx_fmt=png&from=appmsg)

![企业版6.png](https://mmbiz.qpic.cn/sz_mmbiz_png/0icdicRft8tz7xGucUYl8icJicHmKlL1nvMOV3ficicDthTgcrlfnaCpQVUiaVux3t6jf3U126pBtRm6JNzq4l5icF5H9Q/640?wx_fmt=png&from=appmsg)

点击「开始下载」，生成「upgrade 文件夹」存放更新文件，下载完成后打包工具、conf 及 upgrade 文件夹。

**3. 更新控制中心（内网机操作）**
将打包文件拷贝回内网机，运行工具进入「更新中心」页；

点击「开始更新」，支持勾选「自动删除本次更新文件」来节省空间；

![企业版7.png](https://mmbiz.qpic.cn/sz_mmbiz_png/0icdicRft8tz7xGucUYl8icJicHmKlL1nvMOtOIgvPY0xQQRLM7QJ9C1sORRBy5teDpKAcqnYKdE0c3vUKOxmKZ2UA/640?wx_fmt=png&from=appmsg)

若未勾选“下次自动登录”则需再次填写管理员的账号密码，按提示补充后完成更新，弹窗提示 “更新完成” 即结束。

![企业版8.png](https://mmbiz.qpic.cn/sz_mmbiz_png/0icdicRft8tz7xGucUYl8icJicHmKlL1nvMOibENLjLwGfFD3QWjQubDhhbXxVibXAgLiboFNnswF1j7budyxwZmQ5sHQ/640?wx_fmt=png&from=appmsg)

**二、**

**隔离网升级工具：两步高效更新**

**1. 下载升级包（外网机操作）**
登录火绒官网用户中心（https://lic.buy.huorong.cn/），下载隔离网升级工具；

![企业版9.png](https://mmbiz.qpic.cn/sz_mmbiz_png/0icdicRft8tz7xGucUYl8icJicHmKlL1nvMOvkrClh8z3rPLTI0e4p4nlChLcJiayt9KRTle3g56nK1g09j0PJCL7RA/640?wx_fmt=png&from=appmsg)

运行工具，点击「检查更新」，输入序列号密码验证，获取匹配的更新文件；

![企业版10.png](https://mmbiz.qpic.cn/sz_mmbiz_png/0icdicRft8tz7xGucUYl8icJicHmKlL1nvMOicwCdTx6xp4EfstdqeGJBeMWAwgw7U1NIAy3Rko77ggEA9gBq27DgcA/640?wx_fmt=png&from=appmsg)

![企业版11.png](https://mmbiz.qpic.cn/sz_mmbiz_png/0icdicRft8tz7xGucUYl8icJicHmKlL1nvMOQfQaUmnhicQlcPJj83gjq60QBRdf1mD7Eo9rmltqfgVvEPPTasyiaB2g/640?wx_fmt=png&from=appmsg)

按需勾选更新类型，点击「开始下载」，自动生成「conf」和「upgrade」文件夹，建议打包拷贝。

![企业版12.png](https://mmbiz.qpic.cn/sz_mmbiz_png/0icdicRft8tz7xGucUYl8icJicHmKlL1nvMOztSvwhpS5p6IwIdKwriaLM0Aib3MPbRVYyRO35krOb7sHqQgpxzUqDicQ/640?wx_fmt=png&from=appmsg)

**2. 更新控制中心（内网机操作）**
将工具、「conf」及「upgrade」文件夹拷贝至可连接控制中心的电脑；

打开工具进入「更新中心」，点击开始更新，填写控制中心地址；

![企业版13.png](https://mmbiz.qpic.cn/sz_mmbiz_png/0icdicRft8tz7xGucUYl8icJicHmKlL1nvMO7CLPTnv4zo1CFiasBBbGRdHicNSX43wtqSceLZZYWD1LN3XsbHHYCZTQ/640?wx_fmt=png&from=appmsg)

![企业版14.png](https://mmbiz.qpic.cn/sz_mmbiz_png/0icdicRft8tz7xGucUYl8icJicHmKlL1nvMOg7Z6p1KBcRKRfSyyIia01c9E6otFR9bNYUTR6q9KcP6xaicG6wYanfeA/640?wx_fmt=png&from=appmsg)

再次点击「开始更新」，输入管理员账号密码并登录。支持勾选「自动删除本次更新文件」，更新完成后弹窗提示。

![企业版15.png](https://mmbiz.qpic.cn/sz_mmbiz_png/0icdicRft8tz7xGucUYl8icJicHmKlL1nvMOkKHGChB1kJLypcy8lZ42Y27OuWnLQhbVT0ZGmAARmtWEs6KibyImdZg/640?wx_fmt=png&from=appmsg)

![企业版16.png](https://mmbiz.qpic.cn/sz_mmbiz_png/0icdicRft8tz7xGucUYl8icJicHmKlL1nvMOhvVK1Pm2yOkGrGE7Fw50GHAR5UmbYyPHSAa5iaVy7ppnafX3L6WaQUQ/640?wx_fmt=png&from=appmsg)

**三、**

**关键注意事项**

1.两款工具的 conf、upgrade 文件夹需与工具同目录，否则无法正常使用；

2.超过 24 小时未检查更新时，工具会弹窗提醒，建议重新检查确保文件最新；

3.未授权的控制中心在外网下载步骤中可激活授权或更换授权，更新中心时会将新的授权信息同步到控制中心；

4.支持模糊搜索文件，列表中实时显示符合条件的文件；存在搜索条件时，点击「开始下载」按钮，下载的是所有的文件，并非是当前符合搜索条件的文件；

5.可通过「设置」界面配置代理服务器、下载速度限制（1KB/s-100MB/s）、同时下载任务数（1-10 个）。

**四、**

**常见问题速解**

**授权更新失败：**建议您在离线升级工具同步中心页重新进行更换授权后再进行操作；

**版本不一致提示：**确认控制中心地址正确，若版本低于 2.0.10.0，需先通过官网下载离线升级包升级控制中心到最新版本。

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/0icdicRft8tz7xGucUYl8icJicHmKlL1nvMOD1VIU0cQXJ1e93CQZVRIzOibHApq61lNKn3nx1959LbVdTxPOlPH6Bw/640?wx_fmt=gif&from=appmsg)

尊敬的用户：

若您有其他产品使用问题，可通过以下方式联系我们~

****微信公众号******：**主界面---常见问题---人工客服

****火绒官方论坛：****https://bbs.huorong.cn/

****火绒官方服务热线：****400-998-3555（法定工作日8:30-20:30，法定节假日9:30-18:30）

HUORONG

火绒安全成立于2011年，是一家专注、纯粹的安全公司，致力于在终端安全领域为用户提供专业的产品和专注的服务，并持续对外赋能反病毒引擎等相关自主研发技术。多年来，火绒安全产品凭借“专业、干净、轻巧”的特点收获了广大用户的良好口碑。火绒企业版产品更是针对企业内外网脆弱的环节，拓展了企业对于终端管理的范围和方式，提升了产品的兼容性、易用性，最终实现更直观的将威胁可视化、让管理轻便化，充分达到保护企业信息安全的目的。

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/0icdicRft8tz4K1e9ubHiaGLicyPrL2TGOQUVuzGfhiavltoNEsaCLCyJXChRib3yHaPTI00hV8oFkSsvwgunn2k0wSg/640?wx_fmt=other#imgIndex=11)

求点赞

![图片](https://mmbiz.qpic.cn/sz_mmbiz_gif/0icdicRft8tz4GYNjvnCrNwdcoKZrWuGN05z6DXwgVYcdZ6RFjwxdDoeAEia9eYdgyJaAJ0LDBJmxTdm2JUhkc4tg/640?wx_fmt=gif&from=appmsg#imgIndex=12)

求分享

![图片](https://mmbiz.qpic.cn/sz_mmbiz_gif/0icdicRft8tz4GYNjvnCrNwdcoKZrWuGN0CbyZz9kNTCKcA0puOEWfAYZnT6v6rr3kdBWIFw4TlSh7AgzSdOfAng/640?wx_fmt=gif&from=appmsg#imgIndex=13)

求喜欢

![图片](https://mmbiz.qpic.cn/sz_mmbiz_gif/0icdicRft8tz4GYNjvnCrNwdcoKZrWuGN0gBxG1O1Y7YCFGicYGrDUpcBg7iaLgNpCsDzNKcHwHcBgKktMtTSs6ZSA/640?wx_fmt=gif&from=appmsg#imgIndex=14)

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/sz_mmbiz_png/0icdicRft8tz5V9C96RXn1xV11tycAnWHXCicgKqfOS3JOw7jrIJckWH6Hg0bnXibjicPZs1ET2KwtvsRs41ZhCxh2A/0?wx_fmt=png)

火绒安全

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/0icdicRft8tz5V9C96RXn1xV11tycAnWHXCicgKqfOS3JOw7jrIJckWH6Hg0bnXibjicPZs1ET2KwtvsRs41ZhCxh2A/0?wx_fmt=png)

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