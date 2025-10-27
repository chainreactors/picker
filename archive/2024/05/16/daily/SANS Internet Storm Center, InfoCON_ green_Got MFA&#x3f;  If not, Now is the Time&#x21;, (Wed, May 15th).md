---
title: Got MFA&#x3f;  If not, Now is the Time&#x21;, (Wed, May 15th)
url: https://isc.sans.edu/diary/rss/30926
source: SANS Internet Storm Center, InfoCON: green
date: 2024-05-16
fetch_date: 2025-10-06T17:17:53.218824
---

# Got MFA&#x3f;  If not, Now is the Time&#x21;, (Wed, May 15th)

# [Internet Storm Center](/)

[Sign In](/login.html)
[Sign Up](/register.html)

Handler on Duty: [Johannes Ullrich](/handler_list.html#johannes-ullrich "Johannes Ullrich")

Threat Level: [green](/infocon.html)

* [previous](/diary/30924)
* [next](/diary/30930)

# [Got MFA? If not, Now is the Time!](/forums/diary/Got%2BMFA%2BIf%2Bnot%2BNow%2Bis%2Bthe%2BTime/30926/)

**Published**: 2024-05-15. **Last Updated**: 2024-05-15 12:04:47 UTC
**by** [Rob VandenBrink](/handler_list.html#rob-vandenbrink) (Version: 1)

[4 comment(s)](/diary/Got%2BMFA%2BIf%2Bnot%2BNow%2Bis%2Bthe%2BTime/30926/#comments)

I had an interesting call from a client recently - they had a number of "net use" and "psexec" commands pop up on a domain controller, all called from PSEXEC (thank goodness for a good EDR deployed across the board!!).  The source IP was a VPN session.

Anyway, we almost immediately declared an incident, and the VPN that was in use that had just Userid / Password authentication was the ingress.  We found a US employee with an active VPN session from Europe (the classic "impossible geography session") - so the standard "kill the session, deactivate the account / change the password action" ensued.
Followed by a serious conversation - really your userid/password protected VPN is only as strong as your weakest password.  Any you KNOW that some folks have kept their "Welcome123" password that they got at their last "I forgot my password" helpdesk call.  Also, your userid/password VPN is only as strong as the weakest other site that your folks have used their work credentials for.

Anyway the actions and discussion above was followed by the "who would want to target us?" conversation, so off to the logs we went.

The standard Cisco VPN rejected login syslog message looks like this:

```

Local4.Info     <fw.ip.add.ress>    %ASA-6-113005: AAA user authentication Rejected : reason = AAA failure : server = <rad.ius.server.ip> : user = ***** : user IP = <att.ack.er.ip>
```

So, we started by dumping all the Rejected logins for the day (note that this client has syslog in Windows):

```

type fw.ip.add.ress.txt | find "Rejected" > aaafail.txt
```

Now let's see how many events we have in a day:

```

type aaafail.txt | wc -l
 196500
```

Let's look at a representative timeslice.  We'll look at:

* 5pm-6pm (so the time is 17:xx)
* remove any repeating space characters (tr -s " ")
* field 24 is the souce IP address, extract that with "cut"
* sort | uniq -c  Give me just uniq addresses, with counts, sorted in descending order
* After that, I'm just looking (manually) at the attacking hosts with a 10 count or higher

```

type aaafail.txt | find " 17:" | tr -s " " | cut -d " " -f 24 | sort | uniq -c | sort /r
    670 207.180.247.77
     33 80.94.95.200
     18 45.135.232.63
     15 45.140.17.49
     15 45.140.17.44
     15 45.135.232.98
     14 45.140.17.63
     14 45.140.17.54
     14 45.140.17.47
     14 45.135.232.94
     14 45.135.232.101
     14 45.135.232.100
     14 45.134.26.25
     14 193.143.1.62
     13 91.202.233.3
     13 45.140.17.41
     13 45.135.232.89
     13 45.135.232.26
     13 45.134.26.6
     10 31.41.244.44
```

The first thing we notice is that the first IP stands out, so let's block that.
Now we'll look at those IP's a bit closer using ipinfo, see my story on this utility here: [https://isc.sans.edu/diary/Using+Passive+DNS+sources+for+Reconnaissance+and+Enumeration/28596](https://isc.sans.edu/diary/Using%2BPassive%2BDNS%2Bsources%2Bfor%2BReconnaissance%2Band%2BEnumeration/28596)

```

ipinfo  207.180.247.77
IPINFO OUTPUT
{
  "ip": "207.180.247.77",
  "hostname": "cp.srv.plusdatacenter.com",
  "city": "Frankfurt am Main",
  "region": "Hesse",
  "country": "DE",
  "loc": "50.1155,8.6842",
  "org": "AS51167 Contabo GmbH",
  "postal": "60306",
  "timezone": "Europe/Berlin"
}
```

Next we note that these "top 20" hosts generate 953 requests out of the for the hour, so this really does look like 1 outlier, plus ~19-20 hosts in a managed cluster.

OK, let's look at those other two subnets that are over-represented in this top 20 list:

```

ipinfo 45.140.0.0
IPINFO OUTPUT
{
  "ip": "45.140.0.0",
  "city": "Sandnes",
  "region": "Rogaland",
  "country": "NO",
  "loc": "58.8524,5.7352",
  "org": "AS201454 UPHEADS AS",
  "postal": "4301",
  "timezone": "Europe/Oslo"
}

ipinfo 45.135.0.0
IPINFO OUTPUT
{
  "ip": "45.135.0.0",
  "city": "Kyiv",
  "region": "Kyiv City",
  "country": "UA",
  "loc": "50.4547,30.5238",
  "org": "AS208467 MagicService LLC",
  "postal": "03027",
  "timezone": "Europe/Kyiv"
}
```

Note that we're 3 searches in and we still haven't found of the traditional "boogeyman".  No Russia, no DPRK, no Iran (yet).

So, keeping in mind that we're just playing with part of the attack, I started blocking subnets, ASN's, and countries.

We blocked the subnets above, and the attack shifted within seconds to ramp up from a Cloud Service Provider in Germany.  We blocked their address space, and it shifted to a CSP in France.  Two more CSP's later, and we finally cut the "top 20" volumes down, and our high volume hosts were down to 5 hosts in Russia.
Blocking Russia shifted the attack to India, then South America.

You see the patterns here, and have hopefully drawn the same conclusions.

The attackers have pre-built "malicious assets" wherever they can spin up legitimate free or low cost cloud hosts.  The attacker is not attacking from their own IP space or even thier own country.  The entire thing is automated, over the course of that day we saw malicious attacks from roughly 1100 IP addresses as we blocked various subnets and ASNs for various (mostly legitimate) cloud providers.

Looking at the other half of the equation, this attacker in particular was using account names that were not related to the organization being attacked - the userid's being used were a mix of all formats plus favourites such as admin, administrator and root.  So it looks like they were using a combination of standard password dumps as input.  I'd have been more concerned - and wouldn't have played around so much - if the attacker had harvested user account info from LinkedIn and similar sources.  If the credential stuffing attack contains mostly legitimate people names, the chances of success are WAY higher - they're most likely combining legit names with password dump data that matches those names.  Normally we see this sort of thing with red team or more targeted malicious activity, where the per-company costs are a bit higher but because things are targetted, the attack tends to succeed sooner.  In that situation we'd have likely shut down the VPN and implemented MFA offline.  Password dump files such as this are easy to come by, and are generally free - though you can certainly purchase access targeted lists or even purchase access to particular companies from "access as a Service" companies in the "criminal supply chain".  Don't believe folks who use phrases like "the dark web" when describing these (though that does exist too)

Needless to say, we did a crash migration to MFA for their VPN, we had them over within a couple of hours of making the decision.  Since their email was already using MFA, this was free and no fuss at all (thanks Microsoft!) - the MFA prompts were already familiar to the user base.

Lessons learned?

* Nobody is targetting you, they are targetting everyone that hasn't implemented MFA.  Or possibly targetting even the MFA sites, since it's tough to tell either way until you get to the MFA prompt.
* Also from the connection volumes, the attackers were very careful not to lock out accounts.  Each IP address has roughly 15 attempts max in an hour, so that's once every ~4 minutes.
* With just one hit every 4 minutes, just this one example cluster has gobs of capacity to easily scale up to easily target hundreds of other organizations.
* They are targeting VPNs.  None of this "pivot through a website" gymnastics, then "pivot out of the DMZ" heartache, th...