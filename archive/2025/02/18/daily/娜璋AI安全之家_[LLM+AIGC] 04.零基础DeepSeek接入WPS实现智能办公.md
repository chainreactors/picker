---
title: [LLM+AIGC] 04.零基础DeepSeek接入WPS实现智能办公
url: https://mp.weixin.qq.com/s?__biz=Mzg5MTM5ODU2Mg==&mid=2247501493&idx=1&sn=1fc9b744b393a1fc45a2c700d0fef83b&chksm=cfcf7678f8b8ff6e9d1d3979c5a323e8ea28762ff379150b6c4ddea2f3b9e762b93bd89b621e&scene=58&subscene=0#rd
source: 娜璋AI安全之家
date: 2025-02-18
fetch_date: 2025-10-06T20:47:24.001625
---

# [LLM+AIGC] 04.零基础DeepSeek接入WPS实现智能办公

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/0RFmxdZEDROBSnMKhxSuDgJs7xyBvFGkm1CQbH0yUibm0QXgS5dWZgGDuNafBZYvKbpYicK15q1Z2IWjsyL3zn2w/0?wx_fmt=jpeg)

# [LLM+AIGC] 04.零基础DeepSeek接入WPS实现智能办公

原创

Eastmount

娜璋AI安全之家

> 2024年4月28日是Eastmount的安全星球 —— 『网络攻防和AI安全之家』正式创建和运营的日子，并且已坚持5个月每周7更。该星球目前主营业务为 安全零基础答疑、安全技术分享、AI安全技术分享、AI安全论文交流、威胁情报每日推送、网络攻防技术总结、系统安全技术实战、面试求职、安全考研考博、简历修改及润色、学术交流及答疑、人脉触达、认知提升等。下面是星球的新人券，欢迎新老博友和朋友加入，一起分享更多安全知识，比较良心的星球，非常适合初学者和换安全专业的读者学习。
>
> ”

