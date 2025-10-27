---
title: First glance at ChatGPT and its potential for ABAPers
url: https://blogs.sap.com/2023/02/21/first-glance-at-chatgpt-and-its-potential-for-abapers/
source: SAP Blogs
date: 2023-02-22
fetch_date: 2025-10-04T07:42:35.424291
---

# First glance at ChatGPT and its potential for ABAPers

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Enterprise Resource Planning](/t5/enterprise-resource-planning/ct-p/erp)
* [ERP Blog Posts by Members](/t5/enterprise-resource-planning-blog-posts-by-members/bg-p/erp-blog-members)
* First glance at ChatGPT and its potential for ABAP...

Enterprise Resource Planning Blog Posts by Members

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/erp-blog-members/article-id/67395&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [First glance at ChatGPT and its potential for ABAPers](/t5/enterprise-resource-planning-blog-posts-by-members/first-glance-at-chatgpt-and-its-potential-for-abapers/ba-p/13554616)

![kimveasna_xyz](https://avatars.profile.sap.com/c/5/idc5d19b9e5edb7d34533bc004fd8c399012b3a9e4249ad0b62c59f56767edd19e_small.jpeg "kimveasna_xyz")

[kimveasna\_xyz](https://community.sap.com/t5/user/viewprofilepage/user-id/292004)

Explorer

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=erp-blog-members&message.id=67395)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/erp-blog-members/article-id/67395)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13554616)

‎2023 Feb 21
10:02 PM

[17
Kudos](/t5/kudos/messagepage/board-id/erp-blog-members/message-id/67395/tab/all-users "Click here to see who gave kudos to this post.")

12,522

* SAP Managed Tags
* [Artificial Intelligence](https://community.sap.com/t5/c-khhcw49343/Artificial%2520Intelligence/pd-p/c3c3a408-33ea-4c2a-ae6f-05461e76982d)
* [SAP S/4HANA](https://community.sap.com/t5/c-khhcw49343/SAP%2520S%252F4HANA/pd-p/73554900100800000266)

* [SAP S/4HANA

  SAP S/4HANA](/t5/c-khhcw49343/SAP%2BS%25252F4HANA/pd-p/73554900100800000266)
* [Artificial Intelligence

  Product Category](/t5/c-khhcw49343/Artificial%2BIntelligence/pd-p/c3c3a408-33ea-4c2a-ae6f-05461e76982d)

View products (2)

ChatGPT is one of the biggest, if not the biggest, innovation buzz in IT in the past years. If you don't know it, it will itself summarize as :
> ChatGPT is a computer program that can hold a conversation with people in a natural and conversational way. It's a "chatbot" that uses advanced machine learning algorithms to understand and generate human-like language. It's called a "large language model" because it has been trained on a vast amount of text data to generate text that is similar to human language. ChatGPT can be used for a variety of tasks, such as answering questions, generating text, and holding a conversation. It's a powerful tool that can help people communicate with computers in a more natural and intuitive way, and has the potential to be used in many different applications in the future.

I have browsed and learned about the different use cases, and I was astonished to discover that though it is not specialized in one specific area, it is capable of doing SAP ABAP development.

I wanted to give it a try myself, and understand what I could do with it in my everyday work, especially how it could save us some time in our daily (most boring) tasks.

My use case: we have received lately a new business requirement in order to "skip" some of the approvals for purchase orders, under certain limited conditions (purchase order type and plants). Technically, this could be designed as:

* a simple program with inputs as purchase order type and plants

* selection of the relevant PO

* for each one, release the PO

* display results.

Here is my chat discussion with my new friend, verbatim (sorry, this is a bit long).

![](/legacyfs/online/storage/blog_attachments/2023/02/Capture-décran-2023-02-21-à-22.22.10.png)

![](/legacyfs/online/storage/blog_attachments/2023/02/Capture-décran-2023-02-21-à-22.30.04.png)

![](/legacyfs/online/storage/blog_attachments/2023/02/Capture-décran-2023-02-21-à-22.31.25.png)

![](/legacyfs/online/storage/blog_attachments/2023/02/Capture-décran-2023-02-21-à-22.32.15.png)

![](/legacyfs/online/storage/blog_attachments/2023/02/Capture-décran-2023-02-21-à-22.33.03.png)

![](/legacyfs/online/storage/blog_attachments/2023/02/Capture-décran-2023-02-21-à-22.33.50.png)

![](/legacyfs/online/storage/blog_attachments/2023/02/Capture-décran-2023-02-21-à-22.34.31.png)

![](/legacyfs/online/storage/blog_attachments/2023/02/Capture-décran-2023-02-21-à-22.34.57.png)

![](/legacyfs/online/storage/blog_attachments/2023/02/Capture-décran-2023-02-21-à-22.35.47.png)

![](/legacyfs/online/storage/blog_attachments/2023/02/Capture-décran-2023-02-21-à-22.36.21.png)![](/legacyfs/online/storage/blog_attachments/2023/02/Capture-décran-2023-02-21-à-22.37.11.png)![](/legacyfs/online/storage/blog_attachments/2023/02/Capture-décran-2023-02-21-à-22.37.58.png)![](/legacyfs/online/storage/blog_attachments/2023/02/Capture-décran-2023-02-21-à-22.39.28-1.png)![](/legacyfs/online/storage/blog_attachments/2023/02/Capture-décran-2023-02-21-à-22.39.58.png)![](/legacyfs/online/storage/blog_attachments/2023/02/Capture-décran-2023-02-21-à-22.42.19.png)

![](/legacyfs/online/storage/blog_attachments/2023/02/Capture-décran-2023-02-21-à-22.43.39.png)

![](/legacyfs/online/storage/blog_attachments/2023/02/Capture-décran-2023-02-21-à-22.44.26.png)

![](/legacyfs/online/storage/blog_attachments/2023/02/Capture-décran-2023-02-21-à-22.45.14.png)

WOW. Sorry, it is way too technical and too long but what I mean to say is that ChatGPT is REALLY surprising. Not because the code is clean and usable (it is not at all actually), but because it has reached the level of a kid developer (who would have read a lot of books/blogs) or a bad developer (who would have NOT read a lot of books/blogs).

* ChatGPT cognition is based on a statistical model, very advanced one, but still a statistical model: all the code lines he has proposed are a fuzzy mix of all the different source codes he has been through. What is extraordinary is that it was able to propose the correct tables for selection, the correct function to be used

* The NLP (Natural Language Processing) has reached a very high level. From my request, it was able to put a context, infer the expected input/outputs

Beyond the WOW effects, there are still some glitches in my experiment:

* ChatGPT does not invent source code (well, not really), it reproduces code that it has learned. Sometimes, you will notice piece of codes out of nowhere, or piece of codes that are shuffled/replaced by something else totally different. I guess we will face the same issues as with Github Copilot, and maybe issues with some copyrights?

* Though the skeleton source code can look good, it takes you a very long time to fine tune the code with the chat, especially because the answers are not always consistant (the code could randomly change for whatever reason). You will find it faster to change the code yourself.

* I feel that ChatGPT is not trying to provide you with the best answer, but the most common answers from blogs. It may propagate wrong code (just like fake news spread by chatbots).

##

## Conclusion

AI is one of the big innovation of the decade. Its true power is still to be unleashed and everyone is imagining use cases. AI is not only ChatGPT, and many other initiatives exist, OpenAI is at the moment one of the most famous ones.

We may ask ourself what it can bring to SAP folks:

* Speed up some common tasks (scaffolding for developments, chec...