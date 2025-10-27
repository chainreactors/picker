---
title: How I Got $10,000 From GitHub For Bypassing Filtration oF HTML tags
url: https://infosecwriteups.com/how-i-got-10-000-from-github-for-bypassing-filtration-of-html-tags-db31173c8b37?source=rss----7b722bfd1b8d--bug_bounty
source: Bug Bounty in InfoSec Write-ups on Medium
date: 2022-10-18
fetch_date: 2025-10-03T20:06:35.269850
---

# How I Got $10,000 From GitHub For Bypassing Filtration oF HTML tags

[Sitemap](/sitemap/sitemap.xml)

[Open in app](https://rsci.app.link/?%24canonical_url=https%3A%2F%2Fmedium.com%2Fp%2Fdb31173c8b37&%7Efeature=LoOpenInAppButton&%7Echannel=ShowPostUnderCollection&%7Estage=mobileNavBar&source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fhow-i-got-10-000-from-github-for-bypassing-filtration-of-html-tags-db31173c8b37&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

[Medium Logo](https://medium.com/?source=post_page---top_nav_layout_nav-----------------------------------------)

[Write](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-story&source=---top_nav_layout_nav-----------------------new_post_topnav------------------)

[Search](https://medium.com/search?source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fhow-i-got-10-000-from-github-for-bypassing-filtration-of-html-tags-db31173c8b37&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

![](https://miro.medium.com/v2/resize:fill:64:64/1*dmbNkD5D-u45r44go_cf0g.png)

[## InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---publication_nav-7b722bfd1b8d-db31173c8b37---------------------------------------)

·

Follow publication

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:76:76/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_sidebar-7b722bfd1b8d-db31173c8b37---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow publication

# How I Got $10,000 From GitHub For Bypassing Filtration oF HTML tags

[![Saajan Bhujel](https://miro.medium.com/v2/resize:fill:64:64/1*d7sPwJn8zoJsEhtPcvIdfQ.jpeg)](https://saajanbhujel.medium.com/?source=post_page---byline--db31173c8b37---------------------------------------)

[Saajan Bhujel](https://saajanbhujel.medium.com/?source=post_page---byline--db31173c8b37---------------------------------------)

8 min read

·

Oct 16, 2022

--

11

Listen

Share

Hey everyone👋

I hope you’re having an A+ week🚀!

In today’s blog, I am going to tell you that, “*How I Got $10,000 From GitHub For Bypassing A Filtration oF HTML tags*”

Press enter or click to view image in full size

![]()

A few months back, One day I was just scrolling the Twitter feed. And, Suddenly a tweet from [@github](https://twitter.com/github) came into my focus. Basically, The Tweet was regarding GitHub’s new feature that gives the ability to render or display Mathematical expressions(TeX and LaTeX style syntax) in Markdown through the [**MathJax**](https://www.mathjax.org)library.

### What is [**MathJax**](https://www.mathjax.org)?

MathJax is an open-source JavaScript display engine for LaTeX, MathML, and AsciiMath notation that works in all modern browsers, with built-in support for assistive technology like screen readers.

After reading the tweet, I got to know that, “*GitHub is now using MathJax library to display Mathematical expressions in Markdown files*”. So, The first thing I tried was to find any previous or known bugs in the [**MathJax**](https://www.mathjax.org)library. And mainly, I was looking to find any previous XSS or HTML injection CVEs.

Luckily, **I found the known XSS issue in the MathJax library which affects versions <*2.7.4*** *.* And, The Payload should be in a Unicode form to work.

> \unicode{}

Press enter or click to view image in full size

![]()

Known CVE in a MathJax library which affects versions <2.7.4

Then, I created a markdown file in my test repository. And, I started my testing. So, I entered 👇 this payload in a file:

> Payload:- `$$\\u003cu\u003eHello\u003c/u\u003e{}$$` or `$$\\u003cu\u003eWhy\u003c\uffofu\u003e{}$$` , etc.
>
> *\**Note:`$$...$$` *are math delimiters.*

But, Nothing worked for me. And, I knew the reason is that “*The CVE was only vulnerable for version <2.7.4 meanwhile the GitHub is using a newer version*”.

Thus, I thought that “*I had to find a bypass by myself to successfully exploit the attack and* *If somehow I am able to render basic HTML tags like:* `<b>,<i>,<u>`*.*” And, You may be wondering why I said only **basic HTML tags**? Coz, Most of the time websites use WAFs, different kinds of filters, and restrictions to prevent the use of **advanced tags** but they don’t do the same thing for basic and common tags. That’s why I said!.

And once I found a bypass or way to render **basic tags using math expressions**. Then only in this situation, “***I will try to escalate the impact by trying advanced tags***”.

### The First way or method of exploiting:

So, The first thing I did “*was to find any interesting behavior which can be very useful for me to render basic tags using math expressions*”. For this, I tried different-different types of methods(like Unicode, URL encoding, and etc). And again, This also does not work for me.

But, Somehow I was able to find a way that is very helpful for rendering the basic tags using math expressions. I **noticed** that “***when I used basic tags after the*** `\` ***then only that time the tag gets render*** *without any error or without being filtered*”.And, The payload is `$$\<u>HELLO</u>{}$$`

So, I quickly replaced the `<u>` tag with other advance tags(like <script>,<iframe>, <style>) in order to know “*Is the website using more filters to prevent the use of the advance tags?*”. The answer is ***Yessss***, The GitHub markdown files are using some more filters in which “***they simply filtered any advance tags except*** `<style>` ***tags***”.

Then after testing this mathjax integration, I found that it’s possible to add `<style>` tags on using a backslash(`\`) before it (like: `\<style>{property:value}</style>`). So for customizing the CSS, I used these below **payloads** in my `test.md` files:

```
$$\<style>*{display:none}</style>{}$$$$\<style>div{background-color:#66f3e6}</style>{}$$$$\<style>*{font-size:23px;}</style>{}$$$$\<style>body{padding: 50px;background-color: #4b6bb7;}</style>{}$$
```

Hence, I noticed that now I am able to change the CSS of the whole page.

Press enter or click to view image in full size

![]()

Able to change the CSS of the page using this method

And, I created and submitted my first report to GitHub’s HackerOne program. But, You know what happens with my report “***Report closed within 5 mins by bot*** *saying that it is a previously identified issue and is being tracked internally*”. For the minutes, I was so confused and thought that “*The bot is really a bot or a human is behind the bot*”.

So, I asked the program, “*Is this quick response coming from the BOT or from a real person?*”. Then, GitHub’s traiger confirmed and replied, “*Yes, please rest assured that your report was reviewed by a real person. Thanks for checking in on my humanity!*”

All I can say is that “*My first ever bug report to GitHub closed as Duplicate*”.

### The second way or method of exploiting:

GitHub fixed the issue within 24 hours.

So, I thought to retest the issue with my previous method and payloads. And, I found that “*I was no more able to use advance tags with previous method and payloads*”.

And somehow, I managed to find a new way to render tags. But this time, I was only able to use normal tags(like: *<div>,<span>,<section>,<input>,<label>,<button>*) not “<*style*> and <*script*>” in the math expressions.

```
$$<div>Test</div>{}$$$$<input type=text>{}$$$$<button>Click Here</button>{}$$
```

Although, We can also use a few ta...