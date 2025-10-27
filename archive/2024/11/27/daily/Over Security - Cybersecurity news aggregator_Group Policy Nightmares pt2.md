---
title: Group Policy Nightmares pt2
url: https://decoder.cloud/2024/11/26/group-policy-nightmares-pt2/
source: Over Security - Cybersecurity news aggregator
date: 2024-11-27
fetch_date: 2025-10-06T19:20:50.980154
---

# Group Policy Nightmares pt2

# [Decoder's Blog](https://decoder.cloud/ "Decoder's Blog")

Decoder's Blog

[Skip to content](#content "Skip to content")

* [Home](/)
* [Decoder’s Blog](https://decoder.cloud/)
* [Contact](https://decoder.cloud/contact/)

Search for:

Posted on [November 26, 2024November 26, 2024](https://decoder.cloud/2024/11/26/group-policy-nightmares-pt2/) by [Decoder](https://decoder.cloud/author/decoderblogblog/)

# Group Policy Security Nightmares pt2

In this second super short post, I want to explore an unusual Group Policy Object (GPO) configuration I recently encountered.

The GPO in question used a **File Preference** policy to copy a custom `HOSTS` file from a remote share to the local machine’s `HOSTS` file:

![](https://decoder.cloud/wp-content/uploads/2024/11/image-10.png?w=586)

This caught my attention because it introduced an unexpected element to the hostname resolution process.

#### Understanding the Hostname Resolution Order

As many of you know, hostname resolution in Windows follows a predefined order. Typically, it prioritizes the `HOSTS` file over DNS. This means that any entry in the `HOSTS` file will take precedence over DNS lookups, effectively overriding network-level name resolution.

#### The Incredible Twist

So far, so good, this setup might make sense (??) in certain environments for hostname standardization. However, the **incredible discovery** was that the source `HOSTS` file on the remote share **granted “Users” full control!**

![](https://decoder.cloud/wp-content/uploads/2024/11/image-11.png?w=535)

This was a significant red flag. It meant any authenticated user on the domain could potentially modify the file, introducing malicious entries that would propagate to all machines affected by the GPO.

#### Why Is This a Problem?

With this level of access, an attacker could:

* **Redirect Traffic:** Point legitimate hostnames (e.g., `server.company.local`) to malicious IP addresses.
* **Create MitM Opportunities:** Use spoofed entries to route traffic through an attacker-controlled machine.
* **Disrupt Services:** Break connections to critical resources by pointing them to non-existent or incorrect IP addresses.

This configuration essentially opened the door for widespread abuse, leveraging the `HOSTS` file’s precedence over DNS.

#### Thinking Bigger: What Other Configurations Enable Hostname Spoofing?

This discovery led me to consider other scenarios where hostname spoofing might be possible. Here are a few additional configurations:

1. **DnsAdmins Group Privileges:** Members of the privileged `DnsAdmins` group can modify DNS records, giving them the ability to redirect traffic at will.
2. **Zones with Insecure Updates:** DNS zones configured with insecure updates allow even **anonymous users** to perform DNS record changes. Shockingly, this is not an uncommon misconfiguration:

![](https://decoder.cloud/wp-content/uploads/2024/11/image-12.png?w=597)

In this example below, we can see that an anonymous user with network level access can modify DNS records:

![](https://decoder.cloud/wp-content/uploads/2024/11/image-14.png?w=1024)

With these scenarios in mind, I began exploring how these configurations could be abused, particularly in Man-in-the-Middle (MitM) attacks. This experimentation ultimately led me to develop and release my own tool, **KrbRelayEx**, which demonstrates how Kerberos relaying and forwarding can exploit these vulnerabilities and lead to a complete Domain takeover!

![](https://decoder.cloud/wp-content/uploads/2024/11/krbrelayex.png?w=1024)

If you’re interested in diving deeper into this topic, feel free to check out my GitHub repository: <https://github.com/decoder-it/KrbRelayEx>

That’s all 😉

### Share this:

* [Click to share on X (Opens in new window)
  X](https://decoder.cloud/2024/11/26/group-policy-nightmares-pt2/?share=twitter)
* [Click to share on Facebook (Opens in new window)
  Facebook](https://decoder.cloud/2024/11/26/group-policy-nightmares-pt2/?share=facebook)

Like Loading...

# Post navigation

[Previous Article Group Policy Security Nightmares pt 1](https://decoder.cloud/2024/11/08/group-policy-security-nightmares-pt-1/)

[Next Article The (Almost) Forgotten Vulnerable Driver](https://decoder.cloud/2025/01/09/the-almost-forgotten-vulnerable-driver/)

### Leave a comment [Cancel reply](/2024/11/26/group-policy-nightmares-pt2/#respond)

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

* [Comment](https://decoder.cloud/2024/11/26/group-policy-nightmares-pt2/#respond)
* Reblog
* Subscribe
  Subscribed

  + [![](https://s2.wp.com/i/logo/wpcom-gray-white.png?m=1479929237i) Decoder's Blog](https://decoder.cloud)

  Join 43 other subscribers

  Sign me up

  + Already have a WordPress.com account? [Log in now.](https://wordpress.com/log-in?redirect_to=https%3A%2F%2Fr-login.wordpress.com%2Fremote-login.php%3Faction%3Dlink%26back%3Dhttps%253A%252F%252Fdecoder.cloud%252F2024%252F11%252F26%252Fgroup-policy-nightmares-pt2%252F)
* + [![](https://s2.wp.com/i/logo/wpcom-gray-white.png?m=1479929237i) Decoder's Blog](https://decoder.cloud)
  + Subscribe
    Subscribed
  + [Sign up](https://wordpress.com/start/)
  + [Log in](https://wordpress.com/log-in?redirect_to=https%3A%2F%2Fr-login.wordpress.com%2Fremote-login.php%3Faction%3Dlink%26back%3Dhttps%253A%252F%252Fdecoder.cloud%252F2024%252F11%252F26%252Fgroup-policy-nightmares-pt2%252F)
  + [Copy shortlink](https://wp.me/p8ggv8-78O)
  + [Report this content](https://wordpress.com/abuse/?report_url=https://decoder.cloud/2024/11/26/group-policy-nightmares-pt2/)
  + [View post in Reader](https://wordpress.com/reader/blogs/122087370/posts/27454)
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