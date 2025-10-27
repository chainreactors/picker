---
title: LLM + Clean Room: Will LLMs be the death of code copyrights?
url: https://gynvael.coldwind.pl/?id=764
source: gynvael.coldwind//vx.log (en)
date: 2023-03-20
fetch_date: 2025-10-04T10:04:25.053784
---

# LLM + Clean Room: Will LLMs be the death of code copyrights?

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

2023-03-19:

## [LLM + Clean Room: Will LLMs be the death of code copyrights?](?id=764)

llm

**Disclaimer: I am not a lawyer. Furthermore, remember that laws differ between countries.**

Let me preface this post by saying that I don't have answers – I have only (interesting) questions. And perhaps the answer to the question in the headline eventually will follow [Betteridge's law of headlines](https://en.wikipedia.org/wiki/Betteridge%27s_law_of_headlines) anyway.

So what is all this about?

In reverse-engineering there is a concept called [clean room design](https://en.wikipedia.org/wiki/Clean_room_design). In short, it's a method of "copying" (and I'm using this term *very* loosely) someone's implementation of an idea without infringing on their copyrights. And while the term is a bit more generic, I will focus on it's application to software (code). In short, the method boils down to 3 steps:

1. Reverse-engineers analyze the source software and prepare detailed documentation about how things look like and how they are done.
2. Lawyers review the documentation to make sure no piece of code was included (or more generally: no copyrightable items were included).
3. Software engineers implement a new piece of software based on this documentation.

The idea behind clean room design is that while code is copyrightable, algorithms and ideas generally are not. Therefore, while directly copying code is basically illegal in many countries, describing the idea and re-implementing it by someone who never saw the original code seems to be legally fine. Note that this method does nothing about software patents – this is only about "bypassing" copyrights.

All in all this method is quite expensive – neither lawyers, nor reverse-engineers, nor software engineers are cheap.

**And this is where Large Language Models (LLMs) come in.**

The recently released GPT-4 is surprisingly decent both in source code analysis and documentation-based implementation. Sure, it makes a lot of mistakes, but we can assume improved models will appear in the next 5-10 years (including specialized models for exactly this job), so for the sake of the discussion let's assume LLMs eventually will be pretty decent in both tasks. Now, let's augment the clean room design process with LLMs. Here's what we arrive at:

1. Code is fed to LLM asking it to describe what it does without quoting the code.
2. Maybe lawyers review the generated documentation? Or maybe LLM does this too?
3. Generated description is fed to LLM asking it to generate code based on it.

**The outcome is basically the same at a fraction of the cost.**

Furthermore this can be heavily automatized, in the edge case having the form of tool that can be run on a given directory: ./llm-clean-room ./product.

Consequences of cheap and automated clean room design in case of software are hard to predict, but here are some guesses:

* A large corporation might decide it's a more viable strategy to "clone" a piece of software than to comply with e.g. the *highly restrictive viral* open-source [AGPL license](https://en.wikipedia.org/wiki/GNU_Affero_General_Public_License).
* A competitor might "clone" a piece of software from the another company for the fraction of the initial development cost.
* There might be a large shift to SaaS model as a defense tactic, as copyright on code would effectively be ineffective.
* EULAs might start to include clauses disallowing the product to be fed into LLMs for any reason (though I doubt this would be effective at all).
* On the flip side, it might also mean longer life for some orphaned / deprecated products.

So far I did omit a few elephants in the room, so let's point them out:

* First of all there is no consensus about the ownership of the outputted code. Yes, we have the case of the [US Copyright Office leaning towards not granting copyrights for AI generated art](https://www.theverge.com/2022/2/21/22944335/us-copyright-office-reject-ai-generated-art-recent-entrance-to-paradise), however as of now this has not been tested in case of code unless I'm mistaking.
* Second of all, the generated code itself might be based on the source material LLM was taught on, therefore potentially infringing copyrights of original authors. See for example the [GitHub Copilot lawsuit](https://githubcopilotlitigation.com/).
* "Cloning" a project like this is of course only one thing. Debugging it until it works and further maintenance and development is another issue.
* I shudder just thinking about all the security issues introduced in this "cloning" process.

To summarize, we do live in interesting ti...