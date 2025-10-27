---
title: SPF and DMARC use on GOV domains in different ccTLDs, (Fri, Dec 30th)
url: https://isc.sans.edu/diary/rss/29384
source: SANS Internet Storm Center, InfoCON: green
date: 2022-12-31
fetch_date: 2025-10-04T02:48:50.968164
---

# SPF and DMARC use on GOV domains in different ccTLDs, (Fri, Dec 30th)

# [Internet Storm Center](/)

[Sign In](/login.html)
[Sign Up](/register.html)

Handler on Duty: [Johannes Ullrich](/handler_list.html#johannes-ullrich "Johannes Ullrich")

Threat Level: [green](/infocon.html)

* [previous](/diary/29382)
* [next](/diary/29386)

# [SPF and DMARC use on GOV domains in different ccTLDs](/forums/diary/SPF%2Band%2BDMARC%2Buse%2Bon%2BGOV%2Bdomains%2Bin%2Bdifferent%2BccTLDs/29384/)

**Published**: 2022-12-30. **Last Updated**: 2022-12-30 15:43:16 UTC
**by** [Jan Kopriva](/handler_list.html#jan-kopriva) (Version: 1)

[4 comment(s)](/diary/SPF%2Band%2BDMARC%2Buse%2Bon%2BGOV%2Bdomains%2Bin%2Bdifferent%2BccTLDs/29384/#comments)

Although e-mail is one of the cornerstones of modern interpersonal communication, its underlying Simple Mail Transfer Protocol (SMTP) is far from what we might call “robust” or “secure”[[1](https://en.wikipedia.org/wiki/Simple_Mail_Transfer_Protocol)]. By itself, the protocol lacks any security features related to ensuring (among other factors) integrity or authenticity of transferred data or the identity of their sender, and creating a “spoofed” e-mail is therefore quite easy. This poses a significant issue, especially when one considers that most ordinary people don’t tend to question the validity of officially looking messages if it appears that they were sent from a respectable/well-known domain.

Even disregarding the current geopolitical situation, it is clear that certain domains are of significantly higher interest than others to criminals as well as state-sponsored actors when it comes to spoofing e-mail. Among the more interesting ones are – without a doubt – governmental domains, i.e., domain.GOV in the US or domain.GOV.ccTLD in other countries. Which brings us to the topic of today’s diary, which is “how big of an issue e-mail spoofing might be for these particular domains”.

But first things first. Because of the aforementioned lack of "integral" security features, numerous extensions and additions to SMTP were introduced over time that were intended to add different security mechanisms to it – either on end-to-end or hop-to-hop (or originating server to recipient server) basis.

Three of these additions, which deserve special attention from any domain owner, are SPF[[2](https://www.rfc-editor.org/rfc/rfc7208.html)] , DKIM[[3](https://www.rfc-editor.org/rfc/rfc6376.html)] and DMARC[[4](https://www.rfc-editor.org/rfc/rfc7489.html)], which enable domain owners to specify which servers are “allowed” to send e-mail for a specific domain, and implement a corresponding verification and reporting framework. In general, it is considered a good practice to ensure that special SPF, DKIM and DMARC DNS records are set (and corresponding mechanisms and keys are configured on relevant mail servers) for any domain which is going to be used for sending e-mail.

“Enabling” SPF is relatively straightforward, however making sure that DKIM (and, potentially, DMARC) functions correctly is somewhat more complicated. This is the reason why SPF adoption is much wider than it is for either of the other two mechanisms[[5](https://redhuntlabs.com/blog/internet-wide-study-state-of-spf-dkim-and-dmarc.html)].

It is worth adding that it is also considered a good practice[[6](https://www.cloudflare.com/learning/dns/dns-records/protect-domains-without-email/)] to set “blocker” SPF and DMARC DNS records for any domain, that is not going to be used for sending e-mail. These have the following contents and specify that no server is allowed to send e-mail on behalf of the particular domain.

SPF record (TXT record published for domain.tld):

```

v=spf1 -all
```

DMARC record (TXT record published as \_dmarc.domain.tld):

```

v=DMARC1; p=reject;
```

With this short overview out of the way, it should be clear that for any gov.ccTLD domain, at least a valid SPF DNS record (though, ideally, DKIM and DMARC records as well) should be published, even if it was just a “blocking” one.

To discover what percentage of second-level GOV domains actually employ the aforementioned security mechanisms, I wrote a short script that identified ccTLDs in which such domains existed, and gathered and evaluated the corresponding SPF and DMARC records, if these were published (determining whether DKIM is being used by a specific domain is unfortunately impossible without direct communication with the corresponding e-mail server, so no data could be gathered regarding support of this mechanism).

The results were…interesting, if not necessarily optimistic.

A second-level GOV domain existed in 178 of the 247 ccTLDs listed on Wikipedia[[7](https://en.wikipedia.org/wiki/Country_code_top-level_domain)], but only 78 of these gov.ccTLD domains (cca 45%) had an SPF record published. Furthermore, records for 5 domains were either malformed or did not contain an explicit “all” directive, which made them effectively meaningless. Only 33 domains (cca 19 %) had a valid DMARC record published.

You may see detailed results for DMARC and SPF support on the GOV domains in different ccTLDs in the following charts.

[![](https://isc.sans.edu/diaryimages/images/22-12-30-gov_spf_global.png)](https://isc.sans.edu/diaryimages/images/22-12-30-gov_spf_global.png)

[![](https://isc.sans.edu/diaryimages/images/22-12-30-gov_dmarc_global.png)](https://isc.sans.edu/diaryimages/images/22-12-30-gov_dmarc_global.png)

Since – as we mentioned – these results were not overly positive, I’ve filtered out only NATO and EU countries hoping that the numbers would look somewhat better for their ccTLDs. However, as you may see from the following chart, results for these countries were not significantly better (in fact, in some areas, thay were a little worse)...

[![](https://isc.sans.edu/diaryimages/images/22-12-30-gov_spf_dmarc_eu_nato.png)](https://isc.sans.edu/diaryimages/images/22-12-30-gov_spf_dmarc_eu_nato.png)

As the previous charts show, SPF and DMARC (and most likely DKIM as well) use on second-level governmental domains in ccTLDs around the world is far from optimal, and even a less sophisticated threat actor could therefore easily spoof e-mail for these domains…

Which is unfortunate, to say the least.

It should be mentioned, however, that the fact that second-level GOV domains are often not used for anything by themselves probably had a negative impact on the results. In many – If not most – ccTLDs, only third-level domains (e.g., domain.gov.cctld) are actually being used by governmental organizations. In such cases, the third-level domains may well have SPF, DMARC and other security measures configured in accordance with good industry practice, however since the second-level GOV domain is not actually being “used” on its own, no one might have realized the need to make sure that no one can “misuse” it either, at least by setting up relevant “blocker” records, such as the ones we mentioned above.

To end on at least a slightly positive note, 8 of the second-level GOV domains actually had just such a “blocker” SPF record published, which is perhaps more than one might expect.

[1] <https://en.wikipedia.org/wiki/Simple_Mail_Transfer_Protocol>
[2] <https://www.rfc-editor.org/rfc/rfc7208.html>
[3] <https://www.rfc-editor.org/rfc/rfc6376.html>
[4] <https://www.rfc-editor.org/rfc/rfc7489.html>
[5] <https://redhuntlabs.com/blog/internet-wide-study-state-of-spf-dkim-and-dmarc.html>
[6] <https://www.cloudflare.com/learning/dns/dns-records/protect-domains-without-email/>
[7] <https://en.wikipedia.org/wiki/Country_code_top-level_domain>

-----------
Jan Kopriva
[@jk0pr](https://twitter.com/jk0pr)
[Nettles Consulting](https://www.nettles.cz/)

Keywords: [DKIM](/tag.html?tag=DKIM) [DMARC](/tag.html?tag=DMARC) [Email](/tag.html?tag=Email) [SPF](/tag.html?tag=SPF)

[4 comment(s)](/diary/SPF%2Band%2BDMARC%2Buse%2Bon%2BGOV%2Bdomains%2Bin%2Bdifferent%2BccTLDs/29384/#comments)

* [previous](/diary/29382)
* [next](/diary/29386)

### Comments

In the commercial spaces where I work I feel l...