---
title: Researchers: Weak Security Defaults Enabled Squarespace Domains Hijacks
url: https://krebsonsecurity.com/2024/07/researchers-weak-security-defaults-enabled-squarespace-domains-hijacks/
source: Over Security - Cybersecurity news aggregator
date: 2024-07-16
fetch_date: 2025-10-06T17:45:43.626618
---

# Researchers: Weak Security Defaults Enabled Squarespace Domains Hijacks

Advertisement

[![](/b-sysdig/1.png)](https://content.foleon.com/sysdig/sysdig-cloud-defense-report-2025/?utm_source=krebs-on-security&utm_medium=display&utm_campaign=aware_amer_the-right-way_na_ung_display&utm_content=AD000460_1240x110)

Advertisement

[![](/b-ninjio/10.png)](https://ninjio.com/lp46d-krebs/)

[![Krebs on Security](https://krebsonsecurity.com/wp-content/uploads/2021/03/kos-27-03-2021.jpg)](https://krebsonsecurity.com/ "Krebs on Security")

[Skip to content](#content "Skip to content")

* [Home](https://krebsonsecurity.com/)
* [About the Author](https://krebsonsecurity.com/about/)
* [Advertising/Speaking](https://krebsonsecurity.com/cpm/)

# Researchers: Weak Security Defaults Enabled Squarespace Domains Hijacks

July 15, 2024

[12 Comments](https://krebsonsecurity.com/2024/07/researchers-weak-security-defaults-enabled-squarespace-domains-hijacks/#comments)

At least a dozen organizations with domain names at domain registrar **Squarespace** saw their websites hijacked last week. Squarespace bought all assets of **Google Domains** a year ago, but many customers still haven’t set up their new accounts. Experts say malicious hackers learned they could commandeer any migrated Squarespace accounts that hadn’t yet been registered, merely by supplying an email address tied to an existing domain.

![](https://krebsonsecurity.com/wp-content/uploads/2024/07/squarespacelogin.png)

The Squarespace domain hijacks, which took place between July 9 and July 12, appear to have mostly targeted cryptocurrency businesses, including [Celer Network](https://twitter.com/CelerNetwork/status/1811394743794114866), [Compound Finance](https://twitter.com/compoundfinance/status/1811624013841727702), [Pendle Finance](https://twitter.com/pendle_fi/status/1811683909509558562), and [Unstoppable Domains](https://medium.com/%40theporpoise/our-domain-was-hijacked-heres-how-blockchain-can-prevent-this-from-happening-to-you-9b9696d80d07). In some cases, the attackers were able to redirect the hijacked domains to phishing sites set up to steal visitors’ cryptocurrency funds.

New York City-based [Squarespace](https://www.squarespace.com) purchased roughly 10 million domain names from Google Domains in June 2023, and it has been gradually migrating those domains to its service ever since. Squarespace has not responded to a request for comment, nor has it issued a statement about the attacks.

But an analysis released by security experts at [Metamask](https://metamask.io/) and [Paradigm](https://x.com/samczsun/status/1811367830564307451) finds the most likely explanation for what happened is that Squarespace assumed all users migrating from Google Domains would select the social login options — such “Continue with Google” or “Continue with Apple” — as opposed to the “Continue with email” choice.

**Taylor Monahan**, lead product manager at Metamask, said Squarespace never accounted for the possibility that a threat actor might sign up for an account using an email associated with a recently-migrated domain before the legitimate email holder created the account themselves.

“Thus nothing actually stops them from trying to login with an email,” Monahan told KrebsOnSecurity. “And since there’s no password on the account, it just shoots them to the ‘create password for your new account’ flow. And since the account is half-initialized on the backend, they now have access to the domain in question.”

What’s more, Monahan said, Squarespace did not require email verification for new accounts created with a password.

“The domains being migrated from Google to Squarespace are known,” Monahan said. “It’s either public or easily discernible info which email addresses have admin of a domain. And if that email never sets up their account on Squarespace — say because the billing admin left the company five years ago or folks just ignored the email — anyone who enters that email@domain in the squarespace form now has full access to control to the domain.”

The researchers say some Squarespace domains that were migrated over also could be hijacked if attackers discovered the email addresses for less privileged user accounts tied to the domain, such as “domain manager,” which likewise has the ability to transfer a domain or point it to a different Internet address.

![](https://krebsonsecurity.com/wp-content/uploads/2024/07/squarespaceusers.png)

Monahan said the migration has left domain owners with fewer options to secure and monitor their accounts.

“Squarespace can’t support users who need any control or insight into the activity being performed in their account or domain,” Monahan said. “You basically have no control over the access different folks have. You don’t have any audit logs. You don’t get email notifications for some actions. The owner doesn’t get email notification for actions taken by a ‘domain manager.’ This is absolutely insane if you’re used to and expecting the controls Google provides.”

The researchers have published [a comprehensive guide](https://securityalliance.notion.site/A-Squarespace-Retrospective-or-How-to-Coordinate-an-Industry-Wide-Incident-Response-fead693b66c14543a48283d85aec19ad) for locking down Squarespace user accounts, which urges Squarespace users to enable multi-factor authentication (disabled during the migration).

“Determining what emails have access to your new Squarespace account is step 1,” the help guide advises. “Most teams DO NOT REALIZE these accounts even exist, let alone theoretically have access.”

The guide also recommends removing unnecessary Squarespace user accounts, and disabling reseller access in Google Workspace.

“If you bought Google Workspace via Google Domains, Squarespace is now your authorized reseller,” the help document explains. “This means that anyone with access to your Squarespace account also has a backdoor into your Google Workspace unless you explicitly disable it by following the instructions here, which you should do. It’s easier to secure one account than two.”

**Update, July 23, 1:50 p.m. ET:** Squarespace has published [a post-mortem](https://status.squarespace.com/incidents/cw2wf55bps15) about the incident. Their statement blames the domain hijacks on “a weakness related to OAuth logins”, which Squarespace said it fixed within hours, and contradicts the findings presented by the researchers above. Here are the relevant bits from their statement:

“During this incident, all compromised accounts were using third-party OAuth. Neither Squarespace nor any third-party authentication provider made any changes to authentication as part of our migration of Google Domains to Squarespace. To be clear, the migration of domains involved no changes to multi-factor authentication before, during or after.”

“To date there is no evidence that Google Workspace accounts were or are at risk, and we have received no customer reports to this effect. As a reseller, Squarespace manages billing but customers access Workspace directly using their Google account.”

“Our analysis shows no evidence that Squarespace accounts using an email-based login with an unverified email address were involved with this attack.”

*This entry was posted on Monday 15th of July 2024 11:24 AM*

[A Little Sunshine](https://krebsonsecurity.com/category/sunshine/) [Data Breaches](https://krebsonsecurity.com/category/data-breaches/) [Latest Warnings](https://krebsonsecurity.com/category/latest-warnings/) [Web Fraud 2.0](https://krebsonsecurity.com/category/web-fraud-2-0/)

[Google Domains](https://krebsonsecurity.com/tag/google-domains/) [MetaMask](https://krebsonsecurity.com/tag/metamask/) [Paradigm](https://krebsonsecurity.com/tag/paradigm/) [Squarespace](https://krebsonsecurity.com/tag/squarespace/) [Taylor Monahan](https://krebsonsecurity.com/tag/taylor-monahan/)

Post navigation

[← Crooks Steal Phone, SMS Records for Nearly All AT&T Customers](https://krebsonsecurity.com/2024/07/hackers-steal-phone-sms-records-for-nearly-all-att-customers/)
[Global ...