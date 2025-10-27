---
title: Native Base64 decode function in SAP HANA
url: https://blogs.sap.com/2023/02/03/native-base64-decode-function-in-sap-hana/
source: SAP Blogs
date: 2023-02-04
fetch_date: 2025-10-04T05:40:30.729526
---

# Native Base64 decode function in SAP HANA

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Enterprise Resource Planning](/t5/enterprise-resource-planning/ct-p/erp)
* [ERP Blog Posts by Members](/t5/enterprise-resource-planning-blog-posts-by-members/bg-p/erp-blog-members)
* Native Base64 decode function in SAP HANA

Enterprise Resource Planning Blog Posts by Members

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/erp-blog-members/article-id/67985&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [Native Base64 decode function in SAP HANA](/t5/enterprise-resource-planning-blog-posts-by-members/native-base64-decode-function-in-sap-hana/ba-p/13562161)

![JoergAldinger](https://avatars.profile.sap.com/3/1/id31e217dabf6fc7c37593dfcef780a3654ecf7a4a1dbbe6f35af0e32ee7d0e3f5_small.jpeg "JoergAldinger")

[JoergAldinger](https://community.sap.com/t5/user/viewprofilepage/user-id/6838)

Active Contributor

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=erp-blog-members&message.id=67985)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/erp-blog-members/article-id/67985)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13562161)

‎2023 Feb 03
7:57 PM

[4
Kudos](/t5/kudos/messagepage/board-id/erp-blog-members/message-id/67985/tab/all-users "Click here to see who gave kudos to this post.")

3,312

