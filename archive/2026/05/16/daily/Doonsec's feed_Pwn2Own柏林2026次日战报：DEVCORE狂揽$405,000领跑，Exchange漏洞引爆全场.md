---
title: Pwn2Own柏林2026次日战报：DEVCORE狂揽$405,000领跑，Exchange漏洞引爆全场
url: https://mp.weixin.qq.com/s/pW6ihfvEMa8QBRjymahIqQ
source: Doonsec's feed
date: 2026-05-16
fetch_date: 2026-05-17T05:43:24.227995
---

# Pwn2Own柏林2026次日战报：DEVCORE狂揽$405,000领跑，Exchange漏洞引爆全场

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/tbTbtBE6Tibe9CzS89iaU90MlGWk4Tu6TNNbUWByeViaQB6pibLzRoMtCkmhqGzPzzicnAhsA4mKNUpCZKgoyrjXyS5uqR4v5CIC0T0o2WPhjRXs/0?wx_fmt=jpeg)

# Pwn2Own柏林2026次日战报：DEVCORE狂揽$405,000领跑，Exchange漏洞引爆全场

幻泉之洲

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

> Pwn2Own柏林2026第二天比赛落下帷幕，新增15个0-day漏洞，奖金池再添$385,750。DEVCORE团队凭借Exchange远程代码执行漏洞豪取$200,000，以40.5分稳居Master of Pwn榜首。两天累计产生39个独特漏洞，总奖金达$908,750。

## 战况升级，Exchange成最大看点

Pwn2Own柏林2026进入第二天，攻防节奏明显加快。第一天24个0-day漏洞、$523,000奖金的成绩已经够猛了，第二天又怼进去15个独特漏洞，入账$385,750。现在总榜上是39个漏洞，$908,750。还剩一天，DEVCORE以40.5分和$405,000的成绩领跑，但说实话，最后一天什么都有可能发生。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/tbTbtBE6TibdTsHp6ib0mnPebib2icXINWSSvQh6CEvBk1ctpz5tAicvniaG1uK1f4pwG3kNOic6cKnNXNv0OnnPJnMwIrH2ShB0Xxiah1Wu1mgpXu4/640?wx_fmt=png&from=appmsg)

比赛全程实时更新在ZDI博客[1]和社交媒体同步发布，Twitter[2]、Mastodon[3]、LinkedIn[4]和Bluesky[5]都可以追，话题标签是#Pwn2Own Berlin和#P2OBerlin。

## 第二天完整战果

开场不顺。Palo Alto Networks的Tao Yan和Edouard Bochin尝试攻击Apple Safari（仅渲染器），时间耗尽，失败。

