---
title: Restoring Reflective Code Loading on macOS (Part II)
url: https://objective-see.org/blog/blog_0x82.html
source: Objective-See's Blog
date: 2025-11-24
fetch_date: 2025-11-25T03:11:51.016731
---

# Restoring Reflective Code Loading on macOS (Part II)

* [![](/images/logoApple.png)

  Objective-See

  a non-profit 501(c)(3) foundation.](/index.html)
* [ ]

  + [![](/images/aboutIcon.png)
    About](/about.html)
  + [![](/images/conferenceIcon.png)
    #OBTS](https://objectivebythesea.org/)
  + [![](/images/bookIcon.png)
    Book Series](https://taomm.org/)
  + [![](/images/weIcon.png)
    Objective-We](/we.html)
  + [![](/images/storeIcon.png)
    Our Store/Swag](https://objective-see.myshopify.com/)
  + [![](/images/malwareIcon.png)
    Malware Collection](https://github.com/Objective-see/Malware)
* Support Us!
* [![](/images/blogIcon.png)](/blog.html)
* [![](/images/productsIcon.png)

  tools](/tools.html)

---

Restoring Reflective Code Loading on macOS (Part II)

Apple silently 'broke' in-memory code loading on macOS ...let's restore it!

by: Patrick Wardle / November 24, 2025

The **Objective-See Foundation** is supported by:

[![](https://objective-see.org/images/friends/kandji.png)](https://www.kandji.io)

[![](https://objective-see.org/images/friends/fleetdm.png)](https://fleetdm.com)

[![](https://objective-see.org/images/friends/jamf.png)](https://www.jamf.com/?utm_source=objective-see&utm_medium=sponsored-link&utm_campaign=next-gen-security&utm_content=2021-02-05_protect)

[![](https://objective-see.org/images/friends/MoonlockLogoMacPaw.png)](https://moonlock.com)

[![](https://objective-see.org/images/friends/panw.png)](https://www.paloaltonetworks.com)

[![](https://objective-see.org/images/friends/sophos.png)](https://www.sophos.com/)

[![](https://objective-see.org/images/friends/malwarebytes.png)](https://www.malwarebytes.com/)

[![](https://objective-see.org/images/friends/iVerify.png)](https://www.iverify.io)

[![](https://objective-see.org/images/friends/huntress.png)](https://hubs.ly/Q02BYLy80)

**Note:**

Parts of this research were originally presented at [#OBTS v7.0](https://objectivebythesea.org/v7/index.html). In this blog we touch on some of the main highlights and takeaways from the talk, plus provide an open-source PoC.

Most importantly though we cover several important updates, such as support for “reflective” Objective-C payloads.

▪️ (Updated) Open-Source Proof of Concept: [Reflective Code Loader](https://github.com/pwardle/ReflectiveLoader).

▪️ Orignal Slides: “[Mirror Mirror: Restoring Reflective Code Loading on macOS](https://speakerdeck.com/patrickwardle/mirror-mirror-restoring-reflective-code-loading-on-macos)”

### Introduction

At #OBTS v7.0 I discussed restoring reflective code loading on macOS:

After the talk, I decided to publish a detailed write-up, beginning with [Part I](blog_0x7C.html). In that post, I walked through the history of reflective code loading on macOS and explained how Apple recently removed their in-memory loading APIs (e.g. `NSLinkModule`), effectively preventing such loading (at least at the API level):

> macOS malware often (ab)uses APIs such as NSCreateObjectFileImageFromMemory, NSLinkModule etc) to execute in-memory payloads.
>
> Apple has recently updated dyld3 (+these APIs), such that the in-memory payload is now first/always written out to disk 💾
>
> See: <https://t.co/vDuXLs6LXD> [pic.twitter.com/ALyFKSGRco](https://t.co/ALyFKSGRco)
>
> — Patrick Wardle (@patrickwardle) [July 15, 2022](https://twitter.com/patrickwardle/status/1547967373264560131?ref_src=twsrc%5Etfw)

However, at #OBTS (and in [Part I](blog_0x7C.html)) showed how one could rather elegantly incorporate Apple’s older loader code into one’s own loader to fully restore reflective code loading, even on macOS 15 (and, as it turns out, on macOS 26 as well):

```
% ./PoC https://file.io/IAKV6NC6JDC8

macOS Reflective Code Loader

[+] downloading from remote URL...
    payload now in memory (size: 68528), ready for loading/linking...

Press any key to continue...

dyld: 'ImageLoaderMachO::instantiateFromMemory' completed (image addr: 0x600000378180)
dyld: 'image->link' completed

[In-Memory Payload] Hello (reflectively loaded) World!
[In-Memory Payload] I'm loaded at: 0x10b290000

dyld: 'image->runInitializers' completed

Done!
Press any key to exit...
```

Here, in part II, we’ll:

* Add support for Objective-C payloads
* Discuss various methods of detecting reflective code loading

### Objective-C Payloads

In the first part of this blog post series, our in-memory payloads were all native C code. This was not a coincidence. Why? Well, it turns out that even the simplest Objective-C payload would crash.

Take, for example, the following snippet that simply builds an Objective-C (`NSString`) object and prints it out:

```
__attribute__((constructor))
void my_constructor(void) {
    ...

    NSString* msg =
    @"[In-Memory Payload] Hello (reflectively loaded Obj-C compatible) World!\n";

    printf("%s", msg.UTF8String);
}
```

If we compile this into a Mach-O binary and attempt to reflectively load it from a remote URL, it crashes hard:

```
% ./PoC <URL of Objective-C payload>

*** NSForwarding: warning: selector (0x1030f0a5b) for message 'UTF8String' does not match selector known to Objective C runtime (0x20d799473)-- abort

*** Terminating app due to uncaught exception 'NSInvalidArgumentException', reason: '-[__NSCFConstantString UTF8String]: unrecognized selector sent to instance 0x1030f4020'
```

The reason is straightforward. In a nutshell, the dynamic loader (`dyld`) whose code we’ve embedded into our reflective loader doesn’t (really) know anything about Objective-C.

And unless Objective-C classes and methods are properly “registered” with the Objective-C runtime, any attempt to invoke them will crash. This leads to errors like the ones shown earlier, including:

* *“does not match selector known to Objective C runtime”*
* *“unrecognized selector sent to instance”*

**Note:**
In the world of Objective-C, a "selector" is essentially the name of a method. More specifically, a selector ("SEL") is a unique identifier that represents a method's name and its signature in Objective-C. It's how the runtime refers to methods internally.

Normally, `dyld` calls into the Objective-C runtime library, `libobjc.A.dylib` (located in `/usr/lib/`), to handle all the necessary registrations so that referenced Objective-C classes and methods are properly registered and everything runs smoothly. Unfortunately, since `libobjc.A.dylib` (unlike `dyld`) is closed-source, we cannot compile it into our reflective loader.

Luckily, as pointed out by [Ryan Wincey](https://x.com/rwincey), researchers (such as Stanislaw Pankevich) working on dynamically adding Objective-C and Swift code to LLVM had already largely solved this problem.

> A few months ago, I hit a wall trying to reflectively load ObjC libraries with [@patrickwardle](https://twitter.com/patrickwardle?ref_src=twsrc%5Etfw)’s recent macOS reflective loader. The fix? A completely unexpected LLM prompt. 🔥
>
> Problem solved — full write-up here <https://t.co/EfgpXL74we> <https://t.co/moPJIdfYlm>
>
> — b0yd (@rwincey) [July 20, 2025](https://twitter.com/rwincey/status/1947020490821738764?ref_src=twsrc%5Etfw)

**Note:**

You can read Ryan’s writeup here: “[Obj-C Reflective Code Loading on macOS via AI](https://www.securifera.com/blog/2025/07/20/objc-reflective-code-loading-on-macos-via-ai/)”

Specifically, in an excellent article titled “[LLVM JIT, Objective-C and Swift on macOS: knowledge dump](https://stanislaw.github.io/2018-09-03-llvm-jit-objc-and-swift-knowledge-dump.html),” Stanislaw proposed (and implemented) a method to “activate” JIT’d Objective-C components by explicitly registering them with the Objective-C runtime. This involves:

1. Registering selectors
2. Registering classes (and super classes)

**Note:**

We have to register all classes and methods, that includes both our own custom classes and their methods, but also Apple ones that our code invokes (e.g. the NSString class and UTFString method).

Selectors, as noted earlier, are essentially names that identify a method. Recall that in our simple Objective-C paylo...