---
title: Stuffing up the WINDIR env. var. with THE SPACE
url: https://www.hexacorn.com/blog/2024/03/16/stuffing-up-the-windir-env-var-with-the-space/
source: Hexacorn
date: 2024-03-17
fetch_date: 2025-10-04T12:09:12.172348
---

# Stuffing up the WINDIR env. var. with THE SPACE

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

[← Previous](https://www.hexacorn.com/blog/2024/03/16/lolbin-wow-ltd-x-2/)
[Next →](https://www.hexacorn.com/blog/2024/03/31/subfrida-v0-1/)

# Stuffing up the WINDIR env. var. with THE SPACE

Posted on [2024-03-16](https://www.hexacorn.com/blog/2024/03/16/stuffing-up-the-windir-env-var-with-the-space/ "11:40 pm")  by  [adam](https://www.hexacorn.com/blog/author/adam/ "View all posts by adam")

I love revisiting the ‘there is nothing else to be found there anymore’ cases and I described this process [here](https://www.hexacorn.com/blog/2024/01/21/how-to-become-continue-to-be-a-security-researcher/).

Recently, I’ve been thinking of the WINDIR environment variable. I have already [covered](https://www.hexacorn.com/blog/2020/05/23/lolbin-wow-ltd/) a few [cases](https://www.hexacorn.com/blog/2020/05/23/lolbin-ltd/) [where](https://www.hexacorn.com/blog/2024/03/16/lolbin-wow-ltd-x-2/) WoW executables could be forced to execute any executable of our choice after the WINDIR environment variable modification, but it crossed my mind that we may try something new…

If you google what the environment variable maximum length is you will discover it is (allegedly) 32,767 characters. Luckily, Raymond Chan wrote this [post](https://devblogs.microsoft.com/oldnewthing/20100203-00/?p=15083) that gives us a bit more (reliable) insight.

So, my thinking was … if I can force the WINDIR environment variable to fill-in the whole space used by the environment variables…. then in cases where it is used to expand a path (f.ex. for the 64-bit executable from the WoW 32-bit executable level as in cases I linked to above), there may be some path truncation happening that will render the ‘expanded’ version of the path in some unpredictable way… That is, I was hoping that if the WINDIR is long enough f.ex. close to the alleged maximum length of 32K characters, then the rest of the path would be truncated, potentially giving us an opportunity to literally run any executable on the system this way…

That didn’t happen 🙁

After playing around with it I eventually gave up. No truncation occurred, and while results were dependent on the WoW executable I tested (*msra.exe*, *w32tm.exe*, *launchtm.exe*), I have not identified a way to exploit this in any way.

However…

I do want to showcase one interesting observation from this attempt.

The *msra.exe* was a very interesting study.

I generated a [batch file](https://hexacorn.com/d/long_env_var_windir.bat) that was nearly 65K in size. It’s just a rather lengthy *SET WINDIR=<~64K spaces>..\..\windows\notepad.exe*.

So, I ran it from *cmd.exe* terminal, and then executed *c:\WINDOWS\SysWOW64\msra.exe*.

To my surprise, the program ran! Despite the fact that the WINDIR environment variable was far bigger than the alleged maximum environment block size!

Secondly, while it took a few seconds for the *msra.exe* to load, it did eventually show an interesting message box as an indication of an error:

[![](https://www.hexacorn.com/blog/wp-content/uploads/2024/03/long_env_var_windir_msra-546x1024.gif)](https://www.hexacorn.com/blog/wp-content/uploads/2024/03/long_env_var_windir_msra.gif)

The lessons learned is that the environment block can be far larger than 32K!

Using System Informer/Process Hacker we can look at the *msra.exe* process environment block, and here it is — a WINDIR variable taking ~64K:

[![](https://www.hexacorn.com/blog/wp-content/uploads/2024/03/env_var_windir_si_screenshot.png)](https://www.hexacorn.com/blog/wp-content/uploads/2024/03/env_var_windir_si_screenshot.png)

(you can select all, copy it to clipboard, then paste it in Notepad, save file and check file size).

What this example teaches is that you should trust, but verify.

And it’s still possible I missed something and WINDIR or many other environment variables can be abused to do things no one ever considered…

This entry was posted in [Research fails](https://www.hexacorn.com/blog/category/research-fails/) by [adam](https://www.hexacorn.com/blog/author/adam/). Bookmark the [permalink](https://www.hexacorn.com/blog/2024/03/16/stuffing-up-the-windir-env-var-with-the-space/ "Permalink to Stuffing up the WINDIR env. var. with THE SPACE").

[Privacy Policy](https://www.hexacorn.com/blog/privacy-policy/) [Proudly powered by WordPress](https://wordpress.org/ "Semantic Personal Publishing Platform")