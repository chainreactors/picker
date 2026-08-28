---
title: OWN-Defender
url: https://kitploit.com/en/tools/github/nirvanaon/own-defender
source: Kitploit
date: 2026-08-27
fetch_date: 2026-08-28T13:36:34.329882
---

# OWN-Defender

[Skip to content](#main-content)

[![Kitploit](/_next/image?url=%2Flogo.png&w=64&q=75)KITPLOIT](/en)[Tools](/en/tools)[Blog](/en/blog)Categories

EN

[Submit](/en/submit)

[Tools](/en/tools)[Blog](/en/blog)Categories

[Submit](/en/submit)

EN

Hacking, PenTest, and Cybersecurity Tools for Your Security Arsenal!

Kitploit is a directory of hacking, cybersecurity, and pentesting tools. Discover the latest project updates to find vulnerabilities, analyze systems, automate testing, and strengthen your security.

·Analytics preferences·[Feeds](/en/feeds)·[Contact](/en/contact)·[Privacy](/en/privacy)·© 2026 Kitploit

Tool Directory

## Categories

[View all categories](/en/categories)

Loading categories

[Tools](/en/tools)/![GitHub](/providers/github.png)GitHub/nirvanaon/own-defender

![](https://assets.kitploit.com/production/public/tools/53353/907fb06fb68852bb02ce24d2804c47f31e7044dd436e82a51fee5489226d064d-display-v1.webp)

[Defensive Tools](/en/categories/defensive-tools)[Exploitation](/en/categories/exploitation)[Reverse Engineering](/en/categories/reverse-engineering)[Binary Analysis](/en/categories/binary-analysis)[Learning & Education](/en/categories/education)

![GitHub](/providers/github.png)nirvanaon/own-defender

# OWN-Defender

Research project reverse-engineering Windows Security Center COM interfaces to trace AV registration through ATL, vtable, WSCAPI, and RPC, with runtime verification via WMI.

[View Repository](https://github.com/nirvanaon/own-defender)

10331 day ago![Not yet reviewed](/_next/image?url=%2Fbadges%2Fkitploit_badge_not_reviewed_full.png&w=48&q=75)

### Most Popular

[View all →](/en/tools)

Discover the most used tools by our community.

Last 7 DaysLast 30 Days

Explore all tools

Browse our collection of tools

[View all tools →](/en/tools)

Share

# OWN-Defender — Windows Security Center COM Research

**OWN-Defender** is a Windows security research project focused on understanding how **Windows Security Center (WSC)** represents and manages antivirus security products through its COM interfaces.

The project began as an investigation into the behavior demonstrated by [DefendNot](https://github.com/es3n1n/defendnot), but rather than treating the existing implementation as a black box, I used it as a starting point for independent reverse engineering and verification.

![Screenshot 2026-08-26 111717](https://assets.kitploit.com/production/public/readmes/53353/907fb06fb68852bb02ce24d2804c47f31e7044dd436e82a51fee5489226d064d/17aebe39848bcbcec1c2d20d2d6bf3004a444dd3eb8f375deb5d3b5240d26c07-display-v1.webp)

The goal of this project is to understand the complete execution path:

root@kitploit:~

```
COM
 ↓
CLSID / IID
 ↓
CoCreateInstance
 ↓
QueryInterface
 ↓
ATL Interface Map
 ↓
vtable
 ↓
IWscAVStatus4
 ↓
CWscIsv
 ↓
WSCAPI.dll
 ↓
RPC
 ↓
Windows Security Center
```

The project was developed and tested in a controlled Windows research environment.

> **Research / Educational Use Only**
>
> This project is intended for Windows internals research, reverse engineering, security education, and authorized security testing. Do not use it to interfere with security software on systems you do not own or have explicit permission to test.

---

## Research Motivation

The initial question was simple:

> **How does Windows Security Center know that an antivirus product exists?**

Instead of stopping at the public API documentation, I wanted to understand what happens underneath the API.

This led to several questions:

* Which COM class implements the WSC functionality?
* Which IID corresponds to the antivirus interface?
* How does `QueryInterface()` resolve the interface?
* Where is the interface stored in the ATL interface map?
* Why does IDA sometimes show only `__int64 a1` for a method?
* Why does the reconstructed C++ interface contain additional parameters?
* Which `Register()` function is actually the AV registration function?
* How does the registration eventually reach Windows Security Center?
* Where does the RPC boundary appear?
* How can the result be independently verified?

---

# Reverse Engineering Journey

## 1. Identifying the COM Class

The first step was identifying the Windows Security Center COM class.

The project uses the WSC COM class:

root@kitploit:~

```
CLSID_WscIsv
F2102C37-90C3-450C-B3F6-92BE1693BDF2
```

The implementation also contains logic to locate the CLSID dynamically from the Windows registry instead of relying exclusively on a hardcoded value.

Conceptually:

root@kitploit:~

```
HKLM
 └── SOFTWARE
     └── Classes
         └── CLSID
             └── {CLSID}
                 └── Windows Security Center ISV API
```

This provided the first important relationship:

root@kitploit:~

```
Registry
   ↓
CLSID
   ↓
Windows Security Center ISV API
```

---

## 2. Identifying the Correct Interface

The next challenge was determining which COM interface should be requested.

The project uses:

root@kitploit:~

```
IWscAVStatus4
```

with:

root@kitploit:~

```
4DCBAFAC-29BA-46B1-80FC-B8BDE3C0AE4D
```

One of the important lessons from the research was:

> **A GUID name alone is not enough evidence.**

I verified the relationship through reverse engineering rather than assuming that the interface name and GUID were correct.

The investigation included:

* GUID references
* `QueryInterface`
* ATL interface maps
* `_ATL_INTMAP_ENTRY`
* vtable locations
* cross-references
* function implementations
* runtime behavior

---

# 3. Understanding `QueryInterface`

One of the most useful reversing steps was following the implementation of:

root@kitploit:~

```
CComAggObject<CWscIsv>::QueryInterface()
```

which eventually reaches:

root@kitploit:~

```
ATL::CComObjectRootBase::InternalQueryInterface()
```

The ATL interface map is used to compare the requested IID against registered interface entries.

Conceptually:

root@kitploit:~

```
Requested IID
     ↓
QueryInterface()
     ↓
InternalQueryInterface()
     ↓
ATL Interface Map
     ↓
GUID comparison
     ↓
Matching interface
     ↓
Interface pointer
```

This provided independent evidence that the GUID being investigated actually corresponded to the expected COM interface.

---

# 4. The `Register()` Confusion

One of the biggest reversing challenges was understanding why IDA/Ghidra did not always display the method signature I expected.

The reconstructed interface contains:

root@kitploit:~

```
virtual HRESULT __stdcall Register(
    BSTR path,
    BSTR name,
    unsigned int,
    unsigned int
) = 0;
```

However, the decompiler could show an implementation such as:

root@kitploit:~

```
_IWscAVStatus4<CWscIsv>::Register(__int64 a1)
```

At first this looked inconsistent.

Further investigation showed that the decompiler representation was describing a wrapper/thunk and the underlying indirect vtable call rather than presenting the complete logical interface signature.

This became an important lesson:

> **Decompiler output is an interpretation of machine code, not the original source-level truth.**

To resolve these discrepancies, I compared:

root@kitploit:~

```
COM interface definition
        ↓
vtable layout
        ↓
assembly
        ↓
wrapper/thunk
        ↓
calling convention
        ↓
actual target function
```

---

# 5. Multiple `Register()` Functions

Another source of confusion was the presence of multiple functions with names such as:

root@kitploit:~

```
IWscAVStatus2::Register
IWscAVStatus4::Register
IWscFWStatus2::Register
RegisterAV
```

The important realization was that **similar names do not mean identical interfaces**.

For example:

root@kitploit:~

```
AV
 ↓
IWscAVStatus4
 ↓
AV registration
```

while:

root@kitploit:~

```
Firewall
 ↓
IWscFWStatus2
 ↓
Firewall registration
```

The interface number and surrounding implementation had to be verified instead of selecting a function simply because its name contained `Register`.

This was one of the most useful parts of the research because it forced me to correlate:

root@kitploit:~

`...