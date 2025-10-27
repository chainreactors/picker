---
title: Excelling at Excel, Part 2
url: https://www.hexacorn.com/blog/2023/01/08/excelling-at-excel-part-2/
source: Hexacorn
date: 2023-01-09
fetch_date: 2025-10-04T03:21:35.706303
---

# Excelling at Excel, Part 2

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

[← Previous](https://www.hexacorn.com/blog/2023/01/07/excelling-at-excel-part-1/)
[Next →](https://www.hexacorn.com/blog/2023/01/13/decrypting-shell-compiled-shc-elf-files/)

# Excelling at Excel, Part 2

Posted on [2023-01-08](https://www.hexacorn.com/blog/2023/01/08/excelling-at-excel-part-2/ "12:01 am")  by  [adam](https://www.hexacorn.com/blog/author/adam/ "View all posts by adam")

Today I will talk about automated query-building using Excel.

Working as a detection engineering and/or threat hunting specialist we often need to create a lot of queries including a lot of repetitive conditions that follow a very similar syntax. It’s not pretty. It’s not easy to manage. We can do better.

For instance, if our logs refer to process image names (names of the files that are used to launch processes), and we want to write a query that focuses on a bunch of well-known browser processes, and browser file names we have looks like the list below:

* chrome.exe
* firefox.exe
* brave.exe
* iexplore.exe
* microsoftedge.exe
* microsoftedgecp.exe
* opera.exe
* qqbrowser.exe
* 360se.exe
* 360chrome.exe
* sogueexplorer.exe
* maxthon.exe
* vivaldi.exe
* epic.exe
* safari.exe

it may be tempting to write all these query conditions referring to all these process names manually. That is, for every process name listed, you may type something like:

```
image_file_name="*\\chrome.exe" OR
image_file_name="*\\firefox.exe" OR
etc.
```

With Excel, it is an easy task to create a formula that will generate this code for us automagically:

[![](https://www.hexacorn.com/blog/wp-content/uploads/2023/01/exc_2_1-1.png)](https://www.hexacorn.com/blog/wp-content/uploads/2023/01/exc_2_1-1.png)

You type the formula in B1, then populate next rows with CTRL+D.

The result (flip between formulas and values using CTRL+`) looks like this:

[![](https://www.hexacorn.com/blog/wp-content/uploads/2023/01/exc_2_2-1.png)](https://www.hexacorn.com/blog/wp-content/uploads/2023/01/exc_2_2-1.png)

There are many benefits of using Excel to simplify this mundane task – the primary benefit being that it helps us to separate input data (process names of interest) from the actual code/query. It also forces us to keep a list of all browser-related process names in a column A, and the auto-generated code automagically populates the column B. That is, anytime we add a new process name, we can autogenerate code for another condition by simply extending the formula in column B to the next row!

If you are working on automation a lot you may criticize the approach. Why do we even need Excel if we could simply keep a dedicated text file listing all the process names of interest (browsers, or whatever), and then have them ingested by a scheduled task that builds the new query on-the-fly using f.ex. a python script that combines a query template with a dynamically built list of conditions. You are spot on. If you are that far ahead, please carry on. Still, admittedly, if we want to keep everyone happy, why don’t we keep that list in a shared Excel file so it’s easy to add entries to it using a desktop application or a web-based GUI instead of vim or emacs 🙂 — the easier it is for \_anyone\_ to add to this list, the more engagement and participation from your team members in enriching this list you will see. And extracting data from Excel using python, perl, or whatever is supereasy. So, data input for automation can be done in the Excel, while all the gore automation bit can be done in any language we like. Win-Win.

Coming back to our Excel exercise… if you are a good observer, you have probably noticed that the last row still includes the ‘ OR’ at the end, which will obviously cause a syntax error in a larger formula (f.ex. in Splunk’s SPL). You can simply delete the last ‘ OR’ manually after copying the conditions to the Splunk query window, or improve the formula to add ‘ OR’ at the end of the line only if the next row includes a process name in a column A, f.ex.:

[![](https://www.hexacorn.com/blog/wp-content/uploads/2023/01/exc_2_3.png)](https://www.hexacorn.com/blog/wp-content/uploads/2023/01/exc_2_3.png)

resulting in:

[![](https://www.hexacorn.com/blog/wp-content/uploads/2023/01/exc_2_4.png)](https://www.hexacorn.com/blog/wp-content/uploads/2023/01/exc_2_4.png)

We can control the output of such automagically generated code in any way we want. It’s just a matter of writing a proper (sometimes complex) formula.

Apart from all the benefits outlined above, there is one more — by generating queries in an auto-magical way we are avoiding a lot of data entry errors. Not only we are avoiding typos, incorrectly escaped characters, we are also avoiding costly business logic errors which sometimes occur when we put one too many of, or simply miss one ‘ OR’ or ‘ AND’ in long queries — these mistakes may change the logic of the query in a very subtle way leading to many hours of troubleshooting.

The other area where Excel and queries created ‘automagically’ from the input data may be useful is a database of regular expressions. When we threat hunt we use regular expressions a lot. The most naive and traditional approach of using them relies on copypasta (sometimes done wrong!) where the input are old/existing queries, often not even ours, and we can of course do better than that.

What if we designate a single Excel sheet that stores them all, in a plain-vanilla form, peer-reviewed though, and then we can cherry-pick them from the list as we wish, knowing they are solid, reliable, tested, and we may also ensure the sheet includes sample queries relying on these regular expressions, f.ex.:

[![](https://www.hexacorn.com/blog/wp-content/uploads/2023/01/exc_2_6-1024x113.png)](https://www.hexacorn.com/blog/wp-content/uploads/2023/01/exc_2_6.png)

In the interest of full disclosure — I created this just for this article, so there may be some typos, but if you look at this, you probably get the idea. One place for all regexes -> less chances in reinventing the wheel anytime we come across the same problem data parsing/extraction in the future.

There are two classes of regular expressions listed on the screenshot:

* the top ones are used for tokenization that relies on replacing a part of a data input with a token — very useful when we want to normalize some data f.ex. paths or process command line arguments (f.ex. in Least-Frequency Analysis)
* the bottom ones are extraction regular expressions — they take the input and extract a part of it giving us more context or more meaningful way to analyze data

If you are curious how the entries shown above look like in ‘formulas’ mode (CTRL+`), have a look at this:

[![](https://www.hexacorn.com/blog/wp-content/uploads/2023/01/exc_2_5-1-1024x107.png)](https://www.hexacorn.com/blog/wp-content/uploads/2023/01/exc_2_5-1.png)

Again, you may have an immediate knee-jerk reaction now telling you that it’s silly to do it this way, and there are better, more efficient ways to do it. And again I must say — you are way ahead — and this article is probably not for you 🙂

Using Excel right helps us to build processes at first, and then build better processes. These then can be automated, and they really should be.

This entry was posted in [Excel](https://www.hexacorn.com/blog/category/excel/) by [adam](https://www.hexacorn.com/blog/author/adam/). Bookmark the [permalink](https://www.hexacorn.com/blog/2023/01/08/excelling-at-excel-part-2/ "Permalink to Excelling at Excel, Part 2").

[Privacy Policy](https://www.hexacorn.com/blog/privacy-policy/) [Proudly powered by Wor...