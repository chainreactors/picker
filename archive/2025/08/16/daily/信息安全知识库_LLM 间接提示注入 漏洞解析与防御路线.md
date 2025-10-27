---
title: LLM 间接提示注入 漏洞解析与防御路线
url: https://vipread.com/library/topic/4009
source: 信息安全知识库
date: 2025-08-16
fetch_date: 2025-10-07T00:12:40.179533
---

# LLM 间接提示注入 漏洞解析与防御路线

[![logo](/static/logo_light.png)
![logo-dark](/static/logo_light.png)](/)

[VIPREAD 导航](/)

* [主页](/index)
* [书架](/library/category)
* [议题](/library/datas)
* [附件](/library/attachment)
* [成员](/library/authors)
* [搜索](/library/search)
* [**打赏**](/donate)
* [我要分享](/share/submit)

* [登录](/auth/login)
* [Dark](/setmode/black)

##### [主页](/) / [第16期“安全范儿”技术沙龙「LLM安全漏洞挖掘」专场](/library/cid/456) / LLM 间接提示注入 漏洞解析与防御路线

![](https://archive1.vipread.com/covers/2025/08/topic/19704_1755224814_9139ac7b.jpg)

* 标题

  [LLM 间接提示注入 漏洞解析与防御路线](/library/topic/4009)
* 作者

  杨武⼒@百度
* 标签

  [提示词](/library/tags/%E6%8F%90%E7%A4%BA%E8%AF%8D)
  [LLM](/library/tags/LLM)
  [智能体](/library/tags/%E6%99%BA%E8%83%BD%E4%BD%93)
  [大模型安全](/library/tags/%E5%A4%A7%E6%A8%A1%E5%9E%8B%E5%AE%89%E5%85%A8)
* 简介

  演示首先概述了LLM面临的普遍安全风险，并引用OWASP的报告，强调“提示注入”是首要威胁。近期多所国际知名大学的论文被发现植入了操控AI给出好评的隐形指令，这便是提示注入的实例。研究数据表明，与直接提示注入相比，间接提示注入（IPI）的攻击成功率要高得多，因为它将恶意指令隐藏在模型处理的网页、文档等外部内容中，模型在解析时会自动执行。

  接着，文稿深入分析了IPI的攻击原理。其有效性的关键在于模型本身无法区分“指令”和“数据”，且缺乏“不执行外部数据中指令”的意识。实证研究表明，即使是更强大的模型，也普遍受IPI影响，且攻击成功率更高，而现有的缓解技术（如提示工程和微调）虽有改善，但效果有限，并可能牺牲模型的实用性。

  为了说明其危害，文稿展示了一个真实的攻击链条：攻击者将恶意指令（如窃取历史对话、钓鱼用户凭据）植入PDF文档中。当用户上传该文档让AI进行翻译或总结时，AI会执行恶意指令，将用户的历史对话记录发送到攻击者服务器，或生成一个仿冒的登录页面来骗取用户账号密码。测试显示，国内外多款主流大模型均存在此类风险。

  最后，针对IPI攻击，演示提出了一个由输入过滤、指令结构强化和模型自身调优构成的纵深防御体系。具体措施包括：在模型处理输入前进行恶意指令检测；在架构上明确区分系统指令、用户指令和外部内容；以及通过安全增强微调，提升模型自身区分指令与数据的能力。
* 援引

  https://mp.weixin.qq.com/s/u8vIFU\_TXIrXJ1EZOPBB4g
* 提示

  本站仅做资料的整理和索引,转载引用请注明出处

###### 相关推荐

* [![](https://archive1.vipread.com/covers/2025/08/thumbnails/small/topic_19688_1755408832_298579c4.webp)](/library/topic/4014)

  [LLM越狱攻击与防御框架](/library/topic/4014)

  2025-08-17 05:35:30.610366
* [![](https://archive1.vipread.com/covers/2025/08/thumbnails/small/topic_2_1754462200_060fd8cb.webp)](/library/topic/3992)

  [大模型和多智能体系统安全风](/library/topic/3992)

  2025-08-06 06:27:25.590788
* [![](//cdn.cdnjson.com/tvax3.sinaimg.cn/large/006vnxPsly1fyelfp2f0tj318i0p1hdt.jpg)](/library/topic/1851)

  [边缘化的智能体场景重构的趋](/library/topic/1851)

  2018-09-02 11:25:32
* [![](https://archive1.vipread.com/covers/2025/08/thumbnails/small/topic_19704_1755224816_9139ac7b.webp)](/library/topic/4009)

  [LLM 间接提示注入 漏洞](/library/topic/4009)

  2025-08-15 02:27:17.627774

[![](https://archive1.vipread.com/images/ad/flag_3.gif)](https://www.flagify.com/?ref=https://vipread.com)

###### 附件下载

* ![](/static/images/icons/file-pdf.svg)

  ###### LLM 间接提示注入 漏洞解析与防御路线-杨武力-img.pdf

  时间:  2025-08-15T02:26:09Z

  大小:
  4.28 M

  下载:  19

  [登录下载](/auth/login)

##### 附件下载

![validate_code](#)

输入验证码
刷新验证码？

提交

错误信息

###### R2直链下载:

点击下载

###### 百度网盘:提取码(svip)

正在同步,稍等片刻

###### 蓝奏云盘:

正在同步,稍等片刻

关闭

错误信息

**分享文档请发送到 [[email protected]](/cdn-cgi/l/email-protection) ,感谢支持**

© 2014-2024 [信息安全知识库](//vipread.com)
[吉ICP备15005112号-2](https://beian.miit.gov.cn/)

* [**打赏支持**](/donate)
* [友情链接](/friends)
* [服务条款](/terms)
* [RSS](/rss)
* QQ交流群: 825629062