---
title: Keeping an Eye on MFA-Bombing Attacks, (Mon, Aug 18th)
url: https://isc.sans.edu/diary/rss/32208
source: SANS Internet Storm Center, InfoCON: green
date: 2025-08-19
fetch_date: 2025-10-07T00:50:12.857693
---

# Keeping an Eye on MFA-Bombing Attacks, (Mon, Aug 18th)

# [Internet Storm Center](/)

[Sign In](/login.html)
[Sign Up](/register.html)

Handler on Duty: [Johannes Ullrich](/handler_list.html#johannes-ullrich "Johannes Ullrich")

Threat Level: [green](/infocon.html)

* [previous](/diary/32202)
* [next](/diary/32212)

# [Keeping an Eye on MFA-Bombing Attacks](/forums/diary/Keeping%2Ban%2BEye%2Bon%2BMFABombing%2BAttacks/32208/)

**Published**: 2025-08-18. **Last Updated**: 2025-08-18 14:29:47 UTC
**by** [Rob VandenBrink](/handler_list.html#rob-vandenbrink) (Version: 1)

[3 comment(s)](/diary/Keeping%2Ban%2BEye%2Bon%2BMFABombing%2BAttacks/32208/#comments)

I recently woke up (as one does each day, hopefully) and saw a few Microsoft MFA prompts had pinged me overnight.  Since I had just awakened, I just deleted them, then two minutes later clued in - this means that one of my passwords was compromised, and I had no idea which site the compromised creds were for.

I opened the MS Authenticator app on my phone, and saw no option for "view history" - this seems like a huge miss to me.

I finally found it in the MS portal at account.microsoft.com / my signins, which translates to: <https://mysignins.microsoft.com/>.  It's not so helpful that this information has moves ovr time, most of the online documentation tells you to navigate to your privacy settings to get to this page (which is not correct info for today's site).

Once you are there, this page nicely lists all the logins, successful or otherwise, as well as what site or resource they were for as well as the geography.  So if you are being attacked from abroad you can see that immediately in this page.  What it doesn't do is list the login geography and phone geography separately - that would be helpful, as if they don't match that's almost positively an attack, it takes the "I was on vacation" thing off the table (unless your organization uses proxies pre-vpn that is).

So perfect!  What does this mitigate against?  For me today, it tells me which site I need to change my password for.  Also it tells me that I need to contact that customer and tell them that they've been breeched somehow - all of my passwords are unique per-site and customer, so if one is compromised it's not because I used it on some less secure site - I'm not ordering take-out with any of my customer passwords for instance.

This doesn't mean that this customer has had a full compromise, that the attacker recovered it from AD (good luck with that against my longer, random string passwords) - more likely one of their web resources stores passwords in clear text or stores passwords using some reversible encryption.  This also means that organization is rocking it like it's 2005 - a web resource that's most likely using their on-premise AD as it's back-end authentication without MFA - then storing or caching the credentials, you know, for "performance reasons". (those same "performance reasons" that we fought against for years when implementing SSL/TLS).

What is the real attack vector here?  There are a couple:

* Ask Uber about MFA-bombing.  If you target someone junior enough - or senior enough, and send them 2-30-40 MFA requests, chances are that eventually they'll press "OK" to make the flood stop.  Or if the attacker can gain additional info on the target person (like say from LinkedIn), they can contact them via email or SMS, masquerade as an IT support person and instruct them to press "OK".  An MFA attack of this type against an Uber driver in 2022 ended up in a successful (but very brief) compromise.
* Of course, if the compromise got around MFA protections (using either MFA bombing or some direct attack that bypasses authentication), the attacker is still free to pillage that site.  If they can pivot from that site, it's very likely that they'll find themselves on the inside network, where you can likely collect admin level creds from all sorts of places and own the whole shop.
* Even if the attacker can't find a decent pivot, now they've got working credentials, which they can leverage against anything else that you have that's internet facing - both those using MFA or not.  If they are persistent (that's the "P" in APT), eventually they'll find one that they can MFA Bomb, RCE or otherwise compromise, then pivot inbound from, which of course leads them to great destruction and victory, with tears from the target company to speed them on their way!

Many of you are likely admins for organizations though, so the single-person view isn't so useful.  As an administrator, can you see this same history information for your supported users?  Sort of, just without the actual maps (which aren't so useful anyway).  In https:portal.azure.com, navigate to identiy Protection / Dashboard / risk Detections.  Choose "View Attacks", then from there you can pick an individual user and list all of their logins.

While I couldn't find an easy way to navigate to list all users (please use our comment field if you have that?), if you look in the URL, the report for a single user has a URL formatted as:
https://portal.azure.com/#view/Microsoft\_AAD\_IAM/SignInLogsList.ReactView/userObjectId/<User-GUID-goes -in-HEX-here>/timeRangeType/last1month

If you remove the "UserObjedId/<GUID> sections of the URL, this now lists all users in the organization.  From there you can filter the display as needed or simply export it an dice it up with Excel or whatever.

If you've got a way to get to this info directly, or better yet if you have a link to the API (which would allow you to pull this into your SIEM) or Powershell script that can collect this, by all means share in our comment form!

===============
Rob VandenBrink
[[email protected]](/cdn-cgi/l/email-protection)

Keywords: [MFA](/tag.html?tag=MFA) [MFA Bombing](/tag.html?tag=MFA Bombing)

[3 comment(s)](/diary/Keeping%2Ban%2BEye%2Bon%2BMFABombing%2BAttacks/32208/#comments)

* [previous](/diary/32202)
* [next](/diary/32212)

### Comments

Our reader Sharjeel notes that this other link shows "risky users", which includes failed logins, atypical travel and other risks:
https://portal.azure.com/#view/Microsoft\_AAD\_IAM/RiskyUsersBlade

For which I'll note that Azure's monitoring truly is a bit of a labyrinth. Thanks Sharjeel, and by all means keep other links and methods coming folks!

#### Rob VandenBrink

#### Aug 18th 2025 1 month ago

You can go the the Microsoft Entra admin center -> go to Users -> All Users -> sign-in logs -> then use the filter to add filter by status and then you can filter out by failure (select look back window) - I have used this when I have too many brute force attempts to report by "hand". After you set up the filter you can download the failed attempts list as json output or as csv.

#### Pete

#### Aug 18th 2025 1 month ago

[Login here to join the discussion.](/login)

Top of page

×

![modal content]()

[Diary Archives](/diaryarchive.html)

* [![SANS.edu research journal](https://isc.sans.edu/images/researchjournal5.png)](/j/research)
* [Homepage](/index.html)
* [Diaries](/diaryarchive.html)
* [Podcasts](/podcast.html)
* [Jobs](/jobs)
* [Data](/data)
  + [TCP/UDP Port Activity](/data/port.html)
  + [Port Trends](/data/trends.html)
  + [SSH/Telnet Scanning Activity](/data/ssh.html)
  + [Weblogs](/weblogs)
  + [Domains](/data/domains.html)
  + [Threat Feeds Activity](/data/threatfeed.html)
  + [Threat Feeds Map](/data/threatmap.html)
  + [Useful InfoSec Links](/data/links.html)
  + [Presentations & Papers](/data/presentation.html)
  + [Research Papers](/data/researchpapers.html)
  + [API](/api)
* [Tools](/tools/)
  + [DShield Sensor](/howto.html)
  + [DNS Looking Glass](/tools/dnslookup)
  + [Honeypot (RPi/AWS)](/tools/honeypot)
  + [InfoSec Glossary](/tools/glossary)
* [Contact Us](/contact.html)
  + [Contact Us](/contact.html)
  + [About Us](/about.html)
  + [Handlers](/handler_list.html)* [About Us](/about.html)

[Slack Channel](/slack/index.html)

[Mastodon](https://infosec.exchange/%40sans_isc)

[Bluesky](https://bsky...