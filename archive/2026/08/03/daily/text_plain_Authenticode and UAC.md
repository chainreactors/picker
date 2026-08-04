---
title: Authenticode and UAC
url: https://textslashplain.com/2026/08/03/authenticode-and-uac/
source: text/plain
date: 2026-08-03
fetch_date: 2026-08-04T05:00:02.095811
---

# Authenticode and UAC

[Skip to content](#content)

[text/plain](https://textslashplain.com/)

ericlaw talks about security, the web, and software in general

# Authenticode and UAC

Posted by[ericlaw](https://textslashplain.com/author/ericlaw1979/)[2026-08-032026-08-03](https://textslashplain.com/2026/08/03/authenticode-and-uac/)Posted in[dev](https://textslashplain.com/category/dev/), [security](https://textslashplain.com/category/security/)Tags:[Authenticode](https://textslashplain.com/tag/authenticode/), [UAC](https://textslashplain.com/tag/uac/), [UX](https://textslashplain.com/tag/ux/)

When a user attempts to run a file with elevated privilege, Windows will show a User Account Control elevation prompt that asks whether the user trusts the file to run.

For a regular file, the user will see a prompt like this:

[![](https://i0.wp.com/textslashplain.com/wp-content/uploads/2026/08/image-7.png?resize=573%2C535&ssl=1)](https://i0.wp.com/textslashplain.com/wp-content/uploads/2026/08/image-7.png?ssl=1)

For a file signed by a certificate in the **Untrusted Certificates** store, elevation is explicitly blocked:

[![](https://i0.wp.com/textslashplain.com/wp-content/uploads/2026/08/image-9.png?resize=750%2C376&ssl=1)](https://i0.wp.com/textslashplain.com/wp-content/uploads/2026/08/image-9.png?ssl=1)

For a file with a trustworthy signature, the user is *expected* to see a prompt like this one:

[![](https://i0.wp.com/textslashplain.com/wp-content/uploads/2026/08/image-3.png?resize=455%2C392&ssl=1)](https://i0.wp.com/textslashplain.com/wp-content/uploads/2026/08/image-3.png?ssl=1)

However, I’m sometimes sometimes surprised to encounter a different behavior when running signed files.

## Surprise #1 – Windows Files are Special

The first surprise occurred last year when we were working testing the [Defender Deployment tool](https://learn.microsoft.com/en-us/defender-endpoint/defender-deployment-tool-windows). If we looked at the executable in File Explorer’s **Properties** dialog, we saw that it was correctly signed:

[![](https://i0.wp.com/textslashplain.com/wp-content/uploads/2026/08/image-8.png?resize=750%2C456&ssl=1)](https://i0.wp.com/textslashplain.com/wp-content/uploads/2026/08/image-8.png?ssl=1)

However, when double-clicking the file in Explorer, the UAC prompt behaved as if the file were not signed.

[![](https://i0.wp.com/textslashplain.com/wp-content/uploads/2026/08/image-6.png?resize=461%2C493&ssl=1)](https://i0.wp.com/textslashplain.com/wp-content/uploads/2026/08/image-6.png?ssl=1)

What gives?

After investigation, I learned that UAC has a special carve out for files that are signed by the Windows Build lab. If such a file is encountered outside of a limited set of directories deemed “secure” (e.g. `%systemroot%\system32`) the file is treated as unsigned.

*Windows executables are non-hermetic so running them from untrustworthy locations can have [dangerous outcomes](https://textslashplain.com/2015/12/18/dll-hijacking-just-wont-die/). Showing the file as unsigned is intended to discourage a user from doing this.*

## Surprise #2 – Chain Building

Today, I was downloading the updater for the latest update to Telerik Fiddler and unexpectedly encountered the **Unknown Publisher** UAC prompt. Before I fired off a flaming tweet to the team, I double-checked the binary and…

[![](https://i0.wp.com/textslashplain.com/wp-content/uploads/2026/08/image-10.png?resize=750%2C477&ssl=1)](https://i0.wp.com/textslashplain.com/wp-content/uploads/2026/08/image-10.png?ssl=1)

What? I immediately thought of the “only special folders” case I hit last year, but of course this third-party file wasn’t signed by the Windows build lab:

[![](https://i0.wp.com/textslashplain.com/wp-content/uploads/2026/08/image-12.png?resize=298%2C141&ssl=1)](https://i0.wp.com/textslashplain.com/wp-content/uploads/2026/08/image-12.png?ssl=1)

To double-check, I looked at the same file on a different machine, where the correct UAC prompt appeared showing the expected publisher. Hmmm…

I asked Gemini, which hallucinated a *plausible* but incorrect answer:

[![](https://i0.wp.com/textslashplain.com/wp-content/uploads/2026/08/image-13.png?resize=750%2C259&ssl=1)](https://i0.wp.com/textslashplain.com/wp-content/uploads/2026/08/image-13.png?ssl=1)

I knew this guess was wrong right away because I’ve studied the [MoTW behavior](https://textslashplain.com/2016/04/04/downloads-and-the-mark-of-the-web/) *extensively* for decades. Gemini’s *second* guess was better:

[![](https://i0.wp.com/textslashplain.com/wp-content/uploads/2026/08/image-14.png?resize=750%2C288&ssl=1)](https://i0.wp.com/textslashplain.com/wp-content/uploads/2026/08/image-14.png?ssl=1)

This guess was non-hallucinated and plausible, but the fact that the **File Properties** dialog showed the file as correctly signed implied that this guess was wrong.

Still. I looked at my affected machine’s **Trusted Root Certification Authorities** store**s**. Note the **s** there– your trusted roots are a merge of two storage areas, one for your local user account, and one for your local machine.

And here’s where things get interesting: I’ve got the GCC R45 Intermediate certificate in my local user account but not for the local machine:

[![](https://i0.wp.com/textslashplain.com/wp-content/uploads/2026/08/image-11.png?resize=750%2C396&ssl=1)](https://i0.wp.com/textslashplain.com/wp-content/uploads/2026/08/image-11.png?ssl=1)

That seems… *weird*. Weird enough to be an explanation. I complained to Gemini that it had gotten it wrong, but didn’t wait around for its insightful answer:

[![](https://i0.wp.com/textslashplain.com/wp-content/uploads/2026/08/image-16.png?resize=750%2C347&ssl=1)](https://i0.wp.com/textslashplain.com/wp-content/uploads/2026/08/image-16.png?ssl=1)

Instead, I used an old signature troubleshooting trick, enabling **CAPI2 Logging** in the Windows Event Viewer, and getting another data point. The problem was indeed that `consent.exe` (the UAC prompt) was failing to build a chain to a trusted root.

[![](https://i0.wp.com/textslashplain.com/wp-content/uploads/2026/08/image-17.png?resize=750%2C390&ssl=1)](https://i0.wp.com/textslashplain.com/wp-content/uploads/2026/08/image-17.png?ssl=1)

At that point, I used the certificate viewer to export the GCC root from the local user store and imported it into the local machine store.

Success!

[![](https://i0.wp.com/textslashplain.com/wp-content/uploads/2026/08/image-18.png?resize=750%2C404&ssl=1)](https://i0.wp.com/textslashplain.com/wp-content/uploads/2026/08/image-18.png?ssl=1)

Now, unlike Gemini, I have access to the source code to Windows, so I went off to discover exactly what it had already told me in my forgotten browser window:

[![](https://i0.wp.com/textslashplain.com/wp-content/uploads/2026/08/image-19.png?resize=750%2C392&ssl=1)](https://i0.wp.com/textslashplain.com/wp-content/uploads/2026/08/image-19.png?ssl=1)

Gemini further suggested that I try using an Elevated command prompt to verify the file’s signature:

```
signtool verify /pa /v "FiddlerClassicAutoupdater.exe"
```

… but Gemini failed to recognize that using an elevated command prompt isn’t going to use the non-working SYSTEM context. My user account, even elevated, will verify the signature just fine:

[![](https://i0.wp.com/textslashplain.com/wp-content/uploads/2026/08/image-21.png?resize=699%2C695&ssl=1)](https://i0.wp.com/textslashplain.com/wp-content/uploads/2026/08/image-21.png?ssl=1)

Finally, only one real mystery remained: *How did I have the correct intermediate in the local user store and why didn’t whatever* magic *put it there get it into the local machine store too?*

### AIA Fetching

By default, when Windows builds a certificate chain, if it cannot find the Intermediate certificate that the signing certificate chains to, it will look for a place to download that Intermediate using a process called [Authority Information Access (AIA)](https://learn.microsoft.com/en-us/windows-server/security/authority-informa...