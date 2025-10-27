---
title: Bypassing Asymmetric Client Side Encryption Without Private Key
url: https://infosecwriteups.com/bypassing-asymmetric-client-side-encryption-without-private-key-822ed0d8aeb6?source=rss----7b722bfd1b8d--bug_bounty
source: Bug Bounty in InfoSec Write-ups on Medium
date: 2023-03-11
fetch_date: 2025-10-04T09:13:26.275399
---

# Bypassing Asymmetric Client Side Encryption Without Private Key

[Sitemap](/sitemap/sitemap.xml)

[Open in app](https://rsci.app.link/?%24canonical_url=https%3A%2F%2Fmedium.com%2Fp%2F822ed0d8aeb6&%7Efeature=LoOpenInAppButton&%7Echannel=ShowPostUnderCollection&%7Estage=mobileNavBar&source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fbypassing-asymmetric-client-side-encryption-without-private-key-822ed0d8aeb6&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

[Medium Logo](https://medium.com/?source=post_page---top_nav_layout_nav-----------------------------------------)

[Write](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-story&source=---top_nav_layout_nav-----------------------new_post_topnav------------------)

[Search](https://medium.com/search?source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fbypassing-asymmetric-client-side-encryption-without-private-key-822ed0d8aeb6&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

![](https://miro.medium.com/v2/resize:fill:64:64/1*dmbNkD5D-u45r44go_cf0g.png)

[## InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---publication_nav-7b722bfd1b8d-822ed0d8aeb6---------------------------------------)

·

Follow publication

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:76:76/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_sidebar-7b722bfd1b8d-822ed0d8aeb6---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow publication

# Bypassing Asymmetric Client Side Encryption Without Private Key

[![Sourav Kalal](https://miro.medium.com/v2/resize:fill:64:64/1*3dHIoCEZxeENLBxleec9sw.png)](https://blog.souravkalal.tech/?source=post_page---byline--822ed0d8aeb6---------------------------------------)

[Sourav Kalal](https://blog.souravkalal.tech/?source=post_page---byline--822ed0d8aeb6---------------------------------------)

7 min read

·

Mar 10, 2023

--

3

Listen

Share

Press enter or click to view image in full size

![]()

Keys

I recently wrote an article on how we can bypass client-side encryption. With the help of the PyCript burp suite extension, we can make manual and automated pentesting or bug bounty much easier on applications with client-side encryption. The use of the PyCript extension fails when the application uses asymmetric encryption.

Since asymmetric encryption uses private and public key mechanisms. It's not possible to decrypt the request without having both keys. The application will store the public on the client side and will use the public key to encrypt the request. To decrypt we need a private key and in most cases, we won’t have the private key since it's stored on the server side.

The only options left to test the application with asymmetric encryption are using the browser console with breakpoint and in the case of mobile application, we need to use the Frida to log the plain text.

### Solution

The only possible solution I was able to figure out was using the Chrome override feature with PyCript configured in Burp Suite. The Chrome browser allows us to edit the JavaScript file and load the JavaScript file from the local system. We can use it to modify our application JavaScript file to send a plain text request instead of an encrypted request.

Press enter or click to view image in full size

![]()

Browser Flow

The above flow is simple where JavaScript code will send the HTTP request for each action we perform on the browser UI. The same code will call another JavaScript code to encrypt the request and return the encrypted value. The main code will now send the encrypted request and the same will be visible in the burp suite proxy.

Press enter or click to view image in full size

![]()

Modified Flow

In the above, we have modified the encryption code using the chrome override feature to return the original plain text instead of the encrypted request. In this case, we can see the decrypted request in the burp suite proxy. Since the server will expect the encrypted request we will configure the PyCript to encrypt the request using the same public key and encryption logic as the application's JavaScript code.

Using the above approach we will have a plain text request in the burp suite proxy history and we can use the same plain text request everywhere like for repeater or intruder. The application on the server side will receive the encrypted request with the help of the PyCript extension.

### Example

I have the below application by intercepting the request in the proxy I can confirm that the application is using some kind of encryption.

Press enter or click to view image in full size

![]()

Encrypted Request

After looking into the JavaScript code and searching for keywords like `encrypt, key, encryption,decrypt` etc. I got the encryption code.

Press enter or click to view image in full size

![]()

Encryption Code

The above code looks quite simple and easy to understand. The function takes one argument and it will be the plain text data. Next, the code converts the PEM public key and encrypts the plain text data using the key. Lastly, the code base64 encodes the encrypted data and returns it. After doing some research I found that the application is using the node-forge library for encryption.

Press enter or click to view image in full size

![]()

Debug

Now just to confirm that the same code is responsible for encryption, I add a breakpoint and submit the request in the browser. The browser stops when the breakpoint code is triggered. I can confirm that the same code is used for encryption and the function is taking plain text value.

Press enter or click to view image in full size

![]()

Values

I keep the breakpoint the same as it is and call the variables from the console and I got the public key used for encryption. Now we want that the function should return the plain text or the same value instead of the encrypted value.

Press enter or click to view image in full size

![]()

Override

Now to modify the JavaScript code we need to use the override from the chrome browser. Select the `Overrides`from the source tab. Click on the `Select folder for overrides`.

Press enter or click to view image in full size

![]()

Override

Once you select the folder you need to approve it. Click on the allow and it will allow you to modify the files. Now go to the file which we want to edit.

Press enter or click to view image in full size

![]()

Save override

Right-click on the file and select `Save for overrides`. and now if we back to the override tab we can see the same file is added which allows us to edit the JavaScript code.

Press enter or click to view image in full size

![]()

Edit Encryption Logic

Now we need to edit the JavaScript code. We modify the code and remove the encryption code and return the same plain text value that was passed to the function. Once we complete the editing we can save it with `ctrl+s`.

Once it's completed I need to verify if it's working as expected. I go back to the application and perform any action so any request will be sent. In the burp suite, I need to verify if the request is in plain text or not.

Press enter or click to view image in full size

![]()

Plain the request

Now I can confirm that I was able to modify the client-side logic and can see the data in plain text format in the burp suite proxy. The application is giving an error as it was expecting the enc...