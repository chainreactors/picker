---
title: 仅5周！OpenClaw，崩了！
url: https://mp.weixin.qq.com/s/4G3DiugL8OuR7S95eXfn5w
source: Doonsec's feed
date: 2026-04-24
fetch_date: 2026-04-25T04:30:17.222790
---

# 仅5周！OpenClaw，崩了！

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/TVljsu2eAicLFphudm7xuM1oicJD1XoaTkMHiaiaicu8vRU83cjPhRayQqgwjqHZwwib3aJcvO4M2NTCZvyM6Y24nFiah548Re3VO2f2uXQpK1qJwg/0?wx_fmt=jpeg)

# 仅5周！OpenClaw，崩了！

原创

hacking
hacking

Hacking黑白红

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

这几天真的很少人在讨论“龙虾”了！

3月16日GTC大会，黄仁勋亲自站台，将OpenClaw封为“个人AI操作系统”，全场起立鼓掌。

![](https://mmbiz.qpic.cn/mmbiz_jpg/TVljsu2eAicI4oDa8d52tuNkooAvDMevaaPUtBSosDnCKictEibK96Kn6ArzHdGAibNSQZbXNIWvqFh2fgpfNg3FzehqjQQQy51z1htWIR9SF4M/640?wx_fmt=jpeg)

彼时它是GitHub增长最快的开源项目，星标直冲36万。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/TVljsu2eAicIKcYyzVUquE40kHsaYvX4Zkt76ClyM5z8pqd1XiaenAOCCxomiak3dp4HAONDg8flVSyk1W8J5DXhGafT8iau5a4oDnAQic9NZKEA/640?wx_fmt=jpeg)

项目地址：https://github.com/openclaw/openclaw

仅5周！黄仁勋亲自封神的OpenClaw崩了：更新即崩溃、大厂不敢更、下载腰斩

谁也没想到，短短5周，神话崩塌。网友：早就不折腾了，就是个阶段产物。

01、更新即崩溃，大厂不敢装最新版

OpenClaw的致命问题，从一开始就埋在高速迭代里。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/TVljsu2eAicINMuKZttcDRwavuPibqqOvsiaa9OZ4rBNvSsqWR5jDcMwuYfpibqJOmdv9uz1U4TRyjnTVicsp9SJgNNlHULt7oWdjmlHWWNpmNsQ/640?wx_fmt=jpeg)

过去一个月连发十几个版本，一两天一更，用户配置好的Agent频繁报废，Reddit与GitHub吐槽刷屏：

“更新完直接废了”“天天在Debug，不干活”。

更讽刺的是：英伟达与国内大厂，都不敢升级到最新版。

怕崩、怕故障、怕业务停摆，只能死守3月旧版本。维护团队被迫开启“停更周”，只修稳定性，不加新功能，只求用户别再怕更新。

02、Anthropic釜底抽薪，“龙虾税”直接卡死命脉

4月4日，Anthropic突然宣布：禁止Claude订阅用户通过OpenClaw使用额度，必须走API按量计费。

