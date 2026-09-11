---
title: 【黑产链分析】域名过期一年后，武汉某职业院校公众号成了色情站的免费流量入口
url: https://mp.weixin.qq.com/s/Nc_pdNB-a3pa-Nfxa6OFUg
source: Doonsec's feed
date: 2026-09-10
fetch_date: 2026-09-11T06:48:50.865480
---

# 【黑产链分析】域名过期一年后，武汉某职业院校公众号成了色情站的免费流量入口

# 【黑产链分析】域名过期一年后，武汉某职业院校公众号成了色情站的免费流量入口

原创

金夏
金夏

金夏安全

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

最近电脑坏了，导致推文有时差问题。

星期二下午，在一个阳光明媚的日子，笔者在悠哉悠哉冲浪呢，突然YY大佬发了一个聊天记录出来。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Iv8D5nD32icKrfibm79Yo7KXdZM6ngibHanykd2s5zvMuF7bDvd3MdddhhwyFudmrF4yLsMR5yOs1jEOvQdb81YQficMX0wosbfuYV1gcwDLdKg/640?wx_fmt=png&from=appmsg)

本来想着今天难道又是被KFC戏耍的一天？但当笔者点进去时候发现事情并不简单

![](https://mmbiz.qpic.cn/mmbiz_png/Iv8D5nD32icL8bFic3bDUYgKPt8dX9SsvIM2BhiaYo4sDMsicSEq945kF1pxicgZKpsreJXRWSjtxFMj3zp1QGecKTgS0icxAAUicZiaV0QjXGjibnnM/640?wx_fmt=png&from=appmsg)

点开后，映入眼帘的是免费看片四个大字以及一些不堪入目的东西，作为一个资深抗拒诱惑的世内高人，我断然关掉页面，不禁感叹道，真是世风日下，堂堂学府大院，岂能容忍如此污秽之物？

我要看看是哪个胆大妄为之徒胆敢跑来大专圣地传播此等淫秽之物。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Iv8D5nD32icIjw4SVrt7MZYyAQibaCz9A9HsHbB0iaXvxsjJTe6nrzPJoefxObW7cicuFgJU4D65xo33K3JBotpTxQv8Xe61p6dxmv5nP8XfyRM/640?wx_fmt=png&from=appmsg)

事件性质：域名抢注引流。不是公众号被入侵，不是学校官网被黑，而是原域名过期未续费被抢注转卖。

学校公众号「微校园 → 单招成绩」这个菜单，点进去跳的是色情网站。查了一圈，既不是公众号被入侵篡改，也不是学校官网被黑——真正的原因是学校原域名 w\*\*\*e.com 过期未续费，被 DropCatch 抢注平台拍卖后，转卖给了色情影视站运营者。

抢到域名的人拿它搭了个 MacCMS 色情站，叫「万花影院」。学校其实早就迁到 wh\*.edu.cn 了，但公众号菜单里的老链接一直没换，就被这个站当成了免费流量入口。往下挖，这条线上还挂着一整套域名抢注 + 色情站群 + 资源供给的链条，规模不小： 至少 500 个域名、3 个内容品牌、14.5 万条影视资源（含 4950 条色情内容）。

顺着这条线，我锁定了两个没做隐私保护的真实注册邮箱（x\*\*\*9@gmail.com、5\*\*\*8@qq.com）和一个 2789 人的 Telegram 运营频道（@m\*\*\*e），可作为执法调取实名信息的关键线索。

关键数据一览

|  |  |
| --- | --- |
| 500+抢注域名 | 14.5万影视资源条数 |
| 4950色情内容条数 | 2789Telegram 频道成员 |

## 01  事件时间线

从域名注册到事件曝光，这条线有一年多。

我把关键节点按时间顺序摆出来，标红的那两个是整个事件真正的转折点。

