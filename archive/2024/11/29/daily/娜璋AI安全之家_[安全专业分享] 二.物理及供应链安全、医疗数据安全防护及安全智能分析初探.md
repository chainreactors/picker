---
title: [安全专业分享] 二.物理及供应链安全、医疗数据安全防护及安全智能分析初探
url: https://mp.weixin.qq.com/s?__biz=Mzg5MTM5ODU2Mg==&mid=2247501035&idx=1&sn=e52b5d7012ddf9edbc115d1b7282ecad&chksm=cfcf7426f8b8fd307c9880051bc6452528ac77f6cc6f21e7078840b0dac57880cb01cf4de51b&scene=58&subscene=0#rd
source: 娜璋AI安全之家
date: 2024-11-29
fetch_date: 2025-10-06T19:18:50.870261
---

# [安全专业分享] 二.物理及供应链安全、医疗数据安全防护及安全智能分析初探

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/0RFmxdZEDROpVwic9Q0QtP9cvK4PhcWQiaYcew2Uplw4Tqtha95ZOiccmtnbcGuv34iagLricGRWiaiaP0wrZZWL3xVdA/0?wx_fmt=jpeg)

# [安全专业分享] 二.物理及供应链安全、医疗数据安全防护及安全智能分析初探

原创

Eastmount

娜璋AI安全之家

> 2024年4月28日是Eastmount的安全星球 —— 『网络攻防和AI安全之家』正式创建和运营的日子，并且已坚持5个月每周7更。该星球目前主营业务为 安全零基础答疑、安全技术分享、AI安全技术分享、AI安全论文交流、威胁情报每日推送、网络攻防技术总结、系统安全技术实战、面试求职、安全考研考博、简历修改及润色、学术交流及答疑、人脉触达、认知提升等。下面是星球的新人券，欢迎新老博友和朋友加入，一起分享更多安全知识，比较良心的星球，非常适合初学者和换安全专业的读者学习。
>
> ”

