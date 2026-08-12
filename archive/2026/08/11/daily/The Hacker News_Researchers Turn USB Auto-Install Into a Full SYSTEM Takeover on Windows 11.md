---
title: Researchers Turn USB Auto-Install Into a Full SYSTEM Takeover on Windows 11
url: https://thehackernews.com/2026/08/researchers-turn-usb-auto-install-into.html
source: The Hacker News
date: 2026-08-11
fetch_date: 2026-08-12T04:02:50.114480
---

# Researchers Turn USB Auto-Install Into a Full SYSTEM Takeover on Windows 11

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

# [Researchers Turn USB Auto-Install Into a Full SYSTEM Takeover on Windows 11](https://thehackernews.com/2026/08/researchers-turn-usb-auto-install-into.html)

**Swati Khandelwal**Aug 11, 2026Vulnerability / Enterprise Security

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiIoEoCsvghUx_eKGXl-WAFq7pyoOLwg_Sk9a5Ne8vX1Cb7l_DOib3wtO_5NwoogbHqFvU_VWJZd3ceL5ftpWOX5qNx5HNJCmD4_RR7GaiExk0ph2F3sp5eKPthiuTcmnDlJQyvUdkTMfxBUsIlXp_I9-qkSi4zxwVnLPb9bG-T3zFC7oFCI1Mps4VJf1s/s1700-e365/pnp.gif)

Windows Plug and Play can be abused to fetch signed vendor software for an emulated USB device and execute privileged installation components that researchers chained to SYSTEM access on a fully updated Windows 11 machine.

The same PnP path can be triggered over Remote Desktop without physical hardware when supported Plug and Play or low-level USB redirection is enabled; Microsoft says that redirection is not allowed by default.

Security researchers Alejandro Hernando and Borja Martinez described the technique in "**Plug And Pwn: Weaponizing Windows PnP Auto-Install**," research prepared for DEF CON 34.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/zero-trust-claude-d)

They built tooling to emulate arbitrary USB devices and said that, under the required conditions, an unprivileged user can turn the PnP installation path into SYSTEM code execution. Microsoft's own driver documentation describes the underlying selection step: Windows receives hardware and compatible IDs for a device and uses them to find a matching driver package.

According to the [researchers](https://plugandpwn.com/), the physical chain starts by emulating a Sierra Wireless device so Windows installs SwiService.exe, a SYSTEM service exposing a SetDNS primitive. They use it to redirect DNS, then emulate a Sony FeliCa reader whose co-installer retrieves configuration files over plaintext HTTP and derives local filenames from URL paths.

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhEGRaLy42VSUXJSxCyQIvO1KtNM6g9BGsaVVQQ29zHB3211kbm_vS7NSxuP3P2e6JqjssuLGXILS6M7a8TQm4pHkfqVqxxKrar_MMammo8MCRM9OCNYiqP3a_m5-P-8s67mOHt3IP_b0r4jIIwU5E1q79lgd5OL8V7_m5eaEB5z9Jl2vUiM8F5rjBdcpw/s1700-e365/pic-1.gif)

The researchers say a path-traversal flaw lets them place a DLL in System32; reconnecting the Sierra device then loads the planted DLL and yields SYSTEM. Their disclosed demonstration used a fully updated Windows 11 system, so the result should not be generalized to an untested Windows version range.

The remote variant replaces the physical device with synthetic USB traffic over RDP. The researchers' Python client forges a USB identity and presents a phantom Intel RealSense device, causing Windows to follow the redirected device-installation path.

They say the resulting RealSense software can be abused through a CRYPTBASE.dll search-order hijack from a user-writable installation directory, giving the authenticated low-privilege user SYSTEM code execution. Microsoft separately [documents](https://learn.microsoft.com/en-us/azure/virtual-desktop/redirection-configure-usb) that redirected low-level USB peripherals use the same driver-installation process as a physical Windows computer.

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhl7OdtjjB84PsIJKyR5HeL5HeYxeLfmH2ZfgFyGzJClRRAjEbUb0mtzqAW24pbIwyrRzd9l1Uow0Y5NdOP_alxtUR6LBpNi9nGdn68vVUNiuitW2yAweLwgu-3l3zrV176CDH1f6yh_soVUOquHmPSU4LeN1ZpVSSmkE9s_VY_FN9ZYAkxavorgs7uz48/s1700-e365/pic-2.gif)

The remote path is configuration-dependent, not a default Windows exposure. [Microsoft says](https://learn.microsoft.com/en-us/windows/client-management/mdm/policy-csp-admx-terminalserver) Remote Desktop Services does not allow supported Plug and Play and RemoteFX USB redirection by default, and its USB-redirection guidance requires Plug and Play redirection to be enabled before low-level USB forwarding works.

Administrators that do not need the feature can leave it disabled. Microsoft also provides [device-installation restrictions](https://learn.microsoft.com/en-us/windows/client-management/mdm/policy-csp-deviceinstallation) that can allow or block devices by hardware or compatible ID, device-instance ID, and setup class; on a Remote Desktop server, those policies can also affect redirected devices.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/corelight-d)

The physical chain has its own precondition: an attacker has to be able to present an emulated USB device to the target machine.

The research demonstrates abuse of a legitimate privileged installation path combined with weaknesses in signed third-party packages. The vendor-specific Sierra, Sony, and Intel exploit mechanics remain researcher findings and should stay attributed unless matching vendor material independently confirms them.

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

[endpoint security](https://thehackernews.com/search/label/endpoint%20security), [enterprise security](https://thehackernews.com/search/label/enterprise%20security), [privilege escalation](https://thehackernews.com/search/label/privilege%20escalation), [Remote Access Security](https://thehackernews.com/search/label/Remote%20Access%20Security), [Software Security](https://thehackernews.com/search/label/Software%20Security), [USB Security](https://thehackernews.com/search/label/USB%20Security), [Vulnerabilit...