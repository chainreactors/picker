---
title: Port Scanning in Powershell Redux: Speeding Up the Results (challenge accepted&#x21;), (Fri, Dec 9th)
url: https://isc.sans.edu/diary/rss/29324
source: SANS Internet Storm Center, InfoCON: green
date: 2022-12-10
fetch_date: 2025-10-04T01:08:54.184679
---

# Port Scanning in Powershell Redux: Speeding Up the Results (challenge accepted&#x21;), (Fri, Dec 9th)

# [Internet Storm Center](/)

[Sign In](/login.html)
[Sign Up](/register.html)

Handler on Duty: [Johannes Ullrich](/handler_list.html#johannes-ullrich "Johannes Ullrich")

Threat Level: [green](/infocon.html)

* [previous](/diary/29316)
* [next](/diary/29326)

# [Port Scanning in Powershell Redux: Speeding Up the Results (challenge accepted!)](/forums/diary/Port%2BScanning%2Bin%2BPowershell%2BRedux%2BSpeeding%2BUp%2Bthe%2BResults%2Bchallenge%2Baccepted/29324/)

**Published**: 2022-12-09. **Last Updated**: 2022-12-09 12:40:36 UTC
**by** [Rob VandenBrink](/handler_list.html#rob-vandenbrink) (Version: 1)

[3 comment(s)](/diary/Port%2BScanning%2Bin%2BPowershell%2BRedux%2BSpeeding%2BUp%2Bthe%2BResults%2Bchallenge%2Baccepted/29324/#comments)

In the story I wrote in October about using PowerShell for Port Scanning ([https://isc.sans.edu/diary/29202](https://isc.sans.edu/diary/NMAP%2Bwithout%2BNMAP%2BPort%2BTesting%2Band%2BScanning%2Bwith%2BPowerShell/29202)), I noted that the basic "test-connect" operation made for a pretty slow port scanner, which seems to be the message that everyone latched onto.  Of course, my immediate response was "**challenge accepted**!", so let's go - let's make that operation faster!

First, let's do a /24 subnet "no frills" scan for one port, using nmap:

nmap -Pn --open -p22 192.168.122.0/24
Starting Nmap 7.92 ( https://nmap.org ) at 2022-12-08 16:11 Eastern Standard Time
...
<scan results go here >
...
**Nmap done: 256 IP addresses (30 hosts up) scanned in 14.34 seconds**

There, ~14 seconds and change is the time to beat!

Now, using our "system.net.sockets.tcpclient" PowerShell method (that was discussed in October's story) to do the same scan:

$range = @(1..254)
$global:results
$results=@()

foreach($i in $range) {
$h = "192.168.122."+$i
$r = new-object -type psobject
$r | add-member -membertype noteproperty -name item -value $i
$r | add-member -membertype noteproperty -name host -value $h
$r | add-member -membertype noteproperty -name port -value 22
$r | add-member -membertype noteproperty -name state -value ""
$results += $r
}

$
$t1 = get-date

$results | foreach-object  {
    $item = $\_.item-1
    $obj = new-Object system.Net.Sockets.TcpClient
    $connect = $obj.BeginConnect($\_.host,$\_.port,$null,$null)
    $Wait = $connect.AsyncWaitHandle.WaitOne(100,$false)
    If (-Not $Wait) {
        $\_.state = "closed - Timeout"
    } else {
        $\_.state = "Open"
    }

    }

$t2 = get-date
$elapsed = ($t2-$t1).totalseconds
write-host $elapsed "seconds"

This gives us a respectable time of **27.1 seconds**.  Anyway, close, but no cigar - we've somehow got to speed this script up by 50%. Hmm, how to get there?

Enter - Parallel Processing in PowerShell!  Just like in everyone's favourite tongue-twister, "How many Processes could Peter Piper Parse?"

Parallel processing was just introduced into PowerShell in version 7, the foreach-object loop operator now has a "-parallel" option (https://ss64.com/ps/foreach.html).  The trick is keeping the output of all of the threads (which will end at different, non-sequential times) straight.  Another fun restriction of this method is that you can't call outside functions or modules inside the parallel code block, so if you want to use a module, it has to be imported inside the code block.  This is why I didn't us a function in this example - a function would make for all kinds of sense (and a one-line loop), but it won't work once you run it in parallel.  I'll keep the data straight by populating an array with the results - I'm sure there are better ways to do this though.

Let's update the script above for parallel operation:

$range = @(1..254)
# $global:results
$results=@()

foreach($i in $range) {
$h = "192.168.122."+$i
$r = new-object -type psobject
$r | add-member -membertype noteproperty -name item -value $i
$r | add-member -membertype noteproperty -name host -value $h
$r | add-member -membertype noteproperty -name port -value 22
$r | add-member -membertype noteproperty -name state -value ""
$results += $r
}

$t1 = get-date

$results | foreach-object **-Parallel** {
    $item = $\_.item-1
    $obj = new-Object system.Net.Sockets.TcpClient
    $connect = $obj.BeginConnect($\_.host,$\_.port,$null,$null)
    $Wait = $connect.AsyncWaitHandle.WaitOne(100,$false)
    If (-Not $Wait) {
        $\_.state = "closed - Timeout"
    } else {
        $\_.state = "Open"
    }

}

$t2 = get-date
$elapsed = ($t2-$t1).totalseconds
write-host $elapsed "seconds"

**Wowzers!  5.5 seconds!!**  I guess that answers that!
I used nmap as my baseline - there are of course faster scanners, or you can of course speed up nmap by playing with the "T" parameter and other values, but even after changing to T5 in nmap my times were still over 12 seconds.

Back to the PowerShell code - storing the data in objects also has the advantage of allowing you to play with the data and output after execution:

$results[0] | ft

item host          port state
---- ----          ---- -----
   1 192.168.122.1   22 Open

$results | where state -eq Open | select host,port,state

host            port state
----            ---- -----
192.168.122.1     22 Open
192.168.122.5     22 Open
192.168.122.6     22 Open
192.168.122.7     22 Open
192.168.122.8     22 Open
192.168.122.51    22 Open
192.168.122.69    22 Open
192.168.122.178   22 Open
192.168.122.194   22 Open

Just to play with that "parallel" idea a bit more - you can adjust the number of simultaneous threads (the default is 5) by adding a "throttlelimit" value:

$t1 = get-date

$results | foreach-object **-Parallel** {
    $item = $\_.item-1
    $obj = new-Object system.Net.Sockets.TcpClient
    $connect = $obj.BeginConnect($\_.host,$\_.port,$null,$null)
    $Wait = $connect.AsyncWaitHandle.WaitOne(100,$false)
    If (-Not $Wait) {
        $\_.state = "closed - Timeout"
    } else {
        $\_.state = "Open"
    }

    }  **-throttlelimit 50**

I found that for this particular application playing with throttlelimit didn't make too much difference - I seem to always get something between 4 and 6 seconds, no matter what the value.  I expect that a script block that takes longer to execute might benefit from a higher throttlelimit value  (until you max out your memory or cpu that is).

Have you tripped over a new feature in PowerShell 7 that has saved your bacon?  Or do you have a tweak for the code in this story?  Please, share in your comment form!

===============
Rob VandenBrink
[[email protected]](/cdn-cgi/l/email-protection)

Keywords:

[3 comment(s)](/diary/Port%2BScanning%2Bin%2BPowershell%2BRedux%2BSpeeding%2BUp%2Bthe%2BResults%2Bchallenge%2Baccepted/29324/#comments)

* [previous](/diary/29316)
* [next](/diary/29326)

### Comments

Threadsafe dictionary is an easy way to "export" data.
You can use the IP address/ $host as the key. Just make sure each parallel invocation has its own key, and you are home free.

$threadSafeDictionary = [System.Collections.Concurrent.ConcurrentDictionary[string,object]]::new()
Get-Process | ForEach-Object -Parallel {
$dict = $using:threadSafeDictionary
$dict.TryAdd($\_.ProcessName, $\_)
}

#### PHP

#### Dec 12th 2022 2 years ago

Note that Add-Member can take -NotePropertyMembers where you can add multiple properties via a hashtable in one call rather than using multiple times

#### PHP

#### Dec 21st 2022 2 years ago

Note that Add-Member can take -NotePropertyMembers where you can add multiple properties via a hashtable in one call rather than using multiple times

#### PHP

#### Dec 21st 2022 2 years ago

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
  + [SSH/Te...