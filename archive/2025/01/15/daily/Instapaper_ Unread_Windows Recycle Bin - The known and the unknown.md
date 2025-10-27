---
title: Windows Recycle Bin - The known and the unknown
url: https://bebinary4n6.blogspot.com/2025/01/windows-recycle-bin-known-and-unknown.html
source: Instapaper: Unread
date: 2025-01-15
fetch_date: 2025-10-06T20:20:27.391000
---

# Windows Recycle Bin - The known and the unknown

# [Be-binary 4n6](https://bebinary4n6.blogspot.com/)

This is my blog about topics in the field of digital forensics.

## Saturday, January 11, 2025

### Windows Recycle Bin - The known and the unknown

Moin! :-)

Today I write this post about an already really well known artifact of Windows Systems - the Recycle Bin.

Why? Because I had a few more specific questions about the behavior of the recycle bin. I looked for answers to these questions but was not able to find any with a quick search - so I decided to just test it myself.

This post will first give a short overview of the storing mechanism of the recycle bin, something like the well known basics.

After this, I will look into my questions.

My questions were the following:

1. What does happen if the user restores a file?

2. What does happen if a user deletes the same file again after restoring?

3. What does happen if a file is deleted from PowerShell oder CMD?

4. Is there a difference between file systems?

I did the testing on a Windows 10 system. As far as I could see the behavior should by identical to Windows 11.

## The basics

I will only give a short overview of the working without a deep look

As mentioned, I looked at Windows 10 or newer.

For this operating system the Recycle Bin stores two different files for deleted files:

1. The $R file - this file holds the data itself from the deleted file

2. The $I file - this file holds the corresponding meta data for the deleted file

The $I file holds data like the time and date of the deletion in UTC and the original file path and file name. Or, to describe it more correctly, the creation, last accessed and the last write timestamp of the $I file is the deletion timestamp of the original file.

If you have a file with the name "4n6.txt" and delete it, there will be two files in the Recycle Bin directory. One starting with $R, one with $I - and as suffix a 6 char long alphanumeric string. The extension is the same like the original file.

There is one Recycle Bin per partition in Windows. E.g. for drive C: it is c:\$Recycle.Bin

This means first there is an Recycle Bin on every partition.

Additionally, on NTFS file systems, the files in the recycle bin are stored under a folder that is named like the SID of the user who has deleted the file. I will show the difference to FAT32 later in this post. This post won't cover SIDs itself.

And - if the recycle bin is emptied or one specific file is deleted from the recycle bin both files, $I and $R are removed.

I used the tool RBCmd from Eric Zimmerman to do my research - you can find it at <https://ericzimmerman.github.io/#!index.md>

Okay, so let's start with the questions.

#### Restoring a file

What does happen if the user restores a file? I started with a complete empty Recycle Bin.

I deleted three files from my desktop and executed RBCmd with the following output:

