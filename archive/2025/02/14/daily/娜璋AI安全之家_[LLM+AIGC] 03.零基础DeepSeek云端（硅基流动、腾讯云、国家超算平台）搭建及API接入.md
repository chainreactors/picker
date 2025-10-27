---
title: [LLM+AIGC] 03.零基础DeepSeek云端（硅基流动、腾讯云、国家超算平台）搭建及API接入
url: https://mp.weixin.qq.com/s?__biz=Mzg5MTM5ODU2Mg==&mid=2247501451&idx=1&sn=c16c0d24477f33768dbbfe3732a473d3&chksm=cfcf7646f8b8ff507d3c3c845d5f860d3c939d809754b79662918fc8dafe3660600ac19185c2&scene=58&subscene=0#rd
source: 娜璋AI安全之家
date: 2025-02-14
fetch_date: 2025-10-06T20:39:31.841514
---

# [LLM+AIGC] 03.零基础DeepSeek云端（硅基流动、腾讯云、国家超算平台）搭建及API接入

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/0RFmxdZEDRPKwdAia7CDStLEmza6yljl8PEF90RIibMuaDpKflDSKVvx09jJ1ib679mzgT2DlCaBfRsN7y9JdKPPA/0?wx_fmt=jpeg)

# [LLM+AIGC] 03.零基础DeepSeek云端（硅基流动、腾讯云、国家超算平台）搭建及API接入

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

前一篇文章普及了DeepSeek基础知识，并与ChatGPT 4o进行简单对比。这篇文章将带领大家探索DeepSeek，解决DeepSeek经常遇到的 服务器繁忙问题 ，通过硅基流动、腾讯云、国家超算平台实现云端搭建，同时普及本地搭建和API接入知识。基础性文章，希望对初学者有所帮助！且看且珍惜，加油 O(∩\_∩)O

