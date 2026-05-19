---
title: UI可爱又能打：给Hermes Agent套个Web壳部署实录
url: https://mp.weixin.qq.com/s/80PHnm4TJ8AsivVxYG1erw
source: Doonsec's feed
date: 2026-05-18
fetch_date: 2026-05-19T06:02:00.404886
---

# UI可爱又能打：给Hermes Agent套个Web壳部署实录

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/Hjtlibzdr5XicrHCRPtxzADlnetBGktFRTkRQqMGwgQWE51GT8IzczFrToTKFrk1wq9OQzgFsicCBNKvFRjTOyj9h39JTCIfz5AoibeyYYWVzhM/0?wx_fmt=jpeg)

# UI可爱又能打：给Hermes Agent套个Web壳部署实录

原创

小志z
小志z

志在片语

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

之前朋友送了几台云小龙虾 跑了几亿token做测试和简单的挖洞感觉有点方便 但是云OpenClaw我自用还上感觉不稳定 还有各种各样的问题 就准备试试最近比较火的Hermes

> 某厂商的Coding plan有十个 跑了glm5.1 大概5e就没了（

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Hjtlibzdr5X8aAbhR4AaItN75IKqfJ3qQtMIdwUUvDgVy9OT00HU6q6MSQhHNEWXuuN900TQPU8o0yYgYl0KjjicX7j4UcrMH55CLnKmicBJBo/640?wx_fmt=png&from=appmsg)

### 配置系统初始化

更新系统软件包

```
yum update -y
```

因为看见了有内核更新 所以需要重启系统

![](https://mmbiz.qpic.cn/mmbiz_png/Hjtlibzdr5XicibLHFpln37rSwxQUdjrKGfYTfGu7UV7cXU0JXqGDKHwGQ6Izy0OfE2bVqUz00wjckLS9ynTogCqu2lDKs2Hiapic0Pk8ic32gbvQ/640?wx_fmt=png&from=appmsg)

```
reboot
```

### 安装Hermes Agent

直接用官方给的快速安装命令即（确保网络能访问Github

```
curl -fsSL https://raw.githubusercontent.com/NousResearch/hermes-agent/main/scripts/install.sh | bash
```

记得安装前用yum install -y tar git 安装一下包（不然就报错

![](https://mmbiz.qpic.cn/mmbiz_png/Hjtlibzdr5X9ia3NicRzice12rhibgHic3bDp3eztVu4vuw2tibTeuAjeVsJ4OypSicGAYNe26IRwv0LnNdFH0mKOqCCQqKTCGP2tzyBsEKNFhpnFOg/640?wx_fmt=png&from=appmsg)

然后就到了Set up页面 选择第一个 快速设置

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Hjtlibzdr5X8NexKvcE6ZzPibG70TATIn6LMdSBKY84BVdtyPgNHaLbXooJMXL6atvHy47Bhw7D023yq7iaXbUF1SaP9lF6gesAWKoZfXAvTOA/640?wx_fmt=png&from=appmsg)

第二个页面 根据你的需求以及选择的模型 配置自己的apikey

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Hjtlibzdr5XibU4gTOdx7j3ONsybnw0s2Ht3vKLQibymS04lGRlTYibUINic1ia00Jjx2FzR5KDibZ6CyB8AicCLqIq3SZ65G32AsPpG8bn9UFKQ13k/640?wx_fmt=png&from=appmsg)

我这里选择的是我自己的中转 输入api地址以及apikey 就会显示出api可以选择的模型 根据自己需求选择即可

![](https://mmbiz.qpic.cn/mmbiz_png/Hjtlibzdr5X8ZzgDUr8OyfibiaziamibymUQLNaFUhn5HKibr4px3h2o5kVng61QWWr6Kvv3iamhEol0spLCnA9JncKNfVL6hLMArebdqv2wcMOia9g/640?wx_fmt=png&from=appmsg)

这里是选择命令行的后端 我就默认回车即可

![](https://mmbiz.qpic.cn/mmbiz_png/Hjtlibzdr5X8KZ41ZKia7TwztO9lyqrtHvPQPjXbWU1RfyhEUMqbiaKU09Wk8tO52UxIgeChge7jNxPYe7KoSv2klfSYvX161kicAdqRC35bhKw/640?wx_fmt=png&from=appmsg)

然后是配置选择推送平台 就是把结果推送 看需求配置 我这里跳过了

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Hjtlibzdr5X8ibbJegPeRqdUhdaIHCtNsAXYM9BIC588ejZVb9Syk9jIlFLxblctbNPnflKibnKPzS6XedScXTeNic6IfXsXA0CgibavTkSUE43g/640?wx_fmt=png&from=appmsg)

然后最后会问你要不要启动 输入y启动即可

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Hjtlibzdr5X9PuWI7GZIjmBDHHR2ONMFhcF3lN4MFHbjgtj5wyoVHdicjSdU63e06mR4G4h0ibCsOzYMwia4a4pLkE8BWLXK2kucjwAYicABUVCo/640?wx_fmt=png&from=appmsg)

