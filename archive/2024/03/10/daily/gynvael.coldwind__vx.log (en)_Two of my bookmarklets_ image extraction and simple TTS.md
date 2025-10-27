---
title: Two of my bookmarklets: image extraction and simple TTS
url: https://gynvael.coldwind.pl/?id=781
source: gynvael.coldwind//vx.log (en)
date: 2024-03-10
fetch_date: 2025-10-04T12:08:17.707205
---

# Two of my bookmarklets: image extraction and simple TTS

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

2024-03-09:

## [Two of my bookmarklets: image extraction and simple TTS](?id=781)

javascript

A somewhat ancient yet pretty cool feature of web browsers are the [bookmarklets](https://en.wikipedia.org/wiki/Bookmarklet). These are literally just javascript: code snippets saved as bookmarks – they are like the older and less capable siblings of typical browser extensions and are limited to being run when clicked and only in the context of the page you're currently looking at. Anyway, since I use two such bookmarklets pretty reguraly, I decided to share them with you.

Note that both bookmarklets, as well as any updates to them, are available [on my GitHub in the random-stuff repository](https://github.com/gynvael/random-stuff/tree/master/bookmarklets).

P.S. If you decide to explore other bookmarklets out there, remember that random bookmarklet found on the internet may contain malicious code. In such case executing it might leak the page you're looking at, leak authentication information (session cookies), or even give an attacker interactive control over the page in said tab (which allows them to change settings, and at times e-mails or even the account password). So if you can't security-review a bookmarklet, popular extensions in good standing are a safer choice.

### Image extraction

This one is useful is you're dealing with a website which displays images in a weird way that makes it harder to use features like *Save image as...* or *Copy image link*. It basically goes through the DOM and finds every <img> tag and notes the URL to the image, as well as every other tag and notes the url(...) in background-image CSS style (if any). And then it re-renders the page displaying only the images and their URLs.

Minified bookmarklet form (readable form is below):

`` javascript:{const imgs = [];const re = /url\([ \t]*['"`]\x3f([^\)'"`]+)['"`]\x3f[ \t]*\)/;const fnc = function(parent) { Array.from(parent.children).forEach(child => { if (child.tagName === 'IMG') { imgs.push(child.src); } const bg = child.style.backgroundImage; if (bg && bg.toLowerCase().includes("url(")) { const m = bg.match(re); if (m) { imgs.push(m[1]); } else { console.warn("Failed to extract image URL from:", bg); } } fnc(child); });};fnc(document.body);document.body.innerHTML = "";imgs.forEach(img => { const div = document.createElement("DIV"); const p = document.createElement("P"); const a = document.createElement("A"); a.href = img; a.innerText = img; p.appendChild(a); div.appendChild(p); const el = new Image(); el.src = img; div.appendChild(el); document.body.appendChild(div);});} ``

Readable source code:

`` const imgs = [];
const re = /url\([ \t]*['"`]\x3f([^\)'"`]+)['"`]\x3f[ \t]*\)/;
const fnc = function(parent) {
Array.from(parent.children).forEach(child => {
if (child.tagName === 'IMG') {
imgs.push(child.src);
}
const bg = child.style.backgroundImage;
if (bg && bg.toLowerCase().includes("url(")) {
const m = bg.match(re);
if (m) {
imgs.push(m[1]);
} else {
console.warn("Failed to extract image URL from:", bg);
}
}
fnc(child);
});
};
fnc(document.body);
document.body.innerHTML = "";
imgs.forEach(img => {
const div = document.createElement("DIV");
const p = document.createElement("P");
const a = document.createElement("A");
a.href = img;
a.innerText = img;
p.appendChild(a);
div.appendChild(p);
const el = new Image();
el.src = img;
div.appendChild(el);
document.body.appendChild(div);
}); ``

**By the way...**
If want to improve your binary file and protocol skills, check out the workshop I'll be running between April and June → [Mastering Binary Files and Protocols: The Complete Journey](https://hackarcana.com/workshop-session/2025-Q1-Q1-mastering-binary/buy?utm=gyn-blog-inad)

### Poor man's text-to-speech

This is something I use if I want the browser to read me a paragraph or two of the text on a website. Initially I thought I would just use an existing extension for this, but then I remembered that browsers actually have text-to-speech built in in form or the [SpeechSynthesis API](https://developer.mozilla.org/en-US/docs/Web/API/SpeechSynthesis) (window.speechSynthesis and friends), so I decided to make a quick one-liner instead. Of course it turned out that in Chrome on Linux only around 200 characters I've read, so I had to add some code (part of which was ChatGPT generated) which creates a list of "sentences" – i.e. words reformated to make 200-or-less character fragments.

**By the way...**
If want to improve your binary file and protocol skills, check out the workshop I'll be running between April and June → [Mastering Binary Files and Protocols: The Complete ...