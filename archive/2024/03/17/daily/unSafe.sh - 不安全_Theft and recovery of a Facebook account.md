---
title: Theft and recovery of a Facebook account
url: https://buaq.net/go-228550.html
source: unSafe.sh - 不安全
date: 2024-03-17
fetch_date: 2025-10-04T12:08:08.711894
---

# Theft and recovery of a Facebook account

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

![](https://8aqnet.cdn.bcebos.com/d6bac46edde9de1fe33a8898c3c5f3c2.jpg)

Theft and recovery of a Facebook account

This is the story of Vittoria (a pseudonym, henceforth referred to as V). A few days ago, V called m
*2024-3-16 21:46:39
Author: [www.adainese.it(查看原文)](/jump-228550.htm)
阅读量:23
收藏*

---

[![Post cover](https://www.adainese.it/blog/2023/09/26/theft-and-recovery-of-a-facebook-account/evidence4.webp)](https://www.adainese.it/blog/2023/09/26/theft-and-recovery-of-a-facebook-account/evidence4.webp)

This is the story of Vittoria (a pseudonym, henceforth referred to as V). A few days ago, V called me in an emergency: her Facebook account had been stolen by Nhang (a pseudonym, henceforth referred to as N). Identity theft is a criminal offense, sanctioned by Article 494 of the Penal Code. This information will be useful later on.

[![Evidence 4](https://www.adainese.it/blog/2023/09/26/theft-and-recovery-of-a-facebook-account/evidence4.png)](https://www.adainese.it/blog/2023/09/26/theft-and-recovery-of-a-facebook-account/evidence4.png)

For those who use Facebook for their work, such an event is extremely traumatic and must be handled with all due caution.

## The Facts

* Wednesday, V receives notifications on Facebook warning her of abnormal activity on her account. V followed the instructions by reporting the suspicious activity, but being on a mobile device, she was unable to change the password or activate multi-factor authentication.
* Thursday, 7:37 PM: Verify your payment method to resume posting ads (
  [Attachment 1](https://www.adainese.it/blog/2023/09/26/theft-and-recovery-of-a-facebook-account/evidence1.png "Evidence 1")
  )
* Thursday, 7:39 PM: Have you just added an email address? (
  [Attachment 2](https://www.adainese.it/blog/2023/09/26/theft-and-recovery-of-a-facebook-account/evidence2.png "Evidence 2")
  )
* Friday, 12:38 AM: Have you just removed your phone number? (
  [Attachment 3](https://www.adainese.it/blog/2023/09/26/theft-and-recovery-of-a-facebook-account/evidence3.png "Evidence 3")
  )
* Friday, 12:39 AM: Have you just removed your email address? (
  [Attachment 4](https://www.adainese.it/blog/2023/09/26/theft-and-recovery-of-a-facebook-account/evidence4.png "Evidence 4")
  )

From this point on, V can no longer access her account either from her computer or her phone. Additionally, V notices that the account now displays the name and surname of N.

We can imagine what happened:

* V’s password was stolen. This action is possible through numerous techniques ranging from simple phishing portals, the use of more or less public data breaches, to the use of so-called Infostealers.
* V’s account was not protected with multi-factor authentication (MFA).
* N was able to access V’s account and, by changing the password, email, and phone number, locked out V.

## Facebook’s First Failure

For those working in the field of cybersecurity, these types of events represent a series of indicators that, given V’s typical behavior, indicate a compromise (commonly referred to as Behavioral Indicators of Compromise or BIoC). Trying to describe the mechanism simply, each event receives a score, and the group of events is evaluated not individually, but based on the group score.

Specifically:

* If an Italian profile, with accesses only from Italy, is accessed from Vietnam, the event is highly suspicious and we assign it a score of 9/10.
* If a user changes their account password and has never done so before, the event may be suspicious and we assign it a score of 1/10.
* If a user replaces an email, the event may be suspicious and we assign it a score of 6/10.
* If a user removes or replaces their phone number, the event may be suspicious and we assign it a score of 6/10.
* If a user replaces their profile’s name and surname in a radically different way, the event is highly suspicious and we assign it a score of 9/10.

It doesn’t take a security expert to understand that these 5 events, taken together, conclusively determine a compromise of the account.

## Facebook’s First Attempt and Failure

For each event described in the facts paragraph, Facebook sent V an email: by clicking on the “Not me” link, a procedure was triggered that should have allowed V to undo the actions and regain control of her account.

But it didn’t go that way.

V had to send Facebook, via webcam, a live recording of her identity document. But Facebook’s automatic system deemed the information insufficient to recognize V and restore her account access, leaving it with N.

Again, it doesn’t take a security expert to understand that if V uses an official Facebook email to report fraudulent activity, it is highly likely that the event was indeed fraudulent, and the account modification actions should be reversed.

## Account Recovery and Facebook’s Failure

V had two more Facebook emails with links to attempt account recovery. Another attempt failed, but with some difficulty, V managed to activate the third recovery procedure. V now chooses to use not the identity document that always appeared blurred, but the passport: she takes the time to take a good photo of the document with her phone, and this time Facebook recognizes V’s identity and sends her two emails for recovery:

* New email address added to Facebook (
  [Attachment 5](https://www.adainese.it/blog/2023/09/26/theft-and-recovery-of-a-facebook-account/evidence5.png "Evidence 5")
  ).
* You can now access your account again (
  [Attachment 6](https://www.adainese.it/blog/2023/09/26/theft-and-recovery-of-a-facebook-account/evidence6.png "Evidence 6")
  ).

These two emails should be used in the exact order described above: first, the email address must be confirmed with the corresponding confirmation code, then access to the account can be regained with the temporary password and PIN provided in the email.

But it’s not over yet.

V manages to access the account, but the email change procedure fails. So, she finds an account:

* for which she does not know the password (the one in the email is a temporary password to be used once);
* associated with N’s email;
* associated with N’s phone number.

V soon realizes that any attempt to change the password, replace the email, or phone number requires a password, but not the one she possesses; the password requested is the one used by N to lock V out.

However, there is a procedure to proceed even without knowing the password, but it requires a confirmation PIN, sent to N’s email or phone.

[![Missing account](https://www.adainese.it/blog/2023/09/26/theft-and-recovery-of-a-facebook-account/missing_account.png)](https://www.adainese.it/blog/2023/09/26/theft-and-recovery-of-a-facebook-account/missing_account.png)

In a moment of desperation and intuition at the same time, V tries again to open the Facebook app from her phone, which automatically logs into Facebook but requires confirmation from an already open session. Now V can authorize access from the phone using the previously opened session on the computer, and in no time, V manages to change the email, phone number, and set up multi-factor authentication.

But V cannot change the name and surname for two months: it’s a Facebook security policy. V will be presented to her friends as Nhang for two months.

## Other Facebook Failures

In retrospect, I can say that V, despite claiming to have difficulty with technology, reacted well: she had a good degree of autonomy, had excellent insights, and did not get discouraged. And yes, considering how Facebook’s security systems don’t work, she was also very lucky.

So let’s see the other failures of Facebook:

* There is ...