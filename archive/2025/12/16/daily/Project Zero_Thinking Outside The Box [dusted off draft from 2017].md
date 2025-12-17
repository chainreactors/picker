---
title: Thinking Outside The Box [dusted off draft from 2017]
url: https://projectzero.google/2025/12/thinking-outside-the-box.html
source: Project Zero
date: 2025-12-16
fetch_date: 2025-12-17T03:20:39.131099
---

# Thinking Outside The Box [dusted off draft from 2017]

[Project Zero](/)

---

[ ]

* [blog archive](/archive.html)
* [bug reports](https://project-zero.issues.chromium.org/savedsearches/7162405)
* [about](/about-pz.html)
* [Working at PZ](/working-at-project-zero.html)
* [0day: spreadsheet](/0day.html)
* [0day: Root Cause Analyses](https://googleprojectzero.github.io/0days-in-the-wild/rca.html)
* [vulnerability disclosure policy](/vulnerability-disclosure-policy.html)
* [reporting transparency](/reporting-transparency.html)
* search

# Thinking Outside The Box [dusted off draft from 2017]

[2025-Dec-16](/2025/12/thinking-outside-the-box.html "Permalink to this post")
Jann Horn

## Preface

Hello from the future!

This is a blogpost I originally drafted in early 2017. I wrote what I intended to be the first half of this post (about escaping from the VM to the VirtualBox host userspace process with [CVE-2017-3558](https://bugs.chromium.org/p/project-zero/issues/detail?id=1086)), but I never got around to writing the second half ([going from the VirtualBox host userspace process to the host kernel](https://bugs.chromium.org/p/project-zero/issues/detail?id=1091)), and eventually sorta forgot about this old post draftâ¦ But it seems a bit sad to just leave this old draft rotting around forever, so I decided to put it in our blogpost queue now, 8 years after I originally drafted it. Iâve very lightly edited it now (added some links, fixed some grammar), but itâs still almost as I drafted it back then.

When you read this post, keep in mind that unless otherwise noted, it is describing the situation as of 2017. Though a lot of the described code seems to not have changed much since thenâ¦

## Introduction

VM software typically offers multiple networking modes, including a NAT mode that causes traffic from the VM to appear as normal traffic from the host system. Both QEMU and VirtualBox use forks of [Slirp](http://slirp.sourceforge.net/) for this. Slirp is described as follows on its homepage:

*Slirp emulates a PPP or SLIP connection over a normal terminal. This is an actual PPP or SLIP link, firewalled for peopleâs protection. It makes a quick way to connect your Palm Pilot over the Internet via your Unix or Linux box!!! You donât need to mess around with your /etc/inetd.conf or your /etc/ppp/options on your system.*

Slirp is a useful basis for VM networking because it can parse raw IP packets (coming from the emulated network adapter) and forward their contents to the network using the host operating systemâs normal, unprivileged networking APIs. Therefore, Slirp can run in the hostâs userspace and doesnât need any special kernel support.

Both QEMU and VirtualBox donât directly use the upstream Slirp code, but instead use patched versions where, for example, the feature for setting up port forwards by talking to a magic IP address is removed. Especially in VirtualBox, the Slirp code has been altered a lot.

This post describes an issue in VirtualBox and how it can be exploited. Some parts are specific to the host operating system; in those cases, this post focuses on the situation on Linux.

## The packet heap in VirtualBox

The VirtualBox version of Slirp uses a custom zone allocator for storing packet data, in particular, incoming ethernet frames. Each NAT network interface has its own zone (`zone_clust`) with `nmbclusters=1024+32*64=3072` chunks of size `MCLBYTES=2048`. The initial freelist of each zone starts at the high-address end of the zone and linearly progresses towards the low-address end.

The heap uses inline metadata; each chunk is prefixed with the following structure:

```
struct item {
    uint32_t magic; // (always 0xdead0001)
    uma_zone_t zone; // (pointer to the zone; uma_zone_t is struct uma_zone *)
    uint32_t ref_count;
    struct {
        struct type *le_next; // (next element)
        struct type **le_prev; // (address of previous le_next)
    } list; // (entry in the freelist or in used_items, the list of used heap chunks)
};
```

![](data:image/png;base64...)

Chunks are freed through the methods `m_freem -> m_free -> mb_free_ext -> uma_zfree -> uma_zfree_arg -> slirp_uma_free`. The `uma_zfree_arg()` function takes pointers to the real zone structure and to the chunk data as arguments and checks some assertions before calling `slirp_uma_free()` as `zone->pfFree()`:

```
void uma_zfree_arg(uma_zone_t zone, void *mem, void *flags) {
    struct item *it;
    [...]
    it = &((struct item *)mem)[-1];
    Assert((it->magic == ITEM_MAGIC));
    Assert((zone->magic == ZONE_MAGIC && zone == it->zone));

    zone->pfFree(mem,  0, 0); // (zone->pfFree is slirp_uma_free)
    [...]
}
```

Unfortunately, `Assert()` [is `#define`âd to do nothing in release builds](https://www.virtualbox.org/browser/vbox/trunk/include/iprt/assert.h) - only âstrictâ builds check for the condition. The builds that are offered on the VirtualBox download page are normal, non-strict release builds.

Next, `slirp_uma_free()` is executed:

```
static void slirp_uma_free(void *item, int size, uint8_t flags) {
    struct item *it;
    uma_zone_t zone;
    [...]
    it = &((struct item *)item)[-1];
    [...]
    zone = it->zone;
    [...]
    LIST_REMOVE(it, list);
    if (zone->pfFini)
    {
        zone->pfFini(zone->pData, item, (int /*sigh*/)zone->size);
    }
    if (zone->pfDtor)
    {
        zone->pfDtor(zone->pData, item, (int /*sigh*/)zone->size, NULL);
    }
    LIST_INSERT_HEAD(&zone->free_items, it, list);
}
```

`slirp_uma_free()` grabs the zone pointer from the chunk header. Because `Assert()` is compiled out, there is no validation to ensure that this zone pointer points to the actual zone - an attacker who can overwrite the chunk header could cause this method to use an arbitrary zone pointer. Then, the member `pfFini` of the zone is executed, which, for an attacker who can point `it->zone` to controlled data, means that an arbitrary method call like this can be executed:

*`{controlled pointer}`*`({controlled pointer}, {pointer to packet data}, {controlled u32});`

Because the VirtualBox binary, at least for Linux, is not relocatable and has `memcpy()` in its PLT section, this can be used as a write primitive by using the static address of the PLT entry for `memcpy()` as function address:

`memcpy(dest={controlled pointer}, src={packet data}, n={controlled u32})`

This means that, even though the packet heap doesnât contain much interesting data, a heap memory corruption that affects chunk headers could still be used to compromise the VirtualBox process rather easily.

## The Vulnerability

In [changeset 23155](https://github.com/VirtualBox/virtualbox/commit/cd68926f500fe93c6fe4a33992201039eac526e9), the following code was added at the top of `ip_input()`, the method that handles incoming IP packets coming from the VM, before any validation has been performed on the IP headers. `m` points to the buffer structure containing the packet data pointer and the actual length of the packet data, `ip` points to the IP header inside the untrusted packet data. `RT_N2H_U16()` performs an endianness conversion.

```
if (m->m_len != RT_N2H_U16(ip->ip_len))
    m->m_len = RT_N2H_U16(ip->ip_len);
```

This overwrites the trusted buffer length with the contents of the untrusted length field from the IP packet. This is particularly bad because all safety checks assume that m->m\_len is correct - these two added lines basically make all following length checks useless.

Later, in [changeset 59063](https://github.com/VirtualBox/virtualbox/commit/b25d7cade21993266954de30b015310f23b9774d), the following comment was added on top of those lines:

```
/*
* XXX: TODO: this is most likely a leftover spooky action at
* a distance from alias_dns.c host resolver code and can be
* g/c'ed.
*/
if (m->m_len != RT_N2H_U16(ip->ip_len))
    m->m_len = RT_N2H_U16(ip->ip_len);
```

One straightforward way to abuse this issue is to send a small `ICMP_ECHO` packet with a large `ip_len` to the address 10.0.2.3, ...