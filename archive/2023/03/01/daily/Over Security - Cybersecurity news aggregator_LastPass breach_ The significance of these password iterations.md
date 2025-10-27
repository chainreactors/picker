---
title: LastPass breach: The significance of these password iterations
url: https://palant.info/2022/12/28/lastpass-breach-the-significance-of-these-password-iterations/
source: Over Security - Cybersecurity news aggregator
date: 2023-03-01
fetch_date: 2025-10-04T08:21:54.676179
---

# LastPass breach: The significance of these password iterations

[Almost Secure](/)

* [Home](/)
* [Articles](/articles/)
* [Categories](/categories/)
* [About](/about/)
* ##

  Read More Â»

[ ]

# LastPass breach: The significance of these password iterations

2022-12-28
 [Lastpass](/categories/lastpass/)/[Security](/categories/security/)/[Password-Managers](/categories/password-managers/)
 6 mins
 [29 comments](/2022/12/28/lastpass-breach-the-significance-of-these-password-iterations/#comments)

LastPass has been breached, data has been stolen. I already [pointed out](/2022/12/26/whats-in-a-pr-statement-lastpass-breach-explained/) that their official statement is misleading. I also explained that [decrypting passwords in the stolen data is possible](/2022/12/23/lastpass-has-been-breached-what-now/) which doesnât mean however that everybody is at risk now. For assessing whether you are at risk, a fairly hidden setting turned out critical: password iterations.

LastPass provides [an instruction to check this setting](https://support.lastpass.com/help/how-do-i-change-my-password-iterations-for-lastpass). One would expect it to be 100,100 (the LastPass default) for almost everyone. But plenty of people report having 5,000 configured there, some 500 and occasionally itâs even 1 (in words: one) iteration.

![Screenshot of LastPass preferences. The value in the Password Iterations field: 1](/2022/12/28/lastpass-breach-the-significance-of-these-password-iterations/iterations.png)

Letâs say this up front: this isnât the account holdersâ fault. It rather is a massive failure by LastPass. They have been warned, yet they failed to act. And even now they are failing to warn the users who they know are at risk.

#### Contents

* [What is this setting about?](#what-is-this-setting-about)
* [How did the low iteration numbers come about?](#how-did-the-low-iteration-numbers-come-about)
* [What could LastPass do about it now?](#what-could-lastpass-do-about-it-now)

## What is this setting about?

This setting is actually central to protecting your passwords if LastPass loses control of your data (like they did now). Your passwords are encrypted. In order to decrypt them, the perpetrators need to guess your master password. The more iterations you have configured, the slower this guessing will be. The [current OWASP recommendation](https://cheatsheetseries.owasp.org/cheatsheets/Password_Storage_Cheat_Sheet.html#pbkdf2) is 310,000 iterations. So the LastPass default is already factor three below the recommendation.

Whatâs the impact if you have an even lower iterations number configured? Letâs say you have a fairly strong master password, 50 bits of entropy. For example, it could be an eight character random password, with uppercase and lowercase letters, digits and even some special characters. Yes, such password is already rather hard to remember but you want your passwords to be secure.

Or maybe you went for a [diceware password](https://en.wikipedia.org/wiki/Diceware). You took a word list for four dices (1296 words) and you randomly selected five words for your master password.

Choosing a password with 50 bits entropy without it being randomized? No idea how one would do it. Humans are inherently bad at choosing strong passwords. Youâd need a rather long password to get 50 bits, and youâd need to avoid obvious patterns like dictionary words.

Either way, if this is your password and someone got your LastPass vault, guessing your master password on a single graphics card would take on average 200 years. Not unrealistic (someone could get more graphics cards) but usually not worth the effort. But thatâs the calculation for 100,100 iterations.

Letâs look at how time estimates and cost change depending on the number of iterations. Iâll be using the cost estimate by [Jeffrey Goldberg who works at 1Password](https://ioc.exchange/%40jpgoldberg/109589071740635270).

| Iterations | Guessing time on a single GPU | Cost |
| --- | --- | --- |
| 100,100 | Â 200 years | $1,500,000 |
| 5,000 | Â 10 years | $75,000 |
| 500 | Â 1 year | $7,500 |
| 1 | Â 17 hours | $15 |

And thatâs a rather strong password. According to [this older study](https://www.microsoft.com/en-us/research/wp-content/uploads/2006/11/www2007.pdf), the average password has merely 40 bits of entropy. So divide all numbers by 1,000 for that.

## How did the low iteration numbers come about?

The default for LastPass accounts wasnât always 100,100 iterations. Originally it was merely 1 iteration. At some point this was changed to 500 iterations, later to 5,000. And the final change adjusted this value to 100,100 iterations.

I donât know exactly when and how these changes happened. Except for the last one: it happened in February 2018 as a result of [my research](/2018/07/09/is-your-lastpass-data-really-safe-in-the-encrypted-online-vault/#cracking-the-encryption).

**Edit** (2022-12-30): I now know more, thanks to [@Sc00bz@infosec.exchange](https://infosec.exchange/%40sc00bz/109599415792124027). The switch to 500 iterations happened in June 2012, the one to 5,000 iterations in February 2013. To quote Sc00bz: âI shamed the CEO into increasing this. Â«I think it is irresponsible to tell your users the recommended iteration count is 500. When 12 years ago, PBKDF2 had a recommended minimum iteration count of 1000.Â»â

LastPass was notified through their bug bounty program on Bugcrowd. When they reported fixing the issue I asked them about existing accounts. That was on February 24th, 2018.

![Screenshot from Bugcrowd. bobc sent a message (5 years ago): Ok thank you. Our default is now 100k rounds and artificial limits on number of rounds have been removed. palant sent a message (5 years ago) Yes, the default changed it seems. But what about existing accounts?](/2022/12/28/lastpass-breach-the-significance-of-these-password-iterations/bugcrowd.png)

They didnât reply. So I prompted them again in an email on March 15th and got the reply that the migration should take until end of May.

I asked again about the state of the migration on May 23rd. This time the reply was that the migration is starting right now and is expected to complete by mid-June.

On June 25th I was once again contacted by LastPass, asking me to delay disclosure until they finish migrating existing accounts. I replied asking whether the migration actually started now and got the response: yes, it did last week.

[My disclosure of the LastPass issues](/2018/07/09/is-your-lastpass-data-really-safe-in-the-encrypted-online-vault/) was finally published on July 9th, 2018. After all the delays requested by LastPass, [their simultaneously published statement](https://blog.lastpass.com/2018/07/lastpass-bugcrowd-update/) said:

> we are in the process of automatically migrating all existing LastPassÂ users to the new default.

We can now safely assume that the migration wasnât actually underway even at this point. One user reported receiving an email about their account being upgraded to a higher password iterations count, and that was mid-2019.

Worse yet, for reasons that are beyond me, LastPass didnât complete this migration. My test account is still at 5,000 iterations, as are the accounts of many other users who checked their LastPass settings. LastPass would know how many users are affected, but they arenât telling that.

In fact, itâs painfully obvious that LastPass never bothered updating usersâ security settings. Not when they changed the default from 1 to 500 iterations. Not when they changed it from 500 to 5,000. Only my persistence made them consider it for their latest change. And they still failed implementing it consistently.

So we now have people report finding their accounts to be configured with 500 iterations. And for some itâs even merely one iteration. For example [here](https://social.treehouse.systems/%40particles/109566045071178513). And [here](https://news.ycombinator.com/item?id=34152779). And [here](https://snabelen.no/%40vegardlarsen/109575...