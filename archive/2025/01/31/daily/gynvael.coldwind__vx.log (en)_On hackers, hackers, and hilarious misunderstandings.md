---
title: On hackers, hackers, and hilarious misunderstandings
url: https://gynvael.coldwind.pl/?id=799
source: gynvael.coldwind//vx.log (en)
date: 2025-01-31
fetch_date: 2025-10-06T20:07:47.781316
---

# On hackers, hackers, and hilarious misunderstandings

# [![gynvael.coldwin//vx.log](/img/logo.gif)](/?blog=1)

![](/images/something_suspicious.png)

[Available for Consulting and Projects](https://hexarcana.ch/?utm=gyn-blog)
[hackArcana (edu+CTF)](https://hackarcana.com/?utm=gyn-blog-w)

![](/img/gynvael-close.jpg)

* [Return to dashboard ⇪](/)

### *Sections*

* **lang**: [![PL](/images/lang_pl.png)](?blog=1&lang=pl) | [![EN](/images/lang_en.png)](?blog=1&lang=en)
* **RSS**: [![RSS PL](/images/lang_pl.png)](/rss_pl.php) | [![RSS EN](/images/lang_en.png)](/rss_en.php)
* [About me](?id=50)
* [Tools](?id=182)
* [→ YT YouTube (EN)](https://youtube.com/c/GynvaelEN)
* [→ D Discord](/discord)* [→ M Mastodon](https://infosec.exchange/%40gynvael)* [→ T Twitter](https://twitter.com/gynvael)* [→ GH GitHub](https://github.com/gynvael)

        [![](/img/hA-logo.png)](https://hackarcana.com)

        [My edu+CTF site](https://hackarcana.com)

        [![](/img/hexarcana160_2.png)](https://hexarcana.ch)

        [My consulting company](https://hexarcana.ch)

        [![](/img/po_issue_5_rbanner.png)](https://pagedout.institute/)

        [Paged Out! zine](https://pagedout.institute/)

        [![](/img/ds_logo_160.jpg)](https://dragonsector.pl/)

        [Dragon Sector CTF Team](https://dragonsector.pl/)

### *Links / Blogs*

* **Security/Hacking:**
  + [j00ru's blog](https://j00ru.vexillium.org/)
  + [lcamtuf's thing](https://lcamtuf.substack.com/)
  + [pi3's blog](http://blog.pi3.com.pl/)
  + [tavis ormandy's site](https://lock.cmpxchg8b.com/)
  + [pawel golen's blog](http://wampir.mroczna-zaloga.org/)
  + [zaufana trzecia strona](http://zaufanatrzeciastrona.pl/)
  + [niebezpiecznik](https://niebezpiecznik.pl/)
  + [sekurak](https://sekurak.pl/)
* **Reverse Eng./Low-Level:**
  + [security news](https://www.secnews.pl/)
  + [rev3rsed](http://rev3rsed.blogspot.com/)
* **Programming/Code:**
  + [adam sawicki](http://asawicki.info/)

### *Posts*

* [Paged Out! prints are here, and so is #7 CFP deadline,](?id=805)
* [CONFidence 2025 is next week,](?id=804)
* [No, CTRL+D in Linux terminal doesn't send EOF signal,](?id=801)
* [New edu platform and 'Sanitization and Validation and Escaping, Oh My!' article,](?id=800)
* [On hackers, hackers, and hilarious misunderstandings,](?id=799)
* [Paged Out! #5 is out,](?id=797)
* [CVEs of SSH talk this Thursday,](?id=796)
* [Debug Log: Internet doesn't work (it was the PSU),](?id=793)
* [FAQ: The tragedy of low-level exploitation,](?id=791)
* [Solving Hx8 Teaser 2 highlight videos!,](?id=789)
* [→ see all posts on main page](/)

// copyright © Gynvael Coldwind
// design & art by Xa
// logo font (birdman regular) by utopiafonts / Dale Harris

/\* the author and owner of this blog hereby allows anyone to test the security of this blog (on HTTP level only, the server is not mine, so let's leave it alone ;>), and try to break in (including successful breaks) without any consequences of any kind (DoS attacks are an exception here) ... I'll add that I planted in some places funny photos of some kittens, there are 7 of them right now, so have fun looking for them ;> let me know if You find them all, I'll add some congratz message or sth ;> \*/

**Vulns found in blog:**
\* XSS *(pers, user-inter)* by ged\_
\* XSS *(non-pers)* by Anno & Tracerout
\* XSS *(pers)* by Anno & Tracerout
\* Blind SQLI by Sławomir Błażek
\* XSS *(pers) by* Sławomir Błażek

2025-01-30:

## [On hackers, hackers, and hilarious misunderstandings](?id=799)

op-ed

![[...] representatives of this group of hackers, commonly referred to as 'ethical hackers', though theft and home invasion have nothing to do with ethics—but well, I understand, ethical hackers, because that's what they call themselves [...] (a certain Polish MP)](/img/quote-funny.png)
"Hacker", as we in the bizz know well, carries different meanings for different people, and this can cause hilarious misunderstandings. Yesterday, the Polish TV network TVN aired the second part of an ongoing documentary about issues in NEWAG trains that were analyzed by Dragon Sector. Near the end, the documentary featured a recording from the November 2024 meeting of the Parliamentary Infrastructure Committee, which was meant to discuss the matter. During the meeting, one of the Members of Parliament [took issue](https://x.com/SzJadczak/status/1859566048590098496) with the Dragon Sector team being referred to as "hackers"—the quote above is from him (translated from Polish).

This, of course, is nothing new—just another example of someone knowing the colloquial meaning of the word but not its specialized one. This disconnect has existed for at least the past 40 years.

This raises an interesting question—should we use the word "hacker" in formal settings (court, parliamentary committees, etc.), or would we be better understood if we opted for "cybersecurity specialist" or a similar term, as we often do on LinkedIn and other professional platforms?

Or perhaps we should continue using the word "hacker," as it serves as a great litmus test for whether the person we're discussing these topics with is truly familiar with the computer security industry and its terminology. It’s an unexpected but useful canary—or perhaps a reminder—that not everyone speaks "computer."

Returning to the original quote, and on a rather amusing note—or perhaps to balance things out—multiple departments of the Polish government are actively seeking to hire individuals with the "Certified Ethical Hacker" certification. In some cases, you can even get grants to earn it! Additionally, one can find information on government websites about how Dragon Sector [was invited](https://www.bbn.gov.pl/pl/wydarzenia/6376%2CNajlepsza-druzyna-na-swiecie-w-BBN.html) to the National Security Bureau to receive a commemorative letter of congratulations and symbolic gifts after winning the 2014 CTF season.

So, do we continue advocating for our specialized meaning of the word "hacker" in official settings? Or should we revert to something more neutral instead?

Just food for thought :)

**By the way...**
If want to improve your binary file and protocol skills, check out the workshop I'll be running between April and June → [Mastering Binary Files and Protocols: The Complete Journey](https://hackarcana.com/workshop-session/2025-Q1-Q1-mastering-binary/buy?utm=gyn-blog-inad)

## Comments:

2025-01-31 22:04:54 = [4chan](http://)

{

As a well known and controversial hacker, I have to say that this word has very little meaning. The average person will always understand it as the guy in a hoodie in a cafe running the tree command. You're not going to reeducate all of society probably, so I think it's better to decide what to call yourself based on your clientbase. It's probably a question for a marketing expert rather than an IT guy though

}

## Add a comment:

|  |  |
| --- | --- |
| Nick: |  |
| URL (optional): |  |
| Math captcha: 5 ∗ 1 ＋ 5 = |  |
|  | |