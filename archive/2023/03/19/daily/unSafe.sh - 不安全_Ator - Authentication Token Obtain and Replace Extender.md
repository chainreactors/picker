---
title: Ator - Authentication Token Obtain and Replace Extender
url: https://buaq.net/go-154075.html
source: unSafe.sh - 不安全
date: 2023-03-19
fetch_date: 2025-10-04T10:01:58.734309
---

# Ator - Authentication Token Obtain and Replace Extender

* [unSafe.sh - 不安全](https://unsafe.sh)
* [我的收藏](/user/collects)
* [今日热榜](/?hot=true)
* [公众号文章](/?gzh=true)
* [导航](/nav/index)
* [Github CVE](/cve)
* [Github Tools](/tools)
* [编码/解码](/encode)
* [文件传输](/share/index)
* [Twitter Bot](https://twitter.com/buaqbot)
* [Telegram Bot](https://t.me/aqinfo)
* [Search](/search/search)

[Rss](/rss.xml)

[ ]
黑夜模式

![](https://8aqnet.cdn.bcebos.com/ccaf3ec3724c59b976ebec6f774a9dbd.jpg)

Ator - Authentication Token Obtain and Replace Extender

The plugin is created to help automated scanning using Burp in the following scenarios: A
*2023-3-18 19:30:0
Author: [www.kitploit.com(查看原文)](/jump-154075.htm)
阅读量:20
收藏*

---

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiSfXQYf0okK438HwSZLkDzfbu8q8y1qW9uctfIAqwiEyY8s1fIbJW64QDADhW2Jv1RMJY1bjEk8xkOMADc8crGh8ip-HKWlOiCzfr76XX0bXWbLyTU-8WkRrTiFHF99c1qVJRFn3FoNeUfqncbIIVOYtd70FbZRQV4Waf7jEaDkAJ1ZnsTWKeytdR9ng/w640-h404/ator.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiSfXQYf0okK438HwSZLkDzfbu8q8y1qW9uctfIAqwiEyY8s1fIbJW64QDADhW2Jv1RMJY1bjEk8xkOMADc8crGh8ip-HKWlOiCzfr76XX0bXWbLyTU-8WkRrTiFHF99c1qVJRFn3FoNeUfqncbIIVOYtd70FbZRQV4Waf7jEaDkAJ1ZnsTWKeytdR9ng/s903/ator.png)

The plugin is created to help automated scanning using Burp in the following scenarios:

1. Access/Refresh token
2. Token replacement in XML,JSON body
3. Token replacement in cookies

Key advantages:

1. We have also achieved in-memory token replacement to avoid duplicate login requests like in both custom extender, macros/session rules.
2. Easy UX to help obtain data (from response) and replace data (in requests) using regex. This helps achieve complex scenarios where response body is JSON, XML and the request text is also JSON, XML, form data etc.
3. Scan speed - the scan speed increases considerably because there are no extra login requests. There is something called the "Trigger Request" which is the error condition (also includes regex) when the login requests are triggered. The error condition can include (response code = 401 and body contains "Unauthorized request")

The inspiration for the plugin is from ExtendedMacro plugin: [https://github.com/FrUh/ExtendedMacro](https://github.com/FrUh/ExtendedMacro "https://github.com/FrUh/ExtendedMacro")

## Blogs

1. [Authentication Token Obtain and Replace (ATOR)](https://medium.com/%40kashwathkumar/authentication-token-obtain-and-replace-ator-burp-plugin-fast-and-reliable-plugin-to-handle-b19e3621c6a7 "Authentication Token Obtain and Replace (ATOR)")[Burp Plugin](https://www.kitploit.com/search/label/Burp%20Plugin "Burp Plugin") - Part1 - Single step login sequence and single token extraction
2. [Authentication Token Obtain and Replace (ATOR) Burp Plugin - Part2 - Multi step login sequence and multiple extraction](https://medium.com/%40kashwathkumar/authentication-token-obtain-and-replace-ator-burp-plugin-fast-and-reliable-plugin-to-handle-1d9a0b3054e "Authentication Token Obtain and Replace (ATOR) Burp Plugin - Part2 - Multi step login sequence and multiple extraction")

## Getting Started

1. Install Java and Maven
2. Clone the repository
3. Run the "mvn clean install" command in cloned repo of where pom.xml is present
4. Take the generated jar with dependencies from the target folder

### Prerequisites

1. Make sure java environment is setup in your machine.
2. Confgure the [Burp Suite](https://www.kitploit.com/search/label/Burp%20Suite "Burp Suite") to listen the Proxy traffic
3. Configure the java environment from extender tab of BURP

For usage with test application (Install this testing application (Tiredful application) from [https://github.com/payatu/Tiredful-API](https://github.com/payatu/Tiredful-API "https://github.com/payatu/Tiredful-API"))

### Steps

1. Identify the request which provides the error
2. Identify the Error Pattern (details in section below)
3. Obtain the data from the response using regex (see sample regex values)
4. Replace this data on the request (use same regex as step 3 along with the variable name)

### Error Pattern:

Totally there are 4 different ways you can specify the error condition.

1. Status Code: 401, 400
2. Error in Body: give any text from the body content (Example: Access token expired)
3. Error in Header: give any text from header(Example: Unauthorized)
4. Free Form: use this to give multiple condition (st=400 && bd=Access token expired || hd=Unauthorized)

### Regex with samples

1. Use Authorization: Bearer \w\* to match Authorization: Bearer AXXFFPPNSUSSUSSNSUSN
2. Use Authorization: Bearer ([\w+\_-.]\*) to match Authorization: Bearer AXX-F+FPPNS.USSUSSNSUSN

### Break down into end to end tests

1. Finding the Invalid request:
   * http://HOST:PORT/api/v1/exams/MQ==/ with invalid Bearer token.
2. Identifying Error Pattern:
   * The above request will give you 401, here error condition is Status Code = 401
3. Match regex with request data
   * Authorization: Bearer \w\* - this regex will match [access token](https://www.kitploit.com/search/label/Access%20Token "access token") which is passed.
4. Replacement - How to replace
   * Replace the matched text(step 3 regex) with extracted value (Extraction configuration discussed in below, say varibale name is "token")
   * Authorization: Bearer token - extracted token will be replaced.

### Usage with test application

Idea : Record the Tiredful application request in BURP, configure the ATOR extender, check whether token is replaced by ATOR.

1. Open the testing application in browser which you configured with BURP
   * Generate a token from http://HOST:PORT/handle-user-token/
   * Send the request http://HOST:PORT/api/v1/exams/MQ==/ by passing [Authorization](https://www.kitploit.com/search/label/Authorization "Authorization") Beaer token(get it from above step)
2. Add the ATOR jar file as a extender in BURP
3. Right Click on the request(/handle-user-token) in Proxy history and send it to [Authentication](https://www.kitploit.com/search/label/Authentication "Authentication") Token Optain and Replace Extender
4. Add the new entry in Extraction configuration by selecting the "access\_token" value and give name as "token"(it may be any name) Note: For this application,one request is enough to generate a token.Token can also get generated after multiple requests
5. TRIGGER CONDITION:
   * Macro steps will get executed if the condition is matched.
   * After execution of steps, replace the incoming request by taking values from "Pattern" and "Replacement Area" if specified.
   * For our testing,
     + Error condition is 401(Status Code)
     + Pattern is "Authorization: Bearer \w\*" (Specify the regex Pattern how you want to replace with extraction values)
     + Replacement Area is "Authentication: Bearer <NAME which you gave in STEP 4>"
   * Click on "Add" Button.
6. For this example, one replacement is enough to make the incoming request as valid but you can add mutiple replacement for a single condition.
7. Hit the invalid request from Repeater and check the req/res flows in either FLOW/Logger++
   * Invalid Bearer token(http://HOST:PORT/api/v1/exams/MQ==/) from Repeater makes the response as 401.
   * Extender will match this condition and start running the recorded steps, extract the "access\_token"
   * Replace the access token(from step ii) in actual response(from Repeater) and makes this invalid request as valid.
   * In the repeater console, you see 200 OK response.
8. Do the Step7 again and check the flow
   * This time extender will not invoke the steps because existing token is valid and so it uses that.

## Built With

* [SWING](https://javadoc.scijava.org/Java7/javax/swing/package-summary.html "SWING") - Used to add panel

## Contributing

Please read [CONTRIBUTING.md](https://gist.github.com/PurpleBooth/b24679402957c63ec426 "CONTRIBUTING.md") for details on our code of conduct, and the process for submitting pull requests to us.

## Versioning

v1.0

## Authors

* \*\*[https://github.com/FrUh/ExtendedMacro](https://g...