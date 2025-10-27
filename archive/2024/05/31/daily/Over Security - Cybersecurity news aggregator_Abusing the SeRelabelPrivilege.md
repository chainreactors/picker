---
title: Abusing the SeRelabelPrivilege
url: https://decoder.cloud/2024/05/30/abusing-the-serelabelprivilege/
source: Over Security - Cybersecurity news aggregator
date: 2024-05-31
fetch_date: 2025-10-06T16:51:30.399325
---

# Abusing the SeRelabelPrivilege

# [Decoder's Blog](https://decoder.cloud/ "Decoder's Blog")

Decoder's Blog

[Skip to content](#content "Skip to content")

* [Home](/)
* [Decoder’s Blog](https://decoder.cloud/)
* [Contact](https://decoder.cloud/contact/)

Search for:

Posted on [May 30, 2024May 30, 2024](https://decoder.cloud/2024/05/30/abusing-the-serelabelprivilege/) by [Decoder](https://decoder.cloud/author/decoderblogblog/)

# Abusing the SeRelabelPrivilege

In a recent assessment, it was found that a specific Group Poilcy granted via “User Right Assignments” the **SeRelabelPrivilege** to the built-in Users group and was applied on several computer accounts.

I never found this privilege before and was obviously curious to understand the potential implications and the possibility of any (mis)usage scenario.

Microsoft [documentation](https://learn.microsoft.com/en-us/previous-versions/windows/it-pro/windows-10/security/threat-protection/security-policy-settings/modify-an-object-label) is as usual not very clear and helpful, to summarize:

“*Anyone with the **Modify an object label** user right can change the integrity level of a file or process so that it becomes elevated or decreased to a point where it can be deleted by lower integrity processes.*“

Luckily, a [post](https://www.tiraniddo.dev/2021/06/the-much-misunderstood.html) from James Froshaw published in 2021 gave much more details and useful information on possible abuse 😉 . I highly recommend reading it before going on.

I decided to do some experiments to understand how “far” I could go.

I started by assigning to a standard user the *SeRelabelPrivilege* via group policy:

![](https://decoder.cloud/wp-content/uploads/2024/05/image-2.png?w=1024)

The privilege is only available in High Integrity Level (in the case of cmd.exe -> run as administrator):

![](https://decoder.cloud/wp-content/uploads/2024/05/image-3.png?w=1024)

But what does this privilege grant to you? Well, a lot of interesting permissions!

* It allows you to **take ownership** of a resource
* Furthermore, unlike the *SeTakeOwnsership* privilege, it allows you to own resources that have an **integrity level even higher than your own**
* Once you have taken the ownership, you can grant yourself **full control** over the resource (process, tokens,…)
* Quick & dirty: Same as abusing the *SeDebugPrivilege* 🙂

My goal was to take ownership of a SYSTEM process, grant myself full control, and then create a process under the NT AUTHORITY\SYSTEM account.

Perfect Local Privilege Escalation… pardon, just a “Safety Boundary” violation 😉

For this purpose, I created a simple POC:

![](https://decoder.cloud/wp-content/uploads/2024/05/image-4.png?w=1024)

First of all, I needed to get the current user SID and enable the specific privilege. After this, I took the ownership of the process:

![](https://decoder.cloud/wp-content/uploads/2024/05/image-5.png?w=1024)

I needed to open the process with WRITE\_OWNER access. In the *SetSecurityInfo* call, the “LABEL\_SECURITY\_INFORMATION” flag is mandatory, otherwise, I was not able to own a process with an Integrity Level higher than my High IL process.

Once I took the ownership, it was super-easy to grant full control:

![](https://decoder.cloud/wp-content/uploads/2024/05/image-6.png?w=1024)

In this case, I needed to open the process with WRITE\_DAC access, and after setting the explicit access to PROCESS\_ALL\_ACCESS, I gained full control of the process!

*Side note: this is just an example, the same results can be accomplished in different ways by using other API calls.*

Let’s see if it works… 7116 was the winlogon process, which ran under System Integrity and was owned by SYSTEM:

![](https://decoder.cloud/wp-content/uploads/2024/05/image-7.png?w=1024)

Ownership changed and full control was successfully granted:

![](https://decoder.cloud/wp-content/uploads/2024/05/image-8.png?w=1024)

The easiest way to abuse this was to perform a parent process injection. For this purpose, I used my old [psgetsystem](https://github.com/decoder-it/psgetsystem/blob/master/psgetsys.ps1) tool (remember to comment out *Process.EnterDebugMode()*)

![](https://decoder.cloud/wp-content/uploads/2024/05/image-9.png?w=1024)

Et voilà! Got SYSTEM access 🙂

Just for fun, I also took ownership of the token, granted full access to the token, and lowered the IL from System to Medium 😉

![](https://decoder.cloud/wp-content/uploads/2024/05/image-11.png?w=1024)

## Conclusion

From what I understood of this really strange privilege:

* It allows you to take ownership of a resource even if it’s IL > of yours.
* Once you take ownership you can grant yourself full access to the process and tokens.
* The result, from an abuse perspective, is then quite similar to the Debug Privilege
* Manipulating the mandatory label is just a consequence.
* I still don’t understand why MS implemented it

The source code of simple and stupid POC can be found [here](https://github.com/decoder-it/RelabelAbuse)

Thanks to James Forshaw for his useful hints and for helping me demystify this privilege

That’s all 🙂

### Share this:

* [Click to share on X (Opens in new window)
  X](https://decoder.cloud/2024/05/30/abusing-the-serelabelprivilege/?share=twitter)
* [Click to share on Facebook (Opens in new window)
  Facebook](https://decoder.cloud/2024/05/30/abusing-the-serelabelprivilege/?share=facebook)

Like Loading...

# Post navigation

[Previous Article Hello: I’m your Domain Admin and I want to authenticate against you](https://decoder.cloud/2024/04/24/hello-im-your-domain-admin-and-i-want-to-authenticate-against-you/)

[Next Article The “Fake” Potato](https://decoder.cloud/2024/08/02/the-fake-potato/)

### Leave a comment [Cancel reply](/2024/05/30/abusing-the-serelabelprivilege/#respond)

Δ

## Search

Search for:

[Blog at WordPress.com.](https://wordpress.com/?ref=footer_blog)

* [Facebook](http://www.facebook.com)
* [LinkedIn](http://www.linkedin.com)
* [Twitter](http://www.twitter.com)
* [Instagram](http://www.instagram.com)

Privacy & Cookies: This site uses cookies. By continuing to use this website, you agree to their use.
To find out more, including how to control cookies, see here:
[Cookie Policy](https://automattic.com/cookies/)

* [Comment](https://decoder.cloud/2024/05/30/abusing-the-serelabelprivilege/#respond)
* Reblog
* Subscribe
  Subscribed

  + [![](https://s2.wp.com/i/logo/wpcom-gray-white.png?m=1479929237i) Decoder's Blog](https://decoder.cloud)

  Join 43 other subscribers

  Sign me up

  + Already have a WordPress.com account? [Log in now.](https://wordpress.com/log-in?redirect_to=https%3A%2F%2Fr-login.wordpress.com%2Fremote-login.php%3Faction%3Dlink%26back%3Dhttps%253A%252F%252Fdecoder.cloud%252F2024%252F05%252F30%252Fabusing-the-serelabelprivilege%252F)
* + [![](https://s2.wp.com/i/logo/wpcom-gray-white.png?m=1479929237i) Decoder's Blog](https://decoder.cloud)
  + Subscribe
    Subscribed
  + [Sign up](https://wordpress.com/start/)
  + [Log in](https://wordpress.com/log-in?redirect_to=https%3A%2F%2Fr-login.wordpress.com%2Fremote-login.php%3Faction%3Dlink%26back%3Dhttps%253A%252F%252Fdecoder.cloud%252F2024%252F05%252F30%252Fabusing-the-serelabelprivilege%252F)
  + [Copy shortlink](https://wp.me/p8ggv8-1hh)
  + [Report this content](https://wordpress.com/abuse/?report_url=https://decoder.cloud/2024/05/30/abusing-the-serelabelprivilege/)
  + [View post in Reader](https://wordpress.com/reader/blogs/122087370/posts/4915)
  + [Manage subscriptions](https://subscribe.wordpress.com/)
  + Collapse this bar

##

##

Loading Comments...

Write a Comment...

Email (Required)

Name (Required)

Website

###

%d

![](https://pixel.wp.com/b.gif?v=noscript)