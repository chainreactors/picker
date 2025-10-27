---
title: Upcoming Speaking Engagements
url: https://www.schneier.com/blog/archives/2022/10/upcoming-speaking-engagements-24.html
source: Schneier on Security
date: 2022-10-15
fetch_date: 2025-10-03T20:01:07.554953
---

# Upcoming Speaking Engagements

# [Schneier on Security](https://www.schneier.com/)

Menu

* [Blog](https://www.schneier.com)
* [Newsletter](https://www.schneier.com/crypto-gram/)
* [Books](https://www.schneier.com/books/)
* [Essays](https://www.schneier.com/essays/)
* [News](https://www.schneier.com/news/)
* [Talks](https://www.schneier.com/talks/)
* [Academic](https://www.schneier.com/academic/)
* [About Me](https://www.schneier.com/blog/about/)

### Search

*Powered by [DuckDuckGo](https://duckduckgo.com/)*

Blog

Essays

Whole site

### Subscribe

[![Atom](https://www.schneier.com/wp-content/uploads/2019/10/rss-32px.png)](https://www.schneier.com/feed/atom/)[![Facebook](https://www.schneier.com/wp-content/uploads/2019/10/facebook-32px.png)](https://www.facebook.com/bruce.schneier)[![Twitter](https://www.schneier.com/wp-content/uploads/2019/10/twitter-32px.png)](https://twitter.com/schneierblog)[![Email](https://www.schneier.com/wp-content/uploads/2019/10/email-32px.png)](https://www.schneier.com/crypto-gram)

[Home](https://www.schneier.com)[Blog](https://www.schneier.com/blog/archives/)

## Upcoming Speaking Engagements

This is a current list of where and when I am scheduled to speak:

* I’m speaking at the [World Ethical Data Forum](https://worldethicaldataforum.org/), online, October 26-28, 2022.
* I’m speaking at the 24th [International Information Security Conference](https://www.ismsforum.es//evento/733/xxiv-jornada-internacional-de-seguridad-de-la-informaci-n/) in Madrid, Spain, on November 17, 2022.

The list is maintained on [this page](https://www.schneier.com/events/).

Tags: [Schneier news](https://www.schneier.com/tag/schneier-news/)

[Posted on October 14, 2022 at 12:03 PM](https://www.schneier.com/blog/archives/2022/10/upcoming-speaking-engagements-24.html) •
[6 Comments](https://www.schneier.com/blog/archives/2022/10/upcoming-speaking-engagements-24.html#comments)

### Comments

nossl •
[October 18, 2022 4:07 AM](https://www.schneier.com/blog/archives/2022/10/upcoming-speaking-engagements-24.html/#comment-411239)

no https available for speaking inquiries on <https://www.schneier.com/events/> (Link to Leading Authorities, Inc. )?

SpaceLifeForm •
[October 18, 2022 5:20 PM](https://www.schneier.com/blog/archives/2022/10/upcoming-speaking-engagements-24.html/#comment-411275)

@ nossl, Bruce

You can try

‘https://response.leadingauthorities.com/speaking-availability-bruce-schneier

The site trys to support TLS, but the certificate expired 2022-09-27.

Maybe Bruce knows about this, and maybe informed them of the problem. But, you would think that by now, they would have rolled a new cert.

It is not a good look to ask for PII over plain http.

Also, Bruce, it is not a good look on your part to be talking about security, and be affiliated with this group that can not manage their security. Hit them with a cluebat. And fix the link on the events page to be https anyway.

Sorry if this sounds harsh, but it must be said.

Ted •
[October 18, 2022 6:46 PM](https://www.schneier.com/blog/archives/2022/10/upcoming-speaking-engagements-24.html/#comment-411276)

Feel free to delete this response, but maybe this is a current link?

<https://www.leadingauthorities.com/speakers/bruce-schneier>

I saw Lesley Carhart mention LA recently. They currently list 52 Cyber Security speakers. I think the name Leading Authorities is appropriate.

SpaceLifeForm •
[October 18, 2022 9:33 PM](https://www.schneier.com/blog/archives/2022/10/upcoming-speaking-engagements-24.html/#comment-411282)

@ Ted, Bruce, Clive

That is better.

But, there are still two problems.

Bruce, you need to fix the link on the events page to point to

<https://www.leadingauthorities.com/speakers/bruce-schneier>

as Ted found.

And, you need to get them to auto redirect http to https.

Teach them something about security. Hit them with a cluebat.

<https://response.leadingauthorities.com/speaking-availability-bruce-schneier>

is not the same domain as

<https://www.leadingauthorities.com/speakers/bruce-schneier>

It may appear so on quick glance.

They can be completely different servers.

SpaceLifeForm •
[October 18, 2022 11:07 PM](https://www.schneier.com/blog/archives/2022/10/upcoming-speaking-engagements-24.html/#comment-411284)

@ Bruce, Ted, Clive, nossl

Bruce, seriously, something is not right in Dodge.

This is forward and reverse. Connect the dots.

Note that only the reverse on 142.0.173.14 came back authoritative.

dig <http://www.leadingauthorities.com>

; <> DiG 9.16.33-Debian <> <http://www.leadingauthorities.com>
;; global options: +cmd
;; Got answer:
;; ->>HEADER<<- opcode: QUERY, status: NOERROR, id: 1701
;; flags: qr rd ra; QUERY: 1, ANSWER: 4, AUTHORITY: 0, ADDITIONAL: 1

;; OPT PSEUDOSECTION:
; EDNS: version: 0, flags:; udp: 1232
;; QUESTION SECTION:
;www.leadingauthorities.com. IN A

;; ANSWER SECTION:
<http://www.leadingauthorities.com>. 60 IN A 18.67.39.51
<http://www.leadingauthorities.com>. 60 IN A 18.67.39.11
<http://www.leadingauthorities.com>. 60 IN A 18.67.39.33
<http://www.leadingauthorities.com>. 60 IN A 18.67.39.119

dig response.leadingauthorities.com

; <> DiG 9.16.33-Debian <> response.leadingauthorities.com
;; global options: +cmd
;; Got answer:
;; ->>HEADER<<- opcode: QUERY, status: NOERROR, id: 63353
;; flags: qr rd ra; QUERY: 1, ANSWER: 3, AUTHORITY: 0, ADDITIONAL: 1

;; OPT PSEUDOSECTION:
; EDNS: version: 0, flags:; udp: 1232
;; QUESTION SECTION:
;response.leadingauthorities.com. IN A

;; ANSWER SECTION:
response.leadingauthorities.com. 1581 IN CNAME s2941.hs.eloqua.com.
s2941.hs.eloqua.com. 681 IN CNAME p01e.hs.eloqua.com.
p01e.hs.eloqua.com. 86181 IN A 142.0.173.14

dig -x 18.67.39.11

; <> DiG 9.16.33-Debian <> -x 18.67.39.11
;; global options: +cmd
;; Got answer:
;; ->>HEADER<<- opcode: QUERY, status: NOERROR, id: 63800
;; flags: qr rd ra; QUERY: 1, ANSWER: 1, AUTHORITY: 0, ADDITIONAL: 1

;; OPT PSEUDOSECTION:
; EDNS: version: 0, flags:; udp: 1232
;; QUESTION SECTION:
;11.39.67.18.in-addr.arpa. IN PTR

;; ANSWER SECTION:
11.39.67.18.in-addr.arpa. 82726 IN PTR server-18-67-39-11.yto50.r.cloudfront.net.

dig -x 142.0.173.14

; <> DiG 9.16.33-Debian <> -x 142.0.173.14
;; global options: +cmd
;; Got answer:
;; ->>HEADER<<- opcode: QUERY, status: NXDOMAIN, id: 44441
;; flags: qr rd ra; QUERY: 1, ANSWER: 0, AUTHORITY: 1, ADDITIONAL: 1

;; OPT PSEUDOSECTION:
; EDNS: version: 0, flags:; udp: 1232
;; QUESTION SECTION:
;14.173.0.142.in-addr.arpa. IN PTR

;; AUTHORITY SECTION:
173.0.142.in-addr.arpa. 1795 IN SOA ns1.p04.dynect.net. eloquadomain\_ca\_grp.oracle.com. 2275060381 3600 600 604800 1800

SpaceLifeForm •
[October 18, 2022 11:58 PM](https://www.schneier.com/blog/archives/2022/10/upcoming-speaking-engagements-24.html/#comment-411286)

@ Bruce, Ted, Clive, nossl

I forgot to note that the reverse on 142.0.173.14 while it was authoritative, had no ANSWER section. Whereas, the reverse on 18.67.39.11 had an ANSWER, yet it was not authoritative.

I have seen this for many years now.

Your DNS lookup has non-authoritative ANSWERs all of the time.

Mainly, because most DNS lookups occur over non-encrypted UDP which are easily MITM-ed.

[![Atom Feed](https://www.schneier.com/wp-content/themes/schneier/assets/images/rss.png)
Subscribe to comments on this entry](https://www.schneier.com/blog/archives/2022/10/upcoming-speaking-engagements-24.html/feed/)

## Leave a comment [Cancel reply](/blog/archives/2022/10/upcoming-speaking-engagements-24.html#respond)

[Blog moderation policy](https://www.schneier.com/blog/archives/2024/06/new-blog-moderation-policy.html)

[Login](https://www.schneier.com/wp-login.php?redirect_to=https%3A%2F%2Fwww.schneier.com%2Fblog%2Farchives%2F2022%2F10%2Fupcoming-speaking-engagements-24.html "Login")

Name

Email

URL:

[ ]  Remember personal info?

Fill in the blank: the name of this blog is Schneier on \_\_\_\_\_\_\_\_\_\_\_ (required):

Comments:
![](https://www.schneier.com/wp-content/themes/schneier/assets/images/loader.gif)

**Allowed HTML**
<a href="UR...