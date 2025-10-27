---
title: It's best to just assume you’ve been involved in a data breach somehow
url: https://blog.talosintelligence.com/threat-source-newsletter-july-18-2024/
source: Over Security - Cybersecurity news aggregator
date: 2024-07-23
fetch_date: 2025-10-06T17:44:25.265307
---

# It's best to just assume you’ve been involved in a data breach somehow

# Cisco Talos Blog

[ ]

* [Intelligence Center](https://talosintelligence.com/reputation)

  [ ]

  + [# Intelligence Center](https://talosintelligence.com/reputation)
  + BACK
  + [Intelligence Search](https://talosintelligence.com/reputation_center)
  + [Email & Spam Trends](https://talosintelligence.com/reputation_center/email_rep)
* [Vulnerability Research](https://talosintelligence.com/vulnerability_info)

  [ ]

  + [# Vulnerability Research](https://talosintelligence.com/vulnerability_info)
  + BACK
  + [Vulnerability Reports](https://talosintelligence.com/vulnerability_reports)
  + [Microsoft Advisories](https://talosintelligence.com/ms_advisories)
* [Incident Response](https://talosintelligence.com/incident_response)

  [ ]

  + [# Incident Response](/incident_response)
  + BACK
  + [Reactive Services](https://talosintelligence.com/incident_response/services#reactive-services)
  + [Proactive Services](https://talosintelligence.com/incident_response/services#proactive-services)
  + [Emergency Support](https://talosintelligence.com/incident_response/contact)
* [Blog](https://blog.talosintelligence.com)
* [Support](https://support.talosintelligence.com)

More

* Security Resources

  [ ]

  # Security Resources

  + BACK

  Security Resources
  + [Open Source Security Tools](https://talosintelligence.com/software)
  + [Intelligence Categories Reference](https://talosintelligence.com/categories)
  + [Secure Endpoint Naming Reference](https://talosintelligence.com/secure-endpoint-naming)
* Media

  [ ]

  # Media

  + BACK

  Media
  + [Talos Intelligence Blog](https://blog.talosintelligence.com)
  + [Threat Source Newsletter](https://blog.talosintelligence.com/category/threat-source-newsletter/)
  + [Beers with Talos Podcast](https://talosintelligence.com/podcasts/shows/beers_with_talos)
  + [Talos Takes Podcast](https://talosintelligence.com/podcasts/shows/talos_takes)
  + [Talos Videos](https://www.youtube.com/channel/UCPZ1DtzQkStYBSG3GTNoyfg/featured)
* Company

  [ ]

  # Company

  + BACK

  Company
  + [About Talos](https://talosintelligence.com/about)
  + [Careers](https://talosintelligence.com/careers)

# It's best to just assume you’ve been involved in a data breach somehow

By
[Jonathan Munshaw](https://blog.talosintelligence.com/author/jonathan/)

Thursday, July 18, 2024 14:00

[Threat Source newsletter](https://blog.talosintelligence.com/category/threat-source-newsletter/)

Between [AT&T](https://www.scmagazine.com/perspective/why-the-att-breach-matters-and-how-to-respond), all the follow-on activity from [Snowflake](https://www.wired.com/story/snowflake-breach-advanced-auto-parts-lendingtree/), [Microsoft Outlook](https://thehackernews.com/2023/09/outlook-breach-microsoft-reveals-how.html), and more, it’s best to probably just assume at this point that your personal information has somehow been involved in a data breach.

We’re only halfway through 2024, and we’ve already seen some of the largest data breaches and leaks in history. Telecommunications provider AT&T disclosed earlier this month that adversaries stole a cache of data that contained the phone numbers and call records of [“nearly all” of its customers](https://www.theverge.com/2024/7/14/24198294/att-paid-370000-ransom-hacked-customer-data-deleted-may), which equates to about 110 million people.

Even if you’ve yet to receive the dreaded boilerplate notification email from any company, it’s probably just best for all of us to assume that some of our personal information has been accessed, leaked or stolen over the past few years, or it’s going to be eventually.

I took this as an opportunity to check for myself. The ever-popular [Have I Been Pwned?](https://haveibeenpwned.com/) says my personal email address has been involved in 14 breaches, some dating back to 2017 and one as recently as June.

Thankfully, [Trend Micro’s ID Protect](https://idprotect.trendmicro.com/) says that my personal cell phone hasn’t been involved in any data breaches, but that certainly hasn’t stopped me from getting my fair share of spam texts and phone calls.

Outside of those two search engines, I felt like this would be a good space to provide additional resources and advice for anyone reading this. Even if you haven’t been a part of the recent spate of data breaches, I think it’s a good idea to take these steps now anyway, because you never know when the next breach is going to happen.

* **Stop reusing passwords.** [Use a free password manager](https://talostakes.talosintelligence.com/2018149/13767299) to generate random, secure passwords for each new account you create. That way, if one of your passwords \*is\* leaked, it makes it impossible for adversaries to start using those leaked credentials to try and brute force their way into other accounts.
* Once you enroll in that password manager, use it to frequently update and rotate your passwords.
* **Enroll in multi-factor authentication.** [Using any type of MFA](https://talostakes.talosintelligence.com/2018149/12695720) will ensure bad actors aren’t using any leaked credentials to log into other devices, so even if they have a complete set of usernames and passwords, you can still deny their login.
* [**Initiate a fraud alert**](https://consumer.ftc.gov/articles/what-know-about-credit-freezes-and-fraud-alerts) **to credit reporting agencies.** Of course, this only applies to users who live in the U.S. (though I’m sure other countries have something similar; I can only confidently write about the process in the U.S.). This will let potential lenders know that you may be the victim of fraudulent activity so they will take extra steps to ensure it’s actually you filling out a credit application.
* **If a company responsible for exposing your information offers you free credit monitoring, take advantage of it.** We’ll be covering what identity monitoring does for users in tomorrow morning’s episode of Talos Takes, so stay tuned!
* **Set up a unique passcode needed to make changes to certain accounts.** [AT&T is specifically advising customers](https://about.att.com/pages/cyberaware/ni/blog/sim_swap) to set up a passcode needed to prevent any significant account changes, such as porting phone numbers to another carrier.

## The one big thing

Speaking of data breaches, adversaries know that users and companies are concerned about this threat, too, and they’re leveraging that in phishing attacks and scams. Talos researchers [recently observed an ongoing cryptocurrency heist scam](https://blog.talosintelligence.com/data-breaches-fueling-scam-campaigns/) since as early as January 2024, leveraging hybrid social engineering techniques such as vishing and spear phishing, impersonating individuals and legitimate authorities to compromise the victims by psychologically manipulating their trust with social skills. Impersonating investigation officers of CySEC (Cyprus Securities and Exchange Commission), the scammers in this campaign are using a lure theme of refunding a fake seized amount from a fraudulent trading activity in Opteck trading platform to compromise the victims.

### Why do I care?

This particular campaign seems to be successful, as wallets connected to the group have received tens of thousands of U.S. dollars in the Ethereum cryptocurrency. But this is also evidence of a broader trend on the threat landscape: Attackers are going to be using data breaches as a threat and lure going forward. Users who are afraid of their data being leaked may be more likely to click on a phishing email or lure document that claims to have information on a leak. Or they may be more open to clicking on a link claiming to lead to “free” identity monitoring.

### So now what?

The significance of data breaches is facilitating the adversaries in their scam campaigns providing them the information needed to execute fraudulent activities, causing extensive financial, reputational, and psychological damage to individuals and organizations. So, creating securit...