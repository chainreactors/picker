---
title: Windows Tooling Updates: OleView.NET
url: https://googleprojectzero.blogspot.com/2024/12/windows-tooling-updates-oleviewnet.html
source: Project Zero
date: 2024-12-13
fetch_date: 2025-10-06T19:37:09.437780
---

# Windows Tooling Updates: OleView.NET

# [Project Zero](https://googleprojectzero.blogspot.com/)

News and updates from the Project Zero team at Google

## Thursday, December 12, 2024

### Windows Tooling Updates: OleView.NET

Posted by James Forshaw, Google Project Zero

This is a short blog post about some recent improvements I've been making to the [OleView.NET](http://oleview.net) tool which has been released as part of version 1.16. The tool is designed to discover the attack surface of Windows COM and find security vulnerabilities such as privilege escalation and remote code execution. The updates were recently presented at the Microsoft Bluehat conference in Redmond under the name "[DCOM Research for Everyone!](https://github.com/tyranid/infosec-presentations/blob/master/Bluehat/2024/DCOM%2520Research%2520for%2520Everyone%21.pdf)". This blog expands on the topics discussed to give a bit more background and detail that couldn't be fit within the 45-minute timeslot. This post assumes a knowledge of COM as I'm only going to describe a limited number of terms.

## Using the [OleView.NET](http://oleview.net) Tooling

Before we start the discussion it's important to understand how you can get hold of the [OleView.NET](http://oleview.net) tool and some basic usage. The simplest way to get the tooling is to install it from the PowerShell gallery with the Install-Module OleViewDotNet command. This installs both the PowerShell module and the GUI.

Next you need to parse the COM registration artifacts into an internal database. You can do this by running the Get-ComDatabase command. Once it's finished you're ready to go. You will notice that it can take a long time to complete, so it'd be annoying to have to do this every time you want to start researching. For that reason you can use the command Set-ComDatabase -Default to write out the database to a default storage location. Now the next time you start PowerShell you can just run an inspection command, such as Get-ComClass and the default database will be automatically loaded.

This default database is also shared with the GUI, which you can start by running the Show-ComDatabase command. For general research I find the GUI to be easier to use and you can click around and look at the COM registration information. For analysis, the ability to script through PowerShell is more important.

## Researching COM Services

Performing security research in COM usually involves the following steps::

* Enumerate potential COM classes of interest. These might be classes which are accessible outside of a sandbox, running at high privilege or designed to be remotely exposed.
* Validate whether the COM classes are truly accessible from the attack position. COM has various security controls which determine what users can launch, activate and access an object. Understanding these security controls allows the list of COM classes of interest to be limited to only those that are actually part of the attack surface.
* Enumerate exposed interfaces, determine what they do and call methods on them to test for security vulnerabilities.

The last step is the focus of the updates to the tooling, making it easier to determine what an exposed interface does and call methods to test the behavior. The goal is to minimize the amount of reverse engineering needed (although generally some is still required) as well as avoid needing to write code outside of the tooling to interact with the COM service under test.

To achieve this goal, [OleView.NET](http://oleview.net) will pull together any sources of interface information it has, then provide a mechanism to inspect and invoke methods on the interface through the UI or via PowerShell. The sources of information that it currently pulls together are:

1. Known interfaces, either defined in the base .NET framework class libraries or inside [OleView.NET](http://oleview.net).
2. COM interface definitions present in the Global Assembly Cache.
3. Registered type libraries.
4. Windows Runtime interfaces.
5. Extracted proxy class marshaling information.

One useful benefit of gathering this information, is that the tool formats the interface as "source code" so you can manually inspect it.

## Formatting Interfaces Definitions

The [OleView.NET](http://oleview.net) tool uses a database object to represent all the artifacts it has analyzed on your system. The latest released version defines some of these objects to be convertible to "source code". For example the following can be converted if the tool can determine some meta data that to represent the artifact:

* COM interfaces
* COM proxies
* COM Windows Runtime classes.
* Type libraries, interfaces and classes.

How you get to this conversion depends on whether you're using the PowerShell or the UI. The simplest approach is PowerShell, using the ConvertTo-ComSourceCode command. For example, the following will convert an interface object into source code:

PS> Get-ComInterface -Name IMyInterface | ConvertTo-ComSourceCode -Parse

Note that we also need to pass a -Parse option to the command. Some metadata such as type libraries and proxies can be expensive to parse so it won't do that automatically. However, once they're been parsed in the current session the metadata is cached for further use, so for example if you formatted a single interface in a type library, all other interfaces are now also parsed and can be formatted.

The output of this command is the converted "source code" as text. The format depends on metadata source. For example the following is the output from a Windows Runtime type:

[Guid("155eb23b-242a-45e0-a2e9-3171fc6a7fdd")]

interface IUserStatics

{

    /\* Methods \*/

    UserWatcher CreateWatcher();

    IAsyncOperation<IReadOnlyList<User>> FindAllAsync();

    IAsyncOperation<IReadOnlyList<User>> FindAllAsync(UserType type);

    IAsyncOperation<IReadOnlyList<User>> FindAllAsync(UserType type,

                                       UserAuthenticationStatus status);

    User GetFromId(string nonRoamableId);

}

As Windows Runtime types are defined using metadata similar to .NET then the output is a pseudo C# format. In contrast for type library or proxy it's look more like the following:

[

    odl,

    uuid(00000512-0000-0010-8000-00AA006D2EA4),

    dual,

    oleautomation,

    nonextensible

]

interface \_Collection : IDispatch {

    [id(1), propget]

    HRESULT Count([out, retval] int\* c);

    [id(0xFFFFFFFC), restricted]

    HRESULT \_NewEnum([out, retval] IUnknown\*\* ppvObject);

    [id(2)]

    HRESULT Refresh();

};

This is in the Microsoft Interface Definition Language (MIDL) format, the type library version should be pretty accurate and could even be recompiled by the MIDL compiler. For proxies some of the information is lost and so the MIDL generated isn't completely accurate, but as we'll see later there's limited reasons to take the output and recompile.

Another thing to note is that proxies lose name information when compiled from MIDL to their C marshaled representation. Therefore the tool just generates placeholder names, for example, method names are of the form "ProcN". If the proxy is for a type that has a known definition, such as from a Windows Runtime type or a type library then the tool will try and automatically apply the names. If not, you'll need to manually change them if you want them to be anything other than the default.

You can change the names from PowerShell by modifying the proxy object directly. For example the "IBitsTest1" interface looks like the following before doing anything:

[

  object,

  uuid(51A183DB-67E0-4472-8602-3DBC730B7EF5),

]

interface IBitsTest1 : IUnknown {

    HRESULT Proc3([out, string] wchar\_t\*\* p0);

}

You can modify "Proc3" with the following script:

PS> $proxy = Get-ComProxy -Iid 51A183DB-67E0-4472-8602-3DBC730B7EF5

PS> $proxy.Procedures[0].Name = "GetBitsDllPath"

PS> $proxy.Procedures[0].Parameters[0].Name = "DllPath"

Now the formatted output looks like the following:
...