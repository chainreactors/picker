---
title: SecLeaf Q2 CTF 2026 Writeups
url: https://infosecwriteups.com/secleaf-q2-ctf-2026-writeups-e44b5326456a?source=rss----7b722bfd1b8d--bug_bounty
source: Bug Bounty in InfoSec Write-ups on Medium
date: 2026-05-31
fetch_date: 2026-06-01T06:47:06.514409
---

# SecLeaf Q2 CTF 2026 Writeups

[Sitemap](/sitemap/sitemap.xml)

[Open in app](https://play.google.com/store/apps/details?id=com.medium.reader&referrer=utm_source%3DmobileNavBar&source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fsecleaf-q2-ctf-2026-writeups-e44b5326456a&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

[Medium Logo](https://medium.com/?source=post_page---top_nav_layout_nav-----------------------------------------)

Get app

[Write](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-story&source=---top_nav_layout_nav-----------------------new_post_topnav------------------)

[Search](https://medium.com/search?source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fsecleaf-q2-ctf-2026-writeups-e44b5326456a&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

![Unknown user](https://miro.medium.com/v2/resize:fill:64:64/1*dmbNkD5D-u45r44go_cf0g.png)

[## InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---publication_nav-7b722bfd1b8d-e44b5326456a---------------------------------------)

·

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:76:76/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_sidebar-7b722bfd1b8d-e44b5326456a---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

# SecLeaf Q2 CTF 2026 Writeups

[![Aashif](https://miro.medium.com/v2/resize:fill:64:64/1*8QdvHCs5fseRfkj2Vmwayw.jpeg)](https://medium.com/%40Cyb3rX7u?source=post_page---byline--e44b5326456a---------------------------------------)

[Aashif](https://medium.com/%40Cyb3rX7u?source=post_page---byline--e44b5326456a---------------------------------------)

4 min read

·

2 days ago

--

[Listen](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2Fplans%3Fdimension%3Dpost_audio_button%26postId%3De44b5326456a&operation=register&redirect=https%3A%2F%2Finfosecwriteups.com%2Fsecleaf-q2-ctf-2026-writeups-e44b5326456a&source=---header_actions--e44b5326456a---------------------post_audio_button------------------)

Share

From recon to flag capture: a breakdown of my solutions.

Press enter or click to view image in full size

![]()

Hack4Shell — Team Score

First of all, i start with flag format: **SecLeaf{flag}**

### Challenge-1: military\_grade\_encryption (98 points)

Given a file named “**encrypted.txt”.** At first i thought of big encryption technique. But it ended up in simple solution.

> We intercepted an encrypted military transmission during routine monitoring.
> Analysts were unable to identify the encryption scheme used.
> Can you recover the hidden message?

```
U2VjTGVhZntiNDUzNjRfMXNfbjB0XzNuY3J5cHQxMG59
```

It seems like base64 encrypted text. So i used [Cyberchef.io](https://cyberchef.io) with FROM BASE64 to decrypt the text. Then i found the flag.

```
SecLeaf{b45364_1s_n0t_3ncrypt10n}
```

### Challenge-2: important (100 points)

Given a image named “**important.jpg**”. I tried to open the image, it wasn’t opening. It says unsupported file format. Something wierd right?

![]()

Unsupported file format

Then i used ***file***command in my linux machine to find what type of file it was. Then i came to know that it was a ZIP file, which is intentionally kept.

```
-$ file important.jpg
ZIP Archieve file
```

Now i unzipped the zip file and it extracted the flag.txt file.

```
SecLeaf{extensions_can_lie}
```

### Challenge-3: forgotten\_snapshot (100 points)

Given a image named “**snapshot.jpg**”. It is a simple JPEG image file.

> We recovered this image from a damaged backup archive.
>
> Analysts believe the original owner attempted to conceal sensitive information before deletion. Some image data may have survived recovery.

![]()

snapshot.jpg

First i decided to use strings to find, if the flag is hidden in the image.

```
-$ strings snapshot.jpg
```

I was correct. The flag is hidden in the image file which was exposed when the attacker uses strings to find any strings present in the image data.

```
SecLeaf{metadata_never_lies}
```

### Challenge-4: vaultcore (100 points)

Given a file named “**vaultcore**”. We recovered a protected vault executable from an abandoned workstation.

## Get Aashif’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Subscribe

[x]

Remember me for faster sign in

I need to find what file type it was.

```
ELF binary  64-bit, statically linked (no external library dependencies), no section header
```

The secret trick i always use is ***strings*** command.

```
-$ strings vaultcore
SecLeaf{str1ngs_1s_4ll_y0u_n33d}
```

### Challenge-5: double-trouble (300 points)

Again given a file named “**encrypted.txt**”. I conformed that, it would one of the ***cyberchef solvable*** challenge.

> We intercepted a suspicious encoded transmission during routine monitoring.
>
> Analysts believe the message was processed through multiple transformation layers before being transmitted. Can you recover the original message?

```
526e4a7757584a756333737759544e66655452734d325666616a526d5957
64664d3245776148523166513d3d0a
```

It looks like Hex format. So i decoded it.

```
RnJwWXJuc3swYTNfeTRsM2VfajRmYWdfM2EwaHR1fQ==
```

Now it looks like base64 format. Again decoded it.

```
FrpYrns{0a3_y4l3e_j4fag_3a0htu}
```

Now it seems to be in order like ABC{xyz}. It might be rotation of characters, where there is popular method called ROT13, ROT47. I used ROT13 to decode it.

```
SecLeaf{0n3_l4y3r_w4snt_3n0ugh}
```

### Challenge-6: Almost\_there (150 points)

Given a **ZIP file** in the name of “**backup.zip**”. I tried to unzip the zip file, but it wasn’t unzipping. The error here is bad offset.

```
file #1:  bad zipfile offset (local header sig):  0
```

So simply used ***strings*** command and got the output.

```
SecLeaf{repair_the_archive}
```

### Challenge-7: Backup\_leak (150 points)

A web challenge which is more interesting. The developer accidently leaked the backup to public. We need to find the backup file and retrieve the flag.

> ***Target****:* <https://backup-leak.secleaf.tech/index.php>

i tried with /backup, /bak, /backup.zip. No flag found. Then i made curl command to find the flag in smart way.

```
for ext in .bak .backup .old .zip .tar.gz .sql; do
curl https://backup-leak.secleaf.tech/index.php$ext
curl https://backup-leak.secleaf.tech/backup$ext
done
```

Then i found the flag in <https://backup-leak.secleaf.tech/index.php.bak>

![]()

i didn’t saved the flag in my machine :(

### Challenge-8: Memory\_bin (1000 points)

Given “**memory.bin**” file.

> A memory dump file (`memory.bin`) has been provided. Somewhere inside, the real flag is hidden. *"NOTE: The flag you need is hidden in plain sight.*

```
-$ file memory.bin
memory.bin: data

-$ strings memory.bin | grep "SecLeaf"
# many and repeated fake flags
SecLeaf{alm0st_th3r3_just_k1dd1ng} ← FAKE
SecLeaf{y0u_f0und_m3_haha_n0pe} ← FAKE
SecLeaf{wr0ng_flag_ag41n} ← FAKE
SecLeaf{r3ally_th1s_t1me_nope} ← FAKE
```

Then the hint reveals “It was all about hashes”. When I saw the word ‘hash’, my first thought was the MD5 hash function. So I calculated the file’s MD5 hash using `md5sum file`.

![]()

The flag was simply the resulting hash enclosed in the flag format: `SecLeaf{md5_hash}`

```
SecLeaf{019fcb4b2f8de31aa74c62c1f5566f48}
```

Support my work guys.

Clap, Comment, Do follow.

## Thank you

[Cybersecurity](https://medium.com/tag/cybersecuri...