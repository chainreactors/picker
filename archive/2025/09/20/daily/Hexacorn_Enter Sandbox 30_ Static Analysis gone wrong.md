---
title: Enter Sandbox 30: Static Analysis gone wrong
url: https://www.hexacorn.com/blog/2025/09/19/enter-sandbox-30-static-analysis-gone-wrong/
source: Hexacorn
date: 2025-09-20
fetch_date: 2025-10-02T20:25:56.000977
---

# Enter Sandbox 30: Static Analysis gone wrong

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

[← Previous](https://www.hexacorn.com/blog/2025/09/08/beyond-good-ol-run-key-part-151/)
[Next →](https://www.hexacorn.com/blog/2025/09/19/rundll-exporters/)

# Enter Sandbox 30: Static Analysis gone wrong

Posted on [2025-09-19](https://www.hexacorn.com/blog/2025/09/19/enter-sandbox-30-static-analysis-gone-wrong/ "10:18 pm")  by  [adam](https://www.hexacorn.com/blog/author/adam/ "View all posts by adam")

This series is quite old, and I kinda abandoned it at some stage, but today I am reviving it to talk about … static analysis…

Let’s be honest – last 2 decades changed the way we do malware analysis, and for many reasons:

* groundbreaking developments in decompilation,
* groundbreaking developments in deobfuscation,
* groundbreaking developments in devirtualisation,
* groundbreaking developments in emulation,
* groundbreaking developments in sandboxing,
* groundbreaking developments in Satisfiability Modulo Theory (SMT) solvers,
* groundbreaking developments in GenAI,
* demonopolisation and democratisation of reverse engineering tools aka a lot more tools available in general, and even if some are still commercial, they are often cheaper, and many that are free — are literally game changers, and generally speaking… the tooling today is far more accessible than it was 20 years ago,
* emergence of many advanced (and often free) mature malware-oriented sandboxing, hooking and emulation toolkits,
* development of many free tools/techniques enables us to decompile, debundle many installers or compiled scripts,
* software (including malware) developers walking away from protectors, packers and wrappers of yesterday – today it’s often no longer worth it,
* emergence of tools like Detect It Easy, Yara/Yara-X, Capa, Floss, Bulk Extractor, and many forensic tools that allow us to perform a lot of file format-parsing tasks associated with preliminary static sample analysis focused on ‘low hanging fruits’ like:
  + reputational checks, signed binary checks,
  + determining the file format very precisely,
  + automated feature/functionality discovery/extraction/classification,
  + automatic payload decryption/extraction,
  + automatic config decryption/extraction,
  + full metadata parsing/extraction,
  + extraction of strings of interest hidden inside the code that in the past we could only find via dynamic analysis (f.ex. on stack), and of course,
  + large and rich libraries of yara rules help to immediately identify malware sample’s family if it has been already classified before,
  + older programming languages like Visual Basic, Delphi, C, C++ are now replaced by Go, Rust, Python, .NET, Windows Apps, Electron Apps,
* emergence of SaaS and software delivered via browser only,
* disabling OS / Software features by default helped to kill many attack vectors (macros, autorun.inf, etc.),
* decreasing importance of email – it got replaced by IM software with rich features,
* lots of new operating systems, new CPUs, and new architectures expanded the scope, and made Windows less important,
* jailbreaking scene,
* 0day/vulnerability discovery scene,
* lolbins, RMMs and a wave of TTPs that focus on blending in with the environment,
* advances in EDR-based detections,
* advances in decoy-based detections,
* lots of new protections built-in into browsers and file readers/viewers prevent old drive-by attacks,
* smartphones and tablets taking over from desktop computers and laptops for many daily tasks,
* 0days moving from endpoints to IoT, appliances, mobile devices,
* security focus moving from an endpoint attack surface to identity solutions,
* platformisation and a global move from ‘build’ to ‘buy’ lowered the bar for cybersecurity skills required to do the job,
* etc.

In 2010 malware analysts’ skills were measured by the knowledge of debuggers, disassemblers, file formats, packers, etc. Now… we are in 2025 and let’s be honest… malware analysis process of today usually starts with a submission of a sample to a sandbox / sample analysis portal. And, sadly, it very often ends there!

This is where this post begins.

I am quite surprised that many automated malware analysis solutions do not process samples statically very well. They do not do in-depth file format analysis, they do not recognize corrupted files well, and often offer a false sense of security/value by offering a CLEAN verdict for files that simply need more …. reversing love.

See the below example.

I took Notepad.exe from Win10, truncated it with a hex editor, and then submitted it to a few online file analysis services. I am happy that some of them immediately marked the file as *corrupt*ed, but it didn’t stop them from running a full-blown dynamic analysis session on the file I submitted. And in terms of static analysis, some solutions went as far as to report lots of findings related to anti-reversing techniques, cryptography, and lots of far-fetched conclusions that are nonsensical in a context of a) a corrupted file, b) Notepad program (clearly non-malicious), and are simply not a true reflection of reality.

I kid you not, but a truncated notepad sample that will never execute was marked as

* a program that can enumerate processes (because it references *NtQuerySystemInformation* function that is actually used by [warbird](https://stackoverflow.com/questions/40643965/what-is-microsoft-warbird-in-compiler-of-vs2015) protection that invokes this API with a *SystemThrottleNotificationInformation*/*SystemPolicyInformation* parameter),
* a program that accepts drag & drop operations (true),
* a program that has an ability to take screenshots (just because it references a *CreateDC* API function), which is not true,
* and so on and so forth.

Let’s be clear – mapping presence of APIs in the sample’s import table or as a string referencing API name found in a sample’s body to actual ‘threats’ or TTPs is an absurdity that is omnipresent in sandbox reports today and should be corrected asap. This could have worked in 2010, but today these sort of ‘determinations’ must be seen as poor indicators.

And as an analyst, I’d actually like to see why the sample was marked as *corrupt*ed. I’d also like to see the context of the far-fetched API-matching claims as well. You can’t list many Windows API in a negative context (like f.ex. *CreateDC* that notepad uses for… printing) unless you really can prove that it is indeed present in the code to deliver some malicious functionality… It strikes us as an over-simplistic approach that is focused more on the quantity of the findings than the overall quality of the report.

This is where old-school reversing comes in.

A long time ago I wrote my own PE file parser that I always run on all PE samples that I analyze, first. Because I wrote it, I fully control what it tells me, and since I used this tool to analyze many files over the years, corrected it on many occasions, learned a lot about PE file format intricacies on the way, and I have incorporated a lot of PE file format checks into it.

Running it on my truncated Notepad sample I immediately get many red flags:

```
(Raw Offset + Raw size of '.data '=0002EC00>filesize=0002DE00
(Offset to Raw size of '.pdata '=0002EC00>filesize=0002DE00
(Offset to Raw size of '.didat '=0002FE00>filesize=0002DE00
(Offset to Raw size of '.rsrc '=00030000>filesize=0002DE00
(Offset to Raw size of '.reloc '=00030C00>filesize=0002DE00
(wrong appdata ofs/size=0002EC00,00000000)
(.rsrc File Offset 00030000 <> DataDirectoryResourceOffset = 00000000
```

Seeing this kind of result immediately alters the way I do my sample ...