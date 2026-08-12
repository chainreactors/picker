---
title: Signal adds an extra layer of security to make sure you're actually chatting with the right person
url: https://www.theregister.com/security/2026/08/11/signal-adds-an-extra-layer-of-security-to-make-sure-youre-actually-chatting-with-the-right-person/5286461
source: www.theregister.com - Articles
date: 2026-08-11
fetch_date: 2026-08-12T04:02:51.203171
---

# Signal adds an extra layer of security to make sure you're actually chatting with the right person

[Jump to main content](#main)

Search

TOPICS

* Security
  + [All Security](/security)
  + [Cyber-crime](/cyber_crime)
  + [Patches](/patches)
  + [Research](/research)
  + [CSO](/cso)
* Off-Prem
  + [All Off-Prem](/off_prem)
  + [Edge and IoT](/edge_iot)
  + [Channel](/channel)
  + [PaaS and IaaS](/tag/paas-iaas)
  + [SaaS](/saas)
* On-Prem
  + [All On-Prem](/on_prem)
  + [Systems](/systems)
  + [Storage](/storage)
  + [Networks](/networks)
  + [HPC](/hpc)
  + [Personal Tech](/personal_tech)
  + [Cx0](/cxo)
  + [Public Sector](/public-sector)
* Software
  + [All Software](/software)
  + [AI and ML](/tag/ai%20and%20ml)
  + [Applications](/applications)
  + [Databases](/databases)
  + [DevOps](/devops)
  + [OS Platforms](/tag/os%20platforms)
  + [Virtualization](/virtualization)
* Offbeat
  + [All Offbeat](/offbeat)
  + [Columnists](/columnists)
  + [Science](/science)
  + [BOFH](/bofh)
  + [Legal](/legal)
  + [Site News](/site_news)
  + [About Us](https://www.theregister.com/about_us)

* Special Features
  + [All Special Features](/special_features)
  + [Cloud Infrastructure Month 2026](/special_features/cloud_infrastructure_month_2026)
  + [HPE: AI Explainers](/explainer/ai-explainer)
  + [Agentic AI](/special_features/agentic_ai)
  + [The Future of the Datacenter](/special_features/future_of_the_datacenter)
  + [AWS:Reinvent](/special_features/aws_reinvent)
  + [Nvidia GTC](/special_features/nvidia_gtc)
  + [Supercomputing Month](/special_features/2025_11_supercomputing_month)
  + [Computex 2026](/special_features/computex)
  + [AI Infrastructure Month 2026](/special_features/ai_infrastructure_month_2026)
  + [The State of Storage 2026](/special_features/state_of_storage_2026)
  + [RSA Conference](/special_features/rsa)
* Vendor Voice
  + [All Vendor Voice](https://vendorvoice.theregister.com/)
  + [Modernizing Financial Services with FIS and AWS](https://vendorvoice.theregister.com/aws_fis_capital_markets/)
  + [Barco](https://vendorvoice.theregister.com/barco/)
  + [Infinidat](https://vendorvoice.theregister.com/infinidat/)
  + [Everpure](https://vendorvoice.theregister.com/everpure/)
  + [Rubrik](https://vendorvoice.theregister.com/rubrik/)
  + [Make it real with Capgemini and AWS](https://vendorvoice.theregister.com/aws_capgemini/)
  + [Money Movement Hub](https://vendorvoice.theregister.com/aws_fis/)
  + [ZTE](https://vendorvoice.theregister.com/zte_news_and_stories/)
  + [Nutanix: Scale Kubernetes. Not Chaos.](https://vendorvoice.theregister.com/nutantix_cloud_native_apps/)
  + [AWS New Horizon](https://vendorvoice.theregister.com/aws_new_horizon/)
  + [Digicert](https://vendorvoice.theregister.com/digicert)
  + [Netscout](https://vendorvoice.theregister.com/netscout)
* Resources
  + [Intelligence](https://intelligence.theregister.com)
  + [Webinars & Events](https://intelligence.theregister.com/events/list/)
  + [Newsletters](https://account.theregister.com/login?r=https%3A%2F%2Faccount.theregister.com%2Fedit%2Fnewsletter%2F)

Search

[![Go to frontpage. Logo, The Register](/view-resources/dachser2/public/theregister/logo.svg)](https://www.theregister.com)

[![Go to frontpage. Logo, The Register](/view-resources/dachser2/public/theregister/logo.svg)](https://www.theregister.com)

[![Go to frontpage. Logo, The Register](/view-resources/dachser2/public/theregister/logo.svg)](https://www.theregister.com)

* [Sign in](https://account.theregister.com/login)

* [AI](/tag/ai%20and%20ml)
* [Security](/security)
* [AWS](/tag/aws)
* [Microsoft](/tag/microsoft)
* [Developer](/tag/devops)
* [Open Source](/tag/open%20source)
* [BOFH](/tag/bofh)
* [Who, Me?](/tag/who%20me)
* [On Call](/tag/on%20call/)
* [Podcasts](/tag/kettle)

REG AD

security

# Signal adds an extra layer of security to make sure you're actually chatting with the right person

One big caveat, though: You need your contact's phone number

Brandon Vigliarolo
[Brandon
Vigliarolo](https://www.theregister.com/author/brandon-vigliarolo)
GOVERNMENT AND IT NEWS REPORTER

Published
tue 11 Aug 2026 // 22:45 UTC

Signal has introduced a new layer of security to help make sure no one has secretly interfered with your encrypted chats.

The chat app is favored by diplomats, activists, and journalists for its security. It uses end-to-end message encryption and “safety numbers” – cryptographic fingerprints associated with the keys securing a conversation – which users can compare to verify they have the expected encrypted connection with a contact.

But in theory, someone could still intercept messages by corrupting the centralized directory of accounts and posing as somebody else – a classic "man in the middle" attack. Everything would still be encrypted, just going to the wrong place.

REG AD

To fight this possibility, Signal [announced](https://signal.org/blog/automatic-key-verification/) a new feature called Automatic Key Verification (AKV) on Tuesday.

REG AD

From a user perspective, AKV is easy: Tap on a Signal contact’s profile, navigate to the “View Safety Number” screen, and tap on the “Verify automatically” button. It will then show a green checkmark to verify that the contact’s public encryption key matches what Signal’s key transparency system expects.

Behind the scenes, however, Signal has developed a new architecture for detecting whether someone has tampered with the public keys associated with an account to intercept messages, as that would require a change to the public encryption key and, in turn, the safety number that a user might not recognize.

### Ledgers and trees and third parties, oh my!

Signal described the new system as serving as a ledger of public keys in which every change a user makes to their information (e.g., linked phone number) leads to a new iteration of the ledger. Accompanying that ledger is an index, allowing Signal users to verify the information in the ledger about themselves or their contacts to make sure it hasn’t been altered by a malicious third party seeking to intercept messages. This ledger lives on an “open-source key transparency server” Signal created for the AKV process, the company said.

“When Signal users register, change their phone number or username, or re-create their account, Signal records the changes in a log tree ('the ledger') and facilitates searching through the log tree with prefix trees ('the index books'),” Signal said in the announcement.

Digging through an index is hardly automatic, however, so Signal combs the index on the user's behalf to verify the information they’re retrieving about a contact is the most up-to-date. Up-to-date doesn’t mean it’s accurate, however, which is where third-party auditors come in.

Cloudflare and security firm [Trail of Bits](https://www.theregister.com/security/2026/07/04/confidential-computings-trust-mechanism-is-broken-the-fix-may-not-exist/5266056) serve as Signal’s AKV third-party auditors, according to the announcement. Their role in the whole thing is to verify that Signal’s own key transparency server isn’t compromised.

Per the announcement, third-party auditors check the index to ensure entries don’t appear to have been altered. If those checks come out clear, the auditor signs the response to indicate that the keys being provided are the same for both users, thus eliminating the possibility of a man-in-the-middle attack.

REG AD

Yet again we have a security shortcoming, as auditors can guarantee the index and key transparency server hasn’t been tampered with, but can’t verify the accuracy of the data they contain, which is where the final part of the puzzle comes in: Monitoring.

“There are two ways for customers to interact with the ledger: looking up someone else’s address, and looking up their own,” Signal explained. “Monitoring requires Alice and Bob [your usual cryptographic placeholders] to do both of these things on a regular basis, each detecting a different kind of tampering.”

Alice and Bob are each able to monitor their own ledger entries via the Signal app, which peri...