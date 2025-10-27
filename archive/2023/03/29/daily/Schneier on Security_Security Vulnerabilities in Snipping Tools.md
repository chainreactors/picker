---
title: Security Vulnerabilities in Snipping Tools
url: https://www.schneier.com/blog/archives/2023/03/security-vulnerabilities-in-snipping-tools.html
source: Schneier on Security
date: 2023-03-29
fetch_date: 2025-10-04T11:03:18.290077
---

# Security Vulnerabilities in Snipping Tools

# [Schneier on Security](https://www.schneier.com/)

Menu

* [Blog](https://www.schneier.com)
* [Newsletter](https://www.schneier.com/crypto-gram/)
* [Books](https://www.schneier.com/books/)
* [Essays](https://www.schneier.com/essays/)
* [News](https://www.schneier.com/news/)
* [Talks](https://www.schneier.com/talks/)
* [Academic](https://www.schneier.com/academic/)
* [About Me](https://www.schneier.com/blog/about/)

### Search

*Powered by [DuckDuckGo](https://duckduckgo.com/)*

Blog

Essays

Whole site

### Subscribe

[![Atom](https://www.schneier.com/wp-content/uploads/2019/10/rss-32px.png)](https://www.schneier.com/feed/atom/)[![Facebook](https://www.schneier.com/wp-content/uploads/2019/10/facebook-32px.png)](https://www.facebook.com/bruce.schneier)[![Twitter](https://www.schneier.com/wp-content/uploads/2019/10/twitter-32px.png)](https://twitter.com/schneierblog)[![Email](https://www.schneier.com/wp-content/uploads/2019/10/email-32px.png)](https://www.schneier.com/crypto-gram)

[Home](https://www.schneier.com)[Blog](https://www.schneier.com/blog/archives/)

## Security Vulnerabilities in Snipping Tools

Both [Google’s Pixel’s Markup Tool](https://www.bleepingcomputer.com/news/security/google-pixel-flaw-allowed-recovery-of-redacted-cropped-images/) and the [Windows Snipping Tool](https://www.bleepingcomputer.com/news/microsoft/windows-11-snipping-tool-privacy-bug-exposes-cropped-image-content/) have vulnerabilities that allow people to partially recover content that was edited out of images.

EDITED TO ADD (4/14): Steven Murdoch has a [good explanation](https://twitter.com/sjmurdoch/status/1638623990817103888) as to why this happened—and to two very different snipping tools.

Tags: [cybersecurity](https://www.schneier.com/tag/cybersecurity/), [privacy](https://www.schneier.com/tag/privacy/), [vulnerabilities](https://www.schneier.com/tag/vulnerabilities/)

[Posted on March 28, 2023 at 7:13 AM](https://www.schneier.com/blog/archives/2023/03/security-vulnerabilities-in-snipping-tools.html) •
[7 Comments](https://www.schneier.com/blog/archives/2023/03/security-vulnerabilities-in-snipping-tools.html#comments)

### Comments

Vesselin Bontchev •
[March 28, 2023 9:45 AM](https://www.schneier.com/blog/archives/2023/03/security-vulnerabilities-in-snipping-tools.html/#comment-419946)

For an excellent analysis of why this happens in two entirely unrelated code bases, see this thread:

<https://twitter.com/sjmurdoch/status/1638623990817103888>

Clive Robinson •
[March 28, 2023 10:50 AM](https://www.schneier.com/blog/archives/2023/03/security-vulnerabilities-in-snipping-tools.html/#comment-419948)

@ Bruce, ALL,

> “… have vulnerabilities that allow people to partially recover content that was edited out …”

This is effectively true of not just image editing tools, but all edit tools with an undo/recover feature.

From the earliest line editors that “saved edits” through to modern multimedia editors, there are “undo” features of one form or another, because thay’s what falable humans think is a highly desirable feature[1].

Way more than they think “backups” are a desirable feature…

So why should the designers and developers of such tools actually “delete” rather than “not display” how things were?

After all they know that,

“To err is human, and that means that a users shortcomings must by user logic be the designers failure to anticipate.”

So the designers and developers “leave it in” as much as they can…

For a user, who has got their work the way they want it to look, they never stop and think about what they can not see…

The simple fact is there are several ways to solve the “don’t leave anything behind” issue, the easiest being “print out and then photocopy/scan”.

It’s one of the reasons I always say,

“PAPER, Paper, NEVER data…”

And have been saying it since quite a ways back into the last century…

One day maybe… people will learn that their need to have their shortcomings rescued is a sharp double edged sword that cuts both ways…

That is when they need it, and as a consequence, when those who are against them need it…

[1] Way more desirable than making proper backups… Such is “short term thinking” and basic “laziness”…

pedro.frazao •
[March 28, 2023 11:53 AM](https://www.schneier.com/blog/archives/2023/03/security-vulnerabilities-in-snipping-tools.html/#comment-419949)

Probably, this not a bug, only a misalignment of expectations.

All the software for edit photography do a nondestructive editing. Every single photographer expects that.

If a photographer want to share an edited photography, he will export it explicitly, to a new file. This new file will have only the result image.

Clive Robinson •
[March 28, 2023 11:57 AM](https://www.schneier.com/blog/archives/2023/03/security-vulnerabilities-in-snipping-tools.html/#comment-419950)

@ ALL,

The simple version of “a crop alypse” has been around long before the IBM PC existed…

That is it was well known amongst Apple ][ owners, and those with 8080 CP/M machines. The same truncation mark mistake was known to happen on VAX and \*nix OS’s and their predecessors back in the 1960’s and 70’s. And later many programs using non standard C libraries or buffered file writes have done this from the 1970’s onwards[1]. So have been “built in features” of other programing languages (like some implementations of FORTRAN).

When MS-DOS (rip-off of CP/M) came along it had a “text editor”, this used a marker for the end of text of Ctrl-Z. As the Debug “file and memory editor” also came with MS-DOS you could clearly see the “end of text” marker inside the file or memory buffer, as well as the rest of the disk file or buffer end block[2].

So there is nothing in the slightest new in this “bug” method of valid data beyond an end marker, and you would have thought it would be “well known” to developers after around half a century[3]…

Yet as normal in the ICT industry, wr don’t appear to learn from our history…

I guess more people should start asking why?

Especially as I know this end marker problem still exists in many many storage files, and they are not hard to find…

[1] That is as we know a C-string can be any length that will fit in memory. The end of the string is marked by 0x00 ASCII NUL charecter. So if you have a 1024byte long string in a buffer and you only need the first ten bytes writing 0x00 at position 10 is a fast way to do it (ie first position is 0 so 10 is actually the 11th position). However when the buffer gets written out to disk, the fast way is to “write in blocks” so if the storage blocks are 512bytes, then the first half of the original string gets written to storage with the only difference being 0x00 at the 11th position.

[2] Which could be a handy place to put things out of sight, because it would only get overwritten if the file was extended far enough (as FAT-12 gave way to larger FAT’s the size of disk file blocks went up to around 8192bytes so tucking say a password away at the end would probably not get overwritten in a “readme file” that was designed to be well short of a block multiple.

[3] Especially as it’s the way FAT “File Undelete” worked. That is rather than delete a file, MS-DOS just over-wrote the first charecter of the file name in the “File Alocation Table” so undeleting a file was simply a case of usinf Debug to change that first charrcter to a printable ASCII charecter and getting the user to change it to the correct charecter using a DOS of other File manager “rename” option.

Jimbo •
[March 28, 2023 12:15 PM](https://www.schneier.com/blog/archives/2023/03/security-vulnerabilities-in-snipping-tools.html/#comment-419951)

For Windows, why not open the file in paint (which has much better editing), edit as needed and then use snippy to capture the edited image from the screen? Save to a new file (with a new format if needed). Snippy wont have any bytes from the original file so there wont be any reverse editing.

Peter A. •
[March 29, 2023 4:48 AM](https://ww...