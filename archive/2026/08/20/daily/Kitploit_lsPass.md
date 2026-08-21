---
title: lsPass
url: https://kitploit.com/en/tools/gitlab/leestripp/lspass
source: Kitploit
date: 2026-08-20
fetch_date: 2026-08-21T03:03:13.903047
---

# lsPass

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

[Tools](/en/tools)/![GitLab](/providers/gitlab.png)GitLab/leestripp/lspass

![](https://assets.kitploit.com/production/public/tools/50566/345ec7c9d9a5ed33554cf6140300c86b02141bf61dc8944af3c45097afca3199.png)

[Encryption/Decryption Tools](/en/categories/encryption-decryption-tools)[Cryptography](/en/categories/cryptography)[Privacy](/en/categories/privacy)[Identity & Access Management (IAM)](/en/categories/identity-access-management)

![GitLab](/providers/gitlab.png)leestripp/lspass

# lsPass

Local-first encrypted password manager for logins, notes, and API keys, using a SQLite vault sealed with Argon2id and XChaCha20-Poly1305; no cloud or telemetry.

[View Repository](https://gitlab.com/leestripp/lspass)

271 day ago![Not yet reviewed](/_next/image?url=%2Fbadges%2Fkitploit_badge_not_reviewed_full.png&w=48&q=75)

### Most Popular

[View all →](/en/tools)

Discover the most used tools by our community.

Last 7 DaysLast 30 Days

Explore all tools

Browse our collection of tools

[View all tools →](/en/tools)

Share

# lsPass — local, encrypted password manager

GTK4 / gtkmm-4 · C++23 · CMake · SQLite · libsodium

lsPass stores **logins, secure notes and API keys** in a local encrypted
vault. No network, no cloud, no telemetry. Nothing secret is ever written
to disk in plaintext.

## Build & test

root@kitploit:~

```
sudo apt install libgtkmm-4.0-dev libsqlite3-dev libsodium-dev nlohmann-json3-dev
cmake -B build
cmake --build build -j
ctest --test-dir build --output-on-failure   # 41 unit tests
./build/lspass
```

The vault lives at `~/.local/share/lspass/vault.db` (permissions `0600`).

## Debian/Ubuntu package

root@kitploit:~

```
cmake -B build-rel -DCMAKE_BUILD_TYPE=Release
cmake --build build-rel -j
cd build-rel && cpack -G DEB        # requires: dpkg-dev, file
sudo dpkg -i ../packages/deb/lspass_1.0.0_amd64.deb
```

The `.deb` lands in `packages/deb/` and ships the binary, a
`com.lspass.App.desktop` launcher entry, and the app icon
(`packaging/com.lspass.App.svg`, installed into the hicolor theme).

`cmake --install` without CPack uses the default `/usr/local` prefix. Runtime dependencies
(libgtkmm-4.0, libsodium, libsqlite3, …) are resolved automatically by
`dpkg-shlibdeps`, so `apt --fix-broken install` or `sudo apt install ./lspass_1.0.0_amd64.deb` pulls in everything needed.

## Security design (researched best practices)

Based on the OWASP Password Storage Cheat Sheet, the libsodium
documentation, and the envelope-encryption pattern used by established
password managers (Bitwarden, KeePassXC-style key wrapping):

root@kitploit:~

```
master password
      │  Argon2id  (memory-hard KDF, random 128-bit salt,
      ▼            opslimit/memlimit = libsodium "moderate",
    KEK (32 B)     parameters stored in vault for future upgrades)
      │  XChaCha20-Poly1305 (key wrap)
      ▼
    DEK (32 B, random)  ── wraps nothing else, RAM only, never on disk
      │  XChaCha20-Poly1305 AEAD per field
      ▼
SQLite: entries(title, username, url [plaintext metadata],
                secret, notes [sealed blobs: nonce‖ct‖poly1305 tag])
```

Why these choices:

| Decision | Rationale |
| --- | --- |
| **Argon2id** KDF | OWASP first choice for password-derived keys; memory-hard, resistant to GPU/ASIC cracking. Parameters exceed the OWASP minimum (m ≥ 19 MiB, t = 2). |
| **Envelope encryption** (random DEK wrapped by KEK) | Changing the master password only re-wraps 32 bytes instead of re-encrypting the whole vault; DEK compromise is impossible without the KEK. |
| **XChaCha20-Poly1305** AEAD | 192-bit random nonces make nonce reuse a non-issue; Poly1305 authenticates every ciphertext, so **a wrong master password is detected by authentication failure** — no password hash or verifier is stored anywhere. |
| **AAD binding** (`lspass:v1:entry:<id>:<field>`) | Ciphertexts cannot be transplanted between entries or fields by an attacker with write access to the DB file. |
| **Fresh nonce per write** | Every save re-seals with a new random nonce. |
| **Memory hygiene** | Keys live in `SecureBytes`, wiped with `sodium_memzero` on destruction; UI clears password fields immediately after use; clipboard auto-clears 30 s after copy (and only if it still holds our secret). |
| **File permissions** | Vault file is `chmod 0600`. |
| **Password generator** | Kernel CSPRNG with rejection sampling (no modulo bias), guarantees all enabled character classes, excludes ambiguous glyphs by default; ~128-bit entropy at the default 20 chars. |

**Honest trade-off:** `title`, `username` and `url` are stored as
plaintext so the list/search works without decrypting every row. The
secrets themselves (passwords, notes, API keys) are always sealed blobs.
The unit test `secrets_not_stored_in_plaintext` byte-scans the vault
file (incl. WAL) for a canary secret to prove this.

## Testing

`ctest` runs three suites (41 cases) against the GUI-independent core
library. The whole suite is also run under AddressSanitizer + UBSan:

root@kitploit:~

```
cmake -B build-san -DCMAKE_CXX_FLAGS="-fsanitize=address,undefined" \
      -DCMAKE_EXE_LINKER_FLAGS="-fsanitize=address,undefined"
cmake --build build-san -j && ctest --test-dir build-san
```

Release builds add `-fstack-protector-strong`, `-D_FORTIFY_SOURCE=2`,
PIE and full RELRO (`-Wl,-z,relro,-z,now`).

* **crypto** — AEAD round-trips, empty plaintext, truncated-blob rejection,
  wrong-key/tamper/AAD-mismatch rejection, nonce uniqueness, KDF
  determinism, salt & unicode-password handling, key wrap/unwrap,
  constant-time compare edge cases.
* **vault** — create/reopen, wrong-password rejection, CRUD, persistence,
  unicode + 100 KiB secrets, invalid-ID handling, no-plaintext canary
  scan, search, settings persistence, master-password change, tampered
  entry/header detection, corrupted KDF-parameter rejection.
* **generator** — length/charset guarantees incl. boundary lengths, class
  coverage, uniqueness, entropy estimate, passphrase format/bounds,
  invalid-option handling.

## Layout

root@kitploit:~

```
src/core/crypto.{hpp,cpp}     SecureBytes, Argon2id KDF, XChaCha20-Poly1305, key wrap
src/core/vault.{hpp,cpp}      SQLite vault, envelope encryption, CRUD
src/core/generator.{hpp,cpp}  CSPRNG password/passphrase generator
src/ui/                       gtkmm-4 UI (unlock screen, list, editor dialogs)
tests/                        ctest suites (no external framework needed)
```

## License

MIT — see [LICENSE](https://gitlab.com/leestripp/lspass/-/blob/main/LICENSE).

[Download Tool](https://gitlab.com/leestripp/lspass)