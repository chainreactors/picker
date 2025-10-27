---
title: Counting the API arguments…
url: https://www.hexacorn.com/blog/2024/08/07/counting-the-api-arguments/
source: Hexacorn
date: 2024-08-08
fetch_date: 2025-10-06T18:04:04.745003
---

# Counting the API arguments…

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

[← Previous](https://www.hexacorn.com/blog/2024/08/02/the-value-proposition-of-building-and-maintaining-an-internal-threat-hunting-team/)
[Next →](https://www.hexacorn.com/blog/2024/08/13/enter-sandbox-29-the-subtle-art-of-reversing-persuasion-pushing-samples-to-run/)

# Counting the API arguments…

Posted on [2024-08-07](https://www.hexacorn.com/blog/2024/08/07/counting-the-api-arguments/ "9:59 pm")  by  [adam](https://www.hexacorn.com/blog/author/adam/ "View all posts by adam")

Today [Matt](https://x.com/scriptjunkie1) posted a half-joking [twit](https://x.com/scriptjunkie1/status/1821200450080670027) about the acceptable number of arguments that can be passed to a function…

I took the challenge VERY SERIOUSLY and decided to investigate.

In my [old post](https://www.hexacorn.com/blog/2023/10/25/hunting-for-windows-api-prototypes-and-descriptions/) I shared my collections of API prototypes that I had extracted from various Microsoft documentation and other sources over the years; so my task was really easy — analyze this data and find the best candidate APIs that meet the criteria.

I first looked at *2004-2007\_apis.zip* file that included the number of arguments in one of the columns. After merging all this data into a single file, loading it to Excel, and sorting it in a descending order by the number of arguments I immediately [got](https://x.com/Hexacorn/status/1821203420155453679) my first candidate:

* [AccessCheckByTypeResultListAndAuditAlarmByHandle](https://learn.microsoft.com/en-us/windows/win32/api/winbase/nf-winbase-accesscheckbytyperesultlistandauditalarmbyhandlea)

It takes 17 arguments :-O

I then looked at *2013\_apis.zip* file as well — this time I had to write a simple script to parse the file and count number of arguments for each function and then save the results to a file. Same as before, I then loaded it to Excel, sored it in a descending order by the number of arguments and [now](https://x.com/Hexacorn/status/1821204489753317599) I had my final candidate:

* [IDWriteTextAnalyzer::GetGdiCompatibleGlyphPlacements](https://learn.microsoft.com/en-us/windows/win32/api/dwrite/nf-dwrite-idwritetextanalyzer-getgdicompatibleglyphplacements)

– it takes 21 arguments 🙂

Now, there may be other functions that take even more arguments as an input, but I bet they are quite rare. If you find one tough, please let me know and I will update this post.

**Bonus**

The longest api name I have ever encountered is this (1077 characters):

* *ZN5boost12accumulators6detail14build\_acc\_listINS\_6fusion12mpl\_iteratorINS\_3mpl6v\_iterINS5\_6v\_itemINS1\_19accumulator\_wrapperINS0\_4impl18lazy\_variance\_implIdNS0\_3tag4meanEEENSB\_13lazy\_varianceEEENS7\_INS8\_INS9\_11moment\_implIN4mpl\_4int\_ILi2EEEdEENSB\_6momentILi2EEEEENS7\_INS8\_INS9\_11median\_implIdEENSB\_6medianEEENS7\_INS8\_INS9\_22p\_square\_quantile\_implIdNS0\_10for\_medianEEENSB\_28p\_square\_quantile\_for\_medianEEENS7\_INS8\_INS9\_8max\_implIdEENSB\_3maxEEENS7\_INS8\_INS9\_9mean\_implIdNSB\_3sumEEESC\_EENS7\_INS8\_INS9\_8sum\_implIdNSB\_6sampleEEES12\_EENS7\_INS8\_INS9\_10count\_implENSB\_5countEEENS7\_INS8\_INS9\_8min\_implIdEENSB\_3minEEENS5\_7vector0INSH\_2naEEELi0EEELi0EEELi0EEELi0EEELi0EEELi0EEELi0EEELi0EEELi0EEELl0EEEEENS4\_INS6\_IS1R\_Ll9EEEEELb0EE4callINS\_9parameter3aux8arg\_listINS1Z\_15tagged\_argumentINSB\_11accumulatorENS0\_15accumulator\_setIdNS0\_5statsIS1E\_SC\_SZ\_SQ\_SE\_S1H\_S1H\_S1H\_S1H\_S1H\_S1H\_S1H\_S1H\_S1H\_S1H\_S1H\_S1H\_S1H\_S1H\_S1H\_EEvEEEENS1Z\_14empty\_arg\_listEEEEENS3\_4consIS1F\_NS2A\_IS1B\_NS2A\_IS18\_NS2A\_IS14\_NS2A\_IS10\_NS2A\_ISW\_NS2A\_ISR\_NS2A\_ISN\_NS2A\_ISF\_NS3\_3nilEEEEEEEEEEEEEEEEEEERKT\_RKS1T\_RKS1V*

it’s from the sample:

* 8005F35D2C2642B33ADB77CBD100BF64CC7DB611FA789AE18BFFF3F91B26AB40\_4E8BA4874E4D7B99C0BDF31EFBB4051DCDB2F29D

Additionally, the API name that includes the most words in it (11) is:

* AccessCheckByTypeResultListAndAuditAlarmByHandle

This entry was posted in [Archaeology](https://www.hexacorn.com/blog/category/archaeology/), [Silly](https://www.hexacorn.com/blog/category/silly/) by [adam](https://www.hexacorn.com/blog/author/adam/). Bookmark the [permalink](https://www.hexacorn.com/blog/2024/08/07/counting-the-api-arguments/ "Permalink to Counting the API arguments…").

[Privacy Policy](https://www.hexacorn.com/blog/privacy-policy/) [Proudly powered by WordPress](https://wordpress.org/ "Semantic Personal Publishing Platform")