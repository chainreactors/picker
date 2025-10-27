---
title: LAPS 2.0 Internals
url: https://blog.xpnsec.com/LAPSv2-Internals/
source: XPN InfoSec Blog
date: 2023-08-14
fetch_date: 2025-10-04T11:59:12.050101
---

# LAPS 2.0 Internals

[![avatar](/images/profile-image.jpg)](https://blog.xpnsec.com)
[XPN's InfoSec Blog](https://blog.xpnsec.com)

Adam Chester

Hacker and Infosec Researcher

## [XPN InfoSec Blog](https://blog.xpnsec.com "XPN InfoSec Blog")

[« Back to home](https://blog.xpnsec.com "Back to homepage")

# [LAPS 2.0 Internals](/LAPSv2-Internals/)

Posted on

2023-08-13
Tagged in
[windows](/tags#windows), [payload](/tags#payload), [laps](/tags#laps)

For most security consultant out there working with Windows environments, you’ve probably found yourself writing the same recommendation over the years:

“Shared local Administrator password… Deploy LAPS”

This year, LAPS 2.0 was released by Microsoft, and thankfully it now comes built-in to Windows. This time it comes ready for use with Active Directory, as well as being supported in Azure AD aka Entra ID. In this post, we’ll expand on a Twitter thread that I posted on how LAPS 2.0 for Active Directory works under the hood, so you can make those fresh recommendations to your clients, and prepare yourself for the inevitable question: “But we just deployed LAPS.. what does LAPS 2.0 do differently?!”.

## Lab Setup

Before we can explore LAPS 2.0, we’ll need a lab. Let’s set up a quick environment to play around with.

To set up LAPS 2.0 in Active Directory, we need to make sure we are running the April 2023 security update. We can enable the support through Group Policy in `Computer Settings` -> `Administrative Templates` -> `System` -> `LAPS`.

We need to set `Configure password backup directory` to `Active Directory` to enable LAPS, and we’ll enable `Enable Password Encryption` to take advantage of the new password encryption option:

![](https://assets.xpnsec.com/lapsv2-internals/image1.png)

Next, we need to update the AD schema using the PowerShell command `Update-LAPSADSchema`:

![](https://assets.xpnsec.com/lapsv2-internals/image2.png)

To allow computers to manage their newly created LDAP records for LAPS, we create a new OU which we will call `LAPSManaged` and add in any computer objects which should be handled by LAPS.

To grant access to the OU container to computers when handling LAPS, we use:

```
Set-LapsADComputerSelfPermission -Identity OU=LAPSManaged,DC=lab,DC=local
```

![](https://assets.xpnsec.com/lapsv2-internals/image3.png)

With permission now granted to computer accounts within the OU, we use the `Reset-LAPSPassword` cmdlet to force a password to be added to LAPS 2.0 in AD:

![](https://assets.xpnsec.com/lapsv2-internals/image4.png)

Then we can use `Get-LAPSADPassword` to retrieve the password:

![](https://assets.xpnsec.com/lapsv2-internals/image5.png)

That should be enough to get us started, now to reversing!

## Reversing LAPS 2.0

We know from above that `Get-LapsADPassword` has the ability to retrieve plaintext LAPS 2.0 passwords, so it stands to reason that we would start there.

And as we’re dealing with PowerShell, we’ll fire up dnSpy. The DLL we need is found in:

```
C:\Windows\System32\WindowsPowerShell\v1.0\Modules\LAPS
```

Specifically we’ll need the `lapspsh.dll` assembly.

If we search for the `Get-LAPSADPassword` cmdlet, we’ll find a class called `Microsoft.Windows.LAPS.GetLapsADPassword`:

![](https://assets.xpnsec.com/lapsv2-internals/image7.png)

In this class, we have the method `ProcessOneIdentity` which contains the logic for retrieving the LAPS 2.0 credentials from LDAP:

![](https://assets.xpnsec.com/lapsv2-internals/image8.png)

The call to `GetPasswordAttributes` shows the LDAP queries being used to query AD for passwords:

![](https://assets.xpnsec.com/lapsv2-internals/image9.png)

From this method we find several new LDAP attributes being retrieved, but the ones that stand out for us are:

* `msLAPS-EncryptedPassword`
* `msLAPS-Password`

One of the new features of LAPS 2.0 is the support for encrypted credentials. Previously credentials for LAPS were stored in the plain-text attribute `ms-Mcs-AdmPwd`, but now it seems that that `msLAPS-EncryptedPassword` hosts the encrypted credentials, leaving `msLAPS-Password` to host the plain-text password if encryption hasn’t been enabled in Group Policy.

To decrypt the stored passwords, there is a call being made to `BuildPasswordInfoFromEncryptedPassword` which again signals from the debug output that we are in the correct place:

![](https://assets.xpnsec.com/lapsv2-internals/image10.png)

The method `ParseAndDecryptDirectoryPassword` is passed the encrypted data retrieved from the `msLAPS-EncryptedPassword` attribute:

![](https://assets.xpnsec.com/lapsv2-internals/image11.png)

Reviewing this method, we find that the first 16 bytes are used as a “prefix”. The fields in this prefix are:

* Bytes 0 - 3 = Upper Date Time Stamp
* Bytes 4 - 7 = Lower Date Time Stamp
* Bytes 8 - 11 = Encrypted Buffer Size
* Bytes 12 - 15 = Flags

The method then skips over this 16 byte prefix, and decrypts the remaining contents using the method `DecryptBytesHelper`.

`DecryptBytesHelper` is just a wrapper to invoke the function `DecryptNormalMode`, which is present in another DLL:

![](https://assets.xpnsec.com/lapsv2-internals/image12.png)

To reverse this DLL, we need to transition over to Ghidra for disassembly, as these methods are defined in native DLL’s rather than .NET.

Looking at the exported `DecryptNormalMode` function, we see that this is a wrapper around calls to `NCrypt` where the encrypted blob passed from .NET is decrypted:

![](https://assets.xpnsec.com/lapsv2-internals/image13.png)

The decrypted content is then returned to .NET where it is parsed as JSON and the password is recovered:

![](https://assets.xpnsec.com/lapsv2-internals/image14.png)

## Recovery with .NET

Hopefully with this quick walkthrough you can see how we can recreate the process using a standalone .NET tool which will pull down and decrypt LAPS 2.0 credentials.

The first thing that we do is retrieve the LDAP entry:

```
string filter = string.Format("(&(objectClass={0})({1}={2}))", "computer", "distinguishedName", dn);

// Create a new ldap connection
LdapConnection ldapConnection = new LdapConnection(dc);
ldapConnection.SessionOptions.ProtocolVersion = 3;
ldapConnection.Bind();

SearchRequest searchRequest = new SearchRequest(dn, filter, SearchScope.Base, attributeList);

SearchResponse searchResponse = ldapConnection.SendRequest(searchRequest) as SearchResponse;

SearchResultEntry searchResultEntry = searchResponse.Entries[0];
if (searchResponse.Entries.Count != 1)
{
    Console.WriteLine("[!] Could not find computer object");
    return;
}
```

Once we’ve pulled down the LDAP record, we need to actually decrypt the LAPS 2.0 attribute value. We know that Microsoft are using the NCrypt calls to decrypt the content via `lapsutil.dll`, but we’ll just use P/Invoke from .NET rather than calling out to an unmanaged DLL (there is also nothing stopping you from just using the `lapsutil.dll` if you want):

```
[DllImport("ncrypt.dll")]
public static extern uint NCryptStreamOpenToUnprotect(in NCRYPT_PROTECT_STREAM_INFO pStreamInfo, ProtectFlags dwFlags, IntPtr hWnd, out IntPtr phStream);

[DllImport("ncrypt.dll")]
public static extern uint NCryptStreamUpdate(IntPtr hStream, IntPtr pbData, int cbData, [MarshalAs(UnmanagedType.Bool)] bool fFinal);

[DllImport("ncrypt.dll")]
public static extern uint NCryptUnprotectSecret(out IntPtr phDescriptor, Int32 dwFlags, IntPtr pbProtectedBlob, uint cbProtectedBlob, IntPtr pMemPara, IntPtr hWnd, out IntPtr ppbData, out uint pcbData);
```

By calling the NCrypt API from .NET, we can just decrypt the contents directly:

```
uint ret = Win32.NCryptStreamOpenToUnprotect(info, ProtectFlags.NCRYPT_SILENT_FLAG, IntPtr.Zero, out handle);
if (ret == 0)
{
    IntPtr alloc = Marshal.AllocHGlobal(encryptedPass.Length);
    Marshal.Copy(encryptedPass, 16, alloc, encryptedPass.Length - 16);

    // Get the authorized decryptor of the blob
    ret = Win32.NCryptUnprotectSecret(out handle2, 0x41, alloc, (uint)encryptedPass.Length - 16, IntPtr.Z...