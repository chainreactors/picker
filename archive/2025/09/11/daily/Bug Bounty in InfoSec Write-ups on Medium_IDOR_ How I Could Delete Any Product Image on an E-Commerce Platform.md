---
title: IDOR: How I Could Delete Any Product Image on an E-Commerce Platform
url: https://infosecwriteups.com/idor-how-i-could-delete-any-product-image-on-an-e-commerce-platform-8998453a50ea?source=rss----7b722bfd1b8d--bug_bounty
source: Bug Bounty in InfoSec Write-ups on Medium
date: 2025-09-11
fetch_date: 2025-10-02T19:57:42.140722
---

# IDOR: How I Could Delete Any Product Image on an E-Commerce Platform

[Sitemap](/sitemap/sitemap.xml)

[Open in app](https://rsci.app.link/?%24canonical_url=https%3A%2F%2Fmedium.com%2Fp%2F8998453a50ea&%7Efeature=LoOpenInAppButton&%7Echannel=ShowPostUnderCollection&%7Estage=mobileNavBar&source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fidor-how-i-could-delete-any-product-image-on-an-e-commerce-platform-8998453a50ea&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

[Medium Logo](https://medium.com/?source=post_page---top_nav_layout_nav-----------------------------------------)

[Write](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-story&source=---top_nav_layout_nav-----------------------new_post_topnav------------------)

[Search](https://medium.com/search?source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fidor-how-i-could-delete-any-product-image-on-an-e-commerce-platform-8998453a50ea&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

![](https://miro.medium.com/v2/resize:fill:64:64/1*dmbNkD5D-u45r44go_cf0g.png)

[## InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---publication_nav-7b722bfd1b8d-8998453a50ea---------------------------------------)

·

Follow publication

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:76:76/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_sidebar-7b722bfd1b8d-8998453a50ea---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow publication

# **IDOR: How I Could Delete Any Product Image on an E-Commerce Platform**

[![Mahmoud El Manzalawy](https://miro.medium.com/v2/resize:fill:64:64/1*_7PGCL8pdL6wVrcxegetOw.jpeg)](https://is4curity.medium.com/?source=post_page---byline--8998453a50ea---------------------------------------)

[Mahmoud El Manzalawy](https://is4curity.medium.com/?source=post_page---byline--8998453a50ea---------------------------------------)

2 min read

·

Sep 10, 2025

--

Listen

Share

Hello folks,

I’m **Mahmoud El Manzalawy**, a **penetration tester** and **bug bounty hunter** who enjoys discovering vulnerabilities in my free time.
In this write-up, I’ll walk you through How I found Insecure Direct Object Reference (IDOR) in Image Deletion Endpoint .

While testing the platform’s product ad posting feature, I found that the application allows users to upload and delete images for their ads. During this process, I inspected the page source and noticed how the image deletion functionality works.

view page source

Press enter or click to view image in full size

![]()

I Found The JavaScript responsible for image removal is

```
$("body").on("click", ".remove_pic", function() {
    var img = $(this).parent().find("img");
    var img_id = img.data("id");
    parent = $(this).parents("li");
    current = $(this);

    void 0 != img_id && $.ajax({
        url: "/post/deleteimage?Id=" + img_id,
        type: "get",
        dataType: "json",
        complete: function (jqXHR, status) {
            data = jqXHR.responseText;
            data = $.parseJSON(data);
            if (data.success === 0) {
                alert(data.message);
                is_delete = false;
            } else {
                is_delete = true;
                parent.animate({opacity: 0}, 100, function() {
                    current.remove();
                });
            }
        }
    });
});
```

### Root Cause

The deletion request is triggered via a **GET** request to:

```
url: "/post/deleteimage?Id=" + img_id,
```

However, the server does not validate whether the image being deleted actually belongs to the currently authenticated user. Instead, it relies solely on the `imageId` parameter provided by the client-side code.

Since image IDs are predictable, e.g

```
https://site.com/images/product/thumb_931887_158_100.jpg?v=1
```

The identifier here is `931887`, which can easily be enumerated or modified.

### Exploitation

By manipulating the `img_id` parameter in the request, an attacker can delete images uploaded by other users without their consent.

```
GET /post/deleteimage?Id=931887
```

Steps I followed to confirm the vulnerability:

```
1. Crafted a request with an arbitrary img_id.
2. Directly accessed the vulnerable endpoint by passing the chosen img_id.
3. Opened the crafted URL → the image was successfully deleted.
```

This clearly demonstrates that an attacker could delete **any user’s product image** without proper authorization.

Press enter or click to view image in full size

![]()

Press enter or click to view image in full size

![]()

## Impact

This vulnerability allows an attacker to:

* Delete other sellers’ product images.
* Potentially perform mass deletion of product images.
* Severely disrupt business operations and harm user trust.

Thank you for reading my write-up!
 See you soon with another interesting bug write-up! Stay tuned 🚀 😄

Feel free to follow me on **Medium** , **Linkedin** and **X**: **@is4curity**
 Happy bug hunting!

./Egypt 🇪🇬

[Cybersecurity](https://medium.com/tag/cybersecurity?source=post_page-----8998453a50ea---------------------------------------)

[Infosec](https://medium.com/tag/infosec?source=post_page-----8998453a50ea---------------------------------------)

[Vulnerability](https://medium.com/tag/vulnerability?source=post_page-----8998453a50ea---------------------------------------)

[Bug Bounty](https://medium.com/tag/bug-bounty?source=post_page-----8998453a50ea---------------------------------------)

[Penetration Testing](https://medium.com/tag/penetration-testing?source=post_page-----8998453a50ea---------------------------------------)

--

--

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:96:96/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--8998453a50ea---------------------------------------)

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:128:128/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--8998453a50ea---------------------------------------)

Follow

[## Published in InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---post_publication_info--8998453a50ea---------------------------------------)

[71K followers](/followers?source=post_page---post_publication_info--8998453a50ea---------------------------------------)

·[Last published 4 days ago](/how-to-find-p1-bugs-using-google-in-your-target-part-1-e37455324dc1?source=post_page---post_publication_info--8998453a50ea---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow

[![Mahmoud El Manzalawy](https://miro.medium.com/v2/resize:fill:96:96/1*_7PGCL8pdL6wVrcxegetOw.jpeg)](https://is4curity.medium.com/?source=post_page---post_author_info--8998453a50ea---------------------------------------)

[![Mahmoud El Manzalawy](https://miro.medium.com/v2/resize:fill:128:128/1*_7PGCL8pdL6wVrcxegetOw.jpeg)](https://is4curity.medium.com/?source=post_page---post_author_info--8998453a50ea---------------------------------------)

[## Written by Mahmoud El Manzalawy](https://is4curity.medium.com/?source=post_page---post_author_info--8998453a50e...