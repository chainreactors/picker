---
title: Managed Apple Accounts which were out of scope for ABM or ASM federation may be changed to be in scope by the federation process
url: https://derflounder.wordpress.com/2024/10/21/managed-apple-accounts-which-were-out-of-scope-for-abm-or-asm-federation-may-be-changed-to-be-in-scope-by-the-federation-process/
source: Der Flounder
date: 2024-10-22
fetch_date: 2025-10-06T18:47:31.595063
---

# Managed Apple Accounts which were out of scope for ABM or ASM federation may be changed to be in scope by the federation process

# [Der Flounder](https://derflounder.wordpress.com/)

Seldom updated, occasionally insightful.

* [Home](https://derflounder.wordpress.com/ "Home")
* [About](https://derflounder.wordpress.com/about-2/)
* [Contact](https://derflounder.wordpress.com/contact/)

[Home](https://derflounder.wordpress.com/ "Go to homepage")
> [Apple Business Manager](https://derflounder.wordpress.com/category/apple-business-manager/), [Apple School Manager](https://derflounder.wordpress.com/category/apple-school-manager/), [Managed Apple Accounts](https://derflounder.wordpress.com/category/managed-apple-accounts/) > Managed Apple Accounts which were out of scope for ABM or ASM federation may be changed to be in scope by the federation process

## Managed Apple Accounts which were out of scope for ABM or ASM federation may be changed to be in scope by the federation process

October 21, 2024
[rtrouton](https://derflounder.wordpress.com/author/rtrouton/ "Posts by rtrouton") [Leave a comment](#respond)
[Go to comments](#comments)

In [Apple Business Manager](https://support.apple.com/guide/apple-business-manager/sign-up-axm402206497/web) (ABM) or [Apple School Manager](https://support.apple.com/guide/apple-school-manager/sign-up-axm402206497/web) (ASM), you can link to your identity provider (IdP) to ABM and ASM. This allows folks to sign in to Apple devices with the same username and password that they use to log into systems used at their company, school or institution. Apple refers to this as [federated authentication](https://support.apple.com/guide/apple-business-manager/intro-to-federated-authentication-axmb19317543/web) and supports this by creating [Managed Apple Accounts](https://support.apple.com/guide/deployment/managed-apple-accounts-depcaa668a58/web) (MAA) with the username and email address of the user in question, where that information is being provided by that company, school or institution’s IdP. Once this federation process is completed, when someone tries to use their MAA to log into an Apple system, they’ll be provided with the login screen for that company, school or institution’s IdP, in place of using Apple’s own authentication system for Apple Accounts.

However, prior to the federation process happening, a company, school or institution may have manually created MAAs in ABM / ASM for various purposes and want them to keep using Apple’s own authentication system for Apple Accounts in place of authentication using their company, school or institution’s IdP.

This usually applies to MAAs which are used as service accounts in ABM / ASM, where there may only an email alias set up in place of an actual user account set up in the IdP for that MAA. In those scenarios, if there’s no actual user account in the IdP for that MAA, authentication becomes impossible if ABM or ASM is forwarding authentication requests to the IdP.

The best practice in this case is to assign the MAAs in question to a domain which is different from the one being federated. So if you’re planning to federate accounts in the **company.com** domain, you would set up a different domain in ABM or ASM which is not **company.com** and assign those MAAs to that different domain. However, there’s an additional step to take as part of this domain re-assignment process. In addition to assigning the MAA to a different domain, you also need to make sure that the associated email address used with the MAA is also not part of the domain you’re planning to federate.

Why is this? [As part of the documentation Apple provides for the federation process](https://support.apple.com/guide/apple-business-manager/federated-authentication-identity-provider-axmfcab66783/web) , there’s this note in the **Before you begin** section:

***For existing users with an email address in the federated domain, their Managed Apple ID is automatically changed to match that email address.***

![](https://derflounder.wordpress.com/wp-content/uploads/2024/10/screenshot-2024-10-21-at-2.52.png?w=599&h=399 "Screenshot 2024-10-21 at 2.52.png")

What’s this mean? It means that the existing MAA may be set up with the following username and email:

* Username: **something@outside\_domain\_being\_federated.com**
* Email: **something@domain\_being\_federated.com**

However, once the initial federation process has happened the MAA username and email will now look like this:

* Username: **something@domain\_being\_federated.com**
* Email: **something@domain\_being\_federated.com**

Now the previously outside-of-federation-scope MAA ( **something@outside\_domain\_being\_federated.com** ) is in scope for being federated by having its MAA changed to **something@domain\_being\_federated.com.** In turn, this change means that authentication requests for the **something@domain\_being\_federated.com** MAA are being sent on to the company, school or institution’s IdP. That IdP may not actually have a user account for the **something@domain\_being\_federated.com** MAA or be able to authenticate it, which means you can’t log into that MAA.

How do you address this? My recommendation is that prior to federation, you identify all the MAAs you want to remain outside of scope and assign them an email address which is explicitly outside of the domain you’re planning to federate. For example, if your MAA is currently like this:

* Username: **something@outside\_domain\_being\_federated.com**
* Email: **something@domain\_being\_federated.com**

Change it to something like this:

* Username: **something@outside\_domain\_being\_federated.com**
* Email: **something@work\_email\_domain\_which\_is\_not\_the\_domain\_being\_federated.com**

As far as I know, this is a one-time change which is made by the initial ABM / ASM federation process. But I do not know that with 100% certainty, so please make sure to ask the folks at Apple about this issue if you’re planning an ABM / ASM federation process and have existing MAAs which may be affected by this.

### Share this:

* [Click to print (Opens in new window)
  Print](https://derflounder.wordpress.com/2024/10/21/managed-apple-accounts-which-were-out-of-scope-for-abm-or-asm-federation-may-be-changed-to-be-in-scope-by-the-federation-process/#print?share=print)
* Click to email a link to a friend (Opens in new window)
  Email
* More

* [Click to share on Facebook (Opens in new window)
  Facebook](https://derflounder.wordpress.com/2024/10/21/managed-apple-accounts-which-were-out-of-scope-for-abm-or-asm-federation-may-be-changed-to-be-in-scope-by-the-federation-process/?share=facebook)
* [Click to share on LinkedIn (Opens in new window)
  LinkedIn](https://derflounder.wordpress.com/2024/10/21/managed-apple-accounts-which-were-out-of-scope-for-abm-or-asm-federation-may-be-changed-to-be-in-scope-by-the-federation-process/?share=linkedin)
* [Click to share on Reddit (Opens in new window)
  Reddit](https://derflounder.wordpress.com/2024/10/21/managed-apple-accounts-which-were-out-of-scope-for-abm-or-asm-federation-may-be-changed-to-be-in-scope-by-the-federation-process/?share=reddit)
* [Click to share on X (Opens in new window)
  X](https://derflounder.wordpress.com/2024/10/21/managed-apple-accounts-which-were-out-of-scope-for-abm-or-asm-federation-may-be-changed-to-be-in-scope-by-the-federation-process/?share=twitter)
* [Click to share on Pinterest (Opens in new window)
  Pinterest](https://derflounder.wordpress.com/2024/10/21/managed-apple-accounts-which-were-out-of-scope-for-abm-or-asm-federation-may-be-changed-to-be-in-scope-by-the-federation-process/?share=pinterest)
* [Click to share on Tumblr (Opens in new window)
  Tumblr](https://derflounder.wordpress.com/2024/10/21/managed-apple-accounts-which-were-out-of-scope-for-abm-or-asm-federation-may-be-changed-to-be-in-scope-by-the-federation-process/?share=tumblr)
* [Click to share on Pocket (Opens in new window)
  Pocket](https://derflounder.wordpress.com/2024/10/21/managed-apple-accounts-which-were-out-of-scope-for-abm-or-asm-federation-may-be-changed-to-be-in-scope-...