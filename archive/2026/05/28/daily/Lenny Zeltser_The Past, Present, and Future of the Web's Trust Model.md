---
title: The Past, Present, and Future of the Web's Trust Model
url: https://zeltser.com/past-present-future-web-trust-model
source: Lenny Zeltser
date: 2026-05-28
fetch_date: 2026-05-29T06:06:21.391787
---

# The Past, Present, and Future of the Web's Trust Model

[Lenny Zeltser](/)Security builder & leader

 [Projects](/projects) [Writing](/writing) [About](/about)

×

# The Past, Present, and Future of the Web's Trust Model

Observability, short-lived credentials, and active enforcement hold the web's trust model together. Without them, a decade of Certificate Authority failures would've collapsed it. Will those same levers hold for what's coming next?

![The Past, Present, and Future of the Web's Trust Model - illustration](/assets/past-present-future-web-trust-model.DcNjC94X_Z1144xM.webp)

The web’s certificate trust model has held up through more than a decade of CA breaches, misissued certificates, and distrust events. How did it survive that pressure, and where are we heading? You can apply the same patterns to any system where you delegate trust.

## What it was meant to be.

The original [Public Key Infrastructure](https://en.wikipedia.org/wiki/Public_key_infrastructure) design assumed trust that could be delegated through a hierarchy of certificate authorities. Root CAs hard-coded into browsers and operating systems would vouch for intermediate CAs, which in turn would vouch for end-entity certificates. On receiving a certificate, a browser would check the chain against trusted roots and accept it as valid. The approach traces back to the early [X.509](https://en.wikipedia.org/wiki/X.509) standard work and [Netscape’s SSL deployment](https://en.wikipedia.org/wiki/Transport_Layer_Security) in 1995.

Three assumptions underpinned the design:

* CAs would not issue certificates fraudulently.
* Compromised certificates could be revoked, and clients would honor that revocation.
* The list of trusted roots would remain stable.

There was no public log of issued certificates. [Browsers treated certificate revocations as advisory](https://www.imperialviolet.org/2014/04/19/revchecking.html). The system relied on each CA doing its job correctly.

## What happened.

CA failures came in waves, each exposing a different design assumption. [Smaller CA incidents had appeared earlier](https://en.wikipedia.org/wiki/Certificate_authority#CA_compromise), but DigiNotar was the first to force browsers to remove a root CA entirely.

In 2011, [Dutch CA DigiNotar was breached](https://security.googleblog.com/2011/08/update-on-attempted-man-in-middle.html) and issued hundreds of fraudulent certificates. The attackers used a wildcard for \*.google.com to intercept Gmail traffic in Iran. Any CA could issue a valid certificate for any domain, and revocation only helped after detection.

Smaller incidents followed. Misissuance by [TURKTRUST](https://blog.mozilla.org/security/2013/01/03/revoking-trust-in-two-turktrust-certficates/) and [ANSSI](https://blog.mozilla.org/security/2013/12/09/revoking-trust-in-one-anssi-certificate/) in 2013, then [CNNIC](https://blog.mozilla.org/security/2015/03/23/revoking-trust-in-one-cnnic-intermediate-certificate/) in 2015, prompted browsers to tighten scrutiny each time.

Symantec’s CA business [misissued certificates over several years](https://security.googleblog.com/2017/09/chromes-plan-to-distrust-symantec.html), including test certificates [for domains it didn’t control](https://security.googleblog.com/2015/10/sustaining-digital-certificate-security.html). Mozilla and Google [announced a phased rollback of trust](https://blog.mozilla.org/security/2018/03/12/distrust-symantec-tls-certificates/) in 2017. [Chrome removed trust](https://security.googleblog.com/2018/03/distrust-of-symantec-pki-immediate.html) from Symantec’s old infrastructure entirely in 2018. Symantec, then one of the world’s largest CAs, sold its CA business to [DigiCert](https://en.wikipedia.org/wiki/DigiCert) in response to the planned rollback.

Code signing exposed a related but distinct failure mode:

* In 2020, attackers [compromised SolarWinds’ build process](https://www.crowdstrike.com/en-us/blog/sunspot-malware-technical-analysis/). The [backdoored Orion DLL](https://cloud.google.com/blog/topics/threat-intelligence/evasive-attacker-leverages-solarwinds-supply-chain-compromises-with-sunburst-backdoor), signed with SolarWinds’ legitimate certificate, [reached 18,000 customers](https://krebsonsecurity.com/2020/12/solarwinds-hack-could-affect-18k-customers/).
* In 2023, the [3CX compromise](https://cloud.google.com/blog/topics/threat-intelligence/3cx-software-supply-chain-compromise) chained signatures end-to-end. A trojanized Trading Technologies installer ran on a 3CX employee’s machine, giving attackers a foothold inside 3CX, whose own signed installer then shipped to customers.

The CA validated a legitimate publisher, but the compromise occurred downstream of validation.

On the TLS side, in 2024 [Google announced](https://security.googleblog.com/2024/06/sustaining-digital-certificate-security.html) that Chrome would distrust new Entrust certificates, and [Mozilla followed for Firefox](https://www.theregister.com/2024/08/01/mozilla_entrust/). Both cited a multi-year pattern of compliance failures.

In September 2025, Croatian CA Fina was [found to have issued twelve unauthorized certificates](https://blog.cloudflare.com/unauthorized-issuance-of-certificates-for-1-1-1-1/) for Cloudflare’s 1.1.1.1 DNS resolver. Cloudflare’s disclosure acknowledged that its alerting systems missed the misissuance and an outside researcher caught it. Microsoft’s root store [trusted Fina](https://unmitigatedrisk.com/?p=1092), which exposed Microsoft Edge and other Windows apps relying on the OS root store.

Each failure drove a structural response:

![Which Incidents Drove Which Trends](/assets/trust-model-trends-table.1yJLIxzu_2uxsQ3.webp)

## How the trust model held up.

Repeated CA failures revealed that voluntary self-policing wasn’t enough. Web browsers became the enforcers of industry rules, regularly revoking trust from CAs that failed. [Mozilla](https://blog.mozilla.org/security/2016/10/24/distrusting-new-wosign-and-startcom-certificates/) and [Apple](https://support.apple.com/103723) distrusted WoSign and StartCom in 2016 for compliance failures, and Symantec’s 2018 distrust extended that pattern to a major CA. When Entrust drew the same response in 2024, the industry processed it without a crisis.

Nobody outside the CA could see which certificates were being issued. After DigiNotar, that gap could no longer be ignored. Google proposed [Certificate Transparency](https://en.wikipedia.org/wiki/Certificate_Transparency) in 2012 and [shipped enforcement in Chrome](https://www.thesslstore.com/blog/certificate-transparency-april-30-2018/) by 2018. Every publicly-trusted certificate now appears in append-only logs, and services such as [crt.sh](https://crt.sh/) make them queryable. That makes misissuance detectable within minutes, but only if someone watches.

Browsers checked revocation status best-effort and, by default, [proceeded even when checks failed](https://letsencrypt.org/2024/07/23/replacing-ocsp-with-crls/), leaving compromised certificates valid until natural expiration. The [CA/Browser Forum](https://cabforum.org/), a consortium of CAs and browser vendors, gradually shortened certificate validity from [60 months in 2012](https://cabforum.org/working-groups/server/baseline-requirements/faq/) to [200 days in 2026](https://www.digicert.com/blog/tls-certificate-lifetimes-will-officially-reduce-to-47-days). This limited the damage any single failure could cause.

[Certification Authority Authorization (CAA)](https://en.wikipedia.org/wiki/DNS_Certification_Authority_Authorization) gave domain owners a way to constrain certificate issuance. They can publish DNS records declaring authorized CAs, and CAs have been required to check CAA since 2017.

[Let’s Encrypt’s first decade](https://letsencrypt.org/2025/12/09/10-years/) brought mass automation, with free certificates starting in 2015. [ACME](https://en.wikipedia.org/wiki/Automatic_Certificate_Management_Environment), the certificate-automation protocol, was standardized as...