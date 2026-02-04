---
title: Microsoft is Giving the FBI BitLocker Keys
url: https://www.schneier.com/blog/archives/2026/02/microsoft-is-giving-the-fbi-bitlocker-keys.html
source: Schneier on Security
date: 2026-02-03
fetch_date: 2026-02-04T04:08:20.534842
---

# Microsoft is Giving the FBI BitLocker Keys

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

## Microsoft is Giving the FBI BitLocker Keys

Microsoft [gives](https://www.forbes.com/sites/thomasbrewster/2026/01/22/microsoft-gave-fbi-keys-to-unlock-bitlocker-encrypted-data/) the FBI the ability to decrypt BitLocker in response to court orders: about twenty times per year.

> It’s possible for users to store those keys on a device they own, but Microsoft also recommends BitLocker users store their keys on its servers for convenience. While that means someone can access their data if they forget their password, or if repeated failed attempts to login lock the device, it also makes them vulnerable to law enforcement subpoenas and warrants.

Tags: [FBI](https://www.schneier.com/tag/fbi/), [full-disk encryption](https://www.schneier.com/tag/full-disk-encryption/), [Microsoft](https://www.schneier.com/tag/microsoft/), [privacy](https://www.schneier.com/tag/privacy/), [Windows](https://www.schneier.com/tag/windows/)

[Posted on February 3, 2026 at 7:05 AM](https://www.schneier.com/blog/archives/2026/02/microsoft-is-giving-the-fbi-bitlocker-keys.html) •
[13 Comments](https://www.schneier.com/blog/archives/2026/02/microsoft-is-giving-the-fbi-bitlocker-keys.html#comments)

### Comments

Vesselin Bontchev •
[February 3, 2026 7:29 AM](https://www.schneier.com/blog/archives/2026/02/microsoft-is-giving-the-fbi-bitlocker-keys.html/#comment-451829)

It’s not just the FBI – Microsoft hands out these keys to any law enforcement agency of any country with a valid warrant.

And the problem is not so much that the keys are stored on Microsoft’s servers but that they aren’t encrypted there (e.g., with a key stored in the TPM of the device).

The other problem, of course, is that Microsoft is making it increasingly impossible to install Windows without a Microsoft account, in which case a ton of your personal stuff is stored on their servers anyway.

Winter •
[February 3, 2026 7:34 AM](https://www.schneier.com/blog/archives/2026/02/microsoft-is-giving-the-fbi-bitlocker-keys.html/#comment-451830)

MS makes things easy for users. As many (most) user will lose their passwords at least once in a lifetime, MS will have to make password recovery easy.

Again, and example of the eternal choice in cryptography:

> *Easy or Secure*

Anyhow, as I have seen over 4 decades of MS failing to honor their promisses, *always*, I had no illusions of security with bitlocker to begin with.

Personally, I stick with VeraCrypt. It has my sweet point of *easy vs secure*.[1]

If I would ever have to use Windows full disk encryption, I would separate the running machine using bitlocker (just to weed out the script kiddies) and store my personal data in VeraCrypt (or my fancy of the week).

[1] Do not bother to explain the shortcomings of VeraCrypt to me. I don’t fight MOSSAD, GRU, nor NSA. For me, Data At Rest is secure enough, as is my personal trust of the end points. YMMV

TimH •
[February 3, 2026 8:35 AM](https://www.schneier.com/blog/archives/2026/02/microsoft-is-giving-the-fbi-bitlocker-keys.html/#comment-451831)

MS also defaults BL to 128 bit, not the other option 256 bit. Since CPUs have the AES-NI instruction that makes decrytion very fast, this is a deliberate weakening.

gpedit.msc: “If you disable or do not configure this policy setting, BitLocker will use the default encryption method of AES 128-bit with Diffuser”

LULZ •
[February 3, 2026 9:04 AM](https://www.schneier.com/blog/archives/2026/02/microsoft-is-giving-the-fbi-bitlocker-keys.html/#comment-451835)

@Q: What Does FBI Stand For?,

I’m sure you meant populating or breeding instead of “breading.”

wiredog •
[February 3, 2026 9:19 AM](https://www.schneier.com/blog/archives/2026/02/microsoft-is-giving-the-fbi-bitlocker-keys.html/#comment-451836)

Some more information, including mitigation, here:
<https://robpegoraro.com/2026/01/23/the-data-that-i-didnt-know-i-didnt-have-to-back-up-to-microsofts-cloud/>

Annony mouse •
[February 3, 2026 9:30 AM](https://www.schneier.com/blog/archives/2026/02/microsoft-is-giving-the-fbi-bitlocker-keys.html/#comment-451837)

Winter

Easy or Secure

For who?

K.S •
[February 3, 2026 10:59 AM](https://www.schneier.com/blog/archives/2026/02/microsoft-is-giving-the-fbi-bitlocker-keys.html/#comment-451838)

I am not aware of a way to bruteforce 128-bit AES key, so unless other shenanigans (e.g., attacks on the entropy source) involved I don’t see it as a valid criticism of MS.

KC •
[February 3, 2026 11:03 AM](https://www.schneier.com/blog/archives/2026/02/microsoft-is-giving-the-fbi-bitlocker-keys.html/#comment-451839)

A few more thoughts from Matt Green:

<https://bsky.app/profile/matthewdgreen.bsky.social/post/3md3vciumvk2s>

Rontea •
[February 3, 2026 12:24 PM](https://www.schneier.com/blog/archives/2026/02/microsoft-is-giving-the-fbi-bitlocker-keys.html/#comment-451840)

What’s at stake here isn’t just personal privacy—it’s the structural integrity of our democracy. When encryption keys are centrally stored and can be compelled by government order, we create a single point of failure for civil liberties. This isn’t about one FBI request in Guam; it’s about the precedent that access to private data is negotiable. Centralized key storage turns every user device into a potential surveillance node, eroding the principle of individual security that underpins trust in both technology and governance. Democracies thrive when citizens can safely communicate and store information without the constant threat of compelled exposure. Weakening that foundation in the name of convenience or compliance risks shifting the balance of power away from the people and toward unchecked institutional oversight.

FireWave •
[February 3, 2026 1:33 PM](https://www.schneier.com/blog/archives/2026/02/microsoft-is-giving-the-fbi-bitlocker-keys.html/#comment-451841)

The real question is why Microsoft doesn’t encrypt this data. Deriving an encryption key from the user’s password would be straightforward.

Clive Robinson •
[February 3, 2026 2:26 PM](https://www.schneier.com/blog/archives/2026/02/microsoft-is-giving-the-fbi-bitlocker-keys.html/#comment-451842)

@ K.S., ALL,

With regards,

> “I am not aware of a way to bruteforce 128-bit AES key, so unless other shenanigans”

Whilst the algorithm is strong the implementation was brittle when you put it into “go faster stripes” of “loop unrolling”, it opened up side channels, which is something the closed community of the NSA, GCHQ and one or two other SigInt agencies knew a lot about, but few outside knew about it or cared.

I’ve reason to believe that the NSA put “the fix in” via NIST and in effect “rigged the AES competition” very much in their favour. And why MicroSoft received little or no issues writings secure code that was anythin but….

There is a clear history of this going on before the NSA was ever even thought about and goes back to Friedman and his Wife at the Riverbank laboratory and onwards.

You ca...