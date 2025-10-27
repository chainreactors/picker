---
title: 3.4: Finally Freed
url: https://binary.ninja/2023/05/03/3.4-finally-freed.html
source: Binary Ninja
date: 2023-05-04
fetch_date: 2025-10-04T11:39:56.685062
---

# 3.4: Finally Freed

[![](/images/binary-ninja-logo.svg)](/)

* [Features](/features/)
* [Enterprise](/enterprise/)
* [Sidekick](https://sidekick.binary.ninja)
* [Cloud](https://cloud.binary.ninja)
* [Training](/training/)
* [Support](/support/)

  [Extended Support](/support/extended.html)
  [Documentation](/support/#documentation)
  [License/Installer Recovery](/recover/)
  [Renew Current License](/renew/)
  [Slack Signup](https://slack.binary.ninja/)
  [FAQ](/faq/)
  [Sponsorship Information](/sponsorship/)
  [Portal](https://portal.binary.ninja/)
  [Contact Us](/support/)
* [Blog](/blog/)
* [Gear](https://shop.binary.ninja)

[Free](/free)
[Purchase](/purchase)

Participate in our [Reverse Engineering Survey](/survey/) to win free licenses or admission to [RE//verse](https://re-verse.io/)!

# Binary Ninja Blog

## 3.4: Finally Freed

* [Jordan Wiens](https://github.com/psifertex)
* 2023-05-03
* [announcements](/tag/announcements), [stable](/tag/stable)

To find out why our mascot for this release has a pitchfork and more on nerdy naming, read below the fold. For the summary of Braizeâs (3.4) major new features (including one surprise feature that appeared mid-roadmap), hereâs the highlights:

* [Inherited Types (C++ Support)](/2023/05/03/3.4-finally-freed.html#inherited-types)
* [Automatic Outlining](/2023/05/03/3.4-finally-freed.html#automatic-outlining)
* [Sparse Switch Recovery](/2023/05/03/3.4-finally-freed.html#sparse-switch-recovery)
* [Import from BNDB](/2023/05/03/3.4-finally-freed.html#import-from-bndb)
* [Enterprise Improvements](/2023/05/03/3.4-finally-freed.html#enterprise-improvements)
* [Debugger Improvements](/2023/05/03/3.4-finally-freed.html#debugger-improvements)
* [Experimental Features](/2023/05/03/3.4-finally-freed.html#experimental-features)
  + [Components UI](/2023/05/03/3.4-finally-freed.html#components-ui)
  + [MH\_FILESET](/2023/05/03/3.4-finally-freed.html#mh_fileset)
* [Many More](/2023/05/03/3.4-finally-freed.html#other-updates)

Youâll notice the theme of this release has been major improvements in decompilation, weâre really excited with the quality of improvements for the first three major features described above and theyâre joined by several other important improvements as well.

So why is the mascot for this release Binjy with a pitchfork? And what is Braize anyway? In case you missed our [last announcement](https://binary.ninja/2023/01/18/3.3-the-bytes-must-flow.html), weâve begun code-naming releases after Sci-Fi/Fantasy planets and in this case Braize is one of the lesser known [planets](https://coppermind.net/wiki/Braize) in Brandon Sandersonâs Cosmere, but despite its reputation as a prison/hellscape planet in that universe, as huge nerds, we couldnât resist including it early in our naming scheme. In this case, super-powered heroes were released from torment there, just like 3.4 has been released into the world with some super powers of its own! Itâs also fitting that âCâ is [Coruscant](https://www.starwars.com/databank/coruscant), with tomorrow being May the 4th! Feel free to send us your suggestions for [âEâ and beyond](https://github.com/Vector35/binaryninja-api/milestones).

## **Major Changes**

While major releases get all the press, even our point releases include a huge amount of changes. The first three can produce significantly better decompilation results across a variety of binaries and platforms.

### **Inherited Types**

![Create Structure Dialog Box >](/blog/images/3.4-release/CreateStructureDialogBox.png)

It will take more than one new feature to solve C++ reverse engineering, but one of the biggest obstacles has been resolved with this latest feature: the core type system now supports inherited types. So what does that mean? For starters, the UIs and APIs around creating structures have changed. Now when you use `s` to create a structure in linear view or the type sidebar, youâll see many new options:

The updated type system now lets you assign Base Structures, whose members will be inherited by your structure. You can avoid having to create duplicate members for every class in a hierarchy, and cross references will be propagated up the inheritance chain. Base Structures can also be located at an offset, supporting structures with multiple inherited bases.

For virtual function table-like classes, there is now the ability to propagate data variable references to the structure members. Looking at the cross references to a structure member will then include any annotated data variables using that structure. Simply put, if you mark up virtual tables, you can follow their functions from where they are used to what values they could have.

What really matters is what this allows you to do. Consider the following simple example:

```
struct A __packed
{
    struct vtable_for_A* vtable;
    int32_t x;
};

struct __base(A, 0) B
{
    struct vtable_for_B* vtable;
    __inherited int32_t A::x;
    int32_t y;
};

struct __base(B, 0) C
{
    struct vtable_for_C* vtable;
    __inherited int32_t A::x;
    __inherited int32_t B::y;
    int32_t z;
};
```

You can create these types in the above UI, or you can use the notation shown there as weâve extended the clang type parser to include the `__inherited` keyword.

Notice that the virtual tables support inheritance as well!

```
struct __data_var_refs __ptr_offset(0x10) vtable_for_A __packed
{
    void* field_0;
    void* typeinfo;
    int32_t (* sum)(struct A* this);
};

struct __base(vtable_for_A, 0) __data_var_refs __ptr_offset(0x10) vtable_for_B
{
    __inherited void* vtable_for_A::field_0;
    __inherited void* vtable_for_A::typeinfo;
    __inherited int32_t (* vtable_for_A::sum)(struct A* this);
};

struct __base(vtable_for_B, 0) __data_var_refs __ptr_offset(0x10) vtable_for_C
{
    __inherited void* vtable_for_A::field_0;
    __inherited void* vtable_for_A::typeinfo;
    void (* sum)(struct A* this);
};
```

The beauty of this is that, when the types are applied, you get cross-references across the entire binary for not only the base class, but all the children as well. Check out the cross references for Aâs virtual table versus Bâs virtual table in the following sample file:

![Cross References for Class A's Virtual Function Table](/blog/images/3.4-release/AVTableXrefs.png)
![Cross References for Class B's Virtual Function Table](/blog/images/3.4-release/BVTableXrefs.png)

All this combines to make a very powerful type system for object oriented languages like C++. For more details and an even more complicated example showing multiple inheritance, check out the [C++ Types help document](https://docs.binary.ninja/guide/types/cpp.html).

One thing to keep in mind is that compilers donât always follow the layout you expect! While debug info formats like PDBs contain the true data, your types may not always copy/paste directly from source code, so creating and applying the appropriate types may require some manual effort (for now!).

### **Automatic Outlining**

Yes, weâve talked about it [before](https://binary.ninja/2023/01/18/3.3-the-bytes-must-flow.html#automatic-outlining), but not only is the feature now enabled by default, it has had some important upgrades! To recap, this feature identifies instances where either a function call like `strcpy` might have been inlined and turns it back into an outlined function, or even just identifies situations where memory setting operations might have been unrolled (think initializing a stack array or structure to zero) and replaces them with a more convenient to a `memset` operation.

You can tell the feature is enabled by looking in your analyzed binary view for a `.synthetic_builtins` section:

![Synthetic Built-ins Section with memcpy functions](/blog/images/3.4-release/SyntheticBuiltins.png)

This fake section is created and appended to your existing memory layout, as a place to store function prototypes for these built in functions. Then we re-write analysis to point to those buil...