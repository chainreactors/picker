---
title: Reading Location Position Value in Microsoft Word Documents, (Mon, Aug 25th)
url: https://isc.sans.edu/diary/rss/32224
source: SANS Internet Storm Center, InfoCON: green
date: 2025-08-26
fetch_date: 2025-10-07T00:49:19.317486
---

# Reading Location Position Value in Microsoft Word Documents, (Mon, Aug 25th)

# [Internet Storm Center](/)

[Sign In](/login.html)
[Sign Up](/register.html)

Handler on Duty: [Johannes Ullrich](/handler_list.html#johannes-ullrich "Johannes Ullrich")

Threat Level: [green](/infocon.html)

* [previous](/diary/32220)
* [next](/diary/32228)

# [Reading Location Position Value in Microsoft Word Documents](/forums/diary/Reading%2BLocation%2BPosition%2BValue%2Bin%2BMicrosoft%2BWord%2BDocuments/32224/)

**Published**: 2025-08-25. **Last Updated**: 2025-08-25 00:09:14 UTC
**by** [Jesse La Grew](/handler_list.html#jesse-la-grew) (Version: 1)

[0 comment(s)](/diary/Reading%2BLocation%2BPosition%2BValue%2Bin%2BMicrosoft%2BWord%2BDocuments/32224/#comments)

While studying for the GX-FE [1], I started exploring the "**Position**" value in the registry that helps to tell Microsoft Word where you "left off". It's a feature many people that use Word have seen on numerous occasions and is explored in FOR500: Windows Forensic Analysis [2].

**![](https://isc.sans.edu/diaryimages/images/2025-08-25_figure1.PNG)
Figure 1: Word pop-up offering to continue at last location, which is assited by "Position" registry value.**

.

For example, my registry has the following registry information for a test document I created:

```

Windows Registry Editor Version 5.00

[HKEY_CURRENT_USER\Software\Microsoft\Office\16.0\Word\Reading Locations\Document 20]
"File Path"="C:\\Users\\sans_isc\\Documents\\Testing Word Reading Locations.docx"
"Datetime"="2025-08-23T14:39"
"Position"="493796625 5462"

```

There are two numbers associated with the "**Position**" value. Experimentation suggests that the second number in this value is the character count position from the start of the document. I wasn't sure about the first value until I ran along a different article exploring this topic [3].

**![](https://isc.sans.edu/diaryimages/images/2025-08-25_figure2_v2.PNG)
Figure 2: Example value of "Position".**

Phill Moore noticed that the first portion of this value was the "`w14:paraId`", which can be seen in the raw XML of the Word document. Their article helped me understand something I didn't understand from my data during testing. I didn't know why this first number value changed when I was testing. The value seemed static until at some arbitrary point it changed, but then it didn't change anymore after that. It turns out that the document I randomly copied text into had a paragraph break. To create the test document, I copied and pasted text multiple times and at some point had created a new paragraph by hiting enter around page 4. Phill had also suggested that the second value in the "Position" could be character count, which is supported experimentally.

## Experimentation

First, a document was created by copying and pasting text into a Word document. After this, I experimented by opening and closing the document in a variety of ways to understand how the values changed within the registry. After each opening of the document, the "Pick up where you left off" option was used.

|  |  |  |  |
| --- | --- | --- | --- |
| **Starting "Position" Value** | **Action Taken After Opening Document** | **Ending "Position" Value** | **Notes** |
| 493796625 0 | Scroll wheel down 2 clicks | 493796625 0 | First line of text still visible |
| 493796625 0 | Scroll wheel down 3 clicks | 493796625 181 | Second line now the pop-most line visible |
| 493796625 181 | Scrolled down to page 3, left-clicked on line 9 column 55 | 493796625 6698 |  |
| 493796625 6698 | Left-clicked at end of line 1 on page 3 | 493796625 6698 | Document opened on first line of page 3, cursor at start |
| 493796625 6698 | Scroll wheel down 4 clicks, left clicked at end of line 14 | 493796625 7228 | Document opened on first line of page 3, cursor at start |
| 493796625 7228 | No action taken | 493796625 7228 |  |
| 493796625 7228 | Scroll wheel down 2 clicks | 493796625 7406 |  |

**Figure 3: Results from experimenting with different cursor and viewable area placement**

The data demonstrates the second value increasing when scrolling down, although it only increments when the top-most viewable line changes. But what is the value incease? When looking at the differences in the two values, it appears that it's the number of characters that were no longer viewable.

**![](https://isc.sans.edu/diaryimages/images/2025-08-25_figure3.PNG)
Figure 4: Text highlighted that's missing after clicking a scroll wheel down once in Word.**

**![](https://isc.sans.edu/diaryimages/images/2025-08-25_figure5_v2.PNG)
Figure 5: Character count [4] of text matches difference between the second portions of two "Position" values from the registry.**

This helps give a bit more confidence that the second value in for "**Position**" may be the character count. What if we change the "**Position**" value to something that only sets a character count?

|  |  |  |  |
| --- | --- | --- | --- |
| **Starting "Position" Value** | **Action Taken After Opening Document** | **Ending "Position" Value** | **Notes** |
| 0 16542 | No action taken | 55341811 16525 | Was given option to continue from last location  Opened at page 5, line 36, column 18 |

**Figure 6: Experimentation with only setting a non-zero value for second portion of "Position" value.**

**![](https://isc.sans.edu/diaryimages/images/2025-08-25_figure5.PNG)
Figure 7: Starting cursor location upon opening Word document with randomly specified "Position" value in second number position.**

**![](https://isc.sans.edu/diaryimages/images/2025-08-25_figure6.PNG)**

**Figure 8: Starting cursor location after closing and reopening Word document with randomly specified "Position" value in second number position.**

The value of the second number in the "**Position**" field ***is*** the cusor location, but Word appears to set this value to the beginning of the first visible line within Word. This is one reason that the values many not change, even if the cusor is relocated. The value only changes once the top most visible line within Word changes.

You may have noticed that the first value is also different now. This is the new **`w14:paraId`** value that can be seen within the `document.xml` file when the document is extracted using a look like 7-zip (within `word/document.xml`). Unfortunately, this value format is different in the document (hex) than it is in the registry (decimal).

**![](https://isc.sans.edu/diaryimages/images/2025-08-25_figure7.PNG)
Figure 9: w14:paraId value in document.xml compared with the registry "Position" value data when the value from document.xml is converted from hex to decimal.**

What if only the first number value is set (`w14:paraId`)?

|  |  |  |  |
| --- | --- | --- | --- |
| **Starting "Position" Value** | **Action Taken After Opening Document** | **Ending "Position" Value** | **Notes** |
| 55341811 0 | No action taken | 55341811 0 | Was ***not*** given option to continue from last location  Opened at the beginning of page 1 |

**Figure 10: Setting the first number within "Position" to a valid w14:paraId value does not skip to that paragraph.**

This character value is needed to properly position the last viewed location for a document in Word. If an invalid `w14:paraId` is specified with a valid number of characters from start of the document, the continuation feature still functions within Word. From this experiment, the first value may not be used for this continuation feature, but is recorded based on the viewable location in Word at the time Word was closed.

To use this "**Position**" value in forensics, a test system can be set up with the appropriate registry information and the corresponding file can be opened to determine where in the file someone was reading when Word was closed. Programatically, this new information could be used to start extracting data from the Word document at the point of last viewing, which may save some time.

Can you think of any other use for this information? Did someone else figure this out and I just couldn't find i...