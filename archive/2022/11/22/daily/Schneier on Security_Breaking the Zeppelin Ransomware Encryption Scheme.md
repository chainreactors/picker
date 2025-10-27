---
title: Breaking the Zeppelin Ransomware Encryption Scheme
url: https://www.schneier.com/blog/archives/2022/11/breaking-the-zeppelin-ransomware-encryption-scheme.html
source: Schneier on Security
date: 2022-11-22
fetch_date: 2025-10-03T23:25:29.405141
---

# Breaking the Zeppelin Ransomware Encryption Scheme

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

## Breaking the Zeppelin Ransomware Encryption Scheme

Brian Krebs [writes](https://krebsonsecurity.com/2022/11/researchers-quietly-cracked-zeppelin-ransomware-keys/) about how the Zeppelin ransomware encryption scheme was broken:

> The researchers said their break came when they understood that while Zeppelin used three different types of encryption keys to encrypt files, they could undo the whole scheme by factoring or computing just one of them: An ephemeral RSA-512 public key that is randomly generated on each machine it infects.
>
> “If we can recover the RSA-512 Public Key from the registry, we can crack it and get the 256-bit AES Key that encrypts the files!” they wrote. “The challenge was that they delete the [public key] once the files are fully encrypted. Memory analysis gave us about a 5-minute window after files were encrypted to retrieve this public key.”
>
> Unit 221B ultimately built a “Live CD” version of Linux that victims could run on infected systems to extract that RSA-512 key. From there, they would load the keys into a cluster of 800 CPUs donated by hosting giant Digital Ocean that would then start cracking them. The company also used that same donated infrastructure to help victims decrypt their data using the recovered keys.

A company offered recovery services based on this break, but was reluctant to advertise because it didn’t want Zeppelin’s creators to fix their encryption flaw.

Technical [details](https://blog.unit221b.com/dont-read-this-blog/0xdead-zeppelin).

EDITED TO ADD (12/12): When BitDefender publicly advertised a decryption tool for a strain of DarkSide ransomware, DarkSide [immediately updated](https://www.technologyreview.com/2021/05/24/1025195/colonial-pipeline-ransomware-bitdefender/amp/) its ransomware to render the tool obsolete. It’s hard to come up with a solution to this problem.

Tags: [cryptanalysis](https://www.schneier.com/tag/cryptanalysis/), [cybersecurity](https://www.schneier.com/tag/cybersecurity/), [encryption](https://www.schneier.com/tag/encryption/), [ransomware](https://www.schneier.com/tag/ransomware/)

[Posted on November 21, 2022 at 7:08 AM](https://www.schneier.com/blog/archives/2022/11/breaking-the-zeppelin-ransomware-encryption-scheme.html) •
[10 Comments](https://www.schneier.com/blog/archives/2022/11/breaking-the-zeppelin-ransomware-encryption-scheme.html#comments)

### Comments

Clive Robinson •
[November 21, 2022 10:41 AM](https://www.schneier.com/blog/archives/2022/11/breaking-the-zeppelin-ransomware-encryption-scheme.html/#comment-412791)

@ Bruce, ALL,

This use of PubKey, was originally tslked about by Moti Yung a couple of decades back.

Back then factoring a 512bit key was seen as close to impossible.

These days not at all…

So it’s important to mention that 1024bit RSA that is still in usage can be factored. So 1.5k bit would probably be “easy meat” in a decade.

So going for 2k bits would be the absolute minimum for new “one time use” RSA keys these days.

Winter •
[November 21, 2022 11:50 AM](https://www.schneier.com/blog/archives/2022/11/breaking-the-zeppelin-ransomware-encryption-scheme.html/#comment-412793)

There is a lots of annoying RC4 encryption with a hard coded key and shuffling offsets and stripping.

In Short, a lot of Security by Obscurity which was just annoying.

The only thing that really was secure was the RSA-512 encryption. They even tried to remove the public key. Had they succeeded in wiping the public key, they would have been successful. But deleting bits is *Hard*™.

A few years back, RSA-512 would have been unbreakable, now it isn’t.

Lesson to learn: Secure symmetric key lengths grow with a few bits a year. RSA key lengths must grow non-linear (exponentially) over time.

NIST wants us to use RSA 2048 as a minimum now (cannot find the original NIST report).

‘https://www.jscape.com/blog/should-i-start-using-4096-bit-rsa-keys

According to NIST, a 2048 bit RSA key is as strong as a 112 bit symmetric key, which does not really instill a lot of confidence for the coming years. To get to an RSA key as strong as a 128 bit symmetric key, you need an RSA key of >= 3072 bits.[1]

[1] RSA key lengths for 256 bit strength: Don’t ask, use something else.

Clive Robinson •
[November 21, 2022 1:16 PM](https://www.schneier.com/blog/archives/2022/11/breaking-the-zeppelin-ransomware-encryption-scheme.html/#comment-412796)

@ ALL,

Re : Do backups righ…

As you read the Krebs artical you very quickly come to,

> *“… because of the way his predecessor architected things, the company’s data backups also were encrypted by Zeppelin.”*

Backs being encrypted also gets mentioned a few times more in the article. As some so rudely say,

“Take a hint”

The way you are doing your backups is probably wrong…

I’ve mentioned the vulnerability of backups to ransomware of various types on this blog many times over the years. First as an “insider” revenge and later outsiders.

The simple fact is backups are as much as possible “automated” for ease of use/operation. Remember what makes it easy for you frequently works in the attackers favour as well…

The first thing to take onboard is,

1, Issolation is essential.

If the attackers can not reach the systems they can not attack them. This however only means they are forced to change tactics from attacking existing backups to attacking data going to new backups.

You can limit this by,

2, Allways check the backups on an issolated independent system.

The question then is how do you prevent or limit the attackers ability to attack the data going to new backups.

This is very system specific so not amenable to “generalised advice” other than reiterating point 1,

3, Issolation is essential.

As I mention from time to time, almost the first “on site” question I ask is,

“What is the valid business case for this (user) system to be connected directly or indirectly to external communications?”

Or more simply,

“Why’s this got the Internet?”

Mostly in traditional systems removing external connections makes an attackers job much much harder. Unless you are subject to a deliberately planed attack, which most ransomeware is actually not. The ransomware operators will work on the “low hanging fruit principle” and in a very target rich environment like the Internet, go find an easier target to attack.

It’s a point that is long over due for consideration by senior managment.

By and large companies do not pay employees to

1, Surf the web.

Or many other “not work” activities like download copyright protected misic[1].

Also if you have in house “developers” not giving them Internet access, slows down any “code ‘cut-n-paste'” activities they might indulge in. Which all to frequently as they are “minimal example code” drag a whole ship load of vulnerabilities with them.

All to many organisations of all sizes give “Internet access” to all apparentky based on MBA Mantra’s about ...