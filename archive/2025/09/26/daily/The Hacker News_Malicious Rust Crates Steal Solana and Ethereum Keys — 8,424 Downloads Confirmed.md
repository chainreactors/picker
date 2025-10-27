---
title: Malicious Rust Crates Steal Solana and Ethereum Keys — 8,424 Downloads Confirmed
url: https://thehackernews.com/2025/09/malicious-rust-crates-steal-solana-and.html
source: The Hacker News
date: 2025-09-26
fetch_date: 2025-10-02T20:44:49.584521
---

# Malicious Rust Crates Steal Solana and Ethereum Keys — 8,424 Downloads Confirmed

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

[![Salesforce Security Handbook](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjWa8tsMNqlevi1HGF1ALQRGIq7hROPFAbHd3R1RTEOe73T8_Q2xW_-91t2jSGjU5peiPb8QYblGp4igNW-u2Qmlxbp2BKzTVMSvyXDZJmC-BYpiiJHrcnG5drmSP97iZ9PVIf1DeEr7U-7vWpe4HXwfMjt8FGNgq5mOycOJluYr9wF7YOKrQY9MfArwgjt/s728-e100/ai-agent-security-d.png)](https://thehackernews.uk/ai-agent-security-d)

# [Malicious Rust Crates Steal Solana and Ethereum Keys — 8,424 Downloads Confirmed](https://thehackernews.com/2025/09/malicious-rust-crates-steal-solana-and.html)

**Sep 25, 2025**Ravie LakshmananSoftware Security / Malware

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEheeB2-qigE_w1q0O91fb_WY3suGleuiLKD6d4I1712YjTGuyR_ZYH0AWl7ELaPvR5JcYqlCAXwuiJYUXR4A6TfLq-00iMwc25HSqrflxzRyAs3O2HkqDuVNC4W_WB-wxI6_rY-TPQeO_NjaQzmOe1Y8WiNMjrwOFhifAROfcxg_6NpfuC0H1yk7daVZ61l/s790-rw-e365/rust.jpg)

Cybersecurity researchers have discovered two malicious Rust crates impersonating a legitimate library called [fast\_log](https://crates.io/crates/fast_log) to steal Solana and Ethereum wallet keys from source code.

The crates, named faster\_log and async\_println, were published by the threat actor under the alias [rustguruman](https://crates.io/users/rustguruman) and [dumbnbased](https://crates.io/users/dumbnbased) on May 25, 2025, amassing 8,424 downloads in total, according to software supply chain security company Socket.

"The crates include working logging code for cover and embed routines that scan source files for Solana and Ethereum private keys, then exfiltrate matches via HTTP POST to a hardcoded command and control (C2) endpoint," security researcher Kirill Boychenko [said](https://socket.dev/blog/two-malicious-rust-crates-impersonate-popular-logger-to-steal-wallet-keys).

Following responsible disclosure, the maintainers of crates.io have taken steps to remove the Rust packages and disable the two accounts. It has also preserved logs of the threat actor-operated users along with the malicious crates for further analysis.

"The malicious code was executed at runtime, when running or testing a project depending on them," Crates.io's Walter Pearce [said](https://blog.rust-lang.org/2025/09/24/crates.io-malicious-crates-fasterlog-and-asyncprintln/). "Notably, they did not execute any malicious code at build time. Except for their malicious payload, these crates copied the source code, features, and documentation of legitimate crates, using a similar name to them."

[![DFIR Retainer Services](data:image/png;base64...)](https://thehackernews.uk/cloud-insight-d)

The typosquatting attack, as detailed by Socket, involved the threat actors retaining the logging functionality of the actual library, while introducing malicious code changes during a log packing operation that recursively searched Rust files (\*.rs) in a directory for Ethereum and Solana private keys and bracketed byte arrays and exfiltrate them to an Cloudflare Workers domain ("mainnet.solana-rpc-pool.workers[.]dev").

Besides copying fast\_log's README and setting the bogus crates' repository field to the real GitHub project, the use of "mainnet.solana-rpc-pool.workers[.]dev" is an attempt to mimic Solana's [Mainnet beta RPC endpoint](https://solana.com/docs/references/clusters) "api.mainnet-beta.solana[.]com."

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjDPrykQyOM42NiyKzICOXPJctqrXuFtZbt1RoPSKToAmaEHSybPIPA3n3R2v45mUReUJdGSOuSxjwKae9JxAK3Wpgj9gomIg6m4TdTQz8fjFMLsfhTV-mmBXmTwOklsp_MzupgGjvFAYj8UZBbS53am_RViKKeVG-hmmKiuXqhh-0xKaQfA4eK4dj2-cpI/s2600/malware.jpg)

According to crates.io, the two crates did not have any dependent downstream crates, nor did the users publish other crates on the Rust package registry. The GitHub accounts linked to the crates.io publisher accounts remain accessible as of writing. While the GitHub account [dumbnbased](https://github.com/dumbnbased) was created on May 27, 2023, [rustguruman](https://github.com/rustguruman) did not exist until May 25, 2025 – the same day the crates were uploaded.

"This campaign shows how minimal code and simple deception can create a supply chain risk," Boychenko said. "A functional logger with a familiar name, copied design, and README can pass casual review, while a small routine posts private wallet keys to a threat actor-controlled C2 endpoint. Unfortunately, that is enough to reach developer laptops and CI."

### Update

Both the GitHub accounts linked to the Rust crates are no longer available. Boychenko told The Hacker News that the malicious code does not get triggered during compilation or when the crates are downloaded, and that it only kicks in when the program executes and hits the relevant code paths.

"That lowers accidental exposure, but it is not 'low risk.' Anyone who ran code using the crates could have leaked sensitive data," the researcher added. "We have not found public projects that depend on these two crates, and the Rust registry lists no downstream crates. There were 8,424 downloads, which is meaningful for a smaller ecosystem like Rust, but downloads do not equal adopters."

*(The story was updated after publication to include a response from Socket and the latest status of the offending GitHub accounts.)*

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

[Blockchain](https://thehackernews.com/search/label/Blockchain)[cybersecurity](https://thehackernews.com/search/label/cybersecurity)[Ethereum](https://thehackernews.com/search/label/Ethereum)[Malware](https://thehackernews.com/search/label/Malware)[Rust Prog...