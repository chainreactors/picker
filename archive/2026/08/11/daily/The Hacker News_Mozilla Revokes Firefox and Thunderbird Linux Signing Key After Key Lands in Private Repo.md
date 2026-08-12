---
title: Mozilla Revokes Firefox and Thunderbird Linux Signing Key After Key Lands in Private Repo
url: https://thehackernews.com/2026/08/mozilla-revokes-firefox-and-thunderbird.html
source: The Hacker News
date: 2026-08-11
fetch_date: 2026-08-12T04:02:49.839144
---

# Mozilla Revokes Firefox and Thunderbird Linux Signing Key After Key Lands in Private Repo

#1 Trusted Cybersecurity News Platform

Followed by 5.70+ million[**](https://twitter.com/thehackersnews)
[**](https://www.linkedin.com/company/thehackernews/)
[**](https://www.facebook.com/thehackernews)

[![The Hacker News Logo](data:image/png;base64...)](/)

**

**

[** Get the Latest News](#email-outer)

* [Home](/)
* [Newsletter](#email-outer)
* [Webinars](/p/upcoming-hacker-news-webinars.html)

* [Home](/)
* [Threat Intelligence](/search/label/Threat%20Intelligence)
* [Vulnerabilities](/search/label/Vulnerability)
* [Cyber Attacks](/search/label/Cyber%20Attack)
* [Webinars](/p/upcoming-hacker-news-webinars.html)
* [Expert Insights](https://thehackernews.com/expert-insights/)
* [Awards](https://awards.thehackernews.com/)

**

**

**

Resources

* [Webinars](/p/upcoming-hacker-news-webinars.html)
* [Awards](https://awards.thehackernews.com/)
* [Free eBooks](https://thehackernews.tradepub.com)

About Site

* [About THN](/p/about-us.html)
* [Jobs](/p/careers-technical-writer-designer-and.html)
* [Advertise with us](/p/advertising-with-hacker-news.html)

Contact/Tip Us

[**

Reach out to get featured—contact us to send your exclusive story idea, research, hacks, or ask us a question or leave a comment/feedback!](/p/submit-news.html)

Follow Us On Social Media

[**](https://www.facebook.com/thehackernews)
[**](https://twitter.com/thehackersnews)
[**](https://www.linkedin.com/company/thehackernews/)
[**](https://www.youtube.com/c/thehackernews?sub_confirmation=1)
[**](https://www.instagram.com/thehackernews/)

[** RSS Feeds](https://feeds.feedburner.com/TheHackersNews)
[** Email Alerts](#email-outer)

![cybersecurity](data:image/svg+xml;base64...)

# [Mozilla Revokes Firefox and Thunderbird Linux Signing Key After Key Lands in Private Repo](https://thehackernews.com/2026/08/mozilla-revokes-firefox-and-thunderbird.html)

**Swati Khandelwal**Aug 11, 2026Cryptography / Software Supply Chain

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgV1-B4O1t_ddtTQg7WCfQLhdWxNygkI3C3DHfugd_0ogZbFCixAf-J9IffSq3KuSSPDofAEj5wNrVHlzRx3qbj7cPQhbBfnvOXOAJxjTSJ_7rdtZe3ne_R4Yz7Gv_7VrNH8CyB8psfzpejy9EbohuyYW3G1pg4FChDRVv8WPxp8B449rGIXnS4WSoD5JI/s1700-e365/firefox.jpg)

Mozilla has scrapped the cryptographic key behind Firefox and Thunderbird downloads for Linux after an unencrypted copy of it was committed by mistake to one of the company's own private code repositories.

That key is how a user, or a Linux distribution packaging the browser, confirms a downloaded Firefox tarball came from Mozilla and was not tampered with.

That decision carries a cost for anyone who checks what they download: files signed with the old key stop verifying once a user imports the revocation. That covers older Firefox and Thunderbird downloads, not just future ones.

Nothing so far points to anyone outside the company getting hold of the key. The repository was private, the browser maker says a review of available audit records turned up no sign of unauthorized access, and everyone who could see it already had legitimate access anyway. Mozilla revoked it regardless.

Most Firefox and Thunderbird users need to do nothing. Two groups do. Anyone who checks signatures by hand must import the new key plus the revocation for the old one. Anyone installing Firefox from Mozilla's RPM packages may hit a failed update and have to swap the key manually.

The replacement subkey, published Monday, has the fingerprint **827E 6586 0867 9618 CD34 9F93 678E 455D 7676 7AA3** and is valid until August 5, 2028.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/zero-trust-claude-d)

OpenPGP lets a key's owner attach a machine-readable reason for pulling it, and [RFC 4880](https://www.rfc-editor.org/rfc/rfc4880.html) spells out why that matters: a key that is superseded or retired leaves its past signatures valid, while a key revoked because of compromise makes every signature it ever produced suspect.

The Hacker News decoded the revocation certificate published alongside [the new key](https://blog.mozilla.org/security/2026/08/10/updated-gpg-key-for-signing-firefox-and-thunderbird-releases/) and found reason code 2, "key material has been compromised," generated on August 6, 2026 at 11:14 UTC with the note "We no longer trust this key." Mozilla's own account of the incident stops short of saying the key was taken.

It is a subkey revocation, signed by the primary key 14F26682D0916CDD81E37B6D61B7B526D98F0353, which stays in place. Reason code 2, rather than the rotation itself, is what stops older downloads verifying, an effect Mozilla's post describes but attributes only to the nature of GPG signing.

The swap is also about seven months early. The company [rotates this subkey roughly every two years](https://blog.mozilla.org/security/2021/06/02/updating-gpg-key-for-signing-firefox-releases/), guarding against a leak it never learns about. The revoked subkey, **09BE ED63 F346 2A2D FFAB 3B87 5ECB 6497 C1A2 0256**, [announced in April 2025](https://blog.mozilla.org/security/2025/04/01/updated-gpg-key-for-signing-firefox-releases-2/), had until March 2027 to run.

We also examined the full public key [kept in Mozilla's own signing repository](https://github.com/mozilla-releng/scriptworker-scripts/blob/master/signingscript/src/signingscript/data/gpg_pubkey_prod.asc) and found five earlier signing subkeys going back to 2015, every one retired by expiry. This is the first revocation on the key.

On the RPM side, dnf on some distributions handles the change itself, fetching the updated key at the next update and asking the user to confirm the fingerprint. Elsewhere it fails outright, reporting that importing the key did not help, or that the installed repository keys are wrong for the package.

The old key has to come off first, because rpm --import can report success while leaving the stale key in place:

```
sudo rpm -e --allmatches gpg-pubkey-14f26682d0916cdd81e37b6d61b7b526d98f0353
sudo rpm --import https://packages.mozilla.org/rpm/firefox/signing-key.gpg
sudo dnf clean all
```

Thunderbird publishes no official RPM packages, so that step does not apply. openSUSE users run the same two rpm commands, then zypper refresh.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/corelight-d)

Mozilla has not said which repository held the key, how long it sat there, or how it came to light, and does not describe the safeguards it says it added. It says nothing either way about the APT repository serving Debian and Ubuntu users, which uses [a different key](https://support.mozilla.org/en-US/kb/install-firefox-linux), and .deb is not among the affected formats.

The disclosure lands a week after attackers hijacked the GitHub account behind the keyv and cacheable npm packages and published a worm [built to harvest repository, registry, cloud and private-key material](https://thehackernews.com/2026/08/keyv-linked-npm-worm-poisons-hundreds.html) from developer machines and CI pipelines.

Found this article interesting? Follow us on [Google News](https://news.google.com/publications/CAAqLQgKIidDQklTRndnTWFoTUtFWFJvWldoaFkydGxjbTVsZDNNdVkyOXRLQUFQAQ), [Twitter](https://twitter.com/thehackersnews) and [LinkedIn](https://www.linkedin.com/company/thehackernews/) to read more exclusive content we post.

SHARE
[**](#link_share)
[**](#link_share)
[**](#link_share)
**

[**Tweet](#link_share)

[**Share](#link_share)

[**Share](#link_share)

**Share

**
[**Share on Facebook](#link_share)
[**Share on Twitter](#link_share)
[**Share on Linkedin](#link_share)
[**Share on Reddit](#link_share)
[**Share on Hacker News](#link_share)
[**Share on Email](#link_share)
[**Share on WhatsApp](#link_share)
[![Facebook Messenger](data:image/png;base64...)Share on Facebook Messenger](#link_share)
[**Share on Telegram](#link_share)

SHARE **

[Application Security](https://thehackernews.com/search/label/Application%20Security), [browser sec...