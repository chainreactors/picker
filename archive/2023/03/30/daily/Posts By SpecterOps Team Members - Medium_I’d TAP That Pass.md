---
title: I’d TAP That Pass
url: https://posts.specterops.io/id-tap-that-pass-8f79fff839ac?source=rss----f05f8696e3cc---4
source: Posts By SpecterOps Team Members - Medium
date: 2023-03-30
fetch_date: 2025-10-04T11:09:32.747726
---

# I’d TAP That Pass

[Sitemap](/sitemap/sitemap.xml)

[Open in app](https://rsci.app.link/?%24canonical_url=https%3A%2F%2Fmedium.com%2Fp%2F8f79fff839ac&%7Efeature=LoOpenInAppButton&%7Echannel=ShowPostUnderCollection&%7Estage=mobileNavBar&source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Fposts.specterops.io%2Fid-tap-that-pass-8f79fff839ac&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

[Medium Logo](https://medium.com/?source=post_page---top_nav_layout_nav-----------------------------------------)

[Write](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-story&source=---top_nav_layout_nav-----------------------new_post_topnav------------------)

[Search](https://medium.com/search?source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Fposts.specterops.io%2Fid-tap-that-pass-8f79fff839ac&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

![](https://miro.medium.com/v2/resize:fill:64:64/1*dmbNkD5D-u45r44go_cf0g.png)

[## Posts By SpecterOps Team Members](https://posts.specterops.io/?source=post_page---publication_nav-f05f8696e3cc-8f79fff839ac---------------------------------------)

·

Follow publication

[![Posts By SpecterOps Team Members](https://miro.medium.com/v2/resize:fill:76:76/1*D-FDlfkqivRBQZoESrwtqw.png)](https://posts.specterops.io/?source=post_page---post_publication_sidebar-f05f8696e3cc-8f79fff839ac---------------------------------------)

Posts from SpecterOps team members on various topics relating information security

Follow publication

# I’d TAP That Pass

[![Daniel Heinsen](https://miro.medium.com/v2/resize:fill:64:64/1*GrMTMBFX3ZJ18iZClwxhcA.jpeg)](https://medium.com/%40hotnops?source=post_page---byline--8f79fff839ac---------------------------------------)

[Daniel Heinsen](https://medium.com/%40hotnops?source=post_page---byline--8f79fff839ac---------------------------------------)

15 min read

·

Mar 29, 2023

--

Listen

Share

## Summary:

Given that:

1. Temporary Access Passes (TAP) are enabled in the Azure AD tenant
   **AND**
2. You have an authentication admin role in Azure AD

You can assign users a short lived password called a Temporary Access Pass (TAP) that satisfies most multi-factor authentication requirements implemented in Azure AD conditional access without alerting the user or modifying their existing password. In addition, you can take advantage of the OAuth on-behalf-of (OBO) flow to maintain access to the target account, even after the TAP has expired. **Edit:** As of 3/24/2023, Microsoft has fixed the issue of refresh tokens remaining valid after a TAP has expired. I’ll elaborate further in the appropriate sections.

## Read First:

[## Configure a Temporary Access Pass in Azure AD to register Passwordless authentication methods …

### Passwordless authentication methods, such as FIDO2 and Passwordless Phone Sign-in through the Microsoft Authenticator…

learn.microsoft.com](https://learn.microsoft.com/en-us/azure/active-directory/authentication/howto-authentication-temporary-access-pass?source=post_page-----8f79fff839ac---------------------------------------)

[## Microsoft identity platform and OAuth2.0 On-Behalf-Of flow - Microsoft Entra

### The on-behalf-of (OBO) flow describes the scenario of a web API using an identity other than its own to call another…

learn.microsoft.com](https://learn.microsoft.com/en-us/azure/active-directory/develop/v2-oauth2-on-behalf-of-flow?source=post_page-----8f79fff839ac---------------------------------------)

## Drink First:

Coconut cream is key. Take this seriously.

[## The Painkiller Is an Easy, Delicious Tropical Cocktail

### (Nutrition information is calculated using an ingredient database and should be considered an estimate.) Save Recipe…

www.thespruceeats.com](https://www.thespruceeats.com/painkiller-cocktail-recipe-760473?source=post_page-----8f79fff839ac---------------------------------------)

## Intro

In order to add a Temporary Access Pass (TAP) to a user, you’ll need to be:

* an [authentication admin](https://learn.microsoft.com/en-us/azure/active-directory/roles/permissions-reference#authentication-administrator) OR
* [privileged authentication admin](https://learn.microsoft.com/en-us/azure/active-directory/roles/permissions-reference#privileged-authentication-administrator) OR
* [UserAuthenticationMethod.ReadWrite.All](https://graphpermissions.merill.net/permission/UserAuthenticationMethod.ReadWrite.All)

In addition, if you want to enable temporary access passes for the tenant, you’ll need to be either:

* An [Authentication Policy Administrator](https://learn.microsoft.com/en-us/azure/active-directory/roles/permissions-reference#authentication-policy-administrator) or jazzier OR
* [Policy.ReadWrite.AuthenticationMethod](https://graphpermissions.merill.net/permission/Policy.ReadWrite.AuthenticationMethod)

That’s a lot of privilege. If you have any of these privileges, you’ve likely already done some heavy lifting. However, this is still a powerful addition to our Azure AD tradecraft and by the end of this post, I’ll have you convinced that **TAPs are hella cool**.

On our red team engagements and penetration tests, conditional access policies (CAP) often hinder our ability to directly authenticate as a target user. We may have a set of elevated privileges, we may have valid credentials for a target user, but that last step of actually authenticating as the target user is becoming increasingly elusive. TAP abuse helps us with that issue in two ways:

1. We can add a temporary password to a victim user without invalidating their existing password, ensuring that the user won’t notice a password change. Even better, we aren’t forced to change a password on a critical automation account and potentially break some critical system, like a CI/CD pipeline. According to Microsoft documentation: “[Users can also continue to sign-in by using their password; a TAP doesn’t replace a user’s password.](https://learn.microsoft.com/en-us/azure/active-directory/authentication/howto-authentication-temporary-access-pass)”
2. As mentioned above, TAPs satisfy strong multi-factor authentication (MFA) requirements. This means that we can use this password directly, without needing a second factor like an application code or SMS.

## Satisfying MFA requirements with a TAP

Consider the following scenario:

Press enter or click to view image in full size

![]()

Example Scenario

In this scenario, an attacker has an agent installed on *User A*’s workstation, thus has the ability to perform actions in Azure AD as *User A*. *User A* is an authentication administrator. With this access, the attacker is attempting to authenticate as *User B.* There are two CAPs in place:

1. Users can only authenticate from the Target VPN
2. MFA is required

In this scenario, CAP 1 requires our attacker to pivot through *User A’s* workstation because the authentication attempts need to originate from the Target VPN. Because the attacker has the privilege of an authentication administrator, they *could* change the password of *User B*, but they would still be blocked by the MFA CAP. In addition, changing a user password is noisy as hell.

This is why we need a TAP.

To see the difference between a password token vs a TAP token, we can use [AADInternals](https://aadinternals.com/aadinternals/). The first login, shown below, is a vanilla login with no MFA and a normal password in an unauthenticated context:

```
# Unauthenticated context
$token = Get-AADIntAccessTokenForMSGraph -Credentials $cred
Parse-JWTtoken $token

aud                 : https://graph.microsoft.com
iss                 : https://sts.windows.net/6c12b0b0-b2cc-4a73-8252-0b94bfca2145/
...
acct                :...