![图片](https://mmbiz.qpic.cn/mmbiz_png/0RFmxdZEDRN2D0ib34nN6fIBViblH1xb9RujXz10hUiaqGBEeGK2ibe0KUfwu5rBYEAnluHZ0cAKLqASZvicFRJJ3Mw/640?wx_fmt=other&from=appmsg&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp)

感谢读者2024年对本公众号的支持。新的一年继续分享干货，共同进步，感恩同行 ^\_^

近年来，人工智能技术火热发展，尤其随着ChatGPT和DeepSeek被提出，其能够基于在预训练阶段所见的模式、统计规律和知识来生成回答，还能根据聊天的上下文进行互动，真正像人类一样来聊天交流以及完成复杂的NLP任务。基于此，为更好地学习前沿AI知识，了解LLM和AIGC应用实战，本人开启了《LLM+AIGC》专栏，一方面作为在线笔记记录和分享自己的学习过程，另一方面期望帮助更多初学者以及对LLM感兴趣的同学。知识无价人有情，希望我们都能在人生路上开心快乐、共同成长。

该系列主要涵盖三方面：

* **原理篇**——以原理介绍和论文阅读为主
* **实战篇**——以编程构建自制LLM和RAG为主
* **应用篇**——以应用实践和Prompt探索为主

前一篇文章带领大家探索DeepSeek，解决DeepSeek经常遇到的服务器繁忙问题，通过硅基流动、腾讯云、国家超算平台实现云端搭建，同时普及本地搭建和API接入知识。。这篇文章将带领大家了解如何在WPS中接入DeepSeek，并实现智能办公，包括Word和Excel，方便我们编辑各种文案和处理表格。基础性文章，希望对初学者有所帮助！且看且珍惜，加油 O(∩\_∩)O

![在这里插入图片描述](https://mmbiz.qpic.cn/mmbiz_png/0RFmxdZEDRPiajFNxJ8BvPfDR9ZAn5Jxg9IyCgTcbCiaoVHYBylibl3kSf6TDbEwezTnM9RWXy2hEtgckGDZzHFDA/640?wx_fmt=png&from=appmsg)

文章目录：

* **一.DeepSeek接入WPS**

+ **1.安装Office AI**

+ **2.配置DeepSeek**

+ **3.硅基流动配置DeepSeek**

* **二.DeepSeek智能办公实例**

+ **1.Word实例**

+ **2.Excel实例**

* **三.总结**

前文赏析：

* [[LLM+AIGC] 01.应用篇之中文ChatGPT初探及利用ChatGPT润色论文对比浅析](https://mp.weixin.qq.com/s?__biz=Mzg5MTM5ODU2Mg==&mid=2247498715&idx=1&sn=25d1d966ac5dbfdf80cf7e06df977305&scene=21#wechat_redirect)
* [[LLM+AIGC] 02.零基础DeepSeek入门初探及云端搭建详解（ChatGPT对比）](https://mp.weixin.qq.com/s?__biz=Mzg5MTM5ODU2Mg==&mid=2247501379&idx=1&sn=57bd5ed7fef46854c0205d9afabc2479&scene=21#wechat_redirect)
* [[LLM+AIGC] 03.零基础DeepSeek云端（硅基流动、腾讯云、国家超算平台）搭建及API接入](https://mp.weixin.qq.com/s?__biz=Mzg5MTM5ODU2Mg==&mid=2247501451&idx=1&sn=c16c0d24477f33768dbbfe3732a473d3&scene=21#wechat_redirect)
* [LLM+AIGC] 04.零基础DeepSeek接入WPS实现智能办公

---

# 一.DeepSeek接入WPS

首先，我们尝试在WPS中接入DeepSeek，Office接入方法类似。

## 1.安装Office AI

**第一步，下载Office AI。**

* https://www.office-ai.cn/static/introductions/officeai/introduction.html

![在这里插入图片描述](https://mmbiz.qpic.cn/mmbiz_png/0RFmxdZEDROBSnMKhxSuDgJs7xyBvFGkFD6QZaPsvxQX84TanfhW9W62CV6logwmIfwuTTicDeM55ficTwrqCQgQ/640?wx_fmt=png&from=appmsg)

**第二步，安装Office AI助手。**

![在这里插入图片描述](https://mmbiz.qpic.cn/mmbiz_png/0RFmxdZEDROBSnMKhxSuDgJs7xyBvFGkvpZdx9e3Kv07haMAo3e4ewSzMZG8QhyCBRiaUKoq5O4aATibhGYVqCTg/640?wx_fmt=png&from=appmsg)

安装过程中可能会配置相关的环境，如VB。

![在这里插入图片描述](https://mmbiz.qpic.cn/mmbiz_png/0RFmxdZEDROBSnMKhxSuDgJs7xyBvFGkZDYHB7I8s0oSFJllNNcB0pMfcLyj4LwGW27piarviaxldYicOYUpGlbIA/640?wx_fmt=png&from=appmsg)

在WPS Word中出现Office AI即表示安装成功。

![在这里插入图片描述](https://mmbiz.qpic.cn/mmbiz_png/0RFmxdZEDROBSnMKhxSuDgJs7xyBvFGkQcdTZqRWzibXgOVuviaQRhY2XQK2jo6lyE4JoDdEWeHjMiacLr3c6JcRg/640?wx_fmt=png&from=appmsg)

---

## 2.配置DeepSeek

登录成功之后如下图所示，假设存在一段作者之前撰写的论文内容。

![在这里插入图片描述](https://mmbiz.qpic.cn/mmbiz_png/0RFmxdZEDROBSnMKhxSuDgJs7xyBvFGkAFabkIGHZUpevVP6OjbU52RTGqicmAlfjTlxGEgdGJWj4Ww634FvMYQ/640?wx_fmt=png&from=appmsg)

**第一步，点击右下角设置按钮，选中“大模型设置”进行配置。**

![在这里插入图片描述](https://mmbiz.qpic.cn/mmbiz_png/0RFmxdZEDROBSnMKhxSuDgJs7xyBvFGksrEdUvTgo8T9K0LQOc6FgQ82XZvRIbEWDSh1YI7yliaic0aqJiazskXmw/640?wx_fmt=png&from=appmsg)

**第二步，按照前面的文章在DeepSeek官网申请API，并复制API Key。**

![在这里插入图片描述](https://mmbiz.qpic.cn/mmbiz_png/0RFmxdZEDROBSnMKhxSuDgJs7xyBvFGkz4UsIk2XYDqK4pVjiaGZ2RqibDv1ia7pDOiaQ8XgqwffEdP1pfCLoBrMsQ/640?wx_fmt=png&from=appmsg)

**第三步，在大模型设置中，选择“本地模型/API-KEY”。**

![在这里插入图片描述](https://mmbiz.qpic.cn/mmbiz_png/0RFmxdZEDROBSnMKhxSuDgJs7xyBvFGkAPlGHkOdf34JhRjtZatseOUKVP3zs0ZqCHD5bOo5AsvSzYoIQvvIJw/640?wx_fmt=png&from=appmsg)

选择DeepseekR1，模型选择如下：

![在这里插入图片描述](https://mmbiz.qpic.cn/mmbiz_png/0RFmxdZEDROBSnMKhxSuDgJs7xyBvFGksjKF8cCkSzGPxUMzRnRuWUmF4W2EpW86JHZQkkiapqH09Y2CpHQ1aog/640?wx_fmt=png&from=appmsg)

**第四步，在安装过程中可能会提醒需要安装私有化服务器，安装即可，如下图所示。**

![在这里插入图片描述](https://mmbiz.qpic.cn/mmbiz_png/0RFmxdZEDROBSnMKhxSuDgJs7xyBvFGklbMID23MibZyibSNLl06CicmADoDC5CSTkx7VDUnTvLUAJDX5Fcs47XiaA/640?wx_fmt=png&from=appmsg)

![在这里插入图片描述](https://mmbiz.qpic.cn/mmbiz_png/0RFmxdZEDROBSnMKhxSuDgJs7xyBvFGkgWia2bicEbLBlIb7W76KABicRWxPK3YkFvNP5RDaWTD9Itd6l9tLmAI3A/640?wx_fmt=png&from=appmsg)

点击“保存”，显示大模型设置保存成功。

![在这里插入图片描述](https://mmbiz.qpic.cn/mmbiz_png/0RFmxdZEDROBSnMKhxSuDgJs7xyBvFGkLwQtZehquhBuyEwyQYEVjWZpLMMiaSWkp0Iq4jbjTGCbv2Jd0TkGtCg/640?wx_fmt=png&from=appmsg)

安装成功后，则可运行对应的DeepSeek。

> 注意：由于作者API未充钱且当前官网暂停API充钱服务，因此提示该错误。
>
> * 厂商接口返回如下错误： {“error”:{“message”:“Insufficient Balance”,“type”:“unknown\_error”,“param”:null,“code”:“invalid\_request\_error”}} api key已失效或余额不足，请联系API-KEY提供商。

![在这里插入图片描述](https://mmbiz.qpic.cn/mmbiz_png/0RFmxdZEDROBSnMKhxSuDgJs7xyBvFGklecchiaUzI3NibI6cvKVNXnZ5bZHiaKyqyoaic8Vh9DIDrAegN5KAPIialw/640?wx_fmt=png&from=appmsg)

---

## 3.硅基流动配置DeepSeek

**第一步，打开硅基流动的官网，并注册。**

* https://siliconflow.cn/zh-cn/

![在这里插入图片描述](https://mmbiz.qpic.cn/mmbiz_png/0RFmxdZEDROBSnMKhxSuDgJs7xyBvFGk7TnuHAjOEVFlufPMJibHHTEdr0IUw93ssCrq5HHbWODvwQ09euiaQ8yA/640?wx_fmt=png&from=appmsg)

**第二步，注册登录后找到“API 密钥”。**

![在这里插入图片描述](https://mmbiz.qpic.cn/mmbiz_png/0RFmxdZEDROBSnMKhxSuDgJs7xyBvFGk6gzvAaXSZXibHa4sAB33aJDshrsAtXpf6FSkP9ERsKpv8X5GCLTdaxw/640?wx_fmt=png&from=appmsg)

新建API密钥，并定义一个名字。

![在这里插入图片描述](https://mmbiz.qpic.cn/mmbiz_png/0RFmxdZEDROBSnMKhxSuDgJs7xyBvFGklLZSeUD3Z9dVAgcmcib08yPdf385pMRgHqELA6GU4xBIrhPFskPH8og/640?wx_fmt=png&from=appmsg)

复制刚建立的API密钥。

* sk-ho\*\*\*\*\*\*\*\*\*\*tyaaokf

![在这里插入图片描述](https://mmbiz.qpic.cn/mmbiz_png/0RFmxdZEDROBSnMKhxSuDgJs7xyBvFGkZnwlVs74g1MN0Q10g4duPWlL91I9q56uAia9HWU1oGv7SKeribhUjOqg/640?wx_fmt=png&from=appmsg)

**第三步，在WPS Office AI中配置硅基流动的DeepSeek-R1。**

![在这里插入图片描述](https://mmbiz.qpic.cn/mmbiz_png/0RFmxdZEDROBSnMKhxSuDgJs7xyBvFGkeqnVkUTKw8WuFuzmiaKYHnicxO4oshqqICgHmGmdocib4kvf5zCwk0PPQ/640?wx_fmt=png&from=appmsg)

运行结果如下图所示，可以在右侧进行大模型提问并生成相关内容。

![在这里插入图片描述](https://mmbiz.qpic.cn/mmbiz_png/0RFmxdZEDROBSnMKhxSuDgJs7xyBvFGkzcPfjwGgEzGc8B8A6yXVsuTBTgk5u3gCMThBhqG67VUjd1xmQHvAcQ/640?wx_fmt=png&from=appmsg)

![在这里插入图片描述](https://mmbiz.qpic.cn/mmbiz_png/0RFmxdZEDROBSnMKhxSuDgJs7xyBvFGkXc13GrTewMWCZqevmzbiafiaHkuKaRMYO1OKIic7Mjia33rahXib902mQsA/640?wx_fmt=png&from=appmsg)

此外，生成的内容有一个“导出到左侧”按钮，可以将其内容导出。

![在这里插入图片描述](https://mmbiz.qpic.cn/mmbiz_png/0RFmxdZEDROBSnMKhxSuDgJs7xyBvFGkU1bT6uTWgXULWbPdOId373qeX6RLtylLwmTPsJppXsr1ZgdPhXImibA/640?wx_fmt=png&from=appmsg)

---

# 二.DeepSeek智能办公实例

## 1.Word实例

在Office AI中，有个“创作”按钮，可以生成各种类型的文案，如下图所示。

![在这里插入图片描述](https://mmbiz.qpic.cn/mmbiz_png/0RFmxdZEDROBSnMKhxSuDgJs7xyBvFGkB2mXJXbDvUWn1QzJvibpqqlut6xPdIEfpOPUKibeuOmpcJwXGGiaPOGxQ/640?wx_fmt=png&from=appmsg)

比如项目进度汇报：

![在这里插入图片描述](https://mmbiz.qpic.cn/mmbiz_png/0RFmxdZEDROBSnMKhxSuDgJs7xyBvFGkRkKnPGJgNZ6lAiaNP4KnIhUH7N6Zm6htnyibQ3RQjibsgvibWVvkkNmzuQ/640?wx_fmt=png&from=appmsg)
![在这里插入图片描述](https://mmbiz.qpic.cn/mmbiz_png/0RFmxdZEDROBSnMKhxSuDgJs7xyBvFGkP2UvA9QBnEib3Zv8bD8ztcZlT8quZk7YeVSHysVu5nbUZFo5V78IUXw/640?wx_fmt=png&from=appmsg)

此外，DeepSeek还能帮助Word排版，读者可以尝试进一步拓展。

---

## 2.Excel实例

同样，Excel也能导入DeepSeek。然而，打开Excel可能没有Office AI。如何解决呢？

![在这里插入图片描述](https://mmbiz.qpic.cn/mmbiz_png/0RFmxdZEDROBSnMKhxSuDgJs7xyBvFGk5t3wogK3K4BQeDIEysOgm6SVMgHOrL0ENiarHvOdFae78p00aoQGGYA/640?wx_fmt=png&from=appmsg)

**第一步，在“工具”中点击“COM加载项”，因为作者已禁用第三方加载项，开启即可。**

![在这里插入图片描述](https://mmbiz.qpic.cn/mmbiz_png/0RFmxdZEDROBSnMKhxSuDgJs7xyBvFGkX8MjD6SCn2ExsfibInm6a96f856qjKRcrXufSDlOc8ug306WAUIUVnA/640?wx_fmt=png&from=appmsg)

**第二步，加载启用HyExcelAI。**

![在这里插入图片描述](https://mmbiz.qpic.cn/mmbiz_png/0RFmxdZEDROBSnMKhxSuDgJs7xyBvFGkGibaU9OpWTiaiapSJQb6oggabqklaCC5zicvS3zv4pQHUpEJFzBD6qByvw/640?wx_fmt=png&from=appmsg)

![在这里插入图片描述](https://mmbiz.qpic.cn/mmbiz_png/0RFmxdZEDROBSnMKhxSuDgJs7xyBvFGkibUZwYqIeH3LLpLtnJYprsvtkZlicOAV1icI2qVGSk7gJCiaaDZqOiaib1ibQ/640?wx...