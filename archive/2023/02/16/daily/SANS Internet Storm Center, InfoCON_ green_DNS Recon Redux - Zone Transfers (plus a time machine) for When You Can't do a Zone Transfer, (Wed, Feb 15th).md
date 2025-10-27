---
title: DNS Recon Redux - Zone Transfers (plus a time machine) for When You Can't do a Zone Transfer, (Wed, Feb 15th)
url: https://isc.sans.edu/diary/rss/29552
source: SANS Internet Storm Center, InfoCON: green
date: 2023-02-16
fetch_date: 2025-10-04T06:48:39.885116
---

# DNS Recon Redux - Zone Transfers (plus a time machine) for When You Can't do a Zone Transfer, (Wed, Feb 15th)

# [Internet Storm Center](/)

[Sign In](/login.html)
[Sign Up](/register.html)

Handler on Duty: [Johannes Ullrich](/handler_list.html#johannes-ullrich "Johannes Ullrich")

Threat Level: [green](/infocon.html)

* [previous](/diary/29548)
* [next](/diary/29556)

# [DNS Recon Redux - Zone Transfers (plus a time machine) for When You Can't do a Zone Transfer](/forums/diary/DNS%2BRecon%2BRedux%2BZone%2BTransfers%2Bplus%2Ba%2Btime%2Bmachine%2Bfor%2BWhen%2BYou%2BCant%2Bdo%2Ba%2BZone%2BTransfer/29552/)

**Published**: 2023-02-15. **Last Updated**: 2023-02-15 14:53:49 UTC
**by** [Rob VandenBrink](/handler_list.html#rob-vandenbrink) (Version: 1)

[0 comment(s)](/diary/DNS%2BRecon%2BRedux%2BZone%2BTransfers%2Bplus%2Ba%2Btime%2Bmachine%2Bfor%2BWhen%2BYou%2BCant%2Bdo%2Ba%2BZone%2BTransfer/29552/#comments)

When in the recon phase of a security assessment or penetration test, quite often you want to collect the dns names for all hosts in a scope of IP addresses.  I covered how to do that with a few different APIs in this story: ([https://isc.sans.edu/diary/Using+Passive+DNS+sources+for+Reconnaissance+and+Enumeration/28596](https://isc.sans.edu/diary/Using%2BPassive%2BDNS%2Bsources%2Bfor%2BReconnaissance%2Band%2BEnumeration/28596))

On the flip-side, quite often you want to collect DNS records of all hosts in a domain.  With more folks using wildcard certificates these days, certificate transparency isn't always the goldmine that it used to be for that ([https://isc.sans.edu/diary/Using+Certificate+Transparency+as+an+Attack+Defense+Tool/24114](https://isc.sans.edu/diary/Using%2BCertificate%2BTransparency%2Bas%2Ban%2BAttack%2BDefense%2BTool/24114))

What to do?  The various OSINT repositories (and commercial intelligence repos) have an answer for you.

For DNS Dumpster, this will list what you seek:
curl -k "https://api.hackertarget.com/hostsearch/?q=sans.edu"
isc.sans.edu,45.60.31.34
www.sans.edu,45.60.31.34

Note that DNS Dumpster limits you on requests-per-day, you'll need an API key if you want more queries.  They also have a nice web front-end if you're not feeling particulary code-y that day .. <https://hackertarget.com/ip-tools/>

That seems like a short list to me though, let's look at Cisco Umbrella, which uses OpenDNS as it's back-end database - note that this function has been there a while in the web UI, but is fairly new to the API:

curl -s -k "https://investigate.umbrella.com/subdomains/sans.edu" -H "Authorization: Bearer <APIKEY>" -H "Content-Type: application/json"  | jq
[
  {
    "securityCategories": [],
    "firstSeen": "1627675727",
    "name": "\_dmarc.sans.edu"
  },
  {
    "securityCategories": [],
    "firstSeen": "1627675727",
    "name": "\_domainkey.sans.edu"
  },
..... and so on

Umbrella also has a web front-end (login required) - <https://dashboard.umbrella.com/o/7966391/#/investigate>

Back to the code - getting a count:

curl -s -k "https://investigate.umbrella.com/subdomains/sans.edu" -H "Authorization: Bearer <APIKEY>" -H "Content-Type: application/json"  | jq | grep name | wc -l
     20

This is because this API returns values 20 at a time, you use the last value returned as an offset to get the next batch.
What's that, you say?  Sounds like a script?  Great idea you!

Looking one step ahead, after this list is created, we want to collect all of them that are still valid A records, so that we have a list of target hosts to dig deeper in to.

So along the way, let's take all the records that are found and divvy them up into 3 lists:
**$validARecords** - this is mostly what we're looking for - valid DNS A records for hosts in the domain, which we can use for targets
**$validotherrecords** - these are other DNS records (MX, NS, SOA, TXT etc).  Useful, but not usually direct (in scope) targets
**$notvalidrecords** - these are dns records that no longer resolve, these records did exist at one time but have since been removed

This API call also returns a "first seen" date in Unix Epoch time (seconds since 1 Jan, 1970) - since we're coding, let's convert that to readable text along the way, it might be useful in subsequent phases of your gig.

Putting this all into code:

$apikey = "YOUR API KEY GOES HERE"

$headers = @{
'Authorization'="Bearer "+$apikey
}

$domain = "sans.edu"

$validArecords = @()
$validOtherRecords =@()
$notvalidrecords = @()
$dnsrecords =@()

# set the countval to 20 so that the loop will start
$loopcount = 0
$countval = 20

while($countval -ge 20) {
    if ($loopcount -gt 0) {
        # if this is not the first loop through, get the offset and apply it
        $offsetname = ($dnsrecords | select-object -last 1).name
        $callstring = "https://investigate.umbrella.com/subdomains/" + $domain + "?offsetName="+$offsetname
        } else {
        $callstring = "https://investigate.umbrella.com/subdomains/" + $domain
        }

    $retvals = invoke-webrequest -Method 'Get' -uri $callstring -headers $headers -ContentType "application/json"
    $records = ($retvals.content | convertfrom-json) | select firstseen, name
    $countval = $records.count
    $dnsrecords += $records
    write-host "Count is " $dnsrecords.count
    $loopcount += 1
    }

# Convert all the "first seen" dates from Unix Epoch to Strings
# also test each records and assign each to the correct list

foreach ($val in $dnsrecords) {
  # First, fix the "first seen" date
  $date2 = (Get-Date 01.01.1970).AddSeconds($val.firstseen)
  $val.firstseen = ($date2).ToString("yyyy-MM-dd")
  #next, separate out the current A records and expired A records
     if($record = resolve-dnsname -name $val.name -type a -ErrorAction SilentlyContinue) {
        # record is valid - add the ip and update thev valid list
        # check for other record types (SOA, NS, MX etc)
        if($record.type -ne "A") {
              $validotherrecords += $record
            } else {
            # these are the target valid A records
            $tempval = $val
            $tempval | add-member -membertype noteproperty -name ipaddress -value $record.ipaddress
            $validArecords += $tempval
            }
    } else {
        # record is not valid, update the list of invalid records
        $notvalidrecords += $val
    }
}

So, what's in the final lists:

These list of course are the primary targets - straight up A records (in your customer's domain of course):

**$validarecords**

firstSeen  name                     ipaddress
---------  ----                     ---------
2021-01-25 email.sans.edu           136.147.129.27
2022-09-28 localhost.email.sans.edu 127.0.0.1
2017-03-13 isc.sans.edu             {45.60.31.34, 45.60.103.34}
2014-08-03 www.sans.edu             45.60.31.34

These are also valid records and are of potential use, the CNAME records in particular will be of interest (for instance for multiple websites on the same host):

**$validotherrecords | select name,querytype**

Name                                                      QueryType
----                                                      ---------
sans.edu                                                        SOA
sans.edu                                                        SOA
autodiscover.alumni.sans.edu                                  CNAME
autodiscover.outlook.com                                      CNAME
autod.ha-autod.office.com                                     CNAME

.. and so on

Finally, the invalid list - you'll find that these are records that are of historic interest, and have been removed.  Don't discount them though, that doesn't mean that the hosts are gone, just the DNS records - - these are all still worth checking!  (see what I meant about a DNS Time Machine?)

**$notvalidrecords**

firstSeen  name
---------  ----
2021-07-30 \_dmarc.sans.edu
2021-07-30 \_domainkey.sans.edu
2020-09-15 eiqu3eingae1ha9ja4phepaivahqu9xo.\_domainkey.sans.edu
2020-11-01 isc.\_domainkey.sans.edu

.. and so on

As always, as this script evolves I'll maintain it on my github: https://github.com/robvande...