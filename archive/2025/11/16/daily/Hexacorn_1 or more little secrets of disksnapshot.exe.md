---
title: 1 or more little secrets of disksnapshot.exe
url: https://www.hexacorn.com/blog/2025/11/16/1-or-more-little-secrets-of-disksnapshot-exe/
source: Hexacorn
date: 2025-11-16
fetch_date: 2025-11-17T03:12:33.389511
---

# 1 or more little secrets of disksnapshot.exe

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

[← Previous](https://www.hexacorn.com/blog/2025/11/04/1-little-known-secret-of-cliconfg-exe/)
[Next →](https://www.hexacorn.com/blog/2025/11/16/some-unusual-run-time-rundll32-exe-artifacts/)

# 1 or more little secrets of disksnapshot.exe

Posted on [2025-11-16](https://www.hexacorn.com/blog/2025/11/16/1-or-more-little-secrets-of-disksnapshot-exe/ "12:08 am")  by  [adam](https://www.hexacorn.com/blog/author/adam/ "View all posts by adam")

This native tool is not very well known, but it may be useful in some cases.

The tool seems to be parsing volumes directly, bypassing the Windows APIs — hence, it kinda works like a `dir` command, but parses the $MFT of volumes directly (but still via API).

The program accepts a number of command line arguments:

```
DiskSnapshot.exe [options]
        -c write detail data to console
        -i write detail data to console (same as -c)
        -s (deprecated) summary data to console
        -u process large volumes (no limit)
        -j [config] specifies an alternate config file
        -v [volume][path] specifies volume(+path) to process, e.g. "d:" or "d:\foo"
        -d [input-file] print encoded versions of the strings in the input file, for decoding purposes
        -e prints out escalation keywords
        -k calculate checksums for files, used to investigate duplicated on-disk content (c arg required).
        -o [output-file] write detail data to a file
```

It turns out that the ‘checksum’ is actually a SHA256 algorithm, so running:

```
disksnapshot -c -k -v c:\test
```

will list all the files in the c:\test directory, and will calculate the SHA256 of each file.

The other curious command line argument is `-e`. Running:

```
disksnapshot -e > escalation_keywords.txt
```

gives us this [list of keywords](https:///www.hexacorn.com/d/win11_25H2_escalation_keywords.txt) (on Windows 11 25H2). It turns out that this list is based on the content of `c:\WINDOWS\system32\DiskSnapshot.conf` file.

There is an undocumented command line argument `-z` that kinda tries to collect telemetry, but it doesn’t really work. If the call to a function *TelIsTelemetryTypeAllowed(2)* returns 1 it just exits with a message:

```
Telemetry run: telemetry is disabled, exiting
```

Otherwise, it checks if the OS is a retail version (guessing by the function name that is called here), and if it is, it ‘rolls a dice’ and prints the below message:

```
    curtime = _time64(0);
    _o_srand(curtime);
    rand = ::rand();
    if ( rand != 7 * (rand / 7) )
    {
      v4 = o___acrt_iob_func_0(2u);
      fwprintf(v4, L"Telemetry run: failed the dice roll, exiting\n");
      return 0;
    }
```

There is a command line argument `-j` that we can use to change the default config file from `c:\WINDOWS\system32\DiskSnapshot.conf` file to our own, but I am not sure how to use it. The `disksnapshot -j c:\test\test.conf -e` command prints out the content of the custom config, but when I tried to apply it to the volume, it somehow didn’t work. I guess I just don’t fully understand the logic behind this tool.

This entry was posted in [Archaeology](https://www.hexacorn.com/blog/category/archaeology/) by [adam](https://www.hexacorn.com/blog/author/adam/). Bookmark the [permalink](https://www.hexacorn.com/blog/2025/11/16/1-or-more-little-secrets-of-disksnapshot-exe/ "Permalink to 1 or more little secrets of disksnapshot.exe").

[Privacy Policy](https://www.hexacorn.com/blog/privacy-policy/) [Proudly powered by WordPress](https://wordpress.org/ "Semantic Personal Publishing Platform")