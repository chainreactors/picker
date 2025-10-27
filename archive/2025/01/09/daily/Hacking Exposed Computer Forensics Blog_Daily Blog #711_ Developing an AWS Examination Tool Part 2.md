---
title: Daily Blog #711: Developing an AWS Examination Tool Part 2
url: https://www.hecfblog.com/2025/01/daily-blog-711-developing-aws.html
source: Hacking Exposed Computer Forensics Blog
date: 2025-01-09
fetch_date: 2025-10-06T20:26:12.408120
---

# Daily Blog #711: Developing an AWS Examination Tool Part 2

[![Hacking Exposed Computer Forensics Blog](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhV1r9Fx_K3sKHfI8wnPUPPQFkxWhuxayNz8tT11sG8lYQgY1gGiwV9Qdlfeq-b80FMkRdsOwimMVCo2VbnE0aXyGxaTX1YYhUB5IZ4yK1LhASjfZxFmkAstIM9DnylPabPqQ15WEAFysbZ/s384/unnamed.png)](https://www.hecfblog.com/)

* [Extended Mapi](https://www.hecfblog.com/search/label/extended%20mapi)
* [ObjectID](https://www.hecfblog.com/search/label/objectid)
* [Amcache](https://www.hecfblog.com/search/label/amcache)
* [CTF](https://www.hecfblog.com/search/label/ctf)
* [Python](https://www.hecfblog.com/search/label/python)
* [Syscache](https://www.hecfblog.com/search/label/syscache)
* [Daily Blogs](https://www.hecfblog.com/search/label/Daily%20Blog?max-results=6)
  + [Saturday Reading](https://www.hecfblog.com/search/label/Saturday%20reading)
  + [Solution Saturday](https://www.hecfblog.com/search/label/solution%20saturday)
  + [Forensic Lunch](https://www.hecfblog.com/search/label/forensic%20lunch?&max-results=8)
  + [Sunday Funday](https://www.hecfblog.com/search/label/sunday%20funday?&max-results=8)

[Home](https://www.hecfblog.com/)

[Daily Blog](https://www.hecfblog.com/search/label/Daily%20Blog)

Daily Blog #711: Developing an AWS Examination Tool Part 2

# Daily Blog #711: Developing an AWS Examination Tool Part 2

By
[David Cowen](https://www.blogger.com/profile/17629115910611763170 "author profile")
•
January 07, 2025
•

[AI](https://www.hecfblog.com/search/label/AI?&max-results=8)
[ai programming](https://www.hecfblog.com/search/label/ai%20programming?&max-results=8)
[aws](https://www.hecfblog.com/search/label/aws?&max-results=8)
[Daily Blog](https://www.hecfblog.com/search/label/Daily%20Blog?&max-results=8)
•

Comments :
0

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgzDrZ2_WAzCChzJ-TtYIVUczff8V5q0GTIatCzOcX_BiTZbNsV8XTutKKyjxxqREHudO3qF1u3nCeOdQun7rntKdYpmfH6P4HBs88KwCoMLmbmu3bPNVcLgBDPv47kPCEQPMC06Kijd6Zi6OLyEfw-jwNT_nn3MbElRscdVKdn1MIvZ8knyUagZvP-1T8/w624-h640/awsenum2.webp)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgzDrZ2_WAzCChzJ-TtYIVUczff8V5q0GTIatCzOcX_BiTZbNsV8XTutKKyjxxqREHudO3qF1u3nCeOdQun7rntKdYpmfH6P4HBs88KwCoMLmbmu3bPNVcLgBDPv47kPCEQPMC06Kijd6Zi6OLyEfw-jwNT_nn3MbElRscdVKdn1MIvZ8knyUagZvP-1T8/s1024/awsenum2.webp)

---

**Hello Reader,**

Today, we're making progress on our feature wishlist by tackling several key enhancements:

1. **Selecting Credentials**: Currently, it defaults to my AWS profile for FOR509.
2. **Adding Support for Global Views**.
3. **Exporting Inventory**.

### Step 1: Selecting Credentials

We began by addressing the first feature with the following prompt:

> "Prior to enumerating the AWS account, provide a GUI pop-up that asks how the user wants to authenticate to AWS. Options should include:
>
> 1. Profile in the creds file
> 2. An API key provided by the user
>
> If the user selects a profile, they should see a dropdown of available profiles in the creds file to choose from. If they opt to provide an API key, the system should offer a checkbox to store the key with the collection for easy reuse."

This resulted in an error when I ran the Python code. You might think, "Aha! Your lazy adventure ends here—time to fix the code yourself!" But not so fast, dear reader. Instead, I highlighted the error and prompted:

> "I got this error."

After resolving two more errors using the same prompt, the model managed to fix itself, and I got the GUI functionality I wanted. Now I can either provide a key or choose from any profiles already stored within the AWS CLI.

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEh2bwRdw5mE1qPl_7sBCi1oC91-9hnvwbDiUWdk_IjgGsVcMjs9zChdqnYjo0CwCQkuzGGKQRQs0eIMMhAyVEGGi-ubYpkif1h-V8Cd0PGoiwVAWuSAehP4gPRxn-Wic35ELKdjMXzaJvBZX1Xx7e9w1gHE3Zi5m-ipzDWAsM8EReI0cqQbV5rLhko9g08/s1600/AWSauthprompt.jpg)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEh2bwRdw5mE1qPl_7sBCi1oC91-9hnvwbDiUWdk_IjgGsVcMjs9zChdqnYjo0CwCQkuzGGKQRQs0eIMMhAyVEGGi-ubYpkif1h-V8Cd0PGoiwVAWuSAehP4gPRxn-Wic35ELKdjMXzaJvBZX1Xx7e9w1gHE3Zi5m-ipzDWAsM8EReI0cqQbV5rLhko9g08/s293/AWSauthprompt.jpg)

---

### Step 2: Progress Bars

Next, I wanted to add a progress bar to keep users informed during the enumeration process. Here's how I tackled it:

1. **First Prompt**:

   > "Add a GUI progress window that updates as the account is enumerated so the user knows what is happening."

   This worked, but I wanted more. Since enumerating each region can take time, I added a secondary prompt:
2. **Second Prompt**:

   > "Add a second progress bar for each region, showing what is being enumerated."

This introduced a new issue—the progress window popped up but displayed no updates. I informed the model:

> "The progress window popped up, but there were no updates displayed."

The model refactored the code to enable real-time GUI updates while enumeration was running. Voilà! A neat dual-progress bar system was now functional.

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhl2nawllPPLmvAsqEPMh7zfK48M5PDi5sU2U8T1KG6xqOrH6byv-keVjpIkN5b-wH3IG8v5sPK_sEuXO8nhzbGGkK3U7EVvA7Np97W2nICQcDiczT_Q_mGUjj-m6-5Wpdcnu_vuNANSBA1fYkmMw-4-D22N84zStePctR0o4TWgkp6uK-0VVAZ6cTQtec/s320/awsprogressbar.jpg)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhl2nawllPPLmvAsqEPMh7zfK48M5PDi5sU2U8T1KG6xqOrH6byv-keVjpIkN5b-wH3IG8v5sPK_sEuXO8nhzbGGkK3U7EVvA7Np97W2nICQcDiczT_Q_mGUjj-m6-5Wpdcnu_vuNANSBA1fYkmMw-4-D22N84zStePctR0o4TWgkp6uK-0VVAZ6cTQtec/s399/awsprogressbar.jpg)

---

### Step 3: Region Resource Count

To enhance the user experience further, I requested:

> "Add a number next to each listed region summarizing how many resources were found in that region."

This worked beautifully, providing a clear overview of resource counts per region.

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhweHbFdxwi7ke-hJvgK7XsLu51Uo_hMCy0EsfgVwEvFvKyjCqWRZjdZMzW86NLIABBs8l7kqosn6ELBlhAIMmtAceLt3SjDZ3v6kC68aLiHbEXJA-wYOz_mocbFsANsUo5usJcdbgnNojsVj4LA_XGiORUloa3Xfz0LjHTV-1Xh3Q-568BYP3Y3UbEKMU/s320/awsregioncount.jpg)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhweHbFdxwi7ke-hJvgK7XsLu51Uo_hMCy0EsfgVwEvFvKyjCqWRZjdZMzW86NLIABBs8l7kqosn6ELBlhAIMmtAceLt3SjDZ3v6kC68aLiHbEXJA-wYOz_mocbFsANsUo5usJcdbgnNojsVj4LA_XGiORUloa3Xfz0LjHTV-1Xh3Q-568BYP3Y3UbEKMU/s431/awsregioncount.jpg)

---

### Step 4: Exporting Inventory

For the final item on today's list, I wrote a more detailed prompt:

> "Create a toolbar option called 'Export.' When selected, it should open a dialog asking the user to save the output in one of three formats: text (as displayed), JSON, or XLSX. After selecting the format, present a window to choose a save location and filename. The default filename should include the AWS Account ID and the current timestamp, keeping it unique with the chosen extension. Then export all regions' data to the selected file."

This feature worked on the **very first attempt**! The code automatically added `pandas` and `openpyxl` packages to support Excel output.

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhhEwcZayeIBGTmoUNJ62DOKqCQdGRJZeWHrNRgrz5l4TK8rlV1qHrumfO04rNLBNSxUy88NB2HJeeks34asJRQ8tZb2MWvnr-A3wPVZzrQ7xRZhTJxRL8_p-BLOy7SRBlosFqXwTweQOAn0RfgLFOLbRiTB26fkpSV_jrYub-zITtW5Va4t2H7Xbcs0fk/s320/awsexport.jpg)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhhEwcZayeIBGTmoUNJ62DOKqCQdGRJZeWHrNRgrz5l4TK8rlV1qHrumfO04rNLBNSxUy88NB2HJeeks34asJRQ8tZb2MWvnr-A3wPVZzrQ7xRZhTJxRL8_p-BLOy7SRBlosFqXwTweQOAn0RfgLFOLbRiTB26fkpSV_jrYub-zITtW5Va4t2H7Xbcs0fk/s436/awsexport.jpg)

---

### Step 5: Finishing Touches

To wrap things up, I asked the model to create essential project files:

1. **Requirements File**:

   > "Create a `requirements.txt` file with all the necessary packages."
2. **GitHub README**:

   > "Create a README file in Markdown syntax that describes the project, how to install it, how to execute it, and includes an Apache 2 license."

Finally, I pushed the project to its ...