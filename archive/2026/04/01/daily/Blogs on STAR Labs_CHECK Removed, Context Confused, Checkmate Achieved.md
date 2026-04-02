---
title: CHECK Removed, Context Confused, Checkmate Achieved
url: https://starlabs.sg/blog/2026/04-check-removed-context-confused-checkmate-achieved/
source: Blogs on STAR Labs
date: 2026-04-01
fetch_date: 2026-04-02T04:29:27.351632
---

# CHECK Removed, Context Confused, Checkmate Achieved

[![logo](https://starlabs.sg/logo-white.png)](https://starlabs.sg/ "  (Alt + H)")

* [Home](https://starlabs.sg/ "Home")
* [About](https://starlabs.sg/about/ "About")
* [Advisories](https://starlabs.sg/advisories/ "Advisories")
* [Blog](https://starlabs.sg/blog/ "Blog")
* [Achievements](https://starlabs.sg/achievements/ "Achievements")
* [Publications](https://starlabs.sg/publications/ "Publications")
* [Search](https://starlabs.sg/search/ "Search (Alt + /)")

[Home](https://starlabs.sg/) » [Blogs](https://starlabs.sg/blog/)

# CHECK Removed, Context Confused, Checkmate Achieved

April 1, 2026 · 19 min · Shreyas Penkar (@streypaws)

Table of Contents

* [TL;DR](#tldr)
* [Introduction](#introduction)
* [Reversing the Patch](#reversing-the-patch)
* [Understanding Class Member Reparsing](#understanding-class-member-reparsing)
* [Triggering the Effects of Interleaving](#triggering-the-effects-of-interleaving)
* [Can we Checkmate without a CHECK?](#can-we-checkmate-without-a-check)
* [Conclusion](#conclusion)

## TL;DR[#](#tldr)

In January 2026, the [Chrome Releases](https://chromereleases.googleblog.com/2026/01/) blog announced several security fixes across different Chrome components. One entry caught our attention: **[CVE-2026-0899](https://www.cve.org/CVERecord?id=CVE-2026-0899)**, an Out-of-Bounds memory access in V8 discovered by [@p1nky4745](https://x.com/p1nky4745).

Vulnerabilities in V8, especially OOB and Type Confusions are always interesting from a security research perspective. We decided to take a closer look. At the time of writing, the issue was still restricted and no public proof-of-concept was available. After reverse engineering the patch fix, we identified the root cause of the vulnerability and developed a trigger PoC.

Triggering the bug alone was not enough; we wanted to see how far it could go. During our exploitation attempts, we encountered a stubborn **`CHECK`** standing directly in our path. We were equally stubborn, so we removed the **`CHECK`** and tried again. This time, the vulnerability became exploitable, eventually yielding arbitrary read/write primitives.

This post documents our journey reproducing, analyzing, and exploiting CVE-2026-0899, under the guidance of Nguyễn Hoàng Thạch (@hi\_im\_d4rkn3ss).

## Introduction[#](#introduction)

|  |  |
| --- | --- |
| CVE | CVE-2026-0899 |
| Impact | High |
| Affected Products | V8 JS Engine within Google Chrome and other products |
| Bug IDs | crbug-458914193 |
| Patch | [https://chromium-review.googlesource.com/c/v8/v8/+/7203465](https://chromium-review.googlesource.com/c/v8/v8/%2B/7203465) |

We first came across **CVE-2026-0899** in the January 2026 [Chrome Releases](https://chromereleases.googleblog.com/2026/01/) blog, where it was described as an **Out-of-Bounds memory access in V8**. The bug was reported by [@p1nky4745](https://x.com/p1nky4745), who also mentioned discovering it with a [custom fuzzer](https://x.com/p1nky4745/status/2011216193815003225).

A quick look at the patch revealed that the vulnerability lived in V8’s class member initializer reparsing logic. At the time of writing, however, there was no public proof-of-concept available, and the corresponding [Chromium issue](https://issuetracker.google.com/issues/458914193) remained restricted.

This made the bug even more interesting. With only the patch to work from, we set out to reverse-engineer the fix, understand the root cause, and craft our own **trigger PoC**.

## Reversing the Patch[#](#reversing-the-patch)

The patch is available [here](https://chromium.googlesource.com/v8/v8/%2B/978f2b8a73fdc1c6d17fa5966dee81393e2f1533%5E%21/#F8). Let’s examine the different changes that were made. The patch introduces two new `FunctionKind` variants to encode ordering:

* `kClassMembersInitializerFunctionPrecededByStatic`
* `kClassStaticInitializerFunctionPrecededByMember`

It also adds helpers `IsClassInstanceInitializerFunction` and `IsClassStaticInitializerFunction`, and broadens `IsClassInitializerFunction` to cover all four kinds. [1][2]

```
inline bool IsClassInstanceInitializerFunction(FunctionKind kind) {
  return base::IsInRange(
      kind, FunctionKind::kClassMembersInitializerFunction,
      FunctionKind::kClassMembersInitializerFunctionPrecededByStatic); // [1]
}

inline bool IsClassStaticInitializerFunction(FunctionKind kind) {
  return base::IsInRange(
      kind, FunctionKind::kClassStaticInitializerFunction,
      FunctionKind::kClassStaticInitializerFunctionPrecededByMember); // [2]
```

In [parser-base.h](https://chromium-review.googlesource.com/c/v8/v8/%2B/7203465/8/src/parsing/parser-base.h), `EnsureStaticElementsScope` and `EnsureInstanceMembersScope` now choose the appropriate `FunctionKind` based on whether the other type already exists, thereby recording ordering in the scope’s kind. [3] [4]

```
DeclarationScope* EnsureStaticElementsScope(ParserBase* parser, int beg_pos,
                                                int info_id) {
      if (!has_static_elements()) {
        FunctionKind kind =
            has_instance_members()
                ? FunctionKind::kClassStaticInitializerFunctionPrecededByMember // [3]
                : FunctionKind::kClassStaticInitializerFunction;
        static_elements_scope = parser->NewFunctionScope(kind);
        static_elements_scope->SetLanguageMode(LanguageMode::kStrict);
        static_elements_scope->set_start_position(beg_pos);
        static_elements_function_id = info_id;
        // Actually consume the id. The id that was passed in might be an
        // earlier id in case of computed property names.
        parser->GetNextInfoId();
      }
      return static_elements_scope;
    }

    DeclarationScope* EnsureInstanceMembersScope(ParserBase* parser,
                                                 int beg_pos, int info_id) {
      if (!has_instance_members()) {
        FunctionKind kind =
            has_static_elements()
                ? FunctionKind::kClassMembersInitializerFunctionPrecededByStatic // [4]
                : FunctionKind::kClassMembersInitializerFunction;
        instance_members_scope = parser->NewFunctionScope(kind);
        instance_members_scope->SetLanguageMode(LanguageMode::kStrict);
```

Crucially, `ParseClassForMemberInitialization` now pre-allocates the “other” scope when the initializer kind indicates it was preceded by the other type, ensuring the correct ID is reserved before parsing proceeds. Additionally, `ResetInfoId` was updated to accept an initial value, simplifying ID management. [5]

```
    if (initializer_kind ==
        FunctionKind::kClassMembersInitializerFunctionPrecededByStatic) {
      class_info.EnsureStaticElementsScope(this, kNoSourcePosition, -1); // [5]
    } else if (initializer_kind ==
               FunctionKind::kClassStaticInitializerFunctionPrecededByMember) {
      class_info.EnsureInstanceMembersScope(this, kNoSourcePosition, -1);
    }
```

What does all this mean? This V8 patch fixes a parsing issue with JavaScript classes that have both `instance` fields and `static` blocks mixed together. When V8 lazily compiles `class initializers`, it needs to maintain the correct order of function literal IDs. When `instance` and `static` initializers are interleaved, reparsing one initializer could disrupt the ID ordering.

The patch adds two new `FunctionKind` variants in the parser to encode this ordering information, along with helper functions to identify them. It now uses these variants when creating scopes, choosing the appropriate kind based on whether the other initializer type already exists. Most importantly, when reparsing a specific initializer, V8 now pre-allocates the scope for any preceding initializer type to preserve the correct ID sequence. To understand the vulnerability better, let’s examine how the bug manifests in the older code with some examples.

## Understanding Class Member Reparsing[#](#understanding-class-member-reparsing)

V8 basically synthesizes two function...