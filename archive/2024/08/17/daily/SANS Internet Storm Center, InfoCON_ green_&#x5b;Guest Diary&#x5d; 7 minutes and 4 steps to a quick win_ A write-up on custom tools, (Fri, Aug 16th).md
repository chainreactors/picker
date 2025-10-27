---
title: &#x5b;Guest Diary&#x5d; 7 minutes and 4 steps to a quick win: A write-up on custom tools, (Fri, Aug 16th)
url: https://isc.sans.edu/diary/rss/31170
source: SANS Internet Storm Center, InfoCON: green
date: 2024-08-17
fetch_date: 2025-10-06T18:08:07.694115
---

# &#x5b;Guest Diary&#x5d; 7 minutes and 4 steps to a quick win: A write-up on custom tools, (Fri, Aug 16th)

# [Internet Storm Center](/)

[Sign In](/login.html)
[Sign Up](/register.html)

Handler on Duty: [Johannes Ullrich](/handler_list.html#johannes-ullrich "Johannes Ullrich")

Threat Level: [green](/infocon.html)

* [previous](/diary/31168)
* [next](/diary/31174)

# [[Guest Diary] 7 minutes and 4 steps to a quick win: A write-up on custom tools](/forums/diary/Guest%2BDiary%2B7%2Bminutes%2Band%2B4%2Bsteps%2Bto%2Ba%2Bquick%2Bwin%2BA%2Bwriteup%2Bon%2Bcustom%2Btools/31170/)

**Published**: 2024-08-16. **Last Updated**: 2024-08-16 00:08:23 UTC
**by** [Justin Leibach, SANS BACS Student](/handler_list.html#justin-leibach,-sans-bacs-student) (Version: 1)

[0 comment(s)](/diary/Guest%2BDiary%2B7%2Bminutes%2Band%2B4%2Bsteps%2Bto%2Ba%2Bquick%2Bwin%2BA%2Bwriteup%2Bon%2Bcustom%2Btools/31170/#comments)

[This is a Guest Diary by Justin Leibach, an ISC intern as a part of the SANS.edu BACS [1] degree program]

The web logs from my DShield [2] honeypot always produce the most interesting information. I enjoy being “on keyboard” and using command line tools to view, sort, filter and manipulate the .json files, it is weirdly satisfying. Pounding away on my mechanical keyboard is effective for a single log file, but when I started to zoom out a bit and began looking at multiple days, weeks, even months of information, it became clear there must be a better way.

If you are busy, and need a **TLDR**, here it is: My GitHub [3]
Log files combined: **31**
Lines of JSON parsed: **163,510,310**
Countries of origin: **76**
Script running time: **7 minutes**
Steps from start to finish: **4**

My outputs from running the scripts:

|  |  |
| --- | --- |
| ![](https://isc.sans.edu/diaryimages/images/2024-08-16_figure1_2.png) | ![](https://isc.sans.edu/diaryimages/images/2024-08-16_figure2.png) |
| ***Figure 1: Python .png output depicts percentage of the Top 6 countries of Source IP to interact with honeypot. Percentage is based on 6 countries rather than the entire 76 country dataset.*** | ***Figure 2: Snippet from Python output to excel showing the top 13 countries in descending order.*** |

![](https://isc.sans.edu/diaryimages/images/2024-08-16_figure3.png)
***Figure 3: Screenshot capturing running the script and the printed output of a Python Dictionary holding all countries and occurrences.***

## The endgame

Before I started solving the problem, I needed to define it:
*I want to know what countries are probing my honeypot the most, over time, to develop a better threat intelligence picture.*

Here are the major things I thought I needed to do:

| **Step** | **Description** | **Initial Tool Attempt** | **Final Tool Used** |
| --- | --- | --- | --- |
| 1 | Combine JSON Files | Python | BASH |
| 2 | Filter JSON Files | Python | BASH |
| 3 | Search a database of WHOIS, return country name | Python | Python |
| 4 | Produce graphics for quick analysis | Python | Python |

Ideally, it is also a tool that is highly portable and easily modified for other users, even a very new analyst.

## My Toolbox

|  |  |  |
| --- | --- | --- |
| ![](https://isc.sans.edu/diaryimages/images/2024-08-16_figure4_2.png) | **vs.** | ![](https://isc.sans.edu/diaryimages/images/2024-08-16_figure5_2.png) |
| ***Figure 4: Sample BASH snippet for combining JSON files.*** | ***Figure 5: Sample Python code snippet for combining JSON files.*** |

To solve this problem, I knew I wanted to use Python, but sometimes Bash proves the more elegant solution.

**Python:**

1. **Combine the files**: Small files are no problem, but larger files and datasets could not be processed.
   1. Memory errors abound! No matter my angle of approach, I kept receiving the `killed (program exited with code: 137)`, a memory error.
   2. PATHLIB was just not working for me. Dealing with POSIX paths seemed unwieldy for my approach, and code was quickly becoming very non-pythonic.
   3. OS module wasn’t suitable for my use case, as it would potentially exclude use for Windows users.
2. **Filter the files**: Like my attempt at combining files, small sets worked to some extent but created memory errors for larger files.
3. **Search a WHOIS IP database**: Python was the obvious choice here to find the country of origin.
   1. I used a localized database downloaded from a free service and the `geoip2.database` module.
   2. An API could be used in Python to produce similar results.
4. **Produce graphics**: Python is a language used for data science, so another natural choice.
   1. For the pie chart I used the `matplotlib` and `pillows` module
   2. To create the dataframe and excel document I used the `pandas` and `io` modules.

**Bourne Again Shell (BASH):**

BASH scripting is highly portable, and surprisingly powerful. It is usable on any \*NIX machine, MACOS, or Windows with either WSL or a terminal emulator like Git Bash.

1. **Combine the files**:
   1. Still crashing due to memory issues when only using `jq`
   2. Settled on iterating through them, requiring a quick refresher on BASH “`for`” loops.
2. **Filter the files**:  Straightforward \*NIX tools were able to do this.

Moral of the story here: Use the right tool for the job.

## Combine JSON Files

The script I used to combine the files can be found at GitHub [4].

It takes two user inputs.

1. Filepath: This is a folder with all the web logs you want to combine.
2. Filename: This is what you want it to be named.

The script creates an array with all the file paths, then iterates through that array using the jq utility to append to a single file. The real work in the code is happening here:

```

#!/bin/bash

# Debugging output to check the contents of file_list
echo "Files in file_list:"
for f in "${file_list[@]}"; do
  echo "$f"
done

echo "This may take a while"

# iterate through each file in the file list array and combine it into a single json file using jq.
for file in "${file_list[@]}"; do
  jq -s '.' $file >> $temp
done

# command to remove the all arrays in the JSON file. Necessary to properly filter with jq
cat $temp | jq '.[]' > $filename
```

## Filter JSON Files

Through much trial and error, I found that the best way for python to look through the information was to give it a .csv file. So, I created two BASH scripts to do just that.

The first script filters everything and outputs a .csv file, the only problem with this was the sheer amount of Amazon Web Services (AWS) interactions with my AWS hosted honeypot on AWS LightSail. The second script is an improvement, and more versatile for use in any environment. You can run either.

1. Filter all can be found at GitHub [5]
2. Filtering to exclude IP’s input by user can be found at  GitHub [6]

The second script is a bit more complex. It takes an input of IP addresses and assigns them to a variable. Then the hard part, using sed to search and edit, then using jq to filter and tr to transform that output before finally writing to a user designated filename in the current directory. The bulk of the work in the code is here:

```

# from user input, create variable called $filepath
echo -n "Enter absolute path to JSON file to create new csv for source ip: "
read jsonfilepath

# from user input, create variable called $filename to be used later in writing final merged file
echo -n "What do you want you want your new JSON file to be called (please add .csv)?: "
read csvfilename

# from user inpute, create a variable to exclude ip addresses from the CSV.
# In my case I will exclude any IP address associated with Amazon services, as I am using an AWS honeypot as my source
# Example jq for figuring out top offenders that you would likely exclude: cat Merged.json| jq '.sip' | sort | uniq -c | sort
echo -n "Enter all IP addresses you wish to exclude here, separated by a space: "
echo -e "\nExample: 192.168.1.1 192.168.1.2 192.168.1.3"
read IP_Addresses

# Convert the IP addresses into a jq filter
jq_filter=$(printf 'select(.sip and (%s)) | [.sip] | @csv' "$(echo $IP_Addresses | sed 's/ /" and .sip != "/g' | sed 's/^/.sip != "...