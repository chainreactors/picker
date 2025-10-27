---
title: Beyond good ol’ Run key, Part 143
url: https://www.hexacorn.com/blog/2024/10/19/beyond-good-ol-run-key-part-143/
source: Hexacorn
date: 2024-10-20
fetch_date: 2025-10-06T18:49:38.140533
---

# Beyond good ol’ Run key, Part 143

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

[← Previous](https://www.hexacorn.com/blog/2024/10/19/advpack-dll-and-ieadvpack-dll-logging-capability/)
[Next →](https://www.hexacorn.com/blog/2024/10/25/installing-latest-ghidra-w-o-installing-it/)

# Beyond good ol’ Run key, Part 143

Posted on [2024-10-19](https://www.hexacorn.com/blog/2024/10/19/beyond-good-ol-run-key-part-143/ "10:17 pm")  by  [adam](https://www.hexacorn.com/blog/author/adam/ "View all posts by adam")

This entry is a bit convoluted, but it’s still quite interesting. I have discovered it today only to google around and find out someone posted the info about it [back in 2013](https://forum.esetnod32.ru/forum6/topic2836/?PAGEN_1=109). So, I will describe what they did in 2013 + will add one extra bit.

The trick relies on the way the *UserInstStubWrapper* API exported by *advpack.dl*l / *IEAdvpack.dll* works.

When you execute a command like this:

```
rundll32.exe advpack.dll, UserInstStubWrapper test
```

the *UserInstStubWrapper* function will read the value from *RealStubPath*:

```
HKLM\SOFTWARE\Microsoft\Active Setup\Installed Components\test
RealStubPath=<PATH> (f.ex. c:\windows\notepad.exe)
```

and execute the program referenced by it (in this case Notepad).

[![](https://www.hexacorn.com/blog/wp-content/uploads/2024/10/advpack_1.png)](https://www.hexacorn.com/blog/wp-content/uploads/2024/10/advpack_1.png)

As for the extra, there is a twin function called *UserUnInstStubWrapper*. This one requires admin privileges to run, but it behaves in a similar manner – f.ex. for the command:

```
rundll32.exe advpack.dll, UserUnInstStubWrapper test
```

it will reach out to Registry and fetch the value of *RealStubPath* as well, but this time the key it accesses will be the name passed via the command line, but slightly modified by adding a suffix *.Restore* to it:

```
HKLM\SOFTWARE\Microsoft\Active Setup\Installed Components\test.Restore
RealStubPath=<PATH> (f.ex. c:\windows\system32\calc.exe)
```

[![](https://www.hexacorn.com/blog/wp-content/uploads/2024/10/advpack_2.png)](https://www.hexacorn.com/blog/wp-content/uploads/2024/10/advpack_2.png)

So, a persistence opportunity relies on populating these Registry entries first, and then ensuring one of the following commands is executed during autostart by leveraging any of the existing persistence locations (f.ex. Run key):

```
rundll32.exe advpack.dll, UserInstStubWrapper test
rundll32.exe advpack.dll, UserInstStubWrapper test
rundll32.exe ieadvpack.dll, UserUnInstStubWrapper test
rundll32.exe ieadvpack.dll, UserUnInstStubWrapper test
```

If we enable the [advpack logging](https://www.hexacorn.com/blog/2024/10/19/advpack-dll-and-ieadvpack-dll-logging-capability/) we can see these test log entries:

```
-------------------- advpack.dll is loaded or Attached ------------------------------
Date: 10/19/2024 (mm/dd/yyyy)	Time: 15:11:52 (hh:mm:ss)
UserInstStubWrapper:
LaunchAndWait: Cmd=c:\windows\notepad.exe
-------------------- advpack.dll is loaded or Attached ------------------------------
Date: 10/19/2024 (mm/dd/yyyy)	Time: 15:11:58 (hh:mm:ss)
UserUnInstStubWrapper:
LaunchAndWait: Cmd=c:\windows\system32\calc.exe
LaunchAndWait: End hr=0x0, c:\windows\system32\calc.exe
UserUnInstStubWrapper: End hr=0x0
-------------------- advpack.dll is unloaded or Detached ----------------------------
```

This entry was posted in [Archaeology](https://www.hexacorn.com/blog/category/archaeology/), [Autostart (Persistence)](https://www.hexacorn.com/blog/category/autostart-persistence/) by [adam](https://www.hexacorn.com/blog/author/adam/). Bookmark the [permalink](https://www.hexacorn.com/blog/2024/10/19/beyond-good-ol-run-key-part-143/ "Permalink to Beyond good ol’ Run key, Part 143").

[Privacy Policy](https://www.hexacorn.com/blog/privacy-policy/) [Proudly powered by WordPress](https://wordpress.org/ "Semantic Personal Publishing Platform")