---
title: Google Drive Forensics
url: https://blog.cyber5w.com/Google-Drive-Forensics.html
source: Instapaper: Unread
date: 2024-07-19
fetch_date: 2025-10-06T17:43:54.777825
---

# Google Drive Forensics

[![CYBER 5W](/images/logo.png)](/)

## Menu

* [Home](https://www.cyber5w.com/)
* [Blog](/)
* [Academy](https://academy.cyber5w.com/)
* [About](/about/)
* [Contact Us](/contact/)

* [Home](https://www.cyber5w.com/)
* [Blog](/)
* [Academy](https://academy.cyber5w.com/)
* [About](/about/)
* [Contact Us](/contact/)

Search

Search for Blog

![Google Drive Forensics](/images/driveforensics/cover.png)

3 min read
Jul 11, 2024

## Google Drive Forensics

[![Cyber 5W's Picture](https://avatars.githubusercontent.com/u/80437140?s=328&v=32)](/about/)

[Cyber 5W](/about/)
in

[Cloud-Forensics](/tag/Cloud-Forensics)

# OverView

Google Drive is one of the most used storage systems on the planet, Google Drive has over a billion users, For context that’s about 1/8 of the human population! It’s a staggering figure by no doubt, you will likely end up encountering this behemoth of a giant that is Google Drive.

This guide will go over the basics of Google Drive Forensics, allowing readers of all skill levels to follow along if they wish to. The only equipment needed to follow along will be a Google Drive account. (NO EXTRA TOOLS!!!!!).

Let’s jump right into this!

# Case Study

As you can see from the image below we are within the folder named FOR, which is located in My Drive. We can see that there are 6 folders located within this folder.

![Error loading image](/images/driveforensics/image1.png)

You might be asking yourself, how can we get forensics information out of this without using any forensics tools? Well, you’re in luck, just press the three dots next to the folder, and go down to Folder Information as shown below.

![Error loading image](/images/driveforensics/image2.png)

Within folder information first, we are going to click on Details. Details are where you can find simple information about the folder. As seen in the first image below we can learn that only one person has access to this folder. In the second image below we can see who the owner is, but more importantly, we can see the time stamps! The time stamps work the same way as the timestamps do in Windows File Explorer with the main difference being that, In File Explorer, you have accessed, and in Google Drive you have Opened. They are basically the same thing just with different names, don’t lose your head over it.

![Error loading image](/images/driveforensics/image3.png)

![Error loading image](/images/driveforensics/image4.png)

If we click on the tap Activity we will be able to see specific things that happened in said folder.  You can see that at the top are the time stamps of when I was writing this blog.

![Error loading image](/images/driveforensics/image5.png)

Scrolling down further we can see the different types of evidence that Google Drive stores here. Below shows when folders and other documents were created, and under which folder.

![Error loading image](/images/driveforensics/image6.png)

You can even find when documents were moved to the trash.

![Error loading image](/images/driveforensics/image7.png)

The image below shows the same two items from above being restored, then moved back to the trash, and finally showing that the folder Test Folder was Permanently deleted. It should be noted that the untitled document was within the Test Folder, and was shown when it was restored and moved to the trash, but not when it was permanently deleted.

![Error loading image](/images/driveforensics/image8.png)

We can also learn first what it looks like to rename something within Google Drive but also, what both the old and new names are, it also shows when documents were moved into a different folder inside of the folder C5W.

![Error loading image](/images/driveforensics/image9.png)

Now let’s switch folders to the folder named Fun!

Within this folder, you can see two files, and only one user has access to them.

![Error loading image](/images/driveforensics/image10.png)

But if you now click on the file named test2 you will see that three other users have access. This is because these users only have access to this file and not the folder as a whole.

![Error loading image](/images/driveforensics/image11.png)

Clicking on manage access will make the screen shown below appear. This screen shows who currently has access to the file, and what they can do in said file. This can differ from Owner as shown next to Edward, or Editor next to the other three users. There is also a Commenter who can only comment on things, and a Viewer who can only see said document.  Additionally, if you look at the names you will find that only Edward and Alexander have their last name on the top with their email address below. This is because only those two users are in the same Google network, while the last two users show their email addresses twice since their accounts are out of the network.

![Error loading image](/images/driveforensics/image12.png)

If you switch the screen over to Activities you will see that there used to be a fourth user who had access to this account named gtx5fir7gg but was removed by Edward on Jun 21st at 7:38 PM. This user has their name crossed out to show who was removed from the file.

![Error loading image](/images/driveforensics/image13.png)/

Scrolling down we can find out that two of the users had edited the document, but it does not say what they did. To do that you will need to open the document.

![Error loading image](/images/driveforensics/image14.png)/

Within the document, you can find one paragraph nicely written about a rock. Who wrote this poetic paragraph you might ask? Well to be truthful, I have no clue…

![Error loading image](/images/driveforensics/image15.png)

But we can find out together! If you click on the icon in the top right corner that looks like a clock going backward you can view past edits.

![Error loading image](/images/driveforensics/image16.png)

On this new page, we can see who made changes and when. Currently, we are staring at the current version of this document, which was last edited by the user Grant. Grant’s work is in the color Orange to differentiate it from other users. We can see that there used to be more writing on the document but Grant got rid of it.

![Error loading image](/images/driveforensics/image17.png)

If we check what Alexander wrote on June 20th at 4:36 PM we can see that he got rid of a massive paragraph and replaced it with a smaller one about how he had no idea what to write about.

![Error loading image](/images/driveforensics/image18.png)

If you click on the three dots on the side you can choose to, restore the document to said version. Name that version, which will help you find said version later down the road. Or you can pick to make a copy of said version. Either way, the choice is up to you.

![Error loading image](/images/driveforensics/image19.png)

# Closing

Thank you for spending your time reading this document! You might be asking yourself how this information helps me. Well, the importance of knowing this could help professionals catch students cheating in the act. Without having to higher expensive forensics examiners. As just one example.

Author: `Edward Griffith`

[![Virtual Labs](https://blog.cyber5w.com/images/AD/VirtualLabs_V1s.gif)](https://labs.cyber5w.com/)

[![Advertisement](https://blog.cyber5w.com/images/AD/CCMA_V200OFF_043024a.gif)](https://academy.cyber5w.com/courses/C5W-Certified-Malware-Analyst)

[![Windows Registry Analysis](/images/registry_pic/cover.png)

Previous Post

#### Windows Registry Analysis](/introducing-windows-registry)
[![CyberGate Technical Analysis](/images/CyberGate/cover.png)

Next Post

#### CyberGate Technical Analysis](/cybergate-malware-analysis)

### You may also like

### Latest Posts

[![Guide to Mobile Forensics with ALEAPP](/images/mobile_forensics/cover.png)](/a-guide-to-mobile-forensics-with-aleapp)

8 min read
Jan 3, 2025

#### [Guide to Mobile Forensics with ALEAPP](/a-guide-to-mobile-forensics-with-aleapp)

[![Cyber 5W's Picture](https://avata...