---
title: GOP Cries Censorship Over Spam Filters That Work
url: https://krebsonsecurity.com/2025/09/gop-cries-censorship-over-spam-filters-that-work/
source: Over Security - Cybersecurity news aggregator
date: 2025-09-07
fetch_date: 2025-10-02T19:47:44.336455
---

# GOP Cries Censorship Over Spam Filters That Work

Advertisement

[![](/b-sysdig/1.png)](https://content.foleon.com/sysdig/sysdig-cloud-defense-report-2025/?utm_source=krebs-on-security&utm_medium=display&utm_campaign=aware_amer_the-right-way_na_ung_display&utm_content=AD000460_1240x110)

Advertisement

[![](/b-knowbe4/37.jpg)](https://www.knowbe4.com/resources/kits/cybersecurity-awareness-month?utm_source=Krebs&utm_medium=display&utm_campaign=cybersecurityawarenessmonth&utm_content=hrm+)

[![Krebs on Security](https://krebsonsecurity.com/wp-content/uploads/2021/03/kos-27-03-2021.jpg)](https://krebsonsecurity.com/ "Krebs on Security")

[Skip to content](#content "Skip to content")

* [Home](https://krebsonsecurity.com/)
* [About the Author](https://krebsonsecurity.com/about/)
* [Advertising/Speaking](https://krebsonsecurity.com/cpm/)

# GOP Cries Censorship Over Spam Filters That Work

September 5, 2025

[68 Comments](https://krebsonsecurity.com/2025/09/gop-cries-censorship-over-spam-filters-that-work/#comments)

The chairman of the **Federal Trade Commission** (FTC) last week sent a letter to Google’s CEO demanding to know why Gmail was blocking messages from Republican senders while allegedly failing to block similar missives supporting Democrats. The letter followed media reports accusing Gmail of disproportionately flagging messages from the GOP fundraising platform **WinRed** and sending them to the spam folder. But according to experts who track daily spam volumes worldwide, WinRed’s messages are getting blocked more because its methods of blasting email are increasingly way more spammy than that of **ActBlue**, the fundraising platform for Democrats.

![](https://krebsonsecurity.com/wp-content/uploads/2025/09/nyp-google-spam.png)

On Aug. 13, **The New York Post** ran an “exclusive” [story](https://nypost.com/2025/08/13/business/google-caught-flagging-gop-fundraiser-emails-as-suspicious-sending-them-directly-to-spam-memo/) titled, “Google caught flagging GOP fundraiser emails as ‘suspicious’ — sending them directly to spam.” The story cited a memo from Targeted Victory – whose clients include the National Republican Senatorial Committee (NRSC), Rep. Steve Scalise and Sen. Marsha Blackburn – which said it observed that the “serious and troubling” trend was still going on as recently as June and July of this year.

“If Gmail is allowed to quietly suppress WinRed links while giving ActBlue a free pass, it will continue to tilt the playing field in ways that voters never see, but campaigns will feel every single day,” the memo reportedly said.

In an August 28 letter to Google CEO **Sundar Pichai**, FTC Chairman **Andrew Ferguson** cited the New York Post story and warned that Gmail’s parent **Alphabet** may be engaging in unfair or deceptive practices.

“Alphabet’s alleged partisan treatment of comparable messages or messengers in Gmail to achieve political objectives may violate both of these prohibitions under the FTC Act,” Ferguson wrote. “And the partisan treatment may cause harm to consumers.”

However, the situation looks very different when you ask spam experts what’s going on with WinRed’s recent messaging campaigns. **Atro Tossavainen** and **Pekka Jalonen** are co-founders at [Koli-Lõks OÜ](https://www.koliloks.eu/), an email intelligence company in Estonia. Koli-Lõks taps into real-time intelligence about daily spam volumes by monitoring large numbers of “spamtraps” — email addresses that are intentionally set up to catch unsolicited emails.

Spamtraps are generally not used for communication or account creation, but instead are created to identify senders exhibiting spammy behavior, such as scraping the Internet for email addresses or buying unmanaged distribution lists. As an email sender, blasting these spamtraps over and over with unsolicited email is the fastest way to ruin your domain’s reputation online. Such activity also virtually ensures that more of your messages are going to start getting listed on spam blocklists that are broadly shared within the global anti-abuse community.

Tossavainen told KrebsOnSecurity that WinRed’s emails hit its spamtraps in the .com, .net, and .org space far more frequently than do fundraising emails sent by ActBlue. Koli-Lõks published a graph of the stark disparity in spamtrap activity for WinRed versus ActBlue, showing a nearly fourfold increase in spamtrap hits from WinRed emails in the final week of July 2025.

[![](https://krebsonsecurity.com/wp-content/uploads/2025/09/koli-loks-red-v-blue.png)](https://krebsonsecurity.com/wp-content/uploads/2025/09/koli-loks-red-v-blue.png)

Image: Koliloks.eu

“Many of our spamtraps are in repurposed legacy-TLD domains (.com, .org, .net) and therefore could be understood to have been involved with a U.S. entity in their pre-zombie life,” Tossavainen explained in the LinkedIn post.

**Raymond Dijkxhoorn** is the CEO and a founding member of [SURBL](https://www.surbl.org/), a widely-used blocklist that flags domains and IP addresses known to be used in unsolicited messages, phishing and malware distribution. Dijkxhoorn said their spamtrap data mirrors that of Koli-Lõks, and shows that WinRed has consistently been far more aggressive in sending email than ActBlue.

Dijkxhoorn said the fact that WinRed’s emails so often end up dinging the organization’s sender reputation is not a content issue but rather a technical one.

“On our end we don’t really care if the content is political or trying to sell viagra or penis enlargements,” Dijkxhoorn said. “It’s the mechanics, they should not end up in spamtraps. And that’s the reason the domain reputation is tempered. Not ‘because domain reputation firms have a political agenda.’ We really don’t care about the political situation anywhere. The same as we don’t mind people buying penis enlargements. But when either of those land in spamtraps it will impact sending experience.”

The FTC letter to Google’s CEO also referenced a [debunked](https://www.techdirt.com/2022/04/11/despite-what-fox-news-tells-you-a-new-study-did-not-prove-that-gmail-is-biased-against-conservatives/) [2022 study](https://arxiv.org/pdf/2203.16743.pdf) (PDF) by political consultants who found Google caught more Republican emails in spam filters. **Techdirt** editor **Mike Masnick** notes that while the 2022 study also found that other email providers caught more Democratic emails as spam, “Republicans laser-focused on Gmail because it fit their victimization narrative better.”

Masnick said GOP lawmakers then filed both lawsuits and complaints with the **Federal Election Commission** (both of which failed easily), claiming this was somehow an “in-kind contribution” to Democrats.

“This is political posturing designed to keep the White House happy by appearing to ‘do something’ about conservative claims of ‘censorship,'” Masnick [wrote](https://www.techdirt.com/2025/09/04/ftc-chair-fergusons-ridiculous-crusade-threatening-google-over-spam-filters-that-actually-work/) of the FTC letter. “The FTC has never policed ‘political bias’ in private companies’ editorial decisions, and for good reason—the First Amendment prohibits exactly this kind of government interference.”

WinRed did not respond to a request for comment.

The WinRed website says it is an online fundraising platform supported by a united front of the Trump campaign, the **Republican National Committee** (RNC), the NRSC, and the **National Republican Congressional Committee** (NRCC).

WinRed has recently come under fire for aggressive fundraising via text message as well. In June, **404 Media** reported on [a lawsuit](https://www.404media.co/winred-texts-class-action-lawsuit-rnc-donations/) filed by a family in Utah against the RNC for allegedly bombarding their mobile phones with text messages seeking donations after they’d tried to unsubscribe from the missives dozens of times.

One of the family members said they received 27 such messages from 25 numbers, even after sending 20 stop requests. The plaintiffs in that case allege the texts...