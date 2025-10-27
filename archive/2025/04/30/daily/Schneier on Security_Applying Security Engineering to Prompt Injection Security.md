---
title: Applying Security Engineering to Prompt Injection Security
url: https://www.schneier.com/blog/archives/2025/04/applying-security-engineering-to-prompt-injection-security.html
source: Schneier on Security
date: 2025-04-30
fetch_date: 2025-10-06T22:07:08.483550
---

# Applying Security Engineering to Prompt Injection Security

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

## Applying Security Engineering to Prompt Injection Security

This seems like an [important advance](https://arstechnica.com/information-technology/2025/04/researchers-claim-breakthrough-in-fight-against-ais-frustrating-security-hole/) in LLM security against prompt injection:

> Google DeepMind has [unveiled CaMeL](https://arxiv.org/abs/2503.18813) (CApabilities for MachinE Learning), a new approach to stopping prompt-injection attacks that abandons the failed strategy of having AI models police themselves. Instead, CaMeL treats language models as fundamentally untrusted components within a secure software framework, creating clear boundaries between user commands and potentially malicious content.
>
> […]
>
> To understand CaMeL, you need to understand that prompt injections happen when AI systems can’t distinguish between legitimate user commands and malicious instructions hidden in content they’re processing.
>
> […]
>
> While CaMeL does use multiple AI models (a privileged LLM and a quarantined LLM), what makes it innovative isn’t reducing the number of models but fundamentally changing the security architecture. Rather than expecting AI to detect attacks, CaMeL implements established security engineering principles like capability-based access control and data flow tracking to create boundaries that remain effective even if an AI component is compromised.

Research [paper](https://arxiv.org/abs/2503.18813). Good [analysis](https://simonwillison.net/2025/Apr/11/camel/) by Simon Willison.

I wrote about the problem of LLMs intermingling the data and control paths [here](https://cacm.acm.org/opinion/llms-data-control-path-insecurity/).

Tags: [academic papers](https://www.schneier.com/tag/academic-papers/), [AI](https://www.schneier.com/tag/ai/), [Google](https://www.schneier.com/tag/google/), [LLM](https://www.schneier.com/tag/llm/), [security engineering](https://www.schneier.com/tag/security-engineering/)

[Posted on April 29, 2025 at 7:03 AM](https://www.schneier.com/blog/archives/2025/04/applying-security-engineering-to-prompt-injection-security.html) •
[2 Comments](https://www.schneier.com/blog/archives/2025/04/applying-security-engineering-to-prompt-injection-security.html#comments)

### Comments

Clive Robinson •
[April 29, 2025 11:06 AM](https://www.schneier.com/blog/archives/2025/04/applying-security-engineering-to-prompt-injection-security.html/#comment-444891)

@ Bruce, ALL,

The quote from the article you give says,

> *“Instead, CaMeL treats language models as fundamentally untrusted components within a secure software framework, creating clear boundaries between user commands and potentially malicious content.”*

That has been the “standard security model” for more than a couple of thousand years because,

“Simple parts do not give security, you have to build security with them”

It’s why I point out “secure messaging apps are not secure systems”, you have to assess the security of all the parts involved.

Scrx •
[April 29, 2025 5:11 PM](https://www.schneier.com/blog/archives/2025/04/applying-security-engineering-to-prompt-injection-security.html/#comment-444896)

Everything old is new again. Mixing up data and control was just what the Cap’n Crunch whistle did – back in the days of POTS. Those who don’t remember, &c. S.

[![Atom Feed](https://www.schneier.com/wp-content/themes/schneier/assets/images/rss.png)
Subscribe to comments on this entry](https://www.schneier.com/blog/archives/2025/04/applying-security-engineering-to-prompt-injection-security.html/feed/)

## Leave a comment [Cancel reply](/blog/archives/2025/04/applying-security-engineering-to-prompt-injection-security.html#respond)

[Blog moderation policy](https://www.schneier.com/blog/archives/2024/06/new-blog-moderation-policy.html)

[Login](https://www.schneier.com/wp-login.php?redirect_to=https%3A%2F%2Fwww.schneier.com%2Fblog%2Farchives%2F2025%2F04%2Fapplying-security-engineering-to-prompt-injection-security.html "Login")

Name

Email

URL:

[ ]  Remember personal info?

Fill in the blank: the name of this blog is Schneier on \_\_\_\_\_\_\_\_\_\_\_ (required):

Comments:
![](https://www.schneier.com/wp-content/themes/schneier/assets/images/loader.gif)

**Allowed HTML**
<a href="URL"> • <em> <cite> <i> • <strong> <b> • <sub> <sup> • <ul> <ol> <li> • <blockquote> <pre>
**Markdown Extra** syntax via <https://michelf.ca/projects/php-markdown/extra/>

Δ

[← Windscribe Acquitted on Charges of Not Collecting Users’ Data](https://www.schneier.com/blog/archives/2025/04/windscribe-acquitted-on-charges-of-not-collecting-users-data.html) [WhatsApp Case Against NSO Group Progressing →](https://www.schneier.com/blog/archives/2025/04/whatsapp-case-against-nso-group-progressing.html)

Sidebar photo of Bruce Schneier by Joe MacInnis.

[Powered by WordPress](https://wordpress.com/wp/?partner_domain=www.schneier.com&utm_source=Automattic&utm_medium=colophon&utm_campaign=Concierge%20Referral&utm_term=www.schneier.com) [Hosted by Pressable](https://pressable.com/?utm_source=Automattic&utm_medium=rpc&utm_campaign=Concierge%20Referral&utm_term=concierge)

### About Bruce Schneier

![](https://www.schneier.com/wp-content/uploads/2019/10/Bruce-Schneier.jpg)

I am a [public-interest technologist](https://public-interest-tech.com/), working at the intersection of security, technology, and people. I've been writing about security issues on my [blog](/) since 2004, and in my monthly [newsletter](/crypto-gram/) since 1998. I'm a fellow and lecturer at Harvard's [Kennedy School](https://www.hks.harvard.edu/faculty/bruce-schneier), a board member of [EFF](https://www.eff.org/), and the Chief of Security Architecture at [Inrupt, Inc.](https://inrupt.com/) This personal website expresses the opinions of none of those organizations.

### Related Entries

* [AI in the 2026 Midterm Elections](https://www.schneier.com/blog/archives/2025/10/ai-in-the-2026-midterm-elections.html)
* [Daniel Miessler on the AI Attack/Defense Balance](https://www.schneier.com/blog/archives/2025/10/daniel-miessler-on-the-ai-attack-defense-balance.html)
* [Use of Generative AI in Scams](https://www.schneier.com/blog/archives/2025/10/use-of-generative-ai-in-scams.html)
* [Abusing Notion's AI Agent for Data Theft](https://www.schneier.com/blog/archives/2025/09/abusing-notions-ai-agent-for-data-theft.html)
* [Time-of-Check Time-of-Use Attacks Against LLMs](https://www.schneier.com/blog/archives/2025/09/time-of-check-time-of-use-attacks-against-llms.html)
* [Assessing the Quality of Dried Squid](https://www.schneier.com/blog/archives/2025/09/assessing-the-quality-of-dried-squid.html)

### Featured Essays

* [The Value of Encryption](https://www.schneier.com/essays/archives/2016/04/the_value_of_encrypt.html)
* [Data Is a Toxic Asset, So Why Not Throw It Out?](https://www.schneier.com/essays/archives/2016/03/data_is_a_toxic_asse.html)
* [How the NSA Threatens National Security...