[![](https://blogger.googleusercontent.com/img/a/AVvXsEgdq-FTh7cBT4vhMgo-SmEyBWHMC3zayDsxe2tTL8zJwYuCF9OZKMGMh5izhAg5mgHqezWsuAvWioUhc_8jDEIzN3X3-uEG2Vz5XxK66DxnsFhy6waVho01Xss1QBKgrM0ZrmuS4_pAfy2dUoiMMvIBG4NTXYBepbhonl3R960Ew6TUGDbcF1bskFjyjdad=w640-h486)](https://blogger.googleusercontent.com/img/a/AVvXsEgdq-FTh7cBT4vhMgo-SmEyBWHMC3zayDsxe2tTL8zJwYuCF9OZKMGMh5izhAg5mgHqezWsuAvWioUhc_8jDEIzN3X3-uEG2Vz5XxK66DxnsFhy6waVho01Xss1QBKgrM0ZrmuS4_pAfy2dUoiMMvIBG4NTXYBepbhonl3R960Ew6TUGDbcF1bskFjyjdad)

We see in the output the three deleted files are referenced correctly.

Now I restore the files. And re-execute RBCmd with the following output:

[![](https://blogger.googleusercontent.com/img/a/AVvXsEhg8yxObbaDXFWR3C-JJeFki2j4f04i__IH8eG1fSHc0l9rn2Q0oqUrp9k_nLdMYZs8VAfTiGg4PlcriHfdOOiN8usVDAIGU39lgHsRSaZQ0lSPdQ-nVCIwz-Uf8IIkMi6yfZnbAsEV08ml8JY2BngLDr54FtK6scqLAnIlL-dT-EBATGwzGpNVyWDp2uUa=w640-h499)](https://blogger.googleusercontent.com/img/a/AVvXsEhg8yxObbaDXFWR3C-JJeFki2j4f04i__IH8eG1fSHc0l9rn2Q0oqUrp9k_nLdMYZs8VAfTiGg4PlcriHfdOOiN8usVDAIGU39lgHsRSaZQ0lSPdQ-nVCIwz-Uf8IIkMi6yfZnbAsEV08ml8JY2BngLDr54FtK6scqLAnIlL-dT-EBATGwzGpNVyWDp2uUa)

It is the same - this is okay, because the tool parses the $I files. And these files are still there. But the $R files are gone.

I also restarted the system, but without any effect - the $I files are still there.

So, when restoring files, the $I files will stay. This means one can say that a file with a specific name, path and size was deleted in the past and than was restored.

Okay, second question.

#### Deletion of same file after restoring

What does happen if a user deletes the same file again after restoring?

I did a test on another drive with a clean Recycle Bin. First I deleted one file - restored it - deleted it again - RBCmd gives me the following:

[![](https://blogger.googleusercontent.com/img/a/AVvXsEimq7S2mJstX9PFmQBTv2taQ1972N0_dQVFscJW_t0NmuEU2sIEuNnGZq-rtyfhFQpYltkYBfmQ_JdmPrUSIdeKzwkij2MjuHa_Fd8T-j1bUk4VSY6ZFNj-UC4YpJDqb0Pr6tOZICCfUyed9nF9uskHW_3l6g4DoEjBWR8TRZp7FmQZJWq46qHXC9WgTqt0=w640-h398)](https://blogger.googleusercontent.com/img/a/AVvXsEimq7S2mJstX9PFmQBTv2taQ1972N0_dQVFscJW_t0NmuEU2sIEuNnGZq-rtyfhFQpYltkYBfmQ_JdmPrUSIdeKzwkij2MjuHa_Fd8T-j1bUk4VSY6ZFNj-UC4YpJDqb0Pr6tOZICCfUyed9nF9uskHW_3l6g4DoEjBWR8TRZp7FmQZJWq46qHXC9WgTqt0)

As you can see, you have two $I files - different names - but same meta data - except for the deletion timestamp.

This means you can have more than one trace to the same file. For a file you only know the original timestamp, the file path, the file name and the file size. The content is only stored in the $R file.

#### Deletion from Terminal/CMD/Powershell

3. What does happen if a file is deleted via PowerShell or CMD?

When deletion is done from Terminal/Powershell/CMD there will not be any traces in the Recycle Bin. The behavior is similar to Linux - when not using the GUI the files will be deleted directly.

I also tested Double Commander as a different file manager and deleted a file from this app. For Double Commander the normal traces in the Recycle Bin still exist.

#### Different File Systems

So, what I did not mention yet - all testing was done with NTFS as the file system.

Is there a difference to FAT32?

I assumed that this is not the case because I thought the Recycle Bin is written by the Operation System and it is not important what the underlying file system is for the Recycle Bin - perhaps a bit naive.

So, assumptions need to get verified.

I created a FAT32 volume and created a few files and also deleted a few. There was one difference I could see:

On NTFS there was a folder per user in the Recycle Bin with the SID - and in this folder the files ($I and $R) are stored.

ON FAT32 the $I and $R  files are directly stored in the Recycle Bin folder. You do not have any information on the user who has deleted the file in the Recycle Bin. Please find the ouptut of RBCmd of a FAT32 Recycle Bin below:

[![](https://blogger.googleusercontent.com/img/a/AVvXsEgcAm9iHm0DSrsOUWSa1cQX_DMlOXoveiDlqjczYfxh_aVrdxACezlDBNK-4WgYpJnZVhXUoF5T-wGXgOMpeX14J61TWC7qqS2bw6h0hWhFyFMKYXtSMyvr0SthzZsxDSuWVUTBqD98_OvLIiHJWO_JSnHGYwG1QYuxczBtzq15TEj-w6TFgFrWujkbpLHs=w640-h406)](https://blogger.googleusercontent.com/img/a/AVvXsEgcAm9iHm0DSrsOUWSa1cQX_DMlOXoveiDlqjczYfxh_aVrdxACezlDBNK-4WgYpJnZVhXUoF5T-wGXgOMpeX14J61TWC7qqS2bw6h0hWhFyFMKYXtSMyvr0SthzZsxDSuWVUTBqD98_OvLIiHJWO_JSnHGYwG1QYuxczBtzq15TEj-w6TFgFrWujkbpLHs)

#### Conclusion

I had a few specific question and could answer them.

I want to say that you always should use different artifacts to validate results. E.g. you could use the USN journal for validating the deletion of a file. Never trust only one artifact. Look at the whole picture - this post only shows the answers to the really specific questions!

Also, important to say - this post only discusses the behavior of the Recycle Bin - it is not about deletion of files and if they are recoverable or not!

I hope that you also learned a bit and enjoyed your read.

on
[January 11, 2025](https://bebinary4n6.blogspot.com/2025/01/windows-recycle...