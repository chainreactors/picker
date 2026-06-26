---
title: Vibe Coding 困了、累了， Claude 帮我点了杯瑞幸咖啡！
url: https://mp.weixin.qq.com/s/mznVbNSbbXI9e5c_Mmcquw
source: Doonsec's feed
date: 2026-06-25
fetch_date: 2026-06-26T06:06:08.964031
---

# Vibe Coding 困了、累了， Claude 帮我点了杯瑞幸咖啡！

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/0VE9kDxicLUgVJvnaia653JLlI53ld8lJEIBlOFriaZfWlYnnUXW5C9eb1H0qeDeIvAoqhClknpFTPPyKcuOIRqqXxV0ft7oncl4ubpZ42ZAiac/0?wx_fmt=jpeg)

# Vibe Coding 困了、累了， Claude 帮我点了一杯瑞幸咖啡！

原创

~
~

IoT物联网技术

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

![](https://mmbiz.qpic.cn/sz_mmbiz_png/0VE9kDxicLUiaYIruYos13I8DcFlpFsFSojrrC4jH8zt1dLuClbE2VX6iafQyRXZb2EH1Cm2A8iaxYBfDSTVztvmmYU0gkHJrCd8hEnOMlWbOJQ/640?wx_fmt=png&from=appmsg)

> 国内可用的组合 Claude Code + DeepSeek + Luckin MCP

最近，瑞幸咖啡把自己的能力蒸馏了，AI开放平台上线了，支持MCP、CLI、Skill三种接入方式能够实现查附近门店、搜索商品、、优惠券、点咖啡。

* 一句话下单：一句话发起下单，自动串联找店选品，关键节点确认后完成支付
* 智能优惠：自动匹配优惠券和咖啡库券，永不错过最低优惠
* 标准 MCP 协议：基于标准 MCP 协议，接入成本低，现有 AI 应用可快速集成下单能力
* 持久在线：登录状态保留一个月，免去频繁登录，日常使用更省心

格子间的牛马们，天天Vibe Coding 困了、累了，在 Claude Code 里随手一句话，点一杯瑞幸咖啡！

![](https://mmbiz.qpic.cn/mmbiz_png/0VE9kDxicLUjzsrHsw6lH3U4bbrJ1CCVbUVicmsdaOMIaUfWSmhzWFupibxKwCkI0pjfa3PmMSMQPC5HwicZ21ECVmwCtIuxAVROGdNfyuY2ibicI/640?wx_fmt=png&from=appmsg)

## 🤖 快速开始

![](https://mmbiz.qpic.cn/sz_mmbiz_png/0VE9kDxicLUiaYoiaiaKafbaSibHLkAo56FH5pzIulJxOHWwiaRtdJsY5bAe1HHQcYr8j4Z9Cvu0Bf0mxCrytGlcRYmc9Zl1FJaarkGl99bZBSOdM/640?wx_fmt=png&from=appmsg)

1.安装Claude Code

Claude Code 是 Anthropic 官方推出的强大的 AI 智能助手，帮你和 AI 大模型打交道，处理各种繁琐的日常生活、办公任务、软件编程等。Claude Code 对机器要求不高，参考如下

![](https://mmbiz.qpic.cn/mmbiz_png/0VE9kDxicLUiadRvohGqELSBsGXzD6SfERBKvn0NozIQ2HDtqXJibCERuCibSjRsAYZ6YJJLmCdchu7diaqcyQRtnPGhmWTeI33x7kibDFwZ1RHd8/640?wx_fmt=png&from=appmsg)

在国内安装Claude Code ，建议你先配置淘宝npm源

```
# 1. 设置淘宝为默认镜像源npm config set registry https://registry.npmmirror.com
# 2. 验证是否设置成功npm config get registry# 如果返回 https://registry.npmmirror.com，说明配置成功
# 3. 安装 Claude Codenpm install -g @anthropic-ai/claude-code
# 4. 验证是否成功claude --version2.1.185 (Claude Code)# 返回版本号，代表安装成功
```

2.配置 DeepSeek

Claude Code 本质是一个跑在终端里的客户端——它负责读你的代码、调工具、管上下文、跑那个「想 → 做 → 看」的代理循环。但它自己不会思考，每一步都要把请求发给某个大模型，等模型回话。默认这个模型是 Anthropic 的 Claude，在国内，我建议你换成DeepSeek。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/0VE9kDxicLUj0tUwTWWNBQG0PeNhdjIcpBR2QJUzFKLuoRicRQcY3Qg7AX79VcY1LbTUk5KXKzoDbSiav9ba2YPt18ZTYphBIkJMJMDAibWVIS8/640?wx_fmt=png&from=appmsg)

DeepSeek 是兼容Anthropic API 的，你只需要修改以下环境变量，其中 API Key 在 DeepSeek Platform 获取。

```
export ANTHROPIC_BASE_URL=https://api.deepseek.com/anthropicexport ANTHROPIC_AUTH_TOKEN=<你的 DeepSeek API Key>export ANTHROPIC_MODEL=deepseek-v4-pro[1m]export ANTHROPIC_DEFAULT_OPUS_MODEL=deepseek-v4-pro[1m]export ANTHROPIC_DEFAULT_SONNET_MODEL=deepseek-v4-pro[1m]export ANTHROPIC_DEFAULT_HAIKU_MODEL=deepseek-v4-flashexport CLAUDE_CODE_SUBAGENT_MODEL=deepseek-v4-flashexport CLAUDE_CODE_EFFORT_LEVEL=max
```

3.安装 DeepSeek

瑞幸咖啡开放平台 https://open.lkcoffee.com 注册账号，获取token，并安装瑞幸 My Coffee Skill。

![](https://mmbiz.qpic.cn/mmbiz_png/0VE9kDxicLUgtDWhlEbicZLaSJZ8JIiaYPHqzDb6icciaa8Jribwib9icpp3EKLYdqXIicO6F5N8GibtRdEneESvEWrRZKXc3SEhJ6AGOUAhicuSbft3ok/640?wx_fmt=png&from=appmsg)

打开 Claude Code ，让它自己安装瑞幸咖啡 Agent 即可

![](https://mmbiz.qpic.cn/mmbiz_png/0VE9kDxicLUhxATRerAP7QmPkshsPrBgXnN5LYIXoLvxibXAWySFgzELaZXFYrfiaEOnnbETRrmlLtK3PIsEIjG5ibQ7nibxRCs0WpU6vS61tpJc/640?wx_fmt=png&from=appmsg)

## 🌟 点杯咖啡

装好了后，你可以说出你的喜好，让 Claude Code 帮你点咖啡！

> 帮我点一杯瑞幸，其实我咖啡过敏，你看看有哪些不含咖啡因的可选？

![](https://mmbiz.qpic.cn/sz_mmbiz_png/0VE9kDxicLUh7pK0rLhrtMK6EIny83ORibciaSH9kjKyXfVw483HyX6LF1ziaHOCZpQqDC3rMibvzSCibYnt89J2gxwFKW8SCFzqwPJXQvcUV8K4g/640?wx_fmt=png&from=appmsg)

瑞幸咖啡 my-coffee 会根据你的位置，搜索附近的门店列表，让你选择，并展示出匹配的饮品类型，价格，规格等。这里有大杯、特大杯、超大杯，唯独没有中杯，罗老师看了估计又得沉默了。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/0VE9kDxicLUiaxopn1eFbuIxPUdQzzgyffArB0lqrZF83bunibgzhdBe2EGib9WazSCrJef0qfT5m26oP7bQwgpZURxtfQ3sM0pcYaDOup0gRFE/640?wx_fmt=png&from=appmsg)

当你明确门店和品类后， my-coffee 会帮你生成订单

> 那你帮我点一杯橙C冰茶吧，负一层的店就可以

![](https://mmbiz.qpic.cn/mmbiz_png/0VE9kDxicLUiaibOqjCicwkDICJWYvNyu9yFb4DBXm4xpK5DuylzdLnP0WUXkmN0Y258RBfeBBq1fBtyulhYs36moWEcI472G9gaYzLvJjvSM7M/640?wx_fmt=png&from=appmsg)

下单成功后，可以扫码支付。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/0VE9kDxicLUhWaBB5B4xv7tYibiavsGXNvDksmoHwyC5SrOibt3JBVFyUOOFv3dRxSibQe0v6A8eT2cHK5eicQx0sNHtJZTG7Ewmf9yib0LlAkAK4k/640?wx_fmt=png&from=appmsg)

支付完成后，即可获得取餐码、商品、门店地址、支付金额等信息。

![](https://mmbiz.qpic.cn/mmbiz_png/0VE9kDxicLUh2rstwicaWW69WPdNl6vTQggTgkIGF0wgcQa4XTdGszYdH2d0z6EMr6ibCA65KUBPlFnpzQXXBXcu5FGt9PTgp8K5SXeq9GRg5c/640?wx_fmt=png&from=appmsg)

你也可查询订单状态，及时去取你的咖啡了。

![](https://mmbiz.qpic.cn/mmbiz_png/0VE9kDxicLUgEtcmoKwmLrOgKic12P4QrW9SUBAGcdDNbuPHGwIP9sUhfn2yYZYSpadaw0LicujEvKn8LxKcqySClDjNnNZnYjLdQDcHlXgia9E/640?wx_fmt=png&from=appmsg)

🌳 写在最后

![](https://mmbiz.qpic.cn/mmbiz_png/0VE9kDxicLUhz6xjWVyMNJQpO9ZbFKc2x4JnxpbtyRtUPRCSoV2HycH2Zlp4iaN8fyEqHoTpwu1KF84ibdHKpwh5vxDaQBIlH9J1fHcL8OytmI/640?wx_fmt=png&from=appmsg)

早起的鸟儿有虫吃，勇敢的人先享受世界！

随着国民级品牌瑞幸咖啡、蜜雪冰城、滴滴出行、东方航空、肯德基、麦当劳等抢占窗口期，发布 Skill 和 MCP 这种 Agent 服务，趋势已经不可逆了！

当你的Agent能够点咖啡、打出租车、查航班、订酒店、发消息、发邮件、管理文档、规划旅游行程等等，AI Agent 就不再只是一个编程工具，而是悄然无声地从数字世界入侵到了你的日常生活，成为真正的 Javis，未来已来。

看到这里了，你还不快让Claude 点杯咖啡！

![](https://mmbiz.qpic.cn/mmbiz_png/0VE9kDxicLUhMicia7UTW3CmqH1GLf4JToSPDiaCRFqobbAUMucCBwY9icmou7Lwm3EtH26icg7Mv7icHcvh8VNupQIPDicCDa6OdeomlkTGBl9PZRw/640?wx_fmt=png&from=appmsg)

---

点个关注 **🌟，精彩不迷路 ❤️**

**往期推荐**

☞[小赚3万元！全靠这套开源AIoT 企业物联网平台](https://mp.weixin.qq.com/s?__biz=MjM5OTA4MzA0MA==&mid=2454946282&idx=1&sn=ad676c8d5c0785c5915e5c96ba318d82&scene=21#wechat_redirect)

☞[开箱即用！国产开源30+AI视觉算法IoT智能物联网云平台](https://mp.weixin.qq.com/s?__biz=MjM5OTA4MzA0MA==&mid=2454941969&idx=1&sn=bd91e2bdae181e82774c394c0e709f4b&scene=21#wechat_redirect)

☞[国产开源Web 工业IoT组态软件，支持Modbus、OPC，支持拖拉拽](https://mp.weixin.qq.com/s?__biz=MjM5OTA4MzA0MA==&mid=2454941531&idx=1&sn=dce5163565601e80d153821745715745&scene=21#wechat_redirect)

☞[源码交付，7天完成国产信创部署智慧工地方案](https://mp.weixin.qq.com/s?__biz=MjM5OTA4MzA0MA==&mid=2454940216&idx=1&sn=316b42125f746e16289fe04031496b10&scene=21#wechat_redirect)

☞[5万元斩杀线！ 一网统飞无人机AI巡检平台](https://mp.weixin.qq.com/s?__biz=MjM5OTA4MzA0MA==&mid=2454945550&idx=1&sn=403e8d5bad8c53ff1b7514a5e1146255&scene=21#wechat_redirect)

☞[上班摸鱼， 树莓派DIY智能 AI 视频算法监控老板行踪](https://mp.weixin.qq.com/s?__biz=MjM5OTA4MzA0MA==&mid=2454932745&idx=1&sn=532fc401409718148a07b35002c40b98&scene=21#wechat_redirect)

☞[免费开源，千知AI知识图谱平台，支持DeepSeek、Qwen](https://mp.weixin.qq.com/s?__biz=MjM5OTA4MzA0MA==&mid=2454944463&idx=1&sn=879157ebcc69d371ad87aa3816db7bc7&scene=21#wechat_redirect)

☞[信创部署，源码交付！县域低空经济无人机 AI 巡检平台](https://mp.weixin.qq.com/s?__biz=MjM5OTA4MzA0MA==&mid=2454944340&idx=1&sn=0bd578639500191483b4c76cc9083052&scene=21#wechat_redirect)

☞[智慧农业大爆发：AI+物联网+区块链重构“天空地”一体化监测](https://mp.weixin.qq.com/s?__biz=MjM5OTA4MzA0MA==&mid=2454944207&idx=1&sn=27aba015734707013b311674825c37cc&scene=21#wechat_redirect)

☞[一站式AIoT视频聚合平台，适配国标28181和国密35114协议](https://mp.weixin.qq.com/s?__biz=MjM5OTA4MzA0MA==&mid=2454946211&idx=1&sn=0072cf454ac83d98adb64c5767e58901&scene=21#wechat_redirect)

☞[“空中奇兵”无人机多光谱罂粟巡查平台，识别出苗期、花期、果期](https://mp.weixin.qq.com/s?__biz=MjM5OTA4MzA0MA==&mid=2454946024&idx=1&sn=6b7d30937351bcce27a0d930c5727726&scene=21#wechat_redirect)

**免责声明：**本公众号所发布的内容来源于互联网，我们会尊重并维护原作者的权益。由于信息来源众多，若文章内容出现版权问题，或文中使用的图片、资料、下载链接等，如涉及侵权，请及时告知，我们将尽快处理。

预览时标签不可点

修改于

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/tnMEWNbfO5dAnL0wnu7VicnmWCziaZr42icK2RbNCTV6KezOBgYPIZc7hiaZiaTaUnPZzwShBn7FXicr96iamdc0kKPYw/0?wx_fmt=png)

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