---
title: Supersizing your DUO and 365 Integration, (Thu, Oct 27th)
url: https://isc.sans.edu/diary/rss/29194
source: SANS Internet Storm Center, InfoCON: green
date: 2022-10-28
fetch_date: 2025-10-03T21:10:53.353936
---

# Supersizing your DUO and 365 Integration, (Thu, Oct 27th)

# [Internet Storm Center](/)

[Sign In](/login.html)
[Sign Up](/register.html)

Handler on Duty: [Johannes Ullrich](/handler_list.html#johannes-ullrich "Johannes Ullrich")

Threat Level: [green](/infocon.html)

* [previous](/diary/29192)
* [next](/diary/29198)

# [Supersizing your DUO and 365 Integration](/forums/diary/Supersizing%2Byour%2BDUO%2Band%2B365%2BIntegration/29194/)

**Published**: 2022-10-27. **Last Updated**: 2022-10-27 22:52:34 UTC
**by** [Tom Webb](/handler_list.html#tom-webb) (Version: 1)

[0 comment(s)](/diary/Supersizing%2Byour%2BDUO%2Band%2B365%2BIntegration/29194/#comments)

**As soon as defenders started implementing multifactor authentication, attackers tried to get around it. One of the most common methods attackers are currently using is Push or Call Annoyance. Attackers try multiple times to authenticate and annoy the user until they accept the request. Several options address this attack method. This article shows how to use more advanced MFA options on a strategically risky subset of users without a massive rollout to your entire organization. This will allow for more agile adjustments and lower helpdesk calls.**

**With Office 365 and Microsoft Authenticator, their integration and authentication methods based on risk are nice. If you are using Duo with O365, it's more challenging, but we will be upping our game to increase the difficulty for the attackers. Depending on your Duo license, they have additional options for protection on their backend,  but this works for all Duo license levels.**

**Prevent Annoyance Attack**

* **Only allow code authentication or hardware tokens(No push or call)**
* **Use Verified Duo Push, MS Authenticator with Number matching (users can not just accept the request)**

**App Code only authentication is where the only method allowed for multifactor is a passcode from the Mobile App or Hardware Tokens to keep attackers from prompting users. The biggest issue with this is user education and convenience.**

![](https://isc.sans.edu/diaryimages/images/duopolicy.JPG)

**The second way, and the way we are going to cover in detail, is the new Verified Duo push method(1). The user will verify their identity by entering a code into the app. The code is displayed on the device you are using to log in.   Microsoft version of this tech is called MS Authenticator number matching (2).**

![](https://isc.sans.edu/diaryimages/images/authpush.JPG)

**While this does continue to prompt the user for authentication by the attackers, without the code, they can not approve access. It would take additional social engineering to get past this process. I believe this is a more user-friendly experience than just using the code in the app.**

**What if you don't want to apply this to All logins?**

**With our initial deployment, we didn't want every 365 users to do a Verified push every login. As previously stated, MS and DUO do not have the tightest integrations, so to do this risk-based takes some additional setup. We created 2 Duo integrations, one for "Normal Auth" and one for "Secure Auth."   The "Secure Auth" had separate Duo and conditional access policies to meet the new requirements.**

**Supersize Setup**

**1. New Duo 365 Application**

**You need to create a new Duo application. It will require you to use your 365 global admin account during that process. Name the new application integration something like 365 Secure.**

**2. Setup a new policy for the Duo 365 Secure App**

**The policy should look like the below picture as you want this to be very restricted for risky authentications. In this case, it has Verified Duo Push as the only method for authentication. Instead of using the verified push here, you could also use the Mobile code only and hardware token option. Just don't allow SMS, phone, or standard push.**

![](https://isc.sans.edu/diaryimages/images/dpolicy.JPG)

**3. Create a new Custom control in MS 365 Conditional Access.**

**(Following Duo Instructions as needed). But before importing, you need to change the Name and ID like below so you can have two instances of DUO with different names. By default, it wants to use the same name and will error on the import.**

![](https://isc.sans.edu/diaryimages/images/365import.JPG)

**4. New 365 Conditional Access Policy**

**Here is where you should determine what settings you want for the new protections. At a minimum, I think High Sign-in risk. If you do not have many users from outside the US, add location-based too. If you manage and clear risky users, also add that as an option. By tuning the Conditional Access policy right, you will get a few legitimate users that get the policy reducing helpdesk calls while adding much-needed protections.**

**To get a good idea of what's currently going on with your sign-ins, go to portal.azure.com, search for "security" and select Risky Users, Risky Signs and others on the bottom left.**

**5. Stop Evil**

**Below is what would have been a typical annoyance attack that would have been successful without the additional controls in place.**

![](https://isc.sans.edu/diaryimages/images/duolog.JPG)

**Are you using some sweet 365 settings or a neat way of using Multifactor? Leave us a comment.**

**(1)https://duo.com/blog/verified-duo-push-makes-mfa-more-secure**

**(2)https://techcommunity.microsoft.com/t5/microsoft-entra-azure-ad-blog/new-microsoft-authenticator-security-features-are-now-available/ba-p/2464386**

Keywords: [phishing](/tag.html?tag=phishing) [MFA](/tag.html?tag=MFA) [Office 365](/tag.html?tag=Office 365) [Duo](/tag.html?tag=Duo)

[0 comment(s)](/diary/Supersizing%2Byour%2BDUO%2Band%2B365%2BIntegration/29194/#comments)

* [previous](/diary/29192)
* [next](/diary/29198)

### Comments

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

[Bluesky](https://bsky.app/profile/sansisc.bsky.social)

[X](https://twitter.com/sans_isc)

![](/adimg.html?id=)

© 2025 SANS™ Internet Storm Center
Developers: We have an [API](/api/) for you!   [![Creative Commons License](/images/cc.png)](https://creativecommons.org/licenses/by-nc-sa/4.0/)

* [Link To Us](/linkback.html)
* [About Us](/about.html)
* [Handlers](/handler_list.html)
* [Privacy Policy](/privacy.html)