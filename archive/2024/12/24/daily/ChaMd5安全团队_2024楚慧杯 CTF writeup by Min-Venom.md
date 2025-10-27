---
title: 2024楚慧杯 CTF writeup by Min-Venom
url: https://mp.weixin.qq.com/s?__biz=MzIzMTc1MjExOQ==&mid=2247511758&idx=1&sn=62247e6f1c03594712d6235479583733&chksm=e89d8616dfea0f005f0e5830f35813e88375a2f8e7f1eb24a738ebda49e616a51243c8d0f9b5&scene=58&subscene=0#rd
source: ChaMd5安全团队
date: 2024-12-24
fetch_date: 2025-10-06T19:40:55.814336
---

# 2024楚慧杯 CTF writeup by Min-Venom

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/PUubqXlrzBSexXKlVLqFkDAYtfNRq1Ztts8DG1EbZkyRwh16ZzZUOWkE3mR1fYo3R8mSUTD6biccE8iaw6WEzg5Q/0?wx_fmt=jpeg)

# 2024楚慧杯 CTF writeup by Min-Venom

原创

Mini-Venom

ChaMd5安全团队

> > 招新小广告CTF组诚招re、crypto、pwn、misc、合约方向的师傅,长期招新IOT+Car+工控+样本分析多个组招人有意向的师傅请联系邮箱
> >
> > admin@chamd5.org(带上简历和想加入的小组)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/PUubqXlrzBSexXKlVLqFkDAYtfNRq1Ztz5qpd2bWJgEZk1fP6KrOKrT5gibQsTdRiahFuPn4M9ZVeTZmibC1ttVVw/640?wx_fmt=png)

**ChaMd5安全团队**成立于2016年，专注于算法加解密、安全漏洞挖掘、CTF竞赛及安全人才培养。至今团队成员有200+人，分别来自阿里、滴滴、启明星辰、绿盟、知道创宇、奇安信、永信至诚、360、陌陌、牛盾、无声信息等安全公司，且也有部分在校学生与自由职业者。

自团队成立以来，曾荣获来自华为、微软、蚂蚁金服、百度、京东和滴滴等多家企业的致谢，向企业报告的漏洞合计**超****10w+**。团队成员也曾多次在企业 CTF 赛事中获奖。ChaMd5 安全团队**为维护企业安全建设而成立**，竭尽全力培养安全人才，服务于各大企业。

**ChaMd5安全团队**将继续与平台一同进步，也欢迎更多的小伙伴加入我们哦！

