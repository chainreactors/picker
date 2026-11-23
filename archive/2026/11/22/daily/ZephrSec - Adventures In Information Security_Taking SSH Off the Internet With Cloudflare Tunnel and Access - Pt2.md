---
title: Taking SSH Off the Internet With Cloudflare Tunnel and Access - Pt2
url: https://blog.zsec.uk/ssh-ghost-2/
source: ZephrSec - Adventures In Information Security
date: 2026-11-22
fetch_date: 2026-11-23T10:02:59.046649
---

# Taking SSH Off the Internet With Cloudflare Tunnel and Access - Pt2

[Skip to content](#main)

[![ZephrSec - Adventures In Information Security](/content/images/size/w400/2025/05/YoutubeHeader-Recovered-1.png)](https://blog.zsec.uk)

* [About Andy Gill/ZephrFish](https://blog.zsec.uk/about/)
* [My Red Team Course](https://lms.zsec.red/courses/malwareless-adversarial-emulation)
* [ZephrSec](https://zephrsec.com)
* [My Books](https://leanpub.com/b/LearningTheRopes)
* [Photo Blog](https://photos.zsec.uk/)

[Buy me a coffee](https://blog.zsec.uk/support/)

Toggle colour scheme
[Buy me a coffee](https://blog.zsec.uk/support/)
[Subscribe](#/portal/signup)
Menu

[blueteam](/tag/blueteam/)

# Taking SSH Off the Internet With Cloudflare Tunnel and Access - Pt2

Locking the origin to your own Cloudflare zone with authenticated origin pulls, then detection and recovery (auditd, login alerts, off-site backups, patching), sandboxing Ghost and nginx, fail2ban that actually works behind Cloudflare, and hardening the analytics container.

[Andy Gill](/author/andy/)
/
22 November 2026
/
20 min read
/

 views

![](/content/images/size/w30/2025/06/DSC05763.jpg)
![Metal railings at night, red light reflected on wet ground](/content/images/size/w1200/2025/06/DSC05763.jpg)

Railings and red light after the rain, ZephrSnaps

On this page

On this page

If you haven't read Part 1, check it out first, as this is a continuation and picks up more details feeding into fixing up SSH and my VPS lockdown as a three part series.

[Part 1](https://blog.zsec.uk/ssh-ghost-1/) closed the SSH port and moved everything behind Cloudflare Tunnel, so this part picks up the web side: locking the origin so only my Cloudflare zone can reach it, adding detection so I'd actually know if something went wrong, and sandboxing the services that sit behind it.

In this part I'm going to cover:

* Locking the web origin so only my own Cloudflare zone can reach it
* Detection and recovery: auditd, alerts, off-site backups, a cloud firewall and patching
* Sandboxing the services with systemd
* Fail2ban that actually works behind Cloudflare
* Hardening the analytics container

![Diagram: visitor to Cloudflare edge to firewall to nginx to Ghost; direct hits on the origin IP and someone else's Cloudflare zone are both refused](https://blog.zsec.uk/content/images/2026/11/ssh-pt2-origin-lockdown.png)

Only my Cloudflare zone gets through: a direct hit stops at the firewall, someone else's zone stops at nginx

## Step 4: Lock the Web Origin to *Your* Cloudflare Zone

Allowing only Cloudflare's IP ranges proves traffic came *through Cloudflare*, but not whose account sent it. Anyone can point their own Cloudflare zone at your origin IP and skip your WAF, rate limits and cache rules.

### 4a. Keep the Cloudflare IP List Current

A weekly systemd timer fetches Cloudflare's IP ranges and syncs them into nginx `set_real_ip_from`, ufw 443 rules, and fail2ban's `ignoreip`. A bad fetch must never empty your allowlist, so every sanity check runs before anything changes.

1. The script tags its ufw rules with the comment `cloudflare` and only ever removes tagged rules. If your existing 443 rules have no comment, run the script once, check `ufw status` shows the tagged rules, then delete the old untagged ones by number (`ufw status numbered`, then `ufw delete <n>`, highest number first).
2. If your site config already has `set_real_ip_from` lines, remove them so the generated file is the only list.

Add the service and timer:

```
# /etc/systemd/system/cf-ips-refresh.service
[Unit]
Description=Refresh Cloudflare IP ranges
Wants=network-online.target
After=network-online.target

[Service]
Type=oneshot
ExecStart=/usr/local/sbin/cf-ips-refresh
```

```
# /etc/systemd/system/cf-ips-refresh.timer
[Unit]
Description=Weekly Cloudflare IP refresh

[Timer]
OnCalendar=weekly
RandomizedDelaySec=6h
Persistent=true

[Install]
WantedBy=timers.target
```

Save the script as `/usr/local/sbin/cf-ips-refresh` and `chmod 700` it:

```
#!/bin/bash
# /usr/local/sbin/cf-ips-refresh
set -euo pipefail
tmp=$(mktemp -d)
trap 'rm -rf "$tmp"' EXIT

# 1. Fetch both lists. awk drops blank lines and adds the missing final newline.
curl -fsS -m 20 https://www.cloudflare.com/ips-v4 | awk 'NF' > "$tmp/v4"
curl -fsS -m 20 https://www.cloudflare.com/ips-v6 | awk 'NF' > "$tmp/v6"

# 2. Sanity checks: enough ranges, and every line is a CIDR. Any failure exits
#    here, before anything on the server changes.
[ "$(wc -l < "$tmp/v4")" -ge 5 ] || { echo "too few v4 ranges" >&2; exit 1; }
[ "$(wc -l < "$tmp/v6")" -ge 3 ] || { echo "too few v6 ranges" >&2; exit 1; }
if grep -qvE '^[0-9.]+/[0-9]+$' "$tmp/v4"; then echo "bad v4 line" >&2; exit 1; fi
if grep -qvE '^[0-9a-f:]+/[0-9]+$' "$tmp/v6"; then echo "bad v6 line" >&2; exit 1; fi
cat "$tmp/v4" "$tmp/v6" > "$tmp/all"

# 3. nginx: trust CF-Connecting-IP only from Cloudflare. Roll back if nginx -t fails.
conf=/etc/nginx/conf.d/cloudflare-realip.conf
{ sed 's/.*/set_real_ip_from &;/' "$tmp/all"; echo 'real_ip_header CF-Connecting-IP;'; } > "$tmp/realip.conf"
[ -f "$conf" ] && cp "$conf" "$tmp/realip.old"
install -m 644 "$tmp/realip.conf" "$conf"
if ! nginx -t -q; then
  if [ -f "$tmp/realip.old" ]; then cp "$tmp/realip.old" "$conf"; else rm -f "$conf"; fi
  echo "nginx -t failed, rolled back" >&2; exit 1
fi
systemctl reload nginx

# 4. ufw: allow 443 from each range, then remove tagged ranges that have gone.
while read -r c; do
  ufw allow proto tcp from "$c" to any port 443 comment cloudflare > /dev/null
done < "$tmp/all"
ufw status | grep '# cloudflare' | grep -oE '[0-9a-f.:]+/[0-9]+' | sort -u |
while read -r c; do
  grep -qxF "$c" "$tmp/all" || ufw delete allow proto tcp from "$c" to any port 443 > /dev/null
done

# 5. fail2ban: never ban Cloudflare's own addresses (skipped until fail2ban is installed).
if [ -d /etc/fail2ban/jail.d ]; then
  { echo '[DEFAULT]'; echo "ignoreip = 127.0.0.1/8 ::1 $(tr '\n' ' ' < "$tmp/all")"; } \
    > /etc/fail2ban/jail.d/cloudflare-ignoreip.conf
  fail2ban-client reload > /dev/null
fi
```

With all three files in place, run it once by hand and enable the timer:

```
systemctl daemon-reload
systemctl start cf-ips-refresh.service && journalctl -u cf-ips-refresh -n 20
systemctl enable --now cf-ips-refresh.timer
systemctl list-timers cf-ips-refresh.timer
```

A failed run leaves the previous rules in place and shows up as a failed unit in `systemctl --failed`.

### 4b. Reject Hostnames You Don't Serve

If your site's server block is the `default_server`, any Host or SNI gets your site, so add a catch-all that refuses at the TLS handshake:

```
server {
    listen 80 default_server;
    listen [::]:80 default_server;
    server_name _;
    return 444;
}
server {
    listen 443 ssl default_server;
    listen [::]:443 ssl default_server;
    server_name _;
    ssl_reject_handshake on;
}
```

**Before you do, find every name that really points at the box.** I found an old domain CNAMEd to the blog on a zone set to **Flexible SSL**, which meant Cloudflare was fetching it over plain HTTP on port 80, so closing 80 would have quietly broken it. The fix was a Cloudflare redirect rule on that zone (`concat("https://blog.example.com", http.request.uri.path)`, 301), which I confirmed by checking the origin access log for a unique marker path, and only after that could port 80 close.

To deploy the catch-all:

1. Save the two `server` blocks as `/etc/nginx/conf.d/00-catch-all.conf`, which Debian and Ubuntu include inside the `http` block.
2. Remove `default_server` from your site's own `listen` lines, because nginx refuses to start with two default servers on the same port.
3. Close port 80 by deleting its allow rules: `ufw status numbered`, then `ufw delete <n>` for each port 80 rule, highest number first.

Apply and test from the server:

```
nginx -t && systemctl reload nginx
curl -sk --resolve wrong.example:443:127.0.0.1 https://wrong.example/ ; echo "exit $?"   # handshake refused, non-zero exit
curl -sk --resolve blog.example.com:443:127.0.0.1 -o /dev/nu...