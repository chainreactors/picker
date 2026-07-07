---
title: Mass Assignment and the Identity Drift: From Profile Edit to Insurance Takeover
url: https://infosecwriteups.com/mass-assignment-and-the-identity-drift-from-profile-edit-to-insurance-takeover-5eb2be4c1f8e?source=rss----7b722bfd1b8d--bug_bounty
source: Bug Bounty in InfoSec Write-ups on Medium
date: 2026-07-06
fetch_date: 2026-07-07T06:03:25.095711
---

# Mass Assignment and the Identity Drift: From Profile Edit to Insurance Takeover

[Sitemap](/sitemap/sitemap.xml)

[Open in app](https://play.google.com/store/apps/details?id=com.medium.reader&referrer=utm_source%3DmobileNavBar&source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fmass-assignment-and-the-identity-drift-from-profile-edit-to-insurance-takeover-5eb2be4c1f8e&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

[Medium Logo](https://medium.com/?source=post_page---top_nav_layout_nav-----------------------------------------)

Get app

[Write](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-story&source=---top_nav_layout_nav-----------------------new_post_topnav------------------)

[Search](https://medium.com/search?source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fmass-assignment-and-the-identity-drift-from-profile-edit-to-insurance-takeover-5eb2be4c1f8e&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

![Unknown user](https://miro.medium.com/v2/resize:fill:64:64/1*dmbNkD5D-u45r44go_cf0g.png)

[## InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---publication_nav-7b722bfd1b8d-5eb2be4c1f8e---------------------------------------)

·

1. [The Profile](/?source=post_page-----5eb2be4c1f8e---------------------------------------#aa39 "The Profile")
2. [The Request](/?source=post_page-----5eb2be4c1f8e---------------------------------------#a529 "The Request")
3. [Identity Drift](/?source=post_page-----5eb2be4c1f8e---------------------------------------#c5d2 "Identity Drift")
4. [The Second Escalation](/?source=post_page-----5eb2be4c1f8e---------------------------------------#4395 "The Second Escalation")
5. [The Chain](/?source=post_page-----5eb2be4c1f8e---------------------------------------#8838 "The Chain")
6. [Re-Evaluation](/?source=post_page-----5eb2be4c1f8e---------------------------------------#495a "Re-Evaluation")
7. [Remediation](/?source=post_page-----5eb2be4c1f8e---------------------------------------#2df7 "Remediation")

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:76:76/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_sidebar-7b722bfd1b8d-5eb2be4c1f8e---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

# Mass Assignment and the Identity Drift: From Profile Edit to Insurance Takeover

[![Alvin Ferdiansyah](https://miro.medium.com/v2/resize:fill:64:64/1*jCQW4Dcioim59s1E0JwOqQ@2x.jpeg)](https://alvinferd.medium.com/?source=post_page---byline--5eb2be4c1f8e---------------------------------------)

[Alvin Ferdiansyah](https://alvinferd.medium.com/?source=post_page---byline--5eb2be4c1f8e---------------------------------------)

7 min read

·

Jun 13, 2026

--

[Listen](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2Fplans%3Fdimension%3Dpost_audio_button%26postId%3D5eb2be4c1f8e&operation=register&redirect=https%3A%2F%2Finfosecwriteups.com%2Fmass-assignment-and-the-identity-drift-from-profile-edit-to-insurance-takeover-5eb2be4c1f8e&source=---header_actions--5eb2be4c1f8e---------------------post_audio_button------------------)

Share

Press enter or click to view image in full size

![]()

> No customer support call. No re-verification.
>
> Yet the name changes. The date of birth changes. The government ID number changes. But the eKYC status remains verified and every system that relies on that identity continue trusting the account as if nothing happened.

Mass Assignment happens when an application takes fields from a user-controlled request and applies them to an internal object without checking which fields are allowed to change.

A simple version looks like this:

```
{
"name": "Researcher",
"is_admin": true
}
```

The developer may have intended to update only the name. But if the backend assigns every submitted field into the user object, the extra is\_admin value may be written too.

The important part is not the admin flag. The important part is the missing field-level decision. The server should ask “this user is allowed to update this object, but are they allowed to update this field?”

That question matters because one object can contain fields with very different levels of trust. A profile object can contain a nickname, height, weight, legal name, birthdate, government ID number, verification status, and insurance metadata. They may sit next to each other in JSON, but they do not mean the same thing.

Well, most people first meet Mass Assignment through the admin flag example. A request is supposed to update a name. The attacker adds is\_admin. The backend saves it. The user becomes an admin. That example is useful because it is easy to remember. It is also cleaner than most real findings.

This one started in a quieter place: an edit profile endpoint.

Changing a first name is normal.

Changing a verified government ID number is not.

Changing identity itself after verification is definitely not.

Once an account has passed eKYC, attributes such as name, date of birth, gender, and government-issued identification become part of the trust model. They are no longer profile preferences. **They are identity claims.**

If those claims can be rewritten while the verification status remains intact, the problem is no longer profile editing. *It becomes identity drift.*

This writeup is about that chain: Mass Assignment, identity drift, and a second-order insurance impact.

## The Profile

The target was a platform with web and mobile applications. It stored user profile data, supported verified identity, and allowed users to link a third-party insurance or benefit record to their account.

The profile had ordinary fields and sensitive identity fields. From the normal application flow, some of these fields were restricted after we completed the eKYC verification . If a user wanted to change them, the expected path was customer support or another verification process.

Press enter or click to view image in full size

![]()

That business rule made sense. Once a field is used to represent identity, changing it should require more care than changing a preference.

The frontend understood this. The sensitive fields were not exposed as normal editable fields.

The backend did not enforce the same boundary.

## The Request

The only attribute that could be edited directly through this flow was the phone number.

In simplified form, the request generated by the application looked like this:

```
PUT /api/v1/profile/{user_id}/phone HTTP/2
Host: api.[REDACTED]
Cookie: [REDACTED]
Content-Type: application/json

{
  "phone_number": "+628123456789"
}
```

The user was authenticated. The profile belonged to the user. The endpoint was meant to update a phone number and nothing more.

The test was simple: add fields the UI did not send in this flow.

```
PUT /api/v1/profile/{user_id}/phone HTTP/2
Host: api.[REDACTED]
Cookie: [REDACTED]
Content-Type: application/json

{
  "phone_number": "+628123456789",
  "first_name": "EditedFirstName",
  "last_name": "EditedLastName",
  "date_of_birth": "1990-01-01",
  "id_number": "0000000000000000",
  "nationality": "Indonesia"
}
```

The server returned success.

That was interesting, but it was not enough.

With Mass Assignment testing, 200 OK is only a signal. Some APIs accept a body, return success, and silently drop fields they do not want to save. If the value does not persist, the finding is much weaker.

So I read the profile back from the appl...