---
title: New Technique Bypass File Upload
url: https://infosecwriteups.com/new-technique-bypass-file-upload-4c18cef9f9ed?source=rss----7b722bfd1b8d--bug_bounty
source: Bug Bounty in InfoSec Write-ups on Medium
date: 2025-09-29
fetch_date: 2025-10-02T20:50:19.614575
---

# New Technique Bypass File Upload

[Sitemap](/sitemap/sitemap.xml)

[Open in app](https://rsci.app.link/?%24canonical_url=https%3A%2F%2Fmedium.com%2Fp%2F4c18cef9f9ed&%7Efeature=LoOpenInAppButton&%7Echannel=ShowPostUnderCollection&%7Estage=mobileNavBar&source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fnew-technique-bypass-file-upload-4c18cef9f9ed&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

[Medium Logo](https://medium.com/?source=post_page---top_nav_layout_nav-----------------------------------------)

[Write](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-story&source=---top_nav_layout_nav-----------------------new_post_topnav------------------)

[Search](https://medium.com/search?source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fnew-technique-bypass-file-upload-4c18cef9f9ed&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

![](https://miro.medium.com/v2/resize:fill:64:64/1*dmbNkD5D-u45r44go_cf0g.png)

[## InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---publication_nav-7b722bfd1b8d-4c18cef9f9ed---------------------------------------)

·

Follow publication

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:76:76/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_sidebar-7b722bfd1b8d-4c18cef9f9ed---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow publication

# New Technique Bypass File Upload

[![Abbas.heybati](https://miro.medium.com/v2/resize:fill:64:64/1*JNrM4Cyp_7fI4XQ7cTS2hA.jpeg)](https://medium.com/%40abbasheybati1?source=post_page---byline--4c18cef9f9ed---------------------------------------)

[Abbas.heybati](https://medium.com/%40abbasheybati1?source=post_page---byline--4c18cef9f9ed---------------------------------------)

5 min read

·

4 days ago

--

4

Listen

Share

## **This write-up focuses on bypass file upload.**

**Introduction**
 During my security research on Outlook Web, I encountered an unusual behavior that led me to discover a security vulnerability. In this article, I’ll explain how I found this issue, how I analyzed it, and why it happened. This vulnerability is currently being addressed by Microsoft, but the process of discovering and analyzing it can be useful for other security researchers. **The main focus of this article will be on how to bypass file upload restrictions**.

**How the Bug Was Discovered**
 Initially, I wanted to test how Outlook Web handles different types of files. So, I created a test.svg file and attached it to an email in two different ways:

1. **First Method: Attaching the File (Uploading as an Attachment)**

· When I uploaded the SVG file as an attachment, Microsoft made it available for download.

· However, in some cases, uploading this type of file was blocked.

![]()

**2. Second Method: Copy/Pasting (Ctrl+C, Ctrl+V) the File into the Email Body**

* In this case, instead of being made available for download, the file was displayed directly within the body of the email!
* This means the SVG content was embedded in the email without any security filtering and was loaded on the recipient’s side.

Press enter or click to view image in full size

![]()

This difference in behavior seemed unusual to me and worth a deeper investigation.

**Technical Analysis: Why Was This Happening?**

1. **The Role of contentEditable and designMode in Outlook Web**
    Outlook Web uses contentEditable for the email editing area. This feature allows HTML content to be inserted directly into the email body.

* When I attach an SVG file, Microsoft’s server processes the file and applies security rules to it.
* However, when I copy and paste the SVG, its contents are inserted as part of the HTML body of the email, and no security filters are applied to it!

Press enter or click to view image in full size

![]()

This means that Microsoft only applies security restrictions to attached files, but does not perform the same checks on pasted content.

**What is contentEditable and How Does It Work?**
 contentEditable is an attribute in HTML that allows any HTML element to be directly edited by the user, similar to a text editor.

Press enter or click to view image in full size

![]()

**What Happens in the Browser When You Press Ctrl+C and Ctrl+V?**

**Step 1: Copying (Ctrl+C)**
 When you select a file (e.g., test.svg) from your computer and press Ctrl+C, the following happens:

1. **The Operating System (OS) places the file into the clipboard**

* In Windows and macOS, when you press Ctrl+C, the data related to test.svg is stored in the system’s Clipboard API.
* This data can include the raw file bytes, metadata, and even its MIME type (e.g., image/svg+xml).

**2. The Clipboard API holds the information**

* The browser can use the Clipboard API to check what’s in the clipboard.
* Depending on the data type, the browser may retrieve text, images, or even a full file from the clipboard.

**Step 2: Pasting (Ctrl+V) into Outlook Web**
 When you press Ctrl+V inside the email body, several important things happen:

**Scenario 1: Pasting into a contentEditable field (Outlook Web)**
 Since Outlook Web uses contentEditable, the browser inspects the copied data:

1. The browser queries the Clipboard API: “Is there a file or HTML content in the clipboard?”
2. If there is a file (like test.svg), the browser checks whether that file type is allowed to be pasted directly into a contentEditable field.
3. Because SVG is a text-based file (XML-based), the browser may treat its contents as HTML text rather than a file.
4. As a result, the browser inserts the content of test.svg directly into the email body — as if the user pasted an HTML snippet!

This is what allows any malicious code inside the SVG to be executed!

**2. How Could This Behavior Be Exploited?**
 By leveraging this unexpected behavior, I was able to embed code in an SVG file that enabled several types of attacks. I’ll show you two examples:

**a) iframe Inside the SVG**

One limitation was that it wouldn’t load addresses using an IP or HTTP, so I had to purchase a domain and host a fake test page at:
 <https://yamikaza.com/fake.html>

Here’s the embedded SVG code:

```
<svg width="100vw" height="100vh">
    <foreignObject width="100%" height="100%">
        <body xmlns="http://www.w3.org/1999/xhtml" style="margin: 0; height: 100%;">
            <iframe src="https://yamikaza.com/fake.html" width="100%" height="100%" style="border: none;"></iframe>
        </body>
    </foreignObject>
</svg>
```

This code caused a fake page to load within the domain attachment.outlook.live.net, which could appear to users as an official Microsoft page.

Press enter or click to view image in full size

![]()

Press enter or click to view image in full size

![]()

b) Executing JavaScript (XSS) in SVG

```
<svg xmlns="http://www.w3.org/2000/svg" width="400" height="400" viewBox="0 0 124 124" fill="none">
  <rect width="124" height="124" rx="24" fill="#000000"/>
  <script type="text/javascript">
    alert(origin);
  </script>
</svg>
```

This code demonstrated that it was possible to execute JavaScript on the domain attachment.outlook.live.net.
 Although this domain did not have access to the cookies of outlook.live.com, it was still possible to run JavaScript code within this subdomain.

Press enter or click to view image in full size

![]()

**How Did I Test This Attack?**

1. I s...