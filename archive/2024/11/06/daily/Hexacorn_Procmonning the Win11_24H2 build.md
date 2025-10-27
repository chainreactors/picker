---
title: Procmonning the Win11_24H2 build
url: https://www.hexacorn.com/blog/2024/11/05/procmonning-the-win11_24h2-build/
source: Hexacorn
date: 2024-11-06
fetch_date: 2025-10-06T19:17:03.474046
---

# Procmonning the Win11_24H2 build

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

[← Previous](https://www.hexacorn.com/blog/2024/10/26/some-notes-on-windows-11-notepad/)
[Next →](https://www.hexacorn.com/blog/2024/11/07/beating-the-dead-horse-only-to-inject-it-some-more/)

# Procmonning the Win11\_24H2 build

Posted on [2024-11-05](https://www.hexacorn.com/blog/2024/11/05/procmonning-the-win11_24h2-build/ "10:55 pm")  by  [adam](https://www.hexacorn.com/blog/author/adam/ "View all posts by adam")

This is a bunch of random notes from running Procmon on Win11\_24H2 build.

We all know about *autorun.inf* that OS is checking when we attach a new device to the system, but on new devices the system is actually looking for more files — here’s the list:

* \Device\HarddiskVolumeN\audio\_ts\audio\_ts.ifo
* \Device\HarddiskVolumeN\autorun.inf
* \Device\HarddiskVolumeN\AVCHD
* \Device\HarddiskVolumeN\BDAV
* \Device\HarddiskVolumeN\BDMV
* \Device\HarddiskVolumeN\bootex.log
* \Device\HarddiskVolumeN\DCIM
* \Device\HarddiskVolumeN\desktop.ini
* \Device\HarddiskVolumeN\dvd\_rtav\vr\_mangr.ifo
* \Device\HarddiskVolumeN\EFI\Microsoft\Boot\BCD
* \Device\HarddiskVolumeN\EFI\Microsoft\Boot\BCD.LOG
* \Device\HarddiskVolumeN\EFI\Microsoft\Boot\Policies\UnlockToken.pol
* \Device\HarddiskVolumeN\PRIVATE\AVCHD
* \Device\HarddiskVolumeN\Recovery.txt
* \Device\HarddiskVolumeN\SVCD\entries.svd
* \Device\HarddiskVolumeN\SVCD\entries.vcd
* \Device\HarddiskVolumeN\System Volume Information
* \Device\HarddiskVolumeN\System Volume Information\AadRecoveryPasswordDelete
* \Device\HarddiskVolumeN\System Volume Information\ClientRecoveryPasswordRotation
* \Device\HarddiskVolumeN\System Volume Information\FveDecryptedVolumeFolder
* \Device\HarddiskVolumeN\VCD\entries.vcd
* \Device\HarddiskVolumeN\video\_ts\video\_ts.ifo
* \Device\HarddiskVolumeN\WinReOfflineScanningResult.dat

Some of them are obviously media-related, some are Windows Backup-related, and some … I have no clue.

The other interesting bit is that when executed, *lsass.exe* is trying to load a phantom DLL named *“”.dll*:

* C:\Windows\””.DLL
* C:\Windows\System\””.DLL
* C:\Windows\System32\””.DLL

While it looks like an attractive proposition, I am not sure if there is a way to exploit it 🙁 Still, need to come back to it to understand why the process is doing so. Perhaps there is a new data dumping opportunity here, somewhere…

There are a lot of new phantom DLLs, but they are tricky to play with. While writing this post I messed up this build’s booting so many times that I no longer understand which of these test phantom DLLs I added to the system contributed to the damage 🙂 I have added a list of potentials at the bottom of this post.

Then there is *smss.exe* trying to find these:

* C:\Windows\apppatch\drvpatch.sdb
* C:\Windows\System32\wowarmhw.dll
* C:\Windows\System32\xtajit.dll
* C:\Windows\System32\xtajit64.dll
* C:\Windows\System32\xtajit64se.dll
* C:\Windows\SysWOW64\wow64.dll
* C:\Windows\SysWOW64\wow64base.dll
* C:\Windows\SysWOW64\wow64con.dll
* C:\Windows\SysWOW64\wow64win.dll
* C:\Windows\SysWOW64\xtajit64.dll
* C:\Windows\SysWOW64\xtajit64se.dll

Then *spoolsv.exe* trying to access these:

* C:\Windows\System32
* C:\Windows\System32\spool
* C:\Windows\System32\spool\drivers
* C:\Windows\System32\spool\drivers\ARM64
* C:\WINDOWS\system32\spool\drivers\ARM64\3\New\
* C:\WINDOWS\system32\spool\drivers\ARM64\3\Old\
* C:\WINDOWS\system32\spool\drivers\ARM64\4\New\
* C:\WINDOWS\system32\spool\drivers\ARM64\4\Old\
* C:\Windows\System32\spool\drivers\IA64
* C:\WINDOWS\system32\spool\drivers\IA64\3\New\
* C:\WINDOWS\system32\spool\drivers\IA64\3\Old\
* C:\Windows\System32\spool\drivers\W32X86
* C:\Windows\System32\spool\drivers\W32X86\3\New
* C:\Windows\System32\spool\drivers\W32X86\3\Old
* C:\Windows\System32\spool\drivers\x64
* C:\Windows\System32\spool\drivers\x64\3\New
* C:\Windows\System32\spool\drivers\x64\3\Old
* C:\WINDOWS\system32\spool\drivers\x64\4\New\
* C:\WINDOWS\system32\spool\drivers\x64\4\Old\
* C:\Windows\System32\spool\PRINTERS
* C:\Windows\System32\spool\SERVERS
* C:\Windows\System32\ualapi.dll
* C:\Windows\System32\vfprint.dll

There seems to be a lot of cross-architectural code logic present here that needs further exploration.

There also seem to be more phantom DLL loading opportunities that are only available under specific conditions:

* C:\Windows\System32\Unknown.DLL (loaded by svchost.exe when AFAICT there is no network connectivity)
* C:\WINDOWS\SYSTEM32\windowsdefender:\.DLL – a potential phantom DLL but impossible due to file/ADS naming limitations

And finally, there is really a lot of paths the OS is trying to access in the procmon log that suggests some incoherent environment variable parsing:

* C:\Windows\System32\%ProgramFiles(arm)%
* C:\WINDOWS\system32\%systemroot%\system32\wbem\cimwin32.dll
* C:\WINDOWS\system32\%systemroot%\system32\wbem\wmipcima.dll
* C:\WINDOWS\%WINDIR%\System32\SPP\Migration\sppgenmig.dat
* C:\WINDOWS\%WINDIR%\System32\SPP\Migration\sppmig.dat
* C:\Windows\System32\%SystemRoot%\ProgramData\Microsoft\Windows\AppRepository\Packages\MicrosoftWindows.Client.AIX\_1000.26100.29.0\_x64\_\_cw5n1h2txyewy\ActivationStore.dat
* C:\Windows\SystemApps\Microsoft.Windows.StartMenuExperienceHost\_cw5n1h2txyewy\%SystemRoot%\ProgramData\Microsoft\Windows\AppRepository\Packages\MicrosoftWindows.Client.AIX\_1000.26100.29.0\_x64\_\_cw5n1h2txyewy\ActivationStore.dat
* C:\WINDOWS\%WINDIR%\System32\SPP\Migration\sppgenmig.dat
* C:\WINDOWS\system32\%systemroot%\system32\wbem\wmiprov.dll
* C:\Users\<USER>\Desktop\%1
* C:\Users\Public\Desktop\%1

That’s a lot of sideloading and potential LPE vulns to explore…

The full list of possible phantom DLLs can be found here ([win11\_24H2\_phantom\_dlls.txt](https://hexacorn.com/d/win11_24H2_phantom_dlls.txt)). Some of them are obvious path problems, but many are real phantom DLLs.

This entry was posted in [Archaeology](https://www.hexacorn.com/blog/category/archaeology/), [Windows 11](https://www.hexacorn.com/blog/category/windows-11/) by [adam](https://www.hexacorn.com/blog/author/adam/). Bookmark the [permalink](https://www.hexacorn.com/blog/2024/11/05/procmonning-the-win11_24h2-build/ "Permalink to Procmonning the Win11_24H2 build").

[Privacy Policy](https://www.hexacorn.com/blog/privacy-policy/) [Proudly powered by WordPress](https://wordpress.org/ "Semantic Personal Publishing Platform")