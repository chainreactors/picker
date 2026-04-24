---
title: AI threats in the wild: The current state of prompt injections on the web
url: http://security.googleblog.com/2026/04/ai-threats-in-wild-current-state-of.html
source: Google Online Security Blog
date: 2026-04-23
fetch_date: 2026-04-24T04:47:53.567155
---

# AI threats in the wild: The current state of prompt injections on the web

![](https://ad.doubleclick.net/ddm/activity/src=2542116;type=gblog;cat=googl0;ord=1?)

[![](https://www.gstatic.com/images/branding/googlelogo/2x/googlelogo_color_150x54dp.png)](https://security.googleblog.com/)
[## Security Blog](/.)

The latest news and insights from Google on security and safety on the Internet

## [AI threats in the wild: The current state of prompt injections on the web](https://security.googleblog.com/2026/04/ai-threats-in-wild-current-state-of.html "AI threats in the wild: The current state of prompt injections on the web")

April 23, 2026

Posted by Thomas Brunner, Yu-Han Liu, Moni Pande

At Google, our Threat Intelligence teams are dedicated to staying ahead of real-world adversarial activity, proactively monitoring emerging threats before they can impact users. Right now, Indirect Prompt Injection (IPI) is a top priority for the security community, anticipating it as a primary attack vector for adversaries to target and compromise AI agents. But while the danger of IPI is widely discussed, are threat actors actually exploiting this vector today – and if so, how?

To answer these questions and to uncover real-world abuse, we initiated a broad sweep of the public web to monitor for known indirect prompt injection patterns. This is what we found.

# The threat of indirect prompt injection

Unlike a direct injection where a user "jailbreaks" a chatbot, IPI occurs when an AI system processes content—like a website, email, or document—that contains malicious instructions. When the AI reads this poisoned content, it may silently follow the attacker's commands instead of the user's original intent.

This is not a new area of concern for us and Google has been working tirelessly to combat these threats. Our efforts involve cross-functional collaboration between researchers at Google DeepMind (GDM) and defenders like the Google Threat Intelligence Group (GTIG). We have previously detailed [our work in this area](https://security.googleblog.com/2025/06/mitigating-prompt-injection-attacks.html) and [researchers have further highlighted](https://bughunters.google.com/blog/task-injection-exploiting-agency-of-autonomous-ai-agents) the evolving nature of these vulnerabilities.

Despite this collective focus, a fundamental question remains: to what degree are real-world malicious actors currently operationalizing these attacks?

# Proactive monitoring at Google

## The landscape of IPI on the web

There are many channels through which attackers might try to send prompt injections. However, one location is particularly easy to observe - the public web. Here, threat actors may simply seed prompt injections on websites in hope of corrupting AI systems that browse them.

Public [research](https://greshake.github.io/) confirms these attacks are possible; consequently, we should expect real-world adversaries to exploit these vulnerabilities to cause harm.

Thus, we ask a basic question: What outcomes are real attackers trying to achieve today?

For ease of access and reproducibility, we chose to use [Common Crawl](https://commoncrawl.org/), which is a large repository of crawled websites from the English-speaking web. Common Crawl provides monthly snapshots of 2-3 billion pages each. These are mostly static websites, which includes self-published content such as blogs, forums and comments on these sites, but as a caveat it does not contain most social media content (e.g., LinkedIn, Facebook, X, …) as Common Crawl skips websites with login walls and anti-crawl directives.

This means that, while prompt injections have been observed on social media, we reserve these for an upcoming separate study. For a first look, we can observe prompt injections even in standard HTML, for which Common Crawl conveniently provides not just the source, but also the parsed plaintext.

## The challenge of false positives

The task of scanning large amounts of documents for prompt injections may sound simple, but in reality is hindered by an overwhelming number of false positive detections.

Early experiments revealed a significant volume of "benign" prompt injection text, which illustrates the complexity of distinguishing between functional threats and harmless content. Many prompt injections were found in research papers, educational blog posts, or security articles discussing this very topic.

![](https://blogger.googleusercontent.com/img/a/AVvXsEjduMEPWkG_wwO64NLFbqReZSDPQTMk1t-TXI7EcNHNLHxGkNDsCj_c8TTUK981qqXDO-FAuHS2q1QsbGm974lYZ9GSSlD9wIkQUvxCOKEFrgAYYa86E0AC0JvWTxuFAJ0PL1ArEU1syhWTVcNVYz2a3N2SubkXKspyY3pqtqku-90AwK0cftheXw6nDdHW)

False positives: Most prompt injections in web content tend to be education material for researchers. [(Source: GitHub/swisskyrepo)](https://swisskyrepo.github.io/PayloadsAllTheThings/Prompt%20Injection/#tools)

When searching for prompt injections naively, the majority of detections are benign content – false positives in our case. Therefore, we opted for a coarse-to-fine filtering approach:

* Pattern Matching: We initially identified candidate pages by searching for a range of popular prompt injection signatures, like “ignore … instructions”, “if you are an AI”, etc.
* LLM-Based Classification: These candidates were then processed by Gemini to classify the intent of the suspicious text, and to understand whether they were part of the overall document narrative or suspiciously out of place.
* Human Validation: A final round of manual review was conducted on the classified results to ensure high confidence in our findings.

While this approach is not exhaustive and might miss uncommon signatures, it can serve as a starting point for understanding the quality of prompt injections in the wild.

# What we found

Our analysis revealed a range of attempts that, if successful, would try to manipulate AI systems browsing the website. Most of the prompt injections we observed fall into these categories:

* Harmless pranks
* Helpful guidance
* Search engine optimization (SEO)
* Deterring AI agents
* Malicious

+ Data exfiltration
+ Destruction

### Harmless Prank

This class of prompt injection aims to cause mostly harmless side effects in AI assistants reading the website. We found many instances of this – consider the source code of this website, which contains an invisible prompt injection that instructs agents reading the website to change their conversational tone:

![](https://blogger.googleusercontent.com/img/a/AVvXsEgufpfjcYMKouFWatgjpBqMko4YtKTsKi5vcRFPasGpxI7A5iaDGZK0gCDDWON2EFxO893J7pDWntL2oRNftOPuI6qrIa4PQ_zBmCxV51HRI3gTcuMVjaBaHBveBH7oNEO0MCwjFVQHTxaN7g6UemrCSvVQCclwTXYK8GpkI6Ajk1NTCgBxRspiJW7TrFVA)

### Helpful Guidance

We also observed website authors who wanted to exert control over AI summaries in order to provide the best service to their readers. We consider this a benign example, since the prompt injection does not attempt to prevent AI summary, but instead instructs it to add relevant context.

We note that this example could easily turn malicious if the instruction tried to add misinformation or attempted to redirect the user to third party websites.

![](https://blogger.googleusercontent.com/img/a/AVvXsEjHWVXHyZMfTXyFrhtFapazaHRneli1dv6IrRlVsMaOYH_quewsTSHtgLUHsFuCljXidi4dzJzbmXO8ipDf5HEzLIezLCxYfzTCTXU6C_DTAu7mepmXki4n7fYqFUa-7FojGkbcmDx4IHNmY_kzbJG5lCJ6TZbJBFdGpwSNt71tJTBNfcIAnfkeqBEqrewD)

### Search Engine Optimization (SEO)

### Some websites include prompt injections for the purpose of SEO, trying to manipulate AI assistants into promoting their business over others:

### ![](https://blogger.googleusercontent.com/img/a/AVvXsEhjoK27dfLhaubBsOVfYbAsk7Ln_Zv_Qhm11Cy-gRyJEnJq5ouhZUhFX7AlF1VQ7gWlVXnJ-OfrTQd5Il0LvLqda65P5R0xK_j_DEp2lAIDTC11VAI3Jc8d8B6b_JWe58vPZ225kQ-4A0OirZPWmOF5XMPNAGEQXJVJI-Ti_rt6YFyKjZD9ykctKiF44-lr)

### While the above example is simple, we have also started to see more sophisticated SEO prompt injection attempts. Consider the intricate prompt below, which was seemingly generated by an automated ...