---
title: Apple Is Finally Encrypting iCloud Backups
url: https://www.schneier.com/blog/archives/2022/12/apple-is-finally-encrypting-icloud-backups.html
source: Schneier on Security
date: 2022-12-13
fetch_date: 2025-10-04T01:20:22.345575
---

# Apple Is Finally Encrypting iCloud Backups

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

## Apple Is Finally Encrypting iCloud Backups

After way too many years, Apple is *finally* [encrypting iCloud backups](https://www.theverge.com/2022/12/7/23498580/apple-end-to-end-encryption-icloud-backups-advanced-data-protection):

> Based on a screenshot from Apple, these categories are covered when you flip on Advanced Data Protection: device backups, messages backups, iCloud Drive, Notes, Photos, Reminders, Safari bookmarks, Siri Shortcuts, Voice Memos, and Wallet Passes. Apple says the only “major” categories not covered by Advanced Data Protection are iCloud Mail, Contacts, and Calendar because “of the need to interoperate with the global email, contacts, and calendar systems,” according to its press release.
>
> You can see the full list of data categories and what is protected under standard data protection, which is the default for your account, and Advanced Data Protection [on Apple’s website](https://support.apple.com/en-us/HT202303).
>
> With standard data protection, Apple holds the encryption keys for things that aren’t end-to-end encrypted, which means the company can help you recover that data if needed. Data that’s end-to-end encrypted can *only* be encrypted on “your trusted devices where you’re signed in with your Apple ID,” according to Apple, meaning that the company—or law enforcement or hackers—cannot access your data from Apple’s databases.

Note that this system doesn’t have the backdoor that was in Apple’s previous proposal, the one put there under the guise of detecting CSAM.

Apple [says](https://www.wsj.com/articles/apple-plans-new-encryption-system-to-ward-off-hackers-and-protect-icloud-data-11670435635) that it will roll out worldwide by the end of next year. I wonder how China will react to this.

Tags: [Apple](https://www.schneier.com/tag/apple/), [backups](https://www.schneier.com/tag/backups/), [cloud computing](https://www.schneier.com/tag/cloud-computing/), [encryption](https://www.schneier.com/tag/encryption/)

[Posted on December 12, 2022 at 7:00 AM](https://www.schneier.com/blog/archives/2022/12/apple-is-finally-encrypting-icloud-backups.html) •
[10 Comments](https://www.schneier.com/blog/archives/2022/12/apple-is-finally-encrypting-icloud-backups.html#comments)

### Comments

Q •
[December 12, 2022 9:54 AM](https://www.schneier.com/blog/archives/2022/12/apple-is-finally-encrypting-icloud-backups.html/#comment-413774)

The notion of having Apple store and be the gatekeeper for your data is where the real problem is.

The data is encrypted now, but it doesn’t solve the problem of being held hostage by Apple if you ever decide to ditch your iPhone.

Find a way to copy it off the Apple systems and keep all your data under your own control. Then it won’t matter if your iPhone shits itself, or Apple demands more money to continue to provide access, or any of many ways it can all go tits up and you lose access to everything.

TimH •
[December 12, 2022 9:54 AM](https://www.schneier.com/blog/archives/2022/12/apple-is-finally-encrypting-icloud-backups.html/#comment-413775)

It doesn’t seem that great to me. Firstly, Apple holds the keys for iCloud Mail, Contacts, Calendars which means that a Prism (Apple is a member – thanks, Snowden) sweep of idata will find people connections with that, and use that for a warrant.

The statement “The security of your data in iCloud starts with the security of your Apple ID. All new Apple IDs require two-factor authentication to help protect you from **fraudulent** attempts to gain access to your account.” has a weasel word. Access by goverments won’t be fraudulent, will it?

Lastly, the key for “Trusted devices” is in the device. But how easy is it to obtain by the 3rd party who has seized the device?

TimH •
[December 12, 2022 10:05 AM](https://www.schneier.com/blog/archives/2022/12/apple-is-finally-encrypting-icloud-backups.html/#comment-413777)

The real security advice here is to disable phone backups to cloud, i or otherwise.

Gordon Shumway •
[December 12, 2022 10:50 AM](https://www.schneier.com/blog/archives/2022/12/apple-is-finally-encrypting-icloud-backups.html/#comment-413778)

Thanks, Bruce.

You’ve provided the exact context this needs… ‘finally’ (in italics).

Sadly something the sycophantic tech press seems incapable of doing. Apple’s cloud services never should have been launched without the option of zero-knowledge encryption. But, we live in a commercial world of features over function, as you’ve said many times.

Also, notice the services which are still not encrypted; contacts, icloud mail and calendar. Because, of course those aren’t important to keep private, right? Ugh.

I’m sure Apple doesn’t have the resources to implement those things in a private manner. Tim Cook needs his stock options after all.

Clive Robinson •
[December 12, 2022 11:31 AM](https://www.schneier.com/blog/archives/2022/12/apple-is-finally-encrypting-icloud-backups.html/#comment-413780)

@ Bruce, ALL,

> “Note that this system doesn’t have the backdoor that was in Apple’s previous proposal, the one put there under the guise of detecting CSAM.”

If it’s not CSAM as an excuse it will be something else. Do people remember the nonsense excuse that the FBI-DoJ started their “We’ll smash Apple and every on will follow” court case? That turned into such a disaster for the FBI-DoJ psychos they had to pull the rip-cord and bail before an adverse decision was handed down by the Magistrate.

The FBI-DoJ nore many other “Might is Right” socio or psychopaths are not going to give up. If they can not squeeze what they want out of the Corps, or Courts, then they will blackmail the legislators, or worse.

But the real issue as I keep pointing out is not using encryption as such but where and how it is used.

There is no phone available to consumers and even proffessional organisations that is “Secure by Design”.

The reason as I keep saying is

“The lack of security through having the security end points not just in the wrong place but easily bypassable”.

This lack of hard segregation makes any on-board encryption circumventable and/or the encryption keys accessable/vulnerable from the “Over The Air”(OTA) interface.

The fact nobody including Apple want to address this issue, kind of makes this change by Apple both insufficient and effectively just PR.

Yes I know that sounds harsh, but there will be successful attacks on the iPhone probably within a year circumventing it. Such is the nature of the design failing.

Anon •
[December 12, 2022 1:21 PM](https://www.schneier.com/blog/archives/2022/12/apple-is-finally-encrypting-icloud-backups.html/#comment-413782)

I think it’s far too early to declare victory on this front.

They tell in their very own [documentation](https://support.apple.com/en-us/HT202303#Encryption%20of%20certain%20metadata%20and%20usage%20information) that they’re using convergent encryption for deduplication purposes (although ...