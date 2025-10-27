---
title: Obtaining Digital Signature using PKCS#1 Encryption in SAP Process Orchestration (PO) and Cloud Integration (CI)
url: https://blogs.sap.com/2023/04/18/obtaining-digital-signature-using-pkcs1-encryption-in-sap-process-orchestration-po-and-cloud-integration-ci/
source: SAP Blogs
date: 2023-04-19
fetch_date: 2025-10-04T11:34:09.466282
---

# Obtaining Digital Signature using PKCS#1 Encryption in SAP Process Orchestration (PO) and Cloud Integration (CI)

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Technology](/t5/technology/ct-p/technology)
* [Technology Blog Posts by Members](/t5/technology-blog-posts-by-members/bg-p/technology-blog-members)
* Obtaining Digital Signature using PKCS#1 Encryptio...

Technology Blog Posts by Members

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/technology-blog-members/article-id/160520&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [Obtaining Digital Signature using PKCS#1 Encryption in SAP Process Orchestration (PO) and Cloud Integration (CI)](/t5/technology-blog-posts-by-members/obtaining-digital-signature-using-pkcs-1-encryption-in-sap-process/ba-p/13552763)

![former_member603969](https://avatars.profile.sap.com/former_member_small.jpeg "former_member603969")

[former\_member603969](https://community.sap.com/t5/user/viewprofilepage/user-id/603969)

Explorer

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=technology-blog-members&message.id=160520)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/technology-blog-members/article-id/160520)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13552763)

‎2023 Apr 18
10:12 PM

[1
Kudo](/t5/kudos/messagepage/board-id/technology-blog-members/message-id/160520/tab/all-users "Click here to see who gave kudos to this post.")

1,854

