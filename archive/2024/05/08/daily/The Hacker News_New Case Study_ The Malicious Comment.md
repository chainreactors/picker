---
title: New Case Study: The Malicious Comment
url: https://thehackernews.com/2024/05/new-case-study-malicious-comment.html
source: The Hacker News
date: 2024-05-08
fetch_date: 2025-10-06T17:19:16.998049
---

# New Case Study: The Malicious Comment

#1 Trusted Cybersecurity News Platform

Followed by 5.20+ million[**](https://twitter.com/thehackersnews)
[**](https://www.linkedin.com/company/thehackernews/)
[**](https://www.facebook.com/thehackernews)

[![The Hacker News Logo](data:image/png;base64...)](/)

**

**

[** Subscribe – Get Latest News](#email-outer)

* [** Home](/)
* [** Newsletter](#email-outer)
* [** Webinars](/p/upcoming-hacker-news-webinars.html)

* [Home](/)
* [Data Breaches](/search/label/data%20breach)
* [Cyber Attacks](/search/label/Cyber%20Attack)
* [Vulnerabilities](/search/label/Vulnerability)
* [Webinars](/p/upcoming-hacker-news-webinars.html)
* [Expert Insights](https://thehackernews.com/expert-insights/)
* [Contact](/p/submit-news.html)

**

**

**

Resources

* [Webinars](/p/upcoming-hacker-news-webinars.html)
* [Free eBooks](https://thehackernews.tradepub.com)

About Site

* [About THN](/p/about-us.html)
* [Jobs](/p/careers-technical-writer-designer-and.html)
* [Advertise with us](/p/advertising-with-hacker-news.html)

Contact/Tip Us

[**

Reach out to get featured—contact us to send your exclusive story idea, research, hacks, or ask us a question or leave a comment/feedback!](/p/submit-news.html)

Follow Us On Social Media

[**](https://www.facebook.com/thehackernews)
[**](https://twitter.com/thehackersnews)
[**](https://www.linkedin.com/company/thehackernews/)
[**](https://www.youtube.com/c/thehackernews?sub_confirmation=1)
[**](https://www.instagram.com/thehackernews/)

[** RSS Feeds](https://feeds.feedburner.com/TheHackersNews)
[** Email Alerts](#email-outer)

[![Salesforce Security Handbook](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjWa8tsMNqlevi1HGF1ALQRGIq7hROPFAbHd3R1RTEOe73T8_Q2xW_-91t2jSGjU5peiPb8QYblGp4igNW-u2Qmlxbp2BKzTVMSvyXDZJmC-BYpiiJHrcnG5drmSP97iZ9PVIf1DeEr7U-7vWpe4HXwfMjt8FGNgq5mOycOJluYr9wF7YOKrQY9MfArwgjt/s728-e100/ai-agent-security-d.png)](https://thehackernews.uk/ai-agent-security-d)

# [New Case Study: The Malicious Comment](https://thehackernews.com/2024/05/new-case-study-malicious-comment.html)

**May 07, 2024**The Hacker NewsRegulatory Compliance / Cyber Threat

[![Malicious Comment](data:image/png;base64... "Malicious Comment")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhUS3LJkQuicN43D5NrxSf0xflKdo3GHVEdy089NmTUSypwNI70imjfQuBMzwrzNuBwmSdVJ9j-ARjsK2_kBTLRVilr8qOn7__e0I_38Wr6SR1yFGG16q-bOrtZy6HD6VOy2NkScWhynEiftat7H7gIhHRLr4jMiW2dD1wAP8L8FcTcCy9s6mb4QlJM958/s790-rw-e365/case.png)

### How safe is your comments section? Discover how a seemingly innocent 'thank you' comment on a product page concealed a malicious vulnerability, underscoring the necessity of robust security measures. Read the full real-life case study [here](https://www.reflectiz.com/learning-hub/malicious-comment-case-study/).

When is a 'Thank you' not a 'Thank you'? When it's a sneaky bit of code that's been hidden inside a 'Thank You' image that somebody posted in the comments section of a product page! The guilty secret hidden inside this particular piece of code was designed to let hackers bypass security controls and steal the personal identifying information of online shoppers, which could have meant big trouble for them and the company.

The page in question belongs to a global retailer. User communities are often a great source of unbiased advice from fellow enthusiasts, which was why a Nikon camera owner was posting there. They were looking for the ideal 50mm lens and asked for a recommendation. They offered thanks in advance to whoever might take the trouble to respond, and even left a little image that said, "Thank you," too, and to the naked eye it looked fine.

The comment and image stayed on the site for three years(!), but when the company started using the continuous web threat management solution from Reflectiz, a leading web security firm, it detected something troubling within this innocent-looking graphic during a routine monitoring scan. In this article, we give a broad overview of what happened, but if you'd prefer a deeper explanation, along with more details on how you can protect your own comments pages, you can download [the full, in-depth case study here](https://www.reflectiz.com/learning-hub/malicious-comment-case-study/).

## **Altered Images**

One of the best things about the web is the fact that you can easily share images, but as a human looking at hundreds of them every day, it's easy to forget that each one is made up of code, just like any other digital asset on a webpage. That being the case, malicious actors often try to [hide their own code](https://www.reflectiz.com/blog/obfuscation-techniques/) within them, which brings us to the practice of steganography. This is the term for hiding one piece of information inside another. It isn't the same as cryptography, which turns messages into gibberish so they can't be understood. Instead, steganography hides data in plain sight, in this case, inside an image.

## **Anatomy of a Pixel**

You may be aware that computer monitors display images using a mosaic of dots called pixels and that each pixel can emit a mixture of red, green, and blue light. The strength of each color in one of these RGB pixels is determined by a value between 0 and 255, so 255,0,0 gives us red, 0,255,0 gives us green, and so on.

255,0,0 is the strongest red that the screen can display, and while 254,0,0 is slightly less strong, it would look exactly the same to the human eye. By making lots of these small alterations to the values of selected pixels, malicious actors can hide code in plain sight. By changing enough of them, they can create a sequence of values that a computer can read as code, and in the case of the one posted in the photography retailer's comments section, the altered image contained hidden instructions and the address of a compromised domain. It was a surprise to find that the [JavaScript](https://www.reflectiz.com/blog/essential-guide-to-preventing-javascript-injection/) on the page was using the hidden information to communicate with it.

## **Consequences**

The big problem for anyone operating an e-commerce website is that malicious actors are always looking for opportunities to [steal customer PII](https://www.reflectiz.com/blog/prevent-data-harvesting-in-2023/) and payment card details, and altering image files is only one of many possible methods they use. Legislators in a growing number of territories, as well as rule makers in areas like the payment card industry, have responded by implementing detailed regulatory frameworks that impose stringent security requirements on providers along with big fines if they fail.

GDPR requires anybody selling to European Union customers to follow its large and detailed framework. Anytime an e-commerce retailer succumbs to steganography or any other kind of attack that compromises customer information, it can attract fines in the millions of dollars, trigger class action lawsuits, and create bad publicity that leads to reputational damage. That's why it's so crucial to understand how to defend your website from such attacks, [which the full case study explains.](https://www.reflectiz.com/learning-hub/malicious-comment-case-study/)

## **Continuous Protection**

[The case study](https://www.reflectiz.com/learning-hub/malicious-comment-case-study/) goes into depth on how this threat was uncovered and controlled, but the short explanation is that the platform's monitoring technology detected suspicious activity in a web component, then cross referenced certain details with its extensive threat database.

The system routinely identifies and blocks any third-party web components that [track user activity without their permission](https://www.reflectiz.com/learning-hub/case-study-the-risks-of-forgotten-pixels-on-websites/). It detects which third-party components get hold of users' geo-location, camera, and microphone permissions without their consent and it maps all web components that can access sensitive ...