---
title: New VPN Service Can’t Log Users by Design
url: https://torrentfreak.com/new-vpn-service-cant-log-users-by-design/
source: TorrentFreak
date: 2025-06-30
fetch_date: 2025-10-06T22:54:56.404499
---

# New VPN Service Can’t Log Users by Design

[![](https://torrentfreak.com/wp-content/themes/tf-theme-v2/build/assets/img/logo.svg)](/)

![](https://torrentfreak.com/wp-content/themes/tf-theme-v2/build/assets/img/search.svg)

* News ▼
  + [Piracy](https://torrentfreak.com/category/piracy/)
  + [Piracy Research](https://torrentfreak.com/category/research/)
  + [Law and Politics](https://torrentfreak.com/category/law-politics/)
  + [Lawsuits](https://torrentfreak.com/category/lawsuits/)
  + [Anti-Piracy](https://torrentfreak.com/category/anti-piracy/)
  + [Technology](https://torrentfreak.com/category/technology/)
* [Contact](https://torrentfreak.com/contact/)
* [Subscribe](https://torrentfreak.com/subscriptions/)

![](https://torrentfreak.com/wp-content/themes/tf-theme-v2/build/assets/img/x.svg)

# New VPN Service Can’t Log Users by Design

June 29, 2025 by
[Ernesto Van der Sar](https://torrentfreak.com/author/ernesto/)

[Home](https://torrentfreak.com "Go to TorrentFreak.") > [Technology](https://torrentfreak.com/category/technology/ "Go to the Technology category archives.") > [VPN Providers](https://torrentfreak.com/category/technology/vpn-services/ "Go to the VPN Providers category archives.") >

VPN providers typically offer security and privacy as a service. They make it difficult for outsiders, including ISPs, to monitor users' activities. Instead, they require subscribers to trust them with their online traffic. VP.net, a new provider, takes a different approach. The company promises 'cryptographically verifiable privacy' by using special hardware 'safes' (Intel SGX), so even the provider can't track what its users are up to. Trust in technology and hardware is still required, of course.

![vpnet](https://torrentfreak.com/images/vpnet.jpg)
Over the past two decades, the VPN industry has grown spectacularly, with plenty of competition between providers.

The days when [a review](https://torrentfreak.com/which-vpn-providers-really-take-anonymity-seriously-111007-archive/) of VPN logging policies was a novelty are long gone.

While new VPN services launch frequently, it’s rare to see one with a truly unique technical approach. That’s why [VP.net](https://vp.net/l/en-US/) warrants a closer look. Unlike most VPN providers, it doesn’t ask users for their trust; it relies on hardware-enforced privacy instead.

## Trust

When you use a VPN, your internet traffic is encrypted between your device and the VPN’s server. This is great for protecting your data from snooping on public Wi-Fi and your internet provider. However, to route your traffic to its final destination on the internet, the VPN server must decrypt it first.

At this decryption point, it’s technically possible for the VPN provider to access information about your online activity. This is common knowledge and requires that you trust your VPN. It’s also why using shady free VPN apps from unknown companies should be avoided; the user may end up being the product.

For a successful VPN service to thrive, trust, security, and privacy are paramount. Reputable VPN companies build their entire business model on trust, knowing that a breach would be catastrophic for their reputation.

But what if trust was taken out of the equation entirely? This is what VP.net promises to do, at least up to a point.

## VP.net

Like most VPNs, VP.net hides your real IP-address, replacing it with the address of the server you connect to. This connection is encrypted using the popular open-source WireGuard protocol and can’t be spied on by outsiders.

What makes VP.net stand out from many regular VPNs is its special use of a technology called Intel [Software Guard Extensions](https://en.wikipedia.org/wiki/Software_Guard_Extensions) (SGX). SGX enclaves are private areas of memory that essentially act as a secure black box and not even the operators of the service can see what’s happening inside.

*VP.net*

![vpnet](https://torrentfreak.com/images/vpnet-overview.jpg)

The system within the SGX enclave is reportedly built to map user identities to temporary, anonymous tokens. This means the part of the system which knows that “User X is connected” is structurally walled off from the part that knows “someone is accessing website Y.” The design goal is that no one, not even the VPN company, can link “User X” to “Website Y.”

The use of SGX as a verifiable, hardware-enforced separation of user identity and web traffic, is a new concept for a VPN.

## ‘Verified Privacy’

VP.net essentially promises “verified privacy” with this technical setup. If everything works as described, it’s not technically possible for the owners of the server, typically the VPN provider, to log who is doing what and when.

The new VPN service is operated by the American company VP.NET LLC, which in turn is owned by [TCP IP Inc](https://tcpip.co/), which holds the intellectual property rights. That includes pending patents, including one of ‘hardware-based anonymization of network addresses.”

The idea to use SGX as a privacy shield comes from Andrew Lee, the chief privacy architect at VP.net. As the founder of Private Internet Access, which he sold to [Kape](https://www.kape.com/our-brands/) a few years ago, Lee has a long history in the VPN space. However, he believes this new concept is a breakthrough.

“Our zero trust solution does not require you to trust us – and that’s how it should be. Your privacy should be up to your choice – not up to some random VPN provider in some random foreign country,” Lee says.

VP.net says it cannot link traffic data to users, even if it wanted to. If a court order requested such data, the company would first scrutinize its legality but, after that, the only data it has access to are unlinked details, such as payment info and email addresses, provided by the user.

The new VPN company is led by CEO Matt Kim. The company also lists the contentious Bitcoin veterans [Roger Ver](https://en.wikipedia.org/wiki/Roger_Ver) and [Mark Karpelès](https://en.wikipedia.org/wiki/Mark_Karpel%C3%A8s) in their team, who both have had their legal issues in the past.

## Novel, Secure, but Not Infallible

VP.net’s source code is open to the public. To address the challenge of showing that this open-source code is the same as the code running on their servers, VP.net relies on a key SGX [feature](https://vp.net/l/en-US/faq) called ‘remote attestation’.

In essence, this mechanism allows the user’s client to receive cryptographic proof from the server’s hardware, verifying that it is a genuine SGX ‘safe’ and is running the exact, untampered code that was publicly available. This shifts the trust from the company’s promise to a verifiable, hardware-backed process.

The trust through technology aspect is certainly intriguing, but no technology is infallible. The code needs to be functional and secure, as a software flaw could lead to potential security issues.

Another potential problem lies on the hardware side. Intel SGX itself is a physical product that is part of the CPU, which in turn relies on firmware. Like any piece of hardware, [vulnerabilities](https://www.google.com/search?q=sgx+vulnerabilities) have been discovered in SGX in the past.

VP.net is aware of this and says it actively monitors the security of its software and infrastructure, while keeping systems fully up-to-date.

Of course, the true test will be speed and transparency when responding to the next major SGX vulnerability, a scenario for which all users should be prepared.

It’s safe to say that one should never have 100% trust in any VPN solution. In this case, VP.net promises to offer an extra layer of privacy but, in the end, even the most secure systems can be breached.

That said, it is interesting to see a novel approach to the ‘no logging’ discussions. Whether this novelty will scale and be embraced more broadly remains to be seen.

* [![](https://torrentfreak.com/wp-content/themes/tf-theme-v2/build/assets/img/arrow-left.svg)Next Post](https://torrentfreak.com/pirate-iptv-man-back-to-serve-5-years-p...