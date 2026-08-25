---
title: I Changed One “User_Id” and the API Said “Sure” — From Password Reset to Mass Account Takeover
url: https://infosecwriteups.com/i-changed-one-user-id-and-the-api-said-sure-from-password-reset-to-mass-account-takeover-9d4d4e15e022?source=rss----7b722bfd1b8d--bug_bounty
source: Bug Bounty in InfoSec Write-ups on Medium
date: 2026-08-24
fetch_date: 2026-08-25T02:59:22.193524
---

# I Changed One “User_Id” and the API Said “Sure” — From Password Reset to Mass Account Takeover

[Sitemap](/sitemap/sitemap.xml)

[Open in app](https://play.google.com/store/apps/details?id=com.medium.reader&referrer=utm_source%3DmobileNavBar&source=---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fi-changed-one-user-id-and-the-api-said-sure-from-password-reset-to-mass-account-takeover-9d4d4e15e022&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

[Medium Logo](https://medium.com/?source=---top_nav_layout_nav-----------------------------------------)

Get app

[Write](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-story&source=---top_nav_layout_nav-----------------------new_post_topnav------------------)

[Search](https://medium.com/search?source=---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fi-changed-one-user-id-and-the-api-said-sure-from-password-reset-to-mass-account-takeover-9d4d4e15e022&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

![Unknown user](https://miro.medium.com/v2/resize:fill:64:64/1*dmbNkD5D-u45r44go_cf0g.png)

[## InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---publication_nav-7b722bfd1b8d-9d4d4e15e022---------------------------------------)

·

1. [1. It Started With a Boring Password Reset](/?source=post_page-----9d4d4e15e022---------------------------------------#3bf5 "1. It Started With a Boring Password Reset")
2. [2. Time to Remove Things Until It Breaks](/?source=post_page-----9d4d4e15e022---------------------------------------#71a9 "2. Time to Remove Things Until It Breaks")
3. [3. Wait… Where Is the identifier?](/?source=post_page-----9d4d4e15e022---------------------------------------#ba41 "3. Wait… Where Is the identifier?")
4. [4. The Dangerous Parameter: User\_Id](/?source=post_page-----9d4d4e15e022---------------------------------------#163a "4. The Dangerous Parameter: User_Id")
5. [5. Proving Account Takeover](/?source=post_page-----9d4d4e15e022---------------------------------------#86ce "5. Proving Account Takeover")
6. [6. Conclusion and Reporting](/?source=post_page-----9d4d4e15e022---------------------------------------#2c86 "6. Conclusion and Reporting")
7. [7. See you Again](/?source=post_page-----9d4d4e15e022---------------------------------------#3eeb "7. See you Again")

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:76:76/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_sidebar-7b722bfd1b8d-9d4d4e15e022---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

[Bug Bounty](https://medium.com/tag/bug-bounty?source=post_page---header_tags--9d4d4e15e022---------------------------------------)

[Bug Bounty Writeup](https://medium.com/tag/bug-bounty-writeup?source=post_page---header_tags--9d4d4e15e022---------------------------------------)

# I Changed One “User\_Id” and the API Said “Sure” — From Password Reset to Mass Account Takeover 💀

[![Rajdip Chavan](https://miro.medium.com/v2/resize:fill:64:64/1*H114_7iNF_afj1m3bLH7uQ.jpeg)](https://medium.com/%40iamrajchavan?source=post_page---byline--9d4d4e15e022---------------------------------------)

[Rajdip Chavan](https://medium.com/%40iamrajchavan?source=post_page---byline--9d4d4e15e022---------------------------------------)

4 min read

·

21 hours ago

--

1

[Listen](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2Fplans%3Fdimension%3Dpost_audio_button%26postId%3D9d4d4e15e022&operation=register&redirect=https%3A%2F%2Finfosecwriteups.com%2Fi-changed-one-user-id-and-the-api-said-sure-from-password-reset-to-mass-account-takeover-9d4d4e15e022&source=---header_actions--9d4d4e15e022---------------------post_audio_button------------------)

Share

Account takeover vulnerabilities are among the most impactful findings in web and API security assessments. Sometimes they involve complex authentication bypasses, token manipulation, or sophisticated exploit chains. Other times, the vulnerability comes down to one fundamental mistake: **the backend trusts the client to tell it whose password should be changed.**

Password reset functionality is supposed to help users who forget their passwords.

This one was a little more generous.

It was willing to reset **other people’s passwords too.**

During an authorized API penetration test, I came across a password-reset endpoint that looked completely normal at first. A few Burp Repeater requests later, I realized the backend had essentially implemented:

```
Client: Hey API, I'm User 3. Change my password.

API: Any proof?

Client: No.

API: Understandable. Password changed successfully.
```

What started as routine password-reset testing quickly turned into a **Critical Mass Account Takeover** vulnerability.

Here’s how I found it.

## 1. It Started With a Boring Password Reset

While mapping the application’s API endpoints, I found something interesting:

```
POST /users/resetPassword
```

The request body was beautifully simple:

```
{
    "User_Id": "3",
    "New_Password": "Password@123"
}
```

My pentester brain immediately noticed something.

The client was supplying:

```
User_Id
New_Password
```

In other words:

> ***Here is the user whose password I want to change, and here is their new password.***

That’s fine *if* the backend verifies that I’m actually allowed to reset that account.

So the next question was obvious:

**What actually authorizes this password reset?**

## 2. Time to Remove Things Until It Breaks

One of my favorite approaches when testing authentication APIs is extremely sophisticated:

**Delete security controls until something breaks.**

I started looking for the usual suspects:

```
Authorization: Bearer <JWT>

resetToken=<token>

otp=123456

currentPassword=<password>

verificationToken=<token>
```

Surely at least one of these would be required.

So I removed the `Authorization` header.

The request became essentially:

```
POST /users/resetPassword HTTP/2
Host: target.example
Content-Type: application/json

{
    "User_Id": "3",
    "New_Password": "Password@123"
}
```

I hit **Send** in Burp Repeater.

Expected:

```
HTTP/2 401 Unauthorized
```

Maybe:

```
{
    "error": "Authentication required"
}
```

Actual:

```
HTTP/2 200 OK
```

And then came the beautiful response:

```
{
    "Status": "Success",
    "Message": "New Password reset successfully"
}
```

Me:

![]()

## **3. Wait… Where Is the identifier?**

At this point, I assumed I had missed something.

Maybe the application had previously verified something and the backend was maintaining some server-side recovery state.

So I checked again.

No: Authorization

## Get Rajdip Chavan’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Subscribe

[x]

Remember me for faster sign in

No: OTP

No: Reset Token

No: Current Password

No: Session Cookie

The entire security decision appeared to depend on:

```
{
    "User_Id": "3"
}
```

That is when things became interesting.

## 4. The Dangerous Parameter: `User_Id`

The request allowed the client to specify:

```
"User_Id": "3"
```

Whenever I see identifiers like this in security-sensitive functionality, I ask:

> ***What happens if I change it?***

Classic API pentesting.

Using only authorized test accounts, I modified the identifier.

For example:

```
- "User_Id": "3"
+ "User_Id": "4"
```

And kept:

```
"New_Password": "Password@123"
```

Sent the request.

The API responded:

```
{
    "Status": "Success",
    "Me...