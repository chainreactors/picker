---
title: Mark-of-the-Web: Real-World Protection
url: https://textslashplain.com/2024/12/12/mark-of-the-web-real-world-protection/
source: text/plain
date: 2024-12-13
fetch_date: 2025-10-06T19:38:04.807980
---

# Mark-of-the-Web: Real-World Protection

[Skip to content](#content)

[text/plain](https://textslashplain.com/)

ericlaw talks about security, the web, and software in general

# Mark-of-the-Web: Real-World Protection

Posted by[ericlaw](https://textslashplain.com/author/ericlaw1979/)[2024-12-122025-01-11](https://textslashplain.com/2024/12/12/mark-of-the-web-real-world-protection/)Posted in[security](https://textslashplain.com/category/security/)Tags:[MoTW](https://textslashplain.com/tag/motw/), [security](https://textslashplain.com/tag/security/), [zones](https://textslashplain.com/tag/zones/)

Two years ago, I wrote up some [best practices for developers](https://textslashplain.com/2022/12/02/mark-of-the-web-additional-guidance/) who want to take a file’s security origin into account when deciding how to handle it. That post was an update of a [post I’d written six years prior](https://textslashplain.com/2016/04/04/downloads-and-the-mark-of-the-web/) explaining how internet clients (e.g. browsers) mark a file to indicate that it originated from the untrusted Internet.

The *tl;dr* is that **many native apps’ security vulnerabilities can be significantly mitigated by blocking the use of files from the Internet**.

Consider [GrimResource](https://www.elastic.co/security-labs/grimresource), an attack vector documented this summer, whereby attackers would send the victim a Microsoft Management Console (`.msc` file). A user receiving such a file would see a standard security warning prompt:

[![](https://textslashplain.com/wp-content/uploads/2024/12/image-5.png?w=861)](https://textslashplain.com/wp-content/uploads/2024/12/image-5.png)

…and if accepted, the file would open and the attacker could run arbitrary code embedded in the file on the victim’s PC.

From a vulnerability purist’s viewpoint, **there’s no vulnerability here** — everything works as designed. From a security humanist’s viewpoint, however, this is unnecessarily awful.

A more accurate dialog box might read something like this:

[![](https://textslashplain.com/wp-content/uploads/2024/12/image-7.png?w=861)](https://textslashplain.com/wp-content/uploads/2024/12/image-7.png)

However, the*best* fix for this *specific* case is to **forbid MSC files from the Internet entirely**. Effectively *all* legitimate MSC files are pre-installed on the user’s local computer, so any such file from the Internet is almost guaranteed to be malicious. When the Management Console team fixed this bug, they chose the safe approach, simply blocking the file outright with no dangerous options:

[![](https://textslashplain.com/wp-content/uploads/2024/12/image-10.png?w=1024)](https://textslashplain.com/wp-content/uploads/2024/12/image-10.png)

Adding this check was pretty trivial.

```
// Files outside of the Local Computer, Trusted, and Intranet Zones
// are considered "Untrusted".
bool SourceIsUntrusted(LPCWSTR pwszFile)
{
  bool fUntrusted = true;
  DWORD dwZone = (DWORD)URLZONE_INVALID;
  CComPtr<IInternetSecurityManager> pSecMan;
  if (SUCCEEDED(CoInternetCreateSecurityManager(nullptr, &pSecMan, 0)))
  {
    if (SUCCEEDED(pSecMan->MapUrlToZone(pwszFile, &dwZone, 0)))
    {
       fUntrusted = (dwZone >= URLZONE_INTERNET);
       // Note: For the tightest lockdown, instead use
       //   fUntrusted = (dwZone!=URLZONE_LOCAL_MACHINE);
    }
  }
  return fUntrusted;
}
```

The `.msc` loader simply checks whether the source file originates from an untrusted location and if so, it errors out.

There are a few things to note about this `SourceIsUntrusted` function.

First, it **fails closed**— if the security manager cannot be created (very unlikely), the file is treated as untrusted. If the security manager cannot return a Zone mapping for the path (possible with various maliciously-crafted NTFS path strings), it’s treated as untrusted.

Next, it allows opening files from the Local Intranet and Trusted Sites security zones, allowing network admins **some flexibility** if they have some unusual practices in their environment (e.g. storing custom `.msc` files on an internal file share); they can unblock opening such files by using the Windows [Site to Zone Assignment](https://www.bing.com/search?q=Site+to+Zone+Assignment+List) policy.

Finally, you may’ve noticed that the final argument to `[MapUrlToZone](https://learn.microsoft.com/en-us/previous-versions/windows/internet-explorer/ie-developer/platform-apis/ms537133%28v%3Dvs.85%29)` is 0. This is the [MapURLToZone Flags](https://learn.microsoft.com/en-us/previous-versions/windows/internet-explorer/ie-developer/platform-apis/dd759042%28v%3Dvs.85%29) argument, and the default value of 0 is *usually* what you want.

There is, however, **an important exception**.

### Preventing NTLM Hash Leaks

In some cases, your app may wish to block opening remote files, e.g. to prevent a server from being able to see that a given file was opened (a so-called [Canary Token](https://canarytokens.org/nest/)), or to prevent [leakage of the user’s NTLM hash](https://textslashplain.com/2019/10/09/navigating-to-file-urls/#:~:text=to%20Edge%2095%2B.-,What%E2%80%99s%20the%20Risk%3F,-The%20most%20obvious).

Because Windows will attempt to perform NTLM Single Sign On (SSO), when fetching network file paths (e.g. `\\someserver\share\` or `file://someserver/share/`), it can leak the user’s account information (username) and hash of their password to the remote site. *Crucially, NTLM SSO is **not**today restricted by Windows Security Zone like HTTP/HTTPS SSO is:*

[![](https://textslashplain.com/wp-content/uploads/2019/10/image.png?w=1024)](https://textslashplain.com/wp-content/uploads/2019/10/image.png)

By default, Windows limits SSO to only the Intranet Zone for HTTP/HTTPS protocols

By default, the `MapURLToZone` function will connect to the server for a remote filepath to see whether there’s a `Zone.Identifier` alternate data stream on the target file. This potentially leaks NTLM information as a part of that connection.

The **`MUTZ_NOSAVEDFILECHECK`** flag prevents the `MapURLToZone` function from looking for that `Zone.Identifier` stream, protecting the hash.

However, **using `MUTZ_NOSAVEDFILECHECK` flag on a local file will also prevent your code from detecting that the file was downloaded from the Internet**. *Oops*. What’s an app developer to do? The answer is to call it twice:

```
// Files outside of the Local Computer, Trusted, and Intranet Zones
// are considered "Untrusted". Avoid connecting to the target
// server unless the URL's Zone is trustworthy.
bool SaferSourceIsUntrusted(LPCWSTR pwszFile)
{
  bool fUntrusted = true;
  DWORD dwZone = (DWORD)URLZONE_INVALID;
  CComPtr<IInternetSecurityManager> pSecMan;
  if (SUCCEEDED(CoInternetCreateSecurityManager(nullptr, &pSecMan, 0)))
  {
    if (SUCCEEDED(pSecMan->MapUrlToZone(pwszFile, &dwZone, MUTZ_NOSAVEDFILECHECK)))    {
       fUntrusted = (dwZone >= URLZONE_INTERNET);
       // For files currently stored in trusted locations,
       // ensure we also look for any MotW storing the
       // original source location.
       if (!fUntrusted) {
        fUntrusted = (!SUCCEEDED(pSecMan->MapUrlToZone(pwszFile, &dwZone, MUTZ_REQUIRESAVEDFILECHECK))) || (dwZone >= URLZONE_INTERNET);
       }
    }
  }
  return fUntrusted;
}
```

Does every application need to use this more elaborate `SaferSourceIsUntrusted` function?

No.

It’s only worthwhile to prevent `MapUrlToZone` from touching the file if nothing else has already touched it first.

For example, if the user opened Windows Explorer to `\\SomeServer\SomeShare` and double-clicked on `SomeMsc.msc`, they’ve already performed NTLM SSO on the target SMB server, so stopping `MapURLToZone` from doing so isn’t going to improve anything. Similarly, if something called `ShellExecute(`‘\\someserver\someshare\Somemsc.msc`), the Shell itself is going to check for that file’s existence (performing SSO) long before the Management Console handler application gets a chance to touch the file.

On the other hand, imagine that the Managem...