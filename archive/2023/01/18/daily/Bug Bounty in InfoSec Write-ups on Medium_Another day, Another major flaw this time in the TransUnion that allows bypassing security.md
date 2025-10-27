---
title: Another day, Another major flaw this time in the TransUnion that allows bypassing security
url: https://infosecwriteups.com/another-day-another-major-flaw-this-time-in-the-transunion-that-allows-bypassing-security-5c46ea82eae2?source=rss----7b722bfd1b8d--bug_bounty
source: Bug Bounty in InfoSec Write-ups on Medium
date: 2023-01-18
fetch_date: 2025-10-04T04:08:14.715666
---

# Another day, Another major flaw this time in the TransUnion that allows bypassing security

[Sitemap](/sitemap/sitemap.xml)

[Open in app](https://rsci.app.link/?%24canonical_url=https%3A%2F%2Fmedium.com%2Fp%2F5c46ea82eae2&%7Efeature=LoOpenInAppButton&%7Echannel=ShowPostUnderCollection&%7Estage=mobileNavBar&source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fanother-day-another-major-flaw-this-time-in-the-transunion-that-allows-bypassing-security-5c46ea82eae2&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

[Medium Logo](https://medium.com/?source=post_page---top_nav_layout_nav-----------------------------------------)

[Write](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-story&source=---top_nav_layout_nav-----------------------new_post_topnav------------------)

[Search](https://medium.com/search?source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fanother-day-another-major-flaw-this-time-in-the-transunion-that-allows-bypassing-security-5c46ea82eae2&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

![](https://miro.medium.com/v2/resize:fill:64:64/1*dmbNkD5D-u45r44go_cf0g.png)

[## InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---publication_nav-7b722bfd1b8d-5c46ea82eae2---------------------------------------)

·

Follow publication

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:76:76/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_sidebar-7b722bfd1b8d-5c46ea82eae2---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow publication

# Another day, Another major flaw this time in the [TransUnion](https://medium.com/u/1fbfe6c1f78d?source=post_page---user_mention--5c46ea82eae2---------------------------------------) that allows bypassing security

[![Jenya Kushnir](https://miro.medium.com/v2/resize:fill:64:64/1*Vjs789AUkf5t_dcJj3Z2DA.jpeg)](https://jenyakushnir.medium.com/?source=post_page---byline--5c46ea82eae2---------------------------------------)

[Jenya Kushnir](https://jenyakushnir.medium.com/?source=post_page---byline--5c46ea82eae2---------------------------------------)

4 min read

·

Jan 15, 2023

--

Listen

Share

Here we go. *Again*.

Let me start by saying this is really unresponsible by major companies like

[Experian](https://medium.com/u/16bc67716a5c?source=post_page---user_mention--5c46ea82eae2---------------------------------------)

,

[TransUnion](https://medium.com/u/1fbfe6c1f78d?source=post_page---user_mention--5c46ea82eae2---------------------------------------)

, and Equifax even to have this kind of bug, and critical errors in their security system.

The last time was an

[Experian](https://medium.com/u/16bc67716a5c?source=post_page---user_mention--5c46ea82eae2---------------------------------------)

 [bypass that allowed you to change a string in the URL and take you straight bypassing all the security questions to its Credit report.](https://medium.com/%40jenyakushnir/2023-is-here-and-yet-again-experian-strikes-again-7c3dfe94d2ad)

This time it's

[TransUnion](https://medium.com/u/1fbfe6c1f78d?source=post_page---user_mention--5c46ea82eae2---------------------------------------)

 so if you visit one of their websites at <https://membership.trueidentity.com/tucm/orderStep1_form.page>?

Press enter or click to view image in full size

![]()

image 1

My name is Jenya Kushnir I am an independent Cybersecurity researcher from Ukraine. By doing some research and looking at the code I have noticed a bug if you fill out the information like the (image 1) and when you get to the section where you have to enter the last 4 of the SSN number.

Press enter or click to view image in full size

![]()

image 2

The next step will be (image 2) after you fill out all information you point the mouse pointer next to the window where you enter the last 4 of your SSN and click the right button mouse to show the menu.

Press enter or click to view image in full size

![]()

image 3

Here you have to select inspector (image 3).

Press enter or click to view image in full size

![]()

image 4

After you open the inspector, it will display the highlighted line in the line of code like (image 4) above.

Press enter or click to view image in full size

![]()

image 5

Point the mouse at the highlighted line in the inspector click the right button mouse and select Delete element like in (image 5) above.

Press enter or click to view image in full size

![]()

image 6

And here comes the most interesting part of this boring process of entering information.

When you perform the Delete of the element in the next step you should see something like the (image 6). The window line for entering the last 4 of the SSN number was deleted. Now can click Submit button to be transferred to the next page Step 2.

> This error bug in the code lines allows to bypass SSN for the verification process of the
>
> [TransUnion](https://medium.com/u/1fbfe6c1f78d?source=post_page---user_mention--5c46ea82eae2---------------------------------------)
>
>  and skip the verification of identity using SSN number.

Press enter or click to view image in full size

![]()

image 7

In Step 2 you have created as usual username and password for your account (image 7), after completing that can proceed by clicking the I accept button to Step 3.
In Step 3 you will get a screen with an option to confirm your identity by receiving an SMS or phone call with the verification code. *The phone number is the number you used when you entered at the begging of the first page (image 1)*

Another option is that you will be prompted not with the Verification code via SMS, but you will get as usual Identity Verification questions (spoiler: if you get three questions you have to answer only one correctly if you get four questions only two out of the four must be answered correctly)

Press enter or click to view image in full size

![]()

image 8

The final.

> If someone asked me how bad is it, I would answer really bad. Not only this allows me to bypass the security without the last 4 of my SSN, but also with this I can get anyone's Name Address, and DOB and pull their Credit Report, from there the list goes on with the options that can be done by Identity thieves.

As an example one more problem with

[TransUnion](https://medium.com/u/1fbfe6c1f78d?source=post_page---user_mention--5c46ea82eae2---------------------------------------)

, when you pull a Credit report they display your accounts in this format (image 9) it shows the full account number except for the last four digits, well there are credit score websites where Identity thieves can pull credit score and in there they display the last four digits of account numbers by combining this two it gives Identity thieves full access to the full number of account.

P.S. another story for another day.

![]()

image 9

Little bit personal message to readers, thank you for reading this and sharing it with others.
It’s really hard right now here with the whole War going, power blackouts, and everything else, doesn’t want to sound petty but if someone can help out, really who’d appreciated donations.

I who’d use this to buy upgrade my gear, buy a power generator and maybe a Starlink so I can do more research and try to help stop and make it harder for identity thieves

> Wallet addresses below for donations
>
> ВТС — bc1qfeq4hfclexv0y4hx7updzt0pnm7pu38zk0g40e
>
> ETH — 0x43D09322cc162D1C4FaeB674398262bf94...