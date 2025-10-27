---
title: Vulnerabilities in the hidden magic of Lodash, Ramda and Underscore
url: https://positive.security/blog/lodash-ramda-underscore-vulnerabilities
source: Over Security - Cybersecurity news aggregator
date: 2025-05-08
fetch_date: 2025-10-06T22:29:30.041007
---

# Vulnerabilities in the hidden magic of Lodash, Ramda and Underscore

![](https://cdn.prod.website-files.com/5f6498c074436c50c016e745/5f6498c074436cf0ef16e7ad_menu_icon_flipped.png)

[HOME](/)[About](/about)[Services](/services)[Blog](/blog)[Contact](/contact)

[![](https://cdn.prod.website-files.com/5f6498c074436c50c016e745/5f6498c074436c270016e798_purple.png)](/)

# Vulnerabilities in the hidden magic of Lodash, Ramda and Underscore

May 7, 2025

ByÂ

Lukas Euler

![](https://cdn.prod.website-files.com/5f6498c074436c349716e747/67dd3fd15ecbc9ef6670384d_lodash_ramda_underscore_vulns_title_image.png)

-- MARKDOWN --

- Internals of JavaScript/TypeScript's most popular utility libraries can be attacked with special attributes of processed user-supplied objects, such as `\_\_wrapped\_\_`, `@@functional/placeholder` or `length`
- Exploitability is dependent on how the libraries are used, i.e. which function parameters are filled with user-supplied and potentially malicious values
- We show DoS (high probability of vulnerable code patterns), control flow manipulation (medium probability) and RCE (highly unlikely to occur organically, but could be abused to obscure backdoors)
- The findings paired with mitigation suggestions were privately disclosed to the library maintainers first; Lodash did not respond, Ramda and Underscore decided not to implement any fixes, stating that developers must take care of sanitization instead
- This post gives an introduction to the affected internal processes, showcases some of the potentially vulnerable code patterns including possible exploits and provides pointers to enable developers to safeguard against these issues

# Table of contents
- [Introduction](#introduction)
- [Lodash](#lodash)
Â Â Â Â - [Special attributes](#lodash-special-attributes)
Â Â Â Â - [DoS](#lodash-dos-lodash)
Â Â Â Â - [Control flow manipulation](#lodash-control-flow-manipulation)
Â Â Â Â - [RCE](#lodash-rce)
Â Â Â Â - [Bonus RCE](#lodash-bonus-rce)
Â Â Â Â - [How to prevent vulnerabilities](#how-to-prevent-vulnerabilities-in-lodash)
- [Ramda](#ramda)
Â Â Â Â - [Special attributes](#ramda-special-attributes)
Â Â Â Â - [DoS](#ramda-dos)
Â Â Â Â - [Control flow manipulation](#ramda-control-flow-manipulation)
Â Â Â Â - [RCE](#ramda-rce)
Â Â Â Â - [How to prevent vulnerabilities](#how-to-prevent-vulnerabilities-in-ramda)
- [Underscore](#underscore)
Â Â Â Â - [Special attributes](#underscore-special-attributes)
Â Â Â Â - [DoS](#underscore-dos)
Â Â Â Â - [How to prevent vulnerabilities](#how-to-prevent-vulnerabilities-in-underscore)
- [Conclusion](#conclusion)
- [Timeline](#timeline)

# Introduction
Utility libraries provide well tested implementations for functions and procedures commonly required or desired in software development.
The three libraries discussed in this post all saw their initial releases more than 10 years ago in a time when support for even the most basic functional programming primitives such as `Array.forEach` and `Array.map` was not yet widely available in vanilla JavaScript.
In the last decade and a half, JavaScript and TypeScript have also established themselves as popular languages for backend applications which must process large amounts of untrusted user inputs. This has opened up attack vectors to the internals of these libraries which may not have been considered during their inception.
The potential impact of exploiting the vulnerabilities described here also vastly depends on the context:

- For any application that does not process untrusted data submitted by other users, no negative impact should be expected
- Web frontends that display or process untrusted data could crash the victim's browser or suffer from XSS
- In case of a NodeJS web application backend however, these vulnerabilities could be abused to crash a server, bypass authorization checks or fully compromise the server with all of its data

As mentioned in the TL;DR, the XSS/RCE case is very unlikely to occur naturally.

This post is meant to educate and potentially give basis for a civilized discussion.
We strongly disapprove of angry and entitled behavior towards anyone contributing time or resources to FOSS in good faith.

\*\*Interactive challenges/demos\*\*
- This page embeds interactive sandboxed JavaScript playgrounds for each of the issues we describe which are best viewed on a large format screen
- Each playground is pre-populated with a non-malicious user input in JSON format and a vulnerable code snippet from a ficticious application relying on a specific utility library
- The examples can be used as little hacking challenges where only the `userInput` textarea should be used to input a JSON payload that achieves the goal
- The more difficult challenges are quite convoluted and not intended to be solved casually while reading
- \*\*Feel free to skip the challenges and instead transform them into demos by clicking the blue "Fill Solution" button\*\*. This will overwrite the `userInput` textarea to contain an example malicious payload that solves the challenge.

# Lodash
## Lodash special attributes
Many of Lodash's functions can be accessed in two different ways:
1. Accessing an attribute of the global `\_` object and passing all inputs as arguments: `\_.isEqual(1, 1)`
2. Passing an input as an argument to the `\_` function to create a `LodashWrapper`, and calling an attribute of the wrapper with another input as argument: `\_(1).isEqual(1)`
Instances of `LodashWrapper` store the wrapped inputs and other state data in various special attributes. Special attribute values that are already present in the original input to the `\_` function are kept and used.
Note that Lodash comes in [different build varieties](https://github.com/lodash/lodash/wiki/build-differences) ("full", "core", "strict" and "custom" builds), which include different subsets of the functions available in the Lodash code base as well as differing in how some internals are implemented. The behavior of keeping special attribute values from input objects and many of the examples below will only work in the more commonly used ["full" build with usually 50M+ weekly downloads on npm](https://www.npmjs.com/package/lodash)

\*\*LodashWrapper\*\*

- `\_\_wrapped\_\_`: The wrapped value, i.e. the original input argument to the `\_` function
- `\_\_actions\_\_`: An array of function references and arguments to be applied to the `\_\_wrapped\_\_` value when `.value()` is called
- `\_\_chain\_\_`: If this is set to `true`, any function call on the wrapper object other than `.value()` will push data to the `\_\_actions\_\_` array instead of executing immediately
- `\_\_index\_\_`: Keeps track of the current index when iterating via `.next()`
- `\_\_values\_\_`: Array used for iterating via `.next()`
- `\_\_dir\_\_`: Integer (-1|1) defines the direction from which to apply the `.drop()` and `.take()` methods

\*\*LazyWrapper\*\*
Extension of `LodashWrapper` which can defer more array operations
- `\_\_filtered\_\_`: Boolean affecting how other attributes related to array operations are treated
- `\_\_iteratees\_\_`: List of function references buffering `.filter()`, `.map()` and `.takeWhile()` operations
- `\_\_takeCount\_\_`: Integer affecting `.drop()` and `.take()` methods
- `\_\_views\_\_`: Alternative list of objects buffering `.drop()` and `.take()` operations

\*\*Other\*\*
- `length`: Standard JS attribute accessed by collection processing functions when the expected input is an Array-like object
- `\_\_lodash\_hash\_undefined\_\_`: Special value used to stand-in for `undefined` hash values
- `\_\_lodash\_placeholder\_\_`: Special value used as an argument placeholder for function wrapping (e.g. via `\_.bind`)

##Â Lodash DoS
\*\*Abusing `length` property\*\*

Several methods in the library assume a given value is an array and perform actions based on its `length` property, if the `length` value is a Number from `0` to `Number.MAX\_SAFE\_INTEGER`. The [upper limit](https://content.positive.security/code\_playground/libs/lodash-4.17.21.js.html#islength) li...