```
安全厂商漏洞提交
2024年京东SRC“优秀合作伙伴”称号和个人第四名(Str1am_)
2024年盘锦市演练优秀攻击队
2023年京东SRC个人第三名(Str1am_)
2023年补天总榜个人排名第十(r00t4dm)
2023年多点SRC年度第三(Cra5h)
2023年TCL年度第四(Cra5h)
2023年同程SRC个人年度第二(IT小丑)
2023年滴滴SRC个人年度第五(IT小丑)
2023年漏洞盒子团队第一季度 第三名
2023年漏洞盒子团队第三季度 第二名
2023年漏洞盒子团队第四季度 第三名
2023年大连网信办“连盾”第二名
2022年PSRC团队年度第三名
2022年BSRC团队年度第二名
2022年货拉拉获得”黄金轻卡“称号
2021年DSRC获得年度第三名
2021年BSRC获得年度第三名
2017-2020年DSRC(滴滴)年度安全团队第一名
2020年JSRC(京东)团队年度第二名
2020年BSRC(百度)第三名
2020年网易SRC团队年度第二名
2020年58SRC团队年度第二名
2020年字节跳动SRC团队年度第三名
2020年360SRC年度团队第二名
2020年TSRC(腾讯)年度合作伙伴奖
2019年JSRC(京东)团队年度第三名
2019年华为云2019年度团队二等奖、华为终端2019年度最具潜力奖
2019年MTSRC(美团)年度团队第二名
2019年ASRC(阿里)年度合作伙伴奖
2019年合肥市网络安全攻防演练大赛攻防演练赛 线下第八名
2019年BSRC(百度) 年度第三名和校园年度第二名
2018年BSRC(百度) 年度第二名
2017年BSRC(百度)优秀团队

CTF比赛
2024年国城杯 第八名
2024DASCTF 暑假挑战赛 第一名
2024年矩阵杯 优胜奖
2024年举办第一届 VCTF 纳新赛
2023年中华武数杯 三等奖
2023年NCTF 第八名
2022年第五届强网拟态 第九名
2022年安洵杯 第七名
2021年第四届强网拟态 第一名
2021年长安杯总决赛一等奖
2021年巅峰极客 第一名
2020年“祥云杯”线上第三名
2020年GeekPwn云靶场挑战赛第八名
2020年线上网鼎杯"青龙组"第五名
2019年“湖湘杯”网络安全技能大赛线下第四名
2019年XPpwnCTF第五名
2019年SUCTF 线上第三名
2019年第三届“红帽杯”网络安全攻防大赛 线上社会网安第五名

工控比赛
2022年之江杯第五名&内生安全贡献荣誉奖
2020年之江杯第一名
2018年赛博地球杯工业互联网安全大赛线下总排名 第二名

IoT比赛
2023年DataCon漏洞分析赛道第三名
2022年DataCon物联网安全第四名
2020年西湖论剑IOT挑战赛第一名
2019年360SRC48小时IoT破解大赛第四名

AI比赛
2024年DataCon AI第四名
2024年ByteAI安全挑战赛决赛第十名
2022年2022 CCF BDCI 竞技赛单赛题决赛 基于TPU平台实现人群密度估计 二等奖
2022年字节安全AI挑战赛 第四名
2021年iFLYTEK.AI 第十名
2020年BCTF AI PWN第六名
2019年强网杯AI 第十名
2019年BCTF RHG 人工智能第八名

车联网
2024Block Harbor VicOne Automotive CTF 线上 第六名
2024年Super CS车联网安全攻防挑战赛线下 优胜奖
2024年VSEC挑战赛二 第六名
2023年CIICV车联网（智能网联汽车）漏洞挖掘挑战赛 优胜奖
2023年WIDC世界智能驾驶挑战赛 线上第二名
2022 第二届创安杯智能汽车信息安全公开赛 线上第九名
2022 CICV 智能网联汽车漏洞挖掘赛 线下一等奖
2022 CICV智能网联汽车漏洞挖掘赛 线上三等奖
2021年第二届中国智能网联汽车大赛"天融信杯" 铜奖
2021年世界智能驾驶挑战赛 铜奖

区块链
2023年MetaTrustCTF 参与命题
2023年NumenCTF 第十四名
```

- END -

https://github.com/ChaMd5Team/Venom-WP/blob/main/2024-楚慧杯-WriteUp.pdf

![](https://mmbiz.qpic.cn/mmbiz_gif/PUubqXlrzBRH2vOmzbCqYb35uicIicQcxDYmXzZRoiaM7vy41cjBXmbWys0xiadJ2zwYG6ODyDjjBafPDDCDWJCVbg/640?wx_fmt=gif)

更多 Writeup 详情

查看以下链接或点击文末阅读原文

![](https://mmbiz.qpic.cn/mmbiz_gif/PUubqXlrzBRH2vOmzbCqYb35uicIicQcxDR3lbWnKxpic9icIjYzbsJjISBQEicVFia5IOsHMULFVHiakxSAQSlj8cmVg/640?wx_fmt=gif)

结束

招新小广告

ChaMd5 Venom 招收大佬入圈

新成立组IOT+工控+样本分析 长期招新

欢迎联系admin@chamd5.org

![](https://mmbiz.qpic.cn/mmbiz_png/PUubqXlrzBR8nk7RR7HefBINILy4PClwoEMzGCJovye9KIsEjCKwxlqcSFsGJSv3OtYIjmKpXzVyfzlqSicWwxQ/640?wx_fmt=jpeg)

预览时标签不可点

阅读原文

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/PUubqXlrzBRyftF8Oqhh2V8ib6wEgOiaCMdKBLfkLlHAvKibMgjerLzeXXxRmyI9VpjX7e37vjeW2scODia9KHGoqQ/0?wx_fmt=png)

ChaMd5安全团队

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/PUubqXlrzBRyftF8Oqhh2V8ib6wEgOiaCMdKBLfkLlHAvKibMgjerLzeXXxRmyI9VpjX7e37vjeW2scODia9KHGoqQ/0?wx_fmt=png)

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