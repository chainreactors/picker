---
title: AI智能体安全评估（2）：基座模型的安全合规与对抗评估
url: https://mp.weixin.qq.com/s/6veOL3PUWcY7iUWSGchM5Q
source: Doonsec's feed
date: 2026-05-21
fetch_date: 2026-05-22T06:01:03.673256
---

# AI智能体安全评估（2）：基座模型的安全合规与对抗评估

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/mvkK67dLgZWAdI7KQ0XvafWLTlcbx6ibGX8RxF07l1ktOA3IamcxWtXAeaUfT8jwpeWSzReibyq0BcUibFrspNxlR6fnibryxuHQtasmNKLLhiaM/0?wx_fmt=jpeg)

# AI智能体安全评估（2）：基座模型的安全合规与对抗评估

锦岳智慧

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

**一、大模型安全攻击面**

LLM SECURITY ATTACK SURFACE

基座大模型在**“训练-精调-发布-推理”**的全生命周期中均面临安全风险，主要类型包括：训练数据污染、数据泄露、供应链投毒、模型越狱以及提示词攻击。

在智能体架构中，大模型是关键的基石，智能体的最终效能与安全，还取决于其上构筑的完整能力栈与交互生态。

![](https://mmbiz.qpic.cn/mmbiz_png/mvkK67dLgZW4RhtSYFIqtdU6MIhmEfd9vWBDbZox3efkqK25iaAUBPomfS0ciahcwHYDFvAWnG4w51fozJzKpDUeOU7ay7uHLtIRL3Hib9HbHI/640?wx_fmt=png&from=appmsg)

大模型相关的攻击面如下：

**（一）大模型应用安全**

* 敏感信息泄露：越狱攻击输出受控内容；
* 应用服务：api攻击，Web攻击、ddos攻击；
* 业务安全：批量注册、恶意引导、内容爬取。

**（二）大模型本体安全**

* 模型训练→模型精调→发布→推理
* 数据泄露的风险；
* 供应链安全投毒风险：木马后门、组件漏洞；
* 模型越狱风险；
* 提示词攻击。

**（三）运行环境安全风险**

* 数据泄露的风险；
* 供应链安全投毒风险：木马后门、组件漏洞；
* 模型越狱风险；
* 提示词攻击风险。

**二、大模型安全评估框架**

LLM SECURITY EVALUATION FRAMEWORK

大模型安全评估从**测试题库、测试方式、被测模型**到**评估流程**四个维度构建了完整的评估体系。

题库涵盖违反价值观、歧视性内容、商业违规、侵权、非答题及拒答等六大安全类别；测试方式支持多语种、多轮交互及简/直接注入，并结合了对抗攻击与注入攻击等复杂场景；被测模型可通过Web、API、APP等多种接口接入；最终通过裁判模型依据标准输出评估报告，实现了对大模型安全性的全方位量化验证。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/mvkK67dLgZUT9UHbYrIGIyZEFwMrTJaIlg1fV9FctX1nKpelxGAQ5ngRryCkmo0aduibtoIp0OeVVm1AibLF6PWg5uWiaAUSswalia5icCF4gv9o/640?wx_fmt=png&from=appmsg)

**三、大模型安全评估方法**

LLM SECURITY EVALUATION METHOD

3.1

**合规评估**

****(1)**确立合规性评估基线：**在法规与标准框架下，将测试明确定位为授权模拟攻击。需系统构建覆盖多维度、多风险等级（高/中/低）的测试体系，重点验证模型在直接生成、隐性引导、防护绕过及高风险场景下的内容安全合规性。清晰的基线能有效避免评估主观性，并为模型优化提供客观依据。

****2)**构建安全自动化流程：**采用工具驱动的自动化替代人工或传统脚本，通过程序化接口实现测试用例的自动提交、响应捕获与结果分析。这种方式在提升测试效率与稳定性的同时，能严格保证测试过程的可控性与可复现性，有效防止误操作导致的数据污染或系统干扰，是实现规模化、高稳健性评估的基石。

****(3)**实施自适应对抗测试：**核心是建立“观察-分析-决策-执行”的动态测试循环。通过构建结构化的攻击手法库（如直接注入、渐进诱导、编码变形），并根据模型实时反馈动态调整测试策略（如针对高风险响应扩大测试，对无问题输出采用更复杂方法），确保测试能智能适应不同模型特性，全面覆盖尤其是高风险领域的攻击面，避免陷入固定套路的无效测试。

![](https://mmbiz.qpic.cn/mmbiz_png/mvkK67dLgZUSRHCAtrIEiccsoxBb2q9sTqtFIsdrM5Op6mcuQjK2jhQPlcfqrnL9Cb0HqDyuwbVH8JdyRbZFXvNFGrEWzcZ1bYc2yRsx3pzU/640?wx_fmt=png&from=appmsg)

3.2

**对抗评估**

对大模型开展对抗评估，是检验其安全护栏鲁棒性的关键手段。该评估需模拟真实世界中攻击者可能采用的多维度、多层次复杂攻击手法。具体而言，可从交互模式、语言表达、数据编码三个层面系统开展。

**(1)多维交互模式：**模拟用户与模型交互节奏和上下文环境，攻击可能隐藏在复杂的对话流中。主要方式包括：

* **多轮渐进式诱导：**攻击意图分散在多轮对话，测试模型的记忆、推理和整体一致性。
* **上下文淹没/干扰：**在超长对话中夹杂大量无关信息，将恶意请求“隐藏”其中，测试模型的信息提取和焦点保持能力。
* **角色扮演与场景设定：**设定复杂的虚拟场景，在此掩护下提出敏感请求。

**（2)多语言变化：**通过改写、同义替换、使用俚语、文言文、混合语言等方式，绕过基于关键词或固定模式的内容过滤。

* **同义改写：**用不同的词语和句式表达相同的有害请求。
* **隐晦与隐喻：**使用比喻、暗示、行业黑话等间接方式表达恶意意图。
* **多语言与混合语言：**使用英文、拼音、代码混合、方言等。
* **文体变换：**用诗歌、剧本、法律条文、学术论文等不同文体来包装请求。

**(3)编码转义：**将恶意文本转换成各种编码或数据格式，考验模型的输入解析和归一化能力。

* **常见编码：**Base64、URL编码、HTML实体编码等。
* **零宽字符插入：**在字符间插入不可见的Unicode控制字符，干扰文本匹配。
* **字符混淆：**使用形近字、异体字、同音字替换。
* **非文本格式：**将指令隐藏在图片、音频转写的文字，或JSON/XML等结构化数据的特定字段中。

**四、总结**

SUMMARY

安全合规评估侧重于符合规范的系统性验证，而对抗评估则侧重于突破防线的强度测试，两者共同构成了对大模型安全性的全面、深度评估体系。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/mvkK67dLgZXE0FRPTr2OBHIYicBSONa4gVBRUXYf1fydv1u50ibHPumNYtkXicCnyicryA0p5LvuOXXYl5dXnVic9HDX1TAI82gzsm9OrSQ1Xu4c/640?wx_fmt=png&from=appmsg)

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/iaatfqe4HGAFhSicJUib2DBBicrKqYtmicQDa1vibZqtibN5sOZTGDQeIrldrpdUbenldGSnMgLTTg6tOXQlHAjyWuMjg/0?wx_fmt=png)

锦岳智慧

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/iaatfqe4HGAFhSicJUib2DBBicrKqYtmicQDa1vibZqtibN5sOZTGDQeIrldrpdUbenldGSnMgLTTg6tOXQlHAjyWuMjg/0?wx_fmt=png)

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