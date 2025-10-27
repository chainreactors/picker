---
title: Finding that one GPO Setting in a Pool of Hundreds of GPOs, (Tue, Jan 17th)
url: https://isc.sans.edu/diary/rss/29442
source: SANS Internet Storm Center, InfoCON: green
date: 2023-01-18
fetch_date: 2025-10-04T04:12:06.239910
---

# Finding that one GPO Setting in a Pool of Hundreds of GPOs, (Tue, Jan 17th)

# [Internet Storm Center](/)

[Sign In](/login.html)
[Sign Up](/register.html)

Handler on Duty: [Johannes Ullrich](/handler_list.html#johannes-ullrich "Johannes Ullrich")

Threat Level: [green](/infocon.html)

* [previous](/diary/29438)
* [next](/diary/29448)

# [Finding that one GPO Setting in a Pool of Hundreds of GPOs](/forums/diary/Finding%2Bthat%2Bone%2BGPO%2BSetting%2Bin%2Ba%2BPool%2Bof%2BHundreds%2Bof%2BGPOs/29442/)

**Published**: 2023-01-17. **Last Updated**: 2023-01-17 04:06:16 UTC
**by** [Rob VandenBrink](/handler_list.html#rob-vandenbrink) (Version: 1)

[2 comment(s)](/diary/Finding%2Bthat%2Bone%2BGPO%2BSetting%2Bin%2Ba%2BPool%2Bof%2BHundreds%2Bof%2BGPOs/29442/#comments)

I had a call recently from a client, they were looking for which Group Policy in their AD had a specific setting in it.

If your organization is like so many, you have dozens or hundreds of Group Policies (GPOs) in your Active Directory.  They'll all be meaningfully named, but as the years go by, and multiple admins get all admin-y on your domain, that definition of "meaningful" will tend to drift.  Also, you'll often find an admin that says "Oh, that GPO covers the same machines or people that I want to make this change to, I'll add this other thing that GPO"

Long story short, the names of your GPOs will not always be meaningful (to you), and will not always reflect what's inside of them.  Or you might have 7-8-9 GPOs that have similar "meaningful names" with very different settings.

Luckily, PowerShell has a way to bail us out of this mess, at least partly.

First, to collect all of your GPOs into one variable, the command:
$GPOs = Get-GPO -All -Domain $DomainName

Next, to dump any one GPO into an XML variable, you can use:
$GPOReport = Get-GPOReport -Guid $gpo.Id -ReportType Xml
(I'm selecting the GPO by GUID in this case)

From there, you can just look for any ASCII string in that XML unicode - any setting or any value.

if ($GPOReport -match $SearchString) {
    write-line TA-DA, FOUND IT!!"
    }

(not that "-match" is case insensitive by default)

Putting this into one code snip that you can use:

# Set the search string
$SearchString = "Removable"

# init variables
$matchlist = @()

# Get the domain name
$DomainName = $env:USERDNSDOMAIN

# this line is not needed for newer DCs
Import-Module grouppolicy
# collect all GPOs
$GPOs = Get-GPO -All -Domain $DomainName

# Hunt through each GPO XML for the search string
foreach ($gpo in $GPOs) {
    $GPOReport = Get-GPOReport -Guid $gpo.Id -ReportType Xml
    if ($GPOReport -match $SearchString) {
        $matchlist += [string]$gpo.DisplayName
        # this line is just to indicate progress - delete if not needed
        write-host "Match:" $gpo.DisplayName -foregroundcolor "Green"
    }
    else {
        # this line is just to indicate progress - delete if not needed
        Write-Host "No match:" $gpo.DisplayName
    }
}

# output results (likely you want to keep this line)
write-host 'String "'$SearchString'" Found in:' -foregroundcolor "Green"
write-host $matchlist -separator "`n" -foregroundcolor "Green"

Once you know which policy or policies your search has narrowed down to, you can just look at the XML files to find the setting, or dump the GPOReport to HTML instead, or heck, just look at the GPO.

My client?  They where looking for the GPO that blocked and permitted USB disk access, so our search string was looking for "**Removable** Storage" settings.  Was it in the "USB DRIVES" Group Policy? - nope, that would make too much sense (and was the first place they looked).  We ended up finding it in their "Win10 Baseline" policy.  If you are curious, those Removable Storage GPO settings are in both User Configuration and Computer Configuration / Policies / Administrative Templates / System / **Removable** Storage Access

I will likely refine this to also include the individual settings found in some future version, so keep your eyes peeled.  But this first version of the script did the job for me - it narrowed down literally about a hundred GPOs down to just 3 that I had to look at (1 was the correct one, and the other two were actually incorrectly set and had to be fixed)

===============
Rob VandenBrink
[[email protected]](/cdn-cgi/l/email-protection)

Keywords: [gpo](/tag.html?tag=gpo) [powershell](/tag.html?tag=powershell)

[2 comment(s)](/diary/Finding%2Bthat%2Bone%2BGPO%2BSetting%2Bin%2Ba%2BPool%2Bof%2BHundreds%2Bof%2BGPOs/29442/#comments)

* [previous](/diary/29438)
* [next](/diary/29448)

### Comments

Using powershell seems a lot more difficult than using gpresult, at least when it comes to finding what is breaking a specific set of computers. With gpresult I can export all of the applied group policies to a file and easily search that file, either on this computer or a remote computer, and it's native. Sure, this wont search every group policy in the domain but usually this whole process starts because something is broken on a computer. This powershell script could be a neat tool for domain cleanup though. I've used the Microsoft PolicyAnalyzer tool a lot for this in the past. What I really wish is that Microsoft had better logging such that I could put a computer in a debug mode of sorts and see when a policy blocks something for those times when I don't even know what to search for.

#### Sam

#### Jan 17th 2023 2 years ago

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
  + [About Us](/about.html)
  + [Handlers](/handler_list.html)* [About Us](/about.html)

[Slack Channel](/slack/index.html)

[Mastodon](https://infosec.exchange/%40sans_isc)

[Bluesky](https://bsky.app/profile/sansisc.bsky.social)

[X](https://twitter.com/sans_isc)

![](/adimg.html?id=)

© 2025 SANS™ Internet Storm Center
Developers: We have an [API](/api/) for you!   [![Creative Commons License](/images/cc.png)](https://creativecommons.org/licenses/by-nc-sa/4.0/)

* [Link To Us](/linkback.html)
* [About Us](/about.html)
* [Handlers](/handler_list.html)
* [Privacy Policy](/privacy.html)