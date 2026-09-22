---
title: Hash Identifier Tools – Command-Line Password Hash Identification
url: https://www.darknet.org.uk/2026/09/hash-identifier-tools-command-line-password-hash-identification/
source: Over Security
date: 2026-09-21
fetch_date: 2026-09-22T07:04:57.594543
---

# Hash Identifier Tools – Command-Line Password Hash Identification

* [Skip to main content](#genesis-content)
* [Skip to primary sidebar](#genesis-sidebar-primary)
* [Skip to footer](#genesis-footer-widgets)

* [Home](https://www.darknet.org.uk/)
* [About Darknet](https://www.darknet.org.uk/about/)
* [Hacking Tools](https://www.darknet.org.uk/category/hacking-tools/)
* [Popular Posts](https://www.darknet.org.uk/popular-posts/)
* [Darknet Archives](https://www.darknet.org.uk/darknet-archives/)
* [Contact Darknet](https://www.darknet.org.uk/contact-darknet/)
  + [Advertise](https://www.darknet.org.uk/contact-darknet/advertise/)
  + [Submit a Tool](https://www.darknet.org.uk/contact-darknet/submit-a-tool/)

[![darknet.org.uk logo](https://www.darknet.org.uk/wp-content/uploads/2026/03/darknet_header_hacking_cybersec_vF-scaled.png)](https://www.darknet.org.uk/)

Darknet - Hacking Tools, Hacker News & Cyber Security

Darknet is your best source for the latest hacking tools, hacker news, cyber security best practices, ethical hacking & pen-testing.

You are here: [Home](https://www.darknet.org.uk/) / [Cryptography](https://www.darknet.org.uk/category/cryptography/) / Hash Identifier Tools – Command-Line Password Hash Identification

# Hash Identifier Tools – Command-Line Password Hash Identification

Published September 21, 2026 |

Views: 163

I tested hashID 3.1.4 and Name-That-Hash 1.11.0 against the same hash samples. Both recognised `$2a$` bcrypt but rejected the otherwise identical `$2b$` sample. Only Name-That-Hash recognised the Argon2id sample.

![Hash Identifier Tools — Command-Line Password Hash Identification, with one data specimen sorted into several candidate paths; darknet.org.uk.](https://www.darknet.org.uk/wp-content/uploads/2026/09/hash-identifier-tools-command-line-password-hash-identification-640x360.webp)

Both tools were installed through `pip` and tested on 6 September 2026.

Advertisement

Two others worth knowing, haiti and hashcat, are at the end as alternatives. I didn’t run those, and I say so where they appear.

## Different formats, the same hexadecimal shape

Start with the MD5 of the word `password`, a bare 32-character hexadecimal string. Ask [hashID](https://www.darknet.org.uk/2017/02/hashid-identify-different-types-of-hashes/) what it is, and it returns **eighteen** possibilities; ask Name-That-Hash and it returns **twenty-four**. Both are right to.

MD5, NTLM, LM, MD4, the Domain Cached Credentials formats and a dozen others all produce exactly 128 bits of hex, and nothing in the string itself separates them.

Take a concrete case. The empty LM hash constant `aad3b435b51404eeaad3b435b51404ee` – the value that fills the LM field of a Windows credential dump whenever the LM hash is blank – produces the same shapeless list from both tools, headed by MD5 and NTLM.

Both tools returned candidate lists for this sample rather than identifying it specifically as the empty LM constant. For the common hexadecimal formats, an identifier narrows the field and then hands the real decision back to you.

Provenance – which system produced the hash, which file it sat in – resolves what the string cannot. So the identifiers earn their keep on formats that carry a self-describing prefix, and that’s where they start to differ.

Advertisement

## The 2026 blind spot both common tools share

bcrypt hashes announce themselves with a version prefix. Give both tools a classic `$2a$` bcrypt hash, and both identify it correctly – hashID offers bcrypt alongside its two aliases, Name-That-Hash the same. Now change the `a` to a `b` in the prefix, making it `$2b$` and leaving everything else identical:

$ hashid '$2b$10$N9qo8uLOickgx2ZMRZoMyeIjZAgcfl7p92ldGxad68LJZdL17lhWy'
[+] Unknown hash
$ nth -t '$2b$10$N9qo8uLOickgx2ZMRZoMyeIjZAgcfl7p92ldGxad68LJZdL17lhWy'
No hashes found.

|  |  |
| --- | --- |
| 1  2  3  4  5 | $ hashid '$2b$10$N9qo8uLOickgx2ZMRZoMyeIjZAgcfl7p92ldGxad68LJZdL17lhWy'  [+] Unknown hash    $ nth -t '$2b$10$N9qo8uLOickgx2ZMRZoMyeIjZAgcfl7p92ldGxad68LJZdL17lhWy'  No hashes found. |

**Both fail.** `$2b$` isn’t an exotic variant. Python’s maintained bcrypt library generates `$2b$` by default, so passwords hashed through that path today land in this form unless the caller overrides the prefix.

Two different identifiers, both a single `pip` command away, and neither recognises a current bcrypt prefix while both handle the older `$2a$`.

The reported bcrypt results use a 60-character sample; the earlier malformed sample was excluded.

## Where the two identifiers diverge

They part company on Argon2, the algorithm that won the Password Hashing Competition and that current guidance names first for new password storage. Given an Argon2id string, hashID returns `Unknown hash`; Name-That-Hash returns `Argon2id`. That’s the clearest difference in capability between them.

hashID’s pattern table hasn’t changed since 2015. In this test, it missed both `$2b$` and Argon2id; Name-That-Hash recognised Argon2id but shared the `$2b$` miss.

The `$2b$` prefix dates from 2014, before hashID’s March 2015 release, so it’s a gap the tool never covered, not one that opened up under it. Argon2id does post-date it, and the frozen table is the obvious explanation for that miss.

On the MD5 sample, Name-That-Hash also returned the longer list, twenty-four against hashID’s eighteen, though that’s one input and not a census of either tool’s rules. Of the two, it’s the better-informed on this set. But more maintained isn’t the same as complete: the `$2b$` gap belongs to both.

## Other maintained options, not tested here

Two more tools are worth knowing, and both were outside what I could run here – the environment had neither a Ruby runtime nor a hashcat build. So what follows is drawn from their documentation and source, not from a test. Read it as a pointer, not a result standing alongside the two above.

[haiti](https://github.com/noraj/haiti) is a Ruby identifier that’s actively developed, with a v4 release in early 2026 and recent commits. Its documented draw is that it returns the matching [hashcat](https://www.darknet.org.uk/2013/11/hashcat-multi-threaded-password-hash-cracking-tool/) and John the Ripper references beside each candidate, which is the detail you want if identification is a step toward cracking.

It installs as a gem rather than through `pip`. Whether it clears the `$2b$` bar that both tested tools failed is exactly the claim I won’t make without running it.

And if the next step is a crack, identification may not need a separate tool at all. [hashcat](https://github.com/hashcat/hashcat) carries an `--identify` option, documented in its own usage text as showing all supported algorithms for an input hash.

Asking hashcat directly removes a translation step between an identifier’s naming and hashcat’s mode numbers. That option is in hashcat’s source; I didn’t run it here.

## What to actually use

When Darknet covered hashID in 2017, the page already noted it hadn’t been updated since 2015. This comparison asks whether moving to a maintained identifier closes that gap. For `$2b$`, it doesn’t.

For a quick look at a hash you already have context for, either pip-installable identifier is fine, and Name-That-Hash is the better-informed of the two: it knows more recent formats, and it’s still maintained. Keep hashID’s limits in mind – this site’s [closer look at hashID](https://www.darknet.org.uk/2017/02/hashid-identify-different-types-of-hashes/) lays out the full extent of its 2015 freeze.

If you’re working toward a crack, let hashcat identify the hash it’s about to attack. And if identification is a recurring part of your workflow, haiti’s cracker-reference output is worth the gem install.

*Tested 6 September 2026. hashID v3.1.4 and Name-That-Hash 1.11.0 were run against a fixed hash set; haiti and hashcat were not run in this environment, and their behaviour is cited from documentation and source, as noted above.*

Advertisement

## Related Posts:

* [Dark Web Search Engines for Security Research:…](h...