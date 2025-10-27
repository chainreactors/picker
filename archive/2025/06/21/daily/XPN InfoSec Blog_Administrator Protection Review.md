---
title: Administrator Protection Review
url: https://blog.xpnsec.com/administrator-protection/
source: XPN InfoSec Blog
date: 2025-06-21
fetch_date: 2025-10-06T22:53:22.224749
---

# Administrator Protection Review

[![avatar](/images/profile-image.jpg)](https://blog.xpnsec.com)
[XPN's InfoSec Blog](https://blog.xpnsec.com)

Adam Chester

Hacker and Infosec Researcher

## [XPN InfoSec Blog](https://blog.xpnsec.com "XPN InfoSec Blog")

[« Back to home](https://blog.xpnsec.com "Back to homepage")

# [Administrator Protection Review](/administrator-protection/)

Posted on

2025-06-20
Tagged in
[redteam](/tags#redteam), [windows](/tags#windows), [reversing](/tags#reversing)

# Windows Administrator Protection: A Red Team Analysis

I started researching Administrator Protection a few months back, but I must admit that I never really believed that it would ever make it to a release build of Windows in its current form.

Then I saw a post on BlueSky announcing that it is in-fact coming to Windows 11, and soon:

![](https://assets.xpnsec.com/administrator-protection/image1.webp)

In this post, I’ll be dumping my research into Windows Administrator Protection. There isn’t anything too groundbreaking here as I only touched this technology on a surface level for tooling compatibility testing, but the hope is that anyone else diving into this area will find the content useful.

**Note: Administrator Protection is still in active development and everything shown in this post is subject to change as this feature develops.**

## What is Admin Protection and Why Not Use UAC?

You can play around with Admin Protection on the canary build of Windows 11. I warn you in advance, you’ll see those elevation prompts more than before! And that’s by design; Microsoft created Administrator Protection to explicitly eliminate UAC backdoors, which means:

* **No EXE autoelevate backdoors**
* **No COM elevate backdoors**

These workarounds were implemented as a method of avoiding the UAC elevation prompt from appearing too often after users complained during Vista’s UAC debut. Microsoft has since reversed course by outwardly calling out the increase in elevation prompts in their release post:

> With Administrator protection, auto-elevation is removed. Users will notice an increase in consent prompts, though many fewer than the Vista days as much work has been done to clean up elevation points in most workflows.

So other than the removal of backdoors, what else separates Administrator Protection from UAC?

Well, the big one is that **split tokens are (mostly) gone**. Previously under UAC, there were two distinct token states. An administrative user would have a token in medium integrity with all administrative privileges and security groups stripped away. After the user consents to a UAC prompt (e.g., consent.exe) the system grants a high integrity token that restores all privileges and groups. The caveat here is in the filtering, as both tokens belonged to the same user account. In Admin Protection mode, you now have a completely separate admin account with a prefix of `admin_`. In the case of my Windows system, `xpn` has a corresponding `admin_xpn` account when I need the admin privileges and security groups typically granted to a high integrity token. In the Admin Protection world, this is called a **Shadow Admin account**.

## Existing Research

Before I dig too deep into this, I wanted to give a shoutout to Rudy Ooms at Call4Cloud. When I started looking into Shadow Admin accounts, [his was the first blog post](https://call4cloud.nl/local-administrator-protection-privilege-protection/) that I found and it covered Administrator Protection back in October 2024 in a lot of detail.

The reason that I continued beyond this post was because I wanted to understand the operational limitations and our tooling requirements for engagements (we like to be prepared). But I wanted to make it clear that Rudy’s post set the pace and is recommended reading.

Additionally, Microsoft released a detailed post called “[Introducing Administrator Protection](https://techcommunity.microsoft.com/blog/microsoft-security-blog/evolving-the-windows-user-model-%E2%80%93-introducing-administrator-protection/4370453)“.

There are sections from Microsoft’s post where “bypasses” were called out which were bugging me, mainly because I wanted to understand why known vulnerabilities still existed.

The reason that I also reference this is because it actually dives into a lot of details of the new functionality, including gaps in its implementation. Kudos for Microsoft being upfront about their design process.

## What Makes a Shadow Admin Account?

Administrator Protection revolves around the concept of a Shadow Admin account. If we take a look in the service account manager (SAM) hive, we see that the Shadow Admin is just a standard administrator account with a few additional attributes set against it:

![](https://assets.xpnsec.com/administrator-protection/image2.png)

It is actually the `ShadowAccountBackLink` key which links to the security identifier (SID) of the regular user account which determines if an account is classed as a shadow admin or not. Without this key being set, the account is just another admin account and is subject to token filtering.

We can see that this is the case in `samsrv.dll - SamrIsShadowAdminAccount`, which checks if this registry value is present:

![](https://assets.xpnsec.com/administrator-protection/image3.png)

We can use `samlib.dll - SamiIsShadowAdminAccount` programmatically to determine if a SID is a Shadow Admin account:

```
typedef NTSYSAPI NTSTATUS(*p_SamIsShadowAdminAccount)(
	PSID sid,
	void* out1,
	void* out2,
	void* out3
	);

void *modHandle = (void*)LoadLibraryA("samlib.dll");

p_SamIsShadowAdminAccount _SamIsShadowAdminAccount;
_SamIsShadowAdminAccount = (p_SamIsShadowAdminAccount)GetProcAddress((HMODULE)modHandle, "SamiIsShadowAdminAccount");

if (_SamIsShadowAdminAccount == NULL)
{
	std::cout << "Failed to get address of SamIsShadowAdminAccount\n";
	return 1;
}

void* out1 = NULL;
void* out2 = NULL;
void* out3 = NULL;

PSID sid;

// SID to check
if (ConvertStringSidToSidA("S-1-5-21-1524884646-3830121960-1456475082-1003", &sid) == 0) {
	std::cout << "ConvertStringSidToSid failed\n";
	return 1;
}

NTSTATUS status = _SamIsShadowAdminAccount(sid, &out1, &out2, &out3);
if (status != 0) {
	 printf("Cannot find SID\n");
	 return;
}

if (out1 != (void*)0) {
	  printf("This is a shadow admin account\n");
} else {
	  printf("Not a shadow admin account\n");
}
```

## How are Shadow Admin Accounts Created?

Shadow Admin accounts are actually created on first use. If we have a user named `build`, then `admin_build` will actually be created upon elevation.

To do this, Rudy Ooms notes that the `ShadowAdmin::CreateShadowAdminAccount` method is called from `samsrv.dll`.

From an RPC perspective, the entry method called is `SamrFindOrCreateShadowAdminAccount` and can be invoked with the `samlib.dll - SamiFindOrCreateShadowAdminAccount` API method:

```
typedef NTSYSAPI NTSTATUS(*p_SamiFindOrCreateShadowAdminAccount) (
	void* DomainHandle,
	void **out1,
	void** out2
);

void *modHandle = (void*)LoadLibraryA("samlib.dll");

p_SamiFindOrCreateShadowAdminAccount _SamFindOrCreateShadowAdminAccount;
_SamFindOrCreateShadowAdminAccount = (p_SamiFindOrCreateShadowAdminAccount)GetProcAddress((HMODULE)modHandle, "SamiFindOrCreateShadowAdminAccount");
if (_SamFindOrCreateShadowAdminAccount == NULL) {
	return 1;
}

void *modHandle = (void*)LoadLibraryA("samlib.dll");
if (modHandle == NULL) {
	return 1;
}

// SID to create ShadowAdmin account for
if (ConvertStringSidToSidA("S-1-5-21-3889136333-1358944941-3928491093-1001", &sid) == 0) {
	return 1;
}

void* arg1 = NULL;
void* arg2 = NULL;

NTSTATUS status = _SamFindOrCreateShadowAdminAccount((void*)(sid), &arg1, &arg2);
if (status != 0) {
	printf("SamiFindOrCreateShadowAdminAccount returned: %x\n", status3);
}
```

## How Do Users Get a Shadow Account Token?

As with UAC, `Consent.exe` is responsible for creating an access token for the Shadow Admin account. This is done via `LogonUserExExW`. And, as seen below, no password is passed:

![](https://a...