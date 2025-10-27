---
title: This year in LLVM (2022)
url: https://nikic.github.io/2022/12/20/This-year-in-LLVM-2022.html
source: nikic's blog
date: 2022-12-21
fetch_date: 2025-10-04T02:06:06.945791
---

# This year in LLVM (2022)

Blog by **nikic**.
Find me on [GitHub](https://github.com/nikic),
[StackOverflow](https://stackoverflow.com/users/385378/nikic),
[Twitter](http://twitter.com/nikita_ppv) and
[Mastodon](https://mastodon.social/%40nikic).
Learn more [about me](/aboutMe.html).

[« Back to article overview.](/)

# This year in LLVM (2022)

20. December 2022

Towards the end of last year, I switched from working on PHP at JetBrains, to working on LLVM at Red Hat. While it was already under discussion beforehand, this catalyzed the [creation of the PHP foundation](https://blog.jetbrains.com/phpstorm/2021/11/the-php-foundation/), which now pays multiple people to work on PHP. Special thanks for this go to Roman Pronskiy, who did most of the work to set up the foundation, and keeps it running ever since. Also a shout-out to Alexey Gopachenko, the unsung hero of PHP: As the PhpStorm team lead at the time, he drove JetBrains’ active investment in PHP core development and the community at large.

The [PHP 8.2 release](https://www.php.net/releases/8.2/en.php) shipped a couple weeks ago with fairly little contribution from myself. I somehow still managed to make the most controversial change, which is the [deprecation of dynamic properties](https://wiki.php.net/rfc/deprecate_dynamic_properties). And with that out of the way, let me jump into the actual topic of this blog post, which is what I’ve been up to since then.

## Opaque pointers

Historically, pointer types in LLVM carried an element type, for example `i32*`, `<4 x i16>*` or `%struct*`. In LLVM 15, these have been consolidated into an opaque `ptr` type.

The motivation for this change is simple: LLVM IR semantics say that the pointer element type carries no semantic meaning. You can take an `i8*` pointer, bitcast it into an `i32*` pointer and load an `i32` value from it. Optimizations *shouldn’t* make use of the pointer element type – if they do, they are either suboptimal, or outright wrong. But of course, as long as the element type is available, we can hardly blame optimization authors for trying to make use of it.

In addition to that high-level motivation, there are also practical considerations: Opaque pointers remove the need for pointer bitcasts, which improves memory usage and compile-time. It also improves optimization power, because optimizations can no longer fail to handle bitcasts, or rely on element types as (often wildly inaccurate) optimization hints.

The opaque pointer migration started in 2015 and has been moving slowly for a long time, due to the sheer scope of the change. After I joined Red Hat, I spent a significant fraction of my time for many months on bringing this migration over the finishing line, with help from Arthur Eubanks. Some of the larger pieces of work were:

* Migrating the Clang frontend to support opaque pointers. As the element type is no longer tracked by LLVM, frontends need to keep track of it separately. This work started with [storing the element type in Address](https://reviews.llvm.org/D115725), which had this wonderful comment in it:

  > When IR pointer types lose their element type, we should ***simply*** store it in Address instead for the convenience of writing code.

  This was followed by weeks of work migrating many hundreds of users of Address and related APIs to pass explicit element types. Simply.
* Adding support for bitcode auto-upgrade ([D118694](https://reviews.llvm.org/D118694), [D119339](https://reviews.llvm.org/D119339), [D119821](https://reviews.llvm.org/D119821), [D120471](https://reviews.llvm.org/D120471)). LLVM generally does not care about backwards-compatibility, with one exception: LLVM must be able to read bitcode produced by previous versions, auto-upgrading it as necessary.

  This was a significant challenge with opaque pointers: While doing an upgrade to opaque pointers is nominally as simple as discarding the unneeded pointer element types, the problem is performing other auto-upgrades at the same time. For example, historically loads were of the form `load i32* %p`, while now they explicitly specify the loaded type via `load i32, ptr %p`. When the `i32*` gets upgraded to `ptr`, we lose the necessary information to add the load type.

  This is solved by making the bitcode reader keep track of type IDs for all values, as well as which type IDs they contain as subtypes. For example, given a function pointer type like `void(i32*)*`, a series of contained type ID lookups allows us to determine the pointer element type of the parameter. Unfortunately, this does add significant complexity to the reader.
* A number of optimization passes were using “structural reasoning”, where struct pointer element types were used to drive optimizations. These optimizations had to be rewritten essentially from scratch to perform offset-based reasoning instead: Analyze at which offsets and with which types the pointer is actually used. This is a requirement for supporting opaque pointers, but also increases optimization power, because it can support bitcasted pointers.

  Examples of this include [argument promotion](https://reviews.llvm.org/D118685), [global SROA](https://reviews.llvm.org/D117223) and [global ctor evaluation](https://reviews.llvm.org/D115530).
* The long tail of “everything else”. There were hundreds of places inspecting pointer element types. Removing some of them was just a matter of switching to a different API, while others needed more substantial work and/or IR changes.

  Once we got to the point of no longer crashing during compilation, this also involved tracking down miscompiles caused by opaque pointers: These were almost always due to a no longer correct assumption that two instructions using the same pointer also operate on the same type. With opaque pointers, this requires an explicit check.

Opaque pointers were [enabled by default](https://reviews.llvm.org/D123300) for the LLVM 15 release,
with a big caveat: We did not convert all LLVM and Clang tests to use opaque pointers. For Clang,
most tests [were modified](https://reviews.llvm.org/D123115) to pass `-no-opaque-pointers`, while
LLVM tests auto-detect the opaque pointer mode based on what kind of pointer types are used in the
test.

Even with [some automation](https://gist.github.com/nikic/98357b71fd67756b0f064c9517b62a34), converting tests to use opaque pointers is very time consuming. There has been good progress on this, but the migration is not yet complete. We will only be able to drop typed pointer support once the test migration is done. I look forward to removing all that pesky pointer bitcasting code.

Opaque pointers have extensive [migration documentation](https://llvm.org/docs/OpaquePointers.html), and I also gave a talk at CGO-LLVM on the topic ([slides](https://www.slideshare.net/nikita_ppv/opaque-pointers-are-coming), [recording](https://www.youtube.com/watch?v=qWHLf31NnNk)). See those resources for more information.

## Constant expression removal

My next big project of the year was the [removal of constant expressions](https://discourse.llvm.org/t/rfc-remove-most-constant-expressions/63179). Historically, LLVM has supported a constant expression variant of nearly all instructions.

```
@g = external global i32

; Instruction
define ptr @test1() {
  %res = getelementptr i32, ptr @g, i64 1
  ret ptr %res
}

; Constant expression
define ptr @test2() {
  ret ptr getelementptr (i32, ptr @g, i64 1)
}
```

Some notion of constant expressions is needed for global variable initializers:

```
@g = external global i32
@g_end = global ptr getelementptr (i32, ptr @g, i64 1)
```

Only a small handful of “relocatable expressions” can actually be used as initializers. These basically come down to adding an offset to a global and, depending on the object file format, computing the offset between two globals.

However, LLVM conflated this initializer concept with general constant folding and allowed (nearly) all instructions to also be used as constant expressions. This also in...