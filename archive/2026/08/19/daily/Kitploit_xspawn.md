---
title: xspawn
url: https://kitploit.com/en/tools/github/cenobyte-vincit/xspawn
source: Kitploit
date: 2026-08-19
fetch_date: 2026-08-20T02:55:04.134271
---

# xspawn

[Skip to content](#main-content)

[![Kitploit](/_next/image?url=%2Flogo.png&w=64&q=75)KITPLOIT](/en)[Tools](/en/tools)[Blog](/en/blog)Categories

EN

[Submit](/en/submit)

[Tools](/en/tools)[Blog](/en/blog)Categories

[Submit](/en/submit)

EN

Hacking, PenTest, and Cybersecurity Tools for Your Security Arsenal!

Kitploit is a directory of hacking, cybersecurity, and pentesting tools. Discover the latest project updates to find vulnerabilities, analyze systems, automate testing, and strengthen your security.

·Analytics preferences·[Feeds](/en/feeds)·[Contact](/en/contact)·[Privacy](/en/privacy)·© 2026 Kitploit

Tool Directory

## Categories

[View all categories](/en/categories)

Loading categories

xspawn — Spawns macOS programs through launchd's private XPC interface without execing them, making EDR record launchd as parent. Supports one-shot, KeepAlive, and plist-based jobs. | Kitploit

[Tools](/en/tools)/![GitHub](/providers/github.png)GitHub/cenobyte-vincit/xspawn

![](/_next/image?url=https%3A%2F%2Fassets.kitploit.com%2Fproduction%2Fpublic%2Ftools%2F50498%2F540be72658c67d0c4228415c65851d51f4c2fab017792814f9722d2fed7546f1.png&w=3840&q=75)

[Persistence Mechanisms](/en/categories/persistence-mechanisms)[IDS/IPS Evasion](/en/categories/ids-ips-evasion)[Post-Exploitation](/en/categories/post-exploitation)[Red Teaming](/en/categories/red-teaming)[Adversarial Attack](/en/categories/adversarial-attack)

![GitHub](/providers/github.png)cenobyte-vincit/xspawn

# xspawn

Spawns macOS programs through launchd's private XPC interface without execing them, making EDR record launchd as parent. Supports one-shot, KeepAlive, and plist-based jobs.

[View Repository](https://github.com/cenobyte-vincit/xspawn)

81 day ago![Not yet reviewed](/_next/image?url=%2Fbadges%2Fkitploit_badge_not_reviewed_full.png&w=48&q=75)

### Most Popular

[View all →](/en/tools)

Discover the most used tools by our community.

Last 7 DaysLast 30 Days

Explore all tools

Browse our collection of tools

[View all tools →](/en/tools)

Share

# xspawn

xspawn starts a program on macOS through launchd and never execs that program itself. The aim is that an EDR records launchd as the parent, not this tool or the calling shell.

by cenobyte [[email protected]](/cdn-cgi/l/email-protection#5a2c333439332e3b3735282a3b2e28333b3f1a3d373b333674393537) 2026

<https://github.com/cenobyte-vincit/xspawn>

## Summary

xspawn opens `xpc_pipe_create_from_port(bootstrap_port)` and bootstraps the execution of a program through `_xpc_pipe_interface_routine`, the same private XPC pipe launchctl uses, and never execs the program itself.

* Root is refused. There is no other-UID mode.
* One invocation submits or removes one job.
* The client never execs `/bin/launchctl`.

## Requirements

### Runtime host

* macOS (Darwin) with a `gui/<uid>` session

### Build host

* macOS (Darwin) with Xcode Command Line Tools or Xcode
* C17 compiler (`cc`)
* `make`
* **cppcheck** for development (`brew install cppcheck`)

## Build

root@kitploit:~

```
make
```

## Usage

root@kitploit:~

```
xspawn oneshot -l <label> [-o <stdout>] [-e <stderr>] [--] <program> [args...]
xspawn submit  -l <label> [-o <stdout>] [-e <stderr>] [--] <program> [args...]
xspawn remove  -l <label>
xspawn load    -p <plist>
```

One-shot (`RunAtLoad` + `LaunchOnlyOnce`; `0` means no sleep):

root@kitploit:~

```
./xspawn oneshot -l com.example.once -- /tmp/helloworld 0
```

Arguments after `--` are `ProgramArguments`. That includes inline code (`python3 -c`, `perl -e`). CrowdStrike Falcon for macOS records the full `CommandLine`, so use inline code with interpreters sparingly.

root@kitploit:~

```
./xspawn oneshot -l com.example.py -o /tmp/py.out -- \
	/usr/bin/python3 -c "print('hello world')"
```

KeepAlive job, the same lifecycle as `launchctl submit`. Sleep `60` so CrowdStrike Falcon for macOS and `launchctl print` still see the process:

root@kitploit:~

```
./xspawn submit -l com.example.svc \
	-o /tmp/out.log -e /tmp/err.log -- /tmp/helloworld 60
```

Inspect with `launchctl print` (oracle only; this client does not call it):

root@kitploit:~

```
launchctl print gui/$(id -u)/com.example.svc
```

Success shows `type = LaunchAgent` (not `Submitted`), `program` as the absolute path, and `state = running` or briefly `xpcproxy`. `Submitted` means the job did not take the bootstrap path.

Clean up a test job:

root@kitploit:~

```
./xspawn remove -l com.example.svc
```

Load a caller-owned plist (not deleted after the reply):

root@kitploit:~

```
./xspawn load -p /tmp/job.plist
```

`<program>` must be an absolute path. launchd does not search `$PATH`.

`load -p` requires an absolute path ending in `.plist`.

`-o` / `-e` may be relative. They are resolved against the current working directory before they are written into the plist. Omitted `-o` and `-e` are `/dev/null`.

`oneshot` and `submit` probe the label in `gui` and `user` (descriptor 708) before writing the temp plist. A taken label exits with `label already loaded` and no stdout. That check exists so a doomed 800 does not write `$TMPDIR/XXXXXX/XXXXXX.plist` (a DFIR artefact; CrowdStrike Falcon keeps the path in `ASEPFilePath`) or print the XML copy of the job dictionary. A free label prints the temp path, then that XML, then sends 800. `load -p` runs the same occupancy check on the file's `Label`, then prints the caller path and XML. The temp directory is removed on every exit. `remove` is by label.

## Exit codes

| Code | Meaning |
| --- | --- |
| 0 | Bootstrap or bootout XPC succeeded |
| 1 | Usage error, invalid label, root, or launchd/XPC rejection |

## Verify

Build host (`make` and the test tree; often colocated with a `gui` session). These checks are not a clean-runtime proof:

root@kitploit:~

```
make
make test
make test-unit
make test-functional
```

root@kitploit:~

```
./xspawn oneshot -l com.example.once -- /tmp/helloworld 0
```

## Limitations

* Same-user `gui/<uid>` only. Root is refused. No other-UID targeting.
* Ephemeral: not persistent across reboot or logout.
* Private XPC load and bootout constants are pinned to macOS 26.6.1 build 25G76. Re-pin if `sw_vers -buildVersion` changes (see ARCHITECTURE.md).
* Temp plist is `$TMPDIR/XXXXXX/XXXXXX.plist` (`$TMPDIR` must be absolute, else `/tmp`). The directory is removed on every exit. A taken label never creates that file.
* CrowdStrike Falcon for macOS records the temp plist path in the Auto-Start Extensibility Point field (`ASEPFilePath`) in the `ProcessRollup2` event. Process parent remains `launchd`.
* A standalone `xspawn` run is visible as this client: shell history, and an EDR process event for this binary. CrowdStrike Falcon for macOS records the full `CommandLine`, which includes the program path and its arguments. Compile the client into other tooling when that image and argv would be distinctive. Embedding does not remove `ASEPFilePath` or the launchd.log bootstrap line (see ARCHITECTURE.md, Parentage).

## Private XPC protocol

launchd is a Mach bootstrap server. This client does not use public XPC (`xpc_connection_create`). It opens a private libxpc pipe on the inherited `bootstrap_port` with `xpc_pipe_create_from_port(bootstrap_port, 4)`, then sends `_xpc_pipe_interface_routine`. Those symbols are in libxpc and are not in the SDK headers.

The routine ID is the descriptor argument, not a key in the request dictionary. On macOS 26.6.1 build 25G76, load is descriptor 800 and bootout is 801. Interface flags are 6. A `gui/<uid>` session is required: the inherited port is the gui launchd domain only inside an Aqua login session, and this client only sends `type` 8 with `handle` = uid.

Load (800) is an XPC dictionary. The job definition is not in the message body.

root@kitploit:~

```
handle   uid (uint64)
type     8 (gui)
paths    [absolute .plist]
by-cli   true
```

launchd `stat`s the path, parses the plist, then `posix_spawn`s xpcproxy. xpcproxy `exec`s the program in the same PID. Success is pipe return ...