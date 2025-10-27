---
title: Crooks Bypassed Google’s Email Verification to Create Workspace Accounts, Access 3rd-Party Services
url: https://krebsonsecurity.com/2024/07/crooks-bypassed-googles-email-verification-to-create-workspace-accounts-access-3rd-party-services/
source: Krebs on Security
date: 2024-07-27
fetch_date: 2025-10-06T17:52:33.661516
---

# Crooks Bypassed Google’s Email Verification to Create Workspace Accounts, Access 3rd-Party Services

Advertisement

[![](/b-sysdig/1.png)](https://content.foleon.com/sysdig/sysdig-cloud-defense-report-2025/?utm_source=krebs-on-security&utm_medium=display&utm_campaign=aware_amer_the-right-way_na_ung_display&utm_content=AD000460_1240x110)

Advertisement

[![](/b-sysdig/2.png)](https://content.foleon.com/sysdig/sysdig-cloud-defense-report-2025/?utm_source=krebs-on-security&utm_medium=display&utm_campaign=aware_amer_the-right-way_na_ung_display&utm_content=AD000462_1240x160)

[![Krebs on Security](https://krebsonsecurity.com/wp-content/uploads/2021/03/kos-27-03-2021.jpg)](https://krebsonsecurity.com/ "Krebs on Security")

[Skip to content](#content "Skip to content")

* [Home](https://krebsonsecurity.com/)
* [About the Author](https://krebsonsecurity.com/about/)
* [Advertising/Speaking](https://krebsonsecurity.com/cpm/)

# Crooks Bypassed Google’s Email Verification to Create Workspace Accounts, Access 3rd-Party Services

July 26, 2024

[13 Comments](https://krebsonsecurity.com/2024/07/crooks-bypassed-googles-email-verification-to-create-workspace-accounts-access-3rd-party-services/#comments)

**Google** says it recently fixed an authentication weakness that allowed crooks to circumvent the email verification required to create a **Google Workspace** account, and leverage that to impersonate a domain holder at third-party services that allow logins through Google’s “Sign in with Google” feature.

![](https://krebsonsecurity.com/wp-content/uploads/2024/07/signinwithgoogle.png)

Last week, KrebsOnSecurity heard from a reader who said they received a notice that their email address had been used to create a potentially malicious Workspace account that Google had blocked.

“In the last few weeks, we identified a small-scale abuse campaign whereby bad actors circumvented the email verification step in our account creation flow for Email Verified (EV) Google Workspace accounts using a specially constructed request,” the notice from Google read. “These EV users could then be used to gain access to third-party applications using ‘Sign In with Google’.”

In response to questions, Google said it fixed the problem within 72 hours of discovering it, and that the company has added additional detection to protect against these types of authentication bypasses going forward.

**Anu Yamunan**, director of abuse and safety protections at Google Workspace, told KrebsOnSecurity the malicious activity began in late June, and involved “a few thousand” Workspace accounts that were created without being domain-verified.

Google Workspace offers a free trial that people can use to access services like Google Docs, but other services such as Gmail are only available to Workspace users who can validate control over the domain name associated with their email address. The weakness Google fixed allowed attackers to bypass this validation process. Google emphasized that none of the affected domains had previously been associated with Workspace accounts or services.

“The tactic here was to create a specifically-constructed request by a bad actor to circumvent email verification during the signup process,” Yamunan said. “The vector here is they would use one email address to try to sign in, and a completely different email address to verify a token. Once they were email verified, in some cases we have seen them access third party services using Google single sign-on.”

Yamunan said none of the potentially malicious workspace accounts were used to abuse Google services, but rather the attackers sought to impersonate the domain holder to other services online.

In the case of the reader who shared the breach notice from Google, the imposters used the authentication bypass to associate his domain with a Workspace account. And that domain was tied to his login at several third-party services online. Indeed, the alert this reader received from Google said the unauthorized Workspace account appears to have been used to sign in to his account at **Dropbox**.

Google said the now-fixed authentication bypass is unrelated to a recent issue involving cryptocurrency-based domain names that were [apparently compromised in their transition to Squarespace](https://krebsonsecurity.com/2024/07/researchers-weak-security-defaults-enabled-squarespace-domains-hijacks/), which last year acquired more than 10 million domains that were registered via Google Domains.

On July 12, a number of domains tied to cryptocurrency businesses were hijacked from Squarespace users who hadn’t yet set up their Squarespace accounts. Squarespace has since published [a statement](https://status.squarespace.com/incidents/cw2wf55bps15) blaming the domain hijacks on “a weakness related to OAuth logins”, which Squarespace said it fixed within hours.

*This entry was posted on Friday 26th of July 2024 05:31 PM*

[A Little Sunshine](https://krebsonsecurity.com/category/sunshine/) [Latest Warnings](https://krebsonsecurity.com/category/latest-warnings/) [Web Fraud 2.0](https://krebsonsecurity.com/category/web-fraud-2-0/)

[Anu Yamunan](https://krebsonsecurity.com/tag/anu-yamunan/) [Dropbox](https://krebsonsecurity.com/tag/dropbox/) [google](https://krebsonsecurity.com/tag/google/) [Google Workspace](https://krebsonsecurity.com/tag/google-workspace/) [sign in with Google](https://krebsonsecurity.com/tag/sign-in-with-google/) [Slack](https://krebsonsecurity.com/tag/slack/) [Squarespace](https://krebsonsecurity.com/tag/squarespace/)

Post navigation

[← Phish-Friendly Domain Registry “.top” Put on Notice](https://krebsonsecurity.com/2024/07/phish-friendly-domain-registry-top-put-on-notice/)
[Don’t Let Your Domain Name Become a “Sitting Duck” →](https://krebsonsecurity.com/2024/07/dont-let-your-domain-name-become-a-sitting-duck/)

## 13 thoughts on “Crooks Bypassed Google’s Email Verification to Create Workspace Accounts, Access 3rd-Party Services”

1. zuo [July 26, 2024](https://krebsonsecurity.com/2024/07/crooks-bypassed-googles-email-verification-to-create-workspace-accounts-access-3rd-party-services/#comment-612557)

   what Google says is simply not true. Attacks started around early June. I write here as one of the victims from that time. Even more – have a buganizer ticket numer from June the 7th with initial findings. It was fixed about month later.
2. Paul B [July 26, 2024](https://krebsonsecurity.com/2024/07/crooks-bypassed-googles-email-verification-to-create-workspace-accounts-access-3rd-party-services/#comment-612559)

   I’ve had several bogus workplace trials started for my personal domains and had to dig to discover how to shut them down. The flaw is that no verification is required to sign up and start the trial. The trial will expire without control of the domain DNS entries but they should never allow it to even start if you can’t confirm via an in-domain email. This is kindergarten-level security but Google is more interested in making it easy to get hooked in. I have no idea what those first days of free trial allows them to do but it shouldn’t even be a question. I get a ‘thanks for signing up’ email that has no link to abort the fraudulent signup or to require a verification of any sort. Maybe that was pen testing that led to this breach or maybe it was amateurs hoping to cash in somehow. Google=evil.

   Krebs, please give them hell for this!
3. David Keaton [July 27, 2024](https://krebsonsecurity.com/2024/07/crooks-bypassed-googles-email-verification-to-create-workspace-accounts-access-3rd-party-services/#comment-612613)

   The problem started much earlier than advertised. Two separate bad actors created bogus Google Workspace (and its predecessor Google Apps) accounts for my domain in 2012 and again in July, 2023. The first time, I took over the account by proving I owned the domain, and then eventually shut the account down. The second time, I decided not to shut the account down after taking it over, to prevent a third time.

   The second time, Google had “improved” its security so that I had a devil of ...