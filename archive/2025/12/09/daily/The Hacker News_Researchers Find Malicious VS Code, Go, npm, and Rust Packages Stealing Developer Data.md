---
title: Researchers Find Malicious VS Code, Go, npm, and Rust Packages Stealing Developer Data
url: https://thehackernews.com/2025/12/researchers-find-malicious-vs-code-go.html
source: The Hacker News
date: 2025-12-09
fetch_date: 2025-12-10T03:23:03.180576
---

# Researchers Find Malicious VS Code, Go, npm, and Rust Packages Stealing Developer Data

#1 Trusted Cybersecurity News Platform

Followed by 5.20+ million[**](https://twitter.com/thehackersnews)
[**](https://www.linkedin.com/company/thehackernews/)
[**](https://www.facebook.com/thehackernews)

[![The Hacker News Logo](data:image/png;base64...)](/)

**

**

[** Subscribe – Get Latest News](#email-outer)

* [** Home](/)
* [** Newsletter](#email-outer)
* [** Webinars](/p/upcoming-hacker-news-webinars.html)

* [Home](/)
* [Data Breaches](/search/label/data%20breach)
* [Cyber Attacks](/search/label/Cyber%20Attack)
* [Vulnerabilities](/search/label/Vulnerability)
* [Webinars](/p/upcoming-hacker-news-webinars.html)
* [Expert Insights](https://thehackernews.com/expert-insights/)
* [Contact](/p/submit-news.html)

**

**

**

Resources

* [Webinars](/p/upcoming-hacker-news-webinars.html)
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

[![Salesforce Security Handbook](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEi4PKjL50qMNKKq6z8Ofu7tXpz51soFtMEKzX6_qMTj-_Exp3EctK0Z7KiOlubgst1DxPrrk8TgthgjViGZmg4FlcOYG8L63G_dX8731tRGkOc42mbtdMv6KDyjdNKRdCPHkhUQJmcoxcFKLcQjeILTu-wEtAOXsTp7JyWMIuP0k1RJo9sZjTo5dYL8CyFQ/s728-e100/z-dd.png)](https://thehackernews.uk/zz--header-d)

# [Researchers Find Malicious VS Code, Go, npm, and Rust Packages Stealing Developer Data](https://thehackernews.com/2025/12/researchers-find-malicious-vs-code-go.html)

**Dec 09, 2025**Ravie LakshmananMalware / Threat Analysis

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEio8tVeCj4jvHcVJWmXP6jxvW38aUyE_3XFLbB_0g-DluSuxqf0PN5g9TIWTsiAeeBYm99_RsY9Bi_lpQnOZWtfECGdtKZ36-0oVSNHgjwWIAia6bo_3_oFdMkMLWbyu7MknPOkBQ_vafKrLGCQEfbyh66vg7bIhFAUgZ9eaz_-IQSmR0uc-wqr71aDa5zD/s790-rw-e365/software-malware.jpg)

Cybersecurity researchers have discovered two new extensions on Microsoft Visual Studio Code (VS Code) Marketplace that are designed to infect developer machines with stealer malware.

The VS Code extensions masquerade as a premium dark theme and an artificial intelligence (AI)-powered coding assistant, but, in actuality, harbor covert functionality to download additional payloads, take screenshots, and siphon data. The captured information is then sent to an attacker-controlled server.

"Your code. Your emails. Your Slack DMs. Whatever's on your screen, they're seeing it too," Koi Security's Idan Dardikman [said](https://www.koi.ai/blog/the-vs-code-malware-that-captures-your-screen). "And that's just the start. It also steals your WiFi passwords, reads your clipboard, and hijacks your browser sessions."

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/filefix-d)

The names of the extensions are below -

* BigBlack.bitcoin-black (16 installs) - Removed by Microsoft on December 5, 2025
* BigBlack.codo-ai (25 installs) - Removed by Microsoft on December 8, 2025

Microsoft's list of removed extensions from the Marketplace [shows](https://github.com/microsoft/vsmarketplace/blob/main/RemovedPackages.md) that the company also removed a third package named "BigBlack.mrbigblacktheme" from the same publisher for containing malware. Dardikman told The Hacker News that the extension also contained the same malware as the other two, but noted it caused no real-world impact as it was removed quickly.

While "BigBlack.bitcoin-black" activates on every VS Code action, Codo AI embeds its malicious functionality within a working tool, thereby allowing it to bypass detection.

Earlier versions of the extensions came with the ability to execute a PowerShell script to download a password-protected ZIP archive from an external server ("syn1112223334445556667778889990[.]org") and extract from it the main payload using four different methods: Windows native Expand-Archive, .NET System.IO.Compression, DotNetZip, and 7-Zip (if installed).

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEh0O4hUCHCYm9D9MdsW1jEizTokUB3fba0-1kbrO3BZ-Yr4GkwIBxgfnHjoza2v7xVwjBrFCuRq38gv96JaE6eYDRimbc8GTRG0nbvfnegKlTdH2Y9VD0bC_xpTDjnOjP_DninfqfDa0o6yR90vG4XMnqwQROWw2KGQ8Y-fJyje2Ea_N58GntmOFVkkkcHp/s790-rw-e365/data.png)

That said, the attacker is said to have inadvertently shipped a version that created a visible PowerShell window and could have alerted the user. Subsequent iterations, however, have been found to hide the window and streamline the entire process by switching to a batch script that uses a curl command to download the executable and DLL.

The executable is the legitimate Lightshot binary that's used to load the rogue DLL ("Lightshot.dll") via DLL hijacking, which proceeds to gather clipboard contents, a list of installed apps, running processes, desktop screenshots, stored Wi-Fi credentials, and detailed system information. It also launches Google Chrome and Microsoft Edge in headless mode to grab stored cookies and hijack user sessions.

"A developer could install what looks like a harmless theme or a useful AI tool, and within seconds their WiFi passwords, clipboard contents, and browser sessions are being exfiltrated to a remote server," Dardikman said.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/zscaler-ai-event-d)

The disclosure comes as Socket said it identified malicious packages across the Go, npm, and Rust ecosystems that are capable of harvesting sensitive data -

* Go packages named "github[.]com/bpoorman/uuid" and "github[.]com/bpoorman/uid" that have been available since 2021 and typosquat trusted UUID libraries ("github[.]com/google/uuid" and "github[.]com/pborman/uuid") to [exfiltrate data](https://socket.dev/blog/malicious-go-packages-impersonate-googles-uuid-library-and-exfiltrate-data) to a paste site called dpaste when an application explicitly invokes a supposed helper function named "valid" along with the information to be validated.
* A set of [420 unique npm packages](https://socket.dev/blog/elves-on-npm) published by a likely French-speaking threat actor that follows a consistent naming pattern including "elf-stats-\*," some of which contain code to execute a reverse shell and exfiltrate files to a Pipedream endpoint.
* A Rust crate named finch-rust published by faceless, that [impersonates](https://socket.dev/blog/malicious-crate-mimicking-finch-exfiltrates-credentials) the legitimate bioinformatics tool "finch" and serves as a loader for a malicious payload through a credential-stealing package known as "sha-rust" when a developer uses the library's sketch serialization functionality.

"Finch-rust acts as a malware loader; it contains mostly legitimate code copied from the legitimate finch package but includes a single malicious line that loads and executes the sha-rust payload," Socket researcher Kush Pandya said. "This separation of concerns makes detection harder: finch-rust looks benign in isolation, while sha-rust contains the actual malware."

Found this article interesting? Follow us on [Google News](https://news.google.com/publications/CAAqLQgKIidDQklTRndnTWFoTUtFWFJvWldoaFkydGxjbTVsZDNNdVkyOXRLQUFQAQ), [Twitter](https://twitter.com/thehackersnews) and [LinkedIn](https://www.linkedin.com/company/thehackernews/) to read more exclusive content we post.

SHARE
[**](#link_share)
[**](#link_share)
[**](#link_share)
**

[...