---
title: 自研C2如何嵌入AI助手？
url: https://mp.weixin.qq.com/s/F5KNlTJUa0CTVXYHrrka8g
source: Doonsec's feed
date: 2026-02-27
fetch_date: 2026-02-28T03:52:17.894795
---

# 自研C2如何嵌入AI助手？

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/Hb5KMDMWSgjr9MXvcQvXHskkyc0YPsLbJH3Ku0opNShX8WLvJS4MetAY3p7ltcwOJpxviatKECWSbgX67tzwiaenv6JibnYeQaRCRkZYXS4KOM/0?wx_fmt=jpeg)

# 自研C2如何嵌入AI助手？

原创

T3Ysec
T3Ysec

T3Ysec

![]()

在小说阅读器中沉浸阅读

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/8Ovfo3wiaWcEPianhVAh3e6icK6fNEVaOGnVuaJyAg4jsWKozSGU0bNToibPEtQHgGYbPTE1exs9icene4wEL3nuY4Q/640?from=appmsg)

**壹**

****如何在自研C2中嵌入AI助手？****

**壹**

**自研C2，功能展示**

该系统是我自主研发的一套C2框架（协议支持HTTP/ICMP，功能支持**CS大部分操作如bof等等**，特色是**动态数据包**），也是我的毕业设计，在看了大部分攻防的agent发现难点不是在于如何测试漏洞，而是在于发现漏洞后需要一个AI交互的终端去接收shell或者是数据，于是我就实现了MCP+内置大模型助手，为大模型后渗透提供强力的装备。

