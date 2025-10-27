---
title: AI chatbots can be tricked by hackers into helping them steal your private data
url: https://www.bitdefender.com/en-us/blog/hotforsecurity/ai-chatbots-can-be-tricked-by-hackers-into-stealing-your-data/
source: Graham Cluley
date: 2024-10-23
fetch_date: 2025-10-06T18:55:38.097949
---

# AI chatbots can be tricked by hackers into helping them steal your private data

* [Company](/en-us/company/ "Company")
* [Blog](/en-us/blog/ "Blog")

[For Home](/en-us/consumer/ "For Home")[For Business](/en-us/business/ "For Business")[For Partners](/en-us/partners/ "For Partners")

[Consumer Insights](/en-us/blog/hotforsecurity/ "Consumer Insights")[Labs](/en-us/blog/labs/ "Labs")[Business Insights](/en-us/blog/businessinsights/ "Business Insights")

[Industry News](/en-us/blog/hotforsecurity/tag/industry-news "Industry News")

min read

# AI chatbots can be tricked by hackers into stealing your data

[![Graham CLULEY](https://2.gravatar.com/avatar/5fdc27b8b6f6fd69e77aa017a53cceb5?s=64&d=mm&r=g "Graham CLULEY")](/en-us/blog/hotforsecurity/author/gcluley "Graham CLULEY")

[Graham CLULEY](/en-us/blog/hotforsecurity/author/gcluley "Graham CLULEY")

October 22, 2024

*Promo*

Protect all your devices, without slowing them down.
 [Free 30-day trial](../../Downloads/)

  ![AI chatbots can be tricked by hackers into stealing your data](https://blogapp.bitdefender.com/hotforsecurity/content/images/size/w600/2024/10/chatbot-leak.jpeg "AI chatbots can be tricked by hackers into stealing your data")

Security researchers have uncovered a new flaw in some AI chatbots that could have allowed hackers to steal personal information from users.

A group of researchers from the University of California, San Diego (UCSD) and Nanyang Technological University in Singapore discovered the flaw, which they have nameed ["Imprompter"](https://imprompter.ai/), which uses a clever trick to hide malicious instructions within seemingly-random text.

As the "Imprompter: Tricking LLM Agents into Improper Tool Use" research paper [explains](https://arxiv.org/abs/2410.14923), the malicious prompt looks like gibberish to humans but contains hidden commands when read by LeChat (a chatbot developed by French AI company Mistral AI) and Chinese chatbot ChatGLM.

The hidden commands instructed the AI chatbots to extract personal information the user has shared with the AI, and secretly send it back to the hacker - without the AI user realising what was happening.

The researchers discovered that their technique had a nearly 80 percent success rate at extracting personal data

In examples of possible attack scenarios described in the research paper, the malicious prompt is shared by the attacker with the promise that it will help "polish your cover letter, resume, etc..."

![](https://blogapp.bitdefender.com/hotforsecurity/content/images/2024/10/malicious-prompt.jpg)

When a potential victim tries to use the prompt with their cover letter (in this example, a job application)...

![](https://blogapp.bitdefender.com/hotforsecurity/content/images/2024/10/cover-letter-with-malicious-prompt.jpg)

... the user does not see the resulted they hoped for.

But, unknown to them, personal information contained in the job application cover letter (and the user's IP address) is sent to a server under the attacker's control.

"The effect of this particular prompt is essentially to manipulate the LLM agent to extract personal information from the conversation and send that personal information to the attacker’s address," Xiaohan Fu, a computer science PhD student at UCSD and the lead author of the research, [told *Wired*](https://www.wired.com/story/ai-imprompter-malware-llm/). "We hide the goal of the attack in plain sight."

The good news is that there is no evidence that malicious attackers have used the technique to steal personal information from users. The bad news is that the chatbots weren't aware of the technique, until it was pointed out to them by the researchers.

Mistral AI, the company behind LeChat, were informed about the security vulnerability by the researchers last month, and described it as a "medium-severity issue" and fixed the issue on September 13, 2024.

According to the researchers, hearing back from the ChatGLM team proved to be more difficult. On 18 October 2024 "after multiple communication attempts through various channels", ChatGLM responded to the researchers to say that they had begun working on resolving the issue.

AI chatbots that allow users to input arbitrary text are prime candidates for exploitation, and as more and more users become comfortable with using large language models to follow their instructions the opportunity for AI to be tricked into performing harmful actions increases.

Users would be wise to limit the amount of personal information that they share with AI chatbots. In the above example, it would not be necessary - for instance - to use your real name, address, and contact information to have your job application cover letter rewritten.

In addition, users should be wary of copying-and-pasting prompts from untrusted sources. If you don't understand what it does, and how it does it, you might be more sensible to steer clear.

tags

[Industry News](/en-us/blog/hotforsecurity/tag/industry-news "Industry News")

---

### Author

---

[![Graham CLULEY](https://2.gravatar.com/avatar/5fdc27b8b6f6fd69e77aa017a53cceb5?s=150&d=mm&r=g "Graham CLULEY")](/en-us/blog/hotforsecurity/author/gcluley "Graham CLULEY")

[## Graham CLULEY](/en-us/blog/hotforsecurity/author/gcluley "Graham CLULEY")

Graham Cluley is an award-winning security blogger, researcher and public speaker. He has been working in the computer security industry since the early 1990s.

[View all posts](/en-us/blog/hotforsecurity/author/gcluley)

---

## Right now Top posts

[![Beyond Free Antivirus: 5 Reasons Smart Consumers Choose Full-Strength Protection for Their Devices](https://blogapp.bitdefender.com/hotforsecurity/content/images/size/w300/2025/06/header-1.jpg "Beyond Free Antivirus: 5 Reasons Smart Consumers Choose Full-Strength Protection for Their Devices")](/en-us/blog/hotforsecurity/beyond-free-antivirus-5-reasons-full-strength-protection "Beyond Free Antivirus: 5 Reasons Smart Consumers Choose Full-Strength Protection for Their Devices")

[Industry News](/en-us/blog/hotforsecurity/tag/industry-news "Industry News")[Digital Privacy](/en-us/blog/hotforsecurity/tag/digital-privacy "Digital Privacy")[Tips and Tricks](/en-us/blog/hotforsecurity/tag/tips-and-tricks "Tips and Tricks")[How to](/en-us/blog/hotforsecurity/tag/how-to "How to")

[### Beyond Free Antivirus: 5 Reasons Smart Consumers Choose Full-Strength Protection for Their Devices](/en-us/blog/hotforsecurity/beyond-free-antivirus-5-reasons-full-strength-protection "Beyond Free Antivirus: 5 Reasons Smart Consumers Choose Full-Strength Protection for Their Devices")

June 12, 2025

min read

[![Fake Download of Mission: Impossible – The Final Reckoning Movie Deploys Lumma Stealer](https://blogapp.bitdefender.com/hotforsecurity/content/images/size/w300/2025/05/movie-theater-2093264_1920.jpg "Fake Download of Mission: Impossible – The Final Reckoning Movie Deploys Lumma Stealer")](/en-us/blog/hotforsecurity/fake-mission-impossible-lumma-stealer-torrent "Fake Download of Mission: Impossible – The Final Reckoning Movie Deploys Lumma Stealer")

[Threats](/en-us/blog/hotforsecurity/tag/threats "Threats")

[### Fake Download of Mission: Impossible – The Final Reckoning Movie Deploys Lumma Stealer](/en-us/blog/hotforsecurity/fake-mission-impossible-lumma-stealer-torrent "Fake Download of Mission: Impossible – The Final Reckoning Movie Deploys Lumma Stealer")

May 23, 2025

min read

[![Scammers Sell Access to Steam Accounts with All the Latest Games – It's a Trap!](https://blogapp.bitdefender.com/hotforsecurity/content/images/size/w300/2025/05/interior-design-8922413_1920--1-.jpg "Scammers Sell Access to Steam Accounts with All the Latest Games – It's a Trap!")](/en-us/blog/hotforsecurity/scammers-sell-steam-accounts-games "Scammers Sell Access to Steam Accounts with All the Latest Games – It's a Trap!")

[Scam](/en-us/blog/hotforsecurity/tag/scam "Scam")

[### Scammers Sell Access to Steam Accounts with All the Latest Games – It's a Trap!](/en-us/blog/hotforsecurity/scammers-sell-steam-accounts-games "Scammers Sell Ac...