---
title: Account Takeover: An Epic Bug Bounty Story
url: https://buaq.net/go-152972.html
source: unSafe.sh - 不安全
date: 2023-03-12
fetch_date: 2025-10-04T09:21:39.071351
---

# Account Takeover: An Epic Bug Bounty Story

* [unSafe.sh - 不安全](https://unsafe.sh)
* [我的收藏](/user/collects)
* [今日热榜](/?hot=true)
* [公众号文章](/?gzh=true)
* [导航](/nav/index)
* [Github CVE](/cve)
* [Github Tools](/tools)
* [编码/解码](/encode)
* [文件传输](/share/index)
* [Twitter Bot](https://twitter.com/buaqbot)
* [Telegram Bot](https://t.me/aqinfo)
* [Search](/search/search)

[Rss](/rss.xml)

[ ]
黑夜模式

![]()

Account Takeover: An Epic Bug Bounty Story

Hello Folks! I am back after a long time with an interesting (pre) Account Takeover bug and how I ch
*2023-3-11 08:16:48
Author: [infosecwriteups.com(查看原文)](/jump-152972.htm)
阅读量:26
收藏*

---

Hello Folks! I am back after a long time with an interesting (pre) Account Takeover bug and how I chained this with XSS. You might get confused as this is a long writeup, but don’t worry, stick it till the end; I’ve simplified the things at the end for better understanding.

In this blog, I am going to share my interesting Pre - Account Takeover story that happened due to the heavy backend misconfiguration and How I managed to make this a valid issue.

I was hunting on an old private bug bounty program. I knew in my mind that I needed to find a unique issue to avoid duplicates. As usual, fired up my burp and randomly started to browse the target.

No option to change the email

I decided to change the email address. For that, I started examining the other settings, changed the name and captured the request in Burp.

I noticed and started playing with **UserAttributes.** First, I changed the name to **update\_email** and the **value** to an existing account’s mail.
I got an error —
{
“\_\_type”:”InvalidParameterException”,
”message”:”user.update\_email: Attribute does not exist in the schema.\n”
}

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

I switched my focus to Pre — Account Takeover as this error confirmed that I can’t takeover another user’s account. I changed the email address to an unregistered email, and It worked.

I received verification OTP on a new email. However, I was able to successfully change the email address to a new one without undergoing the verification process and got an account without any verification.

Wow! I got too excited, made a report and submitted it :)
Within some hours, they changed it to Not Applicable and sent me this reply:

**Me to myself**

After receiving this response, I returned to the application and tried to login with the victim's mail ([[email protected]](/cdn-cgi/l/email-protection)) and the attacker’s password and got an error — **“username or password is incorrect”**

Then, I tried resetting the password to see if it sent any OTP.
But got a new error — **“The password could not be reset, since the email is not registered or verified.”**

I made notes of all the errors I got and went to sleep. The next day I started again from the beginning but found nothing new. Again opened my notes and read them 2–3 times. After reading this error — “The password could not be reset, since the email is not registered or verified.”
I decided to try to **register** with the victim’s email. When I registered, the application threw a new error — **“ Your account is temporarily not available. Please try to log in in 15 minutes.”**

After 15 mins, I tried to login with the victim’s email and password used during registration. But I still got this error — **“username or password is incorrect.”**
Then I tried to log in with the **victim’s email** ([[email protected]](/cdn-cgi/l/email-protection)) and the **attacker's** ([[email protected]](/cdn-cgi/l/email-protection)) **password**. And to my surprise, I got access to the account!

**Now the main problem was —**

> “The password can be rested by the owner of the email address at any time”

So I went back to the reset password feature, I tried to reset the password and got an error — “The password could not be reset, since the email is not registered or verified.”

Then I tried to get a **new verification** code on the victim’s email and got an error — “ **Invalid username**.”

I was like:

Problem solved! User can’t reset their password through the password reset link.

**This might not have been very clear till now, but I’ll summarise this in short:**

1. Two emails:
   **Attacker — [[email protected]](/cdn-cgi/l/email-protection)
    Victim (Unregistered account) — [[email protected]](/cdn-cgi/l/email-protection)**
2. The application does not have the **functionality to change** the email.
3. From the attacker account, change the email address to the victim’s by enumerating the **UserAttributes** value.
   “UserAttributes”:[
   {“Name”:”email”,
   ”Value”:”[[email protected]](/cdn-cgi/l/email-protection#503329323f223a62677b6910373d31393c7e333f3d)”
   }
4. When the attacker changes the mail, the victim will receive the OTP code for verification.
5. But no need to verify the mail, the attacker already got the victim’s email linked to their account.
6. The **attacker logs out** and tries to **log in** with the **victim’s email** and **attacker’s password**. The application will **not allow** this as the victim’s email is **not registered** yet.
7. The attacker navigates to the registration and **registers with the victim’s** email. The application throws an error — “ Your account is temporarily not available. Please try to log in in 15 minutes.”
8. After 15 mins, the attacker goes back to the login panel and logs in successfully with the **victim’s email and attacker’s password**.
9. When the victim tries to **reset** their password or try to **verify** the account application throws an error — “Invalid username”, meaning that the victim has lost all their ways to retrieve their account.
10. Due to the heavy **misconfiguration**, the attacker has the **account linked** to the victim’s email. The attacker only **registered** the email and did not **verify** the account, that’s why the backend server does not have a record of the victim’s email. (This is my guess only, not sure)

**I blocked all the ways for the victim to retrieve their account:**

1. The victim can’t reset their password by “reset password functionality.”
2. If the victim tries to contact the support team to reset the password, most probably, the chances are the support team will not be able to find the victim’s email in the backend as it is an unverified email — (My guess based on the error I got during password reset and verification resend)

But still, there was one “**If**” condition, what if the victim manages to regain their account?

I found an HTML injection in the name field when I started hunting on the application. I ignored it because there was no impact.
Then I got an idea if somehow I managed to convert this into stored XSS and put XSS payload in the victim’s account, then whenever the victim manages to retrieve their account, the XSS will get triggered.

I put basic XSS payload in the last name field, but the application showed blank white space and no alert.

After trying for some hours, I figured out that the application has only basic protection against XSS, and it filters only <script>, <img>, alert, etc.
Then I constructed a payload, replaced alert with prompt, and it worked!

**<a onmouseover=”prompt(document.cookie)”>Here</a>**

As soon as the victim scrolls over the last name, XSS will get triggered.

I blocked all the ways for the victim to retrieve their password, and even if they managed to...