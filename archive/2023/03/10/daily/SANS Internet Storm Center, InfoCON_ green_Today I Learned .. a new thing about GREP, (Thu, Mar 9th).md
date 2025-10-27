---
title: Today I Learned .. a new thing about GREP, (Thu, Mar 9th)
url: https://isc.sans.edu/diary/rss/29618
source: SANS Internet Storm Center, InfoCON: green
date: 2023-03-10
fetch_date: 2025-10-04T09:11:36.933941
---

# Today I Learned .. a new thing about GREP, (Thu, Mar 9th)

# [Internet Storm Center](/)

[Sign In](/login.html)
[Sign Up](/register.html)

Handler on Duty: [Johannes Ullrich](/handler_list.html#johannes-ullrich "Johannes Ullrich")

Threat Level: [green](/infocon.html)

* [previous](/diary/29614)
* [next](/diary/29620)

# [Today I Learned .. a new thing about GREP](/forums/diary/Today%2BI%2BLearned%2Ba%2Bnew%2Bthing%2Babout%2BGREP/29618/)

**Published**: 2023-03-09. **Last Updated**: 2023-03-09 02:34:48 UTC
**by** [Rob VandenBrink](/handler_list.html#rob-vandenbrink) (Version: 1)

[4 comment(s)](/diary/Today%2BI%2BLearned%2Ba%2Bnew%2Bthing%2Babout%2BGREP/29618/#comments)

Grep is a command line tool I use every single day.  Not much to it, I use:

-i for case insensitive searches
-v to search for "not that thing"
quotes or "\" characters to excape out special characters
the "|" character ("this | that") to search for "this or that"

Not much else to know right?

I was searching Windows DNS Server logs (the text ones) the other day (and what a JOY those are!) - we were putting an ACL on a printer VLAN and noticed that one HP printer was making DNS requests, then opening a cleartext HTTP session to random AWS IP addresses.  OSINT didn't give me great intel on what those hosts were, so spelunking we did go in the DNS logs to see what this was all about!

Great, so let's find the IP's in the file:

C:\dnslogfiles\t>type dc5dns.txt | grep 3.217.159.189
      DATA   3.217.159.189
      DATA   3.217.159.189
      DATA   3.217.159.189
      DATA   3.217.159.189
      DATA   3.217.159.189
      DATA   3.217.159.189
.. and so on.

Not so useful, I said (OK, I added a few other words when I saw the output).  What I really need is that line of "foudn text", plus maybe ~20 lines before and after that text to see more of the DNS query and answer.  I was resigned to writing something that would do that, but then I though - surely I'm not the only person who needed "the text lines around the search text" - maybe it's built into grep?

After a quick "man grep", I found that indeed I was not the first person to wish for that.  From "man grep":
       -A NUM, --after-context=NUM
              Print NUM lines of trailing context after  matching  lines.
              Places a line containing a group separator (described under
              --group-separator) between contiguous  groups  of  matches.
              With  the  -o or --only-matching option, this has no effect
              and a warning is given.

       -B NUM, --before-context=NUM
              Print NUM lines of leading context before  matching  lines.
              Places a line containing a group separator (described under
              --group-separator) between contiguous  groups  of  matches.
              With  the  -o or --only-matching option, this has no effect
              and a warning is given.

Awesome!!  Here I thought this would be a story about some cool code or a sed script that I had to write, but what I'm looking for is already in grep!!

Looking closer at the file, what I wanted was the "found text", with 2 lines before and ~50 lines or so after

C:\dnslogfiles\t>type dc5dns.txt | grep -A 50 -B 37 3.217.159.189 | more

2/23/2023 5:13:14 PM 0C1C PACKET  00000005D8F8BC40 UDP Rcv 205.251.196.95  0747 R Q [2084 A     NOERROR] A      (39)prod-pod4-dvc-signaling-podlb-218071557(9)us-east-1(3)elb(9)amazonaws(3)com(0)
UDP response info at 00000005D8F8BC40
  Socket = 11312
  Remote addr 205.251.196.95, port 53
  Time Query=3087729, Queued=0, Expire=0
  Buf length = 0x0fa0 (4000)
  Msg length = 0x0129 (297)
  Message:
    XID       0x0747
    Flags     0x8420
      QR        1 (RESPONSE)
      OPCODE    0 (QUERY)
      AA        1
      TC        0
      RD        0
      RA        0
      Z         0
      CD        0
      AD        1
      RCODE     0 (NOERROR)
    QCOUNT    1
    ACOUNT    4
    NSCOUNT   4
    ARCOUNT   1
    QUESTION SECTION:
    Offset = 0x000c, RR count = 0
    Name      "(39)prod-pod4-dvc-signaling-podlb-218071557(9)us-east-1(3)elb(9)amazonaws(3)com(0)"
      QTYPE   A (1)
      QCLASS  1
    ANSWER SECTION:
    Offset = 0x0055, RR count = 0
    Name      "[C00C](39)prod-pod4-dvc-signaling-podlb-218071557(9)us-east-1(3)elb(9)amazonaws(3)com(0)"
      TYPE   A  (1)
      CLASS  1
      TTL    60
      DLEN   4
      DATA   3.217.159.189
    Offset = 0x0065, RR count = 1
    Name      "[C00C](39)prod-pod4-dvc-signaling-podlb-218071557(9)us-east-1(3)elb(9)amazonaws(3)com(0)"
      TYPE   A  (1)
      CLASS  1
      TTL    60
      DLEN   4
      DATA   34.204.229.165
    Offset = 0x0075, RR count = 2
    Name      "[C00C](39)prod-pod4-dvc-signaling-podlb-218071557(9)us-east-1(3)elb(9)amazonaws(3)com(0)"
      TYPE   A  (1)
      CLASS  1
      TTL    60
      DLEN   4
      DATA   34.234.159.190
    Offset = 0x0085, RR count = 3
    Name      "[C00C](39)prod-pod4-dvc-signaling-podlb-218071557(9)us-east-1(3)elb(9)amazonaws(3)com(0)"
      TYPE   A  (1)
      CLASS  1
      TTL    60
      DLEN   4
      DATA   54.175.201.22
    AUTHORITY SECTION:
    Offset = 0x0095, RR count = 0
    Name      "[C034](9)us-east-1(3)elb(9)amazonaws(3)com(0)"
      TYPE   NS  (2)
      CLASS  1
      TTL    1800
      DLEN   23
      DATA   (7)ns-1119(9)awsdns-11(3)org(0)
    Offset = 0x00b8, RR count = 1
    Name      "[C034](9)us-east-1(3)elb(9)amazonaws(3)com(0)"
      TYPE   NS  (2)
      CLASS  1
      TTL    1800
      DLEN   25
      DATA   (7)ns-1793(9)awsdns-32(2)co(2)uk(0)
    Offset = 0x00dd, RR count = 2
    Name      "[C034](9)us-east-1(3)elb(9)amazonaws(3)com(0)"
      TYPE   NS  (2)
      CLASS  1
      TTL    1800
      DLEN   19
      DATA   (6)ns-235(9)awsdns-29[C04C](3)com(0)
    Offset = 0x00fc, RR count = 3
    Name      "[C034](9)us-east-1(3)elb(9)amazonaws(3)com(0)"
      TYPE   NS  (2)
      CLASS  1
      TTL    1800
      DLEN   22
      DATA   (6)ns-934(9)awsdns-52(3)net(0)
--
  Msg length = 0x00bd (189)
  Message:
    XID       0x0a56
    Flags     0x8180
      QR        1 (RESPONSE)
      OPCODE    0 (QUERY)
      AA        0
      TC        0
      RD        1
      RA        1
      Z         0
      CD        0
      AD        0
      RCODE     0 (NOERROR)
    QCOUNT    1
    ACOUNT    5
    NSCOUNT   0
    ARCOUNT   0
    QUESTION SECTION:
    Offset = 0x000c, RR count = 0
    Name      "(6)signal(4)pod4(6)avatar(3)ext(2)hp(3)com(0)"
      QTYPE   A (1)
      QCLASS  1
    ANSWER SECTION:
    Offset = 0x002f, RR count = 0
    Name      "[C00C](6)signal(4)pod4(6)avatar(3)ext(2)hp(3)com(0)"
      TYPE   CNAME  (5)
      CLASS  1
      TTL    3499
      DLEN   66
      DATA   (39)prod-pod4-dvc-signaling-podlb-218071557(9)us-east-1(3)elb(9)amazonaws[C026](3)com(0)
    Offset = 0x007d, RR count = 1
    Name      "[C03B](39)prod-pod4-dvc-signaling-podlb-218071557(9)us-east-1(3)elb(9)amazonaws[C026](3)com(0)"
      TYPE   A  (1)
      CLASS  1
      TTL    59
      DLEN   4
      DATA   3.217.159.189
    Offset = 0x008d, RR count = 2
    Name      "[C03B](39)prod-pod4-dvc-signaling-podlb-218071557(9)us-east-1(3)elb(9)amazonaws[C026](3)com(0)"
      TYPE   A  (1)
      CLASS  1
      TTL    59
      DLEN   4
      DATA   34.204.229.165
    Offset = 0x009d, RR count = 3
    Name      "[C03B](39)prod-pod4-dvc-signaling-podlb-218071557(9)us-east-1(3)elb(9)amazonaws[C026](3)com(0)"
      TYPE   A  (1)
      CLASS  1
      TTL    59
      DLEN   4
      DATA   34.234.159.190
    Offset = 0x00ad, RR count = 4
    Name      "[C03B](39)prod-pod4-dvc-signaling-podlb-218071557(9)us-east-1(3)elb(9)amazonaws[C026](3)com(0)"
      TYPE   A  (1)
      CLASS  1
      TTL    59
      DLEN   4
      DATA   54.175.201.22
    AUTHORITY SECTION:
      empty
    ADDITIONAL SECTION:
      empty

Look in the "Question" section, the printer is making a request for an A record for the FQDN "signal.pod4.avatar.ext.hp.com"
The "answer" session shows that this is a CNAME pointed to a bunch of Amazon addresses.  So HP printer / HP hostname, this was loo...