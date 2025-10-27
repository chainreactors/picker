---
title: UndefinedBehaviorSanitizer’s unexpected  behavior
url: https://daniel.haxx.se/blog/2024/10/17/undefinedbehaviorsanitizers-unexpected-behavior/
source: daniel.haxx.se
date: 2024-10-18
fetch_date: 2025-10-06T18:51:48.488641
---

# UndefinedBehaviorSanitizer’s unexpected  behavior

[Skip to content](#content)

[![daniel.haxx.se](https://daniel.haxx.se/blog/wp-content/uploads/2024/11/Daniel-blog-header-colonslash-thin.jpg)](https://daniel.haxx.se/blog/)

# [daniel.haxx.se](https://daniel.haxx.se/blog/)

[Search](#search-container)

Primary Menu

* [About](https://daniel.haxx.se/blog/about/)
* [Privacy](https://daniel.haxx.se/blog/privacy-policy/)

Search for:

![](https://daniel.haxx.se/blog/wp-content/uploads/2019/04/tools-1209764_1280-672x372.jpg)

[cURL and libcurl](https://daniel.haxx.se/blog/category/floss/curl/), [Development](https://daniel.haxx.se/blog/category/development/)

# UndefinedBehaviorSanitizer’s unexpected behavior

[October 17, 2024](https://daniel.haxx.se/blog/2024/10/17/undefinedbehaviorsanitizers-unexpected-behavior/) [Daniel Stenberg](https://daniel.haxx.se/blog/author/daniel/) [3 Comments](https://daniel.haxx.se/blog/2024/10/17/undefinedbehaviorsanitizers-unexpected-behavior/#comments)

The transition from Ubuntu 22 to 24 for *ubuntu-latest* on GitHub actions started recently with [the associated version bumps](https://github.com/actions/runner-images/issues/10636) of a lot of applications. As expected.

One of the version bumps is for clang: it now uses clang 18 by default. clang 18 introduced some changes that turned out to be relevant for me and other curl developers. Yeah, surely for some others as well.

## clang and gcc

In my daily developer life I just typically use gcc for building local stuff – mostly out of old habits. I rebuild and test curl dozens of times every day. In my normal work process I use a couple of different build combinations that enable a lot of third party dependencies and I almost always build curl and libcurl with debug enabled and only statically. It is a debug-friendly setup.

Of course I also have clang installed so that I can try out building with it when I want to, and I have a large set of alternative config setups that I use when I have a particular reason to check or debug such a build.

## CI to the rescue

There are literally many millions of build combinations of curl, and we do some of the most important ones automatically for every pull request and commit in the source repository. They help us avoid regressions. Currently we do almost two hundred different jobs.

Two of those CI jobs build curl using clang and enable some sanitizers: address, memory, undefined and signed-integer-overflow and use those builds to run through the test suite to help us verify that everything still looks fine.

Since it gets done in the CI for every change, I don’t have to run it myself locally very often. We have thus been using the default clang version shipped in Ubuntu 22.04 for this for quite some time now.

## Undefined behavior sanitizer

When the clang version for the Ubuntu jobs on GitHub was bumped up to version 18, the undefined behavior sanitizer job suddenly found plenty of new problems in curl.

In code that had been running without problems for a *long* time (decades in some cases) on countless systems and on almost every imaginable architecture. Unexpected.

## Picky function prototypes

Here is the reason:

The sanitizer now keeps track of exactly how a function pointer prototype is declared and verifies that the function actually called via that pointer is using an *identical* prototype.

This is generally probably a good idea and a sound sanity check for most programs but since the checker insists on identical prototypes, I believe it goes beyond what is undefined behavior – I believe some discrepancies are handled just fine. For example a signed vs unsigned pointer or void vs char pointers. I am however not a compiler developer and neither am I an expert in the C language specifications so maybe I am wrong.

## Example

A function pointer defined to call a function that returns a void and gets a single char pointer input

```
void (*name)(char *ptr);
typedef void (*name_func)(char *ptr);
```

Such a pointer can be made to point to a function that instead takes a void pointer:

```
void target(void *ptr)
{
   printf("Input %p\n", ptr);
}
```

This construct works perfectly fine in C:

```
char *data = "string";
name = (name_func)target;
name(data);
```

In libcurl we set function pointers (callbacks) via a setopt() style function, which cannot validate the pointer at compile time.

When the code example above is tested with the undefined behavior sanitizer and its `-fsanitize=function` check (I believe), it complains about the mismatching prototypes between the pointer and the actually called function.

## How this became annoying

For the example above, the sanitizer report is most welcome, even if I think it goes beyond what is actually *undefined* behavior. It helps us clean up the code.

For libcurl, we have a `CURL *` type returned for a handle from `curl_easy_init()`. This handle is used as an input argument to multiple functions and it is also used as an input argument to several callbacks an application can tell libcurl to call, etc.

That type was originally done like this:

```
typedef void CURL;
```

But in 2016, we changed it to instead become:

```
#if defined(BUILDING_LIBCURL)
typedef struct Curl_easy CURL;
#else
typedef void CURL;
#endif
```

This made us get a more descriptive pointer for the type when we build libcurl. For convenience.

The function pointer is defined internally for libcurl as a struct pointer, but outside in the application land as a void pointer. This works great.

Until this new sanitizer check. Now it complaints loudly because the prototypes for the function called does not match the prototype for the function pointer. The struct vs the void pointers. The sanitizer stores and uses “resolved” typedefs in its checks, not the name of the types visible in code.

## The fix

Since we can’t have build breakage in the CI jobs, [I fixed this](https://github.com/curl/curl/commit/eed3c8f4b722d86621a5946a98f62c6963026596).

We are back to how we did it in the past. With a plain

```
typedef void CURL;
```

… even when we build libcurl. To make sure the pointer and the final function have the same prototypes. To hush up the undefined behavior sanitizer.

This is now in master and how the code in the pending curl 8.11.0 release will look.

## Disabling the check is not enough

While we could disable this particular check in our CI jobs, that would not suffice since we want everyone to be able to run these tools against curl without any warnings or errors.

We also want application authors in general who use libcurl to be able to similarly run this sanitizer against their tools to not get error reports like this.

## Is this a clang issue?

Maybe. I just can’t see how this could happen by mistake, and since it is a feature that has existed for quite a while now already I have not bothered to submit an issue or have any argument or discussion with the clang team. I have simply accepted that this is the way they want to play this and adapt accordingly.

## A historic footnote

In 2016 I wanted to change the type universally to just

```
typedef struct Curl_easy CURL;
```

… as I thought we could do that without breaking neither API nor ABI. I still believe I was right, but the change still caused an “uproar” among some users who had already built code and done things based on the assumption that it was and would always remain a void pointer. Changing the type thus caused build errors at places to a level that made us retract that change and revert back to the #ifdef version showed above.

And now we had to retract even the #ifdef and thus we are back to the pre 2016 way.

## Post-publish update

It has been pointed out to me that the way the C standard is phrased, this tool seems to be correct. More discussions around that can be found in a [long OpenSSL issue from last year](https://github.com/openssl/openssl/issues/22896).

[cURL and libcurl](https://daniel.haxx.se/blog/tag/curl-and-libcurl/)[Development](https://daniel.haxx.se/blog/tag/de...