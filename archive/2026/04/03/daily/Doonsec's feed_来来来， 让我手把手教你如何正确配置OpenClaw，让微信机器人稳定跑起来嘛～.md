---
title: 来来来， 让我手把手教你如何正确配置OpenClaw，让微信机器人稳定跑起来嘛～
url: https://mp.weixin.qq.com/s/ErRok_ouppifGqrJ3fnUNg
source: Doonsec's feed
date: 2026-04-03
fetch_date: 2026-04-04T04:10:45.905784
---

# 来来来， 让我手把手教你如何正确配置OpenClaw，让微信机器人稳定跑起来嘛～

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/ia7TorzX5Pa1h8iblKuaYJuuYRPrBUGHgeOZPLhdWRTZcGCHQH3bniaHk7icEZkSwPccQiciaFC17gzjUDQvJC5Pm2ibm1YQESz054GEibxdsFqSOco/0?wx_fmt=jpeg)

# 来来来， 让我手把手教你如何正确配置OpenClaw，让微信机器人稳定跑起来嘛～

原创

钟智强
钟智强

哪吒网络安全

![]()

在小说阅读器中沉浸阅读

OpenClaw 是啥子？ **OpenClaw 就是一个开源的机器人框架，专门让你在微信上搞自动化回复、对接  AI、定时发消息这些操作，它本身不直接跑在微信里头，而是通过插件去 hook 微信的接口；之所以非要微信 8.0.70  这个版本，是因为这个版本的内部接口被 OpenClaw 的插件（比如 WeChat ClawBot）研究得最透 登录稳、 hook  点不闪退，升到更高版本接口一变就遭不住，降了又缺功能，所以 8.0.70 就是最稳当的那个黄金版本哟**

**废话不多说.......**

**第一步，先把微信升级到 8.0.70 版本，图看下头。**

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/ia7TorzX5Pa3FyiaDnU5cpThC4zDj0iaNr5wMHFVjtsodJW8f9PKXywMaCZX2smawRJK3aCqVy2p5GAPKm3Qb9e6cls4F0iadNoqkolcgZzWdes/640?wx_fmt=jpeg&from=appmsg)

**然后点「插件」，找「微信 ClawBot」，再点‘详情’，**

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/ia7TorzX5Pa04qia58lVWUfnla429whfP6hteWDuIx1Ed9wWibHicDFm2bBbSg2dL4yK4EVFkTPRzsP7OANypCjh0ITG8L2jBWg0YDibLKDw2XP4/640?wx_fmt=jpeg&from=appmsg)

**接下来你就看到下头这个界面了哈。**

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/ia7TorzX5Pa1aCLSnFkcBkib2JzUaMxUzsmD2mzJdwqgibcen5rV01iaiaObBYc0AzQJcncmmb6yXpwiastAsKWl8xBGCbE82YaqcPRySGRfC14SQ/640?wx_fmt=jpeg&from=appmsg)

**在跑以下**这条命令之前，先把 openclaw 先安装哈........****

```
npx -y @tencent-weixin/openclaw-weixin-cli@latest install
```

****等到二维码冒出来咯，你就拿起你的微信，点扫一扫，去扫它哈。****

**从 GitHub 上下：https://github.com/openclaw/openclaw ，然后跑**

```
npm install -g openclaw@latest
```

**但如果你是 Mac 电脑，莫得用 npm 哈，要用**

```
brew install openclaw-cli
```

****等到你把 OpenClaw 装巴适了之后，再接倒整 `@tencent-weixin/openclaw-weixin-cli@latest` 这条命令哈。****

**先登录 https://platform.deepseek.com ，然后点“充值”，把钱给了，再创建一个 API key，把那个 key 复制起。下头按步骤来哈。**

![](https://mmbiz.qpic.cn/mmbiz_png/ia7TorzX5Pa0Q5BvpVzV7ib6aKhNFIGnpmGj3IcS5xTl2BOuYhzymC4icKYiclI9PvmdjeicibXia1UeibGQKXSez63xc66B4iao3ia3vVpgagzHKW36c/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ia7TorzX5Pa1yK0fa5xTTSr9QlmNJReuPHOgNnQ5dXtTwQI5nmYPpoqyfWPzyDXJ772qB05Jyaiaqolf0VRicyOxaKSO5OY5BHiajPPJGLTh2TE/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ia7TorzX5Pa1EUh54rianZqXicIBJzMgcoT1orKAq6dJsrOcADmdo4CZaxj0YK4SZAMwaCogdoCCXNwrRTSHPxA4icMib1ZqsEMe5KBpBtDoPfS0/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ia7TorzX5Pa3ZpyVMt5EibNF3foSzDOBZSwL4GYO2iaqxgpI6VUEpZd4Q6cicZndRcqEvQCCibDNymAu3iaLkfAydacpffTmIh1JMz9eUyB1OMI9g/640?wx_fmt=png&from=appmsg)

**过后，就跑**

```
openclaw config
```

**然后你就看到下头这个屏幕样子了哈。**

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ia7TorzX5Pa1ibmbT7F28rLOIZwo0kMkBIKcAACfnHxY3asic65zn0taD4qAIMsJibb8fQgkMHY2mSnwKc44fjJHl1qCicvQFs2R8eV3mzuDXMZo/640?wx_fmt=png&from=appmsg)

