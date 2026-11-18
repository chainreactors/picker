---
title: Dropbear: the restriction names an address — permitopen/permitlisten not enforced for unix-socket forwarding, docker.sock reachable (HEAD 99baf182, live-proven)
url: https://seclists.org/fulldisclosure/2026/Nov/38
source: Full Disclosure
date: 2026-11-17
fetch_date: 2026-11-18T09:22:47.570596
---

# Dropbear: the restriction names an address — permitopen/permitlisten not enforced for unix-socket forwarding, docker.sock reachable (HEAD 99baf182, live-proven)

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

[![Previous](/images/left-icon-16x16.png)](37)
[By Date](date.html#38)
[![Next](/images/right-icon-16x16.png)](39)

[![Previous](/images/left-icon-16x16.png)](37)
[By Thread](index.html#38)
[![Next](/images/right-icon-16x16.png)](39)

![](/shared/images/nst-icons.svg#search)

# Dropbear: the restriction names an address — permitopen/permitlisten not enforced for unix-socket forwarding, docker.sock reachable (HEAD 99baf182, live-proven)

---

*From*: theknell--- via Fulldisclosure <fulldisclosure () seclists org>
*Date*: Fri, 13 Nov 2026 14:40:22 -0500

---

```
Dropbear is the SSH server that ships where OpenSSH is too big: routers,
embedded systems, rescue images, appliances — anywhere a small, hardened
sshd is wanted. It has been fuzzed and audited for two decades, and its
handling of restricted keys is one of the reasons administrators trust it
with narrow jobs. A key in authorized_keys can carry permitopen="host:port"
and permitlisten="host:port": this key may forward to that destination,
and to no other. Backup keys, tunnel keys, CI keys are handed out on the
strength of that line.

The restriction names an address. A unix socket is not an address, and on
the socket path the restriction is never consulted. Tested against
mkj/dropbear at commit 99baf1828c13e88de048e641d03694bfe8923251
(2026-11-11), built from source, full history reviewed:

1. TCP forwarding enforces the per-destination restrictions. Local TCP
   (direct-tcpip) calls svr_pubkey_allows_local_tcpfwd(desthost, destport)
   at src/svr-tcpfwd.c:202, which walks the key's permitopen list
   (src/svr-authpubkeyoptions.c:98-118). Remote TCP calls
   svr_pubkey_allows_remote_tcpfwd() at src/svr-tcpfwd.c:99, which walks
   the permitlisten list (:123-145). A destination that is not listed is
   administratively prohibited.

2. Unix-socket forwarding — direct-streamlocal () openssh com and
   streamlocal-forward () openssh com — checks only the coarse flag. The
   local path (newstreamlocal, src/svr-streamfwd.c:294) tests
   svr_opts.nolocaltcp and svr_pubkey_allows_tcpfwd(); the remote path
   (svr_remotestreamlocalreq, src/svr-streamfwd.c:219) tests
   svr_opts.noremotefwd and the same function. svr_pubkey_allows_tcpfwd()
   (src/svr-authpubkeyoptions.c:65-72) knows only the no-port-forwarding
   flag. Neither streamlocal path calls either per-destination function,
   and a search of the tree confirms those two functions are referenced
   only from src/svr-tcpfwd.c — never from src/svr-streamfwd.c.

3. The socket paths are on by default: src/default_options.h:76-77 sets
   DROPBEAR_SVR_LOCALSTREAMFWD and DROPBEAR_SVR_REMOTESTREAMFWD to 1,
   and the channel is registered at src/svr-session.c:80.

4. This is an incomplete fix, in the vendor's own words. Commit 796a89ef
   (2024-04-03), "Apply tcp forwarding restrictions to unix sockets too",
   added the coarse gate to newstreamlocal() and updated the manpage to
   say no-port-forwarding covers unix streams. The per-destination
   restrictions — the other half of what that title announces — were not
   applied. The author notes the absence himself at
   src/svr-streamfwd.c:213-214: the check could be relaxed if a
   permitlisten equivalent were added for streamlocal. It has not been,
   on any branch, as of the tested commit. A sibling fix (00cfa132)
   applied a different per-key restriction to the same path, so the path
   is not one the author considers outside the restriction model.

Live proof, against our own rig only (server built from the pinned
source, localhost): a test account's only key carried
permitopen="127.0.0.1:1",no-pty, and a unix echo server listened at
/tmp/target.sock. The permitted TCP destination (127.0.0.1:1) passed the
permitopen check and failed only on connect — the restriction parsed and
active. The non-permitted TCP destination (127.0.0.1:22) was refused:
"Administratively prohibited" — permitopen enforced, same key, same
session. The streamlocal channel to /tmp/target.sock was accepted, and
returned the echo server's banner, UNIX-SOCKET-REACHED. The list was
never consulted. Replicated once from a clean build. Harness and raw log
accompany this paper.

The escalation was fired the same way. The test account was placed in
the docker group — the normal condition for the CI and deploy accounts
that receive restricted keys — and the same key opened a
direct-streamlocal channel to /var/run/docker.sock and issued a Docker
API request over it: HTTP/1.1 200 OK, Api-Version 1.56, the real daemon.
TCP to a non-permitted destination stayed prohibited in the same
session. The Docker socket is host-root-equivalent; the daemon will run
a container with the host filesystem mounted, as root.

Scope, stated plainly: this is not unauthenticated, and it is not a
10.0. The attacker holds a valid key — a key the administrator
deliberately restricted to one destination. Post-bypass reach is
bounded by the sockets that account's OS identity can touch: the Docker
socket, database sockets (/run/mysqld/mysqld.sock,
/run/postgresql/.s.PGSQL.5432), agent and service sockets, and, in the
permitlisten direction, the ability to make the server listen on an
arbitrary writable unix path and shadow a service socket. That bound is
not the boundary under discussion. permitopen exists for accounts that
are not trusted with general reach; for those accounts, streamlocal is
reach the administrator explicitly withheld. Scored as a range for
exactly that reason: 9.9 (AV:N/AC:L/PR:L/UI:N/S:C/C:H/I:H/A:H) when the
account can reach the Docker daemon or a database socket, ~7 when it
can reach only its own sockets.

What held is credited at the same weight. The pre-authentication
surface was audited and exercised in the same pass and nothing is
claimed there: the post-quantum hybrid KEX bounds-checks every read and
asserts full input consumption, its length constants match the
reference implementations, strict-KEX handling is correct, and the
recent pre-auth-adjacent fixes are properly applied. The neighbouring
fixes in the forwarding family were likewise verified in place —
the ssh-askpass write, the long authorized_keys line split, the
curve25519 canonicality checks, the streamfwd drop-privileges error.
The vendor's own fuzz targets, built from the pinned source, ran clean
on seed inputs. This is a logic gap, the class a fuzzer cannot see:
the check exists, is correct, and is wired to only half the doors.

The fix is not complicated. Until a path-based equivalent exists, a key
carrying any per-destination restriction should be refused streamlocal
channels outright; the complete fix is a path-based option enforced in
svr-streamfwd.c with the same list walk the TCP path uses.

The restriction was applied to unix sockets in April 2024. The half of
it that names destinations is the half that was left behind.

Paper: https://archive.org/details/knell-not-an-address

Key: 133883AB9F6EDE5B9BA6B82E27BEDAF0CE152F25 (knell)

Verify: gpg --import knell-public.asc, then
gpg --verify paper-dropbear-FINAL-2026-11-13.md.asc

— knell

More, signed and timestamped:
https://github.com/the-knell

Sent from [Proton Mail](https://proton.me/mail/home) for Android.
_______________________________________________
Sent through the Full Disclosure mailing list
https://nmap.org/mailman/listinfo/fulldisclosure
Web Archives & RSS: https://seclists.org/fulldisclosure/
```

---

[![Previous](/images/left-icon-16x16.png)](37)
[By Date](date.html#38)
[![Next](/images/right-icon-16x16.png)](39)

[![Pr...