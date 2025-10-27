---
title: Google Pixel Devices Shipped with Vulnerable App, Leaving Millions at Risk
url: https://thehackernews.com/2024/08/google-pixel-devices-shipped-with.html
source: The Hacker News
date: 2024-08-17
fetch_date: 2025-10-06T18:08:15.239477
---

# Google Pixel Devices Shipped with Vulnerable App, Leaving Millions at Risk

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

# [Google to Remove App that Made Google Pixel Devices Vulnerable to Attacks](https://thehackernews.com/2024/08/google-pixel-devices-shipped-with.html)

**Aug 16, 2024**Ravie LakshmananMobile Security / Software Security

[![Google Pixel](data:image/png;base64... "Google Pixel")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEj1UeRsTuiqmF4GeS4Xvwv8ft1lsCcYa8XyGCDxnc74JUN5fEob79wnvkPPlMPCWgAhOPgyGuND7TlPGOXjVVQMvET0c4LB6_WrGqSpZqZzm4kuM2NJggGDLvC7nZe8dedNGOTi6Sw4LC1bUKFvFZOsedhXnLXlknrKF4cknJA99zyKkqfcWmXFakIPXHZ2/s790-rw-e365/android.png)

A large percentage of Google's own Pixel devices shipped globally since September 2017 included dormant software that could be used to stage nefarious attacks and deliver various kinds of malware.

The issue manifests in the form of a pre-installed Android app called "Showcase.apk" that comes with excessive system privileges, including the ability to remotely execute code and install arbitrary packages on the device, according to mobile security firm iVerify.

"The application downloads a configuration file over an unsecure connection and can be manipulated to execute code at the system level," it [said](https://iverify.io/blog/iverify-discovers-android-vulnerability-impacting-millions-of-pixel-devices-around-the-world) in an analysis published jointly with Palantir Technologies and Trail of Bits.

"The application retrieves the configuration file from a single U.S.-based, AWS-hosted domain over unsecured HTTP, which leaves the configuration vulnerable and can make the device vulnerable."

[![DFIR Retainer Services](data:image/png;base64...)](https://thehackernews.uk/cloud-insight-d)

The app in question is called [Verizon Retail Demo Mode](https://www.apkmirror.com/apk/verizon-vz/verizon-store-demo-mode/verizon-store-demo-mode-retail-demo-mode-release/verizon-retail-demo-mode-retail-demo-mode-android-apk-download/) ("com.customermobile.preload.vzw"), which [requires](https://www.virustotal.com/gui/file/de45978e16344539aaea32d06fdcefcb53ccde260c7d1e61842eafb3485840b0/details) nearly three dozen different permissions based on artifacts uploaded to VirusTotal earlier this February, including location and external storage. Posts on [Reddit](https://www.reddit.com/r/AndroidQuestions/comments/4x9wuy/verizon_store_demo_mode/) and [XDA Forums](https://xdaforums.com/t/vzw-apps-on-my-phone.3748011/) show that the package has been around since August 2016.

The crux of the problem has to do with the app downloading a configuration file over an unencrypted HTTP web connection, as opposed to HTTPS, thereby opening the door for altering it during transit to the targeted phone. There is no evidence that it was ever exploited in the wild.

|  |
| --- |
| [![Google Pixel](data:image/png;base64... "Google Pixel")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhEUq5PQSspDk8uXK0fm_z_PVrI9_Zthms9VIiy62EhNqaJPtEpPbCAugitZJAPF1J35hRhhJfxbribiyW_s0cX2fD3ADTxLj8MenkwXG9jQMKZjqIPmlWq2rC_B0YN7q79ucTyR44Nk-eV3LSuGMa2m5_CZea8UsRB00p54T0mlmlozTG-RQyIvC_cfxE6/s790-rw-e365/android.png) |
| Permissions requested by the Showcase.apk app |

It's worth noting that the app is not Google-made software. Rather it's developed by an enterprise software company called Smith Micro to put the device in demo mode. It's currently not clear why third-party software is directly embedded into Android firmware, but, on background, a Google representative said the application is owned and required by Verizon on all Android devices.

The net result is that it leaves Android Pixel smartphones susceptible to adversary-in-the-middle (AitM) attacks, granting malicious actors powers to inject malicious code and spyware.

Besides running in a highly privileged context at the system level, the application "fails to authenticate or verify a statically defined domain during retrieval of the application's configuration file" and "uses unsecure default variable initialization during certificate and signature verification, resulting in valid verification checks after failure."

That said, the criticality of the shortcoming is mitigated to some extent by the fact that the app is not enabled by default, although it's possible to do so only when a threat actor has physical access to a target device and developer mode is turned on.

[![CIS Build Kits](data:image/png;base64...)](https://thehackernews.uk/platform-shield-d)

"Since this app is not inherently malicious, most security technology may overlook it and not flag it as malicious, and since the app is installed at the system level and part of the firmware image, it can not be uninstalled at the user level," iVerify said.

In a statement shared with The Hacker News, Google said it's neither an Android platform nor Pixel vulnerability, and that it's related to a package file developed for Verizon in-store demo devices. It also said the app is no longer being used.

"Exploitation of this app on a user phone requires both physical access to the device and the user's password," a Google spokesperson said. "We have seen no evidence of any active exploitation. Out of an abundance of precaution, we will be removing this from all supported in-market Pixel devices with an upcoming Pixel software update. The app is not present on Pixel 9 series devices. We are also notifying other Android OEMs."

### Update

"Physical access isn't enough," GrapheneOS maintainers [said](https://x.com/GrapheneOS/status/1824537309984985335) in a statement shared on X. "They would also need the user's password. This app does not expose any attack surface to a physical attacker for that kind of threat model. It exposes no actual attack surface that's relevant."

"In order to enable and set up this app, you already need to have more control over the device than this app is able to provide by exploiting the insecure way it fetches a configuration file."

### Pixel Update Released to Resolve Issue

Google on September 3, 2024, released its [monthly update](https://source.android.com/docs/security/bulletin/pixel/2...