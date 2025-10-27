---
title: Implementing Tic Tac Toe with 170mb of HTML - no JS or CSS
url: https://portswigger.net/blog/tic-tac-toe-in-html
source: PortSwigger Blog
date: 2023-07-22
fetch_date: 2025-10-04T11:54:46.529567
---

# Implementing Tic Tac Toe with 170mb of HTML - no JS or CSS

[**Your agentic AI partner in Burp Suite - Discover Burp AI now**

**Read more**](https://portswigger.net/burp/ai)

[Login](/users)

[ ]

Products

Solutions

[Research](/research)
[Academy](/web-security)

Support

Company

[Customers](/customers)
[About](/about)
[Blog](/blog)
[Careers](/careers)
[Legal](/legal)
[Contact](/contact)
[Resellers](/support/reseller-faqs)

[My account](/users/youraccount)
[Customers](/customers)
[About](/about)
[Blog](/blog)
[Careers](/careers)
[Legal](/legal)
[Contact](/contact)
[Resellers](/support/reseller-faqs)

[![Burp Suite DAST](/content/images/svg/icons/enterprise.svg)
**Burp Suite DAST**
The enterprise-enabled dynamic web vulnerability scanner.](/burp/enterprise)
[![Burp Suite Professional](/content/images/svg/icons/professional.svg)
**Burp Suite Professional**
The world's #1 web penetration testing toolkit.](/burp/pro)
[![Burp Suite Community Edition](/content/images/svg/icons/community.svg)
**Burp Suite Community Edition**
The best manual tools to start web security testing.](/burp/communitydownload)
[View all product editions](/burp)

[**Burp Scanner**

Burp Suite's web vulnerability scanner

![Burp Suite's web vulnerability scanner'](/mega-nav/images/burp-suite-scanner.jpg)](/burp/vulnerability-scanner)

[**Attack surface visibility**
Improve security posture, prioritize manual testing, free up time.](/solutions/attack-surface-visibility)
[**CI-driven scanning**
More proactive security - find and fix vulnerabilities earlier.](/solutions/ci-driven-scanning)
[**Application security testing**
See how our software enables the world to secure the web.](/solutions)
[**DevSecOps**
Catch critical bugs; ship more secure software, more quickly.](/solutions/devsecops)
[**Penetration testing**
Accelerate penetration testing - find more bugs, more quickly.](/solutions/penetration-testing)
[**Automated scanning**
Scale dynamic scanning. Reduce risk. Save time/money.](/solutions/automated-security-testing)
[**Bug bounty hunting**
Level up your hacking and earn more bug bounties.](/solutions/bug-bounty-hunting)
[**Compliance**
Enhance security monitoring to comply with confidence.](/solutions/compliance)

[View all solutions](/solutions)

[**Product comparison**

What's the difference between Pro and Enterprise Edition?

![Burp Suite Professional vs Burp Suite Enterprise Edition](/mega-nav/images/burp-suite.jpg)](/burp/enterprise/resources/enterprise-edition-vs-professional)

[**Support Center**
Get help and advice from our experts on all things Burp.](/support)
[**Documentation**
Tutorials and guides for Burp Suite.](/burp/documentation)
[**Get Started - Professional**
Get started with Burp Suite Professional.](/burp/documentation/desktop/getting-started)
[**Get Started - Enterprise**
Get started with Burp Suite Enterprise Edition.](/burp/documentation/enterprise/getting-started)
[**User Forum**
Get your questions answered in the User Forum.](https://forum.portswigger.net/)
[**Downloads**
Download the latest version of Burp Suite.](/burp/releases)

[Visit the Support Center](/support)

[**Downloads**

Download the latest version of Burp Suite.

![The latest version of Burp Suite software for download](/mega-nav/images/latest-burp-suite-software-download.jpg)](/burp/releases)

# Implementing Tic Tac Toe with 170mb of HTML - no JS or CSS

[ ]

Gareth Heyes |
21 July 2023 at 14:00 UTC

[CSS](/blog/css)

![Some HTML showing popovers to construct a Tic Tac Toe board](/cms/images/6f/53/39da-article-code-snippet-article.png)

I love it when Chrome releases a new feature, I especially like it when it is experimental. In this post I'm going to show you how I created Tic Tac Toe (Noughts and crosses) with HTML, using one of those experimental features. Creating the game in CSS is trivial - as I've proven when I created a
[3D first person shooter](https://garethheyes.co.uk/games/cascade-of-duty/) - so I wanted to challenge myself to create a game with just HTML.

## How it started

It all started when Chrome implemented [popovers in HTML](https://developer.chrome.com/blog/introducing-popover-api/). My first action was to test it for [XSS](/web-security/cross-site-scripting) vectors and, with the help of the XSS community, we found some pretty cool vectors that allow you to
[exploit hidden inputs and meta tags](https://portswigger.net/research/exploiting-xss-in-hidden-inputs-and-meta-tags).

You would think this is where the story ends, but that's not the case. An idea popped into my head and once it's there, my brain goes into overdrive and I'm compelled to do it. The idea went like this: if you could create a popup using pure HTML, then you have some form of state e.g. the popup is showing or not. I thought you could then use this state information to create a pure HTML game and for whatever reason, Tic Tac Toe stuck in my head. Idea now fully committed, I spent my lunch hours creating the game.

Popovers are quite simple; you use a popover attribute to define the element you want to use as a popover element, which is then hidden. Then you use a popovertarget attribute in another element, usually either an input or a button, to link to the element to show it when you click the button:

`<button popovertarget=myPopover>Show popover</button>
<div id=myPopover popover>Hello world</div>`

## The basic idea

Can you see where this is going? You could use the popups to show a Tic Tac Toe board, and then use the ids for each move. Putting this theory to the test, I did a little experiment to see if you could use multiple popups one after another and it worked! The basic idea now confirmed, I then started to write some code that would generate the permutations. At first I used tables to construct the board, and buttons for the choices:

`` for(i=1;i<10;i++) {
   html +=`<table>
   <tr>
   <td><button popovertarget="x${i}">...</button></td>
   <td><button popovertarget="x${i}">...</button></td>
   <td><button popovertarget="x${i}">...</button></td>
   </tr>
    //…
   `;
}
for(i=1;i<10;i++){
   html +=`
   <div id="x${i}" popover>
   <table>
   <tr>
   <td>${i==1?'<button>X</button>':'<button popovertarget="x${i}-o1">...</button>'}</td>
   <td>${i==2?'<button>X</button>':'<button popovertarget="x${i}-o2">...</button>'}</td>
   <td>${i==3?'<button>X</button>':'<button popovertarget="x${i}-o3">...</button>'}</td>
   </tr>
   //...
   `;
} ``

The first loop generates all of the buttons, without any choices being made. When you click on a button, it targets the popup generated by the second loop. You have to brute force all the players choices, and the second loop then generates a board that targets the next choice and so on. Traditionally "X" goes first, which is convenient because it reduces the amount of boards we need to create. Popovertarget passes every choice made by the player, for example: x1-o2-x3 means X chooses the first position, O chooses the second and X chooses the third, and so on. Nesting loops creates a lot of iterations. You can calculate this by multiplying the number of loops by nine each time, so nine to the power of the number of nested loops. For example:

`9=9
9*9=81
9*9*9=729
9*9*9*9=6561
9*9*9*9*9=59049
//...`

As you can see, the amount of iterations quickly starts to get out of hand.

## Performance problems

I continued building the game in this way however, by the time I got to the sixth or seventh permutation things started to slow down. I discovered that Chrome apparently has a limit of approximately 1023mb that can be stored in a string. However, I got round that limit by splitting it into different strings.

When I got to the later permutations, performance still tanked when rendering the HTML in the browser. I thought about this for a while and decided to abandon tables completely. Chrome was rendering over half a million nodes, so clearly using tables for this was a bad idea. I used br tags and removed the tables to resolve this issue, which got me up to the second to last loop.

Here was the biggest chal...