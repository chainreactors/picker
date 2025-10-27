---
title: 手把手教你如何本地化部署DeepSeek
url: https://mp.weixin.qq.com/s?__biz=MzIzMTIzNTM0MA==&mid=2247497017&idx=1&sn=c755513c5dbf6ec01ad0d40eba61ae44&chksm=e8a5ff5adfd2764cbfc5d5022694332b05284a95fecaccdd14aa436daac1a63d33e4089b7287&scene=58&subscene=0#rd
source: 迪哥讲事
date: 2025-02-03
fetch_date: 2025-10-06T20:35:54.253091
---

# 手把手教你如何本地化部署DeepSeek

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/YmmVSe19Qj4z3j5OicTyT6AsaT3YEfLBm4XSYLO6ibx9axzsUdceupDggBcBJHVLcPGsPqf1xic1PUjwBq13o9mlA/0?wx_fmt=jpeg)

# 手把手教你如何本地化部署DeepSeek

原创

richardo1o1

迪哥讲事

## 正文

## 下载Ollama

进入官网https://ollama.com/download

直接下载对于版本的,笔者这里下载的是mac版本的

![](https://mmbiz.qpic.cn/mmbiz_png/YmmVSe19Qj4z3j5OicTyT6AsaT3YEfLBmG7YlDUPCyEzEnWWLgcIMXMEt16Y3LEL1eTrdicqVAFDNrYKlS9BA2OQ/640?wx_fmt=png&from=appmsg)

下载到本地之后直接解压缩,然后一键安装

![](https://mmbiz.qpic.cn/mmbiz_png/YmmVSe19Qj4z3j5OicTyT6AsaT3YEfLBmzqV1SzPrEe346nJibtgsYtiabLMk8qhpkj0QebhGfDQfhMNF5yXKvvtA/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/YmmVSe19Qj4z3j5OicTyT6AsaT3YEfLBmgO1t7sbbPbGH4siaibZXd1q9T9p6Q8Nsf6vYLqYXnL098WA5TIhsnQicQ/640?wx_fmt=png&from=appmsg)

然后下载对应的大模型如下:

https://ollama.com/library/deepseek-r1

![](https://mmbiz.qpic.cn/mmbiz_png/YmmVSe19Qj4z3j5OicTyT6AsaT3YEfLBmqz9BRiauvzrjSv3wp19IdQ1P5gQtFMMTsxgbJoXofCOyiaP4Iibsv0HBw/640?wx_fmt=png&from=appmsg)

选项和自己电脑配置有关，考虑到自己mac的配置，我这里就选择8b

![](https://mmbiz.qpic.cn/mmbiz_png/YmmVSe19Qj4z3j5OicTyT6AsaT3YEfLBmRiahMxnDp3pfYiaIX6GibLPwdFI9IyNWKubLLVVyHR4Qz4zGUt3LENMog/640?wx_fmt=png&from=appmsg)

如果你显卡和内存可以的话可以直接选择下面的选项

![](https://mmbiz.qpic.cn/mmbiz_png/YmmVSe19Qj4z3j5OicTyT6AsaT3YEfLBmfCNCkOYKsk3HT6W8JwaHeKWAsgJ4cwyEbKtwUC5fugkR6roTSlYrJw/640?wx_fmt=png&from=appmsg)

本地直接运行

```
ollama run deepseek-r1:8b
```

![](https://mmbiz.qpic.cn/mmbiz_png/YmmVSe19Qj4z3j5OicTyT6AsaT3YEfLBmHvD5DEIokM0ay0ia2NBj8CXheqCdgg6aokSLaelrNyJicCsqhqmRUcGA/640?wx_fmt=png&from=appmsg)

经过一段时间的等待,安装完成

```
writing manifest
success
>>> 你是什么模型
<think>
我是DeepSeek-R1，一个由深度求索公司开发的智能助手，我会尽我所能为您提供帮助。
</think>

我是DeepSeek-R1，一个由深度求索公司开发的智能助手，我会尽我所能为您提供帮助。
```

![](https://mmbiz.qpic.cn/mmbiz_png/YmmVSe19Qj4z3j5OicTyT6AsaT3YEfLBmRQLl0gk4FiaZicBicOKw5M2iaAOPJKpXypOP8jgp4gttObwKKTsTCDub7Q/640?wx_fmt=png&from=appmsg)

如你想用本地图形界面版本，可以安装一个UI即可

```
pip install open-webui
```

完成后，输入`open-webui serve`即可。

最后提一嘴: 关于本地部署，大多数人使用的是蒸馏后的8B/32B/70B版本，本质是微调后的Llama或Qwen模型，并不能完全发挥出DeepSeek R1的实力。

要想充分在本地释放R1的能力,显卡得上四路 RTX 4090（4×24 GB 显存）这种级别的配置,网上查了一下,价格达到2w左右,感兴趣的可以去试一波

如果你是一个长期主义者，欢迎加入我的知识星球，我们一起往前走，每日都会更新，精细化运营，微信识别二维码付费即可加入，如不满意，72 小时内可在 App 内无条件自助退款

![](https://mmbiz.qpic.cn/mmbiz_png/YmmVSe19Qj5EMr3X76qdKBrhIIkBlVVyuiaiasseFZ9LqtibyKFk7gXvgTU2C2yEwKLaaqfX0DL3eoH6gTcNLJvDQ/640?wx_fmt=png&from=appmsg)

## 往期回顾

[一款bp神器](http://mp.weixin.qq.com/s?__biz=MzIzMTIzNTM0MA==&mid=2247495880&idx=1&sn=65d42fbff5e198509e55072674ac5283&chksm=e8a5faabdfd273bd55df8f7db3d644d3102d7382020234741e37ca29e963eace13dd17fcabdd&scene=21#wechat_redirect)

[挖掘有回显ssrf的隐藏payload](https://mp.weixin.qq.com/s?__biz=MzIzMTIzNTM0MA==&mid=2247496898&idx=1&sn=b6088e20a8b4fc9fbd887b900d8c5247&scene=21#wechat_redirect)

[ssrf绕过新思路](http://mp.weixin.qq.com/s?__biz=MzIzMTIzNTM0MA==&mid=2247495841&idx=1&sn=bbf477afa30391b8072d23469645d026&chksm=e8a5fac2dfd273d42344f18c7c6f0f7a158cca94041c4c4db330c3adf2d1f77f062dcaf6c5e0&scene=21#wechat_redirect)

[一个辅助测试ssrf的工具](http://mp.weixin.qq.com/s?__biz=MzIzMTIzNTM0MA==&mid=2247496380&idx=1&sn=78c0c4c67821f5ecbe4f3947b567eeec&chksm=e8a5f8dfdfd271c935aeb4444ea7e928c55cb4c823c51f1067f267699d71a1aad086cf203b99&scene=21#wechat_redirect)

[dom-xss精选文章](http://mp.weixin.qq.com/s?__biz=MzIzMTIzNTM0MA==&mid=2247488819&idx=1&sn=5141f88f3e70b9c97e63a4b68689bf6e&chksm=e8a61f50dfd1964692f93412f122087ac160b743b4532ee0c1e42a83039de62825ebbd066a1e&scene=21#wechat_redirect)

[年度精选文章](http://mp.weixin.qq.com/s?__biz=MzIzMTIzNTM0MA==&mid=2247487187&idx=1&sn=622438ee6492e4c639ebd8500384ab2f&chksm=e8a604b0dfd18da6c459b4705abd520cc2259a607dd9306915d845c1965224cc117207fc6236&scene=21#wechat_redirect)

[Nuclei权威指南-如何躺赚](http://mp.weixin.qq.com/s?__biz=MzIzMTIzNTM0MA==&mid=2247487122&idx=1&sn=32459310408d126aa43240673b8b0846&chksm=e8a604f1dfd18de737769dd512ad4063a3da328117b8a98c4ca9bc5b48af4dcfa397c667f4e3&scene=21#wechat_redirect)

[漏洞赏金猎人系列-如何测试设置功能IV](http://mp.weixin.qq.com/s?__biz=MzIzMTIzNTM0MA==&mid=2247486973&idx=1&sn=6ec419db11ff93d30aa2fbc04d8dbab6&chksm=e8a6079edfd18e88f6236e237837ee0d1101489d52f2abb28532162e2937ec4612f1be52a88f&scene=21#wechat_redirect)

[漏洞赏金猎人系列-如何测试注册功能以及相关Tips](http://mp.weixin.qq.com/s?__biz=MzIzMTIzNTM0MA==&mid=2247486764&idx=1&sn=9f78d4c937675d76fb94de20effdeb78&chksm=e8a6074fdfd18e59126990bc3fcae300cdac492b374ad3962926092aa0074c3ee0945a31aa8a&scene=21#wechat_redirect)

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/YmmVSe19Qj4k2mXPm8xlXujVgicTGvZbcictoGLuPERQn9lRPAKkKUB5ut9XMicric8PxLRmSOq0tT5LuGuD1WemBQ/0?wx_fmt=png)

迪哥讲事

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/YmmVSe19Qj4k2mXPm8xlXujVgicTGvZbcictoGLuPERQn9lRPAKkKUB5ut9XMicric8PxLRmSOq0tT5LuGuD1WemBQ/0?wx_fmt=png)

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