---
title: Dnsmasq DNS Remote Heap Buffer Overflow
url: https://blog.exodusintel.com/2026/07/20/dnsmasq-dns-remote-heap-buffer-overflow/
source: Exodus Intelligence
date: 2026-07-20
fetch_date: 2026-07-21T05:01:50.822248
---

# Dnsmasq DNS Remote Heap Buffer Overflow

[Skip to content](#content "Skip to content")

[![Exodus Intelligence](https://blog.exodusintel.com/wp-content/uploads/2018/10/exodus-final-logo-1_small.png "Exodus Intelligence")](https://blog.exodusintel.com/ "Exodus Intelligence")

Menu

* [Blog](https://blog.exodusintel.com/)
  + [Exploit Techniques](https://blog.exodusintel.com/category/exploit-techniques/)
  + [News](https://blog.exodusintel.com/category/news/)
  + [Training](https://blog.exodusintel.com/category/training/)
  + [Vulnerability Analysis](https://blog.exodusintel.com/category/vulnerability-analysis/)
  + [Other](https://blog.exodusintel.com/category/other/)
* [Offerings](https://exodusintel.com/index.html)
* [Company](https://exodusintel.com/about.html)
* [Capabilities](https://exodusintel.com/zeroday.html)
* [Training](https://exodusintel.com/training.html)
* [Advisories](https://blog.exodusintel.com/advisories-2/)

# EXODUS BLOG

---

## Dnsmasq DNS Remote Heap Buffer Overflow

JULY 20, 2026
[Vulnerability Analysis](https://blog.exodusintel.com/category/vulnerability-analysis/), [Exploit Techniques](https://blog.exodusintel.com/category/exploit-techniques/), [General Research](https://blog.exodusintel.com/category/general-research/)

*By David Barksdale*

In this blog post, we discuss a heap buffer overflow vulnerability that we found in Dnsmasq. This vulnerability was fixed in version 2.92rel2 and 2.93 on 11 May 2026 and assigned [CVE-2026-2291](https://nvd.nist.gov/vuln/detail/cve-2026-2291).

We cover the technical analysis of the vulnerability and how we exploited it to gain remote code execution on a OpenWRT target that is configured with a malicious upstream DNS server. Our customers had access to this research before it was independently discovered and released publicly.

## The Breaking Change

The vulnerability was introduced in release 2.73 with the following change:

```
commit cbe379ad6b52a538a4416a7cd992817e5637ccf9 (tag: v2.73rc5)
Author: Simon Kelley <simon@thekelleys.org.uk>
Date:   Tue Apr 21 22:57:06 2015 +0100

    Handle domain names with '.' or /000 within labels.

    Only in DNSSEC mode, where we might need to validate or store
    such names. In none-DNSSEC mode, simply don't cache these, as before.
```

## The Vulnerability

When Dnsmasq processes a reply from an upstream DNS server it will convert the domain names from DNS wire-format to C strings. In the above code change the format of the C string was modified to include an escape sequence for nulls (`0x00`), periods (`0x2E`), and the new escape character (`0x01`), potentially doubling the length of the storage required. Most fixed-length buffers for storing these strings were expanded except for the ones used in the caching system.

The caching system uses a buffer called `bigname` which is only 1,025 bytes in length. When Dnsmasq is caching the resource records in the answer section in a reply from an upstream DNS server, these heap-allocated buffers can be overflowed if their escaped forms exceed 1,025 bytes.

### Unsafe strcpy()

The root cause of the vulnerability is an unsafe `strcpy()` when a domain name is cached. Based on the size of the domain name string the name is either stored in a 50-byte buffer (`sname`) or a 1,025-byte buffer (`bigname`). The length of the string is not checked to ensure it does not exceed the size of the `bigname` buffer. The `really_insert()` function listed below calls the unsafe `strcpy()`.

```
// src/cache.c

static struct crec *really_insert(char *name, union all_addr *addr, unsigned short class,
                                  time_t now,  unsigned long ttl, unsigned int flags)
{
  struct crec *new, *target_crec = NULL;
  union bigname *big_name = NULL;
  int freed_all = (flags & F_REVERSE);
  struct crec *free_avail = NULL;
  unsigned int target_uid;

[Truncated]

  /* Check if we need to and can allocate extra memory for a long name.
     If that fails, give up now, always succeed for DNSSEC records. */
[1]
  if (name && (strlen(name) > SMALLDNAME-1))
    {
      if (big_free)
        {
[2]       big_name = big_free;
          big_free = big_free->next;
        }
      else if ((bignames_left == 0 && !(flags & (F_DS | F_DNSKEY))) ||
[3]            !(big_name = (union bigname *)whine_malloc(sizeof(union bigname))))
        {
          insert_error = 1;
          return NULL;
        }
      else if (bignames_left != 0)
        bignames_left--;

    }

  /* If we freed a cache entry for our name which was a CNAME target, use that.
     and preserve the uid, so that existing CNAMES are not broken. */
  if (target_crec)
    {
      new = target_crec;
      new->uid = target_uid;
    }

  /* Got the rest: finally grab entry. */
  cache_unlink(new);

  new->flags = flags;
  if (big_name)
    {
[4]   new->name.bname = big_name;
      new->flags |= F_BIGNAME;
    }

  if (name)
[5] strcpy(cache_get_name(new), name);
  else
    *cache_get_name(new) = 0;
```

At [1] the length of the `name` string is used to determine if a `bigname` buffer is needed. If the length is greater than `SMALLDNAME-1` (49) the code then allocates a `bigname` buffer by either removing one from a free list [2] or allocating a new one from the heap [3]. At [4] the allocated buffer `big_name` is stored in the cache record and the `F_BIGNAME` flag is set. At [5] the `cache_get_name()` function returns the `bigname` buffer from the cache record and `strcpy()`copies the `name` string to it. Since the `name` string may be larger than the 1,025-byte buffer, this `strcpy()` may overflow the heap buffer.

## Exploitation

To demonstrate an exploit we select a VM running the generic x86 build of OpenWRT version 24.10.4 as our target. The target system is configured to use our malicious server as the upstream DNS server. To exploit the vulnerability a client makes a series of DNS requests to the target: `alloc.me`, `overflow.me`, and `overwrite.me`.

The exploit uses the heap overflow vulnerability to overwrite the `next` pointer of another `bigname` buffer which is on the `big_free` free list. It then uses the normal operation of the cache system to write attacker-controlled data to an attacker-controlled address by allocating the corrupt `bigname` buffer from the free list and writing to it with `strcpy()`. The exploit uses this to overwrite a function pointer in the musl `ld.so` library. The exploit then triggers the function call leading to EIP control. These steps are described in more detail in the following subsections.

### Heap and Free List Preparation

The exploit needs to prepare two `bigname` buffers on the `big_free` list which are adjacent in memory. It does this by responding to the `alloc.me` DNS request with an answer of a chain of CNAME records that are each larger than 50 bytes. The chain is long enough to use up free heap blocks that aren’t adjacent so that the last two buffers are. The DNS answer has the `CD`bit set in the header which causes Dnsmasq to not cache the answer. This causes the allocated `bigname` buffers to be inserted in the `big_free` list to be allocated by the next step.

```
;; Got answer:
;; ->>HEADER<<- opcode: QUERY, status: NOERROR, id: 4345
;; flags: qr aa rd ra; QUERY: 1, ANSWER: 5, AUTHORITY: 0, ADDITIONAL: 0

;; QUESTION SECTION:
;alloc.me.			IN	A

;; ANSWER SECTION:
alloc.me.		60	IN	CNAME	AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA.
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA. 60 IN CNAME BBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBB.
BBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBB. 60 IN CNAME CCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCC.
CCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCC. 60 IN CNAME DDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDD.
DDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDD. 60 IN CNAME invalid.
```

### Heap Overflow

The exploit then responds to the `overflow.me` DNS request with another ch...