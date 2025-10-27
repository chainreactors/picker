---
title: Reversing WordPress CVEs: Baby Steps
url: https://infosecwriteups.com/reversing-wordpress-cves-baby-steps-1069feb50dd4?source=rss----7b722bfd1b8d--bug_bounty
source: Bug Bounty in InfoSec Write-ups on Medium
date: 2023-08-21
fetch_date: 2025-10-04T11:59:16.265790
---

# Reversing WordPress CVEs: Baby Steps

[Sitemap](/sitemap/sitemap.xml)

[Open in app](https://rsci.app.link/?%24canonical_url=https%3A%2F%2Fmedium.com%2Fp%2F1069feb50dd4&%7Efeature=LoOpenInAppButton&%7Echannel=ShowPostUnderCollection&%7Estage=mobileNavBar&source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Freversing-wordpress-cves-baby-steps-1069feb50dd4&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

[Medium Logo](https://medium.com/?source=post_page---top_nav_layout_nav-----------------------------------------)

[Write](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-story&source=---top_nav_layout_nav-----------------------new_post_topnav------------------)

[Search](https://medium.com/search?source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Freversing-wordpress-cves-baby-steps-1069feb50dd4&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

![](https://miro.medium.com/v2/resize:fill:64:64/1*dmbNkD5D-u45r44go_cf0g.png)

[## InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---publication_nav-7b722bfd1b8d-1069feb50dd4---------------------------------------)

·

Follow publication

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:76:76/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_sidebar-7b722bfd1b8d-1069feb50dd4---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow publication

# Reversing WordPress CVEs: Baby Steps

[![Debangshu Kundu](https://miro.medium.com/v2/resize:fill:64:64/1*fqBp7Dj3PDkaC90Ntv3cVA.jpeg)](https://medium.com/%40DK999?source=post_page---byline--1069feb50dd4---------------------------------------)

[Debangshu Kundu](https://medium.com/%40DK999?source=post_page---byline--1069feb50dd4---------------------------------------)

5 min read

·

Aug 20, 2023

--

Listen

Share

Hey all! My first post in a long time. While this isn’t a super brainy one, reproducing it was surely fun.

## Introuction :-

While searching for fun CVEs in Wordpress Plugins, [CVE-2023–2834](https://www.cve.org/CVERecord?id=CVE-2023-2834) caught our eye. The plugin **Bookit** was vulnerable to an Authentication Bypass. As per Patchstack, this was a CVSS 9.8 issue, meaning it was quite impactful! Hence, me and

[Arpeet Rathi](https://medium.com/u/6293eaa6ea87?source=post_page---user_mention--1069feb50dd4---------------------------------------)

 decided to take a look.

Wordpress Bookit Plugin provides the shortcode ‘`[bookit]`‘ to embed an appointment booking calendar into your WordPress site. Users can register for a booking appointment by providing the date and time followed by name, email address, and password for registration.

### Issue Description :-

Versions <2.3.6 of Wordpress Bookit Plugin allow unauthenticated attackers to log in as any existing user on the site, even an administrator, only with the added requirement of knowing their email address.

Press enter or click to view image in full size

![]()

Credits to the original author [Lana Codes](https://patchstack.com/database/researcher/46444da6-46e2-4b6b-9eff-b801e5f3e5ba). Wordfence already has a blog explaining the [patch](https://www.wordfence.com/blog/2023/06/stylemixthemes-addresses-authentication-bypass-vulnerability-in-bookit-wordpress-plugin/).

Lana Codes also has a detailed [writeup](https://lana.codes/lanavdb/0dea1346-fd60-4338-8af6-6f89c29075d4/) on this, that we somehow missed out.

## Technical Details :-

Reviewing the [CVE-2023–2384](https://www.cve.org/CVERecord?id=CVE-2023-2834) record, we are able to deduce the following :-

* The vulnerable version of Bookit Plugin is 2.3.6

Press enter or click to view image in full size

![]()

Wordpress itself provides a self-hosted feature at `plugins.trac.wordpress.org` to view and track changes in plugin versions allowing us to patch diff easily.

Press enter or click to view image in full size

![]()

### Patch Analysis :-

Now, we need two versions, the vulnerable one (2.3.6) and the initial patch (2.3.7) each assigned their revision numbers, 2911433 (2.3.6) and 2919536 (2.3.7) on <https://plugins.trac.wordpress.org/log/bookit/>

Press enter or click to view image in full size

![]()

Bookit — Changeset

Select the versions to Diff (From 2919536 (2.3.7) To 2911433(2.3.6)) and hit `View Changes`

The Changeset interface opens displaying an overview of all additions, edits, and deletions made to the included files.

Press enter or click to view image in full size

![]()

Browsing through the edits made, we arrive at the *get\_customer* function in `/includes/classes/CustomerController.php`

![]()

Going over the previous version’s code (highlighted in green) we are able to deduce that the code first checks if *$data* contains a `user\_id and retrieves the customer’s ID using the `Customers::get` method. However, if the `user_id` field is not present, it retrieves the customer's ID using the `email` parameter, which in-fact is user-supplied.

Now, it retrieves settings using the `SettingsController::get_settings()` method. If the booking type here is set to "registered" and the user is not already logged in (`!is_user_logged_in()`), the code proceeds to start the authentication process.

It first retrieves the user ID associated with the customer using the `Customers::save_or_get_wp_user($data)` method. We already know the `user_id` field is user-supplied and can easily be set to the administrator’s email. It now proceeds to clear the Auth Cookie and set the current user to the specified `user_id` and then set the Auth Cookie corresponding to the same `user_id,` effectively logging the user in.

The `/database/Customers.php` responsible for creating the user, if not found in the database.

![]()

`/database/Customers.php`

So, in theory, this application would let us specify an email while booking an appointment and if the email corresponds to a user ID, it switches the authentication from the current user to the one linked with the email, potentially allowing an admin takeover!

*(Enough said let’s get to the exploit now!)*

## Exploitation and PoC :-

We create a sample website and host the Bookit Plugin via the shortcode `[bookit]`

* This creates a page with a Booking Appointment Widget as shown below :-

Press enter or click to view image in full size

![]()

* Fill in all the details and enter the admin’s email and click Book Now.

Press enter or click to view image in full size

![]()

* This sends the following request to `/wp-admin/admin-ajax.php?action=bookit_book_appointment`

Press enter or click to view image in full size

![]()

* Once, the requirement for the admin’s email ID is met, the server issues the following response setting the cookies to admin and effectively logging us as administrator!

Press enter or click to view image in full size

![]()

* Successfully Logged In!

Press enter or click to view image in full size

![]()

### Video Proof Of Concept :-

But wait! Did you notice something in the patch?

Yes! For y’all clever eyes, you’re right!

The initial patch now, let’s us to login as any other user who is not an admin by issuing us cookies for the same! Hence, one can still **takeover** accounts of Author/other lower privileged users. Still a win-win.

![]()

> This vulnerability was eventually patched in the version **2.3.8** of Bookit Plugin and versions upwards of 2.3.7 are unaffected.

Press enter or click t...