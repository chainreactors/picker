---
title: Environment… is variable
url: https://www.hexacorn.com/blog/2022/12/02/environment-is-variable/
source: Hexacorn
date: 2022-12-03
fetch_date: 2025-10-04T00:23:18.292665
---

# Environment… is variable

[Skip to primary content](#content)

# [Hexacorn](https://www.hexacorn.com/blog/)

## Hexacorn

Search

### Main menu

* [Home](https://www.hexacorn.com/)
* [Services](https://www.hexacorn.com/services.html)
* [Products & Freebies](https://www.hexacorn.com/products_and_freebies.html)
* [Case Studies](https://www.hexacorn.com/case_studies.html)
* [Contact Us](https://www.hexacorn.com/contact.html)

### Post navigation

[← Previous](https://www.hexacorn.com/blog/2022/11/19/cracking-zeppelin/)
[Next →](https://www.hexacorn.com/blog/2022/12/03/using-make_sc_hash_db-py-to-create-api-hashing-dbs/)

# Environment… is variable

Posted on [2022-12-02](https://www.hexacorn.com/blog/2022/12/02/environment-is-variable/ "11:15 pm")  by  [adam](https://www.hexacorn.com/blog/author/adam/ "View all posts by adam")

I love environmental variables. They are often [post-worthy](https://www.google.com/search?q=site:hexacorn.com+environment+variables), and sometimes they are just simply [cool](https://www.hexacorn.com/blog/2019/05/26/plata-o-plomo-code-injections-execution-tricks/).

Yet, many are still not known. Many are still not described.

Looking for ‘easy’ research targets inside the Windows directory one can scan executables and DLLs looking for either a string or an import reference to the functions that operate on Environment variables:

* RtlSetEnvironmentVariable
* setenv
* SetEnvironmentVariable
* GetEnv
* GetEnvironmentVariable
* ExpandEnvironment

These produce really interesting hits!

Looking at the code of puiobj.dll (PrintUI Objects DLL) we can find a weirdly named environment variable F2ED815E-5F18-4860-A8F2-16471D53C5CF that takes a integer value that seems to be a flag controlling how printer queue jobs are presented.

Looking at curl.exe we see the familiar [CURL\_HOME](https://everything.curl.dev/cmdline/configfile) reference that can alter the way curl works (configuration file location).

The xcopy.exe takes into consideration the value of COPYCMD.

In 2022 no one remembers mswsock.dll, but it also uses environment variables:

* SanTcpBypass
* SanResizeDisable
* SanRecvPollCount

The same goes for oleaut32.dll:

* [OANOCACHE](https://www.betaarchive.com/wiki/index.php/Microsoft_KB_Archive/139071#Set_the_OANOCACHE_environment_variable)
* [OAPERUSERTLIBREG](https://learn.microsoft.com/en-us/windows/win32/api/oleauto/nf-oleauto-oaenableperusertlibregistration)
* [OACACHEPARAMS](https://www.betaarchive.com/wiki/index.php/Microsoft_KB_Archive/937360#OACACHEPARAMS_variable_instructions)

Many of environment variable tricks are known by now. Today I posted on [Twitter](https://twitter.com/Hexacorn/status/1598665412081700865) and [Mastodon](https://infosec.exchange/%40hexacorn/109444263329952725) about the use of environment variables inside the LNK files which — while not really being a proper evasion since the shell functions are processed within a context of executing process — may give some new opportunities to attackers too.

But there is always more…

Environment variables are very, very prevalent and all over the place. Many of them are kinda invisible, f.ex. many batch files and the aforementioned LNK files rely a lot them, and many of them are batch-file specific, often used internally and not very well documented.

Here’s a snapshot of various environment variables (many of which are not very well known, I think) present inside the LNK and BAT files on a win10 system with a Visual Studio, Bon Jour, NPCAP, Powershell and Python present:

* %ARGS%
* %AUT%
* %AUTDIR%
* %CABOUTPUT%
* %CD%
* %CLIENTPATH%
* %CRT%
* %CURRDIR%
* %CabOutput%
* %CommandPromptType%
* %CommonProgramFiles%
* %DEVENVDIR%
* %DIR%
* %DIRECTIVEFILE%
* %DevEnvDir%
* %DoDump%
* %Dot11Support%
* %ERRORLEVEL%
* %ExtensionSDKDir%
* %FSHARPINSTALLDIR%
* %Framework40Version%
* %FrameworkDIR32%
* %FrameworkDIR64%
* %FrameworkDir%
* %FrameworkDir32%
* %FrameworkDir64%
* %FrameworkVersion%
* %FrameworkVersion32%
* %FrameworkVersion64%
* %HOMEDRIVE%
* %HOMEPATH%
* %IFCPATH%
* %INCLUDE%
* %KEY\_NAME%
* %LEGACY\_MACHINE\_SETUP\_LOGS\_PATH%
* %LIB%
* %LIBPATH%
* %LOCALAPPDATA%
* %LoopbackAdapter%
* %MACHINE\_AMD64\_SETUP\_LOGS\_PATH%
* %MACHINE\_I386\_SETUP\_LOGS\_PATH%
* %NETFXSDKDir%
* %NPCAP\_DIR%
* %OUTPUTDIR%
* %OutputDir%
* %PATH%
* %PERMACHINECLIENTPATH64%
* %PERMACHINECLIENTPATH86%
* %PERMACHINE\_START\_MENU\_PATH%
* %PERUSER\_START\_MENU\_PATH%
* %PROCESSOR\_ARCHITECTURE%
* %PROGRAMDATA%
* %PROMPT%
* %PYTHONHOME%
* %ProgramFiles%
* %ProgramW6432%
* %RANDOM%
* %RETURNCODE%
* %SDK%
* %SENDMAIL%
* %SID%
* %SQUISHRUNNER%
* %SQUISHSERVER%
* %START\_TYPE%
* %ScriptName%
* %SendMail%
* %SyncLogsExclude%
* %SyncSettingsExclude%
* %SystemRoot%
* %TARGET%
* %TEMP%
* %TEMPFILE%
* %TESTCASE%
* %TESTSUITE%
* %TEST\_INCLUDE%
* %TEST\_LIB%
* %TMP%
* %UCRTVersion%
* %USERPROFILE%
* %UniversalCRTSdkDir%
* %VCIDEInstallDir%
* %VCINSTALLDIR%
* %VCLIB\_GENERAL\_OVERRIDE%
* %VCToolsInstallDir%
* %VCToolsVersion%
* %VCVARS\_USER\_VERSION%
* %VC\_ATLMFC\_IncludePath%
* %VC\_ExecutablePath\_ARM\_ARM%
* %VC\_ExecutablePath\_ARM\_ARM64%
* %VC\_ExecutablePath\_ARM\_x64%
* %VC\_ExecutablePath\_ARM\_x86%
* %VC\_ExecutablePath\_x64\_ARM%
* %VC\_ExecutablePath\_x64\_ARM64%
* %VC\_ExecutablePath\_x64\_x64%
* %VC\_ExecutablePath\_x64\_x86%
* %VC\_ExecutablePath\_x86\_ARM%
* %VC\_ExecutablePath\_x86\_ARM64%
* %VC\_ExecutablePath\_x86\_x64%
* %VC\_ExecutablePath\_x86\_x86%
* %VC\_IFCPath%
* %VC\_LibraryPath\_ATL\_ARM%
* %VC\_LibraryPath\_ATL\_ARM64%
* %VC\_LibraryPath\_ATL\_ARM64EC%
* %VC\_LibraryPath\_ATL\_ARM64EC\_spectre%
* %VC\_LibraryPath\_ATL\_ARM64\_spectre%
* %VC\_LibraryPath\_ATL\_ARM\_spectre%
* %VC\_LibraryPath\_ATL\_x64%
* %VC\_LibraryPath\_ATL\_x64\_spectre%
* %VC\_LibraryPath\_ATL\_x86%
* %VC\_LibraryPath\_ATL\_x86\_spectre%
* %VC\_LibraryPath\_VC\_ARM%
* %VC\_LibraryPath\_VC\_ARM64%
* %VC\_LibraryPath\_VC\_ARM64EC%
* %VC\_LibraryPath\_VC\_ARM64EC\_Desktop%
* %VC\_LibraryPath\_VC\_ARM64EC\_Desktop\_spectre%
* %VC\_LibraryPath\_VC\_ARM64EC\_OneCore%
* %VC\_LibraryPath\_VC\_ARM64EC\_OneCore\_spectre%
* %VC\_LibraryPath\_VC\_ARM64EC\_Store%
* %VC\_LibraryPath\_VC\_ARM64\_Desktop%
* %VC\_LibraryPath\_VC\_ARM64\_Desktop\_spectre%
* %VC\_LibraryPath\_VC\_ARM64\_OneCore%
* %VC\_LibraryPath\_VC\_ARM64\_OneCore\_spectre%
* %VC\_LibraryPath\_VC\_ARM64\_Store%
* %VC\_LibraryPath\_VC\_ARM\_Desktop%
* %VC\_LibraryPath\_VC\_ARM\_Desktop\_spectre%
* %VC\_LibraryPath\_VC\_ARM\_OneCore%
* %VC\_LibraryPath\_VC\_ARM\_OneCore\_spectre%
* %VC\_LibraryPath\_VC\_ARM\_Store%
* %VC\_LibraryPath\_VC\_x64%
* %VC\_LibraryPath\_VC\_x64\_Desktop%
* %VC\_LibraryPath\_VC\_x64\_Desktop\_spectre%
* %VC\_LibraryPath\_VC\_x64\_OneCore%
* %VC\_LibraryPath\_VC\_x64\_OneCore\_spectre%
* %VC\_LibraryPath\_VC\_x64\_Store%
* %VC\_LibraryPath\_VC\_x86%
* %VC\_LibraryPath\_VC\_x86\_Desktop%
* %VC\_LibraryPath\_VC\_x86\_Desktop\_spectre%
* %VC\_LibraryPath\_VC\_x86\_OneCore%
* %VC\_LibraryPath\_VC\_x86\_OneCore\_spectre%
* %VC\_LibraryPath\_VC\_x86\_Store%
* %VC\_VC\_IncludePath%
* %VIRTUAL\_ENV%
* %VS160COMNTOOLS%
* %VSCMD\_ARG\_APP\_PLAT%
* %VSCMD\_ARG\_CHAMELEON%
* %VSCMD\_ARG\_CLEAN\_ENV%
* %VSCMD\_ARG\_HELP%
* %VSCMD\_ARG\_HOST\_ARCH%
* %VSCMD\_ARG\_NO\_EXT%
* %VSCMD\_ARG\_STARTDIR%
* %VSCMD\_ARG\_TGT\_ARCH%
* %VSCMD\_ARG\_VCVARS\_SPECTRE%
* %VSCMD\_ARG\_VCVARS\_VER%
* %VSCMD\_ARG\_WINSDK%
* %VSCMD\_ARG\_no\_logo%
* %VSCMD\_BANNER\_SHELL\_NAME\_ALT%
* %VSCMD\_BANNER\_TEXT\_ALT%
* %VSCMD\_DEBUG%
* %VSCMD\_SKIP\_SENDTELEMETRY%
* %VSCMD\_START\_DIR%
* %VSCMD\_TEST%
* %VSCMD\_VCVARSALL\_INIT%
* %VSCMD\_VER%
* %VSINSTALLDIR%
* %WORKINGDIR%
* %WORKINGDIRONEDRIVE%
* %WindowsLibPath%
* %WindowsSDKDir%
* %WindowsSDKLibVersion%
* %WindowsSDKNotFound%
* %WindowsSDKVersion%
* %WindowsSDK\_ExecutablePath\_x64%
* %WindowsSDK\_ExecutablePath\_x86%
* %WindowsSdkBinPath%
* %WindowsSdkDir%
* %WindowsSdkVerBinPath%
* %cmd%
* %computername%
* %comspec%
* %dir%
* %errorlevel%
* %findSDK%
* %match%
* %originPolicy%
* %result%
* %returnValue%
* %scriptPath%
* %s...