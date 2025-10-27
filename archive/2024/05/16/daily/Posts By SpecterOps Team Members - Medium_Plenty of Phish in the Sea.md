---
title: Plenty of Phish in the Sea
url: https://posts.specterops.io/plenty-of-phish-in-the-sea-4388140d6333?source=rss----f05f8696e3cc---4
source: Posts By SpecterOps Team Members - Medium
date: 2024-05-16
fetch_date: 2025-10-06T17:17:51.683445
---

# Plenty of Phish in the Sea

[Sitemap](/sitemap/sitemap.xml)

[Open in app](https://rsci.app.link/?%24canonical_url=https%3A%2F%2Fmedium.com%2Fp%2F4388140d6333&%7Efeature=LoOpenInAppButton&%7Echannel=ShowPostUnderCollection&%7Estage=mobileNavBar&source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Fposts.specterops.io%2Fplenty-of-phish-in-the-sea-4388140d6333&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

[Medium Logo](https://medium.com/?source=post_page---top_nav_layout_nav-----------------------------------------)

[Write](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-story&source=---top_nav_layout_nav-----------------------new_post_topnav------------------)

[Search](https://medium.com/search?source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Fposts.specterops.io%2Fplenty-of-phish-in-the-sea-4388140d6333&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

![](https://miro.medium.com/v2/resize:fill:64:64/1*dmbNkD5D-u45r44go_cf0g.png)

[## Posts By SpecterOps Team Members](https://posts.specterops.io/?source=post_page---publication_nav-f05f8696e3cc-4388140d6333---------------------------------------)

·

Follow publication

[![Posts By SpecterOps Team Members](https://miro.medium.com/v2/resize:fill:76:76/1*D-FDlfkqivRBQZoESrwtqw.png)](https://posts.specterops.io/?source=post_page---post_publication_sidebar-f05f8696e3cc-4388140d6333---------------------------------------)

Posts from SpecterOps team members on various topics relating information security

Follow publication

## Phishing School

# Plenty of Phish in the Sea

## How to Find the Right Phishing Targets

[![Forrest Kasler](https://miro.medium.com/v2/da:true/resize:fill:64:64/0*twL-x8eyh-Q1_GWn)](https://medium.com/%40fakasler?source=post_page---byline--4388140d6333---------------------------------------)

[Forrest Kasler](https://medium.com/%40fakasler?source=post_page---byline--4388140d6333---------------------------------------)

13 min read

·

May 15, 2024

--

Listen

Share

A weapon is useless unless you have something to aim it at. When we weaponize social engineering, our targets are the humans who have the ability to give us access to the systems and data we want to compromise. In this post, we’ll explore ways to find target users for our phishing campaigns. We’ll then talk about what makes a “good” target vs. a “bad” target.

When looking for the “right” targets, our general approach will be to collect as many potential contacts as possible and then pair down the list based on what we can learn about each individual.

## **Casting a Wider Net**

Before diving into contact collection, we want to make sure that we have a clear picture of the available attack surface. I’ve seen many pentesters take only the main domain the client supplied, run it through theHarvester, linkedInt, maltego, etc. and call the output a targets list. In doing so, these pentesters completely overlooked valuable attack surfaces associated with the target organization’s other domains. We can do better. Here are some of my favorite ways to find our target’s other domains:

### **WHOIS Data — Whoxy and WhoisXML**

When you register a domain, you have to fill out some basic contact information like the organization name and “abuse email” for the WHOIS service. While you can technically put anything you want, and most registrars offer a WHOIS anonymizing service, many organizations still fill out the form with identifiable information. This means that we can often cross-reference WHOIS contact information and find associated domains.

Unfortunately, the WHOIS protocol was never intended to allow lookups based on contact information; however, there are paid APIs like Whoxy and WhoisXML that have indexed millions of WHOIS records and made them searchable. Whoxy is a nice quick check because its API credits are insanely cheap; however, its search functionality is case sensitive and they do not have the same coverage as WhoisXML.

Of course, the WHOIS protocol is a very simple, text-based, call-and-response protocol. With a little scripting and distributed computing, we could pretty easily mine and index our own data as well. If you decide to go this route, keep in mind that many WHOIS providers expressly forbid data mining. You’ve been warned!

### **O365 Mining (All the Phish in a Barrel)**

If your target organization uses AzureAD, then you can use the autodiscover service to get a list of all of their tenant’s domains. Dr. Nestori Syynimaa released a great tool and blog post that covers this method:

[## Just looking: Azure Active Directory reconnaissance as an outsider

### This post is part 1⁄5 of Azure AD and Microsoft 365 kill chain blog series. Azure AD and Office 365 are cloud services…

aadinternals.com](https://aadinternals.com/post/just-looking/?source=post_page-----4388140d6333---------------------------------------)

### **Backlinks**

When organizations set up a website on a domain, they will often add a link back to their main domain somewhere on the website. In the SEO world, these are referred to as “backlinks”. You can use free SEO tools online to enumerate these links and look for any domains you missed with other methods. You will also often see backlinks from other organizations that do business with your target organization. Take note of these as you find them, as we might be able to abuse an implicit trust between these organizations when crafting our campaigns.

### **Sanity Check**

Once we have a list of associated domains, we should do a quick sanity check to find out which ones have a published MX record. There is no use enumerating email addresses for a domain that doesn’t even have a mail server. This is to make sure we don’t waste time or API credits during email collection:

```
dig mx -f domains.txt | grep ANSWER -A 1 | grep MX
```

### **Hi-Ho (Hi-Ho. Let’s grab a net and go!)**

Now that we have a list of associated domains, we can search for contacts at (@) each one. In the next sections, we are going to cover a range of contact collection methods starting with the well-known and simple (little phish) and working up to the more obscure and difficult (bigger phish).

While most of these methods are focused on obtaining email addresses, some of them will also give you phone numbers and mailing addresses. Don’t overlook this extra data! You can call phone numbers to see if they are direct lines and check if the target is still employed at the organization. We can also deliver payloads over the phone or even via snail mail if we have to. Likewise, if your data source includes information like job titles, grab this information too. It could be useful when pairing down our list.

## **The Classics**

**Read the website**: This is a (hopefully) obvious first step, but you might be surprised by the number of times I’ve seen pentesters skip it. On more than one occasion, I’ve found an employee directory on the main website after hearing co-workers complain about “not finding any email addresses” with OSINT tools.

**Google dorks**: Along the same lines, it’s worth a quick Google search to see if there are any employee listings that are not hosted on the main website. There are plenty of OSINT tools that can even automate some common dorks for you. Try using Google to find some ;)

**theHarvester/Skiddy Scripts**: While I haven’t used theHarvester in a while now, I was pleasantly surprised to see that it is still being actively maintained as of 1/1/24. The reason I don’t currently use it is because I tend to view tools like this as just a wrapper for their data sources. If you like using a particular email mining OSINT tool, by all means keep using it. Though I would ...