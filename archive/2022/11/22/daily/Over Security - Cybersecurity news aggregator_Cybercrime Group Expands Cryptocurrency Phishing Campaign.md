---
title: Cybercrime Group Expands Cryptocurrency Phishing Campaign
url: https://pixmsecurity.com/blog/phish/cybercrime-group-expands-cryptocurrency-phishing-operation/
source: Over Security - Cybersecurity news aggregator
date: 2022-11-22
fetch_date: 2025-10-03T23:25:18.549686
---

# Cybercrime Group Expands Cryptocurrency Phishing Campaign

[![Pixm Security Logo](https://pixmsecurity.com/wp-content/themes/Divi-Child/images/pixm-logo-header-white.png)](https://pixmsecurity.com)

* [About](https://pixmsecurity.com/about/)
* [About Us](https://pixmsecurity.com/about-us/)
* [Partners](https://pixmsecurity.com/partners/)
* Resources
  + [Blog](https://pixmsecurity.com/blog/)
  + [News](/news)
* [Login](https://app.pixm.net)
* [Book a Demo](https://pixmsecurity.com/request-demo/)
* [Free Install](https://chrome.google.com/webstore/detail/pixm-phishing-protection/flomofhkchlalfciiibgbfcpolhmglai?hl=en)
* [Free Install](https://apps.apple.com/app/pixm-phishing-protection/id1622871362)
* [Free Install](https://addons.mozilla.org/en-US/firefox/addon/pixm-web/)

Have a question for us?

Contact support at support@pixm.net

[Book a Demo](/request-free-trial/)

Open Menu

## Request Your Demo

"\*" indicates required fields

### Contact Information

First Name\*

Last Name\*

Company\*

Email\*

Work Phone

CAPTCHA

Request Demo

# Cybercrime Group Expands Cryptocurrency Phishing Campaign

# Introduction

PIXM is continuing to track an active criminal group operating four campaigns targeting the users of cryptocurrency exchanges and wallets. The scammers will use an in-browser chat window to initiate a remote desktop session on the victims device, approve their own device as valid to access the users account, and then drain cryptocurrency from the victims wallet.

When PIXMs Threat Research team[first started tracking this group](https://web.archive.org/web/20221207203445/https%3A//pixmsecurity.com/blog/phish/coinbase-attacks-bypass-2fa/), they were only targeting the Coinbase exchange. Over the last 30 days, the group has increased their coverage of cryptocurrency exchanges and wallets, to now include [MetaMask,](https://web.archive.org/web/20221207203445/https%3A//metamask.io/)[Crypto.com](https://web.archive.org/web/20221207203445/https%3A//crypto.com/), [KuCoin](https://web.archive.org/web/20221207203445/https%3A//www.kucoin.com/), and [Coinbase](https://web.archive.org/web/20221207203445/https%3A//www.coinbase.com/).

A list of domains the group has used actively over the last 30 days is listed at the end of this blog post.

Phase 1: 2-Factor Relay Continued

On the new domains associated with the campaign, the 2-Factor relay interception tactic is again in use. Regardless of the credentials the user enters (if they are legitimate or not) the user will be moved to a 2-Step Verification page after clicking ‘login’ where, depending on the platform in question, will be prompted for a 2-Factor code or their phone number used to retrieve their 2-Factor code. The criminal group will first attempt to relay these credentials and 2-Factor codes to the legitimate login portal associated with the platform they are spoofing. Once the user clicks ‘verify’ they will be presented with a message telling them unauthorized activity has occurred on their account.

![](data:image/png;base64...)

*Fig: 2-Factor Relay page, similar to that of the original Coinbase campaign.*

As with the Coinbase attack this group started with, this will initiate a chat window to keep the user on the phishing page in the event the 2-Factor code fails and the threat actor needs to start a remote desktop session with the victim to continue the attack. In our experience, regardless of if the victim enters legitimate credentials or not, the group will ‘chat’ with the victim to keep them in contact should they need to resend the code or proceed to the second phase of the attack.

# Phase 2: ‘Customer Support’ Chat

For a majority of the attacks this group carries out, they will require direct interaction with the user. Their login and verification portals will, by default, produce an error regardless of the actual standing of the user’s account on the real exchange or wallet.

*![](https://web.archive.org/web/20221207203445im_/https://pixmsecurity.com/wp-content/uploads/2022/11/kucoinerror.png)*

![](https://web.archive.org/web/20221207203445im_/https://pixmsecurity.com/wp-content/uploads/2022/11/metamaskerror.png)

*Fig(s): Errors produced on a few of the login portals, which initiate a ‘customer support chat’ with the same threat actor.*

This process is intended to initiate a chat session with a member of the criminal group posing as a customer support representative from the exchange or wallet site you have visited. The criminals will use this interface to attempt to access the users if their initial credential relay failed or time expired. They will prompt the user for their username, password, and 2-Factor authentication code directly in the chat. The criminal will then take this directly to a browser on their machine and again try to access the users account. Should this also fail for any number of reasons (most common of which is that the device the attacker is using to access the victims account or wallet is not an ‘authorized device’ in the user’s profile), the attacker will proceed to phase three with the victim.

The group uses the same [tawk.to](https://web.archive.org/web/20221207203445/https%3A//www.tawk.to/)chat plugin on all of their sites, each with the same customer support representative named “Veronica”, and the same ‘AccountKey’ value for each chat window (which indicated they are all owned and operated by a single tawk.to account).

![](https://web.archive.org/web/20221207203445im_/https://pixmsecurity.com/wp-content/uploads/2022/11/tawktoAccountID.png)

*Fig: Tawk\_AccountKey value which appears the same across all domains associated with the separate campaigns.*

# Phase 3: Remote Desktop Session

If the previous phases have not succeeded in giving the criminal group access to the victims wallet, they will instruct the victim to download a remote access and control application ‘TeamViewer’. They instruct the victim that this is to help them diagnose the issue with their account directly on the users machine. Once the victim has installed TeamViewer on their device, and entered the code provided by the group, the criminal now has full control of the users device, and will guide them through the steps required to authorize their device to the users account and hijack their session.

![](https://web.archive.org/web/20221207203445im_/https://pixmsecurity.com/wp-content/uploads/2022/11/teamviewersession.png)

*Fig: Attacker initiating a remote support session on the victims device.*

The criminal has the user navigate to their email inbox associated with the crypto exchange or wallet account. They will instruct the user to login to their account on the exchange or wallet site. While the user is logging in, the attacker, who has control of the victim device, will enter a random character while the victim is entering their password, which will force it to fail. The attacker will click into the TeamViewer chat box without the victims knowledge, and ask them to enter their password again, which is just sending the password to the criminal in plain text.

*![](https://web.archive.org/web/20221207203445im_/https://pixmsecurity.com/wp-content/uploads/2022/11/teamViewertoCoinbasePassword.png)*

*Fig: Attacker tricking the victim into entering their password directly into the TeamViewer chat box.*

When the user re-authenticates the attacker will simultaneously login to the users account on their device, which will prompt a ‘device confirmation’ link to be sent to the user. The criminal will take over the user’s desktop session and send themselves, via the TeamViewer chat feature, the device confirmation link. They can now use this link to validate their own device to access the user’s account.

![](https://web.archive.org/web/20221207203445im_/https://pixmsecurity.com/wp-content/uploads/2022/11/cryptoscamdeviceconfirmation.png)

*Fig: Attacker sending themselves a device confirmation link from the wallet or cryptocurrency exchange.*

# Phase 4: Drain Funds

This phase may be initiated during any previous phase, it is only c...