---
title: Out Of Band Update: Cobalt Strike 4.7.2
url: https://www.cobaltstrike.com/blog/out-of-band-update-cobalt-strike-4-7-2/
source: Cobalt Strike Research and Development
date: 2022-10-18
fetch_date: 2025-10-03T20:08:01.908876
---

# Out Of Band Update: Cobalt Strike 4.7.2

[Skip to content](#content)

[![Fortra](https://static.fortra.com/fortra-global-assets/fortra-logo-full.svg)
![fortra mobile logo](https://www.cobaltstrike.com/app/themes/helpsystems/img/fortra-delta-white.svg)

![Cobalt Strike](https://www.cobaltstrike.com/app/uploads/2023/06/fta-cobalt-strike-light-1.svg)](https://www.cobaltstrike.com/)

* [Fortra.com](https://www.fortra.com/?utm_source=coresecurity.com&utm_medium=referral&utm_campaign=fortra_secondarynav_link "Fortra.com")
* [Blog](/blog "Blog")
* [Download](https://download.cobaltstrike.com/download "Download")
* [Contact Us](/contact-us "Contact Us")

## Main Navigation

* [REQUEST PRICING](/product/quote-request "REQUEST PRICING")
* [Product](/product "Product")
  + Features
    - [Beacon](https://www.cobaltstrike.com/product/features/beacon "Beacon")
    - [Malleable C2](https://www.cobaltstrike.com/product/features/malleable-c2 "Malleable C2")
    - [Interoperability](https://www.cobaltstrike.com/product/features/interoperability "Interoperability")
    - [Community](https://www.cobaltstrike.com/product/features/community "Community")
    - [Flexibility](https://www.cobaltstrike.com/product/features/flexibility "Flexibility")
    - [UDRL](https://www.cobaltstrike.com/product/features/user-defined-reflective-loader "UDRL")
    - [View More Features >](/product/features/ "View More Features >")
  + Interoperability
    - [Core Impact](https://www.cobaltstrike.com/product/core-impact "Core Impact")
    - [Outflank Security Tooling](https://www.cobaltstrike.com/product/outflank-security-tooling "Outflank Security Tooling")
  + Bundles
    - [Cobalt Strike + Core Impact](/resources/datasheets/advanced-bundle/ "Cobalt Strike + Core Impact")
    - [Cobalt Strike + Outflank Security Tooling](/resources/datasheets/red-team-bundle/ "Cobalt Strike + Outflank Security Tooling")
    - [Cobalt Strike, Core Impact, Outflank Security Tooling](/resources/datasheets/advanced-red-team-bundle/ "Cobalt Strike, Core Impact, Outflank Security Tooling")
    - [View All Product Bundles >](/product/bundles/ "View All Product Bundles >")
* [Industry](https://www.cobaltstrike.com/industry "Industry")
  + [Finance](https://www.cobaltstrike.com/industry/finance "Finance")
  + [Healthcare](https://www.cobaltstrike.com/industry/healthcare "Healthcare")
  + [Government & Public Sector](https://www.cobaltstrike.com/industry/government "Government & Public Sector ")
* [Support](/support "Support")
  + [Training](https://www.cobaltstrike.com/support/training "Training")
  + [User Manuals](https://www.cobaltstrike.com/support/user-manuals "User Manuals")
  + [Community Kit](https://cobalt-strike.github.io/community_kit/ "Community Kit")
* [Resources](/resources "Resources")
  + [Blog](/blog "Blog")
  + [Screenshots](https://www.cobaltstrike.com/resources/screenshots "Screenshots")
  + [Datasheets](/resources/type-datasheet "Datasheets")
  + [Videos](/resources/type-video "Videos")
  + [Events and Webinars](/resources/type-upcoming-event "Events and Webinars")
* [Search](#collapseSearch)

Search for:

[Home](https://www.cobaltstrike.com/) » [Blog](/blog/) » Out Of Band Update: Cobalt Strike 4.7.2

# Out Of Band Update: Cobalt Strike 4.7.2

Tuesday 17 October, 2023

Cobalt Strike 4.7.2 is now available. This is an out of band update to fix a remote code execution vulnerability that is rooted in Java Swing but which can be exploited in Cobalt Strike.

### Remote Code Execution Vulnerability

I’d like to start by giving credit to Rio Sherri ([0x09AL](https://twitter.com/0x09AL)) and Ruben Boonen ([FuzzySec](https://twitter.com/FuzzySec)) from the X-Force Red Adversary Simulation Team for their work in not only researching this vulnerability, but also sharing their findings with me and my team and helping us to mitigate it. They plan on publishing detailed information about this on [their blog](https://securityintelligence.com/posts/analysis-rce-vulnerability-cobalt-strike) later today (if their blog post isn’t live right now, check back later).

The write-up linked above goes into a tremendous amount of detail and is well worth taking the time to read. The very short version is that the underlying cause of this issue is due to Cobalt Strike’s user interface being built using the Java Swing framework. Certain components within Java Swing will automatically interpret any text as HTML content if it starts with <html>. This can be exploited using an object tag, which in turn can load a malicious payload from a webserver, which is then executed by the Cobalt Strike client. Disabling automatic parsing of html tags across the entire client was enough to mitigate this behaviour.

### Why Is There No CVE For This Vulnerability?

While the remote code execution vulnerability could be exploited in Cobalt Strike, I feel that it is important to stress that this isn’t specific to Cobalt Strike and this is the reason why we haven’t submitted a new CVE to cover it. The underlying vulnerability can be found in Java Swing and can be exploited in any Java Swing GUI that renders html, not just Cobalt Strike. We felt that there were parallels between this and the recent log4j vulnerability – thousands of applications that used log4j were vulnerable and yet there aren’t CVEs to cover every single vulnerable application. It is the same case here, although I appreciate that some people may disagree.

It goes without saying that as this is our second out of band update in a matter of weeks, we apologise for any problems that these issues may have caused. If you notice any other issues with Cobalt Strike, please refer to the [online support page](https://www.cobaltstrike.com/support/?__hstc=51647990.dfa3e15903eada2a67bc549792e40605.1691086238250.1691086238250.1691096057689.2&__hssc=51647990.8.1691096057689&__hsfp=2968214243), or report them to our [support email address](/cdn-cgi/l/email-protection#24474b464548500a475157504b5457644c414854575d57504149570a474b49). Licensed users can [run the update program](https://www.cobaltstrike.com/help-update-cobalt-strike?__hstc=51647990.dfa3e15903eada2a67bc549792e40605.1691086238250.1691086238250.1691096057689.2&__hssc=51647990.8.1691096057689&__hsfp=2968214243) to get this version, or download version 4.7.2 from scratch from [the website](https://download.cobaltstrike.com/download?__hstc=51647990.dfa3e15903eada2a67bc549792e40605.1691086238250.1691086238250.1691096057689.2&__hssc=51647990.8.1691096057689&__hsfp=2968214243). We recommend taking a copy of your existing Cobalt Strike folder before upgrading in case you need to revert to the previous version. To purchase Cobalt Strike or learn more, please [contact us](https://www.cobaltstrike.com/quote-request/?__hstc=51647990.dfa3e15903eada2a67bc549792e40605.1691086238250.1691086238250.1691096057689.2&__hssc=51647990.8.1691096057689&__hsfp=2968214243).

![Greg Darwin bio picture](https://www.cobaltstrike.com/app/uploads/2023/07/Greg-profile.jpg)

#### [Greg Darwin](https://www.cobaltstrike.com/profile/greg-darwin)

Software Development Manager

[View Profile](https://www.cobaltstrike.com/profile/greg-darwin)

TOPICS

* [Development](https://www.cobaltstrike.com/blog?_sft_cornerstone=development "Development")
* [Releases](https://www.cobaltstrike.com/blog?_sft_cornerstone=releases "Releases")

[![Fortra](https://static.fortra.com/fortra-global-assets/fortra-logo-full.svg)](https://www.fortra.com "Home")

* tel:+1-800-328-1000
* [Email Us](/cdn-cgi/l/email-protection#9ef7f0f8f1def8f1eceaecffb0fdf1f3)
* [Request Support](https://community.fortra.com/support)
* [Subscribe](https://www.fortra.com/resources/fortra-subscription-center)

* [X](https://twitter.com/_CobaltStrike?s=20)
* [Youtube](https://www.youtube.com/channel/UCXr2bT_K0WpaBrhRlhpFwdw)
* [Reddit](https://www.reddit.com/r/Fortra/)

### Footer Menu 1

* [Features](/product/features/)
  + [Beacon](/product/features/beacon)
  + [Interoperablity](/product/features/interoperability)
  + [Community](/product/features/...