![image.png](https://mmbiz.qpic.cn/mmbiz_png/Hb5KMDMWSghBd57O3mp81OAPvCGS02QrrELz4zTQPTwOBWGyjKRiaABJLe8t03hfaA7Uudo7nPLu1YMRPlDr5cUT1pFyQ392oEsfrdu7fACs/640?from=appmsg)

![image.png](https://mmbiz.qpic.cn/mmbiz_png/Hb5KMDMWSggKuRaCh5g9Q6Oia6wIE3Ndeob2KYygPMVSWAL2uPEay8MTRECVku9KRD4GkwO1SZJpsiaWuTOMiaxPXU8WDr7HXmVS3Z2sBXu4XA/640?from=appmsg)

![image.png](https://mmbiz.qpic.cn/mmbiz_png/Hb5KMDMWSggibPWUnBz432UjtgVF9E2TWKABxqAf9XDIuRoiboAXFWHwBIicBhlViaygNQbribl25YNqxTteBRxgiaBF5hpWBZrFjTVFCb9RyAm2A/640?from=appmsg)

**壹**

****LLM 实现记忆功能思路****

业内对于大模型助手的记忆实现模块主要是缓冲记忆，缓冲窗口记忆，令牌缓冲记忆，摘要总结记忆，摘要缓冲混合记忆和向量存储库记忆这六种记忆模式。

以下是这六种记忆模式的通俗拆解：

---

### **1. 缓冲记忆 (Conversation Buffer Memory)**

这是最基础、最直观的模式。

* **原理：**它像一个“全文复读机”，将对话历史原封不动地存储起来。每次新提问时，它都会把之前的全部对话拼接到 Prompt 中传给 AI。
* **优点：**能够精准还原语境，不会丢失细节。
* **缺点：**随着对话变长，消耗的 Token 会呈爆炸式增长，最终可能超出模型的上下文限制（Context Window）。

### **2. 缓冲窗口记忆 (Conversation Buffer Window Memory)**

为了解决长度问题，它引入了“滑动窗口”。

* **原理：**它只保留最近的 $K$ 轮对话。比如设置 $K=5$，那么它只记得最后 5 组问答，更早的内容会被直接“丢进垃圾桶”。
* **优点：**Token 消耗非常稳定，防止模型因为历史太长而“糊涂”。
* **缺点：**缺乏“长时记忆”，一旦聊得久了，AI 就会忘记开头谈论的主题。

### **3. 令牌缓冲记忆 (Conversation Token Buffer Memory)**

这是一种更科学的“截断”方式。

* **原理：**与其按“对话轮数”截断，不如按“Token 数量”截断。它会实时监控存储的字符数，一旦超过设定的阈值（如 2000 Tokens），就自动删除最早的对话。
* **优点：**能够最大化利用上下文空间，比窗口记忆更精准地控制成本。

### **4. 摘要总结记忆 (Conversation Summary Memory)**

这种模式不再死记硬背。

* **原理：**系统会调用另一个（或同一个）LLM，定期对之前的对话进行浓缩摘要。新对话发生时，AI 看到的是“过去对话的梗概 + 当前问题”。
* **优点：**能够保留对话的长期核心要点，极大地节省空间。
* **缺点：**摘要过程会损失很多细节，且每次生成摘要都要额外消耗 API 费用。

### **5. 摘要缓冲混合记忆 (Conversation Summary Buffer Memory)**

它是“总结”与“缓冲”的结合体，目前最均衡的方案。

* **原理：**1.  对最近的对话保留原始内容（Buffer），确保当下交流的细节。

  2.  对较早之前的对话进行摘要压缩（Summary）。
* **优点：**既保证了近期交流的连贯性和细节，又通过摘要保留了长期的背景信息。

### **6. 向量存储库记忆 (VectorStore-Retriever Memory)**

这种模式本质上是 **RAG（检索增强生成）** 在对话记忆中的应用。

* **原理：**它将每一轮对话都转换成向量（Vector）并存入数据库。当用户提问时，它会去数据库里搜索“语义最相关”的历史记录提取出来。
* **优点：**拥有“海量记忆”。即使聊过一万句，只要你提到了某个关键词，它就能瞬间找回几个月前的相关谈话。
* **缺点：**检索过程可能导致上下文缺乏连续性（只拿到碎片化的记录）。

      在记忆这块我的选择是摘要缓冲混合记忆，这种可以保证在长对话的情况下还能记住用户的习惯和操作。

通过将用户对话和大模型回答的内容嵌入到下一次的对话，实现缓冲窗口记忆，具体的代码：

![image.png](https://mmbiz.qpic.cn/sz_mmbiz_png/Hb5KMDMWSggdAULfQtOebBonRjO1Xq7gNLFgBap9vzxo1zqwvR7SciaicMjsCfhNGueBvd8xUFNR0CZN9D9hSRzeStArUanrxkwU5CiaSJ25DM/640?from=appmsg)

       由于大模型是有输入窗口的大小，在这种模式下长期对话会导致问答的窗口指数级增长，我们需要对上下文进行一个摘要，在这里我配置的是100次对话后需要自动摘要在+历史消息，具体代码：

![image.png](https://mmbiz.qpic.cn/sz_mmbiz_png/Hb5KMDMWSgjtlPvX8nEnXLdP7C7YXFFd0ZJHJvtobD42icrj9XJHMvZoOdib4HFnezBPEXUMHgAGZxjh0UN0rxHWEJRzSeW1RllkU5q1SDb9s/640?from=appmsg)

       压缩完后继续拼接使用。但是这种无法实现一个在程序关闭后下次启动就会丢记忆，在这里我采用了md形式去记录用户和大模型的问题，就相当于整个大模型记忆操作的“白板”就是这个md：

![image.png](https://mmbiz.qpic.cn/sz_mmbiz_png/Hb5KMDMWSgiaUvtEwlHpzbF2p9863phRojMvQ8bXaJp2yTKhYS7ChibFp1NpGgev1liczAC4lbYzTxiaTeCnBq5R2b78Jk5Y1qzM1tbYL3Mgxfg/640?from=appmsg)

![image.png](https://mmbiz.qpic.cn/mmbiz_png/Hb5KMDMWSgiaob9Ef4qXp1vgJ0urCB9pHZPPQz3puJD2pX0kNyp2YmNP8nUR6BvuqOtYnKo3fHjgdgyTWS2LsBZ76ibQJJYmgibxLsTOjicicJMA/640?from=appmsg)

这样就可以实现一个永有长期记忆并且可以指导系统使用和后渗透的“贾维斯”了

**壹**

**给助手实现与C2的交互**

      在这个交互的实现，我想到就是使用MCP，而不是硬 编码的函数在agent中内置工具，如果通过内置函数的话 ：

1.扩展性很差，不能给其他agent使用。

2.会有大量代码侵入原本的框架代码中，后期维护差。

快速使用AI vibe coding开发：先让AI将所有的路由接口提取和接口功能，生成一份接口文档：

![image.png](https://mmbiz.qpic.cn/sz_mmbiz_png/Hb5KMDMWSgia387TbgEGicpsOogKyYJDQ0YjdlQv39Q40uNuPljR8a4JTmWKYSvf4nFa7UbfrBFFicjanmESIgm3EDu7z4cXgqZ8nibKx8qXz8I/640?from=appmsg)

在让AI根据接口文档写一个不入侵原本框架代码的MCP功能，在暴露一个启动函数给C2主逻辑使用就可以。

![image.png](https://mmbiz.qpic.cn/sz_mmbiz_png/Hb5KMDMWSgghfB5jIS7GUwkjLfqy442hZsSpGaFaZjkEUseWXiaFrPryjqz1j3xmAot3pULtmLN5PHM1PtB6UkqovqYuIJdxPlPWNzIibPKCA/640?from=appmsg)

**壹**

**总结**

在 AI 驱动的开发范式下，‘Vibe Coding’ 正逐渐成为主流。开发者核心竞争力的重心理应发生偏移：从底层的代码实现，转向高层的系统架构设计，以及精细化的\*\* Prompt Engineering（提示词工程）\*\*。

       目前 **Eagle C2** 尚处于封闭测试阶段，为了确保系统的稳定性与安全性，暂时还无法面向公众开放。请大家再多给我一点时间，我正全力完善各项功能，力求在正式见面时交出一份完美的答卷。

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/X2dze5v2iauLEYvkJw1bVrkGcuR9buib3puCUlPlGXhXsKs4sbTwCbCViaYiaBWZehNG1Tic8ibgicALzBzotEZZy2zSA/0?wx_fmt=png)

T3Ysec

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/X2dze5v2iauLEYvkJw1bVrkGcuR9buib3puCUlPlGXhXsKs4sbTwCbCViaYiaBWZehNG1Tic8ibgicALzBzotEZZy2zSA/0?wx_fmt=png)

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