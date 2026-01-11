---
title: 【应急响应】记一次VPS反弹shell告警处置
url: https://mp.weixin.qq.com/s/lZ7EfSrn4ddyGNwvufWdww
source: Doonsec's feed
date: 2026-01-10
fetch_date: 2026-01-11T03:37:31.429411
---

# 【应急响应】记一次VPS反弹shell告警处置

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/MjmKb3ap0hBscmafCI0WfibUia554KeaGDaO9Dr0OIyM5cZs42vIyAfLgmpmFOf6evDXF31USV9gSCZouyofcKNQ/0?wx_fmt=jpeg)

# 【应急响应】记一次VPS反弹shell告警处置

原创

弥天安全实验室

弥天安全实验室

![]()

在小说阅读器中沉浸阅读

网安引领时代，弥天点亮未来

![Image](https://mmbiz.qpic.cn/mmbiz_png/MjmKb3ap0hDCVZx96ZMibcJI8GEwNnAyx4yiavy2qelCaTeSAibEeFrVtpyibBCicjbzwDkmBJDj9xBWJ6ff10OTQ2w/640?wx_fmt=other&wxfrom=5&wx_lazy=1&wx_co=1&randomid=2jntd263&tp=webp#imgIndex=0)

**0x00写在前面**

**本次测试仅供学习使用，如若非法他用，与平台和本文作者无关，需自行负责！**

![Image](https://mmbiz.qpic.cn/mmbiz_png/MjmKb3ap0hDCVZx96ZMibcJI8GEwNnAyx4yiavy2qelCaTeSAibEeFrVtpyibBCicjbzwDkmBJDj9xBWJ6ff10OTQ2w/640?wx_fmt=other&wxfrom=5&wx_lazy=1&wx_co=1&randomid=7c3v7kvq&tp=webp#imgIndex=1)

**0x01事件起因**

阿里云服务器产生反弹shell告警，在短信收到了同步信息，具体如下

![](https://mmbiz.qpic.cn/mmbiz_png/MjmKb3ap0hBscmafCI0WfibUia554KeaGDicCKngSSA39fBdHqJxRvWGeKibVtoqwc3R12WjvwgvRgS79cFLsRl1Iw/640?wx_fmt=png&from=appmsg)

同时在控制台看到有详细的反弹代码内容，包括进程路径、进程链

![](https://mmbiz.qpic.cn/mmbiz_png/MjmKb3ap0hBscmafCI0WfibUia554KeaGD69AFyxATZh0q4ssMX5sfqDfYq7Y2Z3icZcRAo09M7ic1MW9wJhkM9A7g/640?wx_fmt=png&from=appmsg)

![Image](https://mmbiz.qpic.cn/mmbiz_png/MjmKb3ap0hDCVZx96ZMibcJI8GEwNnAyx4yiavy2qelCaTeSAibEeFrVtpyibBCicjbzwDkmBJDj9xBWJ6ff10OTQ2w/640?wx_fmt=other&wxfrom=5&wx_lazy=1&wx_co=1&randomid=bzequ3sx&tp=webp#imgIndex=3)

**0x02事件分析**

通过ssh登录到vps服务进行应急分析，具体记录如下：

在查询前对攻击IP进行威胁情报查询，发现关联样本有CS木马。

![](https://mmbiz.qpic.cn/mmbiz_png/MjmKb3ap0hBscmafCI0WfibUia554KeaGDegFHOR7BiaasTuTql4qwluUEdDErbzmyo6vl15s4DX9yADDWtrDBzUg/640?wx_fmt=png&from=appmsg)

1、查看网络连接信息

```
netstat -anp|grep 8888ps -aux |grep 8888
```

![](https://mmbiz.qpic.cn/mmbiz_png/MjmKb3ap0hBscmafCI0WfibUia554KeaGDzBWHAHVPSguV87d2GS4TDVX2csWvflZoJVE98apTISic65ZMSmzVtTw/640?wx_fmt=png&from=appmsg)

2、系统计划任务查看

```
crontab -l
```

![](https://mmbiz.qpic.cn/mmbiz_png/MjmKb3ap0hBscmafCI0WfibUia554KeaGD8nVrb8rLKMJgttBR8qS0wofGyJlEyXKtkgPkmyMuNceZw5VKWbvotg/640?wx_fmt=png&from=appmsg)

删除计划任务

```
crontab -r
```

![](https://mmbiz.qpic.cn/mmbiz_png/MjmKb3ap0hBscmafCI0WfibUia554KeaGDXKpibp7U8Kppjr7K7tZz36TQEfgomtL4BY2MdljmnPEVTqdDArDadsg/640?wx_fmt=png&from=appmsg)

3、通过上述操作之后，发现网络连接还存在，这说明还有隐藏计划任务

![](https://mmbiz.qpic.cn/mmbiz_png/MjmKb3ap0hBscmafCI0WfibUia554KeaGDZbX4bMLvumAq1jAmAqDVKlw7C6lqz9I77Cw9ez7rPQntkro9HgkxYw/640?wx_fmt=png&from=appmsg)

通过查询系统历史操作命令包含端口8888的命令

```
history | grep "8888"
```

![](https://mmbiz.qpic.cn/mmbiz_png/MjmKb3ap0hBscmafCI0WfibUia554KeaGDn75JeYMhiafq5BmL8G0kN4h7K1bAuvA4dWSg1XDW3Dxgllfk6nnzafw/640?wx_fmt=png&from=appmsg)

发现通过echo命令写入反弹shell命令到/var/spool/cron/root路径

![](https://mmbiz.qpic.cn/mmbiz_png/MjmKb3ap0hBscmafCI0WfibUia554KeaGDovDOicz0cgYozMls9WV8UjbiacuXmsaicwJ8EaqIMsqST4icSAGTQen7xg/640?wx_fmt=png&from=appmsg)

查看写入日期为2024年7月31日

![](https://mmbiz.qpic.cn/mmbiz_png/MjmKb3ap0hBscmafCI0WfibUia554KeaGDvjDwZxFcPicHOKqRibtTZ4NpwtIaXE7mksljZ1wAmSx9FAupyHAqR8ibw/640?wx_fmt=png&from=appmsg)

删除写入的反弹代码的该文件

![](https://mmbiz.qpic.cn/mmbiz_png/MjmKb3ap0hBscmafCI0WfibUia554KeaGD4BSdYcMjCTXp7pATIuYtx3xKNmILuWUpTYqd4E9HcDhcgrpSamZ6ng/640?wx_fmt=png&from=appmsg)

4、查网络连接已经消失

![](https://mmbiz.qpic.cn/mmbiz_png/MjmKb3ap0hBscmafCI0WfibUia554KeaGDhnFj0o6Kt36f8fDOGbMTfVUdjLZWX75QPjibflVexhXWqMG2l0Sicbag/640?wx_fmt=png&from=appmsg)

但是发现进程信息还存在，文章为回溯记录，下图为【执行grep进程】

![](https://mmbiz.qpic.cn/mmbiz_png/MjmKb3ap0hBscmafCI0WfibUia554KeaGDkCJdNow6zGZBAJI2gDqsBAa4EXPlFiaPPibLp7BPuricAwvLhU8fwMDXw/640?wx_fmt=png&from=appmsg)

5、证明该事件还未彻底处理✅

继续查询常见路径下是否关于该反弹shell代码相关内容文件

```
grep  -r "103.x.x.x" /etc/ /root/ /home/ 2>/dev/null
```

![](https://mmbiz.qpic.cn/mmbiz_png/MjmKb3ap0hBscmafCI0WfibUia554KeaGDQeOeHWeWUGSwPjNNXrbAbeeYiczpicd6IRDDQ9mr10ECBMCeSOTGk71g/640?wx_fmt=png&from=appmsg)

发现在/root/.bash\_history【历史记录】/etc/cron.d/test路径下有该反弹代码的写入，继续清除。

6、通过ssh连接系统后，查看网络连接发现又出现。

![](https://mmbiz.qpic.cn/mmbiz_png/MjmKb3ap0hBscmafCI0WfibUia554KeaGD9NeXy9ynIMawn9xOo67klXJNIOwicOeRPeSyl039Qp6CdHtprTe2wbw/640?wx_fmt=png&from=appmsg)

此现象说明该反弹shell代码文件还没彻底清理干净，全盘查询反弹IP相关文件，在/etc/profile.d/路径发现一个1.sh的脚本。

```
sudo grep -r "103.x.x.x" /etc /root /home /var /tmp /opt 2>/dev/null
```

![](https://mmbiz.qpic.cn/mmbiz_png/MjmKb3ap0hBscmafCI0WfibUia554KeaGD4OXriaun6tzYRLXfebiaWy07FBqlUnFuHiaUrnqwCH6tkhA9rjBk7licTw/640?wx_fmt=png&from=appmsg)

查看文件内容为，bash反弹shell脚本。

![](https://mmbiz.qpic.cn/mmbiz_png/MjmKb3ap0hBscmafCI0WfibUia554KeaGDITb3qQWDUL0b8F1DRWMicZ2eB9B2UbLFzHFuIew3JToVljSAC1gFsvQ/640?wx_fmt=png&from=appmsg)

删除该文件，最终清理完成。

![](https://mmbiz.qpic.cn/mmbiz_png/MjmKb3ap0hBscmafCI0WfibUia554KeaGDav5bofBbAwKoQ4jNPZoRE2oMBBkTF4qgB18Z1AEUy9ib6Kz6Oic6jjNg/640?wx_fmt=png&from=appmsg)

验证连接后是否还出现相应的网络连接。

成功处置![](https://res.wx.qq.com/t/wx_fed/we-emoji/res/assets/newemoji/LetMeSee.png)

![](https://mmbiz.qpic.cn/mmbiz_png/MjmKb3ap0hBscmafCI0WfibUia554KeaGDw3Wg0sTwEZUlicGau87hOBB1fTyteaUpbSmfuyUG5ucD4ElNhxyQvfw/640?wx_fmt=png&from=appmsg)

![Image](https://mmbiz.qpic.cn/mmbiz_png/MjmKb3ap0hDCVZx96ZMibcJI8GEwNnAyx4yiavy2qelCaTeSAibEeFrVtpyibBCicjbzwDkmBJDj9xBWJ6ff10OTQ2w/640?wx_fmt=other&wxfrom=5&wx_lazy=1&wx_co=1&randomid=bzequ3sx&tp=webp#imgIndex=5)

**0x03事件处置**

1、云防火墙对反弹端口进行限制，对反弹shell IP进行黑名单处置。

2、对终端进行安全基线加固，修改ssh登录密码。

3、终端安装安全防护软件。

4、定期巡检终端系统。

![Image](https://mmbiz.qpic.cn/mmbiz_png/MjmKb3ap0hDCVZx96ZMibcJI8GEwNnAyx4yiavy2qelCaTeSAibEeFrVtpyibBCicjbzwDkmBJDj9xBWJ6ff10OTQ2w/640?wx_fmt=other&wxfrom=5&wx_lazy=1&wx_co=1&randomid=bzequ3sx&tp=webp#imgIndex=3)

**0x0**4事件思考****

1、互联网资产风险无处不在，对外的暴露大大增加了被攻击的风险，最小化原则非常重要。

2、终端的应急处置是一个需要耐心、细心、决心的过程。

3、安全产品 WAF、IDS、IPS 等检测系统，可以阻断该攻击行为。

4、安全的本质就是不断持续对抗，该反弹代码在隐藏性、持久性、多样性都有体现。

弥天简介

学海浩茫，予以风动，必降弥天之润！弥天安全实验室成立于2019年2月19日，主要研究安全防守溯源、威胁狩猎、漏洞复现、工具分享等不同领域。目前主要力量为民间白帽子，也是民间组织。主要以技术共享、交流等不断赋能自己，赋能安全圈，为网络安全发展贡献自己的微薄之力。

口号 网安引领时代，弥天点亮未来

![Image](https://mmbiz.qpic.cn/mmbiz_gif/b96CibCt70iaaqjXT4YxgHVARD1NNv0RvKtiaAvXhmruVqgavPY3stwrfvLKetGycKUfxIq3Xc6F6dhU7eb4oh2gg/640?wx_fmt=gif&wxfrom=5&wx_lazy=1&randomid=h6lqq1ue&tp=webp#imgIndex=8)

知识分享完了

喜欢别忘了关注我们哦~

学海浩茫，

予以风动，

必降弥天之润！

弥  天

安全实验室

![Image](https://mmbiz.qpic.cn/mmbiz_jpg/MjmKb3ap0hDyTJAqicycpl7ZakwfehdOgvOqd7bOUjVTdwxpfudPLOJcLiaSZnMC7pDDdlIF4TWBWWYnD04wX7uA/640?wx_fmt=other&wxfrom=5&wx_lazy=1&wx_co=1&randomid=u34b870m&tp=webp#imgIndex=9)

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/MjmKb3ap0hDw8KzdJMvNibaUicZb081gFUakPPg57pJjSNKOMC1Sia0icMZpBLcRrTd7kV6peRt16pvS9zGSJ36xzA/0?wx_fmt=png)

弥天安全实验室

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/MjmKb3ap0hDw8KzdJMvNibaUicZb081gFUakPPg57pJjSNKOMC1Sia0icMZpBLcRrTd7kV6peRt16pvS9zGSJ36xzA/0?wx_fmt=png)

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