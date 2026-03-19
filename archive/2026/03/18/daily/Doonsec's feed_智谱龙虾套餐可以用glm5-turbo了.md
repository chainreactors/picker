---
title: 智谱龙虾套餐可以用glm5-turbo了
url: https://mp.weixin.qq.com/s/_wEKlkHztP7iCv5tQix6UA
source: Doonsec's feed
date: 2026-03-18
fetch_date: 2026-03-19T04:15:46.922520
---

# 智谱龙虾套餐可以用glm5-turbo了

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/quuJmJ6Atj0Q6aL2QIXPECR5iawuE2uo1r8UuZ3uE8TUz1HmM1H9foaL6yLwnV4DuQELcpE3KkalAh0bZHEXHKGFwLYvsoZutPZDY9eacw18/0?wx_fmt=jpeg)

# 智谱龙虾套餐可以用glm5-turbo了

网安杂谈
网安杂谈

网安杂谈

![]()

在小说阅读器中沉浸阅读

前天还在研究哪种codingplan适合养龙虾，经过这两天的实测，minimax的codingplan感觉不是很聪明，响应也有点慢，但是比较稳定。实话说智谱的codingplan养龙虾真的有点垃圾，动不动就限流。

查了查glm的官方文档，是这么说的：

GLM Coding Plan 支持 OpenClaw 使用，但采用次级调度与尽力交付策略，Coding Agent 任务享有资源抢占优先权，高负载下 OpenClaw 任务将自动触发包括动态排队、限流等公平使用策略。如您需要更极致的龙虾体验，请购买和使用 龙虾套餐

看来这火爆程度，整的算力资源也吃力了。所以推出了这个龙虾套餐，可以用最新的glm5-turbo模型。

![](https://mmbiz.qpic.cn/mmbiz_png/quuJmJ6Atj3udHuPvqbfyQckNNTw1iaa58icoo7WyZugnlZW8LPReeH3fNmS3bicgnGu4EuCzNO5CTHojxNMLbaCXuyjibQ4op6bV8no45nuwXo/640?wx_fmt=png&from=appmsg)

那我们再尝尝龙虾套餐怎么样，可以试试新推出的glm5-turbo养虾。

https://www.bigmodel.cn/claw-plan-team

![](https://mmbiz.qpic.cn/mmbiz_png/quuJmJ6Atj2iaia4ZUY4icL06mhSapic6sTJHbia5hLJ3j7w5ybblsWfbP4l1ccX3pickWtcGPlnmBGrrWJUDYfTiaqoa2gIUY89GvmDpiaiabZE3Xgg/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/quuJmJ6Atj0EkzsujN4kCcx7cPTXsPs8kAahdtW9b9huYBFN86iahb9FvnBgJDOrAWQpGuGBWdvaqNcYbyAicNKQvcRaRT0IrUtqVpeefPyeE/640?wx_fmt=png&from=appmsg)

穷人伤不起，先来一个月的试试看吧。。。配置文档在这里

https://docs.bigmodel.cn/cn/coding-plan/tool/openclaw

买好了先在后台添加新的apikey

![](https://mmbiz.qpic.cn/sz_mmbiz_png/quuJmJ6Atj0KU0nZpOkmKvPypFndGMt94OPDjDZZv6WDZDtgVXxozkD18k9oXOPvrmz61D1HgULRLux9Nqia0yibIoH3DGyxQibntREHcTqZ4w/640?wx_fmt=png&from=appmsg)

然后配置openclaw的模型

openclaw config

选模型配置

![](https://mmbiz.qpic.cn/sz_mmbiz_png/quuJmJ6Atj1obCEpeJicjGDMH9gYgpaFU4BO9LZNDOo879T9ib8s3weicR7CtWicrtVUw7ibK9NPE1hU8IqOKXHZCQ5CibZE9ibaVILELvdwQQeiaNY/640?wx_fmt=png&from=appmsg)

找到Z.AI

![](https://mmbiz.qpic.cn/sz_mmbiz_png/quuJmJ6Atj1sLuFoyyVEKZicE1Lec6EK3icFyH6zV5MEaiaWGwBxmzrWviaXxaH3vpFZicgW7ficxGCv5YD60vzMeKEqhUEdH11Sic42iaCWws84HeU/640?wx_fmt=png&from=appmsg)

注意要选Coding-Plan-CN (GLM Coding Plan CN (open.bigmodel.cn))

![](https://mmbiz.qpic.cn/sz_mmbiz_png/quuJmJ6Atj1uicdeicT1BHrOBIyia4VicRzZ2wgzxpBoVn29n1hVmQtuLkZ5I6PkrmdtsF5zRdqchAsInqbPRCStV7Oz2gl1ne07f2glRiaicY5iaw/640?wx_fmt=png&from=appmsg)

然后填入API key，然后选择相应的模型

![](https://mmbiz.qpic.cn/mmbiz_png/quuJmJ6Atj2b5sWwVjWp8rTsjIgTUTXJdblF6UmYZx2Yricg2ofuPksKHQgbN0S4wRHml8fIBsPzsnjrtSnvoRDialF1OOf2D7IEHa3oFDR78/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/quuJmJ6Atj1a27fF6kuUyhQ0J6iaHVkokqbPdWVQSkI1O1T3PUOribUXJDqwdy95exl3WTpz9MacgTdv0JY66bLzu4rSk6umEBHRZKwodA708/640?wx_fmt=png&from=appmsg)

但是官方龙虾还没法直接选glm5-turbo模型，还得特殊处理一下了。

在已经配置了上一步 Provider 接入后，可以参考下方配置切换到 GLM-5-Turbo 新模型，在~/.openclaw/openclaw.json文件中的 models.providers.zai.models 数组中添加glm-5-turbo模型，在最后一个模型后面添加：注意 JSON 格式数组里面加逗号

```
{  "id": "glm-5-turbo",  "name": "GLM-5-Turbo",  "reasoning": true,  "input": [    "text"  ],  "cost": {    "input": 0,    "output": 0,    "cacheRead": 0,    "cacheWrite": 0  },  "contextWindow": 204800,  "maxTokens": 131072}
```

修改默认模型，找到 `agents.defaults.model.primary`

```
"primary": "zai/glm-5",
```

修改为

```
"primary": "zai/glm-5-turbo",
```

```
找到agents.defaults.models（大约在第71-76行），添加：
```

```
"zai/glm-5-turbo": {}
```

这样就配置好glm-5-turbo啦。

![](https://mmbiz.qpic.cn/mmbiz_png/quuJmJ6Atj0PiaEictj3dJkst6UiadlCI5NfyS03ECtaCQzOpLDkxTuxkkQxVZ0X1q3VdbNCvQzFa3GouTkO7Ficqrfw6SzY7eNUsiack8eSc2Xs/640?wx_fmt=png&from=appmsg)

```
结论，响应速度挺快的，模型也是做了优化，感觉还挺聪明的，但是有用量限制，总的来说可用。
```

```

```

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/Z4jKmMQicbWP0nM8PnhZtqI4yFWpIJ8KdgxKg1XsbSjljI4kic5C0oAfDRiaXCJmmsl66ro1fY3eDJVUAcoib2PRDg/0?wx_fmt=png)

网安杂谈

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/Z4jKmMQicbWP0nM8PnhZtqI4yFWpIJ8KdgxKg1XsbSjljI4kic5C0oAfDRiaXCJmmsl66ro1fY3eDJVUAcoib2PRDg/0?wx_fmt=png)

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