---
title: Email, Email on the Wall, Who Sent You, After All?
url: https://blog.compass-security.com/2024/10/email-email-on-the-wall-who-sent-you-after-all/
source: Over Security - Cybersecurity news aggregator
date: 2024-10-30
fetch_date: 2025-10-06T18:55:19.125975
---

# Email, Email on the Wall, Who Sent You, After All?

## [Compass Security Blog](https://blog.compass-security.com "Compass Security Blog — Offensive Defense")

### Offensive Defense

* [Home](https://blog.compass-security.com/)
* [Archive](https://blog.compass-security.com/archive/)
* [Contact](https://blog.compass-security.com/contact/)
* [Newsletter](https://blog.compass-security.com/mailing-list-tigerinfo/)

* [Home](https://blog.compass-security.com/)
* [Archive](https://blog.compass-security.com/archive/)
* [Contact](https://blog.compass-security.com/contact/)
* [Newsletter](https://blog.compass-security.com/mailing-list-tigerinfo/)

# [Email, Email on the Wall, Who Sent You, After All?](https://blog.compass-security.com/2024/10/email-email-on-the-wall-who-sent-you-after-all/ "Email, Email on the Wall, Who Sent You, After All?")

[October 29, 2024](https://blog.compass-security.com/2024/10/email-email-on-the-wall-who-sent-you-after-all/ "Email, Email on the Wall, Who Sent You, After All?")
 /
[Andreas Arnold](https://blog.compass-security.com/author/aarnold/ "Posts by Andreas Arnold")
 /
[0 Comments](https://blog.compass-security.com/2024/10/email-email-on-the-wall-who-sent-you-after-all/#respond)

[![](https://blog.compass-security.com/wp-content/uploads/2024/08/e1only_A_female_CFO_with_a_cupcake_in_hand_looking_at_a_wall_wi_2e1f1ba3-c2ea-4bb2-9912-9d2ab0869da7.png)](https://blog.compass-security.com/wp-content/uploads/2024/08/e1only_A_female_CFO_with_a_cupcake_in_hand_looking_at_a_wall_wi_2e1f1ba3-c2ea-4bb2-9912-9d2ab0869da7.png)

Franky opens her email in the morning and sees the following email in her inbox:

[![](https://blog.compass-security.com/wp-content/uploads/2024/08/image-3.png)](https://blog.compass-security.com/wp-content/uploads/2024/08/image-3.png)

Franky’s heart raced as she recalled the “pleasure” of eating a cupcake from the CFO a few months back. Not wanting to eat another one of… those cupcakes, Franky’s lizard brain kicks in and she clicks on the link instantly. There is no way she could refuse when the Chief Financial Officer offered one of her cupcakes! On the page, the typical username and password fields stared back at her. She starts typing her username… Suddenly, her rational brain comes back with a vengeance. Why is the password manager not offering to fill in username and password? Dread overcomes her. This wasn’t right! She hadn’t typed the password yet, but what if it was already too late? It should still be safe, right?

Have you or someone you know ever been in this situation? Then you were the target of a CEO fraud, where someone impersonates a CEO to get their hands on sensitive information. But how real the threat of the CFO’s cupcakes is? Let’s find out!

To answer these questions, let’s follow the email from creation to delivery. We will look at the email headers to find out if the email was really sent from Marly. If you want to follow along with an example, open any email sent from an external sender and find the headers. In Outlook, they can be found by opening the email in a new window, clicking on File, then Properties. The headers are listed under “Internet Headers” (as opposed to football headers?). In other tools, they are sometimes found under an option called “raw” which will show the raw email including the headers. MxToolbox has a [handy list](https://mxtoolbox.com/Public/Content/EmailHeaders/) of how to get to the headers in different email clients.

## Mail User Agent (MUA)

After clicking “send” in the email client (or the Email User Agent in [RFC 5068](https://datatracker.ietf.org/doc/html/rfc5068#section-2) parlance), the story of the headers begins immediately. The email client (Outlook, Apple Email, etc.) already adds the first few headers.

```
Date: Wed, 31 Jul 2024 12:30:25 +0000 (UTC)
From: Fictional Franky <[email protected]>
To: "Mythical Marly" <[email protected]>
Reply-To: Fictional Franky <[email protected]>
Message-ID: <[email protected]>
Subject: =?UTF-8?Q?_Invoice_Reminder:_Pay_Now_or_O?=
 =?UTF-8?Q?ur_CFO_Might_Start_Baking_=F0=9F=93=8A=F0=9F=8D=B0_?=
MIME-Version: 1.0
Content-Type: multipart/alternative;
    boundary="----=_Part_2011274_1670263300.1722429025822"
X-Emailer: WebService/1.1.22544 AolEmailNorrin
Content-Length: 40149
```

The clients usually adds a `Date`, `From`, `To`, and `Subject` header (though, according to [RFC 5322](https://datatracker.ietf.org/doc/html/rfc5322#section-3.6), only the `Date` and `From` headers are mandatory). They pretty much do what they say. The `Message-ID` is an ID generated either by the client or the Email Submission Agent (see next chapter). When replying to an email, the email client will add an `In-Reply-To` header containing the `Message-ID`. This makes it possible for email clients to group all messages that are replies to each other in a single thread. Another header of note is the `X-Emailer` header. If present, it shows which program was used to write the message.

The `Reply-To` header specifies an alternate email where a reply will be sent to. This is an optional header. Whenever the `Reply-To` header exists and points to a different email than the `From` header, it is worth investigation why. It could be benign, or it could be an threat actor that sends email from `[[email protected]](/cdn-cgi/l/email-protection)` but tries to receive the replys on a email under their control.

We once had a case where a customer was worried that not just the email account, but also the laptop was infected. The `X-Mailer` header showed that the email was sent from a Mac, while the customer only used Windows laptops. This was a strong indication that the laptop itself was not infected.

Of course, all these headers are added by the client and can be tampered with. The Mail Submission Agent (MSA, see next chapter) should validate that the `From` header is a valid value for the current user. The other fields are usually not validated, as the MSA does not have enough information. The `Date` header, for example, can be in the past in case the email was written offline and then later sent by the email client.

The email is then sent to the MSA.

## Mail Submission Agent (MSA)

The Mail Submission Agent (MSA) is the server where the emails are sent by the Mail User Agent. Basically, the server identified by the “smtp://” gibber-gabber we sometimes have to add manually to the email clients. The MSA verifies that the user is allowed to send emails for the email account listed in the `From` header and figures out how to forward the email to the recipients.

It, of course, also adds some headers! First, it adds a `Received` header to the top that states which Mail User Agent sent the email to the server. The server also adds a `DKIM-Signature`. The DKIM Signature is intended to verify that the email is not tampered with during transmission. More on the security features towards the end.

```
DKIM-Signature: v=1; a=rsa-sha256; c=relaxed/relaxed; d=aol.com; s=a2048; t=1722429146; bh=6ydO6GhkZaP9pOLY53HnWoZDVdbdjSBTwBNNzxVp3Uw=; h=Date:From:To:Subject:References:From:Subject:Reply-To; b=C3HMmETpQBa+I3zTypH2bNcrwIA7DphSNGRBh2dsyx48tENigvyREvImL0h+1lakBo0qt3dE5gygFQf2C9Y3UAelT7yVHmFReLV8P3ssQtYTdT03dIdKJUot/7SbinEAaLL0qjleSY7jCtj5Uk1WMWTSJRi1JOFleuvs3Vuy61n+nrfVIu8/ZRrQg3cBX0jjgRnfFVX/llArg0ijn/iIoqrXFxsw7iFoi78TjZbn0pFOD8cs0/xhdfh/aCMsq/xPpU2NYHFpZX7EYJuuqdog8kM+Yh51c6epwbMn6gn0ako8dJ7Jlx+L34MtD4FJPLRqeZxG4s3d2sNVpxE17Au6zA==
Received: from sonic.gate.mail.ne1.yahoo.com by sonic315.consmr.mail.ne1.yahoo.com with HTTP; Wed, 31 Jul 2024 12:32:26 +0000
```

For each email address in the `To`, `CC` and `BCC` headers, the server forwards the email to the Mail Transfer Agent (MTA) for that domain. The MTA is listed in the `MX` DNS record. For example, if an email is to be sent to “compass-security.com”, it will query the `MX` record of the domain:

```
$ dig compass-security.com +noall +answer MX
compass-security.com.   5       IN      MX      0 compasssecurity-com01i.mail.eo.outlook.com.
```

Here, the email...