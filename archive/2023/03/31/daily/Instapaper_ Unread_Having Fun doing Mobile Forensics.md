---
title: Having Fun doing Mobile Forensics
url: https://leahycenterblog.champlain.edu/2023/03/29/having-fun-doing-mobile-forensics/
source: Instapaper: Unread
date: 2023-03-31
fetch_date: 2025-10-04T11:17:37.027588
---

# Having Fun doing Mobile Forensics

[Champlain College
Shield logo with college name to the right
image/svg+xml](https://www.champlain.edu)

[Contact Us](/contact-us) [Champlain.edu](https://www.champlain.edu)

[The Leahy Center for Digital Forensics & Cybersecurity](https://leahycenterblog.champlain.edu/)

* [About](https://leahycenterblog.champlain.edu/about-the-leahy-center/ "About")
* [Research Projects](https://leahycenterblog.champlain.edu/section/research-projects/ "Research Projects")
* [Student Experience](https://leahycenterblog.champlain.edu/section/student-experience/ "Student Experience")
* [Conferences & Events](https://leahycenterblog.champlain.edu/section/conferences-events/ "Conferences & Events")
* [Partners](https://leahycenterblog.champlain.edu/section/partners/ "Partners")
* [Learn](https://leahycenterblog.champlain.edu/section/learn-with-leahy/ "Learn")

![Modal Close Button](https://leahycenterblog.champlain.edu/wp-content/themes/champlain-view-wordpress-theme/images/close-icon.svg)

##### The Leahy Center for Digital Forensics & Cybersecurity

Search

![Modal Close Button](https://leahycenterblog.champlain.edu/wp-content/themes/champlain-view-wordpress-theme/images/close-icon.svg)

##### The Leahy Center for Digital Forensics & Cybersecurity

* [About](https://leahycenterblog.champlain.edu/about-the-leahy-center/ "About")
* [Research Projects](https://leahycenterblog.champlain.edu/section/research-projects/ "Research Projects")
* [Student Experience](https://leahycenterblog.champlain.edu/section/student-experience/ "Student Experience")
* [Conferences & Events](https://leahycenterblog.champlain.edu/section/conferences-events/ "Conferences & Events")
* [Partners](https://leahycenterblog.champlain.edu/section/partners/ "Partners")
* [Learn](https://leahycenterblog.champlain.edu/section/learn-with-leahy/ "Learn")

* [Contact Us](/contact-us)

# Having Fun doing Mobile Forensics

* [![Twitter Icon](https://leahycenterblog.champlain.edu/wp-content/themes/champlain-view-wordpress-theme/images/social_icons/sticky-twitter.png)](https://twitter.com/intent/tweet?text=Having%20Fun%20doing%20Mobile%20Forensics&url=https%3A%2F%2Fleahycenterblog.champlain.edu%2F2023%2F03%2F29%2Fhaving-fun-doing-mobile-forensics%2F)
* [![Facebook Icon](https://leahycenterblog.champlain.edu/wp-content/themes/champlain-view-wordpress-theme/images/social_icons/sticky-facebook.png)](https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Fleahycenterblog.champlain.edu%2F2023%2F03%2F29%2Fhaving-fun-doing-mobile-forensics%2F)
* [![LinkedIn Icon](https://leahycenterblog.champlain.edu/wp-content/themes/champlain-view-wordpress-theme/images/social_icons/sticky-linkedin-in.png)](https://www.linkedin.com/shareArticle?mini=true&url=https%3A%2F%2Fleahycenterblog.champlain.edu%2F2023%2F03%2F29%2Fhaving-fun-doing-mobile-forensics%2F&title=Having%20Fun%20doing%20Mobile%20Forensics&summary=&source=https%3A%2F%2Fleahycenterblog.champlain.edu)
* ![Email Icon](https://leahycenterblog.champlain.edu/wp-content/themes/champlain-view-wordpress-theme/images/social_icons/sticky-email.png)

[Research Projects](https://leahycenterblog.champlain.edu/section/research-projects/)
March 29, 2023 (November 14, 2024)

Jailbreaking an iOS 15.4 Device with Palera1n

***Warning: When using Palera1n if the jailbroken device powers off or dies then the jailbroken device will no longer be jailbroken and will require the user to jailbreak the device again.***

When working on our Capstone Project, “Apple AirTag Forensics; The Phantom Menace,” we had to jailbreak the phone that we are using so that we could gain access to the root of the device and get better information when we image the device.

At first, this seemed like a daunting task, with many of the methods that we tried to employ failing because of one simple reason: We had an iPhone that was in iOS version 15.4. The only reason this is a problem is that starting with iOS 15 and up, Apple started to crack down on Jailbreaking more and improved the security of their devices, sealing the root file so that it was a lot harder to get access to the root of the device. Recently, however, there have been some breakthroughs in rooting iOS devices with a version higher than iOS 15, but there are even restrictions to that as well.

Through our research, the team was able to find a relatively new jailbreaking method called [Palera1n](https://github.com/palera1n/palera1n)1 which would be able to gain access to the root of our device, given the requirements of the jailbreak are met and followed closely. To ensure that Palera1n worked, we needed to make sure that the device we were using was a vulnerable iOS 15.x or 16.x device, meaning the security chip inside had to be an A8 through an A11.

The next requirement would be to ensure that if you are using a semi-tethered jailbreak, the device needs enough space (5-10 GB) to create the fake file system (fakefs) that would allow the device to be rooted without being hooked up to a computer.

Lastly, passcodes have to be disabled to allow the phone to enter a jailbroken state, with the caveat that on iOS 16 or higher devices, a passcode has never been used on the device, often forcing the user to reset their device.

As long as all of the strict requirements for the device to be jailbroken are met, then you would be able to gain Root Access to the system and be able to successfully complete your Jailbreak. It took our team a few attempts to succeed in this process, but with a lot of work and effort, we were able to successfully jailbreak the device we were using, allowing us to access applications that would not otherwise be available and image the device more thoroughly, providing us with valuable information for our project going forward.

In this section, we will go through the process that we followed when jailbreaking our device, with some images to help explain the processes that are taking place. In the version of Palera1n that was out when we were doing our jailbreak, the first step was to clone the git repository that contained all of the information and tools needed for the jailbreak onto the mac system that we were working with. Once the clone was complete, we changed into the directory that contained all of the Palera1n files and started the jailbreaking process. Using the command found in Figure 1 below, you can start the jailbreaking process. *Note: Make sure to follow the updated directions that are found on the Palera1n GitHub page to ensure that you are using the most up to date method for the jailbreak*

![](https://lh6.googleusercontent.com/0fYt8RP91D7X65QidjMklAf2r6BPYx2jGF03yE9y8KtOf0rfzgpYTLhefgjLwG8nJPOtFz82NNcfzx2LkgSTShYKeBykj0Is3ydNN-gpplU5q1R9bpYJIaViwAwUjLmram5cS_70mlWE81NG4wnX548)

Figure 1: When you start the script provided with the GitHub repository, you get a screen similar to the following.

Once you have started the process, the script will run until it is ready to enter DFU (Device Firmware Upgrade) mode for the first time. The script will prompt the user to press any key and then instruct you on how to get the device into DFU mode. In Figure 2 below, you can see a failed attempt to enter DFU mode. Don’t worry though, the script will jump back to the start and attempt to enter DFU mode again if you mess up any of the steps. In Figure 3 below, you can see what a successful attempt to enter DFU mode looks like on the device.

![](https://lh4.googleusercontent.com/aIAFoxkwRa9syrFqAB9HEH1bRtif6n3dE1KK_FHkWujYywJztcmbN1AdpXRPQiWcYSUNUVm5IJaGTajtFG6Y3yy_1QDQgaxgNkWyVKVvD4NZ1R3IQRG9vmVVl3ULUVqKqCqvqxgDemZ7WGvtI2lQfIc)

Figure 2: Shows a failed attempt at trying to jailbreak the device

![](https://lh6.googleusercontent.com/ej7RYDl99Ekm17hJtwKdW-GN6gvdX4U2jDR6ZXlWr8peewLQvVhRm_RNtf55x6SZLZvCAR87HaSp8LJgjsUb97ywdfpQ7ej-umeUrOHK2Vr8XmU8gPTYfkk3XBbQ6C0Jn90VMOqAABE6zLG6CZJsk5s)

Figure 3: Shows the device entering DFU mode successfully.

Once the device enters DFU mode, it can begin the long process of jailbreaking t...