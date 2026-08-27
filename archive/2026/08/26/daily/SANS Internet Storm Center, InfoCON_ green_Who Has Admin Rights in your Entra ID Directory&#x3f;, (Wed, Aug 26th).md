---
title: Who Has Admin Rights in your Entra ID Directory&#x3f;, (Wed, Aug 26th)
url: https://isc.sans.edu/diary/rss/33284
source: SANS Internet Storm Center, InfoCON: green
date: 2026-08-26
fetch_date: 2026-08-27T12:14:18.567763
---

# Who Has Admin Rights in your Entra ID Directory&#x3f;, (Wed, Aug 26th)

# [Internet Storm Center](/)

[Sign In](/login.html)
[Sign Up](/register.html)

Handler on Duty: [Jan Kopriva](/handler_list.html#jan-kopriva "Jan Kopriva")

Threat Level: [green](/infocon.html)

* [previous](/diary/33280)
* [next](/diary/33290)

Click HERE to learn more about classes Rob is teaching for SANS

# [Who Has Admin Rights in your Entra ID Directory?](/forums/diary/Who%2BHas%2BAdmin%2BRights%2Bin%2Byour%2BEntra%2BID%2BDirectory/33284/)

**Published**: 2026-08-26. **Last Updated**: 2026-08-26 15:58:15 UTC
**by** [Rob VandenBrink](/handler_list.html#rob-vandenbrink) (Version: 1)

[0 comment(s)](/diary/Who%2BHas%2BAdmin%2BRights%2Bin%2Byour%2BEntra%2BID%2BDirectory/33284/#comments)

A common thing that folks should "worry" about in Entra (or any platform really) is "who has rights to administer"?  Who can delete or change key things, or modify them in ways that might not be obvious (accidentally or on purpose).  Yes, we trust our people, but if they've moved on to other roles or to other organizations, they change from "our people" to "used to be our people".
Also, it's common to have too many admins.  For instance, entry level support folks might need rights to change passwords, but they likely shouldn't have rights to change your intune policies or be global admins.  The "too many admins" question is a common one that auditors will zero in on.  This is #4 on the CIS Critical Controls v7 as "Control of Admin Privileges".  In version 8 of the list it's now at #6 under "Access Control Management"

Let's dig into your Entra ID Directory, you might find some surprises in your admin list.

# first, as always connect to the directory
Connect-MgGraph -Scopes "Directory.Read.All", "RoleManagement.Read.All"

# Get the list of activated directory roles and the count of members
$roles = Get-MgDirectoryRole
foreach ($role in $roles) {
    $members = Get-MgDirectoryRoleMember -DirectoryRoleId $role.Id
    [PSCustomObject]@{
        RoleName     = $role.DisplayName
        MemberCount  = $members.Count
    }
}

RoleName                                MemberCount
--------                                -----------
Privileged Authentication Administrator           0
Global Administrator                              5
Password Administrator                            1
Application Administrator                         0
Service Support Administrator                     0
Purview Workload Content Writer                   1
User Administrator                                0
SharePoint Administrator                          0
Intune Administrator                              3
Purview Workload Content Administrator            1
Azure AD Joined Device Local Adminis...           1
Helpdesk Administrator                            0
Office Apps Administrator                         2
Directory Readers                                 0
Billing Administrator                             0
Cloud Application Administrator                   0
Directory Synchronization Accounts                1
Directory Writers                                 0
Exchange Administrator                            0
Authentication Administrator                      2
Groups Administrator                              0
Privileged Role Administrator                     0
License Administrator                             0
Conditional Access Administrator                  3
Global Reader                                     1
Device Managers                                   0

So this output is OK for a stranger that is looking for a "how many is too many" sort of output.  But if you are administering this directory, what you really want is the actual list - you want to know who the people in the list are, and compare that to your understanding of the roles that folks have in your organization.  You are not looking for the answer to "does it look about right?", you are looking for the details "is it actually right?".  A (really) common finding is to have "that auditor from 3 years ago" still in the list with a "Global Reader" or even "Global Administrator" role. You may also have management or even PMs that aren't as technical as they once were with admin rights, and the power of a collosal accidental delete (though that can be a regular AD issue as well).  In this case, that "Global Reader" line above is a shiny, flashing beacon saying "LOOK HERE".  Let's list the individual user accounts and what roles they have in Entra:

# init the list to zero
$adminslist = @()

# get the roles
$roles = Get-MgDirectoryRole

# Cycle through each role and get admin list
$adminslist = foreach ($role in $roles) {
    $members = Get-MgDirectoryRoleMember -DirectoryRoleId $role.Id
    foreach($m in $members) {
    $adminuser        = get-mguser -userid $m.id
    $adminusername    = $adminuser.displayname
    $adminuseraccount = $adminuser.userprincipalname
    [PSCustomObject]@{
        RoleName    = $role.DisplayName
        UserAccount = $adminuseraccount
        UserName    = $adminusername
        }
     }
}

$adminslist | out-gridview

![](https://isc.sans.edu/diaryimages/images/adminslist.png)

Like changing passwords or keys (or planting a tree), the best time to do this is in the past, but TODAY is the second-best time to look at who has admin rights to key things like your Entra or AD directories.  Check your list for Entra, let us know in the comments if you found anything unexpected?  ( Anonymized of course)

===============
Rob VandenBrink
[[email protected]](/cdn-cgi/l/email-protection)

Keywords: [admin count](/tag.html?tag=admin count) [entra](/tag.html?tag=entra) [graph](/tag.html?tag=graph) [Powershell](/tag.html?tag=Powershell)

[0 comment(s)](/diary/Who%2BHas%2BAdmin%2BRights%2Bin%2Byour%2BEntra%2BID%2BDirectory/33284/#comments)

Click HERE to learn more about classes Rob is teaching for SANS

* [previous](/diary/33280)
* [next](/diary/33290)

### Comments

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

© 2026 SANS™ Internet Storm Center
Developers: We have an [API](/api/) for you!   [![Creative Commons License](/images/cc.png)](https://creativecommons.org/licenses/by-nc-sa/4.0/)

* [Link To Us](/linkback.html)
* [About Us](/about.html)
* [Handlers](/handler_list.html)
* [Privacy Policy](/privacy.html)