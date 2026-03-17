---
title: Possible New Result in Quantum Factorization
url: https://www.schneier.com/blog/archives/2026/03/possible-new-result-in-quantum-factorization.html
source: Schneier on Security
date: 2026-03-16
fetch_date: 2026-03-17T04:17:08.709748
---

# Possible New Result in Quantum Factorization

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

## Possible New Result in Quantum Factorization

I’m skeptical about—and not qualified to review—this [new result](https://www.preprints.org/manuscript/202510.1649) in factorization with a quantum computer, but if it’s true it’s a [theoretical improvement](https://www.securityweek.com/quantum-decryption-of-rsa-is-much-closer-than-expected/) in the speed of factoring large numbers with a quantum computer.

Tags: [academic papers](https://www.schneier.com/tag/academic-papers/), [cryptanalysis](https://www.schneier.com/tag/cryptanalysis/), [quantum computing](https://www.schneier.com/tag/quantum-computing/), [RSA](https://www.schneier.com/tag/rsa/)

[Posted on March 16, 2026 at 5:46 AM](https://www.schneier.com/blog/archives/2026/03/possible-new-result-in-quantum-factorization.html) •
[4 Comments](https://www.schneier.com/blog/archives/2026/03/possible-new-result-in-quantum-factorization.html#comments)

### Comments

[Luca Mariot](https://lucamariot.org) •
[March 16, 2026 5:55 AM](https://www.schneier.com/blog/archives/2026/03/possible-new-result-in-quantum-factorization.html/#comment-452905)

Definitely not an improvement; see Aaronson’s blog post: <https://scottaaronson.blog/?p=9615>

Spencer •
[March 16, 2026 6:10 AM](https://www.schneier.com/blog/archives/2026/03/possible-new-result-in-quantum-factorization.html/#comment-452906)

I was also going to post the aaronson link. The summary is that their algorithm relies on an exponential classical computation. So it works on small numbers but can’t scale (the largest composite tested in the paper is 1363).

bro256 •
[March 16, 2026 10:53 AM](https://www.schneier.com/blog/archives/2026/03/possible-new-result-in-quantum-factorization.html/#comment-452907)

People often celebrate new “improvements” in integer factorization, but it’s important to keep perspective.

Even with decades of research and better algorithms, progress *without cheating* is extremely slow. As a simple reminder about factoring 21:

So while papers may claim optimizations or theoretical advances, the practical reality is that factoring numbers with quantum computers remains incredibly difficult.

Clive Robinson •
[March 16, 2026 1:54 PM](https://www.schneier.com/blog/archives/2026/03/possible-new-result-in-quantum-factorization.html/#comment-452909)

@ ALL,

The question at the back of some minds can be answered by,

“Woof… Woof, woof.”

As I noted a few days back as this story surfaced caution should be applied to it…

As with all quantum algorithms, you need to see three things,

1, The size of the “circuit”
2, The “generality” of the solution
3, There is not a faster “classical” non quantum algorithm available.

As I understand it this is about making the classical non quantum part of the algorithm faster, but only for smallish numbers.

[![Atom Feed](https://www.schneier.com/wp-content/themes/schneier/assets/images/rss.png)
Subscribe to comments on this entry](https://www.schneier.com/blog/archives/2026/03/possible-new-result-in-quantum-factorization.html/feed/)

## Leave a comment [Cancel reply](/blog/archives/2026/03/possible-new-result-in-quantum-factorization.html#respond)

[Blog moderation policy](https://www.schneier.com/blog/archives/2024/06/new-blog-moderation-policy.html)

[Login](https://www.schneier.com/wp-login.php?redirect_to=https%3A%2F%2Fwww.schneier.com%2Fblog%2Farchives%2F2026%2F03%2Fpossible-new-result-in-quantum-factorization.html "Login")

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

[← Upcoming Speaking Engagements](https://www.schneier.com/blog/archives/2026/03/upcoming-speaking-engagements-54.html)

Sidebar photo of Bruce Schneier by Joe MacInnis.

[Powered by WordPress](https://wordpress.com/wp/?partner_domain=www.schneier.com&utm_source=Automattic&utm_medium=colophon&utm_campaign=Concierge%20Referral&utm_term=www.schneier.com) [Hosted by Pressable](https://pressable.com/?utm_source=Automattic&utm_medium=rpc&utm_campaign=Concierge%20Referral&utm_term=concierge)

### About Bruce Schneier

![](https://www.schneier.com/wp-content/uploads/2019/10/Bruce-Schneier.jpg)

I am a [public-interest technologist](https://public-interest-tech.com/), working at the intersection of security, technology, and people. I've been writing about security issues on my [blog](/) since 2004, and in my monthly [newsletter](/crypto-gram/) since 1998. I'm a fellow and lecturer at Harvard's [Kennedy School](https://www.hks.harvard.edu/faculty/bruce-schneier), a board member of [EFF](https://www.eff.org/), and the Chief of Security Architecture at [Inrupt, Inc.](https://inrupt.com/) This personal website expresses the opinions of none of those organizations.

### Related Entries

* [New Attack Against Wi-Fi](https://www.schneier.com/blog/archives/2026/03/new-attack-against-wi-fi.html)
* [LLM-Assisted Deanonymization](https://www.schneier.com/blog/archives/2026/03/llm-assisted-deanonymization.html)
* [Side-Channel Attacks Against LLMs](https://www.schneier.com/blog/archives/2026/02/side-channel-attacks-against-llms.html)
* [Prompt Injection Via Road Signs](https://www.schneier.com/blog/archives/2026/02/prompt-injection-via-road-signs.html)
* [Corrupting LLMs Through Weird Generalizations](https://www.schneier.com/blog/archives/2026/01/corrupting-llms-through-weird-generalizations.html)

### Featured Essays

* [Four Ways AI Is Being Used to Strengthen Democracies Worldwide](https://www.schneier.com/essays/archives/2025/11/four-ways-ai-is-being-used-to-strengthen-democracies-worldwide.html)
* [The CrowdStrike Outage and Market-Driven Brittleness](https://www.schneier.com/essays/archives/2024/07/the-crowdstrike-outage-and-market-driven-brittleness.html)
* [How Online Privacy Is Like Fishing](https://www.schneier.com/essays/archives/2024/06/how-online-privacy-is-like-fishing.html)
* [How AI Will Change Democracy](https://www.schneier.com/essays/archives/2024/05/how-ai-will-change-democracy.html)
* [Seeing Like a Data Structure](https://www.schneier.com/essays/archives/2024/05/seeing-like-a-data-structure.html)
* [LLMs’ Data-Control Path Insecurity](https://www.schneier.com/essays/archives/2024/05/llms-data-control-path-insecurity.html)
* [AI and Trust](https://www.schneier.com/essays/archives/2023/12/ai-and-trust.html)
* [The Value of Encryption](https://www.schneier.com/essays/archives/2016/04/the_value_of_encrypt.html)
* [The Eternal Value of Privacy](https://www.schneier.com/essays/archives/2006/05/the_eternal_value_of.html)
* [Terrorists Don't Do Movie Plots](https://www.schneier.com/essays/archives...