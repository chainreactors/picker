---
title: 起底AI中转站
url: https://mp.weixin.qq.com/s/PcI1XXT1EdnJjurHRwCgdg
source: Doonsec's feed
date: 2026-08-14
fetch_date: 2026-08-15T02:48:20.031447
---

# 起底AI中转站

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/2sHfY8zAtFx5QXrgoiamcxEYNw3lJ4wx4byKCzujHMwR42sryvxlmeMU8UTXibdJovcAMiajn1NBerbfVibjA1rnvbRUibZsUKz8zSF4dnVJhAF4/0?wx_fmt=jpeg)

# 起底AI中转站

360Quake空间测绘
360Quake空间测绘

360Quake空间测绘

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

![](https://mmbiz.qpic.cn/mmbiz_png/2sHfY8zAtFzeytibhAMMTnWtKEoLXIej2cXQ7osRKEs9YpH5VzRslENL300yFpx7ITzhWHicDNO8ibian1wp6otr0dIKu8unlFG9jLNwzdMKxHo/640?wx_fmt=png&from=appmsg)

**起底AI中转站**

![](https://mmbiz.qpic.cn/sz_mmbiz_png/2sHfY8zAtFyGRVVedAWzrHxWG7sdZbmtickxcUoKdibxLGraKRLJUKl9xbwCKyuxsqJDGT3R25QSiajVGQiahOHEibDc5fSSicNibdNQ46rx2F8X1g/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/2sHfY8zAtFx598mkVcUE2QZjoLGtFc2icia7SzkuTehH3D3QPtdZRic6x124BSq1mZp8Ps50UZd52ooXxRRhIeEenDE9OiaNW3vFGzvcNmS6jbQ/640?wx_fmt=png&from=appmsg)

**全网40万资产暴露**

**你的API秘钥可能正在被“中转”**

用 Quake 对全网 AI 中转站做了一次完整测绘。这里说的"中转站"特指承担密钥管理 + 协议转发 + 计费分销的后台/网关类基建——光 New API、One API、LiteLLM 三款就超过 40 万资产，国内占近一半。

本文带你拆解它们的指纹、分布与背后的安全账。

![](https://mmbiz.qpic.cn/mmbiz_png/2sHfY8zAtFyz0Ik9S1YetwzF2ZbZyHs1r51Nj999TALU8VlaZGzXTgmiaMScmibIyiaNcwWtNOywicdNcfRbGDtdNk1VzgGLib0kDXaOSgZjZKcg/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/2sHfY8zAtFydaAEuu2T5n920Umpc62YJ4iafHsFOQP8a3BlHhgLSzGicbhiba7TswO1fqwIiafa7HicXTFedPMJCAupxu1IdEpZ71eO8oR4ldHfI/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/2sHfY8zAtFxEwvFm74HMiccVeHXbnjCzgib1IWic3VibknYXlyh0onoEcBalDuCnfYliaejttdUkicU3PvQ1N9ESAGEg9ibkXc14dxydpicGCRlDGy4/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/2sHfY8zAtFw5k9UN0OD4k00ianrcvqmeMF21wMdibnic6Y2x3X9XAMXyz8HrTwnDO4hQa5WZBxeMOKs7IaeYMg23S5pKibPG8Sl47ZJJYiaAtI4Y/640?wx_fmt=png&from=appmsg)

**1**

**什么是AI中转站？**

简单说，AI 中转站就是一个"API 二道贩子"：它在前面接 OpenAI、Claude、Gemini 等大模型官方接口，在后面统一对外提供兼容 OpenAI 协议的 /v1/chat/completions 端点。用户把官方 Key 换成中转站发的 Key，就能：

* 绕过地域限制：官方不服务的地区，中转站能转一手；
* 聚合多模型：一个 Key 调多家模型，按量计费；
* 降价分销：通过渠道差价、聚合流量拿到更低单价。

围绕这套需求，开源社区催生了一批中转后台/网关项目——One API、New API、LiteLLM，它们负责密钥池、渠道、计费、鉴权，是中转生态的"服务器端"。

区分一下容易混淆的东西：NextChat、ChatGPT Next Web、LobeChat 这类是前端对话 UI（自己连官方 Key 就能用的聊天界面），不承担对外发 Key、聚合计费的中转职责，多数是个人自用部署，不在本文统计的中转站范围内，已从数据中剔除。下面所有数字只针对真正的中转后台/网关。

问题也随之而来：中转站本质上是把别人的 Key 和别人的请求做了一次中间人转发。它暴露在公网上时，安全风险被一并放大。

![](https://mmbiz.qpic.cn/mmbiz_png/2sHfY8zAtFwnGN9QZUG3V7lIRP9xgKD8nghP6uyvsInibyTN4UiciaibzdC9dEez2TdKN7CcicaE5IvSfOLOBS0VVSHXoP8Wu0MPgEykCicGXQ0us/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/2sHfY8zAtFwrDxRkSDn9tIzbXqVqxEvxMGYn4JJltibUkgpaAruqgWdy16YUUOZTdVtqHUXZ8N3naPMtZMIYLBuocdK7yv3YP6NCxghm3CaA/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/2sHfY8zAtFwd9y25gWAwuG9zcIwNiblSemSL9KzHz6ibJjysLMw24cwTeM2icQzTdJK2ljScaHYia2SppDvjQhu7V6sgzKk8t0hbDxibW6TGdlQk/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/2sHfY8zAtFxgtU7JV9Aa4EJ7nC6BguOHbibYXAG5FPmX4Hk0liaqTWEpume2c91HFzibCIVY1GV4iaJh43yOmrJgqot0moXzFz0b5vlwhvturP4/640?wx_fmt=png&from=appmsg)

**2**

**全网暴露面：40万资产，国内占近半**

我们用 Quake 对三款主流中转后台/网关做了 title 指纹测绘，组合检索语句：

![](https://mmbiz.qpic.cn/mmbiz_png/2sHfY8zAtFwSsyGvJ64zWEDmJ4ia8uzqGLc0h8KiaqHvaSAhAbs1GAk5ycViasHKajRTdgS8Ju5FNaaMFVrnibibNU420a8Ud8L5ibhXBkMbr6Fwo/640?wx_fmt=png&from=appmsg)

全网命中约 40.9 万资产，地理分布 Top12：

![](https://mmbiz.qpic.cn/mmbiz_png/2sHfY8zAtFztj4gDa9QKgrNPhLEG25FcnWicPclrtiaMQO3qqLqicGAn7dFxaPyBOpOibJgGAqFibVwKk9NTdOPjFN1XlZIUNLEfu3G9Zlibtv9TA/640?wx_fmt=png&from=appmsg)

**两个观察**

* 中国 + 美国合计占约 74%。中国是供给端（大量个人/小团队自建分销），美国则多为云主机上的部署——两国加起来 30 万，几乎是这个生态的全部基本盘。
* 新加坡、日本紧随其后，与"绕地域限制"的典型链路完全吻合：中转节点常落在网络出口附近的机房。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/2sHfY8zAtFwZjqrxkIufz4K5ZXYPoUFCu0fyuqAbBtLDn2dOO9icctjicibx3rYzfoMm6SMRZmLGicv3TNtNWcAyLiakKSpSDbfDYA4E2XSHPwPg/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/2sHfY8zAtFw7KHBEcgF8eKZ6HmTzK3mFrU4UXEabTntEn6s0cU0m2e5xFJT0ibC1uQGjbFiazsP2wXeN0TBNuA4y0alfiaSe8tq9ocLF4SjzME/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/2sHfY8zAtFynf4nHYNkkuJydiafAQpVnE5P6kCwxicAJjvOwZnrrp93zicI0AApnxHEn0ZQygcd3V6zRqUEbrjnkarjqgVk4HMk16uGv3qQnzk/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/2sHfY8zAtFyeJl8xHyymK5HDSDBWicPrKL3BXVc937kMic1Ig5DBKmCBWKVibRBSqkGnnONIgNGIn7zf941T7ia2htwq4WORD5SgflpNyI7oh6U/640?wx_fmt=png&from=appmsg)

国内深入

**香港一地独占 5 万，阿里云成最大宿主**

把镜头拉到国内。组合检索语句限定 country:"China" 后聚合，国内命中约 17.2 万资产，分布呈现高度集中的特征。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/2sHfY8zAtFyWgLwQZPnxNNRjR2lOlBR56IvNlxTicCjfgFibXyEkAJf3iaiaMm9LVyKgOM8KXvG62SY6X2nTsrehnRfAenpKuia3D9BlnLjJXNF8/640?wx_fmt=png&from=appmsg)

**省份分布Top 12**

![](https://mmbiz.qpic.cn/sz_mmbiz_png/2sHfY8zAtFwFNs3P50A2lKQ0FGTvjM4X9CJbhS0AB8X2XsXvjRYTmK8WennicOnPuj9TBviczPaibVcHlwYERjViasDFXfvfkuHZ1KCbDlxmDdQ/640?wx_fmt=png&from=appmsg)

一个反直觉的结论：香港以 5.0 万资产独占全国榜首，超过北京、上海、广东任何一个单独的省/直辖市。

这恰好印证了中转站的"出境跳板"属性——大量部署者把节点放在香港机房，既贴近国内用户、又方便对接境外大模型 API。

香港 + 北京 + 上海 + 广东四地合计 12.6 万，占国内总量的 73%。

**城市分布 Top 10**

![](https://mmbiz.qpic.cn/mmbiz_png/2sHfY8zAtFy1U8ALcibvYYUHoQRn2aQPvaJw5ibVoPcBa3Qcqy9M4nDRC1MhIAYcujXNAya6oaU4RntX7aHg0bySegzZAM2YMbqcuT0drfLvo/640?wx_fmt=png&from=appmsg)

广州+深圳合贡献广东的过半体量，杭州撑起浙江的 78%——北上广深杭五城是中转后台在国内的绝对重心。

**ISP / 云厂商分布**

![](https://mmbiz.qpic.cn/mmbiz_png/2sHfY8zAtFyF1ZEqK40pjtaZGdysj9VgN1r386jhLOiaRNkfODiclia6icxV61Wy2HZjpTANTMWZJ92yIicQ2BnF4TnBSfTZ2icwUH2wAicwbw8Cias/640?wx_fmt=png&from=appmsg)

阿里云以近 5.3 万资产成为国内 AI 中转站的最大宿主，腾讯（3.3 万）、电信（约2.5 万）紧随其后。

前三家合计承载了国内六成以上的中转基建。值得注意的是 cognetcloud、NetLab Global、Cloudie 等"非主流"小 IDC 也挤进前十。这类厂商常以"宽松政策、便宜带宽、少审核"为卖点，是中转/代理类业务偏爱的落地点，安全水位参差，是供应链风险的高发区。

**端口分布**

![](https://mmbiz.qpic.cn/sz_mmbiz_png/2sHfY8zAtFyVaQ8EPQ5rs3h9ysCmJo6lehwCgkU2rF7NQfkoDb7MdNZicu03iamfdQsGs91pFf9bBCbgWA33VNZSBMeuEct7rKFOUCeiatIdkI/640?wx_fmt=png&from=appmsg)

3000 端口以 6.0 万资产一骑绝尘——这正是 New API、One API 等项目开箱即用的默认端口，说明绝大多数部署者根本没改默认配置。

结合"裸 80 端口近 1.6 万、默认端口未改近 6 万"这两个数字，可以推断：国内中转站普遍是"拉起即用"的最小化部署，安全加固几乎为零——这也是后面四本安全账能成立的物理基础。

![](https://mmbiz.qpic.cn/mmbiz_png/2sHfY8zAtFxR4WFEbhkkOZS18cskp61zgY11waLIGZJrb7EkE2cWmQicYgZ7SG3ORA8s0raTThicPib77GE3nYP2Z9mxjWMbvoLJ7Vak3LfOF8/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/2sHfY8zAtFzciba1De56Rr8wYkibjAxZsgJ0vsMcIQia6sUf5y0wR6LTQ7SU7JWmfDib0ibWWBBp9dSPl7K1pibSO6ej7PBCdNhmbDJNVk7ucW3sE/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/2sHfY8zAtFzK068FKC5IKeswZqDyE0OMpk8cd4a6rHG4SdaXiar3hdEYmTnjicCPtQNK6cpFtdibYavo0tBWsKibib0mFzW6Uibn5fz6Fiaib52wsibg/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/2sHfY8zAtFxZb8amiccwj1Axr9Q4Gf3Q3U9oKcBrbqzcibmfkPjsh7ga4tHfib9muicKVs66icfibx5zq8YNWEk5wzKU8YsM5EAvVfRC0y4Pxvibow/640?wx_fmt=png&from=appmsg)

**3**

**主流基建盘点**

谁在撑起这个生态？按单款中转后台/网关拆开看：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/2sHfY8zAtFwh6YdJkal79S6NSfdtF6icH8foVYsh4xiaI05t10ppmkxvaZicFPWPC1tNzBZswbs1xf7nfvvM9mLrtX3kPOo8YnZzJHlZLdjicq4/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/2sHfY8zAtFwl8EdsyVianCydokZCSvVVmXzetOiaIDhPxYMqQXhlp0n0Ox9JkibHV2GxibKmwETTgxgCiaUKAg4n8Aof7Opn7ghicoajedboETEjY/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/2sHfY8zAtFyQDRdzDOOD0Q7b4q0A7wVFELSib42o9JDd3iceLnZJ3MlX4LXLqcxMaKzCIEcy6KEmUMbemCGic6qxCsB5MwhlRiaCvfu2lqvWO2Q/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/2sHfY8zAtFzqhJ5sRtCgsLb3bT9InFvWYPibTvZGfz4tz3rxXsmlRfUITtZkKuqo7ue7EnxM7ceuVCIr9YVZeosu19KLibv4K2XhFmYEUuHdM/640?wx_fmt=png&from=appmsg)

**几个要点**

* New API 是当之无愧的"中转一哥"，23 万资产，单款就占整个中转生态的过半。它是 One API 的二次开发分支，功能更全（多模型聚合、计费、分销层级），是国内分销圈最常被部署的项目。
* LiteLLM 以 9.1 万位居第二。与 New API/One API 的"分销后台"定位不同，LiteLLM 是企业侧的 LLM 网关/代理（统一协议、负载均衡、成本管控），它的 Swagger UI 默认挂在公网，常被当成中转节点裸奔部署。地理上美国（2.66 万）反超中国（0.75 万），说明 LiteLLM 更多被海外团队和云上业务采用。
* One API 作为老牌项目仍有 8.6 万，与 LiteLLM 体量接近，但增速已被 New API 反超。
* 体量小的 Veloera、VoAPI、Uni-API 多为细分圈子的二开项目，命中少但往往配置更随意。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/2sHfY8zAtFz0pwuoygOUmEmDKOTqUhF5wC4lgcXZORSguichGa6ia6sjcM1Vm66qpOTy4ic1xRu7PkdFicfsPWAptnMc7oj5MUqmZHQlfCuRSCo/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qp...