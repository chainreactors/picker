---
title: A successful prototype pollution chained to a DOM XSS
url: https://infosecwriteups.com/a-successful-prototype-pollution-chained-to-a-dom-xss-9887087b56a4?source=rss----7b722bfd1b8d--bug_bounty
source: Bug Bounty in InfoSec Write-ups on Medium
date: 2023-04-22
fetch_date: 2025-10-04T11:33:17.042181
---

# A successful prototype pollution chained to a DOM XSS

[Sitemap](/sitemap/sitemap.xml)

[Open in app](https://rsci.app.link/?%24canonical_url=https%3A%2F%2Fmedium.com%2Fp%2F9887087b56a4&%7Efeature=LoOpenInAppButton&%7Echannel=ShowPostUnderCollection&%7Estage=mobileNavBar&source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fa-successful-prototype-pollution-chained-to-a-dom-xss-9887087b56a4&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

[Medium Logo](https://medium.com/?source=post_page---top_nav_layout_nav-----------------------------------------)

[Write](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-story&source=---top_nav_layout_nav-----------------------new_post_topnav------------------)

[Search](https://medium.com/search?source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fa-successful-prototype-pollution-chained-to-a-dom-xss-9887087b56a4&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

![](https://miro.medium.com/v2/resize:fill:64:64/1*dmbNkD5D-u45r44go_cf0g.png)

[## InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---publication_nav-7b722bfd1b8d-9887087b56a4---------------------------------------)

·

Follow publication

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:76:76/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_sidebar-7b722bfd1b8d-9887087b56a4---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow publication

# A successful prototype pollution chained to a DOM XSS

[![Rachid.A](https://miro.medium.com/v2/resize:fill:64:64/1*ozPqF_1nHwMgPECyOySdDA.png)](https://medium.com/%40zhero_?source=post_page---byline--9887087b56a4---------------------------------------)

[Rachid.A](https://medium.com/%40zhero_?source=post_page---byline--9887087b56a4---------------------------------------)

7 min read

·

Apr 10, 2023

--

4

Listen

Share

Press enter or click to view image in full size

![]()

Source: somewhere on Twitter

I recently found a vulnerability that is a little less common and quite interesting in how it works.

Today I decided to share with you my last little discovery and to explain a little more in detail how **prototype pollution** work.

## What is prototype pollution?

> Definition from **PortSwigger** : Prototype pollution is a JavaScript vulnerability that enables an attacker to add arbitrary properties to global object prototypes, which may then be inherited by user-defined objects. Although prototype pollution is often unexploitable as a standalone vulnerability, it lets an attacker control properties of objects that would otherwise be inaccessible. If the application subsequently handles an attacker-controlled property in an unsafe way, this can potentially be chained with other vulnerabilities.

Press enter or click to view image in full size

![]()

Source: PortSwigger

Therefore, we understand that prototype pollution is not -really- usable as such but **needs to be chained** to be. Before going into little more detail, it is necessary to briefly recall some basic JavaScript notions to understand how this vulnerability works.

## Almost everything is an object in JS

An object — in JavaScript — is a **collection of key-value pairs** whose values can be of different types (string, number, boolean..). The — minimalist — syntax of an object is as follows :

```
let myObject = {
 prop1: "A simple string",
 prop2: 100,
 prop3: true
}
```

There are **two ways to access these different properties**, the first is to use *dot notation* :

```
myObject.prop1   // -> will return "A simple string"
```

The second uses *bracket notation* :

```
myObject['prop2']   // -> will return 100
```

As we will see a little later, we will use one of these two syntaxes to **pollute the prototype**. Remember for the moment that **almost everything in JS is an object** and that each object is *linked* to another object — parent — called **prototype** from which **it inherits the methods and properties**.

## Object-oriented paradigm

Javascript is a multi-paradigm programming language that includes functional, **object-oriented**, procedural, and prototype programming. In our case, it’s the object-oriented side that we’ll be interested in, **it’s a pattern of programming** — which, as the name suggests — uses objects and consists of classes objects, and **prototypes**.

We are not going to develop this vast subject here, but only seek to understand how inheritance and prototyping work in JS.

As explained on *PortSwigger*, whenever you reference a property of an object, *the JavaScript engine first tries to access this directly on the object itself. If the object doesn’t have a matching property, the JavaScript engine looks for it on the object’s prototype instead*.
-> What is meant here by “object’s prototype” is the **parent** object.

When you create a new object, **JavaScript automatically assigns it to one of its built-in prototypes depending on the type of the newly created object** :

![]()

The type of my object here is a **string**. When I try to access a property of my object via **dot notation**, the browser offers me -as we can see in the picture above- a whole bunch of methods/properties that I never created : *toLowerCase*, *toUpperCase* (…).
This is normal, **JavaScript automatically assigned my object to the prototype String**, so *myObject* **inherited** all its properties and methods.

**It is possible to see what the prototype of an object is** using the following syntax (*on most browsers*) :

Press enter or click to view image in full size

![]()

The syntax for accessing a property is the same as for any object as seen previously. The **String** **prototype itself inherits from another prototype**, **which itself inherits from another prototype**, it is possible to move up the chain by simply chaining like this :

```
myObject.__proto__.__proto__.__proto__
```

The important point here is that this syntax serves as a “**getter**” and a “**setter**” at the same time: **it allows access to properties but also to modify them.**

So what if an attacker **could modify a prototype’s property** by overwriting the value of an existing property used in the application with another value? He would “**pollute**” **the prototype**!
But as previously explained this *would not* make it an immediately exploitable vulnerability.

## Recipe for a successful pollution prototype

We will content ourselves here with a passage taken from *PortSwigger*, simple, concise, and explicit:

> *Prototype pollution vulnerabilities typically* ***arise when a JavaScript function recursively merges an object containing user-controllable properties into an existing object****,* ***without first sanitizing the keys****.*
>
> *Successful exploitation of prototype pollution requires the following key components:*
>
> *-* ***A prototype pollution source*** *— This is any input that enables you to poison prototype objects with arbitrary properties.
>
> -* ***A sink*** *— In other words, a JavaScript function or DOM element that enables arbitrary code execution.
>
> -* ***An exploitable gadget*** *— This is any property that is passed into a sink without proper filtering or sanitization.*
>
> *Source:* PortSwigger

## Real case with my find

Now let’s move on to a **real case** with my find. As the program **is private**, I will voluntarily change some details.

By doing my re...