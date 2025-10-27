---
title: My Philosophy and Recommendations Around the LastPass Breaches
url: https://danielmiessler.com/blog/my-philosophy-and-recommendations-around-the-lastpass-breaches/
source: Daniel Miessler
date: 2022-12-25
fetch_date: 2025-10-04T02:30:01.649924
---

# My Philosophy and Recommendations Around the LastPass Breaches

[Daniel Miessler](https://danielmiessler.com)

Main Navigation [home](/)[blog](/blog/)[telos](/telos/)[ideas](/ideas/)[projects](/projects/)[predictions](/predictions/)[speaking](/speaking/)[about](/about/)

# My Philosophy and Recommendations Around the LastPass Breaches

December 24, 2022

[#apple](/archives/?tag=apple) [#business](/archives/?tag=business) [#cybersecurity](/archives/?tag=cybersecurity) [#future](/archives/?tag=future) [#innovation](/archives/?tag=innovation) [#technology](/archives/?tag=technology)

![password vault](/images/a0693a92-6cb8-4824-babb-bde524a4c732-Screenshot_2022-12-24_at_09.54.57-removebg-preview.png)

If you follow Information Security at all you are surely aware of [the LastPass breach situation](https://blog.lastpass.com/2022/12/notice-of-recent-security-incident/?utm_source=danielmiessler.com&utm_medium=newsletter&utm_campaign=my-philosophy-and-recommendations-around-the-lastpass-breaches) >. It started back in August of 2022 as a fairly common breach notification on a blog, but it, unfortunately, turned into more of a blog series.

The initial blog was on August 25th, saying there was a breach, but it wasn’t so bad because they had no access to customer data or password vaults:

Two weeks ago, we detected some unusual activity within portions of the LastPass development environment. After initiating an immediate investigation, we have seen no evidence that this incident involved any access to customer data or encrypted password vaults.

Then on September 15th they announced what they thought was the conclusion to the investigation, celebrating the attackers not getting much:

Although the threat actor was able to access the Development environment, our system design and controls prevented the threat actor from accessing any customer data or encrypted password vaults.

Then on November 30th they then updated the same blog saying they actually did get some customer data, but no password vaults:

We have determined that an unauthorized party, using information obtained in the August 2022 incident, was able to gain access to certain elements of our customers’ information…(snip)…We are working diligently to understand the scope of the incident and identify what specific information has been accessed.

And finally, in the latest update, they reveal that they did actually get the password vaults:

The threat actor was also able to copy a backup of customer vault data from the encrypted storage container which is stored in a proprietary binary format that contains both unencrypted data, such as website URLs, as well as fully-encrypted sensitive fields such as website usernames and passwords, secure notes, and form-filled data. These encrypted fields remain secured with 256-bit AES encryption and can only be decrypted with a unique encryption key derived from each user’s master password using our Zero Knowledge architecture.

So basically:

1. Minor incident, but no customer data or vaults were lost
2. Actually, some data was lost
3. Actually, both data and vaults were lost

It’s especially troubling because the attackers got the sites that are in each vault, meaning they can go on HaveIBeenPwned and see if there are any leaked passwords there and then try those passwords to guess the master password.

## My thoughts on the situation

Anyway, it’s pretty bad, and people have been asking me my thoughts on the situation. And specifically, asking me whether I used LastPass or any other password manager.

The answer is no. I don’t use third-party password managers for precisely this reason, and here’s my logic.

1. Nobody is better at protecting passwords than the three primary providers: Google, Apple, and Microsoft. I would trust any of those three more than any third-party company to protect my passwords. Why?
2. They have the most to lose from their security being bad, so they tend to invest heavily in it
3. They have full researcher and threat intel teams to support their product security teams
4. If their auth mechanisms were to get compromised it would likely be very loud, meaning it would be hard to keep a secret for long
5. Any damage that was done would be handled fairly well, and the response would be quick
6. I believe [auth/password handling belongs with your OS](https://danielmiessler.com/blog/good-app-features-become-os-features/?utm_source=danielmiessler.com&utm_medium=newsletter&utm_campaign=my-philosophy-and-recommendations-around-the-lastpass-breaches&last_resource_guid=Post%3A0f7b2e49-23cc-4455-bf66-5e8eecac6b04) >, not with third-party apps. That’s the natural place for core functionality, which [I wrote about in 2017](https://danielmiessler.com/blog/good-app-features-become-os-features/?utm_source=danielmiessler.com&utm_medium=newsletter&utm_campaign=my-philosophy-and-recommendations-around-the-lastpass-breaches&last_resource_guid=Post%3A0f7b2e49-23cc-4455-bf66-5e8eecac6b04) >.

This is why I will always use integrated (OS-level) password managers over third-party options. Again:

1. They’re better funded
2. They have extensive security teams
3. They basically have unlimited funds to spend on doing auth/passwords right
4. It would be hard to keep a compromise a secret
5. The response from the vendor is likely to be solid
6. The natural home for your auth/OS security is your OS, not third-party apps

This doesn’t mean 1Password or LastPass are bad. They seem to be solid products, the present troubles being ignored. The points above would still apply for me if none of these companies had ever had an incident.

One final point is that I prefer to trust the least number of actors. We already trust our OS so much, and I feel like giving passwords to a second (much less a third) party ends up doubling my attack surface. I’d rather have that single point of failure with a high-security and loud-if-compromised entity than spread it around.

## Ok, but what do I do in the meantime?

Unfortunately, if you are a cross-platform user—which many people are—it’s not easy to get away from something like LastPass, 1Password, Keeper, or whatever. The whole reason they became popular is because people had a need to share passwords across various systems, and that’s what they do.

Apple is currently the only end-to-end-ecosystem when it comes to this. If you’re all-in on Apple you get a password manager (Keychain), browser integration (Safari), a decent cloud offering (iCloud), and they all work seamlessly on mobile as well via iOS.

But the answer can’t be to "just switch to Apple". Many people need to use Windows at work, or need to use Android and/or some other tech for good reason. So I’d say if you are able to get fully into the Apple ecosystem, it’s a very clean option, but it can’t be the long-term answer to this challenge.

The long-term answer to this is for other companies to offer what Apple is offering, i.e., a full-stack solution. Unfortunately, Apple is currently the only place where you can get 1) a desktop OS, 2) a browser, 3) a mobile OS, and 4) a password solution all in one company. That shouldn’t be the case. There should be more companies that have all four.

I’d absolutely trust a full-stack solution from Google or Microsoft. Why? For the reasons I gave above. They’re massive companies with massive security teams, and they’re damn good at securing customer data. There’s always a risk when you put your security eggs in one company nest, but my professional opinion is that—for most people—the risk there is far lower than having it spread across multiple, less-secure companies.

In short, **all companies can be hacked, including companies like LastPass, and it’s much better to have your most sensitive assets with a large company that has nearly infinite security resources to detect and respond when it inevitably happens**.

I personally believe an integrated approach is best for most people, but not all threat models are the same and there could be some situations where it’s better to divide things up....