* SAP Managed Tags
* [SAP Integration Suite](https://community.sap.com/t5/c-khhcw49343/SAP%2520Integration%2520Suite/pd-p/73554900100800003241)
* [Cloud Integration](https://community.sap.com/t5/c-khhcw49343/Cloud%2520Integration/pd-p/67837800100800006801)
* [SAP Process Integration](https://community.sap.com/t5/c-khhcw49343/SAP%2520Process%2520Integration/pd-p/01200615320800000719)
* [SAP Process Orchestration](https://community.sap.com/t5/c-khhcw49343/SAP%2520Process%2520Orchestration/pd-p/477916618626075516391832082074785)

* [Cloud Integration

  SAP Integration Suite](/t5/c-khhcw49343/Cloud%2BIntegration/pd-p/67837800100800006801)
* [SAP Process Integration

  SAP NetWeaver](/t5/c-khhcw49343/SAP%2BProcess%2BIntegration/pd-p/01200615320800000719)
* [SAP Process Orchestration

  Software Product](/t5/c-khhcw49343/SAP%2BProcess%2BOrchestration/pd-p/477916618626075516391832082074785)
* [SAP Integration Suite

  SAP Integration Suite](/t5/c-khhcw49343/SAP%2BIntegration%2BSuite/pd-p/73554900100800003241)

View products (4)

Dear All

**Introduction**

Recently, we had a requirement to generate the digital signature of payment file using PKCS#1 algorithm and push the signed file from SAP to Bank Server. Let us see the steps involved for this process in both PO and CI.

**RSA Key Pair Generation**

Before that, let’s walkthrough the key generation procedure.

* We need to create an RSA key pair using any online tool, one of such is below.

<https://8gwifi.org/RSAFunctionality?rsasignverifyfunctions=rsasignverifyfunctions&keysize=2048>

* Note that it generates public key in PKCS#8 format and private key in PKCS#1 format. Copy the contents of both private and public key to local files (with pem extension). There are multiple blogs to understand the difference between PKCS#1 and PKCS#8. With respect to data representation, the difference is as below.

**PKCS#1 Public Key                                                    PKCS#8 Public Key**![](/legacyfs/online/storage/blog_attachments/2023/04/Picture1-40.png)

**PKCS#1 Private Key                                                  PKCS#8 Private Key**![](/legacyfs/online/storage/blog_attachments/2023/04/Picture2-28.png)

* We can share the Public key in same format(PKCS#8) to third party, whosoever is going to verify the signature.

**Steps in PO**

1. In PO, we do not have a standard function or module to do the PKCS#1 encryption. So, we are going to use the necessary java library to achieve it.

2. PKCS#1 and PKCS#8 are related to each other and we can convert the key from one format to equivalent another format.

3. To use java function, we need to first convert the PKCS#1 private key to its equivalent PKCS#8 private key.

4. For Key conversion, we need to have OpenSSL tool installed in our machine. We are going to convert the private key from PKCS1 to PKCS8 format by running the OpenSSL tool and providing the below command.*pkcs8 -topk8 -in Key\_PKCS1.pem -out Key\_PKCS8.pem -nocrypt*where Key\_PKCS1.pem= PKCS#1 Private Key (input)
   Key\_PKCS8.pem = PKCS#8 Private Key (output)

5. We need to make sure that the input PKCS#1 key is in the same directory path in which we have the OpenSSL application. The output key will also be generated in same path.

6. We need to copy the contents of output PKCS#8 Key, remove the new lines, make it as a single line concatenated String and use it as a parameter input for the PI UDF. The UDF is of below.

//Java Class to be Referenced

java.security.Signature

java.security.spec.PKCS8EncodedKeySpec

java.util.Base64

//Actual Code

AbstractTrace trace = container.getTrace;

//Output Signature will be stored in this String signature

String signature = "";

try

{

//str\_PrivateKey is the parameter to this UDF that contains the PKCS#8 private Key

byte[] b1 = Base64.getDecoder().decode(str\_PrivateKey);

PKCS8EncodedKeySpec spec = new PKCS8EncodedKeySpec(b1);

KeyFactory kf = KeyFactory.getInstance("RSA");

Signature privateSignature = Signature.getInstance("SHA256withRSA");

privateSignature.initSign(kf.generatePrivate(spec));

//str\_Input is the input data to be digitally signed

privateSignature.update(str\_Input.getBytes("UTF-8"));

byte[] s = privateSignature.sign();

signature = Base64.getEncoder().encodeToString(s);

trace.addInfo("Signature of Input - " +signature);

}

catch(Exception e)

{

trace.addWarning("Exception raised - " +e.toString());

}

return(signature);

The above code can be enhanced to append the signature to the original input as per the requirement.

**Steps in CI**

1. In CI, we need to navigate to CI Monitoring -> Keystore -> Add -> RSA Key. Provide the suitable alias name, browse through the saved PKCS#1 Private Key (this is done in RSA Key pair generation step above), fill the required details and click on Add.

2. In the Integration flow, we should add the “Simple Signer” palette such that the input to this step is the message to be digitally signed.

3. We need to add the below parameters under Simple Signer.

   * **Private Key Alias** – The alias name provided in Step 1

   * **Signature Algorithm** – Select the suitable option from dropdown.

   * **Signature Header Name** – Custom name. The output of simple signer holds the signature value in the header parameter with this provided custom name.

4. In the next palette of Iflow, we can get the signature value from the signature header and append it with the original file as per the need.

**Conclusion**

Hope this article is helpful to perform RSA PKCS#1 encryption and it illustrates the difference in steps involved in PO & CI (the latter being much easier to implement) Please feel free to add any comments/suggestions.

Regards

Baskaran

2 Comments

You must be a registered user to add a comment. If you've already registered, sign in. Otherwise, register and sign in.

* [Comment](/plugins/common/feature/oidcss/sso_login_redirect/providerid/sap_ids_prompt?redirectreason=permissiondenied&referer=https%3A%2F%2Fcommunity.sap.com%2Ft5%2Ftechnolog...