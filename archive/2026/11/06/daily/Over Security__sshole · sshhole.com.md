---
title: *sshole · sshhole.com
url: https://sshhole.com/
source: Over Security
date: 2026-11-06
fetch_date: 2026-11-07T08:01:57.832178
---

# *sshole · sshhole.com

# \*sshole

so openssh on musl linux (alpine, openwrt, buildroot, yocto, and a lot of the docker images you've pulled) has had a little problem since 2016.

accounts that should never take a password at all (root, your key-only deploy user, ldap users, the default user on alpine's aws and azure images) take any password longer than 256 characters.

yes, any password. yes. i know. yes.

1. 1980the first star
2. 1990sthe password check
3. 1990sthe fine print
4. 2012crypt stops saying NULL
5. 2012the 256-byte cap
6. 2016bob's salt
7. 2019the fix for the fix
8. 2024ten quiet years
9. 2026how i ran into it

1980

## the first star

back in old unix your password hash just sat in `/etc/passwd`, right next to your username. in a file everyone could read.

in 1980 bill joy put a `*` there for an account called `daemon`. nobody's supposed to ever log in as it.

a `*` isn't a hash, so no password can match it. unix still does this today

[3bsd · /etc/passwd · 1980

**Address**github.com/dspinellis/unix-history-repo/blob/BSD-3/etc/passwd

![daemon:*:1:1:The devil himself:/:](receipts/3bsd-passwd.png)](https://github.com/dspinellis/unix-history-repo/blob/BSD-3/etc/passwd)

the next field is the real name. he wrote "the devil himself"

1990s

## how sshd checks your password

ok so these days the hash lives in `/etc/shadow` and looks like `$6$abc$k2P9…`. the `$6$` means sha512, `abc` is the salt, the rest is the actual hash

you type your password, sshd hashes it with that same salt and checks if it comes out identical. same = you're in. that's it

and if the field is just `*`? there's nothing to match. type whatever you want, it's never getting you in

1990s

## the fine print

one more rule. if `crypt()` can't do its job, it returns NULL. like if the salt asks for some algorithm the system doesn't have, there's nothing to compute, so you get NULL instead of a hash

[the single unix spec · crypt() · 1997

**Address**pubs.opengroup.org/onlinepubs/7908799/xsh/crypt.html

![RETURN VALUE: Upon successful completion, crypt() returns a pointer to the encoded string. Otherwise it returns a null pointer and sets errno to indicate the error.](receipts/posix-crypt.png)](https://pubs.opengroup.org/onlinepubs/7908799/xsh/crypt.html)

pretty clear.

except a lot of programs never check for NULL. they just compare whatever `crypt()` gives back with the stored field, hit the NULL, and crash

2012

## crypt stops saying NULL

so musl (the libc under alpine) goes ok fine, `crypt()` just won't return NULL anymore. if it fails, it returns a single character instead. that character can never match a real password, so programs don't crash, they just see a wrong password

now guess which character they picked for that

"?"

yep. the star. again.

[musl · b3c4cc12 · aug 2012

**Address**git.musl-libc.org/cgit/musl/commit/?id=b3c4cc12

![make crypt return an unmatchable hash rather than NULL on failure. always "succeeding" but giving an unmatchable hash is reportedly a better behavior than failing on error.](receipts/musl-b3c4cc12.png)](https://git.musl-libc.org/cgit/musl/commit/?id=b3c4cc121f70faea45389fe7ddc1127ed5cbd8bb)

"reportedly."

[musl · b3c4cc12 · the diff

**Address**git.musl-libc.org/cgit/musl/commit/?id=b3c4cc12

![diff of crypt_des.c: removed the comment 'Should not happen.' and 'return NULL;', added: return (setting[0]=='*') ? "x" : "*";](receipts/musl-b3c4cc12-diff.png)](https://git.musl-libc.org/cgit/musl/commit/?id=b3c4cc121f70faea45389fe7ddc1127ed5cbd8bb)

"should not happen" gone, NULL gone, `"*"` in

2012

## three weeks later

then musl adds sha512 crypt. the thing is, sha512crypt gets slower the longer the password is, so someone could send one giant password and keep your server busy for a long time. so musl just caps it at 256 bytes and refuses anything longer

[musl · 88bf5a8a · aug 29 2012

**Address**git.musl-libc.org/cgit/musl/commit/?id=88bf5a8a

![add sha256/sha512 crypt. Rich Felker, 2012-08-29.](receipts/musl-88bf5a8a.png)](https://git.musl-libc.org/cgit/musl/commit/?id=88bf5a8a8d7d796f63cca8589f4de67aa8345f1a)

twenty days after the "\*" commit btw

[musl · crypt\_sha512.c @ 88bf5a8a

**Address**git.musl-libc.org/cgit/musl/tree/src/misc/crypt\_sha512.c?id=88bf5a8a

![key limit is not part of the original design, added for DoS protection. #define KEY_MAX 256. if (i > KEY_MAX) return 0;](receipts/musl-keymax.png)](https://git.musl-libc.org/cgit/musl/tree/src/misc/crypt_sha512.c?id=88bf5a8a8d7d796f63cca8589f4de67aa8345f1a#n189)

so past 256 bytes crypt fails. and when crypt fails… it says `"*"`.

[musl · crypt\_sha512.c

**Address**git.musl-libc.org/cgit/musl/tree/src/crypt/crypt\_sha512.c

![on error "*" is returned.](receipts/musl-sha512-header.png)](https://git.musl-libc.org/cgit/musl/tree/src/crypt/crypt_sha512.c#n8)

literally in the comment the whole time

2016

## sshd borrows bob's salt

CVE-2016-6210. ask sshd about a user that doesn't exist and it says no instantly, cause there's nothing to hash. real users take a few ms longer. so just time it and you know who exists

the fix is kinda funny. no real hash to check? sshd grabs some other account's salt and hashes your password anyway, just to waste the same amount of time. still a no, just a slower no

[openssh-commits · jul 2016

**Address**lists.mindrot.org/pipermail/openssh-commits/2016-July/005428.html

![Determine appropriate salt for invalid users.](receipts/openssh-9286875a7.png)](http://lists.mindrot.org/pipermail/openssh-commits/2016-July/005428.html)

"for invalid users." and also, it turns out, real users with a `*`.

2019 → 2022

## the fix for the fix

**2019.** turns out alpine's docker images had no root password. at all. CVE-2019-5021. alpine fixes it by locking root with `!`

but without pam, `!` also kills ssh keys. and cloud images log in with keys.

**2022.** alpine 3.16 switches root to `*`. still locked, keys work again

[alpine aports · fbe926af · shipped in 3.16, 2022

**Address**gitlab.alpinelinux.org/alpine/aports/-/commit/fbe926af.patch

![this still forbids password login but allows logins via ssh keys with pam disabled. # make sure root login is disabled. root:! becomes root:*](receipts/alpine-fbe926af.png)](https://gitlab.alpinelinux.org/alpine/aports/-/commit/fbe926afc76de76e07d078f266badc4144dde8e3)

narrator: it did not.

2016 → 2026

## ten quiet years

why did nobody notice? well, maybe someone did. maybe someone pasted the wrong thing into a password prompt, half a slack message or a whole ssh key, and it just let them in. you've never pasted the wrong thing into a password prompt?? amazing. a fresh box with no passwords set isn't affected. a `*` in shadow needs a wrong try first. openssh tests on openbsd and glibc, musl doesn't test sshd, and most distros go through pam, which never even calls crypt for a `*`.

so as far as anyone knows, nobody noticed. as far as anyone knows.

some people got really close though

[libc-alpha · debian #714219 · 2013

**Address**sourceware.org/legacy-ml/libc-alpha/2013-07/msg00046.html

![The scheme of returning * or x, which are never valid matches, comes from dalias from musl, and I think it is the best compromise/solution.](receipts/libc-alpha-2013.png)](https://bugs.debian.org/714219)

a debian dev asks glibc to copy musl's `"*"`. six years later debian moves to libxcrypt, which says `"*0"`, and closes the bug. one character away.

[musl mailing list · dec 2024

**Address**openwall.com/lists/musl/2024/12/31/2

![Sure there's no reason it couldn't have been 257 or 300 or whatever, but either way you'd get things like this when software has bugs in handling the condition.](receipts/musl-list-2024.png)](https://www.openwall.com/lists/musl/2024/12/31/2)

this thread is about busybox `passwd` breaking on a 257 character password. same `"*"`, same limit. nobody says "sshd"

[openssh-commits · 30 oct 2026

**Address**lists.mindrot.org/pipermail/openssh-commits/2026-October/013271.html

![fix fake password salt generation for bc...