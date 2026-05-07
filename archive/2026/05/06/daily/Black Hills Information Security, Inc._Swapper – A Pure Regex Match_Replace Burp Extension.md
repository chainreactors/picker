---
title: Swapper – A Pure Regex Match/Replace Burp Extension
url: https://www.blackhillsinfosec.com/swapper/
source: Black Hills Information Security, Inc.
date: 2026-05-06
fetch_date: 2026-05-07T05:34:06.396120
---

# Swapper – A Pure Regex Match/Replace Burp Extension

[![Black Hills Information Security, Inc.](https://www.blackhillsinfosec.com/wp-content/uploads/2025/03/BHIS_TEXT_BHIS.png)](https://www.blackhillsinfosec.com "Black Hills Information Security, Inc.")

[RSS](https://www.blackhillsinfosec.com/feed/)

* [All Services](https://www.blackhillsinfosec.com/services/)
  + [Complete Service Guide](https://www.blackhillsinfosec.com/services/complete-service-guide/)
  + [Active SOC](https://www.blackhillsinfosec.com/services/active-soc/)
  + [AI Security Assessments](https://www.blackhillsinfosec.com/services/ai-security-assessments/)
  + [Blockchain Security](https://www.blackhillsinfosec.com/services/blockchain-security/)
  + [Blue Team Services](https://www.blackhillsinfosec.com/services/blue-team-services/)
  + [Continuous Penetration Testing](https://www.blackhillsinfosec.com/services/antisoc/)
  + [High-Profile Risk Assessments](https://www.blackhillsinfosec.com/services/high-profile-risk-assessments/)
  + [Incident Response](https://www.blackhillsinfosec.com/services/incident-response/)
  + [Penetration Testing](https://www.blackhillsinfosec.com/services/)
* [Contact Us](https://www.blackhillsinfosec.com/contact-us/)
  + [Contact Us](https://www.blackhillsinfosec.com/contact-us/)
  + [Email Sign-Up](https://mailchi.mp/blackhillsinfosec.com/bhis-sign-up)
* [About Us](https://www.blackhillsinfosec.com/who-we-are/)
  + [Security Consultants](https://www.blackhillsinfosec.com/about/security-consultants/)
  + [Admin Team](https://www.blackhillsinfosec.com/about/admin-staff/)
  + [Active SOC Team](https://www.blackhillsinfosec.com/about/soc-team/)
  + [Antisyphon Training](https://www.blackhillsinfosec.com/about/antisyphon/)
  + [BHIS Tribe of Companies](https://www.blackhillsinfosec.com/bhis-tribe-of-companies/)
* [Free Resources](https://www.blackhillsinfosec.com/free-cybersecurity-tools/)
  + [Blogs](https://www.blackhillsinfosec.com/blog/)
  + [Free Cybersecurity Tools](https://www.blackhillsinfosec.com/free-cybersecurity-tools/)
  + [Free Cybersecurity Webcasts](https://www.blackhillsinfosec.com/free_cybersecurity_webcasts/)
  + [Podcasts](https://bhispodcasts.transistor.fm/)
  + [RITA](https://www.activecountermeasures.com/free-tools/rita/)
* [Training](https://www.blackhillsinfosec.com/bhis-and-antisyphon-training/)
  + [BHIS & Antisyphon Training](https://www.blackhillsinfosec.com/bhis-and-antisyphon-training/)
  + [WWHF Conference](https://wildwesthackinfest.com)
* [Community](https://blackhillsinfosec.com/community)
  + [Discord](https://discord.gg/BHIS)
  + [LinkedIn](https://www.linkedin.com/company/black-hills-information-security/)
  + [YouTube](https://www.youtube.com/c/BlackHillsInformationSecurity/videos)
  + [Bluesky](https://bsky.app/profile/bhinfosecurity.bsky.social)
  + [Twitter/X](https://twitter.com/BHinfoSecurity)
  + [Upcoming Events](https://blackhillsinfosec.com/events)
* [Fun Stuff](https://spearphish-general-store.myshopify.com/)
  + [Backdoors & Breaches](https://www.blackhillsinfosec.com/tools/backdoorsandbreaches/)
  + [Merch, Zines & More](https://spearphish-general-store.myshopify.com/)
  + [PROMPT# Zine](https://www.blackhillsinfosec.com/prompt-zine/)
  + [REKCAH](https://www.blackhillsinfosec.com/rekcah/)
  + [Books](https://www.blackhillsinfosec.com/tools/books/)

6
May
2026

[Dave Blandford](https://www.blackhillsinfosec.com/category/author/dave-blandford/), [How-To](https://www.blackhillsinfosec.com/category/how-to/), [Informational](https://www.blackhillsinfosec.com/category/informational/), [Mobile](https://www.blackhillsinfosec.com/category/red-team/mobile/), [Web App](https://www.blackhillsinfosec.com/category/red-team/web-app/)
[Burp extensions](https://www.blackhillsinfosec.com/tag/burp-extensions/), [Desktop App Testing](https://www.blackhillsinfosec.com/tag/desktop-app-testing/), [Mobile App Testing](https://www.blackhillsinfosec.com/tag/mobile-app-testing/), [Regex](https://www.blackhillsinfosec.com/tag/regex/), [Web App Testing](https://www.blackhillsinfosec.com/tag/web-app-testing/)

# [Swapper – A Pure Regex Match/Replace Burp Extension](https://www.blackhillsinfosec.com/swapper/)

![](https://www.blackhillsinfosec.com/wp-content/uploads/2024/10/DBlandford-150x150.png)

| [Dave Blandford](https://www.blackhillsinfosec.com/team/david-blandford/)

*Penetration Tester. Developer. Pure GNU/Linux Phone Enthusiast*.

![](https://www.blackhillsinfosec.com/wp-content/uploads/2026/05/swapper_header.png)

There are a thousand (rough guess) different ways in Burp Suite to swap out session token values when using something like Intruder or the Scanner. But what about the edge cases? Recently, I tested an application that used SOAP-based XML requests. The session token was only used once; each request set a new session token and invalidated the old session token, which makes using Burp Suite tools like Intruder rather difficult. (Good luck using Match and Replace for that!) And… there are extensions (which shall remain nameless) out there that specifically state they handle XML, but they don’t.

To get a valid session token to use with Burp Suite tools, I ended up writing a small Python extension (110 lines of code, but who’s counting?) that obtained a new session token for each request, allowing items like Intruder to work as intended. Cool, I was able to use it during the test, but I would like this to be repeatable. So, this blog is releasing **Swapper**, a regex pattern-based match/replace Burp Suite extension.

## Easy to Install

**Install from the Bapp Store here:** <https://portswigger.net/bappstore/0077e9930f0147679b6c5ddbedac52be>

**Or download from here:** <https://github.com/roidrage52/SWAPPER>

![](https://www.blackhillsinfosec.com/wp-content/uploads/2026/05/Swapper_01.png)

Burp Suite needs the Python environment configured. Ensure you have Jython configured for your environment (more information on that here: <https://portswigger.net/burp/documentation/desktop/extend-burp/extensions/troubleshooting#you-need-to-configure-jython-or-jruby>). Add the reference to the Jython JAR file in the Extensions settings.

From the Extensions settings, in the Installed tab, select add and choose Python as the extension type. Then load swapper.py. That’s all there is.

## Easy(ish) to Use

In Burp Suite, select the request that returns the response that contains the value we want to use. Right-click on the request and select “Send to SWAPPER”. This will populate the headers and body in Swapper.

![](https://www.blackhillsinfosec.com/wp-content/uploads/2026/05/Swapper_02.png)

That will populate the SWAPPER configuration tile.

![](https://www.blackhillsinfosec.com/wp-content/uploads/2026/05/Swapper_03.png)

Next is setting up the regex…

## Regex Pattern Matching

If I could travel back in time and talk to myself as an 8th grader, the conversation would somehow be centered around, “You will grow up and use regex everyday of your adult life.” Regex is used to match both the value obtained in the response (the session token, CSRF token) and to find applicable areas in the request to swap out. In Swapper, define your regex patterns inside the “Regex Configuration”.

![](https://www.blackhillsinfosec.com/wp-content/uploads/2026/05/Swapper_04.png)

The “Response Regex” field is where you define the value to pull from the response. The pattern that is matched here will be used later in the “Replacement” field, which is the {token} field. The “Request Regex” field is where you define what values to match in the requests sent (as defined in the Extension Control settings). And lastly, the “Replacement” field is what replaces the match from the “Request Regex”. Again, use {token} to add the value obtained from the Response.

You can test your regex patterns in the extension with the “Test Token Request” feature.

![](https://www.blackhillsinfosec.com/wp-content/uploads/2026/05/Swapper_05.png)

The “Response Regex” regex matched the JWT.

Handles multiple values — That is all. If ...