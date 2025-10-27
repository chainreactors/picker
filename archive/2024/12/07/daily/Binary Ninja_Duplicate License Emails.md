---
title: Duplicate License Emails
url: https://binary.ninja/2024/12/05/duplicate-license-emails.html
source: Binary Ninja
date: 2024-12-07
fetch_date: 2025-10-06T19:38:30.028990
---

# Duplicate License Emails

[![](/images/binary-ninja-logo.svg)](/)

* [Features](/features/)
* [Enterprise](/enterprise/)
* [Sidekick](https://sidekick.binary.ninja)
* [Cloud](https://cloud.binary.ninja)
* [Training](/training/)
* [Support](/support/)

  [Extended Support](/support/extended.html)
  [Documentation](/support/#documentation)
  [License/Installer Recovery](/recover/)
  [Renew Current License](/renew/)
  [Slack Signup](https://slack.binary.ninja/)
  [FAQ](/faq/)
  [Sponsorship Information](/sponsorship/)
  [Portal](https://portal.binary.ninja/)
  [Contact Us](/support/)
* [Blog](/blog/)
* [Gear](https://shop.binary.ninja)

[Free](/free)
[Purchase](/purchase)

Participate in our [Reverse Engineering Survey](/survey/) to win free licenses or admission to [RE//verse](https://re-verse.io/)!

# Binary Ninja Blog

## Duplicate License Emails

* [Jordan Wiens](https://github.com/psifertex)
* [Josh Ferrell](https://github.com/negasora)
* 2024-12-05
* [announcements](/tag/announcements)

![Apologetic Binary Ninja >](/blog/images/sorry.png)

This evening at 17:56:47 ET on 2024-12-05, a bug in our license/update server caused a large number of license emails to be sent to users with an active license. The short summary is that this was not a security incident, no customer data was exposed, no extra purchases were triggered. We donât actually have the ability to trigger additional purchases as we donât store payment information, our credit card processor handles those details.

If youâd like more details into the timeline, what happened to cause the bug and what weâve done to prevent it from happening again, read on!

## Background

Weâve been building out a new customer portal for several months. There are a few goals for the portal. First, weâd like to enable larger organizations to better manage their licenses, renew them in bulk, transfer between users, etc. Second, weâd like to enable users who were previous customers and have not maintained support to have access to old stable versions of Binary Ninja. Our original update server design didnât allow users to download specific older builds and we knew that we wanted to add it at some point.

Hopefully in the next few weeks (or early 2025) weâll be able to show the fully fledged version of this portal and it will make everyoneâs life easier! (Including ours! The portal also means customers can self-service many types of transactions that currently require manual processing.)

Earlier today we pushed a change to our license server to support these changes. The change was fine during testing, right up until itâ¦ wasnât.

## Timeline

**2024-12-05 13:00 ET - 16:00 ET**
:   We migrated the license server to the new codebase and database including testing functionality such as recovering licenses, purchasing, and renewing.

**17:56 ET**
:   A user requests a license recovery, triggering the bug.

**17:56 ET - 18:05 ET**
:   Users begin to contact Vector 35 about the extra emails.

**18:05 ET**
:   Having received the many notices and confirming the duplicates, we begin investigating.

**18:11 ET**
:   Unable to identify the immediate cause, we decide to reboot the infrastructure to see if the emails stop.

**18:13 ET**
:   Confirming the reboot did not resolve the emails (in hindsight likely most were stuck in the outbound SES queue already), we powered off the newly migrated license server.

**18:19 ET**
:   We disable all outbound SES email and begin formulating customer communications.

**18:29 ET**
:   We post to our internal Slack, public Twitter, and Mastodon to let people know about the issue and actions we've taken.

**19:00 ET**
:   We continue to reply to customer communications as well as investigate all the available logs to determine the bug.

**19:55 ET**
:   After confirming that the mail was being blocked outbound, we brought the server back up so that users could still check for updates and switch versions.

**20:22 ET**
:   We investigated both the server logs and source code and identified the flaw that caused the failure. Next up, much more testing and careful monitoring!

**22:25 ET**
:   We post this blog and re-enabled email sending for license purchase/recovery!

## The Bug

But wait, we said we tested license recovery. So how did a new request for a license recovery cause the flood of emails? If a user requested to recover the licenses associated with their email, and their email didnât have a [Ninja ID](https://accounts.binary.ninja/) associated, recovery emails would be sent for ALL licenses without an associated Ninja ID. The intended logic here is to handle the case where we are migrating users off of the purely email-based license system to the new customer portal which is backed by Ninja IDs (the same ID you use to manage your [Sidekick](https://sidekick.binary.ninja) logins). In the coming weeks youâll be able to associate your account and your license so you can also use the portal to manage your license or download previous versions after support ends!

You can see this bug in the following simplified code:

```
def recover():
    email = params.get('email')
    ...
    try:
        user = User.objects.get(email=email)
    except User.DoesNotExist:
        user = None
    ...
    license_selection_query = Q(email__iexact=email) | Q(user=user) # <- BUG
    licenses = License.objects.filter(license_selection_query)
    ...
    send_license_emails(licenses)
```

When user was `None`, licenses would contain all `License` objects where the email address matches, or has no associated user (which is *all* of themâ¦ oops.)

## The Fix

The fix here is obviously not to match Licenses on `user` when `user` is `None`, or essentially changing the code to:

```
...
license_selection_query = Q(email__iexact=email)
if user is not None:
    license_selection_query |= Q(user=user)
...
```

## Other Mitigations

Once weâve recovered after a good nightâs sleep weâll re-visit this and consider other longer-term mitigations we might take.

More robust testing might have caught this condition, some rate limits on the account doing the sending at the email provider level could have prevented this, weâll see what makes the most sense with the benefit of hindsight.

## FAQ

**Q:** Why didn't you catch this in testing?
:   **A:** Because the license we used in testing *had* an associated account already and we missed the failure condition.

**Q:** Was any user data exposed?
:   **A:** Nope, you just got extras of the licenses you could always get at any time by going to the license recovery page.

**Q:** Why do the emails say I purchased Binary Ninja?!
:   **A:** Historically, our license recovery page just triggered a fresh email that looked the same as a purchase. We're changing that going forward to make it more clear which is which (sorry to introduce anxiety that we might have charged you again!)

## About Us

Binary Ninja is brought to you by Vector 35, a group of hackers who started to make games and reverse engineering tools. Or, maybe they're game developers who still think they can hack? Either way, they're having fun doing it.

Â© 2015-2025 Vector 35. All rights reserved.

Binary NinjaÂ® is a registered trademark of Vector 35.

## Contact Us

Vector 35
PO Box 971
Melbourne, FL 32902

[[email protected]](/cdn-cgi/l/email-protection#b1d3d8dfd0c3c8dfd8dfdbd0f1c7d4d2c5dec382849fd2dedc)

+1-866-983-3135

[Slack](https://slack.binary.ninja/)

## [Changelog](/changelog/)

[Software EULA](https://docs.binary.ninja/about/license.html)

[Privacy Policy](/privacy/)