---
title: A Nifty Initial Access Payload
url: https://blog.compass-security.com/2024/12/a-nifty-initial-access-payload/
source: Over Security - Cybersecurity news aggregator
date: 2024-12-18
fetch_date: 2025-10-06T19:44:21.369883
---

# A Nifty Initial Access Payload

## [Compass Security Blog](https://blog.compass-security.com "Compass Security Blog — Offensive Defense")

### Offensive Defense

* [Home](https://blog.compass-security.com/)
* [Archive](https://blog.compass-security.com/archive/)
* [Contact](https://blog.compass-security.com/contact/)
* [Newsletter](https://blog.compass-security.com/mailing-list-tigerinfo/)

* [Home](https://blog.compass-security.com/)
* [Archive](https://blog.compass-security.com/archive/)
* [Contact](https://blog.compass-security.com/contact/)
* [Newsletter](https://blog.compass-security.com/mailing-list-tigerinfo/)

# [A Nifty Initial Access Payload](https://blog.compass-security.com/2024/12/a-nifty-initial-access-payload/ "A Nifty Initial Access Payload")

[December 17, 2024](https://blog.compass-security.com/2024/12/a-nifty-initial-access-payload/ "A Nifty Initial Access Payload")
 /
[Sylvain Heiniger](https://blog.compass-security.com/author/sheinige/ "Posts by Sylvain Heiniger")
 /
[0 Comments](https://blog.compass-security.com/2024/12/a-nifty-initial-access-payload/#respond)

Red Teaming engagements are “realistic” attack simulations designed to test the security posture of an organization and its Blue Team. This term is used in many different ways, so if you’re not sure where to draw the line, Michael Schneier’s [latest blog post](https://www.scip.ch/en/?labs.20241114) provides a good comparison of different types of assessment.

Anyway, when doing attack simulations or red teaming engagements, we often want to run code on a victim machine of our customer. Due to the presence of an Endpoint Detection and Response (EDR) software, this is not an easy task. However, a combination of some well-known techniques will usually do the trick for what we call initial access.

But what do we do when the known techniques fail and we cannot use known initial access methods? In that case, we need to develop a custom payload. Since it’s nice to run our code in a signed process to better blend in, we then check the installed software.

## A wild screenshot tool appears

In a recent engagement, we found an outdated screenshot tool running on startup on our victim machine that allowed users to install plugins. Double-clicking on a file with a custom extension would extract its (zipped) contents and the software would load the plugin DLL. No mark-of-the-web, no execution restrictions, etc. Nice.

### First attempt: Replace the plugin DLL

Can we just make a fake plugin with our malicious DLL? No. Plugins contain a manifest and the plugin DLL has to be signed by the vendor of the software, so it’s secure, right?

### Second attempt: Replace the dependency DLL

We were lucky enough to find an existing plugin that was signed by the vendor, which in turn would load an unsigned DLL. My first thought is, let’s build a dumb payload with a dllmain, replace the unsigned DLL, win.

```
#define WIN32_LEAN_AND_MEAN
#include <windows.h>
__declspec(dllexport) BOOL APIENTRY DllMain(HMODULE hModule,
	DWORD ul_reason_for_call,
	LPVOID lpReserved
)
{
	switch (ul_reason_for_call) {

	case DLL_PROCESS_ATTACH:
	{
		MessageBox(
			0,            /* HWND    hWnd,      */
			"Burp!=B33F", /* LPCTSTR lpText,    */
			"Burp!=B33F", /* LPCTSTR lpCaption, */
			1             /* UINT    uType      */
		);
		break;
	}
	case DLL_PROCESS_DETACH:
	{
		break;
	}
	case DLL_THREAD_ATTACH:
	{
		break;
	}
	case DLL_THREAD_DETACH:
	{
		break;
	}

	}
	return TRUE;
}
```

It didn’t work, the plugin couldn’t be installed.

[![](https://blog.compass-security.com/wp-content/uploads/2024/11/image.png)](https://blog.compass-security.com/wp-content/uploads/2024/11/image.png)

This unsigned DLL is a managed (.NET ) DLL, which means that when it is loaded, the CLR will check its manifest before anything else. Hm, how do we execute code then? A couple of ideas came to mind.

### Third attempt: Decompile, add code, recompile

It’s .NET, right? Simple: decompile, add code recompile. That might work, but when we decompile we notice something annoying. The DLL is used for interoperation with COM and contains only interfaces. Interfaces cannot contain code.

### Fourth attempt: Module initializer

Can we not run static code in C#? The answer is that we can, it’s called a module initializer. Let’s create a class and a method that will execute our shellcode:

```
using System;
using System.IO;
using System.Runtime.InteropServices;
using Microsoft.Win32;

internal static class ModuleInitializer
{
    internal static void Run()
    {
		ModuleInitializer.MessageBox(IntPtr.Zero, "Burp!=B33F", "Burp!=B33F", 1U);
	}

	[DllImport("user32.dll", SetLastError = true, CharSet= CharSet.Auto)]
	public static extern int MessageBox(IntPtr hWnd, String text, String caption, uint type);
}
```

Using <https://github.com/kzu/InjectModuleInitializer>, we inject the above code into the module initializer.

```
.\InjectModuleInitializer.exe .\interoplib.dll
InjectModuleInitializer v1.3

Module Initializer successfully injected in assembly .\interoplib.dll
```

The plugin is installed successfully but the code is not executed. When we use the functionality provided by the plugin (i.e. some parts of the .NET module are actually used), our code (and our shellcode) is executed. This is fine, but not perfect, we would prefer to have the code run on the first click.

### Fifth attempt: PE native entry point

Googling into how to execute code when the DLL is loaded by the CLR led us to this great blog post: <https://blog.washi.dev/posts/entry-points/>.

Adding a PE native entry point to our DLL could do the trick. It would run as soon as the DLL is loaded, which as we can see using Process Monitor happens when the plugin is installed.

Using the author’s [AsmResolver tool](https://github.com/Washi1337/AsmResolver), and building on top of [the example from the blog post](https://gist.github.com/Washi1337/a35acf49b64b07637a3047eec23c4e58), we inject code into the DLL and put its address in the PE native entrypoint.

Result, it works, our (shell)code runs on plugin installation!

## Conclusion

This (rather long) journey allowed us to have a simple payload, that we could deliver via a web page (using HTML smuggling) and which, when double-clicked, would run our shellcode in the signed process of the screenshot tool. Nifty!

Here are our key takeaways:

* Custom extension handlers are a nice way to phish.
* Living in a signed and known process confuses both EDR and Blue Team
* Sometimes you have to get past the first four failed attempts!

[Red Teaming](https://blog.compass-security.com/category/red-teaming/)

[phishing](https://blog.compass-security.com/tag/phishing/)

[##### Previous post

Harvesting GitLab Pipeline Secrets](https://blog.compass-security.com/2024/12/harvesting-gitlab-pipeline-secrets/ "Previous post: Harvesting GitLab Pipeline Secrets")
[##### Next post

Hitchhiker’s Guide to Managed Security](https://blog.compass-security.com/2025/01/hitchhikers-guide-to-managed-security/ "Next post: Hitchhiker’s Guide to Managed Security")

### Recent Posts

* [Ensuring NIS2 Compliance: The Importance of Penetration Testing](https://blog.compass-security.com/2025/09/ensuring-nis2-compliance-the-importance-of-penetration-testing/)
* [Collaborator Everywhere v2](https://blog.compass-security.com/2025/09/collaborator-everywhere-v2/)
* [Taming The Three-Headed Dog -Kerberos Deep Dive Series](https://blog.compass-security.com/2025/09/taming-the-three-headed-dog-kerberos-deep-dive-series/)
* [Into the World of Passkeys: Practical Thoughts and Real-Life Use Cases](https://blog.compass-security.com/2025/08/into-the-world-of-passkeys-practical-thoughts-and-real-life-use-cases/)
* [xvulnhuntr](https://blog.compass-security.com/2025/07/xvulnhuntr/)

### Categories

Categories
Select Category
APT  (8)
Authentication  (18)
Bug Bounty  (6)
Entra ID  (3)
Evasion  (3)
Event  (34)
Exploiting  (18)
Forensic  (25)
Hacking-Lab  (18)
Hardening  (33)
Incident Response  (14)
Industrial Control Syste...