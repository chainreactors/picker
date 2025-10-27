---
title: Account Takeover: An Epic Bug Bounty Story
url: https://infosecwriteups.com/account-takeover-an-epic-bug-bounty-story-dd5468d5773d?source=rss----7b722bfd1b8d--bug_bounty
source: Bug Bounty in InfoSec Write-ups on Medium
date: 2023-03-12
fetch_date: 2025-10-04T09:21:48.029115
---

# Account Takeover: An Epic Bug Bounty Story

[Sitemap](/sitemap/sitemap.xml)

[Open in app](https://rsci.app.link/?%24canonical_url=https%3A%2F%2Fmedium.com%2Fp%2Fdd5468d5773d&%7Efeature=LoOpenInAppButton&%7Echannel=ShowPostUnderCollection&%7Estage=mobileNavBar&source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Faccount-takeover-an-epic-bug-bounty-story-dd5468d5773d&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

[Medium Logo](https://medium.com/?source=post_page---top_nav_layout_nav-----------------------------------------)

[Write](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-story&source=---top_nav_layout_nav-----------------------new_post_topnav------------------)

[Search](https://medium.com/search?source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Faccount-takeover-an-epic-bug-bounty-story-dd5468d5773d&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

![](https://miro.medium.com/v2/resize:fill:64:64/1*dmbNkD5D-u45r44go_cf0g.png)

[## InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---publication_nav-7b722bfd1b8d-dd5468d5773d---------------------------------------)

·

Follow publication

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:76:76/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_sidebar-7b722bfd1b8d-dd5468d5773d---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow publication

# Account Takeover: An Epic Bug Bounty Story

[![Jaydev Ahire](https://miro.medium.com/v2/da:true/resize:fill:64:64/0*jL2MtLvXRjQmkLlO)](https://jaydevahire.medium.com/?source=post_page---byline--dd5468d5773d---------------------------------------)

[Jaydev Ahire](https://jaydevahire.medium.com/?source=post_page---byline--dd5468d5773d---------------------------------------)

7 min read

·

Mar 11, 2023

--

10

Listen

Share

Hello Folks! I am back after a long time with an interesting (pre) Account Takeover bug and how I chained this with XSS. You might get confused as this is a long writeup, but don’t worry, stick it till the end; I’ve simplified the things at the end for better understanding.

Press enter or click to view image in full size

![]()

In this blog, I am going to share my interesting Pre - Account Takeover story that happened due to the Broken Access Control and How I managed to make this a valid issue.

I was hunting on an old private bug bounty program. I knew in my mind that I needed to find a unique issue to avoid duplicates. As usual, fired up my burp and randomly started to browse the target.
I came across a profile section of the site. There was an option to edit only Names and Passwords and not Emails.

Press enter or click to view image in full size

![]()

No option to change the email

I decided to change the email address. For that, I started examining the other settings, changed the name and captured the request in Burp.

Press enter or click to view image in full size

![]()

I noticed and started playing with **UserAttributes.** First, I changed the name to **update\_email** and the **value** to an existing account’s mail.
I got an error —
{
“\_\_type”:”InvalidParameterException”,
”message”:”user.update\_email: Attribute does not exist in the schema.\n”
}

Press enter or click to view image in full size

![]()

Again, I changed the name to **change\_email** and sent the request, but I got the same error —
{
“\_\_type”:”InvalidParameterException”,
”message”:”user.change\_email: Attribute does not exist in the schema.\n”
}

Then I went back to the **signup flow** request and observed that the application was sending a new email address in the Username attribute while signing up. I changed the name to **Username** but got the same error again -
{
“\_\_type”:”InvalidParameterException”,
”message”:”user.Username: Attribute does not exist in the schema.\n”
}

I was about to give up, but as a last try, I sent a request again with only an **email**, and I got a new error!

Press enter or click to view image in full size

![]()

I switched my focus to Pre — Account Takeover as this error confirmed that I can’t takeover another user’s account. I changed the email address to an unregistered email, and It worked.

Press enter or click to view image in full size

![]()

I received verification OTP on a new email. However, I was able to successfully change the email address to a new one without undergoing the verification process and got an account without any verification.

Press enter or click to view image in full size

![]()

Wow! I got too excited, made a report and submitted it :)
Within some hours, they changed it to Not Applicable and sent me this reply:

Press enter or click to view image in full size

![]()

**Me to myself**

After receiving this response, I returned to the application and tried to login with the victim's mail (Cyborj27+9@gmail.com) and the attacker’s password and got an error — **“username or password is incorrect”**

Press enter or click to view image in full size

![]()

Then, I tried resetting the password to see if it sent any OTP.
But got a new error — **“The password could not be reset, since the email is not registered or verified.”**

Press enter or click to view image in full size

![]()

I made notes of all the errors I got and went to sleep. The next day I started again from the beginning but found nothing new. Again opened my notes and read them 2–3 times. After reading this error — “The password could not be reset, since the email is not registered or verified.”
I decided to try to **register** with the victim’s email. When I registered, the application threw a new error — **“ Your account is temporarily not available. Please try to log in in 15 minutes.”**

Press enter or click to view image in full size

![]()

After 15 mins, I tried to login with the victim’s email and password used during registration. But I still got this error — **“username or password is incorrect.”**
Then I tried to log in with the **victim’s email** (cyborj27+9@gmail.com) and the **attacker's** (wrestlingmaster27+2@gmail.com) **password**. And to my surprise, I got access to the account!

**Now the main problem was —**

> “The password can be rested by the owner of the email address at any time”

So I went back to the reset password feature, I tried to reset the password and got an error — “The password could not be reset, since the email is not registered or verified.”

Press enter or click to view image in full size

![]()

Then I tried to get a **new verification** code on the victim’s email and got an error — “ **Invalid username**.”

Press enter or click to view image in full size

![]()

I was like:

Problem solved! User can’t reset their password through the password reset link.

**This might not have been very clear till now, but I’ll summarise this in short:**

1. Two emails:
   **Attacker — Wrestlingmaster27+2@gmail.com
    Victim (Unregistered account) — Cyborj27+9@gmail.com**
2. The application does not have the **functionality to change** the email.
3. From the attacker account, change the email address to the victim’s by enumerating the **UserAttributes** value.
   “UserAttributes”:[
   {“Name”:”email”,
   ”Value”:”cyborj27+9@gmail.com”
   }
4. When the attacker changes the mail, the victim will receive the OTP code for verification.
5. But no need to verify the mail, the attacker already got the victim’s email linked to ...