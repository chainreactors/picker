---
title: A New Kali Linux Archive Signing Key
url: https://www.kali.org/blog/new-kali-archive-signing-key/
source: Over Security - Cybersecurity news aggregator
date: 2025-04-29
fetch_date: 2025-10-06T22:08:36.889072
---

# A New Kali Linux Archive Signing Key

* [Join Free CTF](https://www.offsec.com/events/the-gauntlet/?utm_source=kali&utm_medium=web&utm_campaign=menu)
* [Get Kali](https://www.kali.org/get-kali/)
* [Blog](https://www.kali.org/blog/)
* Documentation

  [Documentation Pages](https://www.kali.org/docs/)
  [Tools Documentation](https://www.kali.org/tools/)
  [Frequently Asked Questions](https://www.kali.org/faq/)
  [Known Issues](https://bugs.kali.org/search.php?project_id=1&category_id[]=General%20Bug&category_id[]=Kali%20Package%20Bug&category_id[]=Kali%20Package%20Improvement&status[]=30&status[]=40&status[]=50&sticky=on&sort=id%2Clast_updated&dir=DESC%2CDESC&hide_status=-2&match_type=0)
* Community

  [Community Support](https://www.kali.org/community/)
  [Forums](https://forums.kali.org/)
  [Discord](https://discord.kali.org/)
  [Join Newsletter](https://www.kali.org/newsletter/)
  [Mirror Location](https://http.kali.org/README?mirrorlist)
  [Get Involved](https://www.kali.org/docs/community/contribute/)
* [Courses](https://www.offsec.com/kali-training/courses/?utm_source=kali&utm_medium=web&utm_campaign=menu)
* Developers

  [Git Repositories](https://gitlab.com/kalilinux)
  [Packages](https://pkg.kali.org/)
  [Auto Package Test](https://autopkgtest.kali.org/)
  [Bug Tracker](https://bugs.kali.org/)
  [Kali NetHunter Stats](https://nethunter.kali.org/)
* About

  [Kali Linux Overview](https://www.kali.org/features/)
  [Press Pack](https://gitlab.com/kalilinux/documentation/press-pack/-/archive/main/press-pack-main.zip)
  [Wallpapers](https://www.kali.org/wallpapers/)
  [Kali Swag Store](https://offsec.usa.dowlis.com/kali/view-all.html)
  [Meet The Kali Team](https://www.kali.org/about-us/)
  [Partnerships](https://www.kali.org/partnerships/)
  [Contact Us](https://www.kali.org/contact/)

LIGHT
[ ] DARK

![](https://www.kali.org/blog/new-kali-archive-signing-key/images/new-kali-signing-key.jpg)
Monday, 28 April 2025

# A New Kali Linux Archive Signing Key

Table of Contents

* [TL;DR](#tldr)
* [Long version](#long-version)
* [Restarting from scratch](#restarting-from-scratch)
* [Q & A](#q--a)

## TL;DR

Bad news for Kali Linux users! In the coming day(s), `apt update` is going to fail for pretty much everyone out there:

```
Missing key 827C8569F2518CC677FECA1AED65462EC8D5E4C5, which is needed to verify signature.
```

Reason is, we had to roll a new signing key for the Kali repository. **You need to download and install the new key manually**, here’s the one-liner:

```
┌──(kali㉿kali)-[~]
└─$ sudo wget https://archive.kali.org/archive-keyring.gpg -O /usr/share/keyrings/kali-archive-keyring.gpg
```

Now your Kali is ready to keep rolling! Sorry for the inconvenience.

---

## Long version

In the coming day(s), pretty much every Kali system out there will fail to update. You are likely to see this error message when you run `apt update`:

```
┌──(kali㉿kali)-[~]
└─$ sudo apt update
Get:1 https://http.kali.org/kali kali-rolling InRelease [41.5 kB]
Err:1 https://http.kali.org/kali kali-rolling InRelease
  Sub-process /usr/bin/sqv returned an error code (1), error message is: Missing key 827C8569F2518CC677FECA1AED65462EC8D5E4C5, which is needed to verify signature.
Fetched 41.5 kB in 3s (16.5 kB/s)
82 packages can be upgraded. Run 'apt list --upgradable' to see them.
Warning: An error occurred during the signature verification. The repository is not updated and the previous index files will be used. OpenPGP signature verification failed: https://http.kali.org/kali kali-rolling InRelease: Sub-process /usr/bin/sqv returned an error code (1), error message is: Missing key 827C8569F2518CC677FECA1AED65462EC8D5E4C5, which is needed to verify signature.
Warning: Failed to fetch https://http.kali.org/kali/dists/kali-rolling/InRelease  Sub-process /usr/bin/sqv returned an error code (1), error message is: Missing key 827C8569F2518CC677FECA1AED65462EC8D5E4C5, which is needed to verify signature.
Warning: Some index files failed to download. They have been ignored, or old ones used instead.
```

This is not only you, this is for everyone, and this is entirely our fault. We lost access to the signing key of the repository, so we had to create a new one. At the same time, we froze the repository (you might have noticed that there was no update since Friday 18th), so nobody was impacted yet. But we’re going to unfreeze the repository this week, and it’s now signed with the new key.

As a result, there’s a bit of manual work for you. You need to download and install this new key manually, as such:

```
┌──(kali㉿kali)-[~]
└─$ sudo wget https://archive.kali.org/archive-keyring.gpg -O /usr/share/keyrings/kali-archive-keyring.gpg
```

If you prefer using curl, that’s just as easy:

```
┌──(kali㉿kali)-[~]
└─$ sudo curl https://archive.kali.org/archive-keyring.gpg -o /usr/share/keyrings/kali-archive-keyring.gpg
```

As a matter of good practice, you should verify that the checksum of the file matches the one below:

```
┌──(kali㉿kali)-[~]
└─$ sha1sum /usr/share/keyrings/kali-archive-keyring.gpg
603374c107a90a69d983dbcb4d31e0d6eedfc325  /usr/share/keyrings/kali-archive-keyring.gpg
```

You can also take a closer look at the new keyring, it contains the old signing key (`ED444FF07D8D0BF6`) and the new signing key (`ED65462EC8D5E4C5`):

```
┌──(kali㉿kali)-[~]
└─$ gpg --no-default-keyring --keyring /usr/share/keyrings/kali-archive-keyring.gpg -k
/usr/share/keyrings/kali-archive-keyring.gpg
--------------------------------------------
pub   rsa4096 2025-04-17 [SC] [expires: 2028-04-17]
      827C8569F2518CC677FECA1AED65462EC8D5E4C5
uid           [ unknown] Kali Linux Archive Automatic Signing Key (2025) <[email protected]>

pub   rsa4096 2012-03-05 [SC] [expires: 2027-02-04]
      44C6513A8E4FB3D30875F758ED444FF07D8D0BF6
uid           [ unknown] Kali Linux Repository <[email protected]>
sub   rsa4096 2012-03-05 [E] [expires: 2027-02-04]
```

And as you can see, `apt update` still works (or works again, if you’re reading this *after* seeing the apt error):

```
┌──(kali㉿kali)-[~]
└─$ sudo apt update
[...]
68 packages can be upgraded. Run 'apt list --upgradable' to see them.
```

Time to update your system!

## Restarting from scratch

In some cases, you might just prefer to rebuild your Kali system(s) from scratch. For that purpose, we updated all of our images so that it contains the new keyring.

Just head to [Get Kali](https://www.kali.org/get-kali/) and grab the latest images. You will notice that the version in the filenames is `2025.1c`. These are the exact same images as the ones we [released a month ago](https://www.kali.org/blog/kali-linux-2025-1-release/), the only difference being that it contains the new keyring. You can also use the weekly images, starting from `2025-W17` they contain the new keyring.

We also updated Kali NetHunter, VM, Cloud, Docker, WSL, etc etc… Please ping us if you think we forgot something.

## Q & A

**Q**. So your key was compromised and you don’t want to admit it, right?

**A**. No. As you can see we still include the old key in the keyring, if it was compromised we would have removed it and provided a revocation certificate.

---

**Q**. I don’t trust this new key! Are you really Kali Linux?

**A**. The new key is signed by some developers from the Kali team, and the signatures are available on the Ubuntu OpenPGP keyserver. You can check it out at <https://keyserver.ubuntu.com/pks/lookup?search=827C8569F2518CC677FECA1AED65462EC8D5E4C5&fingerprint=on&op=index>.

---

**Q**. Wait a moment, I have an impression of *déjà vu*…

**A**. Back in 2018, we had let the GPG key expire accidentally… There’s still an old tweet <https://x.com/kalilinux/status/959515084157538304> to testify.

---

**More questions? Need support?** Head to the Kali Linux [Forums](https://forums.kali.org/), [Discord Channel](https://discord.kali.org/) or [IRC Channel](https://www.kali.org/docs/community/kali-linux-irc-channel/), at your preference, and get in touch. We’ll be happy to help.

Table of Contents

...