****然后你接着选Local（本地），选完过后就看到下头这个菜单列表：****

![](https://mmbiz.qpic.cn/mmbiz_png/ia7TorzX5Pa1MmapRjK8pkDWn8RlLiclK7EcwM2qrTwjFeDne9NMzqUQF47Lw1rqWnagJ35DjH8Sxxp3f43Ng8xNRMUrba2UMEo7wtOic3icsUs/640?wx_fmt=png&from=appmsg)

> **这会儿我们先不忙弄其他的，头一步先把 Model（模型）给它设好。**

现在在这个菜单里头，用上下键选到 **○ Model**（注意前面是圆圈不是黑点），然后回车进去，配置你要用的 AI 模型（比如 OpenAI、本地模型这些）。

等 model 配好了，再回头来配 Workspace、Channels 这些。**然后下一步，这个教程里头我们用 DeepSeek 的推理模型（reasoner）。**

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ia7TorzX5Pa1lKNRFlAHQzUhJSCj1BQI552zzkX99dXRoHP1Zgas31pZyZW0ibKc8JnyT2ug5rPRvv1uuX6MJcXyFF8uATtbHeKBicEnBvILIg/640?wx_fmt=png&from=appmsg)

****然后在这个 Model 或者 auth provider（认证服务商）那个选项头，选到 DeepSeek，再按一下回车就完事。****

******然后把你那个 API key 粘贴到终端头去哈。******

![](https://mmbiz.qpic.cn/mmbiz_png/ia7TorzX5Pa1Yjp38hnjiaWOUGIKW6UJnc31iambzttaicKZIfJYKZu7xMial62NwS3FM3LzgdexnwTEia9WsrgYib6drsDcBcFVmiaFeLLPCQ7N8Z0/640?wx_fmt=png&from=appmsg)

******快拢咯，接下来我们把 Channel给它配起。******

![](https://mmbiz.qpic.cn/mmbiz_png/ia7TorzX5Pa271eLUeGexxZCGd0FnXBXPxrdIRZqrE9UCQUSzyWPUgIT4YmqpUvBcGTrTNOw0pyYicx3r2IiadHPsvictBTS5FDZiazG2jTR2AcM/640?wx_fmt=png&from=appmsg)

**然后你给它选到Configure/Link，也就是“配置/连接”那一个**

![](https://mmbiz.qpic.cn/mmbiz_png/ia7TorzX5Pa2rQ8Ouyk62vMscDJ6aHmiaZibj1lrpdeCN49Lw6iaxIUNhpEjEFRae5alTsnqrBO3zrLOoVILjXbNbRDN5bCn7KqjRqKj9rSCeX8/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/ia7TorzX5Pa3ibLpL0wDiaJwkH8SRhia3RPrib4Nic1YuXXcA2DjaPCLyK47Ic9TMUqdfN1W1MwcLyibHGiclWQcbJLNibY8WI5NFdyHOjl6bu9yTKOM/640?wx_fmt=png&from=appmsg)

**这哈就退出去。最后再敲**

```
openclaw gateway run
```

**或者**

```
openclaw gateway start
```

**车子就发燃咯。**

---

****这哈你就用微信发条消息，整个****

```
/ping
```

****看它回你不, **要是你收到的回复跟下头截图一样，那就要喊一声："恭喜你，搞归一咯！"******

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/ia7TorzX5Pa2AvmfF8yFI65aKh7v1ka0lOFgVysuyiawJvVkStNL5YoyVSHruLussm4ZibzBcsSjc41w1DH2ibv5oL66f9sQF3Q2ibibmrpGNQLCQ/640?wx_fmt=jpeg&from=appmsg)

---

******如果觉得我这个教程对你有帮助的话，给w哦点个关注可不？再进我的群头吹壳子嘛～******

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/ia7TorzX5Pa1bG7BhBC2klWIZt256icIja7cvRlqwxesRcthm6rLEpibUOR45XQ5JKG7V0VEB5DdQmyAKjDc2baPqbfgrowA9uSGkW0aAOUhog/640?wx_fmt=jpeg&from=appmsg)

---

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/9Xx8EkicjWicEcd3af9D02mtgshZPKdXndvibwGAzfG6JYkbK8kTEkptqlGSicib2OmskYW3OQohNwTqz3RdpV0sIIQ/640?wx_fmt=jpeg&from=appmsg)

#openclaw #clawbot #weixin #npm #deepseek #wechatclawbot #小龙虾 #哪吒网络安全

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/sz_mmbiz_png/9Xx8EkicjWicHbRAicRaapa3GviabJibYVw9zs9WR9VqEMvuLm45IegNOPBFbXjj3d6V6wI4DMVlgObM9nFOOeU6j2w/0?wx_fmt=png)

哪吒网络安全

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/9Xx8EkicjWicHbRAicRaapa3GviabJibYVw9zs9WR9VqEMvuLm45IegNOPBFbXjj3d6V6wI4DMVlgObM9nFOOeU6j2w/0?wx_fmt=png)

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