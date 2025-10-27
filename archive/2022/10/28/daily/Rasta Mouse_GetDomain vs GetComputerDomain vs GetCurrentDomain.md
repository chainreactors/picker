---
title: GetDomain vs GetComputerDomain vs GetCurrentDomain
url: https://rastamouse.me/getdomain-vs-getcomputerdomain-vs-getcurrentdomain/
source: Rasta Mouse
date: 2022-10-28
fetch_date: 2025-10-03T21:10:17.975133
---

# GetDomain vs GetComputerDomain vs GetCurrentDomain

[Rasta Mouse](https://rastamouse.me)

* [Home](https://rastamouse.me/)

27 Oct 2022

3 min read

[c#](/tag/c/)

# GetDomain vs GetComputerDomain vs GetCurrentDomain

Many Active Directory enumeration and post-exploitation tools need to figure out which domain they’re in or which domain they need to target. For convenience, PowerShell and C# tools can use the .NET `Domain` class from the `System.DirectoryService.ActiveDirectory` namespace. This class has several methods that can return a relevant Domain object, including `GetComputerDomain()` and `GetCurrentDomain()`.

This post will explore the consequence of using one over another in the scenarios of trying to enumerate and exploit domain/forest trusts. To set the scene, I built a small lab with two forests: `forest-a.local` and `forest-b.local`, and added a one-way trust so that users in FOREST-A may be authenticated in FOREST-B.

Let’s start with a simple example:

```
using System;
using System.DirectoryServices.ActiveDirectory;

var currentDomain = Domain.GetCurrentDomain();
var computerDomain = Domain.GetComputerDomain();

Console.WriteLine("Current Domain");
Console.WriteLine($"|_ Name: {currentDomain.Name}");
Console.WriteLine($"|_ PDC : {currentDomain.PdcRoleOwner.Name}");

Console.WriteLine();

Console.WriteLine("Computer Domain");
Console.WriteLine($"|_ Name: {computerDomain.Name}");
Console.WriteLine($"|_ PDC : {computerDomain.PdcRoleOwner.Name}");
```

When run as a user from FOREST-A on a computer in FOREST-A, both outputs are logically the same.

```
C:\>whoami && hostname
forest-a\administrator
dc-a

C:\>GetDomain.exe
Current Domain
|_ Name: forest-a.local
|_ PDC : dc-a.forest-a.local

Computer Domain
|_ Name: forest-a.local
|_ PDC : dc-a.forest-a.local
```

However, the trust relationship between FOREST-A & FOREST-B allows users from FOREST-A to authenticate to machines in FOREST-B. In which case, the current domain is returned as FOREST-A but the computer domain as FOREST-B.

```
C:\>whoami && hostname
forest-a\administrator
dc-b

C:\>GetDomain.exe
Current Domain
|_ Name: forest-a.local
|_ PDC : dc-a.forest-a.local

Computer Domain
|_ Name: forest-b.local
|_ PDC : dc-b.forest-b.local
```

We may also be running in FOREST-A and want to query FOREST-B directly across the trust. For cases like this, tools provide a `-Domain` (or similar) parameter. This is where `GetDomain` can come into play.

```
var context = new DirectoryContext(DirectoryContextType.Domain, args[0]);
var domain = Domain.GetDomain(context);

Console.WriteLine("Domain");
Console.WriteLine($"|_ Name: {domain.Name}");
Console.WriteLine($"|_ PDC : {domain.PdcRoleOwner.Name}");
```

```
C:\>whoami && hostname
forest-a\administrator
dc-a

C:\>GetDomain.exe forest-b.local
Domain
|_ Name: forest-b.local
|_ PDC : dc-b.forest-b.local
```

## Ok, so what?

Some tools don’t use a provided domain name in the way that you might expect – [StandIn](https://github.com/FuzzySecurity/StandIn) being one example. It has the ability to add new computers to a domain and does have a `--domain` parameter. However, the computer object isn’t created in the domain that you provide.

```
C:\>StandIn.exe --computer TEST --make --domain forest-b.local

[?] Using DC    : dc-a.forest-a.local
    |_ Domain   : forest-a.local
    |_ DN       : CN=TEST,CN=Computers,DC=forest-a,DC=local    <-- still in FOREST-A
    |_ Password : yEkBRdmJ6Eqajiu

[+] Machine account added to AD..
```

This is because it uses `Domain.GetComputerDomain()` to build the LDAP query. This means it will only ever create computers in the computer’s domain, despite us having the appropriate privilege in the target domain.

Here’s the start of the method in question:

```
public static void LDAPMakeMachineAccount(String sMachineName, String sDomain = "", String sUser = "", String sPass = "")
{
    try
    {
        Domain oDom = Domain.GetComputerDomain();    // this is the offending line
        String sPDC = oDom.PdcRoleOwner.Name;

        String sDomName = oDom.Name;
        String sDistName = "CN=" + sMachineName + ",CN=Computers";
```

A more flexible approach could be to check the `sDomain` parameter and if not null, use `GetDomain` instead.

```
Domain oDom;

if (string.IsNullOrWhiteSpace(sDomain))
{
    oDom = Domain.GetComputerDomain();
}
else
{
    var context = new DirectoryContext(DirectoryContextType.Domain, sDomain);
    oDom = Domain.GetDomain(context);
}

String sPDC = oDom.PdcRoleOwner.Name;
```

This time, the computer is created in the target domain.

```
C:\>StandIn.exe --computer TEST --make --domain forest-b.local

[?] Using DC    : dc-b.forest-b.local
    |_ Domain   : forest-b.local
    |_ DN       : CN=TEST,CN=Computers,DC=forest-b,DC=local    <-- FOREST-B, huzzah
    |_ Password : dBQ2Nr4WU6hSQlr

[+] Machine account added to AD..
```

## Closing

If you’re a tool author, it’s worth taking a step back to consider whether your method of resolving a domain makes sense for multiple scenarios. If you’re a tool user, this is handy to know in the event that you need to troubleshoot and make modifications on the fly.

### Published by:

[![Rasta Mouse](https://www.gravatar.com/avatar/2b44f5ca5458931c49e1fa57da6705c1?s=250&r=x&d=mp)](/author/rasta/ "Rasta Mouse")

Rasta Mouse © 2025

* [Sign up](#/portal/)

[Powered by Ghost](https://ghost.org/)