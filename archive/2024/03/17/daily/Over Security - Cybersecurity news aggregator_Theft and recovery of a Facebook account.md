---
title: Theft and recovery of a Facebook account
url: https://www.adainese.it/blog/2023/09/26/theft-and-recovery-of-a-facebook-account/
source: Over Security - Cybersecurity news aggregator
date: 2024-03-17
fetch_date: 2025-10-04T12:10:04.897507
---

# Theft and recovery of a Facebook account

# [Andrea Dainese](/)

* [Home](/)
* [About](/#about)
* [Blog](/blog)
* [Categories](/categories)

# Theft and recovery of a Facebook account

#### Table of contents

* [The Facts](#the-facts)
* [Facebook’s First Failure](#facebooks-first-failure)
* [Facebook’s First Attempt and Failure](#facebooks-first-attempt-and-failure)
* [Account Recovery and Facebook’s Failure](#account-recovery-and-facebooks-failure)
* [Other Facebook Failures](#other-facebook-failures)
* [Criminal Offense](#criminal-offense)
* [Lesson Learned](#lesson-learned)
* [An Open Question](#an-open-question)

#### Latest posts

[![Post cover](/images/categories/learning-paths.webp)](/blog/2025/10/01/circular-dependencies-with-ndo/)

[Circular Dependencies with NDO](/blog/2025/10/01/circular-dependencies-with-ndo/)
October 01, 2025

[![Post cover](/images/vendors/paloalto.webp)](/blog/2025/09/28/modifying-an-object-in-strata-cloud-manager/)

[Modifying an object in Strata Cloud Manager](/blog/2025/09/28/modifying-an-object-in-strata-cloud-manager/)
September 28, 2025

[![Post cover](/images/categories/learning-paths.webp)](/blog/2025/09/24/from-single-site-to-multi-site-with-ndo/)

[From Single-Site to Multi-Site with NDO](/blog/2025/09/24/from-single-site-to-multi-site-with-ndo/)
September 24, 2025

[![Post cover](/images/vendors/paloalto.webp)](/blog/2025/09/21/retrieving-firewall-interfaces-with-strata-cloud-manager/)

[Retrieving firewall interfaces with Strata Cloud Manager](/blog/2025/09/21/retrieving-firewall-interfaces-with-strata-cloud-manager/)
September 21, 2025

[![Post cover](/images/vendors/eve-ng.webp)](/blog/2025/09/20/eve-ng-linux-vm-ssh-troubleshooting/)

[EVE-NG Linux VM SSH troubleshooting](/blog/2025/09/20/eve-ng-linux-vm-ssh-troubleshooting/)
September 20, 2025

#### Categories

[![Category cover](/images/categories/automation.webp)](/categories/automation)

[Automation](/categories/automation)
 159 posts

[![Category cover](/images/categories/learning-paths.webp)](/categories/learning-paths)

[Learning paths](/categories/learning-paths)
 123 posts

[![Category cover](/images/categories/ciso.webp)](/categories/ciso)

[CISO](/categories/ciso)
 23 posts

[![Category cover](/images/categories/personal-security.webp)](/categories/personal-security)

[Personal Security](/categories/personal-security)
 22 posts

[![Category cover](/images/categories/security.webp)](/categories/security)

[Security](/categories/security)
 20 posts

[![Category cover](/images/categories/notes.webp)](/categories/notes)

[Notes](/categories/notes)
 19 posts

[![Category cover](/images/categories/infrastructure.webp)](/categories/infrastructure)

[Infrastructure](/categories/infrastructure)
 12 posts

[![Category cover](/images/categories/ot-ics.webp)](/categories/ot-ics)

[OT/ICS](/categories/ot-ics)
 5 posts

[![Category cover](/images/categories/books.webp)](/categories/books)

[Books](/categories/books)
 3 posts

[![Category cover](/images/categories/unetlab.webp)](/categories/unetlab)

[UNetLab](/categories/unetlab)
 3 posts

[![Category cover](/images/categories/writeup.webp)](/categories/writeup)

[Write-up](/categories/writeup)
 3 posts

[![Category cover](/images/categories/osint.webp)](/categories/osint)

[OSInt](/categories/osint)
 2 posts

[![Category cover](/images/categories/life.webp)](/categories/life)

[My life](/categories/life)
 1 posts

## Theft and recovery of a Facebook account

Andrea Dainese

September 26, 2023

[Personal Security](/categories/personal-security/ "All posts under Personal Security")

[![Post cover](/blog/2023/09/26/theft-and-recovery-of-a-facebook-account/evidence4.webp)](/blog/2023/09/26/theft-and-recovery-of-a-facebook-account/evidence4.webp)

This is the story of Vittoria (a pseudonym, henceforth referred to as V). A few days ago, V called me in an emergency: her Facebook account had been stolen by Nhang (a pseudonym, henceforth referred to as N). Identity theft is a criminal offense, sanctioned by Article 494 of the Penal Code. This information will be useful later on.

[![Evidence 4](/blog/2023/09/26/theft-and-recovery-of-a-facebook-account/evidence4.png)](/blog/2023/09/26/theft-and-recovery-of-a-facebook-account/evidence4.png)

For those who use Facebook for their work, such an event is extremely traumatic and must be handled with all due caution.

## The Facts

* Wednesday, V receives notifications on Facebook warning her of abnormal activity on her account. V followed the instructions by reporting the suspicious activity, but being on a mobile device, she was unable to change the password or activate multi-factor authentication.
* Thursday, 7:37 PM: Verify your payment method to resume posting ads (
  [Attachment 1](evidence1.png "Evidence 1")
  )
* Thursday, 7:39 PM: Have you just added an email address? (
  [Attachment 2](evidence2.png "Evidence 2")
  )
* Friday, 12:38 AM: Have you just removed your phone number? (
  [Attachment 3](evidence3.png "Evidence 3")
  )
* Friday, 12:39 AM: Have you just removed your email address? (
  [Attachment 4](evidence4.png "Evidence 4")
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

V had two more Facebook emails with links to attempt account recovery. Another attempt failed, but with some difficulty, V managed to activate the third recovery procedure. V now chooses to use not the identity document that always appeared blurred, but the passport: she takes the time to take a good photo of the document with her phone...