|  |  |
| --- | --- |
|  | 2025-08-08NS 集群域名注册  x\*\*\*s.com 在 Gname 注册，用于后续管理 500 个抢注域名 |
|  | 2025-09-09w\*\*\*e.com 早期证书  w\*\*\*w.w\*\*\*e.com 和 w\*\*\*e.com 各申请一张单域名 SSL 证书（此时域名可能仍在学校手中或刚被抢注） |
|  | 2025-11-22w\*\*\*e.com 被 DropCatch 抢注  域名过期未续费，DropCatch.com 647 LLC 抢注成功，NS 改为 x\*\*\*s.com（色情站群统一 NS） |
|  | 2026-06-16资源站 API 域名注册  m\*\*\*9.vip 注册，作为色情站群的资源采集 API 服务器 |
|  | 2026-07-01泛域名证书签发  \*.w\*\*\*e.com + w\*\*\*e.com 泛域名 SSL 证书签发，运营者开始全面接管所有子域名 |
|  | 2026-08-24泛域名证书续期  \*.w\*\*\*e.com 证书续期，运营者持续控制该域名 |
|  | 2026-09事件曝光  用户点击学校公众号「单招成绩」菜单，跳转到色情站「万花影院」，标题显示《吃了春药的邻居春晓》 |

## 02  事件起因

2026 年 9 月，YY大佬反映武汉某大专学院的官方公众号不对劲：点底部菜单「微校园 → 单招成绩」，跳出来的不是成绩查询系统，是个色情网站。

我手上拿到的线索如下：

一个聊天记录，说"有人把学校公众号改成片了"；

第一反应肯定是公众号被入侵了，菜单被人改到了恶意站点。但我抓包看了之后才发现，事情没这么简单。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Iv8D5nD32icIjw4SVrt7MZYyAQibaCz9A9HsHbB0iaXvxsjJTe6nrzPJoefxObW7cicuFgJU4D65xo33K3JBotpTxQv8Xe61p6dxmv5nP8XfyRM/640?wx_fmt=png&from=appmsg)▲ 点击之后——「午夜版《吃了春药的邻居春晓》」。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Iv8D5nD32icIHcGEtHWFDQIVrEdDGneCcuyDl3eCPCI1xZ4TgsyBo1orTWR3q13MV1tXrJd2r3hmdt8lIAqh7bRlBbqd3vHAzGQsPa2dlUjU/640?wx_fmt=png&from=appmsg)

▲ 学校公众号底部菜单。「单招成绩」这个入口，点下去跳的已经不是成绩查询系统了。

## 03  被利用的域名和它背后是谁

2.1  页面身份确认

我通过微信 UA 抓了一次 selectfen.asp，HTTP 200 返回 31547 字节完整 HTML。这是一个基于 MacCMS（苹果 CMS）搭建的色情盗版影视站，站名「万花影院」。

关键特征：

• JS 配置 maccms222222 中 url:"w\*\*\*e.com"

• 模板路径 /template/default3/

• 图片资源来自 m\*\*\*2.com（茅台资源站 CDN）

• CNZZ 站长统计 ID：1\*\*\*4

• 底部版权：Copyright © 2019-2026 万花影院 w\*\*\*e.com

我又扒了同站群另一个站的源码，MacCMS 的前端配置全写在页面 HTML 里，一眼就能看到：

```
{ "path": "", "mid": "", "url": "0***o.com",   "wapurl": "wap.test.cn", "mob_status": "0",   "tplurl": "/template/default61/" }
```

这是 MacCMS 的标准配置格式。url 字段把站点域名直接写死，tplurl 指定模板目录。而 wapurl 那儿还留着默认值 wap.test.cn，说明这帮人是批量部署的，压根没挨个改默认配置——典型的站群操作。

更直更直接的证据在 Meta 标签里。页面的 description 自己就把性质写明了：

<meta name="description" content="【青鸟影视】是一个免费porn电影电视剧的网站， 提供高清热播电影电视剧免费观看..." />

人家自己在 SEO 描述里就写了 "porn"，这就不用我判断了。

2.2  域名性质：不是被黑，是被抢注

这是整个事件里最要命的一环。w\*\*\*e.com 和 w\*\*\*w.w\*\*\*e.com 都解析到 23.\*\*\*.\*\*\*.192（美国加州洛杉矶，Cnservers LLC/CloudRadium，AS\*\*\*65）。我查了 WHOIS(RDAP)，结果如下：

|  |  |
| --- | --- |
| 字段 | 值 |
| 注册时间 | 2025-11-22T19:14:55Z |
| 到期时间 | 2026-11-22 |
| 注册商 | DropCatch.com 647 LLC （过期域名抢注拍卖平台） |
| NS 服务器 | NS1.X\*\*\*S.COM NS2.X\*\*\*S.COM （随机字符串域名） |
| 域名状态 | client transfer prohibited |

这是 RDAP 协议返回的原始注册数据：

