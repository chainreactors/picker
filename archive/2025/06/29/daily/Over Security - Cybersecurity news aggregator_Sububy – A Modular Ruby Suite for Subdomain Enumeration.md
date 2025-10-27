---
title: Sububy – A Modular Ruby Suite for Subdomain Enumeration
url: https://www.darknet.org.uk/2025/06/sububy-a-modular-ruby-suite-for-subdomain-enumeration/
source: Over Security - Cybersecurity news aggregator
date: 2025-06-29
fetch_date: 2025-10-06T22:54:00.130666
---

# Sububy – A Modular Ruby Suite for Subdomain Enumeration

* [Skip to main content](#genesis-content)
* [Skip to primary sidebar](#genesis-sidebar-primary)
* [Skip to footer](#genesis-footer-widgets)

* [Home](https://www.darknet.org.uk/)
* [About Darknet](https://www.darknet.org.uk/about/)
* [Hacking Tools](https://www.darknet.org.uk/category/hacking-tools/)
* [Popular Posts](https://www.darknet.org.uk/popular-posts/)
* [Darknet Archives](https://www.darknet.org.uk/darknet-archives/)
* [Contact Darknet](https://www.darknet.org.uk/contact-darknet/)
  + [Advertise](https://www.darknet.org.uk/contact-darknet/advertise/)
  + [Submit a Tool](https://www.darknet.org.uk/contact-darknet/submit-a-tool/)

[![Darknet – Hacking Tools, Hacker News & Cyber Security](data:image/svg+xml...)![Darknet – Hacking Tools, Hacker News & Cyber Security](https://www.darknet.org.uk/wp-content/uploads/2022/12/cropped-darknet_2022_logo.png)](https://www.darknet.org.uk/)

Darknet - Hacking Tools, Hacker News & Cyber Security

Darknet is your best source for the latest hacking tools, hacker news, cyber security best practices, ethical hacking & pen-testing.

# Sububy – A Modular Ruby Suite for Subdomain Enumeration

June 27, 2025

Views: 368

Sububy is an all-in-one subdomain enumeration tool written in Ruby by A3h1nt. It focuses on modularity and accurate discovery, making it useful for red team reconnaissance, OSINT workflows, and bug bounty triage.

![Sububy - A Modular Ruby Suite for Subdomain Enumeration](data:image/svg+xml...)![Sububy - A Modular Ruby Suite for Subdomain Enumeration](https://www.darknet.org.uk/wp-content/uploads/2025/06/Sububy-A-Modular-Ruby-Suite-for-Subdomain-Enumeration-640x427.jpeg)

### What It Does

Sububy includes ten core modules:

* **Cert** – uses Certificate Transparency logs
* **Brute** – performs wordlist-based brute force
* **Dnsd** – queries DnsDumpster (API key required)
* **Vtotal** – retrieves data from VirusTotal (API key required)
* **WebArch** – extracts historical domains from the Wayback Machine
* **Csp** – scrapes subdomains from Content Security Policy headers
* **Sort** – removes duplicates from output
* **Live** – checks for live web services
* **Sshot** – captures screenshots of live targets
* **Info** – collects HTTP response codes and headers

Modules can be run individually or chained together via CLI or from within Ruby itself.

### Installation and Usage

git clone https://github.com/A3h1nt/Sububy.git
cd Sububy
bundle install

|  |  |
| --- | --- |
| 1  2  3 | git clone https://github.com/A3h1nt/Sububy.git  cd Sububy  bundle install |

Run a full scan:

ruby Sububy.rb example.com cert brute dnsd vtotal webarch csp

|  |  |
| --- | --- |
| 1 | ruby Sububy.rb example.com cert brute dnsd vtotal webarch csp |

### Strengths

* Modular and scriptable
* Useful API integrations
* Screenshot and HTTP response data for post-enum triage
* Suitable for headless workflows via IRB or CLI
* Lightweight dependency set (Ruby + gems)

### Limitations

* Ruby is required, which may not be preinstalled in many environments
* API limits apply for Dnsd and Vtotal modules
* Focuses more on precision than volume (not a replacement for massdns)
* No built-in JSON output or API for direct integration

### When to Use It

Sububy is ideal for:

* Reconnaissance in stealth-focused environments
* Bug bounty triage for live hosts and headers
* Adding contextual intelligence (e.g. screenshots, CSP leaks)
* Workflow integration with other Ruby-based tools

Use Sububy when you want more than just domain names—particularly when you need to verify what’s alive, what’s misconfigured, or what headers are exposed.

### Recommendations

* Integrate Sububy into a larger recon pipeline by chaining outputs to Nmap or HTTP probing tools
* Use the Sort and Live modules after any brute force or CT scan to reduce noise
* Consider saving screenshots and headers for post-assessment analysis or reporting
* Pair with assetfinder or amass to compare coverage across passive sources

You can read more or download Sububy here: <https://github.com/A3h1nt/Sububy>

## Related Posts:

* [Leveraging OSINT from the Dark Web - A Practical How-To](https://www.darknet.org.uk/2025/07/leveraging-osint-from-the-dark-web-a-practical-how-to/)
* [Argus - Ultimate Reconnaissance Toolkit for…](https://www.darknet.org.uk/2025/07/argus-ultimate-reconnaissance-toolkit-for-offensive-recon-operations/)
* [Domained - Multi Tool Subdomain Enumeration](https://www.darknet.org.uk/2019/01/domained-multi-tool-subdomain-enumeration/)
* [Sublist3r - Fast Python Subdomain Enumeration Tool](https://www.darknet.org.uk/2017/12/sublist3r-fast-python-subdomain-enumeration-tool/)
* [An Introduction To Web Application Security Systems](https://www.darknet.org.uk/2016/08/an-introduction-to-web-application-security-systems/)
* [Force Push Scanner - Hunt GitHub Dangling Commits…](https://www.darknet.org.uk/2025/07/force-push-scanner-hunt-github-dangling-commits-for-leaked-secrets/)

[Share](https://www.facebook.com/share.php?u=https%3A%2F%2Fwww.darknet.org.uk%2F2025%2F06%2Fsububy-a-modular-ruby-suite-for-subdomain-enumeration%2F)

[Tweet](https://twitter.com/intent/tweet?text=Sububy+-+A+Modular+Ruby+Suite+for+Subdomain+Enumeration&url=https%3A%2F%2Fwww.darknet.org.uk%2F2025%2F06%2Fsububy-a-modular-ruby-suite-for-subdomain-enumeration%2F)

[Share](https://www.linkedin.com/cws/share?url=https%3A%2F%2Fwww.darknet.org.uk%2F2025%2F06%2Fsububy-a-modular-ruby-suite-for-subdomain-enumeration%2F)

[Buffer](https://bufferapp.com/add?url=https%3A%2F%2Fwww.darknet.org.uk%2F2025%2F06%2Fsububy-a-modular-ruby-suite-for-subdomain-enumeration%2F&text=Sububy+-+A+Modular+Ruby+Suite+for+Subdomain+Enumeration)

[WhatsApp](https://api.whatsapp.com/send?text=https%3A%2F%2Fwww.darknet.org.uk%2F2025%2F06%2Fsububy-a-modular-ruby-suite-for-subdomain-enumeration%2F)

[Email](/cdn-cgi/l/email-protection#5a65292f38303f392e67092f382f38237f686a777f686a1b7f686a17353e2f363b287f686a082f38237f686a092f332e3f7f686a3c35287f686a092f383e35373b33347f686a1f342f373f283b2e3335347c38353e2367092f382f38237f686a33297f686a3b7f686a37353e2f363b287f686a082f382377383b293f3e7f686a292f383e35373b33347f686a3f342f373f283b2e3335347f686a2e3535367f686a3c35287f686a150913140e7f68197f686a283f3e7f686a2e3f3b3733343d7f68197f686a3b343e7f686a382f3d7f686a38352f342e237f686a283f393534343b3329293b34393f747f686a133439362f3e3f297f686a393f282e7f68197f686a38282f2e3f7f68197f686a1b0a137f68197f686a3b343e7f686a2939283f3f342932352e7f686a37353e2f363f29747f6a1e7f6a1b7f6a1e7f6a1b083f3b3e7a1735283f7a123f283f607a7f686a322e2e2a297f691b7f681c7f681c2d2d2d743e3b2831343f2e7435283d742f317f681c686a686f7f681c6a6c7f681c292f382f3823773b7737353e2f363b2877282f382377292f332e3f773c352877292f383e35373b3334773f342f373f283b2e3335347f681c)

Filed Under: [Hacking Tools](https://www.darknet.org.uk/category/hacking-tools/) Tagged With: [enumeration](https://www.darknet.org.uk/tag/enumeration/), [subdomain enumeration](https://www.darknet.org.uk/tag/subdomain-enumeration/)

## Primary Sidebar

### Search Darknet

Search the site ...

* [Email](https://www.darknet.org.uk/contact-darknet/)
* [Facebook](https://www.facebook.com/darknet.org.uk/)
* [LinkedIn](https://www.linkedin.com/company/25076296/)
* [RSS](https://www.darknet.org.uk/feed/)
* [Twitter](https://x.com/THEdarknet)

**[Advertise on Darknet](https://www.darknet.org.uk/contact-darknet/advertise/)**

### Latest Posts

[![RustRedOps - Rust Native Offensive Toolkit Collection for Red Teams](data:image/svg+xml...)![RustRedOps - Rust Native Offensive Toolkit Collection for Red Teams](https://www.darknet.org.uk/wp-content/uploads/2025/10/RustRedOps-Rust-Native-Offensive-Toolkit-Collection-for-Red-Teams-100x100.jpg)](https://www.darknet.org.uk/2025/10/rustredops-rust-native-offensive-toolkit-collection-for-red-teams/)

#### [RustRedOps – Rust Native Offensive Toolkit Collection for Red Teams](https://www.darknet.org.uk/2025/10/rustredops-rust-native-offensive-toolkit-collection-for-red-teams/)

Views: 53

RustRedOps is a curated...