![](https://mmbiz.qpic.cn/mmbiz_png/0RFmxdZEDROpVwic9Q0QtP9cvK4PhcWQiapwvM2vlMlibuqZ8dkibLZ8HxyF1by7dk77Giba26KMsuWCDQd4BQNSrHg/640?wx_fmt=png&from=appmsg)

作为一名信息安全、网络安全、系统安全的初学者，我应该掌握哪些基本知识呢？作为一名硕士研究生，我应该如何快速开启学术研究呢？作为一名专业调剂或从未接触过学术论文的学生，我应该如何确定研究方向和开启自己的第一个工作呢？在数智化、网络化时代，我们又将如何开启AI for Science和AI for Security的研究呢？

新开《信息系统安全》系列专业知识分享，希望这些基础知识对大家有所帮助，也欢迎各位大佬、老师和博友批评指正。这篇文章主要涵盖四块内容：

* **（1）结合突发事件分享物理和供应链安全**
* **（2）医疗数据安全**
* **（3）安全智能分析**
* **（4）机器学习入门实战**

前文赏析：

* [[安全专业分享] 一.《信息系统安全》初识及研究生学术初探](https://mp.weixin.qq.com/s?__biz=Mzg5MTM5ODU2Mg==&mid=2247500918&idx=1&sn=4dc8c23fb70a4e0b713a5d6467dafc28&scene=21#wechat_redirect)
* [安全专业分享] 二.物理及供应链安全、医疗数据安全防护及安全智能分析初探

> **温馨提示：**该系列内容以PPT形式分享为主，减少文字内容的描述。同时分享的安全课本内容会少一些，这些内容线下会详细讲解，博客以研究生学术探索和AI安全应用浅析为主。希望未来能与大家线下交流安全技术和探讨学术探索。感恩遇见，不负青春！祝好。

### **前言**

![](https://mmbiz.qpic.cn/mmbiz_png/0RFmxdZEDROpVwic9Q0QtP9cvK4PhcWQiaDHSUdjLia9y6m3cfZgHttDaWTCj3gMPaCcLlqZoLDGuOJaZJtZicAUmg/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/0RFmxdZEDROpVwic9Q0QtP9cvK4PhcWQiaviaqic4ibxQFibMmoSiag9vHCSdJca2pbXibWRwGSF0yggOGxMn7y9UK2Xbw/640?wx_fmt=png&from=appmsg)

PS：个人还是比较菜，简历和简介的3页PPT就不放出来了 O(∩\_∩)O

### **一.物理及供应链安全**

首先，结合最新攻击事件普及了物理安全和供应链安全基础知识。

![](https://mmbiz.qpic.cn/mmbiz_png/0RFmxdZEDROpVwic9Q0QtP9cvK4PhcWQiacYR6oXR0wdunljAxVSblNqebXvSCyAiawOyYF74H3er1vBd8nzbKPHA/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/0RFmxdZEDROpVwic9Q0QtP9cvK4PhcWQiaZYZzPapzko7dKw9KhwVzqVp6o299F0y2zq9lxF5hhMyreClibwLS4qw/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/0RFmxdZEDROpVwic9Q0QtP9cvK4PhcWQiadlHEjAibd6ng5CaAH3ZfxgU9D1FGFzcDXZstcYdNXWW6Go7VHC5jDFA/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/0RFmxdZEDROpVwic9Q0QtP9cvK4PhcWQiaNQLrxdqcWa5EqrC8ib1GVkib46OP9qC8pGhNrTN23R3uy7cDndrnmZmw/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/0RFmxdZEDROpVwic9Q0QtP9cvK4PhcWQiaVicc7bY1ghkLmupjCjTEPPP1kavEJsKdU3nyiaGFYicufr8Qyl3cP6asg/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/0RFmxdZEDROpVwic9Q0QtP9cvK4PhcWQia2v3XHRJk9Kc3knQYes1CfMkZZbuughc6jl28VD4suwQobMgqEm22Mg/640?wx_fmt=png&from=appmsg)

### **二.医疗数据安全**

其次，详细介绍医疗数据安全知识，该部分亦是作者面向医疗行业的某次分享内容（省略版）。主要包括：**医疗数据安全概况、医疗卫生行业中的攻与防、医疗数据保护策略。**

**第一部分：医疗数据安全概况**

![](https://mmbiz.qpic.cn/mmbiz_png/0RFmxdZEDROpVwic9Q0QtP9cvK4PhcWQia54FgY933TP6bjKEW2pIKhZN0icLSA1Wib9856vmMadXHiaDl2roLa4hmg/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/0RFmxdZEDROpVwic9Q0QtP9cvK4PhcWQiajfcImsv8lxBycic2X5UFaTNaGxTI07BicHaViakO5Xa6PNKia1DGpj5yRA/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/0RFmxdZEDROpVwic9Q0QtP9cvK4PhcWQiaKgmxcfCA6ibIbjoIgSu6mAIEpjMZgyzHlOicKnjLjicBNTeicDBFib6eQWg/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/0RFmxdZEDROpVwic9Q0QtP9cvK4PhcWQia2uXfxEbV5GWTsrVgxAO3k3TE2XGsqKT0dASoGC1Kwf09fTJicEpicibuA/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/0RFmxdZEDROpVwic9Q0QtP9cvK4PhcWQiaOhyoNlicqE1G4afGmnrvzicjzBZFMA5hVG7UKeTOT6XanuHapjrFfiaIA/640?wx_fmt=png&from=appmsg)

**第二部分：医疗行业中的攻与防**

![](https://mmbiz.qpic.cn/mmbiz_png/0RFmxdZEDROpVwic9Q0QtP9cvK4PhcWQiaIhTQhox5ibARTCmJKVYdCf0mLEUHer2Vt4adwL3icEeQnU0oLibiaAsvAg/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/0RFmxdZEDROpVwic9Q0QtP9cvK4PhcWQiaeic9MFtDddwIsqfIeJv1NZqnxafZ0UhpN2ya8aZTyt0ZPYsTFM4epdA/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/0RFmxdZEDROpVwic9Q0QtP9cvK4PhcWQiavG7pmgu6h4Pog7HwhicWibqzEB6vKhticBVF8Kj6AyamP1e6ECuRntrcg/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/0RFmxdZEDROpVwic9Q0QtP9cvK4PhcWQia5I3OzFaib6QXGs3zMYBmBnLguVMuHLOC1ziceA34fwEHB4icFpibu8LV6g/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/0RFmxdZEDROpVwic9Q0QtP9cvK4PhcWQia7BZvPSdExtIyaQypSyBycg3d6Q5IjyicUc2Q9JDZps1bnJVWlDibEEtg/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/0RFmxdZEDROpVwic9Q0QtP9cvK4PhcWQiaCib8p3zibD48vsE9flbstvPia8NZ0PtXCFn9FMvwfmzib1ZFY5aicHxx36A/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/0RFmxdZEDROpVwic9Q0QtP9cvK4PhcWQiaaIoLqpTgIKPfSh2U9P7SeAwgBgJiaMAKKKqrRo56diaf6ibNeH0t2HjKg/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/0RFmxdZEDROpVwic9Q0QtP9cvK4PhcWQiaf7QOibdicqciaU2Eo6vo7OOGYHpojg3lpdicb2mkPo2Zg0RFfPlOlibF58g/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/0RFmxdZEDROpVwic9Q0QtP9cvK4PhcWQiaQ3Gkta9R3lHy5B9DXUlI1mOfHt9uUEJtcZNlm3Np2mlLTy8VsThc3Q/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/0RFmxdZEDROpVwic9Q0QtP9cvK4PhcWQia8p6g8siaVj4HXRGtcocg1z8C0pbqwGZaLGTzPPU6u3XMHuZFRp0Vw1g/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/0RFmxdZEDROpVwic9Q0QtP9cvK4PhcWQiavicDUKExJoS0auqBHBBILdPJ3EYqbIzIyXIzUUxiaQ96NBoOA3gUKKdA/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/0RFmxdZEDROpVwic9Q0QtP9cvK4PhcWQia2EBlTHAXZ5tt0oyiaQzuaibxFxySBgrL1JyrwPH1JBCLOdKTM5T88Utg/640?wx_fmt=png&from=appmsg)

**第三部分：医疗数据保护策略（省略）**

![](https://mmbiz.qpic.cn/mmbiz_png/0RFmxdZEDROpVwic9Q0QtP9cvK4PhcWQiaU1iafagcLwsRFecLEZcn8lfV7ChwVEHZ1PGHLJ9BKx8UK2Xa7hgxkWg/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/0RFmxdZEDROpVwic9Q0QtP9cvK4PhcWQia1m56abTfAZm6EebafhGtrvyyWYoExbtqRZxSjSuXcfVP3Jv6vGwAsg/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/0RFmxdZEDROpVwic9Q0QtP9cvK4PhcWQiaL1XkfGgGR7P5ZGLIQywcTT5BEKuricFC0DEx1E1NPnsYViarOJnv7Hxg/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/0RFmxdZEDROpVwic9Q0QtP9cvK4PhcWQiaDM5EuCmgunibpZoou1f7VBP7ibibIGsx0OrBNzDhNjgIWYTibuzF0uNtibA/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/0RFmxdZEDROpVwic9Q0QtP9cvK4PhcWQiaxjAVcMvKP2uFmnkc4PsExMQETQ8fEBQ9Tb3eyjTTjrbzbu02TCPLGg/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/0RFmxdZEDROpVwic9Q0QtP9cvK4PhcWQiaiaW7xznyPKY09vOnJAlmjBRs2VKN8VzW4DCxkF46d9ibeYBpialgwEDMw/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/0RFmxdZEDROpVwic9Q0QtP9cvK4PhcWQiaYIu3B1sLuWvK6RajEwzBu97nEkNjcFFfIo3d7CQeqw9pwQRn6ib3QUA/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/0RFmxdZEDROpVwic9Q0QtP9cvK4PhcWQiafBtfR3GiavPG7F3WHEr1cMtRu6P4SBIVH2WDeDrw6rmkppTv1Fw2aTg/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/0RFmxdZEDROpVwic9Q0QtP9cvK4PhcWQiav3OiaYHVZ4tAvSia2KoibCwnIDrWsUTxJyWwoMr2Cu1Q02ialSudBNpN4g/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/0RFmxdZEDROpVwic9Q0QtP9cvK4PhcWQiax7ENUlT0vDEWVPlERzVs9bKetialicpJmLmDGU27yNmDibRUH7oIWdkNQ/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/0RFmxdZEDROpVwic9Q0QtP9cvK4PhcWQiat7NCpBcHibokSwIQSmtjs1ibRxMGl5KWoFpmM1rjC4kHJGCMxaQZE9vQ/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/0RFmxdZEDROpVwic9Q0QtP9cvK4PhcWQiazTlVBovXpGYCYwL4yaLoDHpeicAAaFic9tjUPFRdjibE3YJ2pJSibjvsSg/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/0RFmxdZEDROpVwic9Q0QtP9cvK4PhcWQiaGee0bicMRquSKkbMoCAer6VGZbYMaPVyibA5uibD023ohBvibzk9Z5SicMA/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/0RFmxdZEDROpVwic9Q0QtP9cvK4PhcWQiarZ1oNb5n4wY0kpE4baHnXmaRHNONib6g9BC9FoqHoBW2zibIYNvtVvyw/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/0RFmxdZEDROpVwic9Q0QtP9cvK4PhcWQiaFCKib24svIcGibTXJV77IxhkbDzfibkwficSn2DichAYlPgvMibmaMb2Zh4Q/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/0RFmxdZEDROpVwic9Q0QtP9cvK4PhcWQiaZgJM9jl6gibtu9mk0J6RudAvVoJIFcsP2BCSgcHstnsjAJTaxbzSZRA/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/0RFm...