{

  "ldhName": "w\*\*\*e.com",

  // 域名名称（LDH = Letter-Digit-Hyphen 格式），

  "handle": "1234567890\_DOMAIN\_COM-VRSN",

  // 注册局分配的域名唯一标识，后缀 DOMAIN\_COM-VRSN 表示 .com 域名的 VRSN（VeriSign）注册局记录

  "status": ["client transfer prohibited"],

  // 域名状态：注册商层面禁止转移（client 表示由注册商设置）

  // 作用是防止域名被未经授权地转出到其他注册商

  "events": [

    {"eventAction": "registration", "eventDate": "2025-11-22T19:14:55Z"},

    // 注册时间：2025-11-22 19:14:55 UTC

    {"eventAction": "expiration",   "eventDate": "2026-11-22T19:14:55Z"}

    // 到期时间：2026-11-22 19:14:55 UTC

    // 注册周期为 1 年

  ],

  "nameservers": [

    {"ldhName": "NS1.X\*\*\*S.COM"},

    // 主名称服务器，负责该域名的 DNS 解析

    {"ldhName": "NS2.X\*\*\*S.COM"}

    // 备用名称服务器，与 NS1 同属 X\*\*\*S.COM，通常为同一服务商

  ],

  "entities": [

    {"roles": ["registrar"], "vcardArray": [...]}

    // 注册商实体：角色为 registrar（注册商）

    // vcardArray 为联系人/机构信息，此处内容被省略，故无法确认具体注册商

  ]

}

注册时间 2025-11-22 是关键。这个点正好卡在 whvcse.com 过期之后。DropCatch 就是专门做过期域名抢注拍卖的平台，它出现在这里，说明域名是过期删除后被抢注的——不是原持有者续费，更不是黑客入侵改 DNS。

关键发现

w\*\*\*e.com 的注册时间卡在域名过期被释放的那个点上。说白了，学校原官网域名过期后没续费，被 DropCatch 抢注，再拍卖转手卖给了做色情站的人。

学校真正在用的官网是 www.whxxx.edu.cn，我查了一下，HTTP 200，正常在线。估计学校是在某个时间点从 w\*\*\*e.com 搬到了 whxxxx.edu.cn，但老域名过期后忘了续费，公众号菜单里的链接也一直没人动。

2.3  泛解析接管所有子域名

域名到手之后，运营者直接上了泛解析 \*.w\*\*\*e.com → 23.\*\*\*.\*\*\*.192，包括 erp、oa、jpkc、gggz 等学校原业务子域名，以及 0-9、a-z 等任意子域名，全部指向同一个色情站服务器。这意味着学校以前所有挂在 w\*\*\*e.com 子域名上的系统，只要外面还有链接引着，现在点进去全是色情内容。

2.4  路径白名单防护

这个站防护做得很严。只开放 selectfen.asp + /template/ + /static/ 这些静态资源，首页、播放页、后台、API、安装文件、APP 下载，一律 403。

代理 IP 也被封了，我走 clash 的时候连接直接被重置。看得出来这帮人有点安全意识，只把自己需要引流的入口露出来。

## 04  基础设施与资源供给链

3.1  图片 CDN：茅台资源站

w\*\*\*e.com 上所有视频封面图，全来自 m\*\*\*2.com。这个站的标题写着「茅台资源站」（mtzy 就是茅台资源的首字母），是个盗版影视采集站，给下游的色情站供内容。

