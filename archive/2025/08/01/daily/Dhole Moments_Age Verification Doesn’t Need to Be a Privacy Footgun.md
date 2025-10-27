---
title: Age Verification Doesn’t Need to Be a Privacy Footgun
url: https://soatok.blog/2025/07/31/age-verification-doesnt-need-to-be-a-privacy-footgun/
source: Dhole Moments
date: 2025-08-01
fetch_date: 2025-10-07T00:47:50.375127
---

# Age Verification Doesn’t Need to Be a Privacy Footgun

[Skip to the content](#site-content)

Search

[Dhole Moments](https://soatok.blog/)

Software, Security, Cryptography, and Furries

Menu

* [Home](https://soatok.blog/)
* [Blog](https://soatok.blog/b/)
* [Explore](https://soatok.blog/explore/)
* [About](https://soatok.blog/about/)

Search

Search for:

Close search

Close Menu

* [Home](https://soatok.blog/)
* [Blog](https://soatok.blog/b/)
* [Explore](https://soatok.blog/explore/)
* [About](https://soatok.blog/about/)

Categories

[Badness](https://soatok.blog/category/society/badness/) [Cryptography](https://soatok.blog/category/cryptography/)

# Age Verification Doesn’t Need to Be a Privacy Footgun

* Post author

  By [Soatok](https://soatok.blog/author/soatok/)
* Post date

  [July 31, 2025](https://soatok.blog/2025/07/31/age-verification-doesnt-need-to-be-a-privacy-footgun/)

![Age Verification Doesn’t Need to Be a Privacy Footgun](https://i0.wp.com/soatok.blog/wp-content/uploads/2025/07/BlogHeader-2025-AgeVerificationPrivacy.png?fit=1200%2C675&ssl=1)

“Won’t someone think of the poor children?” they say, clutching their pearls as they enact another stupid law that will harm the privacy of every adult on Earth and create Prior Restraint that inhibits the freedom of speech in liberal democracies.

![Facepaw](https://i0.wp.com/soatok.blog/wp-content/uploads/2020/04/soatok_stickerpack-facepaw.png?resize=512%2C512&ssl=1)

Art: [CMYKat](https://cmykatgraphics.carrd.co/)

If you’re totally ignorant of how things work, the proposal of “verifying you’re an adult” before you access adult content sounds, superficially, like a reasonable thing to do. But it’s a patently stupid idea at every level.

## Age Verification Makes The Internet Less Secure

In meatspace, if you wanted to go to the adult section of a movie store, you would need to show a clerk your government issued photo ID. They would check that your date of birth was before (current date – 18 years), and if so, they would admit you. This is the sort of experience that people who do not understand technology use to build an intuition for how laws like this operate.

**The Internet is not like meatspace.** When you supply your government ID to a website in order to verify your identity, at least two of the following security and privacy risks introduced at once:

1. The website stores your credential (whether by design or by hacker intervention).
2. The mechanism websites use to prove that the credential is authentic could track who is visiting which adult website in order to build a profile for your tastes and interests for marketing and/or blackmail purposes.
3. Your device (phone, computer, etc.) could have malware installed that pilfers whatever credential you provided in order to e.g. commit identity theft.

That’s a lot of risk for the public to take on. But what are they getting in exchange for it?

![Speechless Sticker](https://i0.wp.com/soatok.blog/wp-content/uploads/2021/04/soatok-telegrams-wave-3-commission-13.png?resize=512%2C512&ssl=1)

[CMYKat](https://cmykatgraphics.carrd.co/)

Well, a lot fewer adults will choose to share their photo ID to look at pornography, which will likely increase sexual aggression since [pornography use by adults inversely correlates with sexual assault](https://www.christopherjferguson.com/pornography.pdf) in every society science has observed.

> (…) the increasing availability of pornography appears to be associated with a decline in rape.

Part of this is deliberate: The anti-porn lobby is largely christofascists and they’re all following the same playbook as the authors of [Project 2025](https://www.project2025.observer/). Y’know, the same clowns that [want to ban sex education](https://msmagazine.com/2024/09/25/florida-ban-sex-ed-schools-project-2025-porn-ban/).

![Soatok grabbing his computer angrily.](https://i0.wp.com/soatok.blog/wp-content/uploads/2024/08/SoatokNerdRage.png?resize=512%2C376&ssl=1)

Art by [AJ](https://bsky.app/profile/ajlovesdinos.bsky.social)

The Christian nationalists behind these movements [also want](https://www.them.us/story/trans-rights-ioda-porn-ban-bill-mike-lee-project-2025) to classify all forms of queer expression as sexual, [and therefore pornographic](https://www.msnbc.com/opinion/msnbc-opinion/project-2025-porn-ban-lgbtq-transgender-rcna161562), to force us back into the closet (lest we be prosecuted as sexual predators for daring to be visibly queer “in front of children”).

Transgender people are at the top of their target list, but make no mistake, they hate cisgender gay and lesbian Americans just as much.

Sometimes what can be explained by stupidity is better explained with malice. This is doubly so with right-wing politics. [The cruelty is the point](https://www.theatlantic.com/ideas/archive/2018/10/the-cruelty-is-the-point/572104/).

This is not a uniquely American problem: Puritanical attitudes towards sex have penetrated every society. The [UK’s Online Safety Act](https://www.politico.com/newsletters/digital-future-daily/2025/07/29/the-uks-new-tech-law-triggers-upheaval-00481803) aims to accomplish the same end goals as the fascists across the pond. The recent ban waves of adult content on Steam and itch.io were caused by an Australian “feminist” group that used [extralegal pressure through payment processors to achieve their goals](https://soatok.blog/2025/07/24/against-the-censorship-of-adult-content-by-payment-processors/).

Needless to say, the attempts to control adult content have been a complete clusterfuck.

## Protecting User Privacy

If it wasn’t clear already, the anti-porn laws are stupid, wrong, and harmful. You should absolutely call your representatives and get these stupid laws overturned if you live in an affected jurisdiction.

But they are, nonetheless, the law in those jurisdictions.

Until they can be repealed by a more competent electorate, we have to operate on the assumption that “age verification” will be a stupid thing we have to live with.

To that end, cryptography actually provides us with an interesting tool for limiting the risks of age verification. They’re called **zero-knowledge proofs**.

### Clueless About Zero-Knowledge Proofs

I will not mince words: zero-knowledge proofs straddle the line between genius and madness.

Sure, you can grok the basic idea of them pretty easily: You can prove that you have knowledge without revealing *what that knowledge is*. There have been lots of YouTube videos that explain this pretty intuitively. Here’s one from Numberphile:

But then you get into the art of turning interactive proofs (as described in the video) into non-interactive proofs. This usually involves a Fiat-Shamir transform, [which comes with many subtle footguns](https://blog.trailofbits.com/2024/06/24/disarming-fiat-shamir-footguns/).

The most basic kind of non-interactive proof you’re likely to run into in the real world is an Schnorr proof–which is the basis for Ed25519 signatures. The signatures are succinct proofs of knowledge of a particular secret number (the private key).

But then you have the madness: Algebraic circuits, polynomial commitments, trusted setups versus recursive proofs, **motherfucking [zero-knowledge VMs](https://github.com/scroll-tech/zkvm-prover)**!

If you stare at [the introductory material for zero-knowledge proofs](https://rdi.berkeley.edu/zk-learning/) for long enough, you will come to appreciate Plato’s account of Socrates in a new light.

> I am the wisest man alive, for I know one thing, and that is that I know nothing.
>
> Your brain on zero knowledge

Why am I describing zero-knowledge proofs this way? Because I want you to appreciate how much they are a departure from the simple world of “should I use AES-GCM or ChaCha20-Poly1305 here?” level cryptography protocol design that most developers find themselves in.

![Blue Screen of Death Sticker](https://i0.wp.com/soatok.blog/wp-content/uploads/2021/04/soatoktelegramswave3-10.png?resize=512%2C512&ssl=1)

[CMYKat](https://cmykatgraphics...