![](https://mmbiz.qpic.cn/mmbiz_jpg/TVljsu2eAicIY54a9aSZbXsmfTQrcBwTmqNjjic0aASjuSWB7ekD5Q5BOc1E9wiaWiaVxpa4GVUicWooNz8nk0fTjzFn0p1LGFnFiclF1gDoJ8nb0/640?wx_fmt=jpeg)

对OpenClaw来说，这是致命一击。

原本每月200美元随便用，改成API后，一天就能烧掉200美元。创始人直接开怼：先抄功能，再封开源，时间线太巧。

更戏剧性的是，不久后创始人Claude账号莫名被封，两小时恢复，但无任何解释。开源项目，命门被大厂捏在手里。

![](https://mmbiz.qpic.cn/mmbiz_jpg/TVljsu2eAicKtpqSTicrBrL6RL8EQha9YXNy72zlibkaOxDBxXwXYG5XkyhEM2pt6LXg7LraJdcYVhHDZMF1fm3ryWg5eEs83JxS46srM71rbY/640?wx_fmt=jpeg)

03、竞品围剿：一行代码迁移，用户疯狂出逃

内忧未平，外患已至。

竞品Hermes狂飙突进，周增速达OpenClaw三倍，贡献者数量完成反超，甚至直接上线一键迁移命令，一行代码从OpenClaw搬走。

![](https://mmbiz.qpic.cn/mmbiz_jpg/TVljsu2eAicJaxZ1mY4HUrWETWMRNoaHDcxe9NgDlBttiby2LB0VwVgCQSE379bvSVGsMl5UhuBkaTg8BOQZlKC5lAxdtW0xfDzmW9raSgu50/640?wx_fmt=jpeg)

用户用脚投票：“终于不用折腾，能安心干活了。”

数据更扎心：NPM下载量自峰值直接腰斩，打回3月初水平。曾经的顶流，正在快速失血。

04、开源困局：志愿者扛不动，路线彻底分裂

OpenClaw的危机，根源在模式。

核心维护者全是兼职，各有本职工作，靠爱发电撑不起企业级稳定性。网友评论：

![](https://mmbiz.qpic.cn/mmbiz_jpg/TVljsu2eAicLYrbXiaQic6riciabI8j22kLA1eLLLDDib0OOoEenqEgRaicrvaPzo9zWJLczw9bPKLiaxhTDDSV7iaERsfnMymK8QiaoHqEoA69Ricwv1s/640?wx_fmt=jpeg)

团队内部路线撕裂：

- 一派要稳：固定周期、严格测试、服务企业

- 一派要快：保持极客节奏，快速试错

历史似曾相识，Linux也曾经历同样阵痛，最终靠LTS长期支持版破局。而业内更直接的建议是：做专业版收费，用商业反哺开源。

最后

从改名爆火、超越React、黄仁勋封神，到四面楚歌，OpenClaw只用了三个月。

它证明了一件事：AI Agent可以一夜爆红，但要走得远，光靠热情与速度远远不够。

稳定性、商业化、生态话语权、不被卡脖子，才是活下去的真正答案。

这场神话破灭，给所有开源AI项目，敲响了最响的警钟。

作者：hacking。前北漂程序员，现在做安全。

文章数据来自网络，大模型优化，侵权删。

**往期****相关****回顾**

[度假变噩梦！徐泽伟因美国网络入侵指控在意大利被扣，妻子：老人孩子还能等多久？](https://mp.weixin.qq.com/s?__biz=Mzg2NDYwMDA1NA==&mid=2247550585&idx=1&sn=d393ee66a57f3a9b6d2895a3e3b9ed9d&scene=21#wechat_redirect)

[被指控网络入侵：中国徐泽伟在意大利被扣押的210天、或被引渡美国](https://mp.weixin.qq.com/s?__biz=Mzg2NDYwMDA1NA==&mid=2247550577&idx=1&sn=34365a236610b5680df0781a39f0e3d7&scene=21#wechat_redirect)

[徐泽伟引渡美国！意大利上诉被驳回，被美国指控黑客入侵](https://mp.weixin.qq.com/s?__biz=Mzg2NDYwMDA1NA==&mid=2247554243&idx=1&sn=5b97552ba5b90774714b65b7e239ebce&scene=21#wechat_redirect)

[朝鲜黑客封神！潜伏6个月盗走2.85亿，DeFi史上最精密猎杀案曝光](https://mp.weixin.qq.com/s?__biz=Mzg2NDYwMDA1NA==&mid=2247553894&idx=1&sn=102a2765f53d5763674c655e99a438c0&scene=21#wechat_redirect)

预览时标签不可点

修改于

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/sz_mmbiz_png/rf8EhNshONTk9JHJcRia5QdqxUfpBz4cb5VGKUIUyrVaviawse20DccoB4C6WKwxm6xVzq4oU7dSdfxryTMc9Vvg/0?wx_fmt=png)

Hacking黑白红

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/rf8EhNshONTk9JHJcRia5QdqxUfpBz4cb5VGKUIUyrVaviawse20DccoB4C6WKwxm6xVzq4oU7dSdfxryTMc9Vvg/0?wx_fmt=png)

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