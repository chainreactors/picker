---
title: Pairwise Authentication of Humans
url: https://www.schneier.com/blog/archives/2025/02/pairwise-authentication-of-humans.html
source: Schneier on Security
date: 2025-02-11
fetch_date: 2025-10-06T20:47:42.534207
---

# Pairwise Authentication of Humans

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

## Pairwise Authentication of Humans

Here’s an [easy](https://ksze.github.io/PeerAuth/) system for two humans to remotely authenticate to each other, so they can be sure that neither are digital impersonations.

> To mitigate that risk, I have developed this simple solution where you can setup a unique time-based one-time passcode (TOTP) between any pair of persons.
>
> This is how it works:
>
> 1. Two people, Person A and Person B, sit in front of the same computer and open this page;- They input their respective names (e.g. Alice and Bob) onto the same page, and click “Generate”;- The page will generate two TOTP QR codes, one for Alice and one for Bob;- Alice and Bob scan the respective QR code into a TOTP mobile app (such as Authy or Google Authenticator) on their respective mobile phones;- In the future, when Alice speaks with Bob over the phone or over video call, and wants to verify the identity of Bob, Alice asks Bob to provide the 6-digit TOTP code from the mobile app. If the code matches what Alice has on her own phone, then Alice has more confidence that she is speaking with the real Bob.

Simple, and clever.

Tags: [authentication](https://www.schneier.com/tag/authentication/), [protocols](https://www.schneier.com/tag/protocols/)

[Posted on February 10, 2025 at 7:00 AM](https://www.schneier.com/blog/archives/2025/02/pairwise-authentication-of-humans.html) •
[22 Comments](https://www.schneier.com/blog/archives/2025/02/pairwise-authentication-of-humans.html#comments)

### Comments

Kini •
[February 10, 2025 7:32 AM](https://www.schneier.com/blog/archives/2025/02/pairwise-authentication-of-humans.html/#comment-442905)

Repeat, and you gain a distress code.

Andreas E •
[February 10, 2025 7:54 AM](https://www.schneier.com/blog/archives/2025/02/pairwise-authentication-of-humans.html/#comment-442906)

You can do this without a webpage (i.e. offline): Open KeePass on Alice’s PC, let it generate a decent seed for a TOTP on Alice’s KeePass database and store a copy on Bob’s KeePass database.

Once they’d want to authenticate to each other, they simply both generate the current TOTP and compare.

Zsolt •
[February 10, 2025 8:12 AM](https://www.schneier.com/blog/archives/2025/02/pairwise-authentication-of-humans.html/#comment-442908)

> “The page will generate two TOTP QR codes, one for Alice and one for Bob”

Why do you need two TOTP seeds for authentication between exactly two people? The only reason I can think of is if you want mutual authentication at the very same moment. Otherwise a single TOTP seed (shared between the two people) should suffice and assuming that the code generators (e.g. Google Authenticator) generate/show a new code every minute, they can both authenticate the other one just a minute apart.

Zsolt •
[February 10, 2025 8:45 AM](https://www.schneier.com/blog/archives/2025/02/pairwise-authentication-of-humans.html/#comment-442909)

Sorry for the previous question, didn’t check the source/demo. Now I see that the two QR-codes have the same secret/seed (so there’s only one shared secret as I already assumed should be) and only the labels are different. So Alice’s phone shows the label “Bob” and Bob’s phone shows the label “Alice” in the Authenticator app.

Sean •
[February 10, 2025 8:55 AM](https://www.schneier.com/blog/archives/2025/02/pairwise-authentication-of-humans.html/#comment-442910)

Seems to me this is something old, long ago solved by PGP, where you each have the public key of the other, and being in front of the same computer in person you can simply have a key swap instead. About as secure, and also allows the message to be encrypted as well each way.

wiredog •
[February 10, 2025 9:34 AM](https://www.schneier.com/blog/archives/2025/02/pairwise-authentication-of-humans.html/#comment-442912)

This gives Alice confidence she’s talking to whoever has Bob’s phone, and vice versa. Whether Alice and Bob are actually holding the phones may be undetermined.

Jack S •
[February 10, 2025 10:36 AM](https://www.schneier.com/blog/archives/2025/02/pairwise-authentication-of-humans.html/#comment-442913)

Yep, confirming the hardware, not the person.

Jay Ashworth •
[February 10, 2025 11:28 AM](https://www.schneier.com/blog/archives/2025/02/pairwise-authentication-of-humans.html/#comment-442915)

As Jack and Wiredog suggest (and I commented on FB), “verify the identity of Bob” seems to be carrying too much water here: even if you’re sure Bob’s phone hasn’t gone walkabout, this protocol doesn’t guarantee to Alice that it *is* Bob; something else has to do that — it’s not in-scope here, right?

Geoffrey •
[February 10, 2025 12:33 PM](https://www.schneier.com/blog/archives/2025/02/pairwise-authentication-of-humans.html/#comment-442918)

This would still be vulnerable to MITM attacks I suppose?

Harry Potter •
[February 10, 2025 2:05 PM](https://www.schneier.com/blog/archives/2025/02/pairwise-authentication-of-humans.html/#comment-442919)

Obligatory XKCD:

Me •
[February 10, 2025 2:10 PM](https://www.schneier.com/blog/archives/2025/02/pairwise-authentication-of-humans.html/#comment-442920)

@Harry Potter

You may be a wizard, but I am apparently psychic. I saw the xkcd link, and immediately knew you were talking about the $5 wrench attack.

Anony •
[February 10, 2025 6:47 PM](https://www.schneier.com/blog/archives/2025/02/pairwise-authentication-of-humans.html/#comment-442924)

Has anyone considered man-in-the-middle with AI? AI could handle the conversation, mimic the other person’s voice, etc; Separating into two independent conversations when the time was right; And rejoining the original parties with a time-lag afterwards…

Like a conversation between a CEO & CFO, and inserting a bit in the middle of the conversation about fraudulently cutting a check to some company right away. That sort of thing has been done before, but involved completely faking the entire CEO side, not inserting extra parts into the CEO side in the middle of a real conversation in real time without either party being the wiser.

Kinda puts Britain’s idea about forcing Apple to break their encryption into perspective… I wonder how many such AI phone calls it would take for their higher-ups to see the light? Perhaps just one, done as a proof-of-concept demonstration?

As for the system described above, we already do something similar by asking questions only the correct party knows: What is your childhood pet’s name? Where did you grow up? Who was your high school sweetheart? What color was your first car? Heck, my credit card company verifies me with extra numbers printed on my credit card that only they know.

I actually saw this happen back when I was a kid, with school bullies phoning up other kids pretending to be someone else. My friends & I just exchanged a password, or an unusual response to a standard question like ‘Hows the weather?”, to verify the other party.

This system is just a more co...