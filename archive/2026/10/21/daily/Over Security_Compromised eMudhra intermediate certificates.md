---
title: Compromised eMudhra intermediate certificates
url: https://blog.talosintelligence.com/compromised-intermediate-certificates/
source: Over Security
date: 2026-10-21
fetch_date: 2026-10-22T06:46:21.501940
---

# Compromised eMudhra intermediate certificates

[Blog](/)

[ ]

* [Intelligence Center](https://talosintelligence.com/reputation)

  [ ]

  + [# Intelligence Center](https://talosintelligence.com/reputation)
  + BACK
  + [Intelligence Search](https://talosintelligence.com/reputation_center)
  + [Email & Spam Trends](https://talosintelligence.com/reputation_center/email_rep)
* [Vulnerability Research](https://talosintelligence.com/vulnerability_info)

  [ ]

  + [# Vulnerability Research](https://talosintelligence.com/vulnerability_info)
  + BACK
  + [Vulnerability Reports](https://talosintelligence.com/vulnerability_reports)
  + [Microsoft Advisories](https://talosintelligence.com/ms_advisories)
* [Incident Response](https://talosintelligence.com/incident_response)

  [ ]

  + [# Incident Response](/incident_response)
  + BACK
  + [Reactive Services](https://talosintelligence.com/incident_response/services#reactive-services)
  + [Proactive Services](https://talosintelligence.com/incident_response/services#proactive-services)
  + [Emergency Support](https://talosintelligence.com/incident_response/contact)
* [Blog](https://blog.talosintelligence.com)
* [Support](https://support.talosintelligence.com)

More

* Security Resources

  [ ]

  # Security Resources

  + BACK

  Security Resources
  + [Open Source Security Tools](https://talosintelligence.com/software)
  + [Intelligence Categories Reference](https://talosintelligence.com/categories)
  + [Secure Endpoint Naming Reference](https://talosintelligence.com/secure-endpoint-naming)
* Media

  [ ]

  # Media

  + BACK

  Media
  + [Talos Intelligence Blog](https://blog.talosintelligence.com)
  + [Threat Source Newsletter](https://blog.talosintelligence.com/category/threat-source-newsletter/)
  + [Beers with Talos Podcast](https://talosintelligence.com/podcasts/shows/beers_with_talos)
  + [Talos Takes Podcast](https://talosintelligence.com/podcasts/shows/talos_takes)
  + [Talos Videos](https://www.youtube.com/channel/UCPZ1DtzQkStYBSG3GTNoyfg/featured)
* Company

  [ ]

  # Company

  + BACK

  Company
  + [About Talos](https://talosintelligence.com/about)
  + [Careers](https://talosintelligence.com/careers)

![](https://storage.ghost.io/c/af/a0/afa04ee3-414f-4481-8d23-7e7c146f192e/content/images/2026/10/threat_advisory.png)

# Compromised eMudhra intermediate certificates

By
[Cisco Talos](https://blog.talosintelligence.com/author/cisco/)

Wednesday, October 21, 2026 16:43

[Threat Advisory](/category/threat-advisory/)

Cisco Talos is aware of eight intermediate certificates belonging to the intermediate certificate authority, [eMudhra](https://emudhra.com/en/post/certificate-security-incident). Rather than possessing the mandatory 384 bits of pseudo-random security, several private keys evaluated single-digit and double-digit integers. This misconfiguration allows an attacker with the private key of any of the compromised intermediate CAs to impersonate any website or service. Six of the TLS certificates, trusted by Chrome, Mozilla, and Apple have been blocked by these vendors already. Two other certificates, used for codesigning by Microsoft, have also been blocked. Talos expects there will be additional patches available across a variety of technologies as software applications work to remediate the certificates’ exposure.

Following the disclosure, eMudhra has revoked the compromised certificates and stopped issuing new certificates under its G3 root.

## Compromise details

The cause of this issue, originated during an April 30, 2025 key generation activity conducted by eMudhra under its emSign Root TLS CA - G3 and cross-signed Comodo AAA Certificate Services.  During a key generation ceremony for 24 subordinate CAs, a flaw in eMudhra’s key generation process created a second set of weak P-384 keys during a wrap/unwrap step. Those keys were mistakenly used for eight intermediate CA certificates. This flaw took the encryption from 384 bytes of entropy down to 3 – 8, making recovering the private keys trivial. The following are the impacted certificates, as illustrated in [Mozilla’s bug report](https://bugzilla.mozilla.org/show_bug.cgi?id=2083449):

```
EM EV TLS CA - G3B (eMudhra BV), CCADB A012304
SHA-256 E7568FE6E12331F4FD7DE61DA4C7559D0F8EB192A218D4741A3BA75184333838
serial c7c41efe92d825f05eae841a4a82c1, issuer emSign Root TLS CA - G3

EM OV TLS CA - G3B (eMudhra BV), CCADB A012308
SHA-256 98B896625C0C230ADEEC3EB2CF6AAD5001ECF9156A68644E82374CE5833BC25B
serial 6cada367fb1c100088120ea202d568, issuer emSign Root TLS CA - G3

EM DV TLS CA - G3B (eMudhra BV), CCADB A012302
SHA-256 42C4ACCD12C4F59597925E1A08A7A90102608543809308D50EC427E118BA1493
serial a4aee678f23362b4c0e460b772f214, issuer emSign Root TLS CA - G3

EM EV TLS CA - G3C (eMudhra Inc), CCADB A012296
SHA-256 432EC25F0D28DE9006D97BF752F17BBB2CD41F669933FCB072D9A1148D0261F3
serial 8009928a64107601af05fa2f19f109, issuer emSign Root TLS CA - G3

EM OV TLS CA - G3C (eMudhra Inc), CCADB A012300
SHA-256 CB6E15165AC802E9B3F993F16C25D41F4E81C21EBDE71AE1B012AC00BF9C7C3F
serial 296926c227a3a1526392b19482a504, issuer emSign Root TLS CA - G3

EM DV TLS CA - G3C (eMudhra Inc), CCADB A012294
SHA-256 0164D7CEAE5BB909C272AF151FF44B1177AE9B47D9424B94F1D9558C30934D19
serial 588b2e3c2bb8cda13e1a1209254321, issuer emSign Root TLS CA - G3

EM OV CS CA - G3B (eMudhra BV), CCADB A012306
SHA-256 9E39DE2881273ACC225A149C72BA3E0F51424963669AB633EE1DC7DF5DB067B4
serial 7818933f8f85b4619a2b35fba83d0a, issuer emSign Root CS CA - G3

EM OV CS CA - G3C (eMudhra Inc), CCADB A012298
SHA-256 4B2460A466F95FD40113BCDCCA2CEB29B3B093921DE45474DA7DF48874C630B1
serial 544b7f922c31ae220a4a922916f6e6, issuer emSign Root CS CA - G3
```

## CVE-2026-111943

Unlike languages that defer entirely to external dynamic system libraries (like OpenSSL), the Go programming runtime implements its own X.509 chain verification engine in the standard library (crypto/x509). While Go usually queries platform certificates, several platforms or static container environments rely on embedded or legacy root certificate pools where certificate revocations are ignored.

To eliminate exploitation across the entire cloud-native ecosystem including Docker, Kubernetes, Terraform, and Prometheus, the Go team designated the compromised certificates as a vulnerability, [CVE-2026-111943,](https://www.cve.org/CVERecord?id=CVE-2026-111943) and released Go versions 1.27.3 and 1.26.10.

 The fixed versions filter out chains containingthe SHA-256 hashes of the SubjectPublicKeyInfo (SPKI) for all eight compromised eMudhra intermediate certificates.

## Impact

These compromised certificates could allow adversaries to impersonate servers and intercept or modify traffic. The impact of their exposure is far more than just web browsers. Other programs that check for TLS certificates might still be impacted since they may not check revocation lists. One clear example is related to virtual private networks (VPNs); these technologies will likely require software updates to mitigate the issue. Based on this guidance, Talos strongly recommends users update software using and handling TLS certificates as fixes become available.

Talos is actively monitoring the impact of these compromised certificates and has not seen any malicious incidents involving them in the wild yet (as of October 21, 2026 14:00 UTC / 10:00 a.m. ET).

## Significance of this breach

Public key infrastructure relies on trust being delegated through certificate chains: root CAs authorize intermediate CAs, which can issue certificates within the scope of their authority. An attacker who obtains an intermediate CA’s private key may be able to issue fraudulent certificates that clients accept, subject to the intermediate certificate’s constraints and each client’s validation controls. In this incident, six compromised intermediates were for TLS and two were for code signing.

 For TLS, an attacker able to intercept or redirect a connection could use a fraudulent certificate to impersonate a server and po...