![](https://mmbiz.qpic.cn/mmbiz_png/Iv8D5nD32icLdOyb6riapMZxe7jOvQJFk6BGFtriaJkvXDTKMMuy5KxACARCVQkeEgzR909Jxxvx5Et8cWqhKJZkc64mViazAQJzFwk315yloPU/640?wx_fmt=png&from=appmsg)

m\*\*\*2.com 的图片走 CDN：

域名

m\*\*\*2.com

▼

CNAME 指向

y\*\*\*o.c\*\*\*e.org

▼

最终解析 IP

51.\*\*\*.\*\*\*.234
加拿大魁北克 OVH，AS\*\*\*76

3.2  茅台资源站帮助中心挖到核心信息

在 m\*\*\*2.com 的帮助中心页面里（55606 字节），我把运营者的基础设施清单整出来了：

官网地址列表：m\*\*\*y.me、m\*\*\*0.com、m\*\*\*y.cc、m\*\*\*y.com、m\*\*\*n.com

核心 API 服务器：c\*\*\*i.m\*\*\*9.vip

P2P 商业加速解析：https://m\*\*\*8.vip:966/?url=

联系方式：QQ 群 7\*\*\*9、Telegram @m\*\*\*e

支持 CMS：MacCMS、SeaCms、FeiFei、MaxCms、CtCms、DuoMiCms、zanpianCms（7 种）

资源量：总计 145146 条

含「伦理片」分类（vodtype/34，即色情内容）

3.3  API 完全开放，无需认证

资源站的核心 API c\*\*\*i.m\*\*\*y.cc 是完全开放的，不需要任何认证，直接调就能把全部资源列表拉下来：

• 总资源量：145146 条，7258 页

• 53 个分类，包括电影、连续剧、综艺、动漫、伦理片（4950 条色情内容）、短剧大全等

• 短剧分类细分到「重生民国」「穿越现代」「反转爽剧」「言情总裁」等 7 个子类——运营者在追短剧风口

• 今日更新约 275 条

我采了 7980 条 API 数据做证据固定，其中包含 100 条伦理片样本（标题如「纳粹女魔头之病房狂魔」「天蝎座之夜4」「名妓」「迷情」等）。

资源供给链

茅台资源站是上游供货的，给 w\*\*\*e.com 这类下游色情站提供影视资源——图片、播放地址、元数据，全从它这儿走。下游站只做引流和展示，内容一条都不是自己产的。「上游资源站 + 下游引流站」这么分工，是盗版影视黑产的标准架构。

3.4  资源站群批量注册

我把资源站相关的 13 个域名拉出来批量查了 WHOIS，发现 m\*\*\*0.com、m\*\*\*1.com、m\*\*\*2.com、m\*\*\*y.com、m\*\*\*n.com 全部在 2024-10-30 同一天批量注册，注册商全部是 合肥聚名网络科技有限公司（juming.com）。这种操作不像个人干的，是有组织的批量囤域名。

|  |  |  |  |
| --- | --- | --- | --- |
| 域名 | 注册时间 | 注册商 | NS |
| m\*\*\*0.com | 2024-10-30 | 合肥聚名 | ns1/n\*\*\*2.j\*\*\*s.com |
| m\*\*\*1.com | 2024-10-30 | 合肥聚名 | ns1/n\*\*\*2.j\*\*\*s.com |
| m\*\*\*2.com | 2024-10-30 | 合肥聚名 | ns1/n\*\*\*2.j\*\*\*s.com |
| m\*\*\*y.com | 2024-10-30 | 合肥聚名 | ns1/n\*\*\*2.j\*\*\*s.com |
| m\*\*\*n.com | 2024-10-30 | 合肥聚名 | ns1/n\*\*\*2.j\*\*\*s.com |
| m\*\*\*9.vip | 2026-06-16 | — | — |

## 05  NS 集群与色情站群

4.1  x\*\*\*s.com：500 域名的管理集群

w\*\*\*e.com 的 NS 是 n\*\*\*1.x\*\*\*s.com 和 n\*\*\*2.x\*\*\*s.com——域名本身就是一串随机字符，看着就不对劲。我把这个 NS 下挂的所有域名查了一遍，总共 500 个域名。

后缀是这么分的：.com 395 个、.cn 73 个、.net 23 个、.org 7 个、.cc 2 个。命名模式：数字+字母 389 个、纯数字 101 个、含横杠 10 个——清一色数字开头的垃圾域名，典型的规模化抢注、停放、恶意引流集群。

x\*\*\*s.com 自身注册于 2025-08-08，注册商 Gname.com Pte. Ltd.（新加坡），NS 为 a\*\*\*1.s\*\*\*s.com / b\*\*\*1.s\*\*\*s.net。

4.2  站群扫描：30-60 个真实色情站

我拿这 500 个域名批量扫了一遍 /selectfen.asp 路径（也就是 w\*\*\*e.com 的入口路径），124 个有响应。排掉统一的 404 停放页，剩下大概 30-60 个是真的色情影视站，全都是 MacCMS 搭的。

已确认的色情站包括：

|  |  |  |  |
| --- | --- | --- | --- |
| 域名 | 站名/特征 | 模板 | 服务器 |
| w\*\*\*e.com | 万花影院（学校域名被抢注） | de...