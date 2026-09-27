---
title: 1 little known secret of aidd.dll
url: https://www.hexacorn.com/blog/2026/09/26/1-little-known-secret-of-aidd-dll/
source: Hexacorn
date: 2026-09-26
fetch_date: 2026-09-27T07:24:40.044738
---

# 1 little known secret of aidd.dll

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

[← Previous](https://www.hexacorn.com/blog/2026/09/26/1-little-known-secret-of-wincsflags-exe/)

# 1 little known secret of aidd.dll

Posted on [2026-09-26](https://www.hexacorn.com/blog/2026/09/26/1-little-known-secret-of-aidd-dll/ "11:39 pm")  by  [adam](https://www.hexacorn.com/blog/author/adam/ "View all posts by adam")

When you run (from admin account):

```
rundll32 aidd.dll, AiddRunTask
```

a lot of interesting things are happening. There are at least 2 files of interest being created:

```
c:\Windows\appcompat\AIDD\AIDDProcessLoadedDllListDBdump.txt
c:\Windows\appcompat\AIDD\ProcessLoadedDllList.db
```

They include a textual and SQLite-based list of executables running and DLLs loaded.

The text file includes 3 sections:

```
@#1 Executable
@#2 DLL
@#3 ExecutableDLL
```

and the SQLite database file includes 3 tables:

```
CREATE TABLE Executable (ID INTEGER PRIMARY KEY AUTOINCREMENT,Path TEXT UNIQUE NOT NULL,Publisher TEXT,ProductName TEXT,Version TEXT,ProgramID TEXT,FileID TEXT);

CREATE TABLE DLL (ID INTEGER PRIMARY KEY AUTOINCREMENT,Path TEXT UNIQUE NOT NULL,Publisher TEXT,ProductName TEXT,Version TEXT,FileID TEXT);

CREATE TABLE ExecutableDLL (ID INTEGER PRIMARY KEY AUTOINCREMENT,ExecutableID INTEGER NOT NULL,DllID INTEGER NOT NULL,DetectedAtLaunch INTEGER DEFAULT 0,LoadCount INTEGER DEFAULT 1,LastLoaded DATETIME,Month1_flag INTEGER DEFAULT 0,Month2_flag INTEGER DEFAULT 0,Month3_flag INTEGER DEFAULT 0,Month4_flag INTEGER DEFAULT 0,Month5_flag INTEGER DEFAULT 0,Month6_flag INTEGER DEFAULT 0,Month7_flag INTEGER DEFAULT 0,Month8_flag INTEGER DEFAULT 0,Month9_flag INTEGER DEFAULT 0,Month10_flag INTEGER DEFAULT 0,Month11_flag INTEGER DEFAULT 0,Month12_flag INTEGER DEFAULT 0,Month1_year INTEGER DEFAULT 0,Month2_year INTEGER DEFAULT 0,Month3_year INTEGER DEFAULT 0,Month4_year INTEGER DEFAULT 0,Month5_year INTEGER DEFAULT 0,Month6_year INTEGER DEFAULT 0,Month7_year INTEGER DEFAULT 0,Month8_year INTEGER DEFAULT 0,Month9_year INTEGER DEFAULT 0,Month10_year INTEGER DEFAULT 0,Month11_year INTEGER DEFAULT 0,Month12_year INTEGER DEFAULT 0,FOREIGN KEY (ExecutableID) REFERENCES Executable(ID),FOREIGN KEY (DllID) REFERENCES DLL(ID),UNIQUE(ExecutableID, DllID));
```

This is a quick&dirty equivalent of what you can get with Sysinternals’ tool listdlls.exe now available natively on Windows 11 26H2

This entry was posted in [Archaeology](https://www.hexacorn.com/blog/category/archaeology/), [little known secrets](https://www.hexacorn.com/blog/category/little-known-secrets/) by [adam](https://www.hexacorn.com/blog/author/adam/). Bookmark the [permalink](https://www.hexacorn.com/blog/2026/09/26/1-little-known-secret-of-aidd-dll/ "Permalink to 1 little known secret of aidd.dll").

[Privacy Policy](https://www.hexacorn.com/blog/privacy-policy/) [Proudly powered by WordPress](https://wordpress.org/ "Semantic Personal Publishing Platform")