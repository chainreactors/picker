---
title: OpenStack Horizon,	it is posible to trigger a POST Request to any address
url: https://seclists.org/fulldisclosure/2022/Oct/13
source: Full Disclosure
date: 2022-10-22
fetch_date: 2025-10-03T20:39:53.579552
---

# OpenStack Horizon,	it is posible to trigger a POST Request to any address

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

[![Previous](/images/left-icon-16x16.png)](12)
[By Date](date.html#13)
[![Next](/images/right-icon-16x16.png)](14)

[![Previous](/images/left-icon-16x16.png)](12)
[By Thread](index.html#13)
[![Next](/images/right-icon-16x16.png)](14)

![](/shared/images/nst-icons.svg#search)

# OpenStack Horizon, it is posible to trigger a POST Request to any address

---

*From*: Sven Anders <fulldisclosure2022@sven.anders.hamburg>
*Date*: Thu, 20 Oct 2022 09:10:11 +0200

---

```
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
openstack_auth/views.py

```
def websso(request):
    """Logs a user in using a token from Keystone's POST."""
    referer = request.META.get('HTTP_REFERER',
settings.OPENSTACK_KEYSTONE_URL)
    auth_url = utils.clean_up_auth_url(referer)
    token = request.POST.get('token')
    try:
        request.user = auth.authenticate(request, auth_url=auth_url,
                                         token=token)
   ...
```

This call is usually called during SAML-Auth, but you can call it on the
command line like this:

``
curl -v 'http://horizon-name:8080/auth/websso/'; -X POST -H 'Referer: https://
referer:5001/' -H 'Content-Type: application/x-www-form-urlencoded' --data-raw
'token=mytoken'
``

The token is not checked.

So an attacker can control the content of the HTTP_REFERER and then an auth
POST request will be sent to this address.

I have changed the referer to a web server https://webserver/su-huhu/ and you
can find inside the logfile:

```
access.log: <ip-address-of-horizon> - - [28/Jun/2022:08:15:06 +0200] "POST /
su-huhu/v3/auth/tokens HTTP/1.1" 404 6529 "-" "openstack_auth
keystoneauth1/4.5.0 python-requests/2.27.1 CPython/3.8.10"
```

# Impact

* An attacker can hide his ip and do a brute force attack to any other ip via
all public available horizon dashboards.
* An attacker can setup a machine, set the referer to this machine and then
send some ugly results (e.g. very long, never ending, wrong json code, ssl
protocol issues) to the horizon service.
* An attacker can analyze which services are available on the horizon host (if
it is behind a firewall, use DNS Servers with private zones). Note that you are
able to change the port number to any number. I have not tested, but perhaps
it is also possible to change the protocol to another value, let's say:
imap://user:passwort@ip/.

# Is this only relevant for xena

The code has changed on master branch, but the bug is still there:
```
# TODO(stephenfin): Migrate to CBV
@sensitive_post_parameters()
@csrf_exempt
@never_cache
def websso(request):
    """Logs a user in using a token from Keystone's POST."""
    if settings.WEBSSO_USE_HTTP_REFERER:
        referer = request.META.get('HTTP_REFERER',
                                   settings.OPENSTACK_KEYSTONE_URL)
        auth_url = utils.clean_up_auth_url(referer)
    else:
        auth_url = settings.OPENSTACK_KEYSTONE_URL
    token = request.POST.get('token')
    try:
        request.user = auth.authenticate(request, auth_url=auth_url,
                                         token=token)
    except exceptions.KeystoneAuthException as exc:
        if settings.WEBSSO_DEFAULT_REDIRECT:
            res = django_http.HttpResponseRedirect(settings.LOGIN_ERROR)
        else:
            msg = 'Login failed: %s' % exc
            res = django_http.HttpResponseRedirect(settings.LOGIN_URL)
            set_logout_reason(res, msg)
        return res
```

only changing the WEBSSO_USE_HTTP_REFERER to false (Default true) will forbid
to call this.

_______________________________________________
Sent through the Full Disclosure mailing list
https://nmap.org/mailman/listinfo/fulldisclosure
Web Archives & RSS: https://seclists.org/fulldisclosure/
```

---

[![Previous](/images/left-icon-16x16.png)](12)
[By Date](date.html#13)
[![Next](/images/right-icon-16x16.png)](14)

[![Previous](/images/left-icon-16x16.png)](12)
[By Thread](index.html#13)
[![Next](/images/right-icon-16x16.png)](14)

### Current thread:

* **OpenStack Horizon, it is posible to trigger a POST Request to any address** *Sven Anders (Oct 20)*

![](/shared/images/nst-icons.svg#search)

## [Nmap Security Scanner](https://nmap.org/)

* [Ref Guide](https://nmap.org/book/man.html)* [Install Guide](https://nmap.org/book/install.html)* [Docs](https://nmap.org/docs.html)* [Download](https://nmap.org/download.html)* [Nmap OEM](https://nmap.org/oem/)

## [Npcap packet capture](https://npcap.com/)

* [User's Guide](https://npcap.com/guide/)* [API docs](https://npcap.com/guide/npcap-devguide.html#npcap-api)* [Download](https://npcap.com/#download)* [Npcap OEM](https://npcap.com/oem/)

## [Security Lists](https://seclists.org/)

* [Nmap Announce](https://seclists.org/nmap-announce/)* [Nmap Dev](https://seclists.org/nmap-dev/)* [Full Disclosure](https://seclists.org/fulldisclosure/)* [Open Source Security](https://seclists.org/oss-sec/)* [BreachExchange](https://seclists.org/dataloss/)

## [Security Tools](https://sectools.org)

* [Vuln scanners](https://sectools.org/tag/vuln-scanners/)* [Password audit](https://sectools.org/tag/pass-audit/)* [Web scanners](https://sectools.org/tag/web-scanners/)* [Wireless](https://sectools.org/tag/wireless/)* [Exploitation](https://sectools.org/tag/sploits/)

## [About](https://insecure.org/)

* [About/Contact](https://insecure.org/fyodor/)* [Privacy](https://insecure.org/privacy.html)* [Advertising](https://insecure.org/advertising.html)* [Nmap Public Source License](https://nmap.org/npsl/)

[![](/shared/images/nst-icons.svg#twitter)](https://twitter.com/nmap "Visit us on Twitter")
[![](/shared/images/nst-icons.svg#facebook)](https://facebook.com/nmap "Visit us on Facebook")
[![](/shared/images/nst-icons.svg#github)](https://github.com/nmap/ "Visit us on Github")
[![](/shared/images/nst-icons.svg#reddit)](https://reddit.com/r/nmap/ "Discuss Nmap on Reddit")