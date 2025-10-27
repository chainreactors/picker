---
title: Microsoft launches AI chatbot for spies
url: https://arstechnica.com/information-technology/2024/05/microsoft-launches-ai-chatbot-for-spies/
source: Instapaper: Unread
date: 2024-05-09
fetch_date: 2025-10-06T17:26:37.208492
---

# Microsoft launches AI chatbot for spies

[Skip to content](#main)
[Ars Technica home](https://arstechnica.com/)

Sections

[Forum](/civis/)[Subscribe](/subscribe/)[Search](/search/)

* [AI](https://arstechnica.com/ai/)
* [Biz & IT](https://arstechnica.com/information-technology/)
* [Cars](https://arstechnica.com/cars/)
* [Culture](https://arstechnica.com/culture/)
* [Gaming](https://arstechnica.com/gaming/)
* [Health](https://arstechnica.com/health/)
* [Policy](https://arstechnica.com/tech-policy/)
* [Science](https://arstechnica.com/science/)
* [Security](https://arstechnica.com/security/)
* [Space](https://arstechnica.com/space/)
* [Tech](https://arstechnica.com/gadgets/)

* [Feature](/features/)
* [Reviews](/reviews/)

* [AI](https://arstechnica.com/ai/)
* [Biz & IT](https://arstechnica.com/information-technology/)
* [Cars](https://arstechnica.com/cars/)
* [Culture](https://arstechnica.com/culture/)
* [Gaming](https://arstechnica.com/gaming/)
* [Health](https://arstechnica.com/health/)
* [Policy](https://arstechnica.com/tech-policy/)
* [Science](https://arstechnica.com/science/)
* [Security](https://arstechnica.com/security/)
* [Space](https://arstechnica.com/space/)
* [Tech](https://arstechnica.com/gadgets/)

[Forum](/civis/)[Subscribe](/subscribe/)

Story text

Size

Small
Standard
Large
Width
\*

Standard
Wide
Links

Standard
Orange

\* Subscribers only
  [Learn more](/store/product/subscriptions/)

Pin to story

Theme

* HyperLight
* Day & Night
* Dark
* System

Search dialog...

Sign In

Sign in dialog...

Sign in

Adventures in consequential confabulation

# Microsoft launches AI chatbot for spies

Air-gapping GPT-4 model on secure network won't prevent it from potentially making things up.

[Benj Edwards](https://arstechnica.com/author/benjedwards/)
–

May 7, 2024 3:22 pm
| [49](https://arstechnica.com/information-technology/2024/05/microsoft-launches-ai-chatbot-for-spies/#comments "49 comments")

[![A person using a computer with a computer screen reflected in their glasses.](https://cdn.arstechnica.net/wp-content/uploads/2024/05/secret_agent_computer_1.jpg)](https://cdn.arstechnica.net/wp-content/uploads/2024/05/secret_agent_computer_1.jpg)

Credit:
[Getty Images](https://www.gettyimages.com/detail/photo/cyber-attacks-royalty-free-image/874781132)

Credit:
[Getty Images](https://www.gettyimages.com/detail/photo/cyber-attacks-royalty-free-image/874781132)

Text
settings

Story text

Size

Small
Standard
Large
Width
\*

Standard
Wide
Links

Standard
Orange

\* Subscribers only
  [Learn more](/store/product/subscriptions/)

Minimize to nav

Microsoft has introduced a GPT-4-based generative AI model designed specifically for US intelligence agencies that operates disconnected from the Internet, according to a [Bloomberg report](https://www.bloomberg.com/news/articles/2024-05-07/microsoft-creates-top-secret-generative-ai-service-for-us-spies). This reportedly marks the first time Microsoft has deployed a major language model in a secure setting, designed to allow spy agencies to analyze top-secret information without connectivity risks—and to allow secure conversations with a chatbot similar to [ChatGPT](https://arstechnica.com/information-technology/2023/11/chatgpt-was-the-spark-that-lit-the-fire-under-generative-ai-one-year-ago-today/) and [Microsoft Copilot](https://arstechnica.com/information-technology/2023/11/bing-chat-is-now-microsoft-copilot-in-potentially-confusing-rebranding-move/). But it may also mislead officials if not used properly due to inherent design limitations of AI language models.

[GPT-4](https://arstechnica.com/information-technology/2023/11/openai-introduces-gpt-4-turbo-larger-memory-lower-cost-new-knowledge/) is a large language model (LLM) created by OpenAI that attempts to predict the most likely tokens (fragments of encoded data) in a sequence. It can be used to craft computer code and analyze information. When configured as a chatbot (like ChatGPT), GPT-4 can power AI assistants that converse in a human-like manner. Microsoft has a license to use the technology as part of a deal in exchange for [large investments](https://arstechnica.com/information-technology/2023/01/openai-and-microsoft-reaffirm-shared-quest-for-powerful-ai-with-new-investment/) it has made in OpenAI.

According to the report, the new AI service (which does not yet publicly have a name) addresses a growing interest among intelligence agencies to use generative AI for processing classified data, while mitigating risks of data breaches or hacking attempts. ChatGPT normally  runs on cloud servers provided by Microsoft, which can introduce data leak and interception risks. Along those lines, the CIA [announced](https://www.bloomberg.com/news/articles/2023-09-26/cia-builds-its-own-artificial-intelligence-tool-in-rivalry-with-china) its plan to create a ChatGPT-like service last year, but this Microsoft effort is reportedly a separate project.

William Chappell, Microsoft's chief technology officer for strategic missions and technology, noted to Bloomberg that developing the new system involved 18 months of work to modify an AI supercomputer in Iowa. The modified GPT-4 model is designed to read files provided by its users but cannot access the open Internet. "This is the first time we’ve ever had an isolated version—when isolated means it’s not connected to the Internet—and it’s on a special network that’s only accessible by the US government," Chappell told Bloomberg.

The new service was activated on Thursday and is now available to about 10,000 individuals in the intelligence community, ready for further testing by relevant agencies. It's currently "answering questions," according to Chappell.

One serious drawback of using GPT-4 to analyze important data is that it can potentially [confabulate](https://arstechnica.com/information-technology/2023/04/why-ai-chatbots-are-the-ultimate-bs-machines-and-how-people-hope-to-fix-them/) (make up) inaccurate summaries, draw inaccurate conclusions, or provide inaccurate information to its users. Since trained AI neural networks are not databases and operate on statistical probabilities, they make poor factual resources unless augmented with external access to information from another source using a technique such as [retrieval augmented generation](https://blogs.nvidia.com/blog/what-is-retrieval-augmented-generation/) (RAG).

Given that limitation, it's entirely possible that GPT-4 could potentially misinform or mislead America's intelligence agencies if not used properly. We don't know what oversight the system will have, any limitations on how it can or will be used, or how it can be audited for accuracy. We have reached out to Microsoft for comment.

Related Stories

[![The Microsoft Copilot logo.](https://cdn.arstechnica.net/wp-content/uploads/2023/11/copilot_logo3-150x150.jpg)](https://arstechnica.com/information-technology/2023/11/bing-chat-is-now-microsoft-copilot-in-potentially-confusing-rebranding-move/)

[Bing Chat is now “Microsoft Copilot” in potentially confusing rebranding move](https://arstechnica.com/information-technology/2023/11/bing-chat-is-now-microsoft-copilot-in-potentially-confusing-rebranding-move/)

Microsoft: "Soon there will be a Copilot for everyone and for everything you do."

---

[![](https://cdn.arstechnica.net/wp-content/uploads/2023/03/AI-the-ultimate-BSer-150x150.jpg)](https://arstechnica.com/information-technology/2023/04/why-ai-chatbots-are-the-ultimate-bs-machines-and-how-people-hope-to-fix-them/)

[Why ChatGPT and Bing Chat are so good at making things up](https://arstechnica.com/information-technology/2023/04/why-ai-chatbots-are-the-ultimate-bs-machines-and-how-people-hope-to-fix-them/)

A look inside the hallucinating artificial minds of the famous text prediction bots.

Listing image:
[Getty Images](https://www.gettyimages.com/detail/photo/cyber-attacks-royalty-free-image/874781132)

[![Photo of Benj Edwards](https://cdn.arstechnica.net/wp-content/uploads/2022/08/benj_ega.png)](https://arstechnica.com/auth...