---
title: Weakening TLS protection, South Korean style
url: https://palant.info/2023/02/06/weakening-tls-protection-south-korean-style/
source: Over Security - Cybersecurity news aggregator
date: 2023-03-01
fetch_date: 2025-10-04T08:22:02.330886
---

# Weakening TLS protection, South Korean style

[Almost Secure](/)

* [Home](/)
* [Articles](/articles/)
* [Categories](/categories/)
* [About](/about/)
* ##

  Read More Â»

[ ]

# Weakening TLS protection, South Korean style

2023-02-06
 [Korea](/categories/korea/)/[Security](/categories/security/)/[Privacy](/categories/privacy/)
 5 mins
 [13 comments](/2023/02/06/weakening-tls-protection-south-korean-style/#comments)

*Note*: This article is also available [in Korean](https://github.com/alanleedev/KoreaSecurityApps/blob/main/03_weakening_tls_protection.md).

Normally, when you navigate to your bankâs website you have little reason to worry about impersonations. The browser takes care of verifying that you are really connected to the right server, and that your connection is safely encrypted. It will indicate this by showing a lock icon in the address bar.

So even if you are connected to a network you donât trust (such as open WiFi), nothing can go wrong. If somebody tries to impersonate your bank, your browser will notice. And it will refuse connecting.

![Screenshot of an error message: Did Not Connect: Potential Security Issue. Firefox detected a potential security threat and did not continue to www.citibank.co.kr because this website requires a secure connection.](/2023/02/06/weakening-tls-protection-south-korean-style/ssl_error.png)

This is achieved by means of a protocol called [Transport Layer Security (TLS)](https://en.wikipedia.org/wiki/Transport_Layer_Security). It relies on a number of trusted Certification Authorities (CAs) to issue certificates to websites. These certificates allow websites to prove their identity.

When investigating [South Koreaâs so-called security applications](/2023/01/02/south-koreas-online-security-dead-end/) I noticed that all of them add their own certification authorities that browsers have to trust. This weakens the protection provided by TLS considerably, as misusing these CAs allows impersonating any website towards a large chunk of South Korean population. This puts among other things the same banking transactions at risk that these applications are supposed to protect.

#### Contents

* [Which certification authorities are added?](#which-certification-authorities-are-added)
* [Will a few more certification authorities really hurt?](#will-a-few-more-certification-authorities-really-hurt)
* [How could this issue be solved?](#how-could-this-issue-be-solved)

## Which certification authorities are added?

After doing online banking on your computer in South Korea, itâs worth taking a look at the trusted certification authorities of your computer. Most likely you will see names that have no business being there. Names like iniLINE, Interezen or Wizvera.

![Screenshot of the Windows âTrusted Root Certification Authoritiesâ list. Among names like GTE CyberTrust or Microsoft, also iniLINE and Interezen are listed.](/2023/02/06/weakening-tls-protection-south-korean-style/authorities.png)

None of these are normally trusted. They have rather been added to the operating systemâs storage by the respective applications. These applications also add their certification authorities to Firefox which, unlike Google Chrome or Microsoft Edge, wonât use operating systemâs settings.

So far I found the following certification authorities being installed by South Korean applications:

| Name | Installing application(s) | Validity | Serial number |
| --- | --- | --- | --- |
| ASTxRoot2 | AhnLab Safe Transaction | 2015-06-18 to 2038-06-12 | 009c786262fd7479bd |
| iniLINE CrossEX RootCA2 | TouchEn nxKey | 2018-10-10 to 2099-12-31 | 01 |
| INTEREZEN CA | Interezen IPInside Agent | 2021-06-09 to 2041-06-04 | 00d5412a38cb0e4a01 |
| LumenSoft CA | KeySharp CertRelay | 2012-08-08 to 2052-07-29 | 00e9fdfd6ee2ef74fc |
| WIZVERA-CA-SHA1 | Wizvera Veraport | 2019-10-23 to 2040-05-05 | 74b7009ee43bc78fce69 73ade1da8b18c5e8725a |
| WIZVERA-CA-SHA2 | Wizvera Veraport, Wizvera Delfino | 2019-10-23 to 2040-05-05 | 20bbeb748527aeaa25fb 381926de8dc207102b71 |

And these certification authorities will stay there until removed manually. The applicationsâ uninstallers wonât remove them.

They are also enabled for all purposes. So one of these authorities being compromised will not merely affect web server identities but also application or email signatures for example.

**Update** (2023-02-19): Someone compiled a [more comprehensive list of these certificates](https://fake-root.github.io/).

## Will a few more certification authorities really hurt?

If you look at the list of trusted certification authorities, there are more than 50 entries on it anyways. Whatâs the problem if a few more are added?

Running a Certificate Authority is a huge responsibility. Anyone with access to the private key of a trusted certification authority will be able to impersonate any website. Criminals and governments around the world would absolutely love to have this power. The former need it to impersonate your bank for example, the latter to [spy on you undetected](https://www.theregister.com/2015/12/03/kazakhstan_to_maninthemiddle_all_internet_traffic/).

Thatâs why there are [strict rules for certification authorities](https://www.mozilla.org/en-US/about/governance/policies/security-group/certs/policy/#2-certificate-authorities), making sure the access to the CAâs private key is restricted and properly secured. Running a certification authority also requires regular external audits to ensure that all the security parameters are still met.

Now with these South Korean applications installing their own Certificate Authorities on so many computers in South Korea, they become a huge target for hackers and governments alike. If a private key for one of these Certificate Authorities is compromised, TLS will provide very little protection in South Korea.

How do AhnLab, RaonSecure, Interezen, Wizvera deal with this responsibility? Do they store the private keys in a [Hardware Security Module (HSM)](https://en.wikipedia.org/wiki/Hardware_security_module)? Are these in a secure location? Who has access? What certificates have been issued already? We have no answer to these questions. There are no external audits, no security practices that they have to comply with.

So people are supposed to simply trust these companies to keep the private key secure. As weâve already seen from [my previous articles](/categories/korea/) however, they have little expertise in keeping things secure.

## How could this issue be solved?

The reason for all these certificate authorities seems to be: the applications need to enable TLS on their local web server. Yet no real certificate authority will issue a certificate for 127.0.0.1, so they have to add their own.

If a certificate for 127.0.0.1 is all they need, there is a simple solution. Instead of adding the same CA on all computers, it should be a different CA for each computer.

So the applications should do the following during the installation:

1. Generate a new (random) certificate authority and the corresponding private key.
2. Import this CA into the list of trusted certification authorities on the computer.
3. Generate a certificate for 127.0.0.1 and sign it with this CA. Application can now use it for its local web server.
4. Destroy the private key of the CA.

In fact, Initech CrossWeb Ex V3 seems to do exactly that. You can easily recognize it because the displayed validity starts at the date of the installation. While it also installs its certificate authority, this one is valid for one computer only and thus unproblematic.

Oh, and one more thing to be taken care of: any CAs added should be removed when the application is uninstalled. Currently none of the applications seem to do it.

Share on:

## See Also:

* [Veraport: Inside Koreaâs dysfunctional application management](/2023/03/06/veraport-inside-koreas-dysfunctional-application-management/)
* [South Koreaâs banking security: Intermediate conclusions](/2023/02/20/south-koreas-bankin...