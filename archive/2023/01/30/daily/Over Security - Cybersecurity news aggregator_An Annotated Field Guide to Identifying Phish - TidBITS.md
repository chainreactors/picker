---
title: An Annotated Field Guide to Identifying Phish - TidBITS
url: https://tidbits.com/2023/01/16/an-annotated-field-guide-to-identifying-phish/
source: Over Security - Cybersecurity news aggregator
date: 2023-01-30
fetch_date: 2025-10-04T05:10:50.083890
---

# An Annotated Field Guide to Identifying Phish - TidBITS

[Skip to content](#content)

[TidBITS
TidBITS](https://tidbits.com)

Thoughtful, detailed coverage of everything Apple for 35 years
 and the [TidBITS Content Network](https://tcn.tidbits.com/apple-pros/) for Apple professionals

Menu

Enter Search

Search

[Log In](/login/)

Username or Email Address

Password

Log In
[Forgot password?](https://tidbits.com/tb-login/?action=lostpassword)

* Weekly Issues
  + [#1774: OS 26.0.1, Apple tees off on EU’s DMA, tracking iPhone camera usage with EXIF, OS 26 update predictions](https://tidbits.com/issues/1774/)
  + [#1773: macOS 26 Tahoe pushes FileVault, removes FireWire support, and snubs M3 Ultra Mac Studios; plus older OS security fixes](https://tidbits.com/issues/1773/)
  + [#1772: OS 26 released, iPhone 17 and iPhone Air, new Apple Watches, AirPods Pro 3, iPhone satellite features remain free](https://tidbits.com/issues/1772/)
  + [#1771: Apple iPhone event, Google antitrust decision, The Browser Company acquired, AI chatbot training and subscription models, publishing advice](https://tidbits.com/issues/1771/)
  + [#1770: OS security updates, Apple TV+ price increase, Apple ecosystem poll results, NMUG talk, AppleCare One issues](https://tidbits.com/issues/1770/)
  + [All Back Issues](/issues/)
* [TidBITS Talk](https://talk.tidbits.com/)
  + [Post Comments](https://talk.tidbits.com/c/comments/5)
  + [Discussions](https://talk.tidbits.com/c/tidbits-talk/6)
  + [Site Feedback](https://talk.tidbits.com/c/site-feedback/3)
  + [SlackBITS 🗣](https://join.slack.com/t/slackbits/shared_invite/zt-36src1dac-HEhPniFV4tYbRTV0IGToVw)
* Membership
  + [Benefits](https://tidbits.com/membership/benefits/)
  + [Join TidBITS!](https://tidbits.com/membership/levels/)
  + [TidBITS Members](https://tidbits.com/members/)
* Get TidBITS
  + [Email](https://tidbits.com/mailing-lists/)
  + [Apple News](https://apple.news/TjCWZPx-CS2u2x6rWr-PwkQ)
  + [Bluesky](https://bsky.app/profile/tidbits.com)
  + [Google News](https://news.google.com/publications/CAAqBwgKMKD4hgsw-ZaFAw)
  + [iOS App](https://itunes.apple.com/us/app/tidbits-news/id348629441?mt=8)
  + [Mastodon](https://mastodon.social/%40TidBITS)
  + [RSS](https://tidbits.com/feed/)
  + [YouTube](https://www.youtube.com/channel/UC6FJi0g8Dc8Ou3D1YmW8nCA)
* Categories
  + [Apple Inc.](https://tidbits.com/category/aapl/)
  + [Apple TV](https://tidbits.com/category/apple-tv/)
  + [Apple Watch](https://tidbits.com/category/apple-watch/)
  + [Artificial Intelligence](https://tidbits.com/category/artificial-intelligence/)
  + [Enterprise](https://tidbits.com/category/enterprise/)
  + [Entertainment](https://tidbits.com/category/entertainment/)
  + [Home Automation](https://tidbits.com/category/automation/)
  + [Inside TidBITS](https://tidbits.com/category/inside/)
  + [iPhone, iPad, & iOS](https://tidbits.com/category/ios/)
  + [Just for Fun](https://tidbits.com/category/fun/)
  + [Mac & macOS](https://tidbits.com/category/mac/)
  + [Mac App Updates](/watchlist)
  + [Media Creation](https://tidbits.com/category/creative/)
  + [Networking](https://tidbits.com/category/net/)
  + [Opinion](https://tidbits.com/category/opinion/)
  + [Problem Solving](https://tidbits.com/category/problem-solving/)
  + [Productivity](https://tidbits.com/category/productivity/)
  + [Security](https://tidbits.com/category/security/)
  + [Tech News](https://tidbits.com/category/tech/)
  + [Tip](https://tidbits.com/category/tip/)

[Adam Engst](https://tidbits.com/author/adam-engst-2-2/)

16 January 2023
[67
comments](#discussion)

# An Annotated Field Guide to Identifying Phish

Do you like phish? Not the band, not tasty seafood dishes, and not the pretty tropical variety. I refer instead to the intellectual challenge of identifying phishing emails that attempt to get you to reveal personal information, often including login credentials or financial details, or entice you to call a phone number where trained operators will attempt to separate you from your money.

Phishing is a big deal, with a [State of Phishing report](https://venturebeat.com/security/report-phishing-attacks-jump-61-in-2022-with-255m-attacks-detected/) from security firm SlashNext claiming that there were more than 255 million phishing attacks in 2022, a 61% increase from the year before. The [Verizon Data Breach Investigations Report](https://www.phishingbox.com/downloads/Verizon-Data-Breach-Investigations-Report-DBIR-2022.pdf) for 2022 says that only 2.9% of employees click through from phishing emails, but with billions of email addresses available to target, the raw numbers are still high.

Even before the LastPass breach (see “[LastPass Shares Details of Security Breach](https://tidbits.com/2022/12/24/lastpass-shares-details-of-connected-security-breaches/),” 24 December 2022) and the news about a [data leak containing email addresses of over 200 million Twitter users](https://www.bleepingcomputer.com/news/security/200-million-twitter-users-email-addresses-allegedly-leaked-online/), I had been noticing more phishing attempts evading Gmail’s generally effective spam filters. I don’t entirely blame Gmail for this—in many cases, I can see how the messages would be hard to catch.

In the past, many phishing attempts were obviously fake, and intentionally so. That’s because they only had to sucker people who were sufficiently inexperienced, credulous, or easily deceived that they would continue to go along with the scam. Now, however, I’m seeing phishing attempts that are more sophisticated and harder to identify quickly.

I’ve been examining phishing attempts for so long that it’s hard for me to imagine what might fool someone else, so I wanted to share some recent attempts that slipped past Gmail’s filters. For each message, I’ve called out some of the ways I identified it as phishing. I suspect that most of you will assume that you would also easily have identified the message as fake, but remember, many people move rapidly through their email without reading carefully. Perhaps my calling out of some of the hallmarks of phishing attempts can help you or the people to whom you forward this article avoid being drawn in.

## Password Reset

This phishing attempt purports to come from a system administrator in charge of my email domain and tries to lure me into clicking a button. The text isn’t very good, but the buttons are, and it’s easy to imagine someone who’s scanning too quickly clicking the button without even reading the text. But that would be a mistake!

[![Phishing email](https://tidbits.com/wp/../uploads/2023/01/Password-Reset-phishing.png)](https://tidbits.com/wp/../uploads/2023/01/Password-Reset-phishing.png)

1. The Subject line for this message is glaring to me because I know how tidbits.com is managed—I do it! So this one wasn’t going to fool me, but I could imagine someone getting a similar message that identified their domain and thinking it was from the IT department. Putting the email address in the Subject might get some people to click because it feels personalized.
2. It feels weird to me that the From line of the message is also tidbits.com. Even if an administrator had to email users about a required password reset, I would expect a name or a role to appear here.
3. The body of the message is a giveaway. The phisher clearly doesn’t know my name and is thus addressing it to my username. With additional data being leaked all the time, however, there’s no guarantee that phishers won’t start personalizing messages more thoroughly. The other problem with this text is that it doesn’t sound like it was written by a native speaker of English. There’s a difference between someone who’s just a weak writer and someone who doesn’t think in English, and the phrase “please kindly reconfirm Password” screams “non-native speaker.” (I presume that phishing attempts are localized into other languages for people in other countries, so replace “English” with whatever your native language is.)
4. These buttons are pretty good—they ...