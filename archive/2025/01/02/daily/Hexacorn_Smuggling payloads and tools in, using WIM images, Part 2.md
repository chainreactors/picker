---
title: Smuggling payloads and tools in, using WIM images, Part 2
url: https://www.hexacorn.com/blog/2025/01/01/smuggling-payloads-and-tools-in-using-wim-images-part-2/
source: Hexacorn
date: 2025-01-02
fetch_date: 2025-10-06T20:06:54.099844
---

# Smuggling payloads and tools in, using WIM images, Part 2

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

[← Previous](https://www.hexacorn.com/blog/2024/12/31/clean-hash-set-12m-rows/)
[Next →](https://www.hexacorn.com/blog/2025/01/25/being-a-tool-while-using-a-tool/)

# Smuggling payloads and tools in, using WIM images, Part 2

Posted on [2025-01-01](https://www.hexacorn.com/blog/2025/01/01/smuggling-payloads-and-tools-in-using-wim-images-part-2/ "12:09 am")  by  [adam](https://www.hexacorn.com/blog/author/adam/ "View all posts by adam")

In this post we explore the *dism.exe* and WIM [images](https://www.hexacorn.com/blog/2024/12/28/wimmountdata-ads/) [a bit](https://www.hexacorn.com/blog/2024/12/31/smuggling-payloads-and-tools-in-using-wim-images/) more.

It turns out that WIM files are containers that can include more than one image. One can create the first image using the /Capture-Image option, and then append new images to the same WIM file using the /Append-Image command line argument.

In a test scenario, I created 3 subfolders containing:

* Image1 – Sysmon
* Image2 – Eicar
* Image3 – Mimikatz

I then created a multi-image *newtest.wim* file using the following syntax:

```
Dism /Capture-Image /ImageFile:”newtest.wim” /CaptureDir:image1_sysmon /Name:sysmon
Dism /Append-Image  /ImageFile:”newtest.wim” /CaptureDir:image2_eicar /Name:eicar
Dism /Append-Image  /ImageFile:”newtest.wim” /CaptureDir:image3_mimikatz /Name:mimikatz
```

To confirm the images were added to the *newtest.wim* file, I ran these commands:

```
dism /list-image /imagefile:"newtest.wim" /index:1
dism /list-image /imagefile:"newtest.wim" /index:2
dism /list-image /imagefile:"newtest.wim" /index:3
```

[![](https://www.hexacorn.com/blog/wp-content/uploads/2024/12/list_image.png)](https://www.hexacorn.com/blog/wp-content/uploads/2024/12/list_image.png)

I was a bit surprised the ADSs were not listed.

Luckily, 7z lists a bit more information:

[![](https://www.hexacorn.com/blog/wp-content/uploads/2024/12/wim_7z_list_files.png)](https://www.hexacorn.com/blog/wp-content/uploads/2024/12/wim_7z_list_files.png)

The content of *[1].xml* is forensically interesting:

```
<WIM>
 <TOTALBYTES>2122196</TOTALBYTES>

 <IMAGE INDEX="1">
  <DIRCOUNT>0</DIRCOUNT>
  <FILECOUNT>1</FILECOUNT>
  <TOTALBYTES>4563248</TOTALBYTES>
  <HARDLINKBYTES>0</HARDLINKBYTES>
  <CREATIONTIME>
   <HIGHPART>0x01DB5BD0</HIGHPART>
   <LOWPART>0x5FAF914D</LOWPART>
  </CREATIONTIME>
  <LASTMODIFICATIONTIME>
   <HIGHPART>0x01DB5BD0</HIGHPART>
   <LOWPART>0x5FB40FD8</LOWPART>
  </LASTMODIFICATIONTIME>
  <WIMBOOT>0</WIMBOOT>
  <NAME>sysmon</NAME>
 </IMAGE>

 <IMAGE INDEX="2">
  <DIRCOUNT>0</DIRCOUNT>
  <FILECOUNT>1</FILECOUNT>
  <TOTALBYTES>68</TOTALBYTES>
  <HARDLINKBYTES>0</HARDLINKBYTES>
  <CREATIONTIME>
   <HIGHPART>0x01DB5BD0</HIGHPART>
   <LOWPART>0x6DB1F772</LOWPART>
  </CREATIONTIME>
  <LASTMODIFICATIONTIME>
   <HIGHPART>0x01DB5BD0</HIGHPART>
   <LOWPART>0x6DB6281B</LOWPART>
  </LASTMODIFICATIONTIME>
  <WIMBOOT>0</WIMBOOT>
  <NAME>eicar</NAME>
 </IMAGE>

 <IMAGE INDEX="3">
  <DIRCOUNT>0</DIRCOUNT>
  <FILECOUNT>4</FILECOUNT>
  <TOTALBYTES>1440600</TOTALBYTES>
  <HARDLINKBYTES>0</HARDLINKBYTES>
  <CREATIONTIME>
   <HIGHPART>0x01DB5BD0</HIGHPART>
   <LOWPART>0x6FE89BE7</LOWPART>
  </CREATIONTIME>
  <LASTMODIFICATIONTIME>
   <HIGHPART>0x01DB5BD0</HIGHPART>
   <LOWPART>0x6FEDA2E8</LOWPART>
  </LASTMODIFICATIONTIME>
  <WIMBOOT>0</WIMBOOT>
  <NAME>mimikatz</NAME>
 </IMAGE>
</WIM>
```

I was also curious how the file will be ‘seen’ by VT, so I submitted it [here](https://www.virustotal.com/gui/file/2dbeac07a022fff3a6bdcb2de0801e6d120c8123b27d43d183f03c6c42c1d01b). To my surprise, we got multiple different detections, hitting on different internal images – either Eicar or Mimikatz (I was hoping that my first image, sysmon, will help to bypass most of the scans – I was wrong):

[![](https://www.hexacorn.com/blog/wp-content/uploads/2024/12/wim_multiple_images_vt_test-1024x291.png)](https://www.hexacorn.com/blog/wp-content/uploads/2024/12/wim_multiple_images_vt_test.png)

Coming back to the newly created file, *newtest.wim*, it’s important to mention that apart from the multiple images it can host, it can also be split into smaller chunks (same as 7z, zip, or rar archives).

Running the following command:

```
dism /split-image /imagefile:"newtest.wim" /SWMFile:"newtest.swm" /FileSize:1
```

will split our *newtest.wim* file into 3 swm files:

```
    4,435 newtest.swm
1,417,386 newtest2.swm
  704,883 newtest3.swm
    2,126,704 bytes
```

I am not sure I follow how the 1M boundary I asked for led to creation of these 3 files with file sizes looking quite random, but one way or another, an ability to split a WIM file into SWM file chunks may come handy.

They certainly come handy when it comes to bypassing VT detections:

* [newtest.swm](https://www.virustotal.com/gui/file/11234fe904c17815913cd040b97269ce841255f42f45c96d14996a29d581bd1c) – 0
* [newtest2.swm](https://www.virustotal.com/gui/file/2de82e10cc8e413ebb0c1d002e20d95b8992ae63d9f95d1e210e953c1dbfe76d) – 0
* [newtest3.swm](https://www.virustotal.com/gui/file/48a0d9526ebce6ec07b1b60c20e3fbf470b69a9274ec0ae2bc059a37ca002610) – … or… not… yup, okay, we are still getting caught:

[![](https://www.hexacorn.com/blog/wp-content/uploads/2024/12/swm3_vt_test-1024x293.png)](https://www.hexacorn.com/blog/wp-content/uploads/2024/12/swm3_vt_test.png)

The last bit I want to quickly cover here is the /EA command line argument that we can use during image creation (/Capture-Image). The default behavior for the /Capture-Image is to collect both files, and their Alternate Data Streams, but /EA options extends the collection to Extended Attributes as well. This enables us to ‘outsource’ hiding data and payloads (in either ADS or EAs) to *dism.exe* process, as all the mounting-related, but ‘dodgy’ file system ‘object creation’ activities will be associated with this process only.

I think *dism.exe* is a tool that ended up being overlooked by many of us, but I hope we will all pay more attention to it now… This Microsoft [page](https://learn.microsoft.com/en-us/windows-hardware/manufacture/desktop/dism-image-management-command-line-options-s14?view=windows-11) describes this tool’s command line arguments in great detail.

Happy hunting!

This entry was posted in [Archaeology](https://www.hexacorn.com/blog/category/archaeology/), [Forensic Analysis](https://www.hexacorn.com/blog/category/forensic-analysis/) by [adam](https://www.hexacorn.com/blog/author/adam/). Bookmark the [permalink](https://www.hexacorn.com/blog/2025/01/01/smuggling-payloads-and-tools-in-using-wim-images-part-2/ "Permalink to Smuggling payloads and tools in, using WIM images, Part 2").

[Privacy Policy](https://www.hexacorn.com/blog/privacy-policy/) [Proudly powered by WordPress](https://wordpress.org/ "Semantic Personal Publishing Platform")