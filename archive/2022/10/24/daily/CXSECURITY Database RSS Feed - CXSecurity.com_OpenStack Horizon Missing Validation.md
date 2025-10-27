---
title: OpenStack Horizon Missing Validation
url: https://cxsecurity.com/issue/WLB-2022100061
source: CXSECURITY Database RSS Feed - CXSecurity.com
date: 2022-10-24
fetch_date: 2025-10-03T20:42:43.587006
---

# OpenStack Horizon Missing Validation

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
|  |  | |  | | --- | | **OpenStack Horizon Missing Validation** **2022.10.23**  Credit:  **[Sven Anders](https://cxsecurity.com/author/Sven%2BAnders/1/)**  Risk: **Medium**  Local: **No**  Remote: ****Yes****  CVE: **N/A**  CWE: **N/A** | |

Hi,
we opened a bug at OpenStack, 3 month ago, but nobody takes care about it. Due
to the OpenStack guidlines the bug report is now public readable.
https://bugs.launchpad.net/horizon/+bug/1980349
I am not a security expert and do not know how bad this bug is, there is now
CVE and so on. Please be kind.
# Description of the bug
We use OpenStack horizon in the following version: `git+https://opendev.org/
openstack/horizon@9d1bb3626bc1dbcf29a55aeb094f4350067317cd#egg=horizon`
In Horizon there is the following code in Xena:
openstack\_auth/views.py
```
def websso(request):
"""Logs a user in using a token from Keystone's POST."""
referer = request.META.get('HTTP\_REFERER',
settings.OPENSTACK\_KEYSTONE\_URL)
auth\_url = utils.clean\_up\_auth\_url(referer)
token = request.POST.get('token')
try:
request.user = auth.authenticate(request, auth\_url=auth\_url,
token=token)
...
```
This call is usually called during SAML-Auth, but you can call it on the
command line like this:
``
curl -v 'http://horizon-name:8080/auth/websso/' -X POST -H 'Referer: https://
referer:5001/' -H 'Content-Type: application/x-www-form-urlencoded' --data-raw
'token=mytoken'
``
The token is not checked.
So an attacker can control the content of the HTTP\_REFERER and then an auth
POST request will be sent to this address.
I have changed the referer to a web server https://webserver/su-huhu/ and you
can find inside the logfile:
```
access.log: <ip-address-of-horizon> - - [28/Jun/2022:08:15:06 +0200] "POST /
su-huhu/v3/auth/tokens HTTP/1.1" 404 6529 "-" "openstack\_auth
keystoneauth1/4.5.0 python-requests/2.27.1 CPython/3.8.10"
```
# Impact
\* An attacker can hide his ip and do a brute force attack to any other ip via
all public available horizon dashboards.
\* An attacker can setup a machine, set the referer to this machine and then
send some ugly results (e.g. very long, never ending, wrong json code, ssl
protocol issues) to the horizon service.
\* An attacker can analyze which services are available on the horizon host (if
it is behind a firewall, use DNS Servers with private zones). Note that you are
able to change the port number to any number. I have not tested, but perhaps
it is also possible to change the protocol to another value, let's say:
imap://user:passwort@ip/.
# Is this only relevant for xena
The code has changed on master branch, but the bug is still there:
```
# TODO(stephenfin): Migrate to CBV
@sensitive\_post\_parameters()
@csrf\_exempt
@never\_cache
def websso(request):
"""Logs a user in using a token from Keystone's POST."""
if settings.WEBSSO\_USE\_HTTP\_REFERER:
referer = request.META.get('HTTP\_REFERER',
settings.OPENSTACK\_KEYSTONE\_URL)
auth\_url = utils.clean\_up\_auth\_url(referer)
else:
auth\_url = settings.OPENSTACK\_KEYSTONE\_URL
token = request.POST.get('token')
try:
request.user = auth.authenticate(request, auth\_url=auth\_url,
token=token)
except exceptions.KeystoneAuthException as exc:
if settings.WEBSSO\_DEFAULT\_REDIRECT:
res = django\_http.HttpResponseRedirect(settings.LOGIN\_ERROR)
else:
msg = 'Login failed: %s' % exc
res = django\_http.HttpResponseRedirect(settings.LOGIN\_URL)
set\_logout\_reason(res, msg)
return res
```
only changing the WEBSSO\_USE\_HTTP\_REFERER to false (Default true) will forbid
to call this.

[**See this note in RAW Version**](https://cxsecurity.com/ascii/WLB-2022100061)

[Tweet](https://twitter.com/share)

Vote for this issue:
 0
 0

50%

50%

#### **Thanks for you vote!**

#### **Thanks for you comment!** Your message is in quarantine 48 hours.

Comment it here.

Nick (\*)

Email (\*)

Video

Text (\*)

(\*) - required fields.
Cancel
Submit

|  |  |
| --- | --- |
|  | **{{ x.nick }}** ![]() | Date: {{ x.ux \* 1000 | date:'yyyy-MM-dd' }} *{{ x.ux \* 1000 | date:'HH:mm' }}* CET+1  ---   {{ x.comment }} |

Show all comments

---

Copyright **2025**, cxsecurity.com

|  |

Back to Top