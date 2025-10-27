---
title: How You Respond to Security Researchers Says Everything About You
url: https://soatok.blog/2023/01/21/how-you-respond-to-security-researchers-says-everything-about-you/
source: Dhole Moments
date: 2023-01-22
fetch_date: 2025-10-04T04:33:33.140711
---

# How You Respond to Security Researchers Says Everything About You

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

[Security Community](https://soatok.blog/category/technology/software-security/security-community/)

# How You Respond to Security Researchers Says Everything About You

Tails from the Cryptographic Side of Security Research

* Post author

  By [Soatok](https://soatok.blog/author/soatok/)
* Post date

  [January 21, 2023](https://soatok.blog/2023/01/21/how-you-respond-to-security-researchers-says-everything-about-you/)
* [5 Comments on How You Respond to Security Researchers Says Everything About You](https://soatok.blog/2023/01/21/how-you-respond-to-security-researchers-says-everything-about-you/#comments)

![How You Respond to Security Researchers Says Everything About You](https://i0.wp.com/soatok.blog/wp-content/uploads/2023/01/BlogHeader-2023-ResponseToSecurityResearchers.png?fit=1200%2C675&ssl=1)

Whether businesses thrive or shutter depends largely on *trust*. This is as true of restaurants and fursuit makers as it is of password managers and private messaging apps.

Trust is hard to gain, but easy to lose. Mathematics would therefore indicate that the products and services that the most nervous people trust would be exceptionally rare; perhaps nonexistent.

However, trust is also a very social phenomenon. Society depends on trust relationships to remain functional. At some point, you have to stop scrutinizing in order to get anything done, and that means saying, e.g., “Okay, I’ll trust AMD not to ship a targeted backdoor to the CPU going into the computer I use to draw furry art on.”

Where the trust dynamics get interesting is when you introduce **security researchers** into the mix. Security researchers include hackers, code-breakers, hobbyists, engineers, and many other types of professionals that generally have one common goal in mind:

To identify vulnerabilities that could hurt users.

![](https://i0.wp.com/soatok.blog/wp-content/uploads/2020/04/soatok_stickerpack-hacker.png?resize=512%2C512&ssl=1)

by [CMYKat](https://cmykatgraphics.carrd.co/)

Security researchers generally have no ethical obligation to protect the vendor or the vendor’s reputation; only their users or customers. A naïve person might conclude that security researchers are a wild card, in that light.

Most security researchers, however, value their professional relationships and the community they work in, and generally don’t want unnecessary conflicts in their life.

Why am I stating all this? Because I firmly believe that **the best lens through which to judge a company’s culture is to examine how they respond to security researchers**.

I’d like to talk about some of my experiences with this topic, as well as recent events in the security community.

![Grin Sticker](https://i0.wp.com/soatok.blog/wp-content/uploads/2021/03/soatoktelegramswave3-01.png?resize=512%2C512&ssl=1)

Credit: [CMYKat](https://cmykatgraphics.carrd.co/)

## A Tale Of Two Password Managers

In 2022, I decided to assess the security of several password managers in order to make a recommendation for my friends’ new business. Two of these password managers had bounty programs on Bugcrowd (which, at the time, was [not prepared to handle cryptographic bug reports](https://soatok.blog/2022/06/14/when-soatok-used-bugcrowd/)).

Before I dive into these details, it’s probably worth reading [my recent post about password-based cryptography](https://soatok.blog/2022/12/29/what-we-do-in-the-etc-shadow-cryptography-with-passwords/).

### Soatok Reports Issues to 1Password

**Note:** I’ve received permission from 1Password to share the details of one of the issues I disclosed to them.

1Password has several implementations of the same protocols, so I decided to look at their Android app.

My initial process for studying Android apps is pretty boring:

1. Download the .apk file (usually from apkcombo)
2. Rename the .apk file’s extension to .zip
3. Extract the `classes.dex`, `classes2.dex`, etc. files
4. Use dex2jar to convert the class files into a Java archive
5. Use JD-GUI or Luyten to study the decompiled source code.

This isn’t sufficient for confirming vulnerabilities or developing a proof-of-concept exploit, but it’s enough to identify many cryptographic weaknesses (assuming you’re familiar enough with cryptographic software implementations to find weaknesses just from studying the source code).

![](https://i0.wp.com/soatok.blog/wp-content/uploads/2022/02/Soatok-ScruffKerfluff.png?resize=768%2C614&ssl=1)

Art: [ScruffKerfluff](https://scruffkerfluff.carrd.co/)

With 1Password, my target of interest was their SRP implementation, which in Luyten had a method looked like this at the time of my analysis:

```
public BigInteger generateVerifier(
    final byte[] array,
    final String s,
    final int n,
    final String s2,
    String lowerCase
) throws Exception {
    lowerCase = lowerCase.toLowerCase(Locale.US);
    return this.g.modPow(
        SRP6Util.computeXForPBES2g_HS256WithMethod(
            "SRPg-496",
            array,
            s,
            n,
            new AccountKey(s2),
            lowerCase
        ),
        this.N
    );
}
```

Notice the string `SRPg-496`. Later in the call-chain, it invokes a method to fetch SRP constants based on this parameter, which is implemented like so:

```
private void setSrpParams() {
	if (this.mMethod.endsWith("2048")) {
		this.N = SRPConstants.N_2048;
		this.g = SRPConstants.g_2048;
		this.expSize = 32;
	}
	else if (this.mMethod.endsWith("4096")) {
		this.N = SRPConstants.N_4096;
		this.g = SRPConstants.g_4096;
		this.expSize = 38;
	}
	else if (this.mMethod.endsWith("8192")) {
		this.N = SRPConstants.N_8192;
		this.g = SRPConstants.g_8192;
		this.expSize = 48;
	}
	else {
		this.N = SRPConstants.N_1024;
		this.g = SRPConstants.g_1024;
		this.expSize = 32;
	}
}
```

The string being passed in ends with `496`, not `4096`. This means that their SRP code was falling back to the default case, which uses 1024-bit parameters rather than the intended 4096-bit security level.

All because of what appeared to be *a typo*!

I wrote a quick report containing this observation (and explaining my understanding of the real-world risk). Within *two hours*, they responded:

> That’s a great observation! I did some quick digging into this code, and luckily (for us) this is far more of an innocent issue than it may appear at first.
>
> In SRP, the clients don’t normally compute the verifier, the server does [1](https://en.wikipedia.org/wiki/Secure_Remote_Password_protocol). That’s also the case here: the Android app in normal use doesn’t generate an SRP verifier at all. It turns out that the class you found here was used for testing purposes, and is in fact not called from any of our code at all anymore.
>
> It’s still poor hygiene on our part that that class is even there if it isn’t used at all, so we’ve started tracking an issue internally to get class out of there. Thanks for digging into our code to find this though!
>
> Rick from 1Password

I went on to discover a few more bugs in other 1Password codebases, but I haven’t been given permission to disclose those yet.

However, I can say they consistently had quick, professional, informed, and friendly responses to my reports. They were a delight to report security issues to.

![Drakeposting Yes Sticker](https://i0.wp.com/soatok.blog/wp-content/uploads/2021/04/soatoktelegramswave3-08.png?resize=512%2C512&ssl=1)

[CMYKat](https://cmykatgraphics.carrd.co/)

### Soatok Reports Issues to LastPass

**Note:** I cannot talk about what I found a...