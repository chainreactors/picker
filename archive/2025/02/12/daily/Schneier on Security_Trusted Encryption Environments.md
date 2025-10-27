---
title: Trusted Encryption Environments
url: https://www.schneier.com/blog/archives/2025/02/trusted-encryption-environments.html
source: Schneier on Security
date: 2025-02-12
fetch_date: 2025-10-06T20:40:11.285685
---

# Trusted Encryption Environments

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

## Trusted Execution Environments

Really good—and detailed—[survey](https://dl.acm.org/doi/pdf/10.1145/3634737.3644993) of Trusted Execution Environments (TEEs.)

Tags: [academic papers](https://www.schneier.com/tag/academic-papers/), [encryption](https://www.schneier.com/tag/encryption/)

[Posted on February 11, 2025 at 7:08 AM](https://www.schneier.com/blog/archives/2025/02/trusted-encryption-environments.html) •
[5 Comments](https://www.schneier.com/blog/archives/2025/02/trusted-encryption-environments.html#comments)

### Comments

Rene Bastien •
[February 11, 2025 10:56 AM](https://www.schneier.com/blog/archives/2025/02/trusted-encryption-environments.html/#comment-442943)

Bruce, there is a type. It should be Trusted Execution Environment.

Who? •
[February 11, 2025 11:04 AM](https://www.schneier.com/blog/archives/2025/02/trusted-encryption-environments.html/#comment-442944)

Not sure in other TEEs, but at least Intel® Software Guard Extensions™ (SGX) has fixed some of the vulnerabilities described in this article in the last years by means of firmware upgrades.

It would be great if current operating systems start using these TEEs; even if these enclaves are far from being perfect, they are another layer in a security model. Right now we have limited support for VM memory encryption, but no way to use SGX to —we say— store OpenSSH encryption keys. Only Linux has some sort of support for SGX, but up to my knowledge it is not enabled by default.

Who? •
[February 11, 2025 11:06 AM](https://www.schneier.com/blog/archives/2025/02/trusted-encryption-environments.html/#comment-442945)

@ Rene Bastien

Agreed, I guess Bruce has worked too much on encryption. 😉

Who? •
[February 11, 2025 11:12 AM](https://www.schneier.com/blog/archives/2025/02/trusted-encryption-environments.html/#comment-442946)

Markus Friedl has done a great work supporting SGX as a FIDO-style authenticator; however, being an OpenBSD developer, his work is available only on Linux. It is sad not having support for SGX in OpenBSD.

Me •
[February 11, 2025 12:09 PM](https://www.schneier.com/blog/archives/2025/02/trusted-encryption-environments.html/#comment-442948)

@Rene Bastien

Not sure if your typo is intentional or not…

[![Atom Feed](https://www.schneier.com/wp-content/themes/schneier/assets/images/rss.png)
Subscribe to comments on this entry](https://www.schneier.com/blog/archives/2025/02/trusted-encryption-environments.html/feed/)

## Leave a comment [Cancel reply](/blog/archives/2025/02/trusted-encryption-environments.html#respond)

[Blog moderation policy](https://www.schneier.com/blog/archives/2024/06/new-blog-moderation-policy.html)

[Login](https://www.schneier.com/wp-login.php?redirect_to=https%3A%2F%2Fwww.schneier.com%2Fblog%2Farchives%2F2025%2F02%2Ftrusted-encryption-environments.html "Login")

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

[← Pairwise Authentication of Humans](https://www.schneier.com/blog/archives/2025/02/pairwise-authentication-of-humans.html) [Delivering Malware Through Abandoned Amazon S3 Buckets →](https://www.schneier.com/blog/archives/2025/02/delivering-malware-through-abandoned-amazon-s3-buckets.html)

Sidebar photo of Bruce Schneier by Joe MacInnis.

[Powered by WordPress](https://wordpress.com/wp/?partner_domain=www.schneier.com&utm_source=Automattic&utm_medium=colophon&utm_campaign=Concierge%20Referral&utm_term=www.schneier.com) [Hosted by Pressable](https://pressable.com/?utm_source=Automattic&utm_medium=rpc&utm_campaign=Concierge%20Referral&utm_term=concierge)

### About Bruce Schneier

![](https://www.schneier.com/wp-content/uploads/2019/10/Bruce-Schneier.jpg)

I am a [public-interest technologist](https://public-interest-tech.com/), working at the intersection of security, technology, and people. I've been writing about security issues on my [blog](/) since 2004, and in my monthly [newsletter](/crypto-gram/) since 1998. I'm a fellow and lecturer at Harvard's [Kennedy School](https://www.hks.harvard.edu/faculty/bruce-schneier), a board member of [EFF](https://www.eff.org/), and the Chief of Security Architecture at [Inrupt, Inc.](https://inrupt.com/) This personal website expresses the opinions of none of those organizations.

### Related Entries

* [Digital Threat Modeling Under Authoritarianism](https://www.schneier.com/blog/archives/2025/09/digital-threat-modeling-under-authoritarianism.html)
* [Time-of-Check Time-of-Use Attacks Against LLMs](https://www.schneier.com/blog/archives/2025/09/time-of-check-time-of-use-attacks-against-llms.html)
* [Assessing the Quality of Dried Squid](https://www.schneier.com/blog/archives/2025/09/assessing-the-quality-of-dried-squid.html)
* [New Cryptanalysis of the Fiat-Shamir Protocol](https://www.schneier.com/blog/archives/2025/09/new-cryptanalysis-of-the-fiat-shamir-protocol.html)
* [Friday Squid Blogging: The Origin and Propagation of Squid](https://www.schneier.com/blog/archives/2025/09/friday-squid-blogging-the-origin-and-propagation-of-squid.html)
* [GPT-4o-mini Falls for Psychological Manipulation](https://www.schneier.com/blog/archives/2025/09/gpt-4o-mini-falls-for-psychological-manipulation.html)

### Featured Essays

* [The Value of Encryption](https://www.schneier.com/essays/archives/2016/04/the_value_of_encrypt.html)
* [Data Is a Toxic Asset, So Why Not Throw It Out?](https://www.schneier.com/essays/archives/2016/03/data_is_a_toxic_asse.html)
* [How the NSA Threatens National Security](https://www.schneier.com/essays/archives/2014/01/how_the_nsa_threaten.html)
* [Terrorists May Use Google Earth, But Fear Is No Reason to Ban It](https://www.schneier.com/essays/archives/2009/01/terrorists_may_use_g.html)
* [In Praise of Security Theater](https://www.schneier.com/essays/archives/2007/01/in_praise_of_securit.html)
* [Refuse to be Terrorized](https://www.schneier.com/essays/archives/2006/08/refuse_to_be_terrori.html)
* [The Eternal Value of Privacy](https://www.schneier.com/essays/archives/2006/05/the_eternal_value_of.html)
* [Terrorists Don't Do Movie Plots](https://www.schneier.com/essays/archives/2005/09/terrorists_dont_do_m.html)

[More Essays](https://www.schneier.com/essays/)

### Blog Archives

* [Archive by Month](https://www.schneier.com/blog/calendar.html/)
* [100 Latest Comments](https://www.schneier.com/blog/newcomments.html/)

#### Blog Tags

* [3d printers](https://www.schneier.com/tag/3d-printers/)
* [9/11](https://www.schneier.com/tag/9-11/)
* [A Hacker's Mind](https://www.schneier.com/tag/a-hackers-mind/)
* [Aaron Swartz](https://www.schne...