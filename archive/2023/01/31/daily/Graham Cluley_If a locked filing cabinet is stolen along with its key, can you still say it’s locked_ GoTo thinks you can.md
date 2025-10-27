---
title: If a locked filing cabinet is stolen along with its key, can you still say it’s locked? GoTo thinks you can
url: https://grahamcluley.com/goto-backup-data-breach/
source: Graham Cluley
date: 2023-01-31
fetch_date: 2025-10-04T05:16:17.753295
---

# If a locked filing cabinet is stolen along with its key, can you still say it’s locked? GoTo thinks you can

[Skip to content](#content)

[Graham Cluley](https://grahamcluley.com/)

Cybersecurity and AI keynote speaker

[BOOK ME](/about-this-site/public-speaking/ "Book cybersecurity expert Graham Cluley to speak at your event")

[Speaking](/ "Home") · [Writing](/writing/ "Writing") · [Podcasts](/podcasts/ "The AI Fix and Smashing Security podcasts") · [Video](/video/ "Video") · [Contact](/contact/ "Contact Graham Cluley") · [About](/about-this-site/ "About Graham Cluley") · [Games](/misc/ "Games")   [🔍](/search "Search")

⁠This week's sponsor: [Browse privately with a secure VPN that safeguards your privacy. Unblock content worldwide. Get 64% Off Proton VPN.](https://grahamcluley.com/go/protonvpn/)

[ⓘ](/sponsorship/ "Learn more about sponsoring this website")

This article is more than **2 years old**

# If a locked filing cabinet is stolen along with its key, can you still say it’s locked? GoTo thinks you can

[![Graham Cluley](https://grahamcluley.com/wp-content/uploads/2023/07/cropped-cluley-250-jpeg-70x70.webp)

Graham Cluley](https://grahamcluley.com/author/grahamcluley/ "Link to other articles by Graham Cluley") @ 2:37 pm, January 30, 2023

![](/wp-content/uploads/2024/11/bluesky-icon-48-1.png "Bluesky") [@grahamcluley.com](https://bsky.app/profile/grahamcluley.com "Link to @grahamcluley.com on Bluesky")
![](/wp-content/uploads/2024/11/mastodon-icon-48.png "Mastodon") [@[email protected]](https://mastodon.green/%40gcluley "Follow @gcluley on Mastodon")

![If a locked filing cabinet is stolen along with its key, can you say it's still locked? GoTo thinks you can](https://grahamcluley.com/wp-content/uploads/2023/01/goto-730.jpeg)

Last week, GoTo (the parent company of LastPass, which has been the victim of some [recent horrendous security breaches](https://grahamcluley.com/lostpass-after-the-lastpass-hack-heres-what-you-need-to-know/) itself) [announced](https://www.goto.com/blog/our-response-to-a-recent-security-incident "Link to GoTo security notice") it had also been hacked.

Here’s part of what GoTo said:

> Our investigation to date has determined that a threat actor exfiltrated encrypted backups from a third-party cloud storage service related to the following products: Central, Pro, join.me, Hamachi, and RemotelyAnywhere.

Urk. That’s bad. Losing backups is arguably as bad as [losing your password vaults](https://grahamcluley.com/lostpass-after-the-lastpass-hack-heres-what-you-need-to-know/). But hey, good to know the backups were encrypted…

> We also have evidence that a threat actor exfiltrated an encryption key for a portion of the encrypted backups.

Oh. So when you said the backups were encrypted, you actually meant that they were encrypted *but* they could be unencrypted with ease?

To say the backups were encrypted is a bit like trying to argue that a locked box is locked, if the key to the locked box is stolen at the same time as the box.

> The affected information, which varies by product, may include account usernames, salted and hashed passwords, a portion of Multi-Factor Authentication (MFA) settings, as well as some product settings and licensing information. In addition, while Rescue and GoToMyPC encrypted databases were not exfiltrated, MFA settings of a small subset of their customers were impacted.

GoTo has apparently been forcing password resets on affected accounts and reauthorising MFA settings “out of an abundance of caution.”

[**Sign up to our free newsletter**.
Security news, advice, and tips.](/gchq-newsletter/)

Apparently the breach occurred at a third-party cloud storage service, which GoTo and the beleagured LastPass both use.

Although, no doubt, there will be questions as to whether GoTo had adequately configured the security of the cloud-based storage for its backups, there are perhaps even more questions to ask regarding how careful it was being with the encryption key for those backups.

*Found this article interesting? [Follow Graham Cluley on LinkedIn](https://www.linkedin.com/comm/mynetwork/discovery-see-all?usecase=PEOPLE_FOLLOWS&followMember=grahamcluley "Link to @grahamcluley.com on LinkedIn"), [Bluesky](https://bsky.app/profile/grahamcluley.com "Link to @grahamcluley.com on Bluesky"), or [Mastodon](https://mastodon.green/%40gcluley "Link to @gcluley@mastodon.green on Mastodon") to read more of the exclusive content we post.*

---

* [Data loss](https://grahamcluley.com/category/data-loss/)
* [Encryption](https://grahamcluley.com/category/cryptography/)

* [#backup](https://grahamcluley.com/tag/backup/)
* [#data breach](https://grahamcluley.com/tag/data-breach/)
* [#Encryption](https://grahamcluley.com/tag/encryption/)
* [#LastPass](https://grahamcluley.com/tag/lastpass/)

[![Graham Cluley](https://grahamcluley.com/wp-content/uploads/2023/07/cropped-cluley-250-jpeg-64x64.webp)](https://grahamcluley.com/author/grahamcluley/ "Link to other articles by Graham Cluley")[**Graham Cluley**](https://grahamcluley.com/author/grahamcluley/ "Link to other articles by Graham Cluley")

Graham Cluley is an award-winning [keynote speaker](/about-this-site/public-speaking/) who has given presentations around the world about cybersecurity, hackers, and online privacy. A veteran of the computer security industry since the early 1990s, he wrote the first ever version of Dr Solomon's Anti-Virus Toolkit for Windows, makes regular [media appearances](/about-this-site/media/), and hosts the popular ["The AI Fix"](https://theaifix.show) and ["Smashing Security"](https://www.smashingsecurity.com) podcasts.
Follow him on [LinkedIn](https://www.linkedin.com/comm/mynetwork/discovery-see-all?usecase=PEOPLE_FOLLOWS&followMember=grahamcluley), [Bluesky](https://bsky.app/profile/grahamcluley.com) and [Mastodon](https://mastodon.green/%40gcluley), or [drop him an email](/contact).

## You may also like...

* [![LostPass: after the LastPass hack, here’s what you need to know](https://grahamcluley.com/wp-content/uploads/2023/01/lostpass-1.jpeg)](https://grahamcluley.com/lostpass-after-the-lastpass-hack-heres-what-you-need-to-know/ "LostPass: after the LastPass hack, here’s what you need to know")

  [LostPass: after the LastPass hack, here’s what you need to know](https://grahamcluley.com/lostpass-after-the-lastpass-hack-heres-what-you-need-to-know/ "LostPass: after the LastPass hack, here’s what you need to know")
* [![LastPass has been hacked. Change your master password now](https://grahamcluley.com/wp-content/uploads/2015/06/lastpass-hack-thumb.jpeg)](https://grahamcluley.com/lastpass-hacked-change-master-password/ "LastPass has been hacked. Change your master password now")

  [LastPass has been hacked. Change your master password now](https://grahamcluley.com/lastpass-hacked-change-master-password/ "LastPass has been hacked. Change your master password now")
* [![Flaws found in LastPass password manager by security researchers](https://grahamcluley.com/wp-content/uploads/2015/11/lastpass-thumb.jpeg)](https://grahamcluley.com/flaws-lastpass-password-manager-security-researchers/ "Flaws found in LastPass password manager by security researchers")

  [Flaws found in LastPass password manager by security researchers](https://grahamcluley.com/flaws-lastpass-password-manager-security-researchers/ "Flaws found in LastPass password manager by security researchers")

## What do you think? Leave a comment [Cancel reply](/goto-backup-data-breach/#respond)

Your email address will not be published. Required fields are marked \*

Comment \*

Name \*

Email \*

Website

Δ

This site uses Akismet to reduce spam. [Learn how your comment data is processed.](https://akismet.com/privacy/)

## Podcasts

[![The AI Fix](https://grahamcluley.com/wp-content/uploads/2025/07/the-ai-fix-200.webp)

The AI Fix](https://theaifix.show "Link to The AI Fix podcast")

Hosted by Graham Cluley and Mark Stockley.

Winner of the best new podcast award in 2025.

**Latest episode:**
**["AI behaves… until it knows you’re watching"](https://theaifix.show/70)**

September...