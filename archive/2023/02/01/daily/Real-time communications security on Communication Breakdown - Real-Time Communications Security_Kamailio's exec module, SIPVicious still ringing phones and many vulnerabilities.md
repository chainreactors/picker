---
title: Kamailio's exec module, SIPVicious still ringing phones and many vulnerabilities
url: https://www.rtcsec.com/newsletter/2023-01-rtcsec-news/
source: Real-time communications security on Communication Breakdown - Real-Time Communications Security
date: 2023-02-01
fetch_date: 2025-10-04T05:19:45.745592
---

# Kamailio's exec module, SIPVicious still ringing phones and many vulnerabilities

[Skip to main content](#content)

[![Enable Security logo](https://www.enablesecurity.com/assets/img/logo-header-white.min.ac2c259ad95c9e369b3d7e44d9986a07c2c45fec663fbceaefe184e92011793a.svg)](/)

* [Get in touch](/contact/)

* Security Testing
  + [VoIP Penetration Testing](/voip-penetration-testing/)
  + [WebRTC Penetration Testing](/penetration-testing/)
  + [VoIP Security Assessment](/voip-security-assessment/)
  + [DDoS Resilience Testing](/ddos-testing/)
  + [Code & Config Analysis](/code-and-config-analysis/)
  + [Fuzz Testing](/fuzz-testing/)
* [SIPVicious](/sipvicious/)
* [Consultancy](/consultancy/)
* [Research](/research/)
* [Blog](/blog/)
* [Newsletter](/newsletter/)
* [About](/about/)
* [Contact](/contact/)

# Kamailio’s exec module, SIPVicious still ringing phones and many vulnerabilities

Published on Jan 31, 2023

This new year starts off with a number of RTC security related news and we have some original content to share with you too!

In this edition, we cover:

* Our news: The dangers of using the Kamailio exec module and our pentesting schedule
* Our news: Updates to the awesome RTC hacking list
* The Threema weaknesses paper from ETH Zurich
* Presentations of interest from Blackhat and Nullcon Berlin
* Receiving calls on your deskphone from SIPVicious - still happening!
* Various vulnerabilities in Cisco products, Juniper and Chrome’s WebRTC

RTCSec newsletter is a free periodic newsletter bringing you commentary and news around VoIP and WebRTC security. We cover both defensive and offensive security as they relate to Real-time Communications.

What is RTC security anyway? Real-time communications security is what determines if you can communicate in real time in a safe way - whether it be with other humans or machines.

You may sign up to receive the RTCSec newsletter [here](https://www.enablesecurity.com/subscribe/). Do:

* forward to that person who may find this newsletter particularly fruitful.
* let me know if we should include or cover any RTC security news.

To view past issues, please visit our website at <https://www.enablesecurity.com/newsletter/>.

---

## Our news

### Penetration testing or security assessment in 2023? (advert)

If you’re subscribed to this newsletter, chances are you’re also thinking about pentesting your RTC products and services in 2023.

At the moment we’re working on filling our work schedule for Q2 2023. If you’d like to be included in our thoughts, reply to me or [contact us](https://www.enablesecurity.com/contact/).

### The dangers of using the Kamailio exec module

Kamailio is one of our favorite SIP servers … so we wrote about the most obvious ways that it can be insecurely configured, leading to remote code execution. Our new article is about the exec module.

The summary reads as follows:

* The combination of pseudo-variables and Kamailio’s exec can be risky and may result in code injection.
* By using special SIP headers and environment variables, it becomes effortless to exploit a vulnerable configuration.
* We have created a Docker environment to assist readers in reproducing this vulnerability and testing solutions.
* Protection is tricky and the official documentation may have previously misled developers - we aim to fix that by updating the module’s official documentation.
* Kamailio configurations should use a strict allow list or avoid the module altogether.

Thanks to the Kamailio developers for quickly reviewing and accepting our updated documentation pull request!

Read the entire post here: <https://www.enablesecurity.com/blog/kamailio-exec-module-considered-harmful/>

### Updated Awesome RTC hacking & pentesting resources list

The Awesome real-time communications hacking list has been updated with the following from last year:

* blog posts related to VoIP and WebRTC security:
  + MSTeams Direct Routing abuse
  + OpenSSL CVE-2022-0778 vs WebRTC applications
  + our latest blog post - *Kamailio’s exec module considered harmful*
* VoIP Hopper added to the list of open-source tools

Check it out at <https://github.com/EnableSecurity/awesome-rtc-hacking>

## What’s happening?

### Threema weaknesses paper was published and the drama

Security researchers from the Applied Cryptography group at ETH Zurich published a paper outlining 7 attacks that affected Threema, often advertised as the *most secure messenger*. The paper was published on its own domain, called breakingthe3ma.app and comes together with a logo. The vendor addressed all security issues quickly, within weeks. They also upgraded the protocols involved to address some of the vulnerabilities outlined as well as previously known issues.

Threema also published a blog post which downplays or disputes the claims made on the Breaking Threema website (published by the researchers). They wrote that **none of them ever had any considerable real-world impact** and that the attacks assume extensive / unrealistic prerequisites such as physical access to an unlocked Android device.

Then, of course, the usual Twitter drama ensued.

Heated online debates aside, it is worth heeding or at least considering the researchers’ lessons, which were the following (quoted):

> 1. **Using modern, secure libraries for cryptographic primitives does not, on its own, lead to a secure protocol design**: libraries such as NaCl or libsignal can be misused while building more complex protocols and developers must be wary not to be lulled into a false sense of security. While the mantra don’t roll your own crypto is now widely known, it should be extended to don’t roll your own cryptographic protocol (assuming one already exists that meets the developer’s requirements). In the case of Threema, the bespoke C2S protocol could be replaced by TLS.
> 2. **Beware of cross-protocol interactions**: even if a protocol on its own is considered secure, there is no *a priori* guarantee that it will be secure when composed with other protocols. Cross-protocol interactions can undermine the original security guarantees, as we have shown with the vouch box forgery and Kompromat attacks. Such bad interactions can be prevented by following the *key separation principle* which states that a system should use different keys for different purposes.
> 3. **Proactive, not reactive security**: our inability to find an attack on a protocol does not imply it is secure. New attacks could be found at any moment and known attacks only get stronger over time if left unaddressed. Often, secure systems and protocols follow a *design-release-break-patch* process (a *reactive* approach). This is inconvenient for users and often requires the maintenance of backwards compatibility. Developers should instead adopt a *proactive* approach, where the system or protocol is formally analyzed during the design stage.

The attacks outlined were the following:

1. Ephemeral key compromise impersonation (network attacker)
2. Vouch box forgery (network attacker)
3. Message reordering and deletion (compromised server)
4. Replay and reflection attacks (compromised server)
5. Kompromat attack (was actually previously fixed but included because they rediscovered it) (compromised server)
6. Cloning via Threema ID export (compelled access)
7. Compression side-channel (compelled access)

Primary references:

* <https://breakingthe3ma.app/> - the researcher’s website presenting their paper
* <https://threema.ch/en/blog/posts/news-alleged-weaknesses-statement> - Threema’s official statement

Together with the researcher’s website, and Threema’s statement blog post, we recommend those interested in the details to read (or listen to) the following:

* <https://blog.dbrgn.ch/2023/1/14/threema/> - Some thoughts on ETH’s Threema Analysis by a Threema software engineer; gives some useful background and analysis
* <https://www.youtube.com/watch?v=QVt6RkYfGy0> - Security Cryptography Whatever Podcast - Threema with Kenny Paterson, Matteo Scarlata, & Kien Tuong Truong; discussions with the researchers the...