![](https://mmbiz.qpic.cn/mmbiz_jpg/tbTbtBE6TibfxicumjWFoWicVGobuefcsN8cadf6QE5tboZczUh6miajPxJALV7siafpYvECCYiasu71nNshOtTUBnp6OsgverRw1UPJicTibDOaNX8/640?wx_fmt=webp&from=appmsg)

Rapid7的Stephen Fewer也没能搞定Microsoft SharePoint，同样超时失败。

![](https://mmbiz.qpic.cn/mmbiz_jpg/tbTbtBE6TibfD437Eh9xG2O0galiasbXpiaoRpN7Uae3ZDQbE5vB4PEiauMWricgtYsjgOFDJEbSCMyWDNicEpibRNE2QQfYggv8Ut21GFV89xYghE/640?wx_fmt=webp&from=appmsg)

Team DDOS的Ben Koo（@kiddo\_pwn）在第二轮用了一个use-after-free漏洞，成功提权Red Hat Enterprise Linux for Workstations，拿到$10,000和1个Master of Pwn积分。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/tbTbtBE6TibchbrYoj0GSbJ2dv3sh0cvRaa55gaZibWjX8gjmO7QBoPTK5tbkON4HUF0cVI05y5weCXFle6wtVTsGohITGfC18BRr1dALCFxI/640?wx_fmt=webp&from=appmsg)

OtterSec的三人组Nikolaos Mourousias（@deltaclock）、Caue Obici（@caueobici）和Bruno Halltari（@BrunoModificato）表现亮眼，用代码注入漏洞拿下LM Studio第二轮，$20,000加4分，满血全胜。

![](https://mmbiz.qpic.cn/mmbiz_jpg/tbTbtBE6TibdeDaYTaiaAvHicIMyaHGlp3ganibyZjiablVibAhSzTEXibibyy6NdQ1EysibsicZlxg1d3RibPmyDIGUcZQNwh3ERscicjVGWrkw9dsD2ibA/640?wx_fmt=webp&from=appmsg)

Summoning Team的Sina Kheirkhah（@SinSinology）虽然在台上成功演示了针对Claude Desktop（编码代理类别）的攻击，但用的漏洞之前已经有人报过了，算碰撞，奖金$10,000和2分照给。

![](https://mmbiz.qpic.cn/mmbiz_jpg/tbTbtBE6Tibc76oFo0Zebu4x0jx0LAdJfkkBwPmBzAch0gyF3pMCOPhUxaD98cbToKW4hGYucCpnQpaOk5fwuxvl7CH9CFT9d41xiaW6gquZo/640?wx_fmt=webp&from=appmsg)

Viettel Cyber Security的Le Duc Anh Vu（@vulda17）拿下Cursor，$30,000加3分，又是全胜。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/tbTbtBE6TibecSB1fibRIqv9ic6ZrmNlBDS9U4iblzHvamBJIRicmL1VL7MC9rX7Gl632fl8ic56nVbWbKI3k5yoGz4lovlKaY0kh0hrg3Qr4iaEOI/640?wx_fmt=webp&from=appmsg)

Kakaogames的Kiyong Kwak和三星电子的Song Nuri撤回了Apple Safari（仅渲染器）的报名。

![](https://mmbiz.qpic.cn/mmbiz_jpg/tbTbtBE6TibeuXQMdzMafnPtHbSv5KPyd3QtthKER9qiaj5mzsSrLQuO6By8DSpebWLGstUXpNh9ayJhZMWUA2fqQwWxicNY5cXlzic3Ehs268g/640?wx_fmt=webp&from=appmsg)

科罗拉多大学博尔德分校Abstract Team的Ruitong攻击Red Hat Enterprise Linux for Workstations，没能按时完成，失败。

Summoning Team的Sina Kheirkhah（@SinSinology）再次出场，第二轮拿下OpenAI Codex，$20,000加4分。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/tbTbtBE6Tibe6KjTLC0smoDMX234UeYNLSjMdc9dehDxEqepeRYpHRTqAXPB7pFJVNogXFo1iafXYGUSZNA3DsodbTHJ46emHJfHvibicFd18ib4/640?wx_fmt=webp&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_jpg/tbTbtBE6Tibdde1ibicpRcJIVWficSJAujRoaNpWkuBO6p083oQ6TJp2o878Ko1mQIiaicK6yMUJDza8I2dsX7T8aaCeIM8tRmm7NKLvkNMgLUxpQ/640?wx_fmt=webp&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_jpg/tbTbtBE6Tibdp8LVjUiaw6kqCqscdgCKXmUsJqU3mKQcuNw6k7wko62zcRIjribllLtU30vyMCuM9JR9GDz9hhXZs7SP6Ticia3Yib60gambOn6Es/640?wx_fmt=webp&from=appmsg)

STARLabs SG的Billy（@st424204）、Bruce Chen（@bruce30262）、Pan Zhenpeng（@Peterpan980927）和Weiming Shi（@bestswngs）攻击NVIDIA Megatron Bridge，漏洞碰撞，拿$2,500和1分。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/tbTbtBE6TibdQtRxYPk9pnF3QYzFCJ0YINDYQLE9hCAr2iaAibsSLGBwiagCET3djdN9etWQB3UoljcNuYOoh5XKRkRwUf4kqicM8u6iaVbbMQnLs/640?wx_fmt=webp&from=appmsg)

Alon Ben Tsur（@iamgweej）和Yahav Azran（@\_yahav）撤回了Red Hat Enterprise Linux for Workstations的提权报名。

![](https://mmbiz.qpic.cn/mmbiz_jpg/tbTbtBE6TibfgYPic9YibmlVfwQDKic45Z2lqaZnjA0vDlQNa8yJFBeV5mNy6MZJawHmqeMBK2rkibfcia8dtJ7LvOWMpushSYjNGQ6lHCiaK1OuCs/640?wx_fmt=webp&from=appmsg)

**全场最高潮来了。**DEVCORE的Orange Tsai（@orange\_8361）用3个漏洞串联，在Microsoft Exchange上实现SYSTEM权限远程代码执行，$200,000加20分。这个成绩基本锁定了Master of Pwn的领先地位。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/tbTbtBE6Tibd3S18NJFiaXPpOKrbxpu6ajKGJ9BTsX8gCuw2xU38DViaaqpFnpibDVOq7C844k42hLJWPKkvEaHXkewZWMyFk2bdVwR0mV74h8g/640?wx_fmt=webp&from=appmsg)

Out Of Bounds的David Tae和Louis Hur攻击Ollama，发生单漏洞碰撞，$28,000加3分。

![](https://mmbiz.qpic.cn/mmbiz_jpg/tbTbtBE6TibfwibeYOicoSyExmdWNHPicVX1KDXxAu3lGyhDC6dickOaexr3s1Yn4ucgVBONjxOoibTSTzqsibbTV6CXibyiaEPXe6HuHkSJECSgeFAc/640?wx_fmt=webp&from=appmsg)

Viettel Cyber Security的Nguyen Thanh Dat（@rewhiles）攻击Mozilla Firefox（仅渲染器），超时失败。

![](https://mmbiz.qpic.cn/mmbiz_jpg/tbTbtBE6TibeAagfXlpkSiawx1STDq7ScOiatI8gjSP6JXkmrdAgCu9UkwH0uiaWmmMhJZw5wWfeFKhbiaBKhXpibVpyGejRU9LsMQEI5HYfC1zQw/640?wx_fmt=webp&from=appmsg)

Compass Security的Cyrill Bannwart、Emanuele Barbeno、Yves Bieri、Lukasz D.和Urs Mueller（@compasssecurity）第二轮拿下Cursor，$15,000加3分。

![](https://mmbiz.qpic.cn/mmbiz_jpg/tbTbtBE6Tibeg5ibauxPUoe51icIeVgelup4UAVmffF1eIceX2YGHsSicibl1j8OqxhngZqaSic7EfnUEHd59AN3WoAW7mVyhKl0MV2bpic21b3MTc/640?wx_fmt=webp&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_jpg/tbTbtBE6TibdIuodxEhj4MSibuILIN69iaJChdW9ia6xWbugRnzlWZKXIA7FhiaOC6KwEOticYLY1qVtsW6pO68HFw57mjUTCo74CnVq38syz6wvA/640?wx_fmt=webp&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/tbTbtBE6TibeibSquNFMX9dsMp1QtKtCIRqHicQc7WRYp6UBFKYFlkIFp8icD9iaDhlcq4YPTT4m6kUmogWjicMbeHMnZ4EUrN9icgIV11zzQ8yVhs/640?wx_fmt=webp&from=appmsg)

Siyeon Wi用整数溢出漏洞在第四轮提权Microsoft Windows 11，$7,500加3分。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/tbTbtBE6TibdL1mZw85P1Z3ibbWmhf6YnL4RAhSpnicjOKYKmbUOmtGb7JZlREUuOjfufr4GwoQNGmuPfQfg0aLvwPFICm5NO76OasMEicWvRQw/640?wx_fmt=webp&from=appmsg)

Out Of Bounds的Byung Young Yi（@yibarrack）攻击LiteLLM，单漏洞碰撞，$17,750加3.75分。

![](https://mmbiz.qpic.cn/mmbiz_jpg/tbTbtBE6TibcqSmpcmZDGUcY8Cj4icibuMSicpCeDRiabCcic58qljhgrfcFaV7ZTHLmIicmvcnqTdxp3q5s8RkSI3o7oggZTHpy8E1PuxTufGUOnE/640?wx_fmt=webp&from=appmsg)

0xDACA（@0xDACA）和Noam Trobishi（@NTrobishi）用use-after-free漏洞第二轮拿下NV Container Toolkit，$25,000加5分。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/tbTbtBE6Tibe2cc99n3SPjh38ibofQTzcibKTJOthWAicTjSJx66VicGibZQiaIT7cLZBoQWKuaVUCMUoPUqpw4cHE7mrJKVeN1ibg1D4LiarjEaagVg/640?wx_fmt=webp&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_jpg/tbTbtBE6Tibdt5icGstOia0VypTpCMluRFee3eD4icanFacw9QNEXCJfm1qvmK6KS6rxiaZEibrG8qhoVTVDGQLJHYkTzdn28zbl2Lh3DSRDOgKpg/640?wx_fmt=webp&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/tbTbtBE6TibeCatgHNYOfhSfNvpZ2BO63ZpvDIdib24eyuhSoAPoawMyWAic01DyaNHrDR8KOFagZXKDbXyia55OGnkCgogRF5RTQ8kbd8oTjLI/640?wx_fmt=webp&from=appmsg)

## 最后一天看什么

两天下来，漏洞类型从use-after-free到整数溢出再到代码注入，目标从浏览器、操作系统一路打到AI编码工具和企业邮件系统。Exchange那20分的大活儿基本上让DEVCORE稳坐钓鱼台，但Pwn2Own的规矩是不到最后一刻不封盘。第三天还会有哪些靶标被拿下，以及有没有人能从DEVCORE手里抢走Master of Pwn，值得盯着。

---

### 参考资料

[1] https://www.zerodayinitiative.com/blog

[2] https://www.twitter.com/thezdi

[3] https://infosec.exchange/@thezdi

[4] https://www.linkedin.com/company/zerodayinitiative

[5] https://bsky.app/profile/thezdi.bsky.social

[6] https://www.zerodayinitiative.com/blog/2026/5/15/pwn2own-berlin-2026-day-two-results

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/KK6rkaWbMNbNvNRWVlQ1KyqceSk3WZAqKUsEjFj2Mfib1H7RQOOarzKolWvdD1W3PGicFOEABZLLpNoL2u9RdAXg/0?wx_fmt=png)

幻泉之洲

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/KK6rkaWbMNbNvNRWVlQ1KyqceSk3WZAqKUsEjFj2Mfib1H7RQOOarzKolWvdD1W3PGicFOEABZLLpNoL2u9RdAXg/0?wx_fmt=png)

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