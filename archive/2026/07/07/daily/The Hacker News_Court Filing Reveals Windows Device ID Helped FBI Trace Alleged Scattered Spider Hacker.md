---
title: Court Filing Reveals Windows Device ID Helped FBI Trace Alleged Scattered Spider Hacker
url: https://thehackernews.com/2026/07/court-filing-reveals-windows-device-id.html
source: The Hacker News
date: 2026-07-07
fetch_date: 2026-07-08T05:05:52.948391
---

# Court Filing Reveals Windows Device ID Helped FBI Trace Alleged Scattered Spider Hacker

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

[![cybersecurity](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgrKWHErc__Wn0forfQ5eJ5sIR1hVKCHCTeNQOaAX4lbygJ8S1Xpemx6JXl78dpwiT65DDBGURp48A3EemKzmli-jXPI3v1928MnJm-1j2ZPUaFXCvuySFhyphenhyphenKR-Li6fAinFT2bhLgsqUSNUR_ggMAnOHi3jD1qYWHXvueX8WdtxAd6GYety9cBGYABo18hX/s728-e100/tt-d.jpg)](https://thehackernews.uk/ai-zero-trust-h-d)

# [Court Filing Reveals Windows Device ID Helped FBI Trace Alleged Scattered Spider Hacker](https://thehackernews.com/2026/07/court-filing-reveals-windows-device-id.html)

**Swati Khandelwal**Jul 07, 2026Cybercrime / Law Enforcement

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiRD_854zsswRvh7xWklnbEkAjmk7UZy_-dQzlueMbq1ib7deDs-QH0av7XRZ1WEq3vcX57cDDcioIdkebKCiF7qr8xC9Evw7GmFuDS0kQt3mnpXgb3Q2H62eHPIgCy3rk1Mj3uM-Mge0XTfMgSCGaumk3i5KatoyrFnu_PUhg8cZGY1ZAd185qsNqZ1jE/s1700-e365/md-id.jpg)

U.S. prosecutors linked an alleged Scattered Spider hacker to a break-in at a luxury jewelry retailer using a persistent Windows device ID, according to a newly unsealed [federal complaint](https://www.justice.gov/usao-ndil/media/1450651/dl?inline).

Microsoft records tied that ID first to the account the attackers used to keep access during the May 2025 intrusion, then to online accounts prosecutors say belong to 19-year-old Peter Stokes.

Stokes is charged with conspiracy, computer intrusion, and fraud. A dual U.S.-Estonian citizen known online as "Bouquet," he was [extradited from Finland](https://www.justice.gov/usao-ndil/pr/alleged-member-criminal-cyber-hacking-group-scattered-spider-arrested-finland-and) and made his first court appearance in Chicago on June 30, [as THN reported](https://thehackernews.com/2026/07/19-year-old-scattered-spider-suspect.html). He is presumed innocent pending trial.

## How the break-in worked

Between May 12 and 15, 2025, attackers phoned the retailer's IT help desk from Google Voice numbers, posed as locked-out employees, and got staff to reset employees' passwords and the mobile devices tied to their multifactor authentication.

Within a few hours, they controlled three accounts, two belonging to IT administrators. They installed ngrok and a second tunneling tool called Teleport, moved data to Amazon cloud storage, and pulled out at least 77 gigabytes.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/ai-vuln-protection-d)

They appear to have tried to deploy ransomware, but the retailer's security team blocked it and evicted them from the network. The attackers still sent a ransom email, subject line "IMPORTANT: WE STOLE THE DATA, CONTACT UMMEDIATELY [sic]," and later asked for $8 million in cryptocurrency. The company did not pay. The breach still cost it about $2 million in disruption, investigation, and cleanup.

The way in was the help desk, not a software flaw. The fix is a process, not patching: verify identity before any reset with a callback to a number already on file, manager sign-off, or video checks for privileged accounts. Phishing-resistant MFA like FIDO2 keys blunts the group's other methods, but does nothing if a help desk will reset an account on a phone call.

## The ID that led investigators to Stokes

Investigators worked back to Stokes from the device that opened the ngrok account. Microsoft told the FBI it carried Global Device Identifier g:6755467234350028, which Microsoft describes as a persistent identifier tied to a single Windows installation, one that survives operating-system updates but changes when Windows is reinstalled.

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgFbYa32joF8DOReh1321F01AkruM0FzkBpvyrqiWZidt4076Hx3p3jMX0en8hWebNvDixi9vyHxB0GemIv8aeMCzV-836MeIdbXFFvu_SwmqSMBOgv10RQeqFvQqHT1j0M4GM34EWbms6CsUT0rk9ErCb5PCN6XCx2O6A8YVGzd4iubYz0aAeoveGFNrg/s1700-e365/case-1.jpg)

Microsoft records show that the device visited the ngrok signup page at 19:21 UTC on May 12, 2025, the same minute the ngrok account was created, and reached the retailer's website through the same proxy about three hours later.

The device also kept surfacing on the same IP addresses, at the same times, as Snapchat, Apple, and Facebook accounts prosecutors attribute to Stokes: an address in his home city of Tallinn, Estonia, in June 2024, then New York in November and Thailand in February 2025, matched by State Department travel records.

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEi_tqLsbsXI2iGH_g6wI_7XoBW1ytj2Ve1cr4CEnwccqV0NlQTUKV8w5onVvSQZZJodoYBWkJFyVwPvH5k_2T6a8TDn0yqe-AD0INEyLCrwZdiHGhjtMC7mCBPzkRxpjJxaYxk-Uf4o2kY67tQ81VkGGQ7BeT3LkobdbbY_XRpOmo7k8EEgEnuFyK1HrFY/s1700-e365/case-2.jpg)

The complaint shows an operator who hid the attack, behind a VPN proxy, tunneling tools, and aliases, but not himself. Prosecutors say his Snapchat flaunted cash, watches, and diamond chains reading "HACK THE PLANET," along with the very trips that placed him in those cities. He even posted photos of an Estonian police station and taunted that the feds had no idea what they had let get away.

## One arrest, and why it may not slow the threat

Investigators can now tie a single operator to the machine that set up an attack. But one arrest barely touches the wider threat.

In separate, recent research, [Group-IB argues](https://www.group-ib.com/blog/connecting-scattered-spider/) Scattered Spider is not really one group at all. It is a loose collective of small, independent cells, most no bigger than five people, tied together by shared tricks, tools, and chat rooms rather than a shared boss. Group-IB compares it to the Anonymous movement and says arresting some of these cells "will not stop the threat itself."

[![Cybersecurity](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiqmM4NpfZsx4cw-HrXQlCjZQmrF8bYnmB23AmpOPi16kPNB9lvICjpdYEclxJwyQ9OE8GgzQ8aOEI68tRuxNqov0MHz2Sq8xEPiYWM3Js6FM5t2nm2JHWodmR7qVSot14ZtWVqQRQ6B88OnMaVxCPwRG7xGPoIIZxF6QAhWVhMkQfs11NjyNtHsGEUH4_q/s728-e100/sygnia-d-1.jpg)](https://thehackernews.uk/sygnia-cyber-response-d-1)

Prosecutors describe Scattered Spider as one group behind more than 100 intrusions and over $100 million in ransoms. Group-IB says the label fits a scene better than a gang, and argues that loose structure is why the activity survives each arrest.

## Part of a longer run of cases
...