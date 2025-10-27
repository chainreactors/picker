---
title: Cloudflare Reports that Almost 7% of All Internet Traffic Is Malicious
url: https://www.schneier.com/blog/archives/2024/07/cloudflare-reports-that-almost-7-of-all-internet-traffic-is-malicious.html
source: Schneier on Security
date: 2024-07-18
fetch_date: 2025-10-06T17:52:10.412534
---

# Cloudflare Reports that Almost 7% of All Internet Traffic Is Malicious

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

## Cloudflare Reports that Almost 7% of All Internet Traffic Is Malicious

[6.8%](https://blog.cloudflare.com/application-security-report-2024-update), to be precise.

From [ZDNet](https://www.zdnet.com/article/cloudflare-reports-almost-7-percent-of-internet-traffic-is-malicious/):

> However, [Distributed Denial of Service (DDoS)](https://www.zdnet.com/article/what-is-a-ddos-attack-everything-you-need-to-know-about-ddos-attacks-and-how-to-protect-against-them/) attacks continue to be cybercriminals’ weapon of choice, making up over 37% of all mitigated traffic. The scale of these attacks is staggering. In the first quarter of 2024 alone, Cloudflare blocked 4.5 million unique DDoS attacks. That total is nearly a third of all the DDoS attacks they mitigated the previous year.
>
> But it’s not just about the sheer volume of DDoS attacks. The sophistication of these attacks is increasing, too. Last August, [Cloudflare mitigated a massive HTTP/2 Rapid Reset DDoS attack that peaked at 201 million requests per second (RPS).](https://www.zdnet.com/article/google-cloud-aws-and-cloudflare-report-largest-ddos-attacks-ever/) That number is three times bigger than any previously observed attack.
>
> It wasn’t just Cloudflare that was hit by the largest DDoS attack in its history. Google Cloud reported the same attack peaked at an astonishing 398 million RPS. So, how big is that number? According to Google, Google Cloud was slammed by more RPS in two minutes than Wikipedia saw traffic during September 2023.

Tags: [cybercrime](https://www.schneier.com/tag/cybercrime/), [denial of service](https://www.schneier.com/tag/denial-of-service/), [Internet](https://www.schneier.com/tag/internet/)

[Posted on July 17, 2024 at 12:03 PM](https://www.schneier.com/blog/archives/2024/07/cloudflare-reports-that-almost-7-of-all-internet-traffic-is-malicious.html) •
[26 Comments](https://www.schneier.com/blog/archives/2024/07/cloudflare-reports-that-almost-7-of-all-internet-traffic-is-malicious.html#comments)

### Comments

Peter A. •
[July 17, 2024 12:40 PM](https://www.schneier.com/blog/archives/2024/07/cloudflare-reports-that-almost-7-of-all-internet-traffic-is-malicious.html/#comment-439373)

That is likely true. Attacks are running constantly, against all IP addresses. Not only DDoSes, all the exploitation scripts are banging in.

Quite a time ago, I was installing a fresh PC. First burned a new install CD on a known good box. Then booted the new PC with no network, installed a rather minimal system, hardened it a little, disabled and uninstalled unneeded stuff, configured what was needed to be configured, including quite strict firewall rules and logging.

The moment I brought the network interface up and the virgin box got the first IP address in its electronic life (on a dial-up link!), firewall logs started to fill with alerts. I was shocked.

Today it is much worse. On my servers, I have moved essential public-facing services to non-standard ports; not to achieve security by obscurity, but to save disk space consumed by log lines reporting bogus connections, requests, and authentication attempts. It helped for about half a year only, bots already have learned that my few addresses are different. I need to reconfigure everything again and see for how long it helps.

Jodie Rich •
[July 17, 2024 1:06 PM](https://www.schneier.com/blog/archives/2024/07/cloudflare-reports-that-almost-7-of-all-internet-traffic-is-malicious.html/#comment-439374)

I don’t trust them to judge this. For example, try running “torify wget -S <https://www.ietf.org/rfc/rfc7258.txt>“. Cloudflare (as seen from the “Server:” header) blocks that request, presumably assuming malice. There was also a several-month period when I couldn’t access the IETF site at all via Tor Browser (along with many other sites, including Cloudflare’s blog and Stack Exchange). Ironic and disappointing given the content of that RFC and the IETF’s occasionally-proclaimed support for anonymity.

[Ryan](https://snarfed.org/) •
[July 17, 2024 2:40 PM](https://www.schneier.com/blog/archives/2024/07/cloudflare-reports-that-almost-7-of-all-internet-traffic-is-malicious.html/#comment-439375)

Wait, there are two different reports linked here, CrowdStrike’s and Cloudflare’s?

Morley •
[July 17, 2024 4:48 PM](https://www.schneier.com/blog/archives/2024/07/cloudflare-reports-that-almost-7-of-all-internet-traffic-is-malicious.html/#comment-439376)

Sounds expensive. I wonder what percent of my internet bill paid for DDOS attacks.

finagle •
[July 17, 2024 4:53 PM](https://www.schneier.com/blog/archives/2024/07/cloudflare-reports-that-almost-7-of-all-internet-traffic-is-malicious.html/#comment-439377)

Clearly they need to persuade crackers to use VPNs, IPv6 or any browser that is not the absolute latest, because they routinely put CAPTCHAs or just block any of those scenarios.

Me •
[July 17, 2024 5:02 PM](https://www.schneier.com/blog/archives/2024/07/cloudflare-reports-that-almost-7-of-all-internet-traffic-is-malicious.html/#comment-439378)

Only 7%?

Does that mean things are improving?

Or is my memory of this number being higher in the past false?

Clive Robinson •
[July 17, 2024 6:01 PM](https://www.schneier.com/blog/archives/2024/07/cloudflare-reports-that-almost-7-of-all-internet-traffic-is-malicious.html/#comment-439379)

@ ALL,

Their definition of “malicious” is fairly “technical” so restricted. Thus this nearly 7% of traffic is actually a “low water mark” not a “high water mark”.

The thing is it’s actually the “high water mark” that is the one we should be trying to quantify and break out into classes of instances so that we can build defensive measures in efficient ways.

Clive Robinson •
[July 17, 2024 6:52 PM](https://www.schneier.com/blog/archives/2024/07/cloudflare-reports-that-almost-7-of-all-internet-traffic-is-malicious.html/#comment-439381)

@ ALL,

People have in the past kind of indicated that my view point on business machines not being connected to the Internet without a very clear business case is a bit paranoid…

But read in the article,

> *“In one case, attackers attempted to exploit a JetBrains TeamCity DevOps authentication bypass a mere 22 minutes after the proof-of-concept code was published. That speed is faster than most organizations can read the security advisory, let alone patch their systems.
> “*

So before the overworked underpaid tech support bods can even read a security advisory let alone act on it, attackers are into systems securing their toe-hold entry and moving horizontally etc to own more of the organisational infrastructure…

The simple and very old logic of,

“If they can not reach machines they can not attack them.”

As a security mitigation has made sense in the past and makes even more sense today…

finagle •
[July 18, 2024 5:00 AM](https://www.schneier.com/blog/archives/2024/07/cloudflare-reports-that-almost-7-of-all-internet...