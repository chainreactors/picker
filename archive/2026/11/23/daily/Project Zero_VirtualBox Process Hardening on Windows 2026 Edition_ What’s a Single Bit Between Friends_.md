---
title: VirtualBox Process Hardening on Windows 2026 Edition: What’s a Single Bit Between Friends?
url: https://projectzero.google/2026/11/virtualbox-process-hardening.html
source: Project Zero
date: 2026-11-23
fetch_date: 2026-11-24T11:47:56.972844
---

# VirtualBox Process Hardening on Windows 2026 Edition: What’s a Single Bit Between Friends?

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

# VirtualBox Process Hardening on Windows 2026 Edition: What's a Single Bit Between Friends?

[2026-Nov-23](/2026/11/virtualbox-process-hardening.html "Permalink to this post")
James Forshaw

Back in 2017 I did some research into Oracle VirtualBox on Windows. Specifically I focussed on their mechanism to protect their VM processes from the user on the host. The protection was to gate who could open the kernel driver, which might allow for privilege escalation due to the way it was designed. At the time I found 3 ways of bypassing the protection, with an additional issue in COMâs runtime I reported in 2020. These issues were all written up in [this post](/2017/08/bypassing-virtualbox-process-hardening.html).

Fast forward to 2026 and I decided to look at VirtualBox again to see if much had changed. This time I found 3 new bypasses for protected processes, with an additional bug which was a broken fix for the 2020 bypass breaking due to changes in Windows.
In this blog post I want to focus on one specific issue [CVE-2026-87268](https://project-zero.issues.chromium.org/issues/544665516) which abused a feature of the .NET Framework which, when combined with the implementation of the DLL loader hooks implemented by VirtualBox, permitted a bypass of the checks and allowed me to load arbitrary code into the protected process. Letâs dig into the root cause of the issue in .NET first, before moving on to exploitation in VirtualBox.

### .NET Assembly Loading

The .NET Framework is interesting when it comes to bypassing process hardening as it supports loading assemblies from a memory buffer as long as you stick to only using managed code. This is obviously useful if the hardened process is maintained through verifying what DLLs can or cannot be loaded as it bypasses the traditional image mapping process. As the .NET runtime implementation is Microsoft signed, itâs usually permitted to load by any such checks.

The canonical way to load from a memory buffer is to use the [Assembly::Load](https://learn.microsoft.com/en-us/dotnet/api/system.reflection.assembly.load?view=net-10.0#system-reflection-assembly-load\(system-byte\(\)\)) static method which accepts a byte array. This does require you to run some .NET code first, or find a confused deputy to do the work for you. I used this API method to [bypass VirtualBox](https://project-zero.issues.chromium.org/issues/42450112) process hardening back in 2017, I was able to get to the API through the JScript script engine, culminating in me releasing the generic [DotNetToJScript](https://github.com/tyranid/dotnettojscript) tool.

Iâd always assumed this was the limit of bootstrapping arbitrary .NET from a memory buffer. If you tried to load a .NET assembly from a file itâd map it as an image section which would hit any DLL hardening checks and block an unsigned and untrusted binary from loading. However, in a âDohâ moment I realized Iâd never verified this behavior to be true, thus I decided to take a look.

The most important function to mapping a .NET assembly into memory seems to be `PEImageLayout::Map`, which is roughly the following in the version 4 of CLR.DLL which implements the runtime:

```
PEImageLayout *PEImageLayout::Map(HANDLE file) {
  PEImageLayout* image = new MappedImageLayout(file);
  if (!image->Image) {
    image = new FlatImageLayout(file);
  }
  if (image->Image) {
    if (!PEDecoder::CheckFormat(image->Image))
       ThrowWin32(ERROR_BAD_EXE_FORMAT);
  }
  return image;
}
```

What is interesting is this code creates a `MappedImageLayout` object based on the file. If that fails itâll fall back to using a different object, `FlatImageLayout`. The names kind of give away what theyâre doing, but just to be sure letâs look at the implementations of the constructors:

```
void MappedImageLayout::MappedImageLayout(HANDLE file) {
  HANDLE mapping = CreateFileMapping(file, nullptr, SEC_IMAGE | PAGE_READONLY);
  if (mapping) {
    this->Image = CLRMapViewOfFileEx(mapping);
  } else {
    if (GetLastError() != ERROR_BAD_EXE_FORMAT)
      ThrowLastError();
  }

  DWORD policy = 0;
  if (EEConfig::EnforceCodeIntegrity()
   || (SUCCEEDED(WldpGetLockdownPolicy(nullptr, &policy, nullptr))
   && !WLDP_LOCKDOWN_IS_OFF(policy) && !WLDP_LOCKDOWN_IS_CONFIG_CI(policy))
  ) {
     ThrowWin32(ERROR_BAD_EXE_FORMAT);
  }
  // ...
}
```

The constructor for `MappedImageLayout` uses the [CreateFileMapping](https://learn.microsoft.com/en-us/windows/win32/api/memoryapi/nf-memoryapi-createfilemappingw) API to convert the file handle into a section object. The code passes the `SEC_IMAGE` flag which instructs the kernel to assume the file is a PE executable and build an image section object including mapping in executable memory pages. Any protections which rely on verifying an imageâs signature or location can be notified and take appropriate action. However if the `CreateFileMapping` call fails the code checks if the last error was not `ERROR_BAD_EXE_FORMAT` and throws ending the load entirely.

An additional check is made here to check if âCode Integrityâ is enforced through the [Windows Lockdown Policy (WLDP)](https://learn.microsoft.com/en-us/windows/win32/api/wldp/) APIs. This checks for the â[Dynamic Code Security](https://learn.microsoft.com/en-us/windows/security/application-security/application-control/app-control-for-business/design/appcontrol-and-dotnet#app-control-and-net-dynamic-code-security-hardening)â code integrity policy being enabled or if a [User Mode Code Integrity (UMCI)](https://learn.microsoft.com/en-us/windows/security/application-security/application-control/app-control-for-business/design/select-types-of-rules-to-create#:~:text=Valid%20supplemental%20option-,0,-Enabled%3AUMCI) policy is enforced. If it is then an error is thrown ending the loading process. Weâll come back to this check when it becomes relevant.

Assuming the mapping fails with the `ERROR_BAD_EXE_FORMAT` error, then the loading process continues, creating a `FlatImageLayout` object instead:

```
void FlatImageLayout::FlatImageLayout(HANDLE file) {
  HANDLE mapping = CreateFileMapping(file, nullptr, PAGE_READONLY);
  if (mapping) {
    this->Image = CLRMapViewOfFileEx(mapping);
  } else {
    ThrowLastError();
  }
  // ...
}
```

This constructor is simpler, it just calls `CreateFileMapping` without the `SEC_IMAGE` flag. Therefore the file is mapped into memory as a data only section. Thereâs no executable pages, but that doesnât matter for .NET. The final check, back in the first code snippet verifies that the PE file is valid with a call to `PEDecoder::CheckFormat`, throwing if itâs not valid.

The take away from this is if we can get .NET to load a valid assembly file, but cause the first call to `CreateFileMapping` to fail with the `ERROR_BAD_EXE_FORMAT` error we can get it to execute the file from memory. Any protection code which is expecting to check the loaded image section will not see the load and untrusted arbitrary code would be executed.

Note this behavior only seems to work on .NET Framework v4, not the older .NET Framework such as v3.5 and v2. From what I can tell in the earlier frameworks, while this check can be bypassed in the same way and the `FlatImageLayout` object created, the runtime passes the assembly to the `LoadLibrary` API later in the loading process where it will fail to load. I didnât spend much time checking if this was bypassable, as the older .NET Frameworks are no longer installed ...