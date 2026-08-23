---
title: foxcage — Updated!
url: https://kitploit.com/en/posts/gitlab-grepular-foxcage-6b90df100153bf7223dd75703bb39004564c150ca61d97961a35b5d78ebe881e
source: Kitploit
date: 2026-08-22
fetch_date: 2026-08-23T02:56:57.694412
---

# foxcage — Updated!

[Skip to content](#main-content)

[![Kitploit](/_next/image?url=%2Flogo.png&w=64&q=75)KITPLOIT](/en)[Tools](/en/tools)[Blog](/en/blog)Categories

EN

[Submit](/en/submit)

[Tools](/en/tools)[Blog](/en/blog)Categories

[Submit](/en/submit)

EN

Hacking, PenTest, and Cybersecurity Tools for Your Security Arsenal!

[Back to updates](/en/updates)

![](https://assets.kitploit.com/production/public/tools/8188/06f237c0d633e11bb0124526ab1b6be91d6beef402b9322f8eb6a70f49221c55.png)

UpdatedAug 22, 2026

# foxcage — Updated!

Run Firefox in a rootless Podman container with dropped capabilities, isolated networking, and ephemeral storage to contain sandbox escapes and prevent host compromise.

Share

# ![foxcage icon](https://assets.kitploit.com/production/public/readmes/8188/0df41fe24a1ebc1de3bc0a0714b24bfb19f75a49b05ebb719cd96ff9f4f3bf5d.png) foxcage

Run Firefox in a rootless Podman container for security isolation. Your browser runs with almost no Linux capabilities, in its own user and network namespace, isolated from the host — while still having full GPU acceleration, audio, and DRM support.

## Why foxcage?

Firefox already has a multi-process sandbox that isolates web content renderers using Linux namespaces and seccomp-bpf. For most threats, this is effective. foxcage adds a second wall: if an attacker exploits a vulnerability that escapes Firefox's sandbox (which happens — there are CVEs for this), they land inside a locked-down container instead of your full user session.

### What foxcage protects against

* **Post-exploit file access.** A sandbox escape on bare Firefox gives access to everything your user can read: `~/.ssh`, `~/.gnupg`, browser profiles for other browsers, password manager databases, documents, source code. In foxcage, the attacker sees only what you've explicitly mounted in.
* **On-disk tracking residue.** The `@tmp` ephemeral cage leaves zero trace on disk after the window closes — including extensions, HSTS state, TLS session cache, and DNS cache that Firefox's Private Browsing still persists. Multiple `@tmp` cages run concurrently without interfering with each other.
* **Persistence.** On bare Firefox, malware can write to `~/.config/autostart`, `~/.bashrc`, cron, or anywhere else to survive a reboot. foxcage's ephemeral container (`--rm`) means nothing persists unless you've bind-mounted it.
* **Lateral network movement.** By default, the container can't probe services on `localhost`. On bare Firefox, a sandbox escape has full network access. (Use `[network] mode = "host"` if a cage needs localhost access, e.g. for local development — but see the caveat under "Networking": host mode also exposes the host's abstract Unix sockets.)
* **Privilege escalation.** The container drops all Linux capabilities except `CAP_SYS_CHROOT` and blocks new privilege acquisition. Setuid binaries, kernel exploits via obscure syscalls, and similar escalation paths are cut off.

### What foxcage does not protect against

* **Browser-level attacks.** Phishing, malicious extensions, and anything that operates within Firefox's normal functionality is unaffected — foxcage isolates the container from the host, not the user from the browser.
* **Bind-mounted directories.** Anything you mount in (`profile`, `downloads_dir`, extra bind mounts) is fully accessible to a compromised browser. If you mount a host profile directory, an attacker can tamper with it just as on bare Firefox.
* **Audio capture via PulseAudio.** The PulseAudio socket is bind-mounted into the container. Although it is mounted read-only at the filesystem level, Unix domain sockets are bidirectional — a compromised process can still send recording requests through the socket. A browser sandbox escape could potentially record audio from the host microphone.
* **Wayland compositor exploits.** The Wayland socket is passed through. Wayland compositors isolate clients from each other by design, but a vulnerability in the compositor itself would be reachable.

### Security configuration

The container runs with:

* All Linux capabilities dropped (only `CAP_SYS_CHROOT` added back for Firefox's content sandbox; `CAP_SETUID`/`CAP_SETGID` added temporarily when `init.root` is configured)
* `no-new-privileges` to prevent privilege escalation
* Rootless user namespace (`--userns keep-id`)
* Private `/dev/shm` (not shared with host) — configurable size via `shm_size`
* Isolated networking via pasta with host loopback blocked by default
* DNS uses host DNS by default (configurable via `network.dns`)
* Only specific sockets from `XDG_RUNTIME_DIR` are bind-mounted in (Wayland, PulseAudio, PipeWire, and the filtered D-Bus proxy) — the full host runtime directory is never exposed
* Access to the host's D-Bus session bus is always mediated by a filtered `xdg-dbus-proxy` running on the host. Only `org.freedesktop.Notifications`, `org.freedesktop.portal.Desktop`, `org.mozilla.*`, and (for forks) the fork's own namespace (e.g. `org.librewolf.*`) are reachable — session services like the keyring and the SSH/GPG agent are blocked
* **Portal access is broad.** `org.freedesktop.portal.Desktop` is allowed as a whole, because that is how the file picker, "open link in another app", and screen sharing work. It also exposes `RemoteDesktop` (synthetic keyboard/mouse for the whole session), `Camera` and `Location`. Those are gated by your desktop's own approval dialogs rather than by foxcage — and the `RemoteDesktop` prompt resembles the screen-share prompt, so read approval dialogs before accepting them. `xdg-dbus-proxy` has no "deny one interface" rule, so narrowing this means enumerating every interface Firefox needs; see `docs/DESIGN.md` for why that is not done by default
* All bind mounts (`profile`, `downloads_dir`, extra `[mounts] bind`) use `nosuid,noexec`
* Browser download verified against GPG signatures: Firefox against Mozilla's signed SHA-512 checksums, LibreWolf against the LibreWolf Maintainers detached signature plus sibling SHA-256. Verification is stricter than `gpg --verify`, which exits 0 for a signature made by a *revoked* key and for any key in the keyring. foxcage additionally requires that the signature chains to the pinned primary key, and refuses any release signed by a subkey its owner revoked as compromised — see [Revoked signing keys](#revoked-signing-keys)
* Ephemeral container (`--rm`) — filesystem writes are lost on exit
* No host devices (webcam, security keys, printers) passed through unless explicitly enabled

Each `[network]` and `[mounts]` option you enable trades some isolation for convenience. The defaults are the most restrictive configuration that still gives you a usable browser.

## Requirements

* Python 3.11+
* Podman (rootless)
* Wayland compositor (X11 is not supported)
* pasta (`sudo apt install passt`) — unless `network.mode = "host"`
* xdg-dbus-proxy (`sudo apt install xdg-dbus-proxy`)
* PulseAudio or PipeWire with PulseAudio compatibility (for audio)
* GPU with DRI support — optional; without `/dev/dri` foxcage warns and Firefox renders in software

Run foxcage as your normal desktop user, not as root or via `sudo` — the sandbox maps your user into the container, and running as root removes the isolation foxcage exists to provide. It refuses to start as root.

**Tested environment:** Debian 13 (Trixie) with GNOME 3. Other Linux distributions and Wayland compositors may work but have not been tested.

## Installation

foxcage is a single Python script with no dependencies outside the Python standard library. Copy it to a directory in your `PATH`:

root@kitploit:~

```
sudo cp foxcage /usr/local/bin/foxcage
```

Or for a user-local install:

root@kitploit:~

```
cp foxcage ~/.local/bin/foxcage
```

Make sure the script is executable (`chmod +x foxcage`).

Check which revision you have with `foxcage --version` — useful when reporting a problem, since foxcage is installed by copying a single file.

## Usage

root@kitploit:~

```
./foxcage
```

On first run the script bui...