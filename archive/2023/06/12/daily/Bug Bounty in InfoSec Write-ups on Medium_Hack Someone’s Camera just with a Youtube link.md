---
title: Hack Someone’s Camera just with a Youtube link
url: https://infosecwriteups.com/hack-someones-camera-just-with-a-youtube-link-a580d397192c?source=rss----7b722bfd1b8d--bug_bounty
source: Bug Bounty in InfoSec Write-ups on Medium
date: 2023-06-12
fetch_date: 2025-10-04T11:45:17.577142
---

# Hack Someone’s Camera just with a Youtube link

[Sitemap](/sitemap/sitemap.xml)

[Open in app](https://rsci.app.link/?%24canonical_url=https%3A%2F%2Fmedium.com%2Fp%2Fa580d397192c&%7Efeature=LoOpenInAppButton&%7Echannel=ShowPostUnderUser&%7Estage=mobileNavBar&source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](/m/signin?operation=login&redirect=https%3A%2F%2Fmedium.com%2F%40RajneeshKarya%2Fhack-someones-camera-just-with-a-youtube-link-a580d397192c&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

[Medium Logo](/?source=post_page---top_nav_layout_nav-----------------------------------------)

[Write](/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-story&source=---top_nav_layout_nav-----------------------new_post_topnav------------------)

[Search](/search?source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](/m/signin?operation=login&redirect=https%3A%2F%2Fmedium.com%2F%40RajneeshKarya%2Fhack-someones-camera-just-with-a-youtube-link-a580d397192c&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

![](https://miro.medium.com/v2/resize:fill:64:64/1*dmbNkD5D-u45r44go_cf0g.png)

# Hack Someone’s Camera just with a Youtube link

[![Rajneesh Kumar Arya](https://miro.medium.com/v2/resize:fill:64:64/1*a7KPXIpCqRnq7KYHJ8PTpA.png)](/%40RajneeshKarya?source=post_page---byline--a580d397192c---------------------------------------)

[Rajneesh Kumar Arya](/%40RajneeshKarya?source=post_page---byline--a580d397192c---------------------------------------)

4 min read

·

Jun 3, 2023

--

Listen

Share

Press enter or click to view image in full size

![]()

Hello learners, I am back again with my new and really interesting blog.
I know most of you have seen in the movies how hackers can gain access to the victim’s camera and capture their pictures and their current location as well. So, In this blog, we are going to see how hackers can access your camera and your current location. But before starting let me give you a good news that I started a youtube channel for cybersecurity students where they can learn cybersecurity from the beginning to advance and trust me you’ll not find content like this on Youtube before. [https://youtube.com/@securedsyntax](https://youtube.com/%40securedsyntax) that’s the link for it so enjoy and learn Hacking with Me.

> Disclaimer: Do not use these technique to hack anyone unless you have permission.

At first you need to download the tool called CamPhish which is available in github you can access it through this [**link**](https://github.com/techchipnet/CamPhish)**.**

Or you can download it just by typing the following command to your terminal.

```
git clone https://github.com/techchipnet/CamPhish
```

After Installing the tool just run it and you should see the following options

Press enter or click to view image in full size

![]()

You can continue with anyone but I recommend you to continue with option 1 which is Ngrok. So, Ngrok is the tool that will expose you.

![]()

Don’t think like that its not like that what you are thinking. It will just expose your home network to the Internet. You just need to go to the ngrok’s official website and create a account there and get your authtoken, copy it down somewhere for future use.

After this it will ask you which type of template you want I recommend you to use option 2 for youtube link because these two seems more suspicious so we’ll continue with youtube for that just select 2 and press ENTER.

Press enter or click to view image in full size

![]()

As you select the Live Youtube TV option it will then ask you for a watch ID which you can get from Youtube. Let me show you how, So select any vedio on [youtube.com](https://youtube.com) in my case I am selecting a song SCOPIN by KORDHELL.

![]()

and check the url you’ll get the watch ID. See the screenshot below.

Press enter or click to view image in full size

![]()

The selected text after watch?v= is the watch ID. just copy it and paste on the terminal where the program is asking for watch ID.

Press enter or click to view image in full size

![]()

after that it will ask your ngrok’s authtoken just paste your token and hit ENTER.

Press enter or click to view image in full size

![]()

After that it will start a php server, ngrok server and you’ll get a link send this link to your victim and for that you need some social engineering skills to get clicks on your link.

Press enter or click to view image in full size

![]()

As you can see in the Direct link we have our link so as the victim clicks on it they will get a youtube page of the song I’ve selected but on the other hand the magic starts working see the screenshot below and guess what ? I got pictures of victim which stored in my CamPhish folder itself.

Press enter or click to view image in full size

![]()

![]()

Do you see how easy it is to hack someone’s camera ? So, be aware of that kind of cyber crimes and scams and teach your parents or friends as well. So, that they’ll not get trapped into these kind of cyber attacks because old and non technical persons are good targets for them.

I hope you all like this blog but before ending it let me tell you one more think I told you that we’ll access its camera as well as live location so for live location we’ll cover that in our next blog for that just follow me for more content like this and switch on your email subscription so that you’ll get notified And just pin down your comment so that I can get what you want me to cover next.

TILL THEN KEEP LEARNING 📕 KEEP EXPLORING 🔍 AND DO HACKING 😈!!!!

[Cybersecurity](/tag/cybersecurity?source=post_page-----a580d397192c---------------------------------------)

[Cyber Security Awareness](/tag/cyber-security-awareness?source=post_page-----a580d397192c---------------------------------------)

[Ethical Hacking](/tag/ethical-hacking?source=post_page-----a580d397192c---------------------------------------)

[Bug Bounty](/tag/bug-bounty?source=post_page-----a580d397192c---------------------------------------)

[Penetration Testing](/tag/penetration-testing?source=post_page-----a580d397192c---------------------------------------)

--

--

[![Rajneesh Kumar Arya](https://miro.medium.com/v2/resize:fill:96:96/1*a7KPXIpCqRnq7KYHJ8PTpA.png)](/%40RajneeshKarya?source=post_page---post_author_info--a580d397192c---------------------------------------)

[![Rajneesh Kumar Arya](https://miro.medium.com/v2/resize:fill:128:128/1*a7KPXIpCqRnq7KYHJ8PTpA.png)](/%40RajneeshKarya?source=post_page---post_author_info--a580d397192c---------------------------------------)

[## Written by Rajneesh Kumar Arya](/%40RajneeshKarya?source=post_page---post_author_info--a580d397192c---------------------------------------)

[795 followers](/%40RajneeshKarya/followers?source=post_page---post_author_info--a580d397192c---------------------------------------)

·[5 following](/%40RajneeshKarya/following?source=post_page---post_author_info--a580d397192c---------------------------------------)

Cybersecurity content writer | Freelancers of content writing and security services | Open to gigs: rajnirajni54565456@gmail.com

## No responses yet

[Help](https://help.medium.com/hc/en-us?source=post_page-----a580d397192c---------------------------------------)

[Status](https://status.medium.com/?source=post_page-----a580d397192c---------------------------------------)

[About](/about?autoplay=1&source=post_page-----a580d397192c---------------------------------------)

[Careers](/jobs-at-medium/work-at-medium-959d1a85284e?source=post_page-----a580d397192c---------------------------------------)

Press

[Blog](https://blog.medium.com/?source=post_page-----a580d397192c---------------------------------------)

[Privacy](https://policy.medium.com/medium-privacy-policy-f03bf92035c9?source=post_page-----a580d397192c---------------------------------------)

[Rules](https://policy.medium.com/m...