* SAP Managed Tags
* [SAP Business One](https://community.sap.com/t5/c-khhcw49343/SAP%2520Business%2520One/pd-p/01200615320800000816)
* [SAP Business One, version for SAP HANA](https://community.sap.com/t5/c-khhcw49343/SAP%2520Business%2520One%252C%2520version%2520for%2520SAP%2520HANA/pd-p/67838200100800004775)
* [SAP HANA](https://community.sap.com/t5/c-khhcw49343/SAP%2520HANA/pd-p/73554900100700000996)

* [SAP Business One

  SAP Business One](/t5/c-khhcw49343/SAP%2BBusiness%2BOne/pd-p/01200615320800000816)
* [SAP Business One, version for SAP HANA

  SAP Business One](/t5/c-khhcw49343/SAP%2BBusiness%2BOne%25252C%2Bversion%2Bfor%2BSAP%2BHANA/pd-p/67838200100800004775)
* [SAP HANA

  Software Product](/t5/c-khhcw49343/SAP%2BHANA/pd-p/73554900100700000996)

View products (3)

Recently I had to work around some limitations in SAP Business One's Service Layer. As a result, I had to decode some BASE64 string that was stored in our customer's database, modify the (unencoded) string and then save it back, all from within a native SAP HANA Stored Procedure.

To my surprise, there is no native function to achieve this, at least not that I could find in my couple of hours of investigation.

So I set out to build my own function to allow for decoding Base64 strings on the database level.

I am posting this function here, so that others can save themselves a few hours if they are ever presented with the same problem.

Note: This is probably not the most performant way of doing this, but since it's not going to be executed massively it is good enough for our purpose. The function returns the decoded value of a 400-character string in 1-2 ms on our test server. If you do have have performance improvements, please share!

```
CREATE OR REPLACE FUNCTION "CEODO_FN_Base64Decode"

(

	base64 varchar(8000)

)

RETURNS decoded nvarchar(4000)

LANGUAGE SQLSCRIPT

SQL SECURITY INVOKER

DETERMINISTIC

AS

BEGIN

	declare i int;

	declare binstring varchar(16);

	binstring = '';

	decoded = '';

	FOR i IN 1..LENGTH(:base64) DO

		binstring := binstring ||

			CASE

				SUBSTRING(:base64, i, 1)

				WHEN 'A' THEN '000000'

				WHEN 'B' THEN '000001'

				WHEN 'C' THEN '000010'

				WHEN 'D' THEN '000011'

				WHEN 'E' THEN '000100'

				WHEN 'F' THEN '000101'

				WHEN 'G' THEN '000110'

				WHEN 'H' THEN '000111'

				WHEN 'I' THEN '001000'

				WHEN 'J' THEN '001001'

				WHEN 'K' THEN '001010'

				WHEN 'L' THEN '001011'

				WHEN 'M' THEN '001100'

				WHEN 'N' THEN '001101'

				WHEN 'O' THEN '001110'

				WHEN 'P' THEN '001111'

				WHEN 'Q' THEN '010000'

				WHEN 'R' THEN '010001'

				WHEN 'S' THEN '010010'

				WHEN 'T' THEN '010011'

				WHEN 'U' THEN '010100'

				WHEN 'V' THEN '010101'

				WHEN 'W' THEN '010110'

				WHEN 'X' THEN '010111'

				WHEN 'Y' THEN '011000'

				WHEN 'Z' THEN '011001'

				WHEN 'a' THEN '011010'

				WHEN 'b' THEN '011011'

				WHEN 'c' THEN '011100'

				WHEN 'd' THEN '011101'

				WHEN 'e' THEN '011110'

				WHEN 'f' THEN '011111'

				WHEN 'g' THEN '100000'

				WHEN 'h' THEN '100001'

				WHEN 'i' THEN '100010'

				WHEN 'j' THEN '100011'

				WHEN 'k' THEN '100100'

				WHEN 'l' THEN '100101'

				WHEN 'm' THEN '100110'

				WHEN 'n' THEN '100111'

				WHEN 'o' THEN '101000'

				WHEN 'p' THEN '101001'

				WHEN 'q' THEN '101010'

				WHEN 'r' THEN '101011'

				WHEN 's' THEN '101100'

				WHEN 't' THEN '101101'

				WHEN 'u' THEN '101110'

				WHEN 'v' THEN '101111'

				WHEN 'w' THEN '110000'

				WHEN 'x' THEN '110001'

				WHEN 'y' THEN '110010'

				WHEN 'z' THEN '110011'

				WHEN '0' THEN '110100'

				WHEN '1' THEN '110101'

				WHEN '2' THEN '110110'

				WHEN '3' THEN '110111'

				WHEN '4' THEN '111000'

				WHEN '5' THEN '111001'

				WHEN '6' THEN '111010'

				WHEN '7' THEN '111011'

				WHEN '8' THEN '111100'

				WHEN '9' THEN '111101'

				WHEN '+' THEN '111110'

				WHEN '/' THEN '111111'

				ELSE '' END;

		IF (LENGTH(:binstring) >= ![:smiling_face_with_sunglasses:](/html/@21D8126BF47555B5D081C1E25D328808/emoticons/1f60e.png ":smiling_face_with_sunglasses:") THEN

			decoded := decoded || CHAR(

				TO_INT(SUBSTRING(:binstring, 1, 1)) * 128 +

				TO_INT(SUBSTRING(:binstring, 2, 1)) * 64 +

				TO_INT(SUBSTRING(:binstring, 3, 1)) * 32 +

				TO_INT(SUBSTRING(:binstring, 4, 1)) * 16 +

				TO_INT(SUBSTRING(:binstring, 5, 1)) * 8 +

				TO_INT(SUBSTRING(:binstring, 6, 1)) * 4 +

				TO_INT(SUBSTRING(:binstring, 7, 1)) * 2 +

				TO_INT(SUBSTRING(:binstring, 8, 1)) * 1);

			binstring := SUBSTRING(:binstring, 9);

		END IF;

	END FOR;

END;
```

Happy coding!

Joerg

2 Comments

You must be a registered user to add a comment. If you've already registered, sign in. Otherwise, register and sign in.

* [Comment](/plugins/common/feature/oidcss/sso_login_redirect/providerid/sap_ids_prompt?redirectreason=permissiondenied&referer=https%3A%2F%2Fcommunity.sap.com%2Ft5%2Fenterprise-resource-planning-blog-posts-by-members%2Fnative-base64-decode-function-in-sap-hana%2Fba-p%2F13562161%23comment-on-this)

Copy Link
![](https://community.sap.com/html/@EE5D5986E9F4E5657DCEACB7532B5C39/assets/bluesky-dark.svg)Bluesky
Linkedin

Related Content

* [Embedding Native Android Crypto in SSAM: A QR-Code Security Story](/t5/enterprise-resource-planning-blog-posts-by-sap/embedding-native-android-crypto-in-ssam-a-qr-code-security-story/ba-p/14209674)
  in [Enterprise Resource Planning Blog Posts by SAP](/t5/enterprise-resource-planning-blog-posts-by-sap/bg-p/erp-blog-sap)  4 weeks ago
* [Warehouse Management in SAP S/4HANA Cloud Public Edition 2502 Release – What’s New](/t5/enterprise-resource-planning-blog-posts-by-sap/warehouse-management-in-sap-s-4hana-cloud-public-edition-2502-release-what/ba-p/14013819)
  in [Enterprise Resource Planning Blog Posts by SAP](/t5/enterprise-resource-planning-blog-posts-by-sap/bg-p/erp-blog-sap)  2025 Feb 13
* [SAPUI5 Custom Application: Digital Signature Draw Pad](/t5/enterprise-resource-planning-blog-posts-by-members/sapui5-custom-application-digital-signature-draw-pad/ba-p/13967618)
  ...