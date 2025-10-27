---
title: LostPass: after the LastPass hack, here’s what you need to know
url: https://grahamcluley.com/lostpass-after-the-lastpass-hack-heres-what-you-need-to-know/
source: Graham Cluley
date: 2023-01-04
fetch_date: 2025-10-04T03:02:10.816697
---

# LostPass: after the LastPass hack, here’s what you need to know

[Skip to content](#content)

[Graham Cluley](https://grahamcluley.com/)

Cybersecurity and AI keynote speaker

[BOOK ME](/about-this-site/public-speaking/ "Book cybersecurity expert Graham Cluley to speak at your event")

[Speaking](/ "Home") · [Writing](/writing/ "Writing") · [Podcasts](/podcasts/ "The AI Fix and Smashing Security podcasts") · [Video](/video/ "Video") · [Contact](/contact/ "Contact Graham Cluley") · [About](/about-this-site/ "About Graham Cluley") · [Games](/misc/ "Games")   [🔍](/search "Search")

⁠This week's sponsor: [Browse privately with a secure VPN that safeguards your privacy. Unblock content worldwide. Get 64% Off Proton VPN.](https://grahamcluley.com/go/protonvpn/)

[ⓘ](/sponsorship/ "Learn more about sponsoring this website")

This article is more than **2 years old**

# LostPass: after the LastPass hack, here’s what you need to know

[![Graham Cluley](https://grahamcluley.com/wp-content/uploads/2023/07/cropped-cluley-250-jpeg-70x70.webp)

Graham Cluley](https://grahamcluley.com/author/grahamcluley/ "Link to other articles by Graham Cluley") @ 4:23 pm, January 3, 2023

![](/wp-content/uploads/2024/11/bluesky-icon-48-1.png "Bluesky") [@grahamcluley.com](https://bsky.app/profile/grahamcluley.com "Link to @grahamcluley.com on Bluesky")
![](/wp-content/uploads/2024/11/mastodon-icon-48.png "Mastodon") [@[email protected]](https://mastodon.green/%40gcluley "Follow @gcluley on Mastodon")

![LostPass: after the LastPass hack, here's what you need to know](https://grahamcluley.com/wp-content/uploads/2023/01/lostpass-1.jpeg)

### What’s happened?

Just days before Christmas, when most people probably weren’t paying too much attention, password management service LastPass [revealed](https://blog.lastpass.com/2022/12/notice-of-recent-security-incident/ "Link to LastPass announcement") that hackers had accessed customers’ password vaults.

### That sounds really bad. But wasn’t there news of a LastPass hack earlier in the year?

You’re probably thinking of the original announcement LastPass made back on August 25 2022, where it said that a hacker had managed to gain access to a developer’s account, and stolen some of its source code from a development environment.

Back then LastPass said that it had “seen no evidence that this incident involved any access to customer data or encrypted password vaults.”

### So they were wrong when they said that?

Well, LastPass might have not *seen* any evidence that customers’ passwords vaults had been accessed then, but…

### But when a company says it has “seen no evidence” of anything bad happening, that’s not necessarily the same as saying “nothing bad happened”?

Correct. And sure enough, just before Christmas, LastPass confirmed that the information stolen from a developer’s account in the August 2022 attack was actually “used to target another employee, obtaining credentials and keys which were used to access and decrypt some storage volumes…”

![Part of LastPass blog post](https://grahamcluley.com/wp-content/uploads/2023/01/lastpass-blog-post.jpeg)

### Gulp! That sounds much worse. So let me get this straight – the theft of the password vaults and other data from LastPass may well have occurred in August or September… long before they announced it as I was distracted wrapping Christmas presents?

Perhaps. LastPass hasn’t said when it believes the theft of the password vaults occurred, but the most important thing to you is probably *what* the stolen data contained, and how it could be exploited by hackers.

### Ok. I’m bracing myself. Tell me the worst…

The stolen data includes the following *unencrypted* data:

* company names
* end user names
* billing addresses
* telephone numbers
* email addresses
* IP addresses which customers used to access LastPass
* website URLs from your password vault

In other words, cybercriminals now know that you use LastPass, they know how to contact you, and they know which websites you use.

That’s valuable information for anyone attempting to phish further information from you, as they could easily pose as one of the websites you access and send you a scam email.

Furthermore, simply knowing which websites you access (and store in your password manager) might reveal private information about you that you would have rather remain confidential.

And further still, it’s possible you stored password reset links for these websites in your password manager that might not have expired, or other sensitive information or tokens in your website URLs that you wouldn’t want to fall into the wrong hands.

### This sound terrible…

Hang on, I haven’t finished.

Because the hackers also stole *encrypted* customer data including:

* website usernames and passwords
* secure notes
* form-filled data

### But that’s encrypted, right?

Yes, it’s encrypted. The hackers need to determine what your LastPass master password is, to access the crown jewels – the usernames and passwords to all your online accounts.

### Well, I have a strong, hard-to-guess, unique password. And I have two-factor authentication (2FA) enabled on my LastPass account. So I’m safe…

Hmm, well… 2FA is irrelevant in this case. The hackers have already stolen the password vault data, they don’t need to bother logging into anyone’s LastPass account.

Similarly, changing your password now doesn’t undo the data breach. It may still be a sensible step to take, of course.

And what’s going to help the hackers is that many many LastPass users are likely to have chosen master passwords that are much weaker than LastPass itself recommends.

Since 2018, LastPass says it has [recommended](https://support.lastpass.com/help/what-is-the-lastpass-master-password-lp070014 "Link to LastPass support knowledgebase") and required a “twelve-character minimum for master passwords”.

Aside from the fact that the number of characters alone isn’t a good indicator of password strength, it appears that customers who have been with LastPass since before 2018 have not been required to update their master passwords to meet LastPass’s own recommendations – leaving the encrypted parts of their password vaults much more vulnerable.

### It sounds like LastPass missed an opportunity to boost its users’ security there…

Yes, it does rather.

And what’s more, security researchers have revealed that at least some of the master passwords stored by LastPass for its longer-standing users’ vaults have been encrypted in a way which makes them far too easy to crack.

### What do you mean?

As researcher Wladimir Palant [details](https://palant.info/2022/12/28/lastpass-breach-the-significance-of-these-password-iterations/ "Link to Almost Secure blog"), LastPass salts-and-hashes master passwords using the PBKDF2 algorithm, with 100,100 iterations.

The number of “iterations” is an indication of just how much “work” someone (or more likely a modern graphics card) is going to have to do to break your password.

However, many LastPass users who have had their accounts for a long time appear to have only had their accounts configured for 5000 iterations, or in some cases as low as 500, or even one!

Such poorly-secured vaults may not take too long (or cost too much money) to unlock.

![Snippet from Palant's blog](https://grahamcluley.com/wp-content/uploads/2023/01/palant-blog.jpeg)

Snippet from Wladimir Palant’s blog post.

And, as LastPass rival 1Password [explains](https://blog.1password.com/not-in-a-million-years/ "Link to 1Password blog"), the figures become much worse when it is a human-created password that the hackers are trying to crack rather than a truly randomly-generated one.

Oh, by the way, OWASP’s 2021 [guidance](https://cheatsheetseries.owasp.org/cheatsheets/Password_Storage_Cheat_Sheet.html "LInk to OWASP password storage cheat sheet") is for… err… 310,000 or more iterations…

### Years ago, shouldn’t LastPass have contacted those customers who had a low number of iterations, and forced them to boost their security?

You would think ...