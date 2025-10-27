---
title: AI Agent应用攻击面漫谈
url: https://vipread.com/library/topic/4008
source: 信息安全知识库
date: 2025-08-16
fetch_date: 2025-10-07T00:12:38.922488
---

# AI Agent应用攻击面漫谈

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

##### [主页](/) / [第16期“安全范儿”技术沙龙「LLM安全漏洞挖掘」专场](/library/cid/456) / AI Agent应用攻击面漫谈

![](https://archive1.vipread.com/covers/2025/08/topic/19704_1755223435_babbdfdf.jpg)

* 标题

  [AI Agent应用攻击面漫谈](/library/topic/4008)
* 作者

  黎轲（郁离歌、）@字节跳动
* 标签

  [LLM](/library/tags/LLM)
  [智能体](/library/tags/%E6%99%BA%E8%83%BD%E4%BD%93)
  [MCP](/library/tags/MCP)
  [攻击面](/library/tags/%E6%94%BB%E5%87%BB%E9%9D%A2)
  [沙盒](/library/tags/%E6%B2%99%E7%9B%92)
* 简介

  该报告深入探讨了AI Agent应用面临的攻击面。首先，报告概述了AI Agent的定义、决策流程（感知、规划、行动）和关键特性（自主性、适应性等），并介绍了其在客服、办公助手等领域的广泛应用。其核心技术架构由大型语言模型（Model）、代理运行时（Agent Runtime）、功能工具（Tools）以及底层支持服务（Supporting Services）构成。

  报告的核心部分详细剖析了AI Agent各组件的潜在安全风险。
  1. **大型语言模型（LLMs）**：主要面临提示词注入攻击，攻击者可通过直接或间接方式注入恶意指令，从而操控Agent执行非预期的操作，如窃取数据或执行恶意代码。报告强调，不仅用户输入不可信，模型生成的内容同样需要被视为不可信来源。
  2. **消息传输**：以WebSocket为例，若缺乏正确的安全配置（如Origin校验），易遭受跨站WebSocket劫持（CSWSH），导致聊天数据被窃取。
  3. **输入与输出处理**：对模型生成内容的处理不当会引发严重漏洞。例如，直接执行模型生成的代码可能导致远程代码执行（RCE），而将模型输出渲染为HTML则可能造成跨站脚本（XSS）攻击。
  4. **工具（Tools）**：作为Agent与外部世界交互的桥梁，工具是风险最集中的区域。数据分析功能可能导致代码执行，网页访问功能可能引发服务端请求伪造（SSRF），数据库操作则可能存在SQL注入风险。
  5. **沙盒环境**：用于执行代码的沙盒若配置不当，如网络或文件系统隔离存在缺陷，攻击者可能实现沙盒逃逸，进一步危害宿主系统。

  最后，报告对未来防御方向进行了展望，提出了三大关键策略：遵循**最小权限原则**限制Agent能力；通过**动态监控**实时追踪并拦截Agent的异常意图与行为；以及将**传统应用安全与大模型安全相结合**，构建纵深防御体系。
* 援引

  https://mp.weixin.qq.com/s/u8vIFU\_TXIrXJ1EZOPBB4g
* 提示

  本站仅做资料的整理和索引,转载引用请注明出处

###### 相关推荐

* [![](https://archive1.vipread.com/covers/2025/08/thumbnails/small/topic_19688_1755611621_5adc2489.webp)](/library/topic/4017)

  [【西湖论剑gcsis.cn](/library/topic/4017)

  2025-08-19 13:56:02.151091
* [![](//cdn.cdnjson.com/tvax3.sinaimg.cn/large/006vnxPsly1gec6uvo5l1j314q0nfq7v.jpg)](/library/topic/2800)

  [从RSAC创新沙盒看中美网](/library/topic/2800)

  2020-04-22 11:14:12
* [![](https://archive1.vipread.com/covers/2025/08/thumbnails/small/topic_19704_1755223438_babbdfdf.webp)](/library/topic/4008)

  [AI Agent应用攻击面](/library/topic/4008)

  2025-08-15 02:05:44.011328
* [![](https://archive1.vipread.com/covers/2025/08/thumbnails/small/topic_2_1754463893_70785fa1.webp)](/library/topic/3994)

  [大型语言模型 (LLM)](/library/topic/3994)

  2025-08-06 07:04:48.434567

[![](https://archive1.vipread.com/images/ad/flag_3.gif)](https://www.flagify.com/?ref=https://vipread.com)

###### 附件下载

* ![](/static/images/icons/file-pdf.svg)

  ###### AI Agent应用攻击面漫谈-黎轲-img.pdf

  时间:  2025-08-15T02:03:15Z

  大小:
  2.52 M

  下载:  25

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