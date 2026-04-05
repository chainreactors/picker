---
title: Ollama连夜跳版本，只为迎接Google扮猪吃老虎的Gemma 4？
url: https://mp.weixin.qq.com/s/RxmVHY3j_8RyU2nidhWZrQ
source: Doonsec's feed
date: 2026-04-04
fetch_date: 2026-04-05T04:36:49.176392
---

# Ollama连夜跳版本，只为迎接Google扮猪吃老虎的Gemma 4？

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/9j14GSZeRZaTf3RBlhnJ4MmGBNicOMLp5T9AVWvQeQfm7dbfyKia2DZnibdcVnryvzGia6FoHqSZuCflibyLPNzrPZ1OR1dKTN9wH1sYxsiagSzSQ/0?wx_fmt=jpeg)

# Ollama连夜跳版本，只为迎接Google扮猪吃老虎的Gemma 4？

原创

衡水铁头哥
衡水铁头哥

铁军哥

![]()

在小说阅读器中沉浸阅读

俗话说：士别三日，当刮目相看。在AI圈，这话得改成“士别三小时”。让我看看，到底是谁这么大阵仗？

![](https://mmbiz.qpic.cn/sz_mmbiz_png/9j14GSZeRZaH8E57ok3nEBhjPZgI3mLedtjjVYRHx1KBGBpKIsGqtz8gBgtu5TYE42xNGqSzicShrj6BCn4eYJpFqFkvLAltMOicSVIu2KMAs/640?wx_fmt=png)

刚打算喝口水，一看GitHub，Ollama竟然为了跑通Google最新的Gemma 4模型，直接将版本升级到了v0.20.0。要知道，我们上次测试的时候（[8G显存跑AI：Llama3.1完胜Qwen3.5？Ubuntu下四大模型横评，速度竟差一倍！](https://mp.weixin.qq.com/s?__biz=MzI4NjAzMTk3MA==&mid=2458865722&idx=1&sn=f3bae6db4d28132a3daaefdde00350ce&scene=21#wechat_redirect)），ollama的版本还是v0.18.4，而这，仅仅是上周的事情！

![](https://mmbiz.qpic.cn/sz_mmbiz_png/9j14GSZeRZbYZUAiaboMft7LgGCQO1SRQ2vptRo1WEw7icwXMxrz9iaUSXHuLLoygtGR4Sf3siaEWYwTDySym0XN4licCmZxb5sdRo8jvKNHrXIo/640?wx_fmt=png)

换句话说，上个版本v0.19.0，也仅仅保持了4天不到。

![](https://mmbiz.qpic.cn/mmbiz_png/9j14GSZeRZYCFAppSwF6ohicd4Etyps3vQVIGZ8sQ3yqZp24G8s0ibZO6zcckIc090jFDBNZzy7eOkFR3NKLx42QyVljVzgibaPLaib4zAXib0HM/640?wx_fmt=png)

自古好马配好鞍，咱手里的RTX4070又是时候拉出来溜溜了。接下来，让我们见识一下最新版ollama叠加Gemma 4的变态性能！还是老问题：

你是一个资深网络工程师。我现在的网络拓扑如下：R1和R2运行OSPF，都在Area 0。R2和R3运行BGP（eBGP）。R2将OSPF路由重分发进了BGP。

现在出现了一个故障：R3能够学习到R1的Loopback接口路由，但是R3无法ping通R1的Loopback接口。请列出排查此故障的3个最可能原因，并给出具体的排查命令（假设设备为华为VRP操作系统）。要求逻辑严密，不要有废话。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/9j14GSZeRZadLaGYO2XwMDM3iaTzXOfvkfrUHibXHu0NVEaDE7GwnlryhG5Xa6V344yblFfgvIRhNRFjPiaRZ09D7qDUs58GT0XjfUYTS7lYVk/640?wx_fmt=png)

看，输出速率109.58 TPS，相比上次测试的冠军选手llama3.1:8B的50.4 TPS，大幅提升117 %。简直是天下武功、唯快不破。

注意看，这次gemma4的模型参数跟以往有所不同，这里面别有洞天。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/9j14GSZeRZbQydW3EObiaSXaspK8tCKcQvoGkDPvsic9pRVqobuXfMHB9mhTNnRdxJLbddzKBdO1gWsdLV6CibHc3EwiaXX2hpEvcDZTg9ibsbeM/640?wx_fmt=png)

对于以往的常规模性参数（[目前来看，ollama量化过的DeepSeek模型应该就是最具性价比的选择](https://mp.weixin.qq.com/s?__biz=MzI4NjAzMTk3MA==&mid=2458859385&idx=1&sn=19114c1432f3195512121e3ae6822c97&scene=21#wechat_redirect)），文件大小是可以预估的。比如bf16精度，模型文件大小近似为模型参数量的2倍，例如gemma4:31b-it-bf16的模型大小为63 GB；如果是INT8量化，模型文件大小比模型参数量稍大一些，例如gemma4:31b-it-q8\_0的模型大小为34 GB；如果是INT4量化，模型文件大小比模型参数量的一半稍大一些，例如gemma4:31b-it-q4\_K\_M的模型大小为20 GB。我们之前测试的llama3.1:8B的INT4量化版本模型文件大小为4.9 GB，qwen3.5:9B的INT4量化版本模型文件大小为6.6 GB。

如果按照这个规律，这个gemma4:e2b-it-q4\_K\_M模型文件的大小应该不超过2 GB，但实际呢？

![](https://mmbiz.qpic.cn/sz_mmbiz_png/9j14GSZeRZZQGHGmyXK8mzU3nxtnKo3sJSq5JzpZwBUhK7J9TJzIHkwIZhmRv1ZxG60KfB5ibfkibh1nGgVKsK7cW2iaolrbAQEwwd5xXIZ6FA/640?wx_fmt=png)

7.2 GB，这还是Gemma 4所有模型里面最小的模型了，也是我RTX4070能运行的最大模型。

![](https://mmbiz.qpic.cn/mmbiz_png/9j14GSZeRZZyPKpvBYW6joaLGiauGIaSIHWRmW6f0IV8WfqgoKC8KM5xDOnR4dTNcgokkQfg4FPbiaZcWOibI8CYQicpic0EupG6PelPfex86Oh8/640?wx_fmt=png)

如果按照常规模型文件大小反推，7.2 GB比9B模型的6.6 GB还要大，那实际模型参数可能已经达到10B。模型名称中的e实际上就是“Effective”系列，虽然逻辑表现对标2B，但其物理参数可能高达10B。而Effective的效果就是，Google为了让它拥有超越量级的智商，往里面塞了海量的知识密度。它的脑容量很大，但思考路径很短。浓缩的都是精华，膨胀的都是显存。

据说，Gemma 4 E2B-IT的整体能力已经逼近Gemma 3 27B，甚至在AIME 2026（数学/逻辑）、LiveCodeBench v6（编程）、τ2-bench（Agent任务流）等方面大幅领先。

对了，它还支持图像识别呢，我们换成截图再试试。

![](https://mmbiz.qpic.cn/mmbiz_png/9j14GSZeRZZOicRLZSHW2xmGYgdibTiaUWDYibeicpoSuEZoJPt7o9ZhW7HdLeQPVibh076icIP8NKdlsjtmRzaict6lusk6hpkiaS5ah2axbRnZj21s/640?wx_fmt=png)

依旧很稳定，输出速度为105.62 TPS。

![](https://mmbiz.qpic.cn/mmbiz_png/9j14GSZeRZZOtEzCkhCickQttuq6VyjULMeFyNrhfBRQ1wWuSxcM4PXiaFfODDKPib3zFsdUFxMJQRU17ctEkvOCEcQ2JhN41M3O4KRJsswVRk/640?wx_fmt=png)

资源占用方面，显存相对吃紧，达到了7383 MB，超过90 %，再大估计就要卸载到CPU了。

那我们试试搭配codex一起跑一下。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/9j14GSZeRZZ4Yk97mSXh4nj4pbJCPGibeibBcM6jyHzLaXpUhZvEmTPqILdnszqIwuuaVrdphbvfica43AyByw1dF1EadFnW7vrrKUKJv4VibHc/640?wx_fmt=png)

可以看到，因为模型参数比较小，显存也比较小，跑任务还是有点难度，分明有128K上下文却没有七秒钟的记忆，竟然还跟我玩起了“马什么梅啊”的梗。看来在本地工具调用的协议上，这头猛兽还有点水土不服。

虽然目前它还像一个四肢发达、头脑简单的壮汉，但别担心，谷歌这次更新的Effective架构肯定会被其他家跟进。而且他是开源的，应该很快，我们就能看到国内模型跟进这种以小博大的思路，实现遥遥领先的弯道超车了！

你觉得Google这种“虚报参数、实打实占显存”的策略，是技术革新还是显存刺客？如果让你用RTX 4070跑模型，你是要体积小、功能弱的轻量级，还是体积大、功能全的全能王？

行配置呢？

\*\*\*推荐阅读\*\*\*

[我们的WireGuard管理系统支持手机电脑了！全平台终端配置，支持扫码连接，一键搞定](https://mp.weixin.qq.com/s?__biz=MzI4NjAzMTk3MA==&mid=2458864213&idx=1&sn=ec85efce2a3b76ba244c71ccbdc09347&scene=21#wechat_redirect)

[保姆级教程：一条命令部署OpenVPN管理系统V4版，支持Win/Mac/安卓/iOS全平台接入](https://mp.weixin.qq.com/s?__biz=MzI4NjAzMTk3MA==&mid=2458864329&idx=1&sn=32eef6d6ce107136b389e05a4f206060&scene=21#wechat_redirect)

[成本省下99.7%！用40元的腾讯云服务器自建IPsecVPN，成功对接企业级飞塔防火墙](https://mp.weixin.qq.com/s?__biz=MzI4NjAzMTk3MA==&mid=2458864080&idx=1&sn=2de5d9d701d53b2c613b0c852329afb2&scene=21#wechat_redirect)

[别再乱选VPN了！实测数据告诉你：为什么L2TP是个“坑”](https://mp.weixin.qq.com/s?__biz=MzI4NjAzMTk3MA==&mid=2458865859&idx=1&sn=39ed55e57690feb1583a1a5bfb032b72&scene=21#wechat_redirect)

[密码复杂度满分却被秒破？腾讯云“白名单”闹剧与AI泄密的血泪复盘](https://mp.weixin.qq.com/s?__biz=MzI4NjAzMTk3MA==&mid=2458865769&idx=1&sn=ee32640578feb17a34732c5c2d15aa3b&scene=21#wechat_redirect)

[彻底告别密码登录！Ubuntu最强安全加固与效率提升指南](https://mp.weixin.qq.com/s?__biz=MzI4NjAzMTk3MA==&mid=2458865884&idx=1&sn=be4a6621ff07aafc6ee88eb3edfb311d&scene=21#wechat_redirect)

[告别OSPF！EVE-NG专业版+BGP Unnumbered打通Underlay的完整实战](https://mp.weixin.qq.com/s?__biz=MzI4NjAzMTk3MA==&mid=2458865266&idx=1&sn=786e8f723b95694923b257be09dbef8d&scene=21#wechat_redirect)

[从180秒到0.01秒：智算中心Underlay路由优化的速度与激情](https://mp.weixin.qq.com/s?__biz=MzI4NjAzMTk3MA==&mid=2458865295&idx=1&sn=2d4494418a2c988de36cd01ebb9f5f73&scene=21#wechat_redirect)

[嵌套虚拟化的极限时延：在2000 Mbps的风暴中，我找到了性能的真谛](https://mp.weixin.qq.com/s?__biz=MzI4NjAzMTk3MA==&mid=2458865830&idx=1&sn=f4aec87c91c032f3b43b2379717a50c7&scene=21#wechat_redirect)

[单边写入为何秒杀双边传输？从UDP 4791到BTH头，看懂RDMA的灵魂构造！](https://mp.weixin.qq.com/s?__biz=MzI4NjAzMTk3MA==&mid=2458865671&idx=1&sn=e77403c40336b5049c6d80627a0dd984&scene=21#wechat_redirect)

[手机也能跑DeepSeek-R1/Qwen3了：零成本搭建AI推理平台](https://mp.weixin.qq.com/s?__biz=MzI4NjAzMTk3MA==&mid=2458865100&idx=1&sn=ff8219a72e9800481c1e23911037e804&scene=21#wechat_redirect)

[2048卡昇腾910C集群算力集群交付工程手册](https://mp.weixin.qq.com/s?__biz=MzI4NjAzMTk3MA==&mid=2458863852&idx=1&sn=ac753705858b85d06703dab5c42a3856&scene=21#wechat_redirect)

[2048卡H100算力中心100G无阻塞存储网建设方案](https://mp.weixin.qq.com/s?__biz=MzI4NjAzMTk3MA==&mid=2458862851&idx=1&sn=7eabab449575723128152249370b069a&scene=21#wechat_redirect)

![](https://mmbiz.qpic.cn/mmbiz_jpg/5fL4uXAOMM7kUuIMJ8JGRicTGrVN3LAad2qWVLSLkZvOL0KSCibicfllib6L4g7Clp5vaZUhAgWoiahdV3kAHa2Wk6A/640?wx_fmt=jpeg)

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/5fL4uXAOMM65ich03QCp6qic3cwTmicnHZA49U7FN4y6cb4bY57OvvctIZH4ftcY5quyNfmPOvACGfVU5upxylUnQ/0?wx_fmt=png)

铁军哥

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/5fL4uXAOMM65ich03QCp6qic3cwTmicnHZA49U7FN4y6cb4bY57OvvctIZH4ftcY5quyNfmPOvACGfVU5upxylUnQ/0?wx_fmt=png)

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