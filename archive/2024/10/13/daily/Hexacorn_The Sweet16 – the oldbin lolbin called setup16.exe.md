---
title: The Sweet16 – the oldbin lolbin called setup16.exe
url: https://www.hexacorn.com/blog/2024/10/12/the-sweet16-the-oldbin-lolbin-called-setup16-exe/
source: Hexacorn
date: 2024-10-13
fetch_date: 2025-10-06T18:49:52.792809
---

# The Sweet16 – the oldbin lolbin called setup16.exe

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

[← Previous](https://www.hexacorn.com/blog/2024/10/02/using-guids-to-guide-the-id-of-samples-capabilities-or-unique-attributable-properties/)
[Next →](https://www.hexacorn.com/blog/2024/10/19/advpack-dll-and-ieadvpack-dll-logging-capability/)

# The Sweet16 – the oldbin lolbin called setup16.exe

Posted on [2024-10-12](https://www.hexacorn.com/blog/2024/10/12/the-sweet16-the-oldbin-lolbin-called-setup16-exe/ "9:17 pm")  by  [adam](https://www.hexacorn.com/blog/author/adam/ "View all posts by adam")

I don’t even know how to start. I wrote about old [InstallShield](https://www.hexacorn.com/blog/2017/10/14/beating-shields-of-edr-with-the-16-bit-setup/) setup before, and today’s topic is very similar – the old, yet still present setup file residing (on Win10, 11) in the following location:

```
c:\windows\SysWOW64\setup16.exe
```

Running it gives us this misleading message box #1:

[![](https://www.hexacorn.com/blog/wp-content/uploads/2024/10/sweet16_1.png)](https://www.hexacorn.com/blog/wp-content/uploads/2024/10/sweet16_1.png)

After quick study of setup16.exe code I was able to determine what command line arguments it needed and then craft a simple example LST config to act as my setup file.

The program accepts the switch -m that allows us to pass a name of an alternative LST file to it, so we can run a command like this:

```
c:\windows\SysWOW64\setup16.exe -m c:\test\test.lst
```

Creating a dummy file c:\test\test.lst and running the test we get this misleading message box #2:

[![](https://www.hexacorn.com/blog/wp-content/uploads/2024/10/sweet16_2.png)](https://www.hexacorn.com/blog/wp-content/uploads/2024/10/sweet16_2.png)

After analyzing the code a bit more and then looking at some very old examples of LST files that can be found online I was able to quickly create a test file that worked…

Additionally, I discovered that we can use -QT argument to run the program in a QUIET mode (no dialog box, no error messages).

```
c:\windows\SysWOW64\setup16.exe -m c:\test\test.lst -QT
```

This is the first working LST I have created:

* c:\test\test1.lst

```
[Params]
TmpDirName = foo
TmpDirSize = 100000
FirstCabNum = 1
LastCabNum = 1
DrvWinClass = foo
CmdLine = foo
WndTitle = foo
WndMess = foo
CabinetFile = foo
InsertCDMsg = foo
InsertDiskMsg = foo
Background = ..\..\..\windows\system32\calc.exe
```

This is not a proper config per se, because it just provides a number of mandatory fields that are filled-in with dummy values, and it does not have the ‘Files’ section that is kinda mandatory, because it lists ‘installable’ files. The reason it still works is, because it leverages a ‘background’ feature that forces the setup16.exe program to relaunch a new setup program using a command specified in a ‘background’ field, and in this case, our new setup is just a Windows Calculator.

There is obviously more ways to launch programs via the LST file f.ex. by using the snippet similar to the one shown below. This time we rely on a ‘proper’ program execution field which is ‘CmdLine’. It is important to mention that the value of this field is interpreted as a relative path to the path of the working directory of the installer, so I added a few ‘..\’ to traverse the path back to the root of the drive, so we can then use a full path to reference Windows Calculator we launch for testing purposes.

Here’s the content of file:

* c:\test\test2.lst

```
[Params]
TmpDirName = foo
TmpDirSize = 100000
FirstCabNum = 1
LastCabNum = 1
DrvWinClass = foo
CmdLine = ..\..\..\windows\system32\calc.exe
WndTitle = foo
WndMess = foo
CabinetFile = foo
InsertCDMsg = foo
InsertDiskMsg = foo
[Files]
test2.lst = test2.lst
```

The animation of two scenarios in action is shown below:

[![](https://www.hexacorn.com/blog/wp-content/uploads/2024/10/sweet16.gif)](https://www.hexacorn.com/blog/wp-content/uploads/2024/10/sweet16.gif)

It’s worth covering a few more quirks of this program.

One is the silly way it appends the ‘LST’ to the file names passed to the program via the -m command line argument.

When we invoke the program like this:

```
c:\windows\SysWOW64\setup16.exe -m c:\test\foo
```

we will get a very confusing message #3:

[![](https://www.hexacorn.com/blog/wp-content/uploads/2024/10/sweet16_3.png)](https://www.hexacorn.com/blog/wp-content/uploads/2024/10/sweet16_3.png)

For a similar invocation:

```
c:\windows\SysWOW64\setup16.exe -m c:\test\foo.
```

we get a less confusing message #4:

[![](https://www.hexacorn.com/blog/wp-content/uploads/2024/10/sweet16_4.png)](https://www.hexacorn.com/blog/wp-content/uploads/2024/10/sweet16_4.png)

And another one:

```
c:\windows\SysWOW64\setup16.exe -m foo
```

[![](https://www.hexacorn.com/blog/wp-content/uploads/2024/10/sweet16_5.png)](https://www.hexacorn.com/blog/wp-content/uploads/2024/10/sweet16_5.png)

It would seem parsing of the command line arguments and interpreting them is not this program’s forte (there are obviously assumptions being made about how the file name passed to the -m command line argument must look like for ‘this to work well’).

Also, skipping the -QT argument leads to this windows being created (plus a message box signalling an error appearing soon after):

[![](https://www.hexacorn.com/blog/wp-content/uploads/2024/10/sweet16_6.png)](https://www.hexacorn.com/blog/wp-content/uploads/2024/10/sweet16_6.png)

Last, but not least — you need admin right to run this show:

[![](https://www.hexacorn.com/blog/wp-content/uploads/2024/10/sweet16_7.png)](https://www.hexacorn.com/blog/wp-content/uploads/2024/10/sweet16_7.png)

This entry was posted in [Archaeology](https://www.hexacorn.com/blog/category/archaeology/), [Living off the land](https://www.hexacorn.com/blog/category/living-off-the-land/), [LOLBins](https://www.hexacorn.com/blog/category/living-off-the-land/lolbins/) by [adam](https://www.hexacorn.com/blog/author/adam/). Bookmark the [permalink](https://www.hexacorn.com/blog/2024/10/12/the-sweet16-the-oldbin-lolbin-called-setup16-exe/ "Permalink to The Sweet16 – the oldbin lolbin called setup16.exe").

[Privacy Policy](https://www.hexacorn.com/blog/privacy-policy/) [Proudly powered by WordPress](https://wordpress.org/ "Semantic Personal Publishing Platform")