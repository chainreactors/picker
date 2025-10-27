---
title: The UK Bans Default Passwords
url: https://www.schneier.com/blog/archives/2024/05/the-uk-bans-default-passwords.html
source: Schneier on Security
date: 2024-05-03
fetch_date: 2025-10-06T17:16:51.519651
---

# The UK Bans Default Passwords

# [Schneier on Security](https://www.schneier.com/)

Menu

* [Blog](https://www.schneier.com)
* [Newsletter](https://www.schneier.com/crypto-gram/)
* [Books](https://www.schneier.com/books/)
* [Essays](https://www.schneier.com/essays/)
* [News](https://www.schneier.com/news/)
* [Talks](https://www.schneier.com/talks/)
* [Academic](https://www.schneier.com/academic/)
* [About Me](https://www.schneier.com/blog/about/)

### Search

*Powered by [DuckDuckGo](https://duckduckgo.com/)*

Blog

Essays

Whole site

### Subscribe

[![Atom](https://www.schneier.com/wp-content/uploads/2019/10/rss-32px.png)](https://www.schneier.com/feed/atom/)[![Facebook](https://www.schneier.com/wp-content/uploads/2019/10/facebook-32px.png)](https://www.facebook.com/bruce.schneier)[![Twitter](https://www.schneier.com/wp-content/uploads/2019/10/twitter-32px.png)](https://twitter.com/schneierblog)[![Email](https://www.schneier.com/wp-content/uploads/2019/10/email-32px.png)](https://www.schneier.com/crypto-gram)

[Home](https://www.schneier.com)[Blog](https://www.schneier.com/blog/archives/)

## The UK Bans Default Passwords

The UK is the first country to [ban default passwords](https://therecord.media/united-kingdom-bans-defalt-passwords-iot-devices) on IoT devices.

> On Monday, the United Kingdom became the first country in the world to ban default guessable usernames and passwords from these IoT devices. Unique passwords installed by default are still permitted.
>
> The [Product Security and Telecommunications Infrastructure Act 2022](https://www.legislation.gov.uk/ukpga/2022/46/contents/enacted) (PSTI) introduces new minimum-security standards for manufacturers, and demands that these companies are open with consumers about how long their products will receive security updates for.

The UK may be the first country, but as far as I know, California is the first jurisdiction. It [banned default passwords](https://techcrunch.com/2018/10/05/california-passes-law-that-bans-default-passwords-in-connected-devices/) in 2018, the law taking effect in 2020.

This sort of thing benefits all of us everywhere. IoT manufacturers aren’t making two devices, one for California and one for the rest of the US. And they’re not going to make one for the UK and another for the rest of Europe, either. They’ll remove the default passwords and sell those devices everywhere.

Another [news article](https://arstechnica.com/gadgets/2024/04/connected-devices-with-awful-default-passwords-now-illegal-in-uk/).

EDITED TO ADD (5/14): To clarify, the regulations say that passwords must be either chosen by the user, or else unique to the device. If unique preset passwords are used, they can’t be produced by an algorithm that makes them easily guessable. Here is the [actual language](https://www.legislation.gov.uk/uksi/2023/1007/schedule/1/paragraph/1/made) of the regulation.

Tags: [botnets](https://www.schneier.com/tag/botnets/), [Internet of Things](https://www.schneier.com/tag/internet-of-things/), [passwords](https://www.schneier.com/tag/passwords/), [UK](https://www.schneier.com/tag/uk/)

[Posted on May 2, 2024 at 7:05 AM](https://www.schneier.com/blog/archives/2024/05/the-uk-bans-default-passwords.html) •
[17 Comments](https://www.schneier.com/blog/archives/2024/05/the-uk-bans-default-passwords.html#comments)

### Comments

Peter •
[May 2, 2024 7:31 AM](https://www.schneier.com/blog/archives/2024/05/the-uk-bans-default-passwords.html/#comment-436153)

Bit click baity, it’s only on IOT devices, i.e..who cares. The real damage is vendor backdoor default passwords, not user facing ones.

Jos •
[May 2, 2024 8:12 AM](https://www.schneier.com/blog/archives/2024/05/the-uk-bans-default-passwords.html/#comment-436156)

@Peter

Gilbert •
[May 2, 2024 10:50 AM](https://www.schneier.com/blog/archives/2024/05/the-uk-bans-default-passwords.html/#comment-436158)

I am afraid this might not work. A lot of politicians think you can use laws to fix problems. But criminals do not obey law. Chinese companies that put hardcoded root passwords into products they sale.. They don’t even tell customers that those passwords do exist. And the UK government is not going to unpack, disassemble and study each appliance firmware to check that, because it takes time, money and needs to be done on each update.

Big sellers of hardware might follow the law because they have a huge market and don’t want their products to be sale-forbidden in UK. But IoT appliances are numerous, companies come and go, and they don’t really care. Most of them even put “EC” marks on their products and they don’t even follow european’s certifications.

What the UK is really doing is asking people that put hardcoded, default passwords into their products to stop doing it ? They already know it’s not a good idea to hardcode those things. Just look at Cisco : how many times did they got burned with security issues because of those hardcoded “root level” passwords in their products ? Again, and again and they keep hardcoding those : <https://www.schneier.com/blog/archives/2023/10/cisco-cant-stop-using-hard-coded-passwords.html>

Those that do that in covert will surely not obey nor follow those laws.

This is one serious issue with politicians : they think complex problems have simple solutions. And they believe that making a law will fix the problem.

It won’t.

Hans •
[May 2, 2024 11:03 AM](https://www.schneier.com/blog/archives/2024/05/the-uk-bans-default-passwords.html/#comment-436159)

@Gilbert
And the UK government is not going to unpack, disassemble and study each appliance firmware to check that, because it takes time, money and needs to be done on each update.

That is not the job of the government. That is the executive branch and even they can delegate to private control organizations. The Law makers have to create the basis for the executive to work on.

And they believe that making a law will fix the problem.

Not arguing wit the “simple solutins” complaint. But those laws give a basis for the executive or judicative to work on. Cisco might forget passwords if there is no real risc. But they will not risk getting banned from the british market. Even a thread of a large fine may be enough for a money oriented business. Without laws at such, that threat does not exist.

Who? •
[May 2, 2024 11:09 AM](https://www.schneier.com/blog/archives/2024/05/the-uk-bans-default-passwords.html/#comment-436160)

A nightmare for Fortinet, even if not exactly an IoT manufacturer. They are even worse than Cisco in this area.

noname •
[May 2, 2024 11:16 AM](https://www.schneier.com/blog/archives/2024/05/the-uk-bans-default-passwords.html/#comment-436162)

Word is if you come across a default password to first tell the manufacturer.

Also the Office for Product Safety Standards (OPSS).

Hope, where applicable, users feel empowered to make passwords random.

*(2) Passwords must be—
(a)unique per product; or
(b)defined by the user of the product.*

<https://www.centerforcybersecuritypolicy.org/insights-and-research/the-uk-psti-act-comes-into-effect>

lola •
[May 2, 2024 11:27 AM](https://www.schneier.com/blog/archives/2024/05/the-uk-bans-default-passwords.html/#comment-436163)

> Bit click baity, it’s only on IOT devices

…and also not a ban on default passwords, but only “guessable default passwords” (though I can’t find the details in the linked law). Similarly, the California law says a device is okay if “(1) The preprogrammed password is unique to each device manufactured. (2) The device contains a security feature that requires a user to generate a new means of authentication before access is granted to the device for the first time”—contrary to the Techcrunch summary, there’s no apparent requirement to “change the unique password to something new”; it looks to me like the default password could remain, whether active or temporarily disabled.

So, it’s likely that shipping a product with a per-device default password printed on it, as many router manufacturers do, r...