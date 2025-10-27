---
title: Finding Gaps in Syslog - How to find when nothing happened, (Wed, Dec 7th)
url: https://isc.sans.edu/diary/rss/29314
source: SANS Internet Storm Center, InfoCON: green
date: 2022-12-09
fetch_date: 2025-10-04T01:02:20.955918
---

# Finding Gaps in Syslog - How to find when nothing happened, (Wed, Dec 7th)

# [Internet Storm Center](/)

[Sign In](/login.html)
[Sign Up](/register.html)

Handler on Duty: [Johannes Ullrich](/handler_list.html#johannes-ullrich "Johannes Ullrich")

Threat Level: [green](/infocon.html)

* [previous](/diary/29304)
* [next](/diary/29316)

# [Finding Gaps in Syslog - How to find when nothing happened](/forums/diary/Finding%2BGaps%2Bin%2BSyslog%2BHow%2Bto%2Bfind%2Bwhen%2Bnothing%2Bhappened/29314/)

**Published**: 2022-12-07. **Last Updated**: 2022-12-08 12:41:43 UTC
**by** [Rob VandenBrink](/handler_list.html#rob-vandenbrink) (Version: 1)

[5 comment(s)](/diary/Finding%2BGaps%2Bin%2BSyslog%2BHow%2Bto%2Bfind%2Bwhen%2Bnothing%2Bhappened/29314/#comments)

I recently got a call from a client, they had an outage that required a firewall reboot, but couldn't give me an exact clock time.  They were looking for anything in the logs just prior to that reboot that might indicate a carrier issue, as they had experienced a few outages like this recently.

This was a Cisco ASA firewall, so we of course had logs - LOTS of logs - 2-3-4GB per day, depending on the day, with dozens or more events per second, so way more than is practical to find that "gap" in the logs that you'll see from a device reboot.   What I needed was to find that gap in the logs so that I'd know where to look for problems (right before that).  So how do we find "nothing happens" in a log file?  First, let's look at a typical log entry:

2022-12-07 00:00:00       Local7.Info    172.16.200.1    Dec 07 2022 00:00:00: %ASA-6-302020: Built ....

So you can see, we have a date/time stamp (from the syslog server), the syslog facility, source IP, a date/time stamp (from the device), the message code (ie the Cisco assigned identifier for this message type), then the message itself in text.  The first date / time stamp are separated by a space, then a tab between that and the facility, and another tab between the facility and the souce IP address.  From there on everything is delimited by spaces.

Since I'm looking for a gap in the timestamps, I can just use that first field, so this gets easy!  Let's use the "cut" command to parse out unique seconds and unique minutes

cat 172.016.200.001-2022-12-07.txt | cut -f 1 | sort | uniq > seconds.txt

if your syslog is on windows then you'll likely use "type" instead of "cat".   For a firewall this is too much information though, you'll usually have multiple events per second so looking for a gap will give you white-line-fever in no time.  Lets leave off the seconds field  and look for unique minutes instead:

cat 172.016.200.001-2022-12-07.txt | cut -f 1 | cut -d ":" -f 1,2 | sort | uniq > minutes.txt

Note the two different uses of cat - the first one pulls the first field (delimited by a tab), which is the date+time.  The second one uses the colon for a delimiter, so the first field is the date+hour, the second field is the minutes.

Since the first timestamp is followed by a tab, we don't need to tell the first cut command what delimiter to use.  Log records should all be sequential, especially since we're parsing the timestamp from the syslog server,but I put a "sort" in their anyway, just on principle ("sort | uniq" is a string that should be stored in your fingers).

Since it was ~11am at the time, I took the "minutes.txt" file, opened it in notepad, went to the bottom and scrolled up a few, and found a gap almost right away of just over 1 hour, from 8:37 to 9:37.

![](https://isc.sans.edu/diaryimages/images/gap%20found.png)

If the log was across a longer time period I might have dumped it into Excel and looked for non-sequential records with some cell math.  Or you could use a powershell snip like the one below:

First, create a header line and dump it to a file (note the tab characters **`t**).  The header row gets really handy, it makes importing a delimited file way easier, as this will auto-name the fields.  This is also a handy thing to keep, if you are parsing these logs frequently keeping various header files around is a time-saver:

$header = "timestamp`tfacility`tsource\_ip`tmessage"
$header > import.txt

next, shell out to a command prompt and append the syslog file to the header, for later import

cmd
type fw.txt >> import.txt
exit

Now import the file, use the tab ("`t") as the initial delimeter

$syslog = import-csv -Delimiter "`t" -path .\import.txt

Look at a record:

$syslog[5]

timestamp           facility    source\_ip    message
---------           --------    ---------    -------
2022-12-07 00:00:00 Local7.Info 172.16.200.1 Dec 07 2022 00:00:00: %ASA-6-305011: Built dynamic UDP translation from.

Perfect, let's process the file now:

**#Use the year value to verify each record**
$year = 2022

**# let's look for a minimum gap of 3 minutes**
$difference = 3

**# set an initial value to the "previous record" - cast the timestamp string to the "datetime" type**
$previous = [datetime]($syslog[0].timestamp)

foreach ($record in $syslog.timestamp) {
 **# only process properly formed records (that start with YYYY) - records that wrap with CRLF will error out so discard them here**
   if($record.substring(0,4) -eq $year) {
       $current = [datetime]($record)
     **# totalminutes will convert days, hours, minutes etc difference to just minutes**
       $gap = ($current - $previous).totalminutes
       if ($gap -ge $difference) {
           write-host $gap "minute gap Identified between" $previous and $current
           $p = $previous
           $c = $current
       }
       $previous = $current
    }
}

When we run this, we get one line of output:

**70.05 minute gap Identified between 12/7/2022 8:27:25 AM and 12/7/2022 9:37:28 AM**

Perfect, just what I was looking for!

Since they power cycled this box during the problem, I was looking for a ~4 minute gap (a typical boot time of an ASA firewall), then I was going to look at events immediately before that gap.  But what I saw instead was 100% normal activity, followed by a 1 hour, 10 minute gap where no events happened, then normal activity again.  So in this case no carrier issue - if the uplink was dead we'd have at least seen internal traffic trying to get out.

What was the problem? I'm suspecting a loose power cable or a flaky power supply, no definitive answer yet.  This box is running the same OS as dozens of other ASAs I work with, and there are no OS type errors, so it really does look like hardware.

Plus this unit wasn't built as a redundant pair and this model doesn't have a redundant power supply - that's all getting fixed sometime soon!

Have you used a fun log forensics trick you can share?  Especially if you have a handy script, or if the root cause was a letdown like this one?  Please, use our comment form to share!

===============
Rob VandenBrink
[[email protected]](/cdn-cgi/l/email-protection)

Keywords:

[5 comment(s)](/diary/Finding%2BGaps%2Bin%2BSyslog%2BHow%2Bto%2Bfind%2Bwhen%2Bnothing%2Bhappened/29314/#comments)

* [previous](/diary/29304)
* [next](/diary/29316)

### Comments

I like the article, however there are a few points I'd make.

1) Following the 2nd command example, you have "Note the two different uses of cat" where I believe you intended to say "...of cut" instead.

2) In the paragraph following that, you have:
"""but I put a "sort" in their anyway, just on principle ("sort | uniq" is a string that should be stored in your fingers)."""

In that section, you have a typo which should be "there" instead. (And are missing a space after the comma leading that portion.)

But more importantly than that, I'd say that "sort -u" should be stored in people's fingers instead of the pair of "sort|uniq" honestly. It saves an extra pass through a large file, and also saves an extraneous process launch, while being universally available in all versions of sort that I ever seem to find in use.

3) Then within the PowerShell examples, you suggested shelling out to cmd, which I don't understand. There is a (relatively) long-standing alias in Power...