然后等待 Agent初始化即可

![](https://mmbiz.qpic.cn/mmbiz_png/Hjtlibzdr5X9Gze0cuQ1LIXIwe5sGD9NxGxiaL8WAAQSZYvoYlYo4dnziaicv5U8vibpNvtoZy4qK87L3YM4j8aIviavpelrSsSbNFXib9XiaVcWE74/640?wx_fmt=png&from=appmsg)

最后记得刷新一下终端 就可以用hermes命令啦

```
source ~/.bashrc
```

然后就可以正常使用啦（如果实在不行就用绝对路径访问

```
hermes
```

### 部署Hermes-Web-UI

> 因为机器是在大内网里面的服务器PVE虚拟化出来的，用ssh使用确实不方便（就想着打个洞整个Web页面

安装必要的编译工具组以及依赖

```
yum install make gcc gcc-c++ python3 lsof -y
```

安装Hermes-Web-UI

```
npm install -g hermes-web-ui
```

启动Hermes Gateway并后台运行

```
nohup /usr/local/bin/hermes gateway &
```

启动Hermes-Web-UI服务

```
npx hermes-web-ui start
```

这样就没问题啦 访问URL即可（localhost改成你对应的ip地址访问就好啦

![](https://mmbiz.qpic.cn/mmbiz_png/Hjtlibzdr5X963C6WWBXEKficqcXwJHUPQMiaosMvkZal9J7wyAP7iaGH9LN2CYLCiaMJSKEBEtzslJ83pblhS9ibalO7q3pNtibF6he8zB1CCeice4/640?wx_fmt=png&from=appmsg)

打开对应的URL就能使用网页版啦

![](https://mmbiz.qpic.cn/mmbiz_png/Hjtlibzdr5XicFJBzxBHos2tTiaunoCfxYgTIeBqa2IQSpGB7wtAE6TeOSickudo9kj7mZpJiaUrb9peQFftY1ricPM82uBZibcnxghvFCvmwZRRYU/640?wx_fmt=png&from=appmsg)

尝试对话一下下 UI可爱捏

![](https://mmbiz.qpic.cn/mmbiz_png/Hjtlibzdr5XicWnmln6lEQtBkibpsjluZBtlRGYlwoMibRsvJ1SjTSByq8Mw7PVBYc53m2lGLXaTGSZvMVyRB12YfQAnDw9Pbdr6LL8Ejgrnyvo/640?wx_fmt=png&from=appmsg)![](https://mmbiz.qpic.cn/sz_mmbiz_png/Hjtlibzdr5X9GLjwUqSIxECE8MlC8LCO8icnuHCia09zfFMQdQrnZBXNZyHcET2ayfxOL3iatMC75HjSnmNz2GTIt3cnVZyHnwzjCc3HOslC5O4/640?wx_fmt=png&from=appmsg)

好用好用 拿这个做代码审计和接口测试用起来快哉快哉（下面是挖了一个小洞的消耗 就是缓存命中率低一点

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Hjtlibzdr5X8m27icwhxqxtXQSDG16fLJktNKicias3HDB1LKejGF58uxeSsWxO0W3ibQmnPIBkyglsoFXvM8ib6AlgAmlY46MjgDLoZKvEeTWsXU/640?wx_fmt=png&from=appmsg)

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/9sGuXCD0aGx7dZqFspfFfHmfPEOUds23ibFibYPtvSsjS80euzsm0cuYoAeRkdqWPu4ukZEmfaRk4ibPKtpK2LvYg/0?wx_fmt=png)

志在片语

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/9sGuXCD0aGx7dZqFspfFfHmfPEOUds23ibFibYPtvSsjS80euzsm0cuYoAeRkdqWPu4ukZEmfaRk4ibPKtpK2LvYg/0?wx_fmt=png)

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