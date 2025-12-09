---
title: A Remote Pre-Authentication Overflow in LLDB's debugserver
url: https://objective-see.org/blog/blog_0x83.html
source: Objective-See's Blog
date: 2025-12-08
fetch_date: 2025-12-09T03:16:55.076366
---

# A Remote Pre-Authentication Overflow in LLDB's debugserver

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

When Good /bins Go Bad

A Remote Pre-Authentication Overflow in LLDB's debugserver

by: Nathaniel Oh / December 7, 2025

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

In this guest blog post, [Nathaniel Oh](https://www.linkedin.com/in/calysteon/) details a recent bug he discovered and reported to Apple — a remote pre-authentication buffer overflow in LLDB’s `debugserver`, now patched as **CVE-2025-43504**.

Mahalo to Nathaniel for sharing his research! 🙏🏽

## Introduction

Growing up, I always enjoyed digging through the DVD bins at my local Walmart. I noticed a lot of the same movies were left on top, but if you actually dug in, you’d find more interesting and niche titles.

When a program overflows a buffer, you’re essentially reaching into its bargain bin. Depending on how far you reach, the DVDs - or in this case, the overwritten structures in memory - can change.

Today’s bargain `/bin` is CVE-2025-43504: A remote pre-authentication global buffer overflow I found in [LLDB’s `debugserver`](https://github.com/llvm/llvm-project/tree/main/lldb/tools/debugserver).

## How Did We Get Here?

During application development, developers often find the need to debug their app on a physical iOS device. To accomplish this, Xcode mounts a Developer Disk Image on the target iPhone and then pairs with it.

Once paired, the macOS host is able to communicate with the iOS client using the `debugserver` installed onto the client. Now any client that can establish a GDB-remote session to the device’s `debugserver` can reach the `qSpeedTest` handler and overflow the vulnerable buffer.

Let’s take a look at the Xcode 26.1 security release page to better understand how Apple categorized CVE-2025-43504:

![](../images/blog/blog_0x83/advisory.png)
CVE-2025-43504

Due to modern-day software mitigations, Apple considers buffer overflows to primarily be a denial-of-service issue rather than a corruption primitive. As we will explore today, this is generally true as an attacker will need to overcome several hurdles and likely pair this issue with another bug to achieve arbitrary code execution.

### One Small Step for Pwn, One Giant Leap for Pwnkind

If you would like to experiment with a pre-patched version of `debugserver`, use the following commit or any commits prior to [ac8e7be5fbd11f731ffc81bf3bbae50a5a4d83de](https://github.com/llvm/llvm-project/commit/ac8e7be5fbd11f731ffc81bf3bbae50a5a4d83de):

```
git clone https://github.com/llvm/llvm-project.git
cd llvm-project
git checkout 37cd595c1ccb1fd84ebdfeb0d959744a4d13726c
```

## You’re Going to Need a Bigger Debugger

Before the patch in [RNBRemote.cpp](https://github.com/llvm/llvm-project/blob/main/lldb/tools/debugserver/source/RNBRemote.cpp), any remote user who could connect to an iOS device’s `debugserver` could send a pre-authentication `qSpeedTest` packet to `RNBRemote::HandlePacket_qSpeedTest` and corrupt adjacent structures in the global data segment of `debugserver`.

However, there’s an important caveat: we only control the *length* of the corruption. The contents of the payload are fixed to a stream of `'a'` characters. While students may enjoy the consistently high marks, the practical utility of this overflow is greatly limited by the fact that we can’t control the actual bytes being written-only how far the flood of `'a'`s goes.

Now, let’s take a look under the hood of [`RNBRemote::HandlePacket_qSpeedTest`](https://github.com/llvm/llvm-project/blob/main/lldb/tools/debugserver/source/RNBRemote.cpp#L4417-L4431) to see exactly what is going on:

```
rnb_err_t RNBRemote::HandlePacket_qSpeedTest(const char *p) {
  p += strlen("qSpeedTest:response_size:");
  char *end = NULL;
  errno = 0;
  // We control the length of response_size
  uint64_t response_size = ::strtoul(p, &end, 16);
  if (errno != 0)
    return HandlePacket_ILLFORMED(
        __FILE__, __LINE__, p,
        "Didn't find response_size value at right offset");
  else if (*end == ';') {
    static char g_data[4 * 1024 * 1024 + 16];
    strcpy(g_data, "data:");
    // The overflow of g_data by a's occurs here
    memset(g_data + 5, 'a', response_size);
    g_data[response_size + 5] = '\0';
    return SendPacket(g_data);
  } else {
    return SendErrorPacket("E79");
  }
}
```

The role of `RNBRemote::HandlePacket_qSpeedTest()` is to process incoming `qSpeedTest:response_size:<hex>;` packets without requiring authentication from a remote user who can communicate to the iOS device’s `debugserver` binary.

However, once a remote user is able to send a `qSpeedTest:response_size:<hex>;` packet to `debugserver`, no authentication checks occur within `debugserver` prior to processing the user-supplied `response_size`. Therefore, any user who can communicate with an iOS device mounted with a Developer Disk Image is able to overflow `debugserver` via a `qSpeedTest:response_size:<hex>;` packet.

### Just Keep Swimmin’ Swimmin’ Swimmin'

Now that we’ve reached the vulnerable function `RNBRemote::HandlePacket_qSpeedTest()`, let’s examine exactly how the overflow occurs. First, the user-supplied size `<hex>` in the `qSpeedTest:response_size:<hex>;` packet is extracted and stored in the variable `response_size`:

```
p += strlen("qSpeedTest:response_size:");
char *end = NULL;
errno = 0;
uint64_t response_size = ::strtoul(p, &end, 16);
```

If parsing succeeds and the next character is a semicolon, a function‑local static 4 MiB + 16‑byte buffer `g_data` is initialized and seeded with the ASCII header `"data:"`:

```
if (errno != 0)
  return HandlePacket_ILLFORMED(__FILE__, __LINE__, p,
                                "Didn't find response_size value at right offset");
else if (*end == ';') {
  static char g_data[4 * 1024 * 1024 + 16];
  strcpy(g_data, "data:");
```

### Oops, I Did It Again

Putting it all together, `memset` then fills the static 4 MiB + 16‑byte buffer `g_data` with `'a'` using the user-controlled `response_size` value as the number of `'a'`s to use.

```
  // The overflow of g_data by 'a's occurs here
  memset(g_data + 5, 'a', response_size);
  g_data[response_size + 5] = '\0';
```

Therefore, whenever a remote LLDB client sends a `qSpeedTest:response_size:<hex>;` packet with a `response_size` greater than the 4 MiB + 16‑byte buffer, a buffer overflow occurs and corrupts adjacent global variables stored in the global data segment (`.bss`) of `debugserver`.

## When Good Bins Go Bad

Now...