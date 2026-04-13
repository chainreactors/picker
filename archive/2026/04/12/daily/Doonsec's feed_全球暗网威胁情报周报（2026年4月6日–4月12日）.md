---
title: 全球暗网威胁情报周报（2026年4月6日–4月12日）
url: https://mp.weixin.qq.com/s/QOI8yUEyFC5NHtLxF_NHmQ
source: Doonsec's feed
date: 2026-04-12
fetch_date: 2026-04-13T04:54:14.580155
---

# 全球暗网威胁情报周报（2026年4月6日–4月12日）

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/es3jUghv8rib8Tiasken7RgtkZnlVqfib19H5HgiaLcxdAnNpavrpf8SXc96Gq4sV0x01XBd2icsDFiccxRiaUGGoqjabPLKibXlVk0atQLZaPT3KnE/0?wx_fmt=jpeg)

# 全球暗网威胁情报周报（2026年4月6日–4月12日）

原创

NightTeam
NightTeam

夜组OSINT

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

## 📌 执行摘要

过去7天全球网络威胁活动维持高位，共监测到 **433起** 重大事件：

* **数据泄露**：297起（涉及129个攻击者，58个国家/地区）
* **勒索软件**：136起（涉及33个攻击团伙，36个国家/地区）

![](https://mmbiz.qpic.cn/sz_mmbiz_png/es3jUghv8r9gMskdYCLS6dExh372Mws5BKN3SPTDs5icpjYjutiaRErDovicO0X7oiaSEkfX2pqrELYaZKJfpQhPLhsRpq93wBZMPMyibV0egiaWA/640?wx_fmt=png&from=appmsg)

**核心趋势**：

* 数据泄露以**scattered LAPSUS$ hunters**（63起）和**xorcat**（14起）为主，Grubder在本周早期仍保持高活跃，呈现“批量收割+快速变现”特征。
* 勒索软件高度集中，**The Gentlemen**（27起）、**akira**（16起）、**Qilin**（14起）三团伙已占全部事件的41.9%。
* 美国仍是两大类威胁的最大受害国（数据泄露42起、勒索软件54起），墨西哥、以色列、法国紧随其后。
* 高价值目标频现：伊朗IRGC军事情报数据库、以色列机密数据、NSCC超级计算中心、印度选举委员会、T-Mobile等。

## 🔥 数据泄露周报（297起）

![数据泄露](https://mmbiz.qpic.cn/sz_mmbiz_jpg/es3jUghv8r8wicSEYE2wc1T6NofzZeXl6v1KKLb3R8BNuYGBtajUf54mN9KwpP5AvAEicc4fy3kIHgozxgiacyDybRPviaCw9ZnVdEOHb2fpylg/640?wx_fmt=jpeg&from=appmsg)

数据泄露

**最活跃攻击者Top10**

| 排名 | 攻击者 | 事件数量 |
| --- | --- | --- |
| 1 | scattered LAPSUS$ hunters | 63 |
| 2 | xorcat | 14 |
| 3 | Dedale Office | 8 |
| 4 | ShinyHunters | 8 |
| 5 | Arnoldsudney | 6 |
| 6 | SpeakTeam | 6 |
| 7 | Datavortex | 5 |
| 8 | crazyboy68 | 4 |
| 9 | XP95 | 4 |
| 10 | NormalLeVrai | 4 |

**受害国家/地区Top10**：美国（42起）、墨西哥（20）、以色列（19）、法国（17）、西班牙（14）、英国（12）、印度（11）、俄罗斯（10）、中国（9）、哥伦比亚（8）

**重点行业集中度**：电子商务与在线服务占43.6%，政府管理11.5%，金融服务14.7%。

## 🔥 勒索软件周报（136起）

![勒索软件](https://mmbiz.qpic.cn/sz_mmbiz_jpg/es3jUghv8r94nhIc5olvbUuFjKkN94Iiau2icyiayDibgCct30fSztgOkyDdtWNA2SeMj7DZv4RAEOSr5WZxbRSDJroewThuoAVP0KqO6YRPiclo/640?wx_fmt=jpeg&from=appmsg)

勒索软件

**最活跃团伙Top10**

| 排名 | 团伙 | 事件数量 |
| --- | --- | --- |
| 1 | The Gentlemen | 27 |
| 2 | akira | 16 |
| 3 | Qilin | 14 |
| 4 | INC RANSOM | 9 |
| 5 | PEAR | 7 |
| 6 | CoinbaseCartel | 7 |
| 7 | KRYBIT | 5 |
| 8 | AUDIT TEAM | 5 |
| 9 | NightSpire | 4 |
| 10 | LOCKBIT 5.0 | 4 |

**受害国家/地区Top10**：美国（54起）、英国（8）、法国（5）、澳大利亚（5）、加拿大（4）、中国（4）、西班牙（4）、埃及（4）、印度（4）、中国台湾（4）

**重点行业集中度**：房地产26.7%、医疗与生命科学24.4%、制造业20.0%、科技13.3%。

## 📈 整体威胁态势分析与防御建议

1. **数据泄露**：scattered LAPSUS$ hunters单周63起，占总数的21.2%，主要针对美国、墨西哥、以色列的教育、科研和政府机构。公民身份数据、科研项目数据、登录凭证成为主要变现标的。
2. **勒索软件**：The Gentlemen单周27起，占总数的19.9%，重点打击美国、英国、澳大利亚的房地产、医疗和制造业。双重勒索（加密+数据泄露）仍是主流手段。
3. **交叉风险**：同一周内，SpeakTeam（数据泄露）与The Gentlemen（勒索软件）均对墨西哥教育/企业目标发起攻击，显示部分团伙已形成“数据窃取→勒索”复合攻击链。
4. **高风险国家**：美国（96起总计）、墨西哥、以色列、法国。中国企业需警惕xorcat与scattered LAPSUS$ hunters的持续收割。

**重点防御建议**：

* **企业**：立即核查是否出现在scattered LAPSUS$ hunters、The Gentlemen、akira受害者名单；加强备份隔离与EDR部署。
* **政府/科研机构**：重点防范IRGC数据库、以色列机密数据、新加坡NSCC等高敏泄露的后续利用。
* **高风险行业**：房地产、医疗、制造业、电信、金融需提升24小时威胁监测等级。
* **通用措施**：启用凭据泄露监测服务；每日更新Top10团伙IOC；开展全员反钓鱼与勒索软件演练。

## 威胁情报全球监控系统

由全球威胁情报系统（dark.libaisec.com）实时监测发现，订阅会员可查看威胁情报详情。

![dark.libaisec.com](https://mmbiz.qpic.cn/mmbiz_jpg/es3jUghv8ribibWxrSicH09cCr0kXFWNcAxxNicicxSfm4foo7Zrt3EiauiaewcRPTnSKAIxC8r9chmlQuP0icTXz3R0NMicl6qr7zJm6Ffbh4hh8shQ/640?wx_fmt=jpeg&from=appmsg)

dark.libaisec.com

**监测内容**

* 数据泄露事件
* 勒索软件事件
* DDoS攻击事件
* 恶意软件事件
* 访问权限售卖
* 网页篡改事件
* 日志泄露事件
* 网络钓鱼事件
* 漏洞情报监控
* ......

系统会员了解及订阅可联系以下微信，备注来源【威胁情报】

![威胁情报](https://mmbiz.qpic.cn/sz_mmbiz_png/es3jUghv8ricAqGHUWHoCGbtOGs0CdYlWpQjcge0IJCwp8bL10tfTc5mKibeS9v26miaLBJWBpw7Dk2QI3sC2CHs25Z0jw6ga8oj96icwa5QGq0/640?wx_fmt=png&from=appmsg)

威胁情报

预览时标签不可点

阅读原文

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/sz_mmbiz_png/GLyX5CgG8A1AjQiarwFHPJibeWbc1nhED6yPPhcfplNAzMjXJx106p9J3HaRZUNyBAhECfklMPvyOsReia0qaVV8A/0?wx_fmt=png)

夜组OSINT

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/GLyX5CgG8A1AjQiarwFHPJibeWbc1nhED6yPPhcfplNAzMjXJx106p9J3HaRZUNyBAhECfklMPvyOsReia0qaVV8A/0?wx_fmt=png)

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