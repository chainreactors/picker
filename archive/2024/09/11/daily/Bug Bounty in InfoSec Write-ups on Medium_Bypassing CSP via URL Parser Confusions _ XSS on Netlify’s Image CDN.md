---
title: Bypassing CSP via URL Parser Confusions : XSS on Netlify’s Image CDN
url: https://infosecwriteups.com/bypassing-csp-via-url-parser-confusions-xss-on-netlifys-image-cdn-755a27065fd9?source=rss----7b722bfd1b8d--bug_bounty
source: Bug Bounty in InfoSec Write-ups on Medium
date: 2024-09-11
fetch_date: 2025-10-06T18:27:01.702556
---

# Bypassing CSP via URL Parser Confusions : XSS on Netlify’s Image CDN

[Sitemap](/sitemap/sitemap.xml)

[Open in app](https://rsci.app.link/?%24canonical_url=https%3A%2F%2Fmedium.com%2Fp%2F755a27065fd9&%7Efeature=LoOpenInAppButton&%7Echannel=ShowPostUnderCollection&%7Estage=mobileNavBar&source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fbypassing-csp-via-url-parser-confusions-xss-on-netlifys-image-cdn-755a27065fd9&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

[Medium Logo](https://medium.com/?source=post_page---top_nav_layout_nav-----------------------------------------)

[Write](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-story&source=---top_nav_layout_nav-----------------------new_post_topnav------------------)

[Search](https://medium.com/search?source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fbypassing-csp-via-url-parser-confusions-xss-on-netlifys-image-cdn-755a27065fd9&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

![](https://miro.medium.com/v2/resize:fill:64:64/1*dmbNkD5D-u45r44go_cf0g.png)

[## InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---publication_nav-7b722bfd1b8d-755a27065fd9---------------------------------------)

·

Follow publication

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:76:76/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_sidebar-7b722bfd1b8d-755a27065fd9---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow publication

# Bypassing CSP via URL Parser Confusions : XSS on Netlify’s Image CDN

[![Sudhanshu Rajbhar](https://miro.medium.com/v2/resize:fill:64:64/2*IwNAX8FaOfAcFwqXw4t0Cg.jpeg)](https://sudhanshur705.medium.com/?source=post_page---byline--755a27065fd9---------------------------------------)

[Sudhanshu Rajbhar](https://sudhanshur705.medium.com/?source=post_page---byline--755a27065fd9---------------------------------------)

7 min read

·

Aug 31, 2024

--

Listen

Share

Heyyy Everyonee,

In this blogpost I am going to talk about my finding which was a XSS on Netlify’s Image CDN used in <https://app.netlify.com> and how I managed to bypass this CSP `Content-Security-Policy: script-src ‘none’` (for those of you who aren’t much familiar with this CSP , in simple terms it means no script execution will be there in any case) along with that some other things which can be applied on other sites also which are using Netlify’s Image CDN , for those of you unfamiliar with what it is would recommend reading this article:

[## Netlify Image CDN

### Transform images on demand without impacting build times. Handle content negotiation automatically.

docs.netlify.com](https://docs.netlify.com/image-cdn/overview/?source=post_page-----755a27065fd9---------------------------------------)

In short many popular Static Site Generators have this Image CDN functionality where they optimize the images used on the website. This is useful in cases where you want to make the site load faster by reducing the time taken for loading images as less as possible.

Some examples of this are:

[## Optimizing: Images | Next.js

### Optimize your images with the built-in `next/image` component.

nextjs.org](https://nextjs.org/docs/pages/building-your-application/optimizing/images?source=post_page-----755a27065fd9---------------------------------------)

[## Nuxt Image: Optimized Images for your Nuxt Apps

### Plug-and-play image optimization for Nuxt apps. Resize and transform your images using built-in optimizer or your…

image.nuxt.com](https://image.nuxt.com/?source=post_page-----755a27065fd9---------------------------------------)

[## Preoptimizing Your Images | Gatsby

### Gatsby ships with excellent image optimization capabilities (see the image tutorial for more info). However, this image…

www.gatsbyjs.com](https://www.gatsbyjs.com/docs/preoptimizing-images/?source=post_page-----755a27065fd9---------------------------------------)

All these have the same goal where they take a url as an input either via a parmeter or from the path and optimize the image. A lot of stuff goes behind the scene when you make a request to such endpoint, if you are interested luckily all of them are open source so you can take a deep dive and maybe find some cool bugs.

```
/_next/image?url=
/_gatsby/image/:url
/.netlify/image?url=
/_ipx/w_200/:url
```

Also you will find these endpoints will often have some checks in place like which url you are allowed to make requests to which is all configurable as per the docs. They aslo validate the Content-Type of the requested image, like `image/svg+xml` as it could allow xss and other checks to like checking the response buffer too , to make sure the requested image url is really is an image or not before serving the response back.

Some don’t do any checks for images and even allow you to serve html response via this endpoint, as the requested url is fetched server side not client side it can also be good candidate for SSRF (I am not just bluffing all these some cool hackers have proved all these things are possible) like they were able to bypass the domain check to make request to any url or get xss or even Full read SSRF

It’s a really interesting attack surface after seeing some awesome research done by Assetnote and Sam Curry in the past on this, I decided to look into them as well , so far have some interesting leads which I hope can be turned into a bug maybe. But well that’s a different topic if I did find something, will make sure to write a blog about it.

[## Exploiting Web3's Hidden Attack Surface: Universal XSS on Netlify's Next.js Library

### On August 24th, 2022, we reported a vulnerability to Netlify affecting their Next.js "netlify-ipx" repository which…

samcurry.net](https://samcurry.net/universal-xss-on-netlifys-next-js-library/?source=post_page-----755a27065fd9---------------------------------------)

[## Exploiting Static Site Generators: When Static Is Not Actually Static

### Over the last ten years, we have seen the industrialization of the content management space. A decade ago, it felt like…

www.assetnote.io](https://www.assetnote.io/resources/research/exploiting-static-site-generators-when-static-is-not-actually-static?source=post_page-----755a27065fd9---------------------------------------)

Enough background details now back to the finding,so sites built on Netlify has this Image Optimization endpoint

```
/.netlify/images?url=
```

An example url can be this: [https://app.netlify.com/.netlify/images?url=https://app.netlify.com/favicon.ico](https://app.netlify.com//.netlify/images?url=https%3A%2F%2Fapp.netlify.com%2Ffavicon.ico)

There are some more parameters which can also be used to return the image with a different width or height,etc. The url parameter only allows you to fetch files from whitelisted hosts only, this hosts can be configured via the netlify.toml file

```
[images]
  remote_images = [
          "https://my-images.com/.*",
          "https://animals.more-images.com/[bcr]at/.*"]
```

By default the same origin urls are also accepted in the `url` parameter. You can see in the above config , it makes the use of regex also `.*`so even little mistakes can have some side effects there.

As earlier I told some providers don’t do any check on this whether the requested url returns a valid image or not this is in the case of Netlify.

So you can even do thing like this, here I am requesting...