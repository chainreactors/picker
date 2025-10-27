---
title: Like Shooting Phish in a Barrel
url: https://posts.specterops.io/like-shooting-phish-in-a-barrel-926c1905bb4b?source=rss----f05f8696e3cc---4
source: Posts By SpecterOps Team Members - Medium
date: 2024-07-03
fetch_date: 2025-10-06T17:45:59.514357
---

# Like Shooting Phish in a Barrel

[Sitemap](/sitemap/sitemap.xml)

[Open in app](https://rsci.app.link/?%24canonical_url=https%3A%2F%2Fmedium.com%2Fp%2F926c1905bb4b&%7Efeature=LoOpenInAppButton&%7Echannel=ShowPostUnderCollection&%7Estage=mobileNavBar&source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Fposts.specterops.io%2Flike-shooting-phish-in-a-barrel-926c1905bb4b&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

[Medium Logo](https://medium.com/?source=post_page---top_nav_layout_nav-----------------------------------------)

[Write](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-story&source=---top_nav_layout_nav-----------------------new_post_topnav------------------)

[Search](https://medium.com/search?source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Fposts.specterops.io%2Flike-shooting-phish-in-a-barrel-926c1905bb4b&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

![](https://miro.medium.com/v2/resize:fill:64:64/1*dmbNkD5D-u45r44go_cf0g.png)

[## Posts By SpecterOps Team Members](https://posts.specterops.io/?source=post_page---publication_nav-f05f8696e3cc-926c1905bb4b---------------------------------------)

·

Follow publication

[![Posts By SpecterOps Team Members](https://miro.medium.com/v2/resize:fill:76:76/1*D-FDlfkqivRBQZoESrwtqw.png)](https://posts.specterops.io/?source=post_page---post_publication_sidebar-f05f8696e3cc-926c1905bb4b---------------------------------------)

Posts from SpecterOps team members on various topics relating information security

Follow publication

## PHISHING SCHOOL

# Like Shooting Phish in a Barrel

## Bypassing Link Crawlers

[![Forrest Kasler](https://miro.medium.com/v2/da:true/resize:fill:64:64/0*twL-x8eyh-Q1_GWn)](https://medium.com/%40fakasler?source=post_page---byline--926c1905bb4b---------------------------------------)

[Forrest Kasler](https://medium.com/%40fakasler?source=post_page---byline--926c1905bb4b---------------------------------------)

11 min read

·

Jul 2, 2024

--

Listen

Share

You’ve just convinced a target user to click your link. In doing so, you have achieved the critical step in social engineering:

**Convincing someone to let you in the door!**

Now, we just have a few more technical controls that might get in the way of us reeling in our catch. The first of which is link crawlers.

## **What’s a Link Crawler?**

Link crawlers, or “protected links” are one of the most annoying email controls out there. I don’t hate them because of their effectiveness (or ineffectiveness) at blocking phishing. I hate them because they are a real pain for end users and so many secure email gateways (SEGs) use them as a security feature these days. Here’s what they do, and why they suck:

### **What link crawlers do**

They replace all links in an email with a link to their own web server with some unique ID to look up the original link. Then, when a user clicks a link in the email, they first get sent to purgatory… oops, I mean the “protected link” website. The SEG’s web server looks up the original link, and then sends out a web crawler to check out the content of the link’s webpage. If it looks too phishy, the user will be blocked from accessing the link’s URL. If the crawler thinks the page is benign, it will forward the user on to the original link’s URL.

### **Why link crawlers suck**

First, have you ever had to reset your password for some web service you rarely use, and they sent you a one-time-use link to start the reset process? If your secure email gateway (SEG) replaces that link with a “safe link”, and has to check out the real link before allowing you to visit it, then guess what? You will never be able to reset your password because your SEG keeps killing your one-time-use links! I know that some link crawlers work in the opposite order (i.e. crawling the link right after the user visits) to get around this problem, but most of them click first, and send the user to a dead one-time-use URL later.

Second, these link replacements also make it so that the end user actually has no clue where a link is really going to send them. Hovering the link in an email will always show them a URL for the SEG’s link crawling service so there is no way the user can detect a masked link.

Third, I see these “security features” as really just an overt data grab by the SEGs that implement them. They want to collect valuable user behavior telemetry more than they really care about protecting them from phishing campaigns. I wonder how many SEGs sell this data to the devil… oops, I mean “marketing firms”. It all seems very “big brother” to me.

Lastly, this control is not even that hard to bypass. I think if link crawlers were extremely effective at blocking phishing attacks, then I would be more forgiving and able to accept their downsides as a necessary evil. However, that is not the case. Let’s go ahead and talk about ways to bypass them!

## **Parser Bypasses**

Similar to bypassing link filter protections, if the SEG’s link parser doesn’t see our link, then it can’t replace it with a safe link. By focusing on this tactic we can sometimes get two bypasses for the price of one. We’ve already covered this in [Feeding the Phishes](https://medium.com/specter-ops-posts/feeding-the-phishes-276c3579bba7), so I’ll skip the details here.

## **Completely Automated Public Turing test to tell Computers and Humans Apart (CAPTCHA)**

Link crawlers are just robots. Therefore, to defeat link crawlers, we need to wage war with the robots! We smarty pants humans have employed CAPTCHAs as robot bouncers for decades now to kick them out of our websites. We can use the same approach to protect our phishing pages from crawlers as well. Because SEGs just want a peak at our website content to make a determination of whether it’s benign, there is no real motivation for them to employ any sort of CAPTCHA solver logic. For us, that means our CAPTCHAs don’t even have to be all that complicated or secure like they would need to be to protect a real website. I personally think this approach has been overused and abused by spammers to the point that many users are sketched out by them, but it’s still a valid link crawler bypass for many SEGs and a pretty quick and obvious choice.

### **Fun Fact (think about it)**

*Because the test is administered by a computer, in contrast to the standard Turing test that is administered by a human, CAPTCHAs are sometimes described as reverse Turing tests.* — Wikipedia

## **Join the Redirect Arms Race**

**Warning:** I don’t actually recommend this, but it works, and therefore we have to talk about it. I’ll try to keep it brief.

**Q:** If you are tasked with implementing a link checker, how should you treat redirects like HTTP 302 responses?

**A:** They are common enough that you should probably follow the redirect.

**Q:** What about if it redirects again? This time via JavaScript instead of an HTTP response code. Should you follow it?

**A:** Yes, this is common enough too, so maybe we should follow it.

**Q:** But how many times?

**A:** ???

That’s up to you as the software engineer to decide. If you specify a depth of 3 and your script gets redirected 3 times, it’s going to stop following redirects and just assess the content on the current page. Phishers are going to redirect 4 times and defeat your bot. You’re going to up the depth, then they are going to up the redirects, and so on and so forth ad nauseam.

**Welcome to the redirect arms race.**

I see this “in the wild” all the time so it must work as a bypass, but it is annoying, and cliche, and kinda dumb in my opinion. So…

**Please don’t join the redirect arms race!!!**

## **Alert!**

Link crawling bots tend to...