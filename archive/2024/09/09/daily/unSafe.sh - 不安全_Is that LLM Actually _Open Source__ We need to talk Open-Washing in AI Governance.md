---
title: Is that LLM Actually "Open Source"? We need to talk Open-Washing in AI Governance
url: https://buaq.net/go-260828.html
source: unSafe.sh - 不安全
date: 2024-09-09
fetch_date: 2025-10-06T18:20:06.696907
---

# Is that LLM Actually "Open Source"? We need to talk Open-Washing in AI Governance

* [unSafe.sh - 不安全](https://unsafe.sh)
* [我的收藏](/user/collects)
* [今日热榜](/?hot=true)
* [公众号文章](/?gzh=true)
* [导航](/nav/index)
* [Github CVE](/cve)
* [Github Tools](/tools)
* [编码/解码](/encode)
* [文件传输](/share/index)
* [Twitter Bot](https://twitter.com/buaqbot)
* [Telegram Bot](https://t.me/aqinfo)
* [Search](/search/search)

[Rss](/rss.xml)

[ ]
黑夜模式

![](https://8aqnet.cdn.bcebos.com/ba915776d4f9547729d7b8f4e5f4ace6.jpg)

Is that LLM Actually "Open Source"? We need to talk Open-Washing in AI Governance

Figure demonstrating how quantitative openness judgments can be turned into actionable metrics by as
*2024-9-8 23:0:15
Author: [hackernoon.com(查看原文)](/jump-260828.htm)
阅读量:7
收藏*

---

Figure demonstrating how quantitative openness judgments can be turned into actionable metrics by assigning weights to specific features to create a gradient of evaluation.

### **What You’ll Learn**

In this blog, we dive deep into the complexities of AI openness, focusing on how [Open Source](https://opensource.org/?ref=hackernoon.com) principles apply—or fail to apply—to Large Language Models (LLMs) like BloomZ and Llama 2. By the end of this article, you’ll understand the historical context of Open Source licensing, the current challenges in defining "openness" in AI, and the phenomenon of "open-washing", which is misleading consumers and developers alike. We also introduce a comprehensive evaluation framework that integrates the [Open Source AI Definition (OSAID)](https://discuss.opensource.org/t/draft-v-0-0-9-of-the-open-source-ai-definition-is-available-for-comments/513?ref=hackernoon.com) with complementary insights from other frameworks to help you make more informed decisions about AI models. Finally, we’ll conclude with actionable best practices to develop the composite judgment to quantitatively measure transparency for any “Open Source” large language model.

It’s also helpful to explore alternatives that complement widely accepted definitions. As we will discuss, some perspectives—including recent analyses—suggest that frameworks like the **Open Source AI Definition (OSAID)** benefit from additional dimensions, particularly in how they address issues like data transparency. The [Model Openness Framework](https://arxiv.org/abs/2403.13784?ref=hackernoon.com) and its roots in Open Science principles offer a complementary perspective that may serve as an additional guidepost for evaluating AI openness. We are still in the earliest days of regulatory compliance in this space.

### **Why This Matters**

The world of AI is complex and rapidly evolving, often pushing open-source principles to their limits. Understanding these nuances is vital for developers, researchers, and consumers who want to ensure that AI systems are not only innovative but also transparent, ethical, and accountable. With the rise of "open-washing"—where AI models are falsely marketed as open source—it’s more important than ever to have a robust framework for evaluating these claims. By being equipped with this knowledge, you can make informed decisions that align with the true values of openness and transparency in AI development.

### **The Historical Context of Open Source Licensing**

To understand where we’re going, it’s essential to know where we’ve been. The [Open Source movement](https://en.wikipedia.org/wiki/Open_source?ref=hackernoon.com) was born out of a rebellion against the growing dominance of proprietary software in the 1980s when the [Free Software Foundation (FSF)](https://www.fsf.org/?ref=hackernoon.com) and introduced the GNU General Public License (GPL). This license was a game-changer, guaranteeing users the freedom to use, modify, and share software—essentially putting power back into the hands of developers and users.

Fast forward to the late 1990s, and the [Open Source Initiative (OSI)](https://opensource.org/?ref=hackernoon.com) was established to promote and protect Open Source software by certifying licenses that complied with the Open Source Definition (OSD). The OSD laid down the law for what could and couldn’t be called "open source," ensuring that the term wasn’t watered down or misused.

### **The Example of Large Language Models (LLMs) and the Limits to "Openness"**

Enter the world of AI, where the lines between open and closed systems become even blurrier. Large Language Models (LLMs), such as GPT-3 or its successors, serve as prime examples of how "open source" can be a deceptive term in the AI landscape. LLMs are sophisticated AI systems trained on massive datasets to generate human-like text. These models have sparked significant interest and investment due to their ability to perform a wide range of tasks, from translation to creative writing. However, despite the impressive capabilities of these models, the concept of "openness" often falls short when examined closely.

In the research paper *[“Rethinking Open Source Generative AI: Open-Washing and the EU AI Act,](https://www.mpi.nl/publications/item3588217/rethinking-open-source-generative-ai-open-washing-and-eu-ai-act?ref=hackernoon.com)”* In their analysis, researchers Dr. Liesenfeld and his team compare BloomZ and Llama 2, two prominent LLMs, as examples of varying degrees of openness in AI. This comparison offers a practical demonstration of how to apply an openness matrix to generative AI models:

![Comparison of BloomZ and Llama 2 on 14 dimensions of openness, illustrating framework. ](https://hackernoon.imgix.net/images/RHANbxrXjsYoxIMTyKJFleCFJyC3-h8034ue.jpeg?auto=format&fit=max&w=3840)

#### **BloomZ: A Case Study in True Openness**

[BloomZ](https://huggingface.co/bigscience/bloomz?ref=hackernoon.com) represents a model that genuinely embraces the principles of open source, setting a high standard for transparency and accessibility in AI.

* **Availability**: BloomZ makes the source code for training, fine-tuning, and running the model available, representing a high degree of openness. The LLM data used to train BloomZ is extensively documented, making it transparent about its data sources and processes. Both the base model weights and the instruction-tuned version are openly available, allowing for replication and scrutiny by the broader community.
* **Documentation**: The BloomZ project is well-documented, with detailed descriptions available in multiple scientific papers and an active [GitHub repository](https://github.com/bigscience-workshop?ref=hackernoon.com). The data curation and fine-tuning processes are comprehensively covered, providing insights into the model’s architecture, training data, and responsible use. Peer-reviewed papers further support its transparency, including an estimation of the carbon footprint, which is rarely documented in AI projects.
* **Access and Licensing**: BloomZ is distributed through the Petals API, and its source code is released under the [Apache 2.0 license](https://www.apache.org/licenses/LICENSE-2.0?ref=hackernoon.com), an OSI-approved license. The model weights are covered under the Responsible AI License (RAIL), which imposes restrictions to prevent harmful use, adding a layer of ethical responsibility.

#### **[Llama 2](https://llama.meta.com/llama2/?ref=hackernoon.com): The Pitfalls of Open-Washing**

In stark contrast, Llama 2 exemplifies the concept of "open-washing," where the label of open-source is applied without fully meeting the principles of openness.

* **Availability**: In stark contrast, Llama 2 does not make its source code available. Only the scripts for running the model are shared, and the LLM data is vaguely described, with limited details provided in a corporate preprint. Access to the base model weights is restricted, requiring a consent form, and the data used for instruction tuning remains undisclosed, further limiting transparency.
* **Documentation**: The documentation for Llama 2 is minimal, with the source code itself not being open. The architecture is described in less detail, scattered across corporate websites a...