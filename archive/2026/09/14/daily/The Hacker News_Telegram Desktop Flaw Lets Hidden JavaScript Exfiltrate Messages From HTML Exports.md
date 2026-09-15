---
title: Telegram Desktop Flaw Lets Hidden JavaScript Exfiltrate Messages From HTML Exports
url: https://thehackernews.com/2026/09/telegram-desktop-flaw-lets-hidden.html
source: The Hacker News
date: 2026-09-14
fetch_date: 2026-09-15T07:03:15.609182
---

# Telegram Desktop Flaw Lets Hidden JavaScript Exfiltrate Messages From HTML Exports

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

[![cybersecurity](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiHP9KRFkaxKFUKQNRU3CkfxCyJLEuIfmo6ov7iWHHRBE1ShJKfXdPvozMZMVuvOJipQ8Qbap3UBmtjKvZh-xBqLeUartPWmRuQj2W8nqdCk2_XlYLXpj15R4Du2oJ1nNVPqIuR-TwbMyPQe4gxxCcMYvUMbFO_Nin2OdhyzkJvX8Sn83aEbM1C5sgaaCqI/s728-nu-rw-lo-l85-e365/wiz-sep-d.png)](https://thehackernews.uk/claude-security-guide-d)

# [Telegram Desktop Flaw Lets Hidden JavaScript Exfiltrate Messages From HTML Exports](https://thehackernews.com/2026/09/telegram-desktop-flaw-lets-hidden.html)

**Swati Khandelwal**Sep 14, 2026Vulnerability / Data Security

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEh7YYT-Mf718wZ9kLasqkkPZ1Drw4dlLUMaHtOPuWRltuG7bOcA-d4bFr4GRmer0MMohBwgv7HFVFADi-EeDvIMcbEaJUiyn8t-iLxtR8PVRDWHLmxKnofrZgoPOH_RS7qaUkzd0Ery8Rr7oWlgoPJligCMSSywXmXdMHgzuER6M77sWisfdMOo_rqudmk/s1700-nu-rw-lo-l85-e365/telehgram.jpg)

A flaw in Telegram Desktop let a bot's message plant hidden JavaScript inside chats that users exported to HTML files, security researchers at ExPatch said in a [writeup](https://expatch.com/writeups/telegram-html-export-xss.html) published on September 12.

In Telegram, the message looked ordinary, with a link button, and the script ran only when someone opened the export file in a web browser. It could then copy every message in that file to an attacker-controlled server, or rewrite what the page displayed.

Telegram shipped [a fix](https://github.com/telegramdesktop/tdesktop/releases/tag/v7.0.1) in July, but the app update does not update files exported with earlier versions, so old HTML exports can still carry the script.

Telegram Desktop, Telegram's app for Windows, macOS, and Linux, can save a single chat or all chats from an account as HTML pages that open in a browser. Bots can attach rows of buttons under their messages, which Telegram calls inline keyboards, and the bot chooses the text shown on each button.

Until the fix, the export code wrote that button text directly into the HTML page without escaping it, the researchers Denis Rostilov and Aleksander Rostilov found.

Escaping converts characters such as < so that a browser shows them as text instead of treating them as code, and the export applied it to message text, sender names, and other fields.

A bot could therefore put a script tag in a button's text, padded with invisible characters so that the button looked empty in the Telegram Desktop build they tested.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/trust-world-update-d)

The bot does not need to be in the chat it targets. A message whose only buttons are web links keeps those buttons when it is forwarded, so any member who forwards the bot's message into a group carries the script with it, the researchers found. The message then sits in the chat's history like any other until it is deleted, and can be exported months or years later.

They reported the flaw to Telegram on June 3, two days after finding it, and say they tested it only on their own accounts and test groups. Their writeup does not claim that anyone has used the flaw against real users.

When an export file containing the message was opened, the script ran without any further click, the researchers said. It could read every message in that file, including sender names and timestamps, the chat's name, type, and member count, and the local file path, and send them all to the attacker's server.

Telegram Desktop's export code splits long exports into files of 1,000 messages each, so one file exposes at most its own contents, not the whole chat or the Telegram account.

The script could also rewrite the page. In the researchers' demonstration, it replaced the whole export with a fake Telegram "verification" form.

The same control could change dates, senders, or message text in a file being used as a record, they said. It did not change Telegram's own copy of the chat or the export file saved on disk.

The researchers rated the flaw 8.2 out of 10 on the CVSS 3.1 scale, and no score from Telegram or from the U.S. National Vulnerability Database (NVD) exists as of September 14.

Three things had to be true for the script to run: the HTML export was made using a Telegram Desktop version before the fix, the message carrying the script fell within the exported chat, and the file was opened in a browser with JavaScript enabled.

The researchers examined only Telegram Desktop's HTML export and did not address the JSON export format or the export features of Telegram's other apps.

Whether a forwarded bot message ends up in an export depends on how the export is made. Exporting a single chat from its menu includes every member's messages. A full-account export includes, by default, only the account owner's own messages in groups and channels, but all messages in one-to-one chats and chats with bots, according to the export code and [Telegram's documentation](https://core.telegram.org/import-export).

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/enterprise-ai-security-a)

The fix, [commit 8457d13a](https://github.com/telegramdesktop/tdesktop/commit/8457d13aa795fadf99c955d2a04f00ebc3c59df9) by Telegram Desktop developer John Preston, adds the missing escaping. It was written on June 30 and reached the [6.9.4 beta](https://github.com/telegramdesktop/tdesktop/releases/tag/v6.9.4) on July 3 and the 7.0.1 stable release on July 14, the first fixed versions published on GitHub. The unescaped line had been in stable releases since 4.15.1 in March 2024, about two years and four months.

* **Affected:** Telegram Desktop 4.15.1 (March 2024) through 6.9.3
* **Fixed:** 6.9.4 beta (July 3, 2026), 7.0.1 (July 14, 2026) and later

The researchers advise users to:

* Update [Telegram Desktop](https://desktop.telegram.org/) to 7.0.1 or later, or to 6.9.4 or later on the beta channel.
* After updating, export again any chats that were exported to HTML before the fix, or open the old files only with JavaScript disabled.
* Treat any HTML export made before the fix as untrusted, especially one from a large group where the origin of each message is hard to check.

Until the app is updated, there is no reason to create new HTML exports, since only exports produced by the older code carry the flaw.

As of September 14, Telegram had published no gu...