![在这里插入图片描述](https://mmbiz.qpic.cn/mmbiz_png/0RFmxdZEDRPiajFNxJ8BvPfDR9ZAn5Jxg9IyCgTcbCiaoVHYBylibl3kSf6TDbEwezTnM9RWXy2hEtgckGDZzHFDA/640?wx_fmt=png&from=appmsg)

文章目录：

* **一.硅基流动云端搭建DeepSeek**
* **二.腾讯云搭建DeepSeek**
* **三.国家超算平台搭建DeepSeek**
* **四.本地搭建DeepSeek**
* **五.DeepSeek API接口使用**
* **六.总结**

前文赏析：

* [[LLM+AIGC] 01.应用篇之中文ChatGPT初探及利用ChatGPT润色论文对比浅析](https://mp.weixin.qq.com/s?__biz=Mzg5MTM5ODU2Mg==&mid=2247498715&idx=1&sn=25d1d966ac5dbfdf80cf7e06df977305&scene=21#wechat_redirect)
* [[LLM+AIGC] 02.零基础DeepSeek入门初探及云端搭建详解（ChatGPT对比）](https://mp.weixin.qq.com/s?__biz=Mzg5MTM5ODU2Mg==&mid=2247501379&idx=1&sn=57bd5ed7fef46854c0205d9afabc2479&scene=21#wechat_redirect)
* [LLM+AIGC] 03.零基础DeepSeek云端（硅基流动、腾讯云、国家超算平台）搭建及API接入

---

# 一.硅基流动云端搭建DeepSeek

**第一步，打开硅基流动的官网，并注册。**

* https://siliconflow.cn/zh-cn/

![在这里插入图片描述](https://mmbiz.qpic.cn/mmbiz_png/0RFmxdZEDRPKwdAia7CDStLEmza6yljl8NAnMsD21icvxkoUczPDX6CQaeZGDM042Qs3mlUPHezjzJzH9roq0v6w/640?wx_fmt=png&from=appmsg)

**第二步，注册登录后找到“API 密钥”。**

![在这里插入图片描述](https://mmbiz.qpic.cn/mmbiz_png/0RFmxdZEDRPKwdAia7CDStLEmza6yljl8yAGAqODHgJficbtZWlzO67ccxfY1GSlfrIyRP1bUcDG2IQaMJCjVKVw/640?wx_fmt=png&from=appmsg)

新建API密钥，并定义一个名字。

![在这里插入图片描述](https://mmbiz.qpic.cn/mmbiz_png/0RFmxdZEDRPKwdAia7CDStLEmza6yljl8uvDE2NrNm2E7ZkjNgoZ9BDSlNHkyMLmLXUTnia6rGxB9BM9wibMt2KCA/640?wx_fmt=png&from=appmsg)

复制刚建立的API密钥。

* sk-ho\*\*\*\*\*\*\*\*\*\*tyaaokf

![在这里插入图片描述](https://mmbiz.qpic.cn/mmbiz_png/0RFmxdZEDRPKwdAia7CDStLEmza6yljl86oVejtzGAK2NMwibRyQTAXXRjCrRnO3y8u18MK7u4xLEYK9Bb9OL6Cg/640?wx_fmt=png&from=appmsg)

**第三步，打开Chatbox AI官方网站，点击“启用网页版”。**

* https://chatboxai.app/zh

![在这里插入图片描述](https://mmbiz.qpic.cn/mmbiz_png/0RFmxdZEDRPKwdAia7CDStLEmza6yljl8fZPuhkQNcswZWh6EE9EyNneWZTa4JZpaz5jaoYkae33jVLXbMs6gXQ/640?wx_fmt=png&from=appmsg)

> 读者可以选择右上角语言为中文。

**第四步，在弹出的窗口中选择“使用自己的API Key或本地模型”。**

![在这里插入图片描述](https://mmbiz.qpic.cn/mmbiz_png/0RFmxdZEDRPKwdAia7CDStLEmza6yljl8tTHh29iaSPLwl1265ic7JZtPYmlfriausVyo3eicqEskMviaOZtrZfh6ibTA/640?wx_fmt=png&from=appmsg)

**第五步，选择硅基流动我们刚创建的API。**

![在这里插入图片描述](https://mmbiz.qpic.cn/mmbiz_png/0RFmxdZEDRPKwdAia7CDStLEmza6yljl8EG8RukTD9YfMQRjzetAIAOEicSibTb7a2bNibC3icicLBsqUJtT5K5X4AUg/640?wx_fmt=png&from=appmsg)

**第六步，粘贴API密钥并选择DeepSeek-R1模型，并点击保存。**

![在这里插入图片描述](https://mmbiz.qpic.cn/mmbiz_png/0RFmxdZEDRPKwdAia7CDStLEmza6yljl81WvkOvsAQt1a9XOeBrTA32WaQjsOIZBs7EVuMgfZQneicQp5UDTRPuA/640?wx_fmt=png&from=appmsg)

![在这里插入图片描述](https://mmbiz.qpic.cn/mmbiz_png/0RFmxdZEDRPKwdAia7CDStLEmza6yljl8CuG5jvibdweyT2mAPTkhCpKjF2biaX0IBia926QYndZdial3N0q74dllibg/640?wx_fmt=png&from=appmsg)

第七步，创建一个新的对话开始聊天和智能问答。

![在这里插入图片描述](https://mmbiz.qpic.cn/mmbiz_png/0RFmxdZEDRPKwdAia7CDStLEmza6yljl8iaumMmiaVhFfYxM7CONO1OVNSUHoqsAzqPLmAptmuG1z9sJgSyVhoL9Q/640?wx_fmt=png&from=appmsg)

至此，我们创建了自己的云端DeepSeek模型，可以进行交互。譬如前面的3个问题，其结果如下图所示：

![在这里插入图片描述](https://mmbiz.qpic.cn/mmbiz_png/0RFmxdZEDRPKwdAia7CDStLEmza6yljl8ib2qrYtXO5H8rHeibEst2qeRjwWPNNyBRFBxLZ4P03or9IVRm802wU3Q/640?wx_fmt=png&from=appmsg)

整体效果还不错，可以看到其思考过程，并给出简单的学习流程图。

![在这里插入图片描述](https://mmbiz.qpic.cn/mmbiz_png/0RFmxdZEDRPKwdAia7CDStLEmza6yljl8fpiaBclX7HVxS7xGuiaYnrZPu63MhqEMkXODc8J0MggfXCw05zUIicZGg/640?wx_fmt=png&from=appmsg)
![在这里插入图片描述](https://mmbiz.qpic.cn/mmbiz_png/0RFmxdZEDRPKwdAia7CDStLEmza6yljl8IeCFcPxbZobREibVR4DmaxaoczOR7Y698vtBNibQJib7IGnrOqBESicFZg/640?wx_fmt=png&from=appmsg)

最后给出利用ChatGPT辅助学习Python机器学习的学习建议，包括简单的示例代码。

![在这里插入图片描述](https://mmbiz.qpic.cn/mmbiz_png/0RFmxdZEDRPKwdAia7CDStLEmza6yljl8kEHeAfV9NDX97wiar9Xz7BOs9Wxvu2ReefTfIOhYJh0rkLiahMqia1kFQ/640?wx_fmt=png&from=appmsg)
![在这里插入图片描述](https://mmbiz.qpic.cn/mmbiz_png/0RFmxdZEDRPKwdAia7CDStLEmza6yljl8PCnicW9h3x0UwvichLGTicuPLQZIRqKbjoDrakC7SBib2B8Kp3f0aw9wdA/640?wx_fmt=png&from=appmsg)

---

# 二.腾讯云搭建DeepSeek

下面介绍腾讯云如何搭建DeepSeek，其至2月25日前免费。

**第一步，注册并登录腾讯云。**

![在这里插入图片描述](https://mmbiz.qpic.cn/mmbiz_png/0RFmxdZEDRPKwdAia7CDStLEmza6yljl8bEY9fT6ybSoIph7h2LeuksH0SGdT2o6dhA0W2Nob4ibKSNhSpeAibetQ/640?wx_fmt=png&from=appmsg)

**第二步，在“产品”中找到“人工智能与机器学习”->“腾讯云 TI平台”。**

![在这里插入图片描述](https://mmbiz.qpic.cn/mmbiz_png/0RFmxdZEDRPKwdAia7CDStLEmza6yljl8T0n97vaKeowgNUdOXP8okkwnnWqicl36Oliay5Wqtcza5VN5NJ9Kv4dQ/640?wx_fmt=png&from=appmsg)

**第三步，在该页面点击“立即使用”。**

![在这里插入图片描述](https://mmbiz.qpic.cn/mmbiz_png/0RFmxdZEDRPKwdAia7CDStLEmza6yljl8Hhz2URmfia90BjKfu71hvvn73F6Ge5cxpJYK38Fmg7T2odFXTcfan0A/640?wx_fmt=png&from=appmsg)

运行结果如下图所示，进行简要的授权。

![在这里插入图片描述](https://mmbiz.qpic.cn/mmbiz_png/0RFmxdZEDRPKwdAia7CDStLEmza6yljl8F2q4mwupNBgicY4I2Q1BEwWVKRwev4ZUs32yLBg0pft9eB2lJJ2mPSw/640?wx_fmt=png&from=appmsg)

![在这里插入图片描述](https://mmbiz.qpic.cn/mmbiz_png/0RFmxdZEDRPKwdAia7CDStLEmza6yljl8ckq97Ok0zPNh4eQbSyWkPNQ4sGvp1kBkd0oVDCoqiciazMYRkSXAjSYg/640?wx_fmt=png&from=appmsg)

**第四步，在大模型广场中选择“DeepSeek系列模型”。**

![在这里插入图片描述](https://mmbiz.qpic.cn/mmbiz_png/0RFmxdZEDRPKwdAia7CDStLEmza6yljl8k1kgtGgkrTETzM3Da4DYayqDGGsTjElM8icEgHkVuMTReKmGw8Uicjpg/640?wx_fmt=png&from=appmsg)

进入页面可以看到基础用法，也可以点击“模型体验”进行简单测试。注意，我们需要查看API调用指引。

> 如您需要直接调用腾讯云上的 DeepSeek API，请通过以下链接获取API接口文档及费用说明：
>
> * https://cloud.tencent.com/document/product/1772/115963

![在这里插入图片描述](https://mmbiz.qpic.cn/mmbiz_png/0RFmxdZEDRPKwdAia7CDStLEmza6yljl8J05JLWdc7Jo4GshHgDahjpDVkmIPPFRicYFr68ub1JPZtj4f5knoNXQ/640?wx_fmt=png&from=appmsg)

**第五步，点击上述链接，查看API接口描述。**

> 限时免费至2025年2月25日

![在这里插入图片描述](https://mmbiz.qpic.cn/mmbiz_png/0RFmxdZEDRPKwdAia7CDStLEmza6yljl8FcqRbow7licZT1jlLD0S3KOFZQwG6BkG1bOpSGLNaTMHAEmTViamevLw/640?wx_fmt=png&from=appmsg)

**第六步，点击 API KEY管理进行相关配置。**

![在这里插入图片描述](https://mmbiz.qpic.cn/mmbiz_png/0RFmxdZEDRPKwdAia7CDStLEmza6yljl8uZdr65L3tkpfRicII5xNDwzTt2FI7ebFfArnF4caVra7bAaJGFXP6qg/640?wx_fmt=png&from=appmsg)

![在这里插入图片描述](https://mmbiz.qpic.cn/mmbiz_png/0RFmxdZEDRPKwdAia7CDStLEmza6yljl8Myr1Wqufy1rhsn8v5Fz825zMBIuFDJUOuECvfYicFznf2OGNB8xKQaA/640?wx_fmt=png&from=appmsg)

控制台界面如下图所示：

![在这里插入图片描述](https://mmbiz.qpic.cn/mmbiz_png/0RFmxdZEDRPKwdAia7CDStLEmza6yljl8odkHTL2ahNazeCgIxJtHhd91hGGQibAB7JebFwIHtiaRngJ8DxxO2ialw/640?wx_fmt=png&from=appmsg)

**第七步，点击左栏“API KEY管理”，创建API KEY。**

![在这里插入图片描述](https://mmbiz.qpic.cn/mmbiz_png/0RFmxdZEDRPKwdAia7CDStLEmza6yljl8T4AqtJ14wBogGlpRibGujMZTzxYwz3xZghTAiajyyKo0CMEDT3Z6O9UA/640?wx_fmt=png&from=appmsg)

系统会自动创建，查看复制即可。

![在这里插入图片描述](https://mmbiz.qpic.cn/mmbiz_png/0RFmxdZEDRPKwdAia7CDStLEmza6yljl8sWiaaKDjnmJ5nicBbjHEoJpLTZcUbWsKuBHydYEVYpiaDwDzj4dx7qT3Q/640?wx_fmt=png&from=appmsg)

**第八步，下载Chatbox或在网页版配置。**

* https://chatboxai.app/zh

![在这里插入图片描述](https://mmbiz.qpic.cn/mmbiz_png/0RFmxdZEDRPKwdAia7CDStLEmza6yljl86OxROttmCRZZIIYqeextiaH8N6G72Tsf2CKSvyfP6DIfd0bI2fkahyA/640?wx_fmt=png&from=appmsg)

安装Chatbox。

![在这里插入图片描述](https://mmbiz.qpic.cn/mmbiz_png/0RFmxdZEDRPKwdAia7CDStLEmza6yljl8wrAIbKTF8G8nKicrE2w1eeNBkJXszqDicrwzO52tfsTs7Sawpt0kdzAA/640?wx_fmt=png&from=appmsg)

关闭并点击“设置”。

![在这里插入图片描述](https://mmbiz.q...