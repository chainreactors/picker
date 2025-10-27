---
title: Using make_sc_hash_db.py to create API hashing DBs
url: https://www.hexacorn.com/blog/2022/12/03/using-make_sc_hash_db-py-to-create-api-hashing-dbs/
source: Hexacorn
date: 2022-12-04
fetch_date: 2025-10-04T00:28:54.813432
---

# Using make_sc_hash_db.py to create API hashing DBs

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

[← Previous](https://www.hexacorn.com/blog/2022/12/02/environment-is-variable/)
[Next →](https://www.hexacorn.com/blog/2022/12/08/the-future-of-soc/)

# Using make\_sc\_hash\_db.py to create API hashing DBs

Posted on [2022-12-03](https://www.hexacorn.com/blog/2022/12/03/using-make_sc_hash_db-py-to-create-api-hashing-dbs/ "10:43 pm")  by  [adam](https://www.hexacorn.com/blog/author/adam/ "View all posts by adam")

If you ever used *[shellcode\_hashes](https://github.com/mandiant/flare-ida/blob/master/plugins/shellcode_hashes_search_plugin.py)* IDA plugin from Mandiant, you probably have also used *make\_sc\_hash\_db.py* before. But, if you haven’t, this post is for you.

The focus of the article is on the the *make\_sc\_hash\_db.py* script – it is used to generate a SQLite database *sc\_hashes.db* that in turn is used by *shellcode\_hashes\_search\_plugin.py* (used from IDA GUI) to identify immediate values that could be hashes of known APIs inside the decompiled binary. It’s fast and superhandy for position independent code analysis, including inline and implanted PE file loaders that rely on such API hashing functionality (multiple API hashing algos are supported).

As per the *readme.md*, the *make\_sc\_hash\_db.py* can be called with the following arguments:

```
python make_sc_hash_db.py <database name> <dll directory>
```

The best is of course to run it on a subset of the c:\windows\system32 directory, with a focus on the most common libraries and the *sc\_hashes.db* speaks to that directly, including only API hashes for the following libraries:

* advapi32.dll
* advpack.dll
* chrome.dll
* comctl32.dll
* comdlg32.dll
* crypt32.dll
* dnsapi.dll
* gdi32.dll
* hal.dll
* imagehlp.dll
* IPHLPAPI.DLL
* kernel32.dll
* lsass.exe
* mpr.dll
* msvcrt.dll
* netapi32.dll
* nss3.dll
* ntdll.dll
* ntoskrnl.exe
* odbc32.dll
* ole32.dll
* oleaut32.dll
* psapi.dll
* shell32.dll
* shfolder.dll
* shlwapi.dll
* termdd.sys
* urlmon.dll
* user32.dll
* userenv.dll
* winhttp.dll
* wininet.dll
* winmm.dll
* winsta.dll
* ws2\_32.dll
* wship6.dll
* wsock32.dll

BUT

it’s also handy to have a larger data set available.

When I played with it a few years ago, I generated all hashes from the whole C:\windows\system32 directory.

Why?

Because you never know when you will stumble upon a hash value that is not represented inside the *sc\_hashes.db*.

Now, you may think that replacing default *sc\_hashes.db* with your *full\_blown\_system32\_dataset.db* is the best idea ever, but it’s not. The *sc\_hashes.db* is 50MB file, and the the *full\_blown* one is ~600MB. SQLite is fast, but Ida+python+SQLite, not so much. So, you have been warned.

The bottom line:

Use default *sc\_hashes.db* for all your cases first, and only if you find hashes outside of this set, try to look for the hash inside the *full\_blown* one (either via SQLIte interface, or via grep/rg on a text export). Finally, if you discover which DLL the API hash belongs to, you can always generate a new SQLite DB set based on that single DLL (just needs to be copied to a working directory for the *make\_sc\_hash\_db.py* script to process it).

And if you don’t understand any of it, just download this [full\_blown\_limited\_output.zip](https://hexacorn.com/d/full_blown_limited_output.zip) file (45MB warning). It includes many hashes and many APIs. You can simply grep it for unknown API hash. Who knows, maybe you will get lucky…

This entry was posted in [Malware Analysis](https://www.hexacorn.com/blog/category/malware-analysis/) by [adam](https://www.hexacorn.com/blog/author/adam/). Bookmark the [permalink](https://www.hexacorn.com/blog/2022/12/03/using-make_sc_hash_db-py-to-create-api-hashing-dbs/ "Permalink to Using make_sc_hash_db.py to create API hashing DBs").

[Privacy Policy](https://www.hexacorn.com/blog/privacy-policy/) [Proudly powered by WordPress](https://wordpress.org/ "Semantic Personal Publishing Platform")