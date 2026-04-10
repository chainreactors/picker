---
title: Password Manager Angst
url: https://www.tbray.org/ongoing/When/202x/2026/04/09/Password-Manager-Angst
source: ongoing by Tim Bray
date: 2026-04-09
fetch_date: 2026-04-10T04:44:54.770223
---

# Password Manager Angst

# Password Manager Angst

![Opens, and navigates to, search input field](/ongoing/misc/smallmag.png)

Our family has used
[1Password](https://1password.com) for many years. Most recently 1Password 7, now at least three years out of
date. We didn’t want to upgrade to the latest version, went looking for alternatives, and have been exploring
[Bitwarden](https://bitwarden.com). The best choice isn’t obvious; here’s the story thus far.

Important note: I suspect that most-to-all of the people reading this already are using a password manager. If you’re not,
please, ***PLEASE*** start now. Your browser probably has an OK one built-in, which is much better than
nothing.
[Here](https://www.cyber.gc.ca/en/guidance/password-managers-security-itsap30025) is a good write-up on the basics.

Our needs ·
They’re not fancy. The house contains Macs and Androids and Windows and an iPad.
We have hundreds of accounts (some require an authenticator) and a basketfull of secure notes: Government-ID numbers, recovery
codes, and so on.

1Password7 and 8 ·
1Password had this nice feature where you could sync between devices without involving any 1Password servers, in a variety
of ways. We used one of those and liked it.
1Password8 insists on storing your data (encrypted, more on that later). That always bothered me because, obviously, that
repository is a top-priority juicy target for all the bad guys, who range from employees of the Chinese government to geeky
narcos.

So we’ve been ignoring 1Password’s increasingly plaintive reminders that we were using years-out-of-date software
and chugging along with version 7. But, early this year, they broke our sync mode on the Android app and were pretty blunt that the only
way to get it back was to go to 1P8.

Alternatives ·
There are plenty of password managers (Let’s just say “PMs”) out there, but as a regular scanner of the landscape,
it seems to me that 1Password
(hereinafter “1P”) and Bitwarden (“Bw”) stand out as leaders. The rest of this piece will focus on those two.
If you think I’m wrong, say so below but also please say why.

Note that Bw comes in two flavors: That offered as a subscription service by the company of the same name, or as an open-source
software suite you can build and run yourself.

This is not to say that the PMs that are starting to appear built-in to browsers and OSes are worthless or unimportant,
just that some of us need a little more.

The threat models ·
Two are obvious. The first is incompetence, like for example
[LastPass](https://en.wikipedia.org/wiki/LastPass#Security_incidents), who apparently left the doors more or less
wide open to those bad guys I mentioned a few paragraphs ago. Complete horror-show.

The second is legal compulsion, where a government applies pressure to a PM provider to cough up our
secrets. Anybody who thinks governments won’t try is fooling themselves, because they’ve repeatedly said they want to, and are
eager to pass ill-considered legislation such as the
[CLOUD Act](https://en.wikipedia.org/wiki/CLOUD_Act). So we care about that aspect a lot.

1P vs Bw: Security ·
I think they both have acceptably-good security postures; check out
[Bitwarden Security Whitepaper](https://bitwarden.com/help/bitwarden-security-white-paper/) and
[About the 1Password security model](https://support.1password.com/1password-security/).

Both of them offer to host your data outside of the US, specifically in Canada or the EU.

But it doesn’t matter *that* much if a bad guy or bad government gets their hands on your password store; what
matters is whether or not they can decrypt it. I’m not an infosec professional but I know some and listen to them, and both
those security postures give me a good feeling. It’s not an accident that they’re pretty similar.

The actual threat isn’t so much that an adversary cracks the crypto; that’s very unlikely. It’s that they find a way to force
a PM vendor to build a back door into their software to get access to keys and passwords. For that reason, it would warm
my heart if either or both of Bw and 1P were to post a
[Warrant Canary](https://en.wikipedia.org/wiki/Warrant_canary).

But I’m going to give Bw a very slight edge. First, because of the fact that you can build and run it yourself, if you’re
willing to take responsibility for operating a server with strong security requirements. (I’m not.)

The source being open potentially offers a second, and more important I think, advantage: If they were able to get a
[Reproducible build](https://en.wikipedia.org/wiki/Reproducible_builds) working, you’d have assurance that the code
you can download is the one their service is running. Which reduces the attack surface. (Mind you,
[not to zero](https://www.cs.cmu.edu/~rdriley/487/papers/Thompson_1984_ReflectionsonTrustingTrust.pdf).) Reproducible
builds are hard, but if they did that, it would make a difference to me.

On the other hand, Bw’s software development process
[embraces GenAI](https://contributing.bitwarden.com/contributing/ai/) generally and Claude specifically.
At this stage in the growth of those technologies, this sends a chill up my spine. To be fair, 1P’s website
shouts that it’s just the thing for agentic security, whatever that means. And we don’t know anything about 1P’s internal
software-dev process.

1P vs Bw: Fit and finish ·
1P wins this one. The problem is, do they always pop up when needed and never when they’re not? Can they fill every login
field that needs filling? Does the popup show you just what you need and nothing extraneous? I’ve used both and 1P is just
better.

Business issues ·
This one is also pretty well a saw-off. Both of them have taken substantial chunks of VC money and thus are going to
come under relentless pressure to enshittify. I worry a little less about this because from what I read,
there’s not much lock-in.

Personal experience too: I recently did an export of everything out of 1P and into Bw and it all Just Worked, albeit putting all
my stuff into a folder named "No Folder" that I can’t figure out how to rename.

Both Bw and 1P are subscription-only, at a price that seems fair to me.

Death and recovery and pen and paper ·
As I was reading up on this stuff, the issue of recovering access to your PM after it had been lost came up a couple of times.
Here’s a scenario where that could be really important: I die. And then my wife needs to get access to bank accounts and
business emails and so on.

Somebody (I’ve lost the link) was horrified that one of the PMs suggested writing the password down on a piece of paper as a
last-resort measure, but I’m here to tell you that they’re wrong. My wife has an envelope containing a piece of paper on which
appear the passwords for my PM and Mac, my mobile-phone PIN, and a very small number of other secret things she might really
need if I’m suddenly gone. I have no idea where she put it, but she’s really smart so I don’t worry.

You should probably do something like this too.

What will we do? ·
We’ve paid for a year’s worth of both Bw and 1P. At the moment, we’re leaning to 1P because it’s a little more polished.
Which matters because my PM is something I use many times every day. Also they’re somewhat Canadian.

If you think we’ve missed something, please do let us know.

---

**Updated: 2026/04/09**

---

## Contributions

Comment feed for ongoing:[![Comments feed](/ongoing/Feed.png)](/ongoing/comments.atom)

From: [Paul Bryan](https://pbryan.ca) (Apr 09 2026, at 17:11)

The easiest and most manageable solution I've landed on is an offline KeePass-compatible password manager (e.g. KeePassXC, KeePassDX, Secrets, etc.) and sync the file between devices (I've elected for my laptop to be master, and replicate to my tablet and mobile phone).

This works well for my untimely death, as I've just written the passphrase to my devices and password database on an index card and put it in my safety deposit box. My wife and son know how to access it, and are familiar enough with the pas...