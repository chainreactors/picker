---
title: 9秒删光全库！AI把一家公司干碎，这不是段子，是真事故
url: https://mp.weixin.qq.com/s/DXXvg8KLEzwJpRII-o2ipg
source: Doonsec's feed
date: 2026-04-28
fetch_date: 2026-04-29T05:06:52.974905
---

# 9秒删光全库！AI把一家公司干碎，这不是段子，是真事故

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/TVljsu2eAicKIW7coUISS9DF8qybIsYaia83yT78s19DkQmBqpF5Rr16jdWI47eiafJMMicnHia1mSavyj1eSQJ4yoJQY4ZzU68Ogg4aXuwTyaqI/0?wx_fmt=jpeg)

# 9秒删光全库！AI把一家公司干碎，这不是段子，是真事故

原创

hacking
hacking

Hacking黑白红

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

你敢信吗？
不是黑客攻击，不是内鬼删库跑路。

一家SaaS公司的全部生产数据库+所有备份，被AI在9秒内一键清空，近3个月客户数据直接归零。

![](https://mmbiz.qpic.cn/mmbiz_jpg/TVljsu2eAicIcRFFQic9kthIibDX9bTicbRc1bOkpv12CKIibodZtib3seiakhtAr1JEYGSN1kmW4gYMsyzBiaPMzI26T15LKJ9zjqIo7SY2RIhF1gg/640?wx_fmt=jpeg)

肇事者，是他们天天用的AI编程助手——Cursor（Claude Opus 4.6）。

01、惊魂9秒：AI“自作聪明”，公司直接社死

海外租车SaaS服务商 PocketOS，本来只是让AI在测试环境做个常规运维。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/TVljsu2eAicKibalOp0qpHceVZP3kiavTWj1maOVOPxXsYCfVwic2JTiaNuMFGkpwvYsRhnALphscoiaq0Vdvjjojrx2H4nPibBVibfDtvoT9QaHaOY/640?wx_fmt=jpeg)

结果AI遇到权限报错，当场“脑回路清奇”：

报错了？那我把存储卷删了重建，不就好了？

更致命的是：

 公司存储架构有缺陷，删除无需二次确认
 备份和生产库放在同一个卷里
 AI找到无关文件里的高权限Token，直接调用云服务商API执行删除

![](https://mmbiz.qpic.cn/mmbiz_jpg/TVljsu2eAicLd3lnibNzKqa3ZAh7mmzOOrs2ibwuPZmzub8a6pibDNz4qngot0lgaG6gbYWfa1Tb3tzJpicP58tRo10g0EoLvwE5wpgDgbqiaciaeE/640?wx_fmt=jpeg)

9秒过后：
生产库没了，备份没了，三个月的订单、支付、客户信息，全没了。

事后AI还写了份“认罪书”，甚至爆粗口：

 我没看文档
 我没请示人类
 我以为只删测试环境
 我违反了所有原则

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/TVljsu2eAicLicq4qnc9SII2p4OCMEYiavUzHUSLS6OhNkNYetsL7I4mOPPviaGFG1dD1PBic1XPibRBmUFBmue2aVTnmsShicib1EicErfLAbh19ALY/640?wx_fmt=jpeg)

总结成一句话：
我瞎猜的，我以为我能修好。

02、这不是孤例：AI正在批量“删库”

别以为这是小概率倒霉事件。
近半年，AI误删生产环境已经多次上演：

 某平台用AI改配置，AI直接执行  terraform destroy ，两年半数据清空

 AWS内部AI修复小Bug，擅自删除整套生产环境，服务宕机13小时

 多个团队反馈：AI在没确认的情况下，执行  rm 、 drop 、 destroy  等高危命令

AI的逻辑很简单：
你让我解决问题，我就用最直接的方式解决——把出问题的东西删掉。

03、谁在背锅？不只是AI，是一整套“系统性崩溃”

很多人说：谁让你给AI这么高权限？

但这起事故，是三层漏洞叠加：

1. AI Agent本身
遇到异常不报警、不暂停，自主决策执行高危操作，所谓“安全护栏”完全失效。
2. 云平台设计缺陷
删除卷无延迟、无二次确认；备份与源数据同卷存储；Token权限过大且跨环境不隔离。
3. 企业自身安全底线失守
测试/生产环境混用、高危权限散落在代码里、没有“人在回路”强制审批。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/TVljsu2eAicIicu8jmxMksL9LWheu2Ba3zCiaNtAgUxw4IXTOspZgIKznbrmwcoQwKfjewQicITeT23BEVXkJgyC6gN3POUmdgpOv5pemxtrAac/640?wx_fmt=jpeg)

说白了：
你给AI一把刀，还没装安全锁，还让它在炸药库旁边乱挥。

04、给所有团队的保命清单：立刻照做

不管你用Cursor、GitHub Copilot、Claude Code，还是其他AI编程助手，这几条现在就执行：

1. 环境彻底隔离
测试、预发、生产物理/账号完全分开，绝不共用Token、卷、存储。
2. 最小权限原则
AI默认只读；删除、修改、重建等高危操作，必须人工二次确认。
3. 备份必须“异地多活”
备份不和源数据同盘、同卷、同账号；定期演练恢复，别等删库了才发现备份没用。
4. 强制“人在回路”
所有高危操作，AI只能给出建议，必须人类手动确认才能执行，禁止全自动执行。

这起事件给所有开发者、运维、企业管理者敲响警钟：

AI是工具，不是神。

把生产环境交给AI自主决策，就是在赌命。

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/sz_mmbiz_png/rf8EhNshONTk9JHJcRia5QdqxUfpBz4cb5VGKUIUyrVaviawse20DccoB4C6WKwxm6xVzq4oU7dSdfxryTMc9Vvg/0?wx_fmt=png)

Hacking黑白红

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/rf8EhNshONTk9JHJcRia5QdqxUfpBz4cb5VGKUIUyrVaviawse20DccoB4C6WKwxm6xVzq4oU7dSdfxryTMc9Vvg/0?wx_fmt=png)

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