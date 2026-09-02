---
title: seer snap-latest
url: https://kitploit.com/en/posts/github-epasveer-seer-snap-latest
source: Kitploit
date: 2026-09-01
fetch_date: 2026-09-02T06:40:09.181054
---

# seer snap-latest

[Skip to content](#main-content)

[![Kitploit](/_next/image?url=%2Flogo.png&w=64&q=75)KITPLOIT](/en)[Tools](/en/tools)[Blog](/en/blog)Categories

EN

[Submit](/en/submit)

[Tools](/en/tools)[Blog](/en/blog)Categories

[Submit](/en/submit)

EN

Hacking, PenTest, and Cybersecurity Tools for Your Security Arsenal!

[Back to updates](/en/updates)

![](https://assets.kitploit.com/production/public/tools/13232/21aaca6333f3cdf2ecaf3405c4917962dff8bc36ea1ae2025a83cd3ba2fc6792.png)

New releaseSep 1, 2026

# seer snap-latest

Seer - a gui frontend to gdb

Share

# Introduction

Seer - a gui frontend to gdb for Linux. (Ernie Pasveer [[email protected]](/cdn-cgi/l/email-protection#86e3f6e7f5f0e3e3f4c6e7f2f2a8e8e3f2))

This project is actively worked on. The aim is a simple, yet pleasing gui to gdb.

Please report any bugs or desired features to my email or create a [task](https://github.com/epasveer/seer/issues) in my
GitHub project page.

# Installation

Seer can be installed either from a package manager or from source.

> [!NOTE]
> Make sure the requirements are met before installing.

## Requirements

* Linux
* C++17
* gdb with "mi" interpreter (check by running: `gdb --interpreter=mi`)
* CMake (3.5.0 or newer)
* QT6

  + When building Seer from source, you will need the QT6 "devel" packages installed on your system for your distribution.
    - Core
    - Gui
    - Widgets
    - PrintSupport
    - Charts
    - Svg
  + Qt6 build instructions are here: <https://github.com/epasveer/seer/wiki/Building-Seer---Qt6>
* QT5

  + **Seer no longer compiles with Qt5.** The 2.3 source tree is the last one that does.
  + Qt5 build instructions are here: <https://github.com/epasveer/seer/wiki/Building-Seer---Qt5>

## Install from package

Available through the following package managers:

### Pamac (Manjaro)

root@kitploit:~

```
$ pamac install seer
```

### zypper (openSUSE Tumbleweed)

root@kitploit:~

```
$ zypper install seergdb
```

### Flathub

Flathub website. [Here](https://flathub.org/en/apps/io.github.epasveer.seer)

root@kitploit:~

```
$ flatpak install flathub io.github.epasveer.seer
```

### Flatpak

Beta Seer versions. [Seer's release page](https://github.com/epasveer/seer/releases/tag/flatpak-latest) on github.

**Important**: `flatpak-spawn --host`, needed in `GDB Launcher` to run gdb. See <https://github.com/epasveer/seer/issues/377#issuecomment-3620844808>.

Download `seer.flatpak`. Install it:

root@kitploit:~

```
$ flatpak install -y --bundle --user seer.flatpak
```

### Snap

Beta Seer versions. [Seer's release page](https://github.com/epasveer/seer/releases/tag/snap-latest) on github.

root@kitploit:~

```
$ snap install seergdb_<version>.snap --dangerous
```

## Install from source

(Recommended) Seer can be built with Qt6 by following the instructions below.

<https://github.com/epasveer/seer/wiki/Building-Seer---Qt6>

It can still be built with Qt5, for the time being by following the instructions below.

<https://github.com/epasveer/seer/wiki/Building-Seer---Qt5>

# NEWS

Check out [Seer's Wiki page](https://github.com/epasveer/seer/wiki) on github.

* Version v1.17 will be the last Qt5 release.
* The next release will be v2.0 and will be Qt6 based. However, for the time being, it's still able to be compiled with Qt5.
* If you want the latest stable Qt5 source, grab v1.17 from here: <https://github.com/epasveer/seer/releases/tag/v1.17>

# Starting Seer

Seer is meant to easily start the program to debug from the command line. gdb has multiple
methods for debugging a program. So Seer naturally does too.

Go to the Wiki to see all the ways to run Seer.

<https://github.com/epasveer/seer/wiki/Starting-Seer>

# GUI overview

Examples of the various Seer views and dialogs.

## Main View

The main view for Seer looks like this:
![](https://assets.kitploit.com/production/public/readmes/13232/a447b13ab75f585cc3a37deb6664ebb7c11991b43369d5f164345cf4e5d00856.png)

* Source/Function/Types/Variables/Libraries

  + The list of source/header files that were used in the program.
  + Search for Functions, Types, and Static Variables.
    Dobule clicking will open the source file.
  + The list of shared libraries referenced by the program.
  + The list of source/header files can be searched. This will "shrink" the list of files shown.
  + Double clicking on a file will open it in the Code Manager.
* Variable/Register Info

  + Show variable and register values.
  + "Logger" - log the value of a variable. Manually enter it or double click on the variable in the file
    that is opened in the code manager.
  + "Tracker" - create a list of variables to show the value for whenever gdb reaches a stopping point
    (step, next, finish, etc.). When the stopping point is reached, all variables in the list will show
    their potentially new value.
  + "Registers" - show the values of all cpu registers.
* Code Manager.

  + The large area of the middle part of the Seer gui.
  + Source files are opened in this view.
  + Text in a file can be seached for with ^F.
  + Variables can be added to the "Logger" by double clicking the variable name.
    Double click with CTLR key pressed will prepend variable with "*".
    Double click with SHIFT key pressed will prepend variable with "&".
    Double click with CTRL+SHIFT key pressed will prepend variable with "*&".
  + Variables can be added to the "Tracker" by selecting the variable name and RMB and select
    "Add variable to Tracker".
  + Variables can be added to the "Memory Visualizer" by selecting the variable name and RMB and select
    "Add variable to Memory Visualizer".
  + A breakpoint/printpoint can be created by RMB on a specific line.
  + Can execute to a specific line by RMB on a specific line.
  + Tabs in this view can be detached by double-clicking a tab.
* Breakpoints, Watchpoints, Catchpoints, Printpoints, manual gdb commands, and logs.

  + The area below the Code Manager.
  + Manual commands. Manually enter a gdb or gdbmi command.
    The commands are remembered for the next Seer use.
  + Breakpoint manager. Create and manage breakpoints.
  + Watchpoint manager. Create and manage watchpoints.
    A watchpoint monitors when a variable is accessed (read, write, read/write).
  + Catchpoint manager. Create and manage catchpoints.
    A catchpoint stops execution on a C++ throw/rethrow/catch call.
  + Printpoint manager. Create and manage printpoints.
    A printpoint is like a breakpoint but it allows you to print variables at
    that printpoint. See gdb's 'dprintf' call.
  + GDB output. A log of any output from the gdb program itself.
  + Seer output. A log of any output from the Seer program itself. As diagnostics.
  + Tabs in this view can be detached by double-clicking a tab.
* Stack frame information.

  + Stack frame list. A frame can be double clicked to change the scope (the current function).
  + Stack frame arguments. For each frame, print the arguments passed to each function.
  + Stack locals. For the current function, print the values of the local variables.
* Thread information.

  + Thread ids. A list of all threads. Double click on a thread id to change the scope (the current thread).
  + Thread frames. For each thread, list its stack frames.
* Supports Gdb's Reverse Debugging mode.

  + Turn instruction recording on or off.
  + Set playback direction to forward or reverse.

## Open Dialog

When the open executable dialog is invoked, it looks like this:
![](https://assets.kitploit.com/production/public/readmes/13232/cffa8498dae058171a55418ccda9226204cbc8fca9e07434ce5aebc4cb289ed5.png)

## Seer Console

All text output from the executable will go to the Seer console. Text input for the executable can be entered via the console too.
![](https://assets.kitploit.com/production/public/readmes/13232/3b24b1d1677b963e121e76926045fe4352a84edaebc45ea128ee688278948e29.png)

## Assembly View

Normally Seer will just show the source code as tabs in the Code Manager. The program's assembly can also be sho...