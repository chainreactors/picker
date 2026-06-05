---
title: Hacking Meta’s AI Chatbot
url: https://www.schneier.com/blog/archives/2026/06/hacking-metas-ai-chatbot.html
source: Schneier on Security
date: 2026-06-04
fetch_date: 2026-06-05T06:14:17.130120
---

# Hacking Meta’s AI Chatbot

# [Schneier on Security](https://www.schneier.com/)

Menu

* [Blog](https://www.schneier.com)
* [Newsletter](https://www.schneier.com/crypto-gram/)
* [Books](https://www.schneier.com/books/)
* [Essays](https://www.schneier.com/essays/)
* [News](https://www.schneier.com/news/)
* [Talks](https://www.schneier.com/talks/)
* [Academic](https://www.schneier.com/academic/)
* [About Me](https://www.schneier.com/blog/about/)

### Search

*Powered by [DuckDuckGo](https://duckduckgo.com/)*

Blog

Essays

Whole site

### Subscribe

[![Atom](https://www.schneier.com/wp-content/uploads/2019/10/rss-32px.png)](https://www.schneier.com/feed/atom/)[![Facebook](https://www.schneier.com/wp-content/uploads/2019/10/facebook-32px.png)](https://www.facebook.com/bruce.schneier)[![Twitter](https://www.schneier.com/wp-content/uploads/2019/10/twitter-32px.png)](https://twitter.com/schneierblog)[![Email](https://www.schneier.com/wp-content/uploads/2019/10/email-32px.png)](https://www.schneier.com/crypto-gram)

[Home](https://www.schneier.com)[Blog](https://www.schneier.com/blog/archives/)

## Hacking Meta’s AI Chatbot

Hackers are [convincing](https://techcrunch.com/2026/06/01/hackers-hijacked-instagram-accounts-by-tricking-meta-ai-support-chatbot-into-granting-access/) Meta’s AI support chatbot to let them take over other peoples’ accounts:

> A [video](https://x.com/DarkWebInformer/status/2061253599758315527) posted on X showed the step-by-step process to hack someone’s Instagram account. The hacker allegedly used a VPN to spoof the targets’ presumed location to avoid triggering Instagram’s automated account protections. Then, the hacker opened a chat with Meta AI Support Assistant and asked the bot to add a new email address to the target’s account. The chatbot can be seen sending a verification code to the email address provided by the hacker; the hacker then shares the verification code with the chatbot, which prompts the chatbot to show a button to “Reset Password.” The hacker enters a new password and takes over the victim’s account.
>
> […]
>
> On Monday, Instagram spokesperson Andy Stone said in [a reply](https://x.com/andymstone/status/2061489833441145103) to Wong’s post and others that the issue was now fixed. It’s unclear how many Instagram users had their accounts improperly accessed.

It’s not that easy. Probably this particular tactic is now blocked. But there are others, many others, and they cannot be blocked as a class. The real problem is that LLM chatbots are not trustworthy enough for this application.

Another news [article](https://www.404media.co/hackers-simply-asked-meta-ai-to-give-them-access-to-high-profile-instagram-accounts-it-worked/).

Tags: [AI](https://www.schneier.com/tag/ai/), [chatbots](https://www.schneier.com/tag/chatbots/), [cybersecurity](https://www.schneier.com/tag/cybersecurity/), [hacking](https://www.schneier.com/tag/hacking/), [LLM](https://www.schneier.com/tag/llm/), [Meta](https://www.schneier.com/tag/meta/)

[Posted on June 4, 2026 at 7:04 AM](https://www.schneier.com/blog/archives/2026/06/hacking-metas-ai-chatbot.html) •
[5 Comments](https://www.schneier.com/blog/archives/2026/06/hacking-metas-ai-chatbot.html#comments)

### Comments

Clive Robinson •
[June 4, 2026 9:21 AM](https://www.schneier.com/blog/archives/2026/06/hacking-metas-ai-chatbot.html/#comment-454904)

@ Bruce, ALL,

**To err is human but to really FUp takes a computer**

Is an oldish expression that with DNN AI is getting a new lease of life.

As you note,

> “Hackers are convincing Meta’s AI support chatbot to let them take over other peoples’ accounts”

What works on humans, works on human mimics as well…

But for different reasons.

However you also note,

> “Probably this particular tactic is now blocked. But there are others, many others, and they cannot be blocked as a class. The real problem is that LLM chatbots are not trustworthy enough for this application.”

It’s not “trustworthy” that is the issue, as that is an “observer mistake” of assuming or ascribing false beliefs about a machine having “human traits” (anthropomorphization).

The real issue is a consequence of,

“But there are other [tactics], many others, and they cannot be blocked as a class.”

It’s not just one type of class it’s many classes depending on how you want to slice and dice the vulnerability attributes.

But more importantly as I’ve previously noted there is “proof” that such tactics can not be blocked.

Whilst some of the maths proof is fairly simple (a variation on the Cantor Diagonal Argument) it is easier to think it through logically.

Let’s assume you have a guardrail system to try to recognise / catch such tactics, to do so the guardrail system has to be as, if not more powerful, than the LLM as it has to be able to have not just seen the tactic before in one instantiation, it has to see all possible instantiations of the same tactic including those that are new.

Is that possible?

Well aside from the issue of there are not enough resources. There is the issue of even simple keyed obfuscation or encryption.

If the tactic instance is encrypted in some way, and the guardrail does not have the key but the LLM does, then it’s game over for the guardrail system.

KC •
[June 4, 2026 10:33 AM](https://www.schneier.com/blog/archives/2026/06/hacking-metas-ai-chatbot.html/#comment-454905)

When Meta [says](https://about.fb.com/news/2026/03/boosting-your-support-and-safety-on-metas-apps-with-ai/): *“We’re rigorously testing each of these AI systems, building in safeguards and evaluating their performance…”* It does feel like some of this rigorous testing is happening in real-time.

I don’t know what safeguards Meta is using, but I am checking out Nvidia’s [LLM guardrails library](https://docs.nvidia.com/nemo/guardrails/latest/configure-rails/guardrail-catalog/index.html).

Just for the sake of example, I’d pin this particular email / pw reset hack under the category of ‘LLM Self-Check’ which would determine if the user input should be allowed for further processing.

Are there input analysis libraries for these types of things?

anonymouse random •
[June 4, 2026 1:37 PM](https://www.schneier.com/blog/archives/2026/06/hacking-metas-ai-chatbot.html/#comment-454907)

Meta’s AI usage is absurd. First, the API that the chatbot uses to send the password-reset email should send it only to previously securely-set address(es). Second, the AI should not have direct access to the password-reset tokens, so that — even if it somehow works around the first safeguard — it would be unable to send a valid password-reset token by itself.

Did Meta use AI to design and code its password-reset feature?

lurker •
[June 4, 2026 2:31 PM](https://www.schneier.com/blog/archives/2026/06/hacking-metas-ai-chatbot.html/#comment-454909)

@anonymouse, ALL

This is just a demonstration that Meta has the form of an octopus without that animal’s brain. This is a class of attack that Meta invites by its very structure. Good luck with stopping it …

sh or tu rl . at / 6jm6s •
[June 4, 2026 6:40 PM](https://www.schneier.com/blog/archives/2026/06/hacking-metas-ai-chatbot.html/#comment-454917)

In Idaho, muslims and their friends in the Boise police department covered up an attempted murder and deliberately destroyed a law-abiding Christian Family.

Please help spread the truth – police corruption in Boise Idaho is through the roof – it’s gotta stop!

Read all about it here:

sh or tu rl . at / 6jm6s

[![Atom Feed](https://www.schneier.com/wp-content/themes/schneier/assets/images/rss.png)
Subscribe to comments on this entry](https://www.schneier.com/blog/archives/2026/06/hacking-metas-ai-chatbot.html/feed/)

## Leave a comment [Cancel reply](/blog/archives/2026/06/hacking-metas-ai-chatbot.html#respond)

[Blog moderation policy](https://www.schneier.com/blog/archives/2024/06/new-blog-moderation-policy.html)

[Login](https://www.schneier.com/wp-login.php?redirect_to=https%3A%2F%2Fwww.schneier.com%2Fblog%2Farchives%2F2026%2F...