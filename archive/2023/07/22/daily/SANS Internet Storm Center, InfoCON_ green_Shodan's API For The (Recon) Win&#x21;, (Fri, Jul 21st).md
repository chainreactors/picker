---
title: Shodan's API For The (Recon) Win&#x21;, (Fri, Jul 21st)
url: https://isc.sans.edu/diary/rss/30050
source: SANS Internet Storm Center, InfoCON: green
date: 2023-07-22
fetch_date: 2025-10-04T11:56:34.569912
---

# Shodan's API For The (Recon) Win&#x21;, (Fri, Jul 21st)

# [Internet Storm Center](/)

[Sign In](/login.html)
[Sign Up](/register.html)

Handler on Duty: [Johannes Ullrich](/handler_list.html#johannes-ullrich "Johannes Ullrich")

Threat Level: [green](/infocon.html)

* [previous](/diary/30048)
* [next](/diary/30054)

# [Shodan's API For The (Recon) Win!](/forums/diary/Shodans%2BAPI%2BFor%2BThe%2BRecon%2BWin/30050/)

**Published**: 2023-07-21. **Last Updated**: 2023-07-21 01:18:10 UTC
**by** [Rob VandenBrink](/handler_list.html#rob-vandenbrink) (Version: 2)

[0 comment(s)](/diary/Shodans%2BAPI%2BFor%2BThe%2BRecon%2BWin/30050/#comments)

Ever been on a call with a client, and had that "I need a full set of nmap results for that host in 5 seconds" moment?  Like when you're trying to scope out the size of a project (maybe a pentest project) and if you \*just\* had the list of open ports you'd have an answer other than "I'll call you back", because nmap will take 10 minutes?

Well Shodan has you covered, but even that takes a login.  Shodan has you even better covered with their API!  First, get your API key, you'll find it in your account page.

You'll find the API documentation here: https://developer.shodan.io/api
But for "recon on the fly", you'll just need a few API calls.  You can do all of these using curl, so they're easy to script

This one will give you info on a target host:
curl -s -k "https://api.shodan.io/shodan/host/<host\_ip>?key=%shodan-api-key%"

Like most jason based APIs, if you want to read the returned data with your eyes (instead of code), running it through jq really helps (stay tuned, more on this on Monday)

Looking at 45.6.103.34 (one of the IP's behind isc.sans.edu), we get a BOATLOAD of information,

curl -s -k "https://api.shodan.io/shodan/host/45.60.103.34?key=%shodan-api-key%"   | jq
{
  "region\_code": "ON",
  "tags": [
    "cdn"
  ],
  "ip": 758933282,
  "area\_code": null,
  "domains": [
    "cio.org",
    "ranges.io",
    "cyberaces.org",
    "sans.co",
    "imperva.com",
    "cyberfoundations.org",
    "securingthehuman.org",
    "sans.org",
    "giac.net",
    "sans.edu",
    "giac.org",
    "cybercenters.org"
  ],
  "hostnames": [
    "cio.org",
    "ranges.io",
    "cyberaces.org",
    "sans.co",
.. and so on

If you run this through "wc -l", you'll find that there are **12353 lines** in the results for this host. That's a lot to plow through!  It includes open ports, services on them, certificates, CVEs that might be in play, everything you'd get in the Shodan web interface.  I tend to run this command through "less", then search for what I need.

If you just want port information for an IP, you can use the same API and grep for it:

.

Running that against the same host give us:
      "port": 25,
      "port": 53,
      "port": 80,
      "port": 81,
      "port": 82,
      "port": 83,
      "port": 84,
      "port": 88,
      "port": 389,
      "port": 443,
      "port": 444,
      "port": 465,
      "port": 554,
      "port": 587,
      "port": 631,
      "port": 636,
      "port": 1024,
      "port": 1177,
      "port": 1234,
      "port": 1337,
      "port": 1400,
      "port": 1433,
 .... for a total of 130 open ports

No surprise there, we are a research site after all ...

How about for the entire DNS zone "sans.org"?
curl -s -k "https://api.shodan.io/dns/domain/%1?key=%shodan-api-key" | jq | less

As with all Shodan data, all the data you get back is historic - that's how you get it so quick.  They scan the internet and when you check a host via the API or website, you are querying their database of saved values, not the host itself.  This means that if it's a faster-moving host, your data might be off a bit here or there, it's from yesterday or maybe last week.  If you look at any particular record, you'll find a timestamp on it so you can see how current it is.

So this type of information is good to point you in the right direction to narrow down a real port scan, to get ballpark values if you are scoping out a project and similar work.  Or if need to query "find me all of port "X" on the internet", this is a great way to get that job done in a few seconds.

Let's look for all the hosts that run ssh on port than 22:

curl -s -k "https://api.shodan.io/shodan/host/search?key=%shodan-api-key%&query=ssh&port:22" | grep \"ip\": | wc -l
  97

Yup, this API also returns larger datasets in chunks, mainly so that you can reasonably digest it.  You can "page" through the data by adding a page number:
curl -s -k "https://api.shodan.io/shodan/host/search?key=%shodan-api-key%&query=ssh&port:22&page=2"
(and so on).
This isn't too practical by hand, the cursor (the pointer that keeps track of where you are in the list) will time out after a short period of inactivity, but it does great in a while loop.

A more typical answer is you generally want to narrow down your searches to a reasonable result set.  Or if you want to search the entire internet and just get counts, there's an API just for that.  Let's look for SSH on port 22:
curl -s -k "https://api.shodan.io/shodan/host/count?key=%shodan-api-key%&query=ssh+port:22" | jq
{
  "matches": [],
  "total": 19033015
}

How about SSH that's on ports OTHER than 22?
curl -s -k "https://api.shodan.io/shodan/host/count?key=%shodan-api-key%&query=ssh+-port:22" | jq
{
  "matches": [],
  "total": 22832793
}

Look for telnet on port 23 and on "not port 23", that'll keep you up at night!

Or, say you were digging into open RDP ports.  Look at our page for that port (https://isc.sans.edu/data/port.html?port=3389), you'd see a down-tick in recent scanning activity for that port.  I wonder how many internet-facing hosts have RDP open on 3389?:
curl -s -k "https://api.shodan.io/shodan/host/count?key=%shodan-api-key%&query=port:3389" | jq
{
  "matches": [],
  "total": 3333166
}

Yikes!!
How about RDP with screenshots?
curl -s -k "https://api.shodan.io/shodan/host/count?key=%shodan-api-key%&query=windows+port:3389+has\_screenshot:true" | jq
{
  "matches": [],
  "total": 635901
}

Webcams with screenshots?  Not as many as I thought, though the count of live webcams with unauthenticated or default-creds video is likely higher
curl -s -k "https://api.shodan.io/shodan/host/count?key=%shodan-api-key%&query=webcam+has\_screenshot:true" | jq
{
  "matches": [],
  "total": 235
}

Looking for a specific vulnerability?  Let's hunt for CVE-2022-43497, one of the FortiOS vulns that can be detected with a non-intrusive scan:
curl -s -k "https://api.shodan.io/shodan/host/count?key=%shodan-api-key%&query=vuln:cve-2022-43497
{"matches": [], "total": 73208}

(note, you can't query for vulns with a base Shodan subscription, you'll need the small business subscription or better for this)

You can also combine any of the above with "default password" as a search term.  And yes, you'll find stuff here too - just looking for a total of non-specific devices with default creds:
curl -s -k "https://api.shodan.io/shodan/host/count?key=%shodan-api-key%&query=default+password" | jq
{
  "matches": [],
  "total": 30956
}
I'm sure that this count is higher, they're only comparing against what their list of default creds is.

You can add to your query using more filters (https://beta.shodan.io/search/filters) and narrow things down further by adding "facets" like country, city or ASN to your query (https://beta.shodan.io/search/facet)

Long story short, this is a way cool way to get a ton of information in just a few seconds, these are some handy scripts to keep ready-to-run in your search path!

Example scripts, along with the other recon scripts I've posted recently can all be found in my github: https://github.com/robvandenbrink/recon\_scripts

If you've got a cool shodan search that you've used, please share in our comment section!

===============
Rob VandenBrink
[[email protected]](/cdn-cgi/l/email-protection)

Keywords: [api](/tag.html?tag=api) [shodan](/tag.html?tag=shodan)

[0 comment(s)](/diary/Shodans%2BAPI%2BFor%2BThe%2BRecon%2BWin/30050/#comments)

* [previous](...