---
title: Fooling the Sandbox: A Chrome-atic Escape
url: https://starlabs.sg/blog/2025/07-fooling-the-sandbox-a-chrome-atic-escape/
source: Blogs on STAR Labs
date: 2025-07-11
fetch_date: 2025-10-06T23:24:34.393177
---

# Fooling the Sandbox: A Chrome-atic Escape

[![logo](https://starlabs.sg/logo-white.png)](https://starlabs.sg/ "  (Alt + H)")

* [Home](https://starlabs.sg/ "Home")
* [About](https://starlabs.sg/about/ "About")
* [Advisories](https://starlabs.sg/advisories/ "Advisories")
* [Blog](https://starlabs.sg/blog/ "Blog")
* [Achievements](https://starlabs.sg/achievements/ "Achievements")
* [Publications](https://starlabs.sg/publications/ "Publications")
* [Search](https://starlabs.sg/search/ "Search (Alt + /)")

[Home](https://starlabs.sg/) » [Blogs](https://starlabs.sg/blog/)

# Fooling the Sandbox: A Chrome-atic Escape

July 10, 2025 · 11 min · Vincent Yeo (@goatmilkkk)

Table of Contents

* [The Hunt Begins: Finding the Trigger for CVE-2024-30088](#the-hunt-begins-finding-the-trigger-for-cve-2024-30088)
* [Down the Rabbit Hole: Following the Breadcrumbs](#down-the-rabbit-hole-following-the-breadcrumbs)
* [The Eureka Moment: Understanding the Race](#the-eureka-moment-understanding-the-race)
* [Weaponizing the Discovery](#weaponizing-the-discovery)
* [Entering Chrome Renderer Sandbox](#entering-chrome-renderer-sandbox)
  + [Roadblock #1: The Integrity Police](#roadblock-1-the-integrity-police)
    - [Solution: Breaking the Security Descriptor](#solution-breaking-the-security-descriptor)
    - [The Precision Surgery Problem](#the-precision-surgery-problem)
  + [Roadblock #2: The Job Object Prison](#roadblock-2-the-job-object-prison)
    - [Solution: The Great Escape](#solution-the-great-escape)
  + [Demo](#demo)
  + [Summary](#summary)
  + [Afterthoughts](#afterthoughts)

For my internship, I was tasked by my mentor Le Qi to analyze CVE-2024-30088, a double-fetch race condition bug in the Windows Kernel Image `ntoskrnl.exe`. A public POC demonstrating EoP from Medium Integrity Level to SYSTEM is available on GitHub [here](https://github.com/tykawaii98/CVE-2024-30088).

Additionally, I was challenged (more like forced 💀) to chain the exploit to escape the Chrome Renderer Sandbox, achieving EoP from Untrusted Integrity Level to SYSTEM.

*Easy, right?* 🤡

Note: CVE-2024-30088 came out [before 24H2](https://windows-internals.com/kaslr-leaks-restriction/), so I analyzed it using a 23H2 Windows VM instead

## The Hunt Begins: Finding the Trigger for CVE-2024-30088[#](#the-hunt-begins-finding-the-trigger-for-cve-2024-30088)

The bug can be triggered from `NtQueryInformationToken` when its `TokenInformationClass` field is set to the `TOKEN_ACCESS_INFORMATION` constant. At first glance, this function looks completely innocent, just letting processes retrieve information about access tokens if it has the appropriate access rights:

```
__kernel_entry NTSYSCALLAPI NTSTATUS NtQueryInformationToken(
  [in]  HANDLE                  TokenHandle,
  [in]  TOKEN_INFORMATION_CLASS TokenInformationClass,
  [out] PVOID                   TokenInformation, // usermode buffer
  [in]  ULONG                   TokenInformationLength,
  [out] PULONG                  ReturnLength
);
```

* This is a read function, but that does not mean we cannot achieve arbitrary write with it
* For TOCTOU, it’s important to trace `TokenInformation` since it is a buffer that can be controlled by the user
  + **Take note of when the kernel writes to it**

## Down the Rabbit Hole: Following the Breadcrumbs[#](#down-the-rabbit-hole-following-the-breadcrumbs)

Looking through the switch case for the `TOKEN_ACCESS_INFORMATION` constant in `NtQueryInformationToken`, only `SepCopyTokenAccessInformation` stood out to me since it was the only function that takes in `TokenInformation` (the user-supplied buffer) as an argument.

```
NtQueryInformationToken( ... ) {

    ...

    case TokenAccessInformation: // case 22

        ...

        if ( v5 < TokenAccessInformationBufferSize )
        goto LABEL_58;
        SepCopyTokenAccessInformation(
            v30,
            userBuffer, // TokenInformation field
            v5,
            v147,
            v157,
            Handle,
            v156,
            v155,
            v154,
            v153,
            v152,
            v151,
            v150,
            v110,
            v109);

       ...

}
```

Following `SepCopyTokenAccessInformation`, I discovered it copies a bunch of data about the token into the user buffer before calling `AuthzBasepQueryInternalSecurityAttributesToken` to copy over the security attributes of the token object.

```
__int64 __fastcall SepCopyTokenAccessInformation(
        _TOKEN *Token,
        _TOKEN_ACCESS_INFORMATION *userBuffer,
        UINT64 userBufferLength,
        UINT64 PrivilegeCount,
        UINT64 GroupsLength,
        UINT64 GroupsSALength,
        UINT64 RestrictedSidsLength,
        UINT64 RestrictedSidsSALength,
        UINT64 PackageSidLength,
        UINT64 CapabilitySidsLength,
        UINT64 CapabilitySidsSALength,
        UINT64 TrustSidLength,
        UINT64 SecurityAttributesLength,
        UINT8 UseNewTrust,
        void *NewTrustSid) {

	...

    userBuffer->AuthenticationId = Token->AuthenticationId; // copy over some token data
    v16 = PrivilegeCount;
    userBuffer->TokenType = Token->TokenType;
    userBuffer->ImpersonationLevel = Token->ImpersonationLevel;
    userBuffer->Flags = Token->TokenFlags;
    userBufferEnd = userBuffer + userBufferLength;

    ...

    AuthzBasepQueryInternalSecurityAttributesToken(
        Token->pSecurityAttributes,
        userBufferSecurityAttributes, // copy over token security attributes
        userBufferEnd - userBufferSecurityAttributes,
        &v38
    );
    v36 = &userBufferSecurityAttributes[SecurityAttributesLength];
    userBuffer->SecurityAttributes = userBufferSecurityAttributes;
	return SepConvertTokenPrivilegesToLuidAndAttributes(Token, v36->Privileges);

  }
```

Then, `AuthzBasepQueryInternalSecurityAttributesToken` calls `AuthzBasepCopyoutInternalSecurityAttributes`, which is where the bug can be found.

```
__int64 __fastcall AuthzBasepQueryInternalSecurityAttributesToken(
        _AUTHZBASEP_SECURITY_ATTRIBUTES_INFORMATION *tokenSecurityAttributes,
        _DWORD *userBufferSecurityAttributes,
        unsigned int securityAttributesSize,
        unsigned int *a4) {

	...

        result = AuthzBasepCopyoutInternalSecurityAttributes( // bug in here
        tokenSecurityAttributes,
        userBufferSecurityAttributes,
        securityAttributesSize);

	...

}
```

## The Eureka Moment: Understanding the Race[#](#the-eureka-moment-understanding-the-race)

The bug occurs when the `_UNICODE_STRING` struct in `TokenObject->SecurityAttributesList` gets copied over to the user buffer.

```
typedef struct _UNICODE_STRING {
  USHORT Length;
  USHORT MaximumLength;
  PWSTR  Buffer; // note: this is a pointer to the string (not the string itself!)
} UNICODE_STRING, *PUNICODE_STRING;
```

Particularly, it emerges due to the following sequence of operations:

1. Kernel stores a pointer `pBuffer` inside the user buffer
2. Kernel copies a string to the memory pointed to by `pBuffer`

```
__int64 __fastcall AuthzBasepCopyoutInternalSecurityAttributes(
        _AUTHZBASEP_SECURITY_ATTRIBUTES_INFORMATION *tokenSecAttr,
        int *userBufferSecurityAttributes,
        unsigned int a3) {

    ...

    ADJ(offsetToUserBuffer)->unicodeString.MaximumLength = maxLength;
    ADJ(offsetToUserBuffer)->unicodeString.Length = 0;
    ADJ(offsetToUserBuffer)->unicodeString.Buffer = pBuffer; // [1] specify addr to write to
    RtlCopyUnicodeString(&ADJ(offsetToUserBuffer)->unicodeString, (SA_Entry + 0x20)); // [2] copy over string

    v9 = AuthzBasepCopyoutInternalSecurityAttributeValues(SA_Entry, offsetToUserBuffer - 104, v18, v6 - v18, &v20);
    if ( (v9 & 0x80000000) != 0 )
    goto LABEL_18;

    ...

}
```

Between steps [1] and [2], we can use a racing thread to change `pBuffer` (the address the kernel writes to), obtaining a partial write primitive.

## Weaponizing the Discovery[#](#weaponizing-the-discovery)

Since there are already public POCs out there, I will just describe the exploit process at a high...