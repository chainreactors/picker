---
title: MasterCard DNS Error Went Unnoticed for Years
url: https://krebsonsecurity.com/2025/01/mastercard-dns-error-went-unnoticed-for-years/
source: Krebs on Security
date: 2025-01-23
fetch_date: 2025-10-06T20:26:45.191959
---

# MasterCard DNS Error Went Unnoticed for Years

Advertisement

[![](/b-action1/1.jpg)](https://action1.com/double-endpoints-free-cam2025/?utm_source=paidmedia&refid=Display_CAM_Krebs)

Advertisement

[![](/b-knowbe4/41.png)](https://gateway.on24.com/wcc/eh/1815783/human-risk-management-summit?partnerref=krebs)

[![Krebs on Security](https://krebsonsecurity.com/wp-content/uploads/2021/03/kos-27-03-2021.jpg)](https://krebsonsecurity.com/ "Krebs on Security")

[Skip to content](#content "Skip to content")

* [Home](https://krebsonsecurity.com/)
* [About the Author](https://krebsonsecurity.com/about/)
* [Advertising/Speaking](https://krebsonsecurity.com/cpm/)

# MasterCard DNS Error Went Unnoticed for Years

January 22, 2025

[107 Comments](https://krebsonsecurity.com/2025/01/mastercard-dns-error-went-unnoticed-for-years/#comments)

The payment card giant **MasterCard** just fixed a glaring error in its domain name server settings that could have allowed anyone to intercept or divert Internet traffic for the company by registering an unused domain name. The misconfiguration persisted for nearly five years until a security researcher spent $300 to register the domain and prevent it from being grabbed by cybercriminals.

![](https://krebsonsecurity.com/wp-content/uploads/2025/01/akamne.png)

From June 30, 2020 until January 14, 2025, one of the core Internet servers that MasterCard uses to direct traffic for portions of the mastercard.com network was misnamed. MasterCard.com relies on five shared Domain Name System (DNS) servers at the Internet infrastructure provider **Akamai** [DNS acts as a kind of Internet phone book, by translating website names to numeric Internet addresses that are easier for computers to manage].

All of the Akamai DNS server names that MasterCard uses are supposed to end in “akam.net” but one of them was misconfigured to rely on the domain “**akam.ne**.”

This tiny but potentially critical typo was discovered recently by **Philippe Caturegli**, founder of the security consultancy [Seralys](https://www.seralys.com/). Caturegli said he guessed that nobody had yet registered the domain akam.ne, which is under the purview of the top-level domain authority for the West Africa nation of [Niger](https://en.wikipedia.org/wiki/Niger).

Caturegli said it took $300 and nearly three months of waiting to secure the domain with the registry in Niger. After enabling a DNS server on akam.ne, he noticed hundreds of thousands of DNS requests hitting his server each day from locations around the globe. Apparently, MasterCard wasn’t the only organization that had fat-fingered a DNS entry to include “akam.ne,” but they were by far the largest.

Had he enabled an email server on his new domain akam.ne, Caturegli likely would have received wayward emails directed toward mastercard.com or other affected domains. If he’d abused his access, he probably could have [obtained website encryption certificates (SSL/TLS certs)](https://krebsonsecurity.com/2024/08/local-networks-go-global-when-domain-names-collide/) that were authorized to accept and relay web traffic for affected websites. He may even have been able to [passively receive Microsoft Windows authentication credentials](https://krebsonsecurity.com/2020/02/dangerous-domain-corp-com-goes-up-for-sale/) from employee computers at affected companies.

But the researcher said he didn’t attempt to do any of that. Instead, he alerted MasterCard that the domain was theirs if they wanted it, copying this author on his notifications. A few hours later, MasterCard acknowledged the mistake, but said there was never any real threat to the security of its operations.

“We have looked into the matter and there was not a risk to our systems,” a MasterCard spokesperson wrote. “This typo has now been corrected.”

Meanwhile, Caturegli received a request submitted through **Bugcrowd**, a program that offers financial rewards and recognition to security researchers who find flaws and work privately with the affected vendor to fix them. The message suggested his public disclosure of the MasterCard DNS error via [a post on LinkedIn](https://www.linkedin.com/feed/update/urn%3Ali%3Aactivity%3A7285038365236682753/) (after he’d secured the akam.ne domain) was not aligned with ethical security practices, and passed on a request from MasterCard to have the post removed.

![](https://krebsonsecurity.com/wp-content/uploads/2025/01/mastercard-response.png)

MasterCard’s request to Caturegli, a.k.a. “Titon” on infosec.exchange.

Caturegli said while he does have an account on Bugcrowd, he has never submitted anything through the Bugcrowd program, and that he reported this issue directly to MasterCard.

“I did not disclose this issue through Bugcrowd,” Caturegli wrote in reply. “Before making any public disclosure, I ensured that the affected domain was registered to prevent exploitation, mitigating any risk to MasterCard or its customers. This action, which we took at our own expense, demonstrates our commitment to ethical security practices and responsible disclosure.”

Most organizations have at least two authoritative domain name servers, but some handle so many DNS requests that they need to spread the load over additional DNS server domains. In MasterCard’s case, that number is five, so it stands to reason that if an attacker managed to seize control over just one of those domains they would only be able to see about one-fifth of the overall DNS requests coming in.

But Caturegli said the reality is that many Internet users are relying at least to some degree on public traffic forwarders or DNS resolvers like **Cloudflare** and **Google**.

“So all we need is for one of these resolvers to query our name server and cache the result,” Caturegli said. By setting their DNS server records with a long TTL or “Time To Live” — a setting that can adjust the lifespan of data packets on a network — an attacker’s poisoned instructions for the target domain can be propagated by large cloud providers.

“With a long TTL, we may reroute a LOT more than just 1/5 of the traffic,” he said.

The researcher said he’d hoped that the credit card giant might thank him, or at least offer to cover the cost of buying the domain.

“We obviously disagree with this assessment,” Caturegli wrote in [a follow-up post](https://www.linkedin.com/feed/update/urn%3Ali%3Aactivity%3A7285038365236682753?commentUrn=urn%3Ali%3Acomment%3A%28activity%3A7285038365236682753%2C7285289297706909697%29&dashCommentUrn=urn%3Ali%3Afsd_comment%3A%287285289297706909697%2Curn%3Ali%3Aactivity%3A7285038365236682753%29) on LinkedIn regarding MasterCard’s public statement. “But we’ll let you judge— here are some of the DNS lookups we recorded before reporting the issue.”

![](https://krebsonsecurity.com/wp-content/uploads/2025/01/mastercard-domains.png)

Caturegli posted this screenshot of MasterCard domains that were potentially at risk from the misconfigured domain.

As the screenshot above shows, the misconfigured DNS server Caturegli found involved the MasterCard subdomain **az.mastercard.com**. It is not clear exactly how this subdomain is used by MasterCard, however their naming conventions suggest the domains correspond to production servers at Microsoft’s **Azure** cloud service. Caturegli said the domains all resolve to Internet addresses at Microsoft.

“Don’t be like Mastercard,” Caturegli concluded in his LinkedIn post. “Don’t dismiss risk, and don’t let your marketing team handle security disclosures.”

One final note: The domain akam.ne has been registered previously — in December 2016 by someone using the email address um-i-delo@yandex.ru. The Russian search giant Yandex reports this user account belongs to an “Ivan I.” from Moscow. Passive DNS records from [DomainTools.com](https://www.domaintools.com) show that between 2016 and 2018 the domain was connected to an Internet server in Germany, and that the domain was left to expire in 2018.

This is interesting given [a comment on Caturegli’s LinkedIn post from an ex-Clo...