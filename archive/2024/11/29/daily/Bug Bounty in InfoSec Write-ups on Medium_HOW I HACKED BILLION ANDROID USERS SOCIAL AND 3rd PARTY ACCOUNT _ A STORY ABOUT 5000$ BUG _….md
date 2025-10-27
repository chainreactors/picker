---
title: HOW I HACKED BILLION ANDROID USERS SOCIAL AND 3rd PARTY ACCOUNT | A STORY ABOUT 5000$ BUG |…
url: https://infosecwriteups.com/how-i-hacked-billion-android-users-social-and-3rd-party-account-a-story-about-5000-bug-54d8b6ce75df?source=rss----7b722bfd1b8d--bug_bounty
source: Bug Bounty in InfoSec Write-ups on Medium
date: 2024-11-29
fetch_date: 2025-10-06T19:15:05.374851
---

# HOW I HACKED BILLION ANDROID USERS SOCIAL AND 3rd PARTY ACCOUNT | A STORY ABOUT 5000$ BUG |…

[Sitemap](/sitemap/sitemap.xml)

[Open in app](https://rsci.app.link/?%24canonical_url=https%3A%2F%2Fmedium.com%2Fp%2F54d8b6ce75df&%7Efeature=LoOpenInAppButton&%7Echannel=ShowPostUnderCollection&%7Estage=mobileNavBar&source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fhow-i-hacked-billion-android-users-social-and-3rd-party-account-a-story-about-5000-bug-54d8b6ce75df&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

[Medium Logo](https://medium.com/?source=post_page---top_nav_layout_nav-----------------------------------------)

[Write](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-story&source=---top_nav_layout_nav-----------------------new_post_topnav------------------)

[Search](https://medium.com/search?source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fhow-i-hacked-billion-android-users-social-and-3rd-party-account-a-story-about-5000-bug-54d8b6ce75df&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

![](https://miro.medium.com/v2/resize:fill:64:64/1*dmbNkD5D-u45r44go_cf0g.png)

[## InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---publication_nav-7b722bfd1b8d-54d8b6ce75df---------------------------------------)

·

Follow publication

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:76:76/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_sidebar-7b722bfd1b8d-54d8b6ce75df---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow publication

# HOW I HACKED BILLION ANDROID USERS SOCIAL AND 3rd PARTY ACCOUNT | A STORY ABOUT 5000$ BUG | CVE-2021–0334

[![Karthikeyan.V](https://miro.medium.com/v2/resize:fill:64:64/1*7Dwtch8Uu2UNSxmjHtFs8Q.png)](https://medium.com/%40karthithehacker?source=post_page---byline--54d8b6ce75df---------------------------------------)

[Karthikeyan.V](https://medium.com/%40karthithehacker?source=post_page---byline--54d8b6ce75df---------------------------------------)

5 min read

·

Nov 15, 2024

--

1

Listen

Share

*In this blog, I will explain the process of how I discovered a vulnerability that triggers the mobile application which in turn allows me to take over multiple accounts.*

### DEEPLINK

***Deep links are a type of link that sends users directly to an app instead of a website or a store. They are used to send users straight to specific in-app locations, saving users the time and energy locating a particular page themselves — significantly improving the user experience.***

***Deep linking does this by specifying a custom URL scheme (iOS Universal Links) or an intent URL (on Android devices) that opens your app if it’s already installed. Deep links can also be set to direct users to specific events or pages, which could tie into campaigns that you may want to run.***

### Attack

Android has a component called app link to say it exactly it’s called deep link which is specifically developed for triggering any mobile application. As mentioned earlier, even if the app is updated it is possible to hijack it. how a researcher exploits it is … when an attacker develops an app he develops it with a deep link, secondly, that deep-link triggers the evil website. for example, if an update is out today the second update is out the next day and a bunch of users installs and update it. Whatever you give here it’s loaded in the deep link application. You know if you reset the password the link will be sent to the attacker and he can steal the token and he can do whatever he wants, so this is the scenario.

The researcher develops the malware with a deep link hijacking payload to exploit any deep-link integrated android application.

**STEPS :**

1. The researcher develops the malware with his own deep link hijacking payload. In this case, he then tests it on his own deep link (Deeplink: <https://cappriciosec.com)>.

2. Whenever the user clicks this link a prompt appears asking to select either. one of the options to choose “ *JUST ONCE*”or the other option “*ALWAYS*”.

3. When a user clicks the option “ *ALWAYS*” the malware opens and whenever he/she clicks the link it gets triggered automatically. This is the basic mechanism.

4. The researcher modifies the malware, in the first case he programmed in such a way that it triggers only the cappriciosec.com and then he added an additional payload that triggers any app link

5. Now the researcher releases an update in the google play store, Users will get an update and the users will update it

6. After the update, the application malware functionality will change because the researcher updated a new payload in the malware. as we already know the user had allowed access which in turn triggers the malware. Whenever the user clicks the Cappriciosec link.

Now if the user opens any link it will automatically trigger the malware and the pop-up will never ask the option to choose “just once” or “always”.

**WHY IT IS VULNERABLE?**

Earlier it was mentioned that the user allowed permission to open cappriciosec.com but after the update, any link is allowed to process and no pop-up appears. This all happens without the user’s knowledge so this is the vulnerable part.

**IMPACT**

Without the update, it was possible to inject a payload. The great impact is , it is easy to bypass the validation such as two-factor authentication, email verification code or token, password reset link or token, account credentials, and so on .. any web-related things can be easily hijacked. But to do this it doesn’t need users authentication just by a code it was able to do this, any HTTP related things can be easily hijacked by this type of vulnerability

> **VULNERABILITY DISCOVERED By** :- karthithehacker (
>
> [Karthikeyan.V](https://medium.com/u/a14784d94f2c?source=post_page---user_mention--54d8b6ce75df---------------------------------------)
>
> )
>
> **COLLABORATED & REPORT WRITTEN BY :-** [**jeyasri**](https://www.linkedin.com/in/jeyasri-a-7b571a1a9/)**.A (jeyasri**\_\_001)

**TIMELINE**

> **Reported to android os security team :** Date Aug 7, 2020 12:11PM
>
> **Created issue** : Aug 10, 2020 11:37PM
>
> **Assigned date** : Aug 11, 2020 10:42AM

Press enter or click to view image in full size

![]()

> Updated more

Press enter or click to view image in full size

![]()

Press enter or click to view image in full size

![]()

![]()

![]()

![]()

> **Fixed date** : Feb 2, 2021 1:57AM
>
> Acknowledgements :- <https://source.android.com/docs/security/overview/acknowledgements>
>
> **Rewarded date** : Feb 2, 2021 1:57AM
>
> **Reward**: $5000

Press enter or click to view image in full size

![]()

Press enter or click to view image in full size

![]()

### Note:-

We have requested the android security team to keep this CVE private, so we cannot disclose the payload, malware source code, and the POC videos

WRITER:- [AGNES RUSALIYA](https://www.linkedin.com/in/agnes-rusaliya-3b18481b7/)

**For further inquiries or more information about this vulnerability, you can reach out to**

**POC by:** [@karthithehacker](http://twitter.com/karthithehacker)**Mail:** contact@karthithehacker.com
**Website:** <https://www.karthithehacker.com/>

If you’re interested in our **VAPT service**, contact us at ceo@cappriciosec.com or contact@cappriciosec.com.

For enrolling my cybersecurity and Bugbounty course,

WhatsApp +91 82709 13635.

## Connect with Me:

* **Mail:** contact@karthithehacker...