---
title: All that JavaScript for… spear phishing?
url: https://blog.nviso.eu/2024/10/02/all-that-javascript-for-spear-phishing/
source: NVISO Labs
date: 2024-10-03
fetch_date: 2025-10-06T18:52:21.357384
---

# All that JavaScript for… spear phishing?

[Skip to content](#content)

[![NVISO Labs](https://blog.nviso.eu/wp-content/uploads/2022/12/cropped-abn-zcrj_400x400-1.png)](https://blog.nviso.eu/)

[NVISO Labs](https://blog.nviso.eu/)

Cyber security research, straight from the lab! 🐀

* [twitter](https://twitter.com/NVISO_Labs)
* [linkedin](https://www.linkedin.com/company/nviso-cyber)
* mail us
* [our company](https://www.nviso.eu)
* [SSO](https://blog.nviso.eu/wp-admin/edit.php)

Menu

* [All](https://blog.nviso.eu/)
* [Blue Team](https://blog.nviso.eu/category/blue-team/)
* [Cloud Security](https://blog.nviso.eu/category/cloud-security/)
  + [AWS](https://blog.nviso.eu/category/cloud-security/aws/)
  + [Azure](https://blog.nviso.eu/category/cloud-security/azure/)
  + [GCP](https://blog.nviso.eu/category/cloud-security/gcp/)
  + [Microsoft 365](https://blog.nviso.eu/category/cloud-security/microsoft-365/)
* [Awareness](https://blog.nviso.eu/category/awareness/)
* [Forensics](https://blog.nviso.eu/category/forensics/)
* Other
  + [Application Security](https://blog.nviso.eu/category/application-security/)
  + [IoT Security](https://blog.nviso.eu/category/iot-security/)
  + [Web Security](https://blog.nviso.eu/category/web-security/)
  + [Industrial Security](https://blog.nviso.eu/category/industrial-security/)
  + [Mobile Security](https://blog.nviso.eu/category/mobile-security/)
  + [Cyber Strategy](https://blog.nviso.eu/category/cyber-strategy/)
  + [Purple Team](https://blog.nviso.eu/category/purple-team/)
  + [Red Team](https://blog.nviso.eu/category/red-team/)
  + [Events](https://blog.nviso.eu/category/events/)

# All that JavaScript for… spear phishing?

[Bart Parys](https://blog.nviso.eu/author/bart-parys/ "Posts by Bart Parys")

[Blue Team](https://blog.nviso.eu/category/blue-team/)

October 2, 2024October 31, 2024
11 Minutes

NVISO employs several hunting rules in multiple Threat Intelligence Platforms and other sources, such as VirusTotal. As you can imagine, there is no lack of APT (Advanced Persistent Threat) campaigns, cybercriminals and their associated malware families and campaigns, phishing, and so on. But now and then, something slightly different and perhaps novel passes by.

In this blog post, we’ll describe such a campaign which we assess has been created by an actor with at least a medium level of technical competence due to multiple obfuscation layers in ultimate payload delivery.

**Stage 1 – Initial Lure**

The initial lure consists of a classic “bait” scheme involving a so called voicemail left by a caller, and urging the recipient to download a ZIP file containing HTML attachment as shown in Figure 1.

![](https://blog.nviso.eu/wp-content/uploads/2024/10/image.png)

Figure 1 – Voice mail lure

Figure 2 displays the further email context.

![](https://blog.nviso.eu/wp-content/uploads/2024/10/image-1.png)

Figure 2 – Email details

From the email context, it appears the email was sent from a legitimate business which has been compromised in order to send out the phishing campaign.

The subject of the email in turn is simply the name of the targeted company, and the attachment name follows the pattern of “*Companyname* Micro.protected.zip”.  The ZIP contains a single HTML which follows the same naming pattern.

The HTML contains obfuscated JavaScript and once the intended target opens the HTML file, it will automatically perform several rounds of decoding, deobfuscation and decryption to eventually lead to a customised spear phishing page. This technique is also known as “HTML smuggling”, a technique where attackers embed certain code, such as JavaScript, into an HTML file which will be automatically rendered (loaded) by the browser.

The technique has gained popularity over the years as it may bypass certain security mechanisms such as email gateways or even endpoint detection systems as an HTML file *typically* does not contain malicious content.

Let’s dive into the next stages.

**Stage 2 – The HTML and JavaScript**

To follow along, the HTML we will analyse in the next sections has the following properties:

* **MD5:** cde00cb2b65ee286fec3017beb953795
* **SHA1:** eabfaa69c1e3b6a04d17c76987becd63b5b78076
* **SHA256:** 287691ade84c692b9ea3af2bee22096d13584c817fcb7c908c3c4c17c582aa5f

Note the sample has also been made available on MalwareBazaar.

As described previously, the JavaScript embedded in the HTML will be similar to what’s shown in Figure 3 below.

![](https://blog.nviso.eu/wp-content/uploads/2024/10/image-2.png)

Figure 3 – obfuscated JavaScript

The script initialises an array of what appears a mix of binary (e.g. `1100011`) and hex values (e.g. `3c`). When dealing with JavaScript, the decoding functionality is typically near the end of the file, and this is no different in our case, as displayed in Figure 4:

![](https://blog.nviso.eu/wp-content/uploads/2024/10/image-3.png)

Figure 4 – Decoding function

The following snippet displays the *beautified* decoding function:

```
let decodedHtml = "";

for (let mixed of arr) {

  let isHex = mixed[0] != '1';

  if (isHex) {

    decodedHtml += String.fromCharCode(parseInt(mixed, 16));

  } else {

    decodedHtml += String.fromCharCode(parseInt(mixed, 2));

  }

}

document.write(decodedHtml)
```

JavaScript

The decoding function is straightforward: it will validate if a character is in hex or binary format and perform the decoding using [`fromCharCode`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String/fromCharCode). Once completed, it will “write” the decoded content to the same HTML page and execute it.

When dealing with any type of JavaScript, there’s a classic set of clues that will indicate something malicious going on, such as [`eval`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/eval), [`document.write`](https://developer.mozilla.org/en-US/docs/Web/API/Document/write), certain verbs and functions…

Decoding or deobfucation can happen in a myriad of ways, for example, we can redirect output to a message box, we can substitute an eval for an action, but in this case we can take a simple approach: just let the script decode itself!

**Stage 3 – The JavaScript and… the JavaScript**

But how can we let the script decode itself? The easiest way is to replace `document.write` with [`console.log`](https://developer.mozilla.org/en-US/docs/Web/API/console/log_static). This will simply output or redirect the content of `decodedHtml`, which ultimately contains the payload or next stage, to the console.

To perform this, open up your favourite browser: in our example, we’ll use Google Chrome. Note that you should still perform this kind of analysis in a secure environment such as a sandbox or Virtual Machine: some JavaScript payloads may contain an exploit, immediately download and execute malware (rather than portray a phishing page), or may contain some sneaky `evals` that when missed, might alter the results you are expecting.

Open Google Chrome, go to Developer Tools (or press **CTRL** + **SHIFT** + **i**), open the Console tab. You may need to allow pasting, and finally we can add in the content of the HTML. Note you will need to remove the`<script>` tags for it to function correctly.

Replacing `document.write` with `console.log` yields:

![](https://blog.nviso.eu/wp-content/uploads/2024/10/image-4.png)

Figure 5 – Decoded script

Great success! It appears we were able to get the payload. However, a next encoded block awaits in value `u`, and the script appears to call a file hosted on Cloudflare for further functionality.

As before, let’s go to the end of the script and we can observe the following function:

![](https://blog.nviso.eu/wp-content/uploads/2024/10/image-5.png)

Figure 6 – Next decoding function

The same decoding function, beautified:

```
function p(d, h) {

              const b = CryptoJS.enc.Base64.parse(d);

              const m = CryptoJS.enc.Utf8.parse(h);

              const v = CryptoJS.AES.decrypt({ ciph...