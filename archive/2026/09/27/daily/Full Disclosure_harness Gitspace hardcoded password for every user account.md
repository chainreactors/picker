---
title: harness Gitspace hardcoded password for every user account
url: https://seclists.org/fulldisclosure/2026/Sep/83
source: Full Disclosure
date: 2026-09-27
fetch_date: 2026-09-28T07:56:59.216672
---

# harness Gitspace hardcoded password for every user account

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

[![Previous](/images/left-icon-16x16.png)](82)
[By Date](date.html#83)
[![Next](/images/right-icon-16x16.png)](71)

[![Previous](/images/left-icon-16x16.png)](82)
[By Thread](index.html#83)
[![Next](/images/right-icon-16x16.png)](71)

![](/shared/images/nst-icons.svg#search)

# harness Gitspace hardcoded password for every user account

---

*From*: Khashayar Fereidani <info () fereidani com>
*Date*: Thu, 24 Sep 2026 14:42:12 +0000

---

```
# harness Gitspace hardcoded password for every user account

**Author:** Khashayar Fereidani
**Disclosure Date:** 2026-09-24
**Advisory:** https://fereidani.com/harness-gitspace-hardcoded-password-for-every-user-account
**Contact:** https://fereidani.com/contact

## Description

Gitspaces are Harness's hosted development environments: a container with
the user's source tree, running an SSH server and an IDE, with its ports
published on the host machine. Access is supposed to be controlled by a
secret the user configures. In practice the password of the Linux account
inside every Gitspace container is the same public constant,
`app/gitspace/secret/password_resolver.go:26`:

```go
const defaultPassword = "Harness@123"

func (p *PasswordResolver) Resolve(_ context.Context, _
ResolutionContext) (ResolvedSecret, error) {
return ResolvedSecret{
SecretValue: defaultPassword,
}, nil
}
```

`Resolve` discards the entire `ResolutionContext`, parameter by parameter.
The caller does pass the configured reference: `ResolveSecret` builds the
context with `SecretRef: *config.GitspaceInstance.AccessKeyRef`
(`app/gitspace/orchestrator/utils/secret.go:46`), but the resolver never
reads it, so the user's choice of secret is ignored and the value cannot be
rotated per instance. The wire set registers exactly this one resolver
(`app/gitspace/secret/wire.go:20`), so every password-type resolution in the
product returns the constant.

The resolved value becomes the account password inside the container. On
resume, the orchestrator stores it
(`app/gitspace/orchestrator/orchestrator_resume.go:50`) and the user setup
script applies it (`manage_user.sh` under
`app/gitspace/orchestrator/utils/script_templates/`, line 49):

```sh
elif [ "user_credentials" = "$accessType"  ] ; then
    echo "$username:$accessKey" | chpasswd
```

The constant ships in the public repository, so it is known to anyone who
has read the source, and it is identical in every deployment, every release
image and every Gitspace instance. The `ssh_key` branch of the same script
writes the resolved value into `authorized_keys`
(`manage_user.sh:43-46`); since that value is also the constant, that access
type simply does not work, which is further proof that the configured
reference is never honored.

## Reproduction

The resolver can be exercised directly. This in-package test asks it to
resolve a configured secret reference:

```go
package secret

import (
"context"
"testing"
)

func TestPocHardcodedPassword(t *testing.T) {
resolved, err := (&PasswordResolver{}).Resolve(context.Background(),
ResolutionContext{
UserIdentifier:     "victim",
GitspaceIdentifier: "gs-1",
SecretRef:          "my-configured-secret-ref",
SpaceIdentifier:    "space1",
})
if err != nil {
t.Fatal(err)
}
t.Logf("Resolve(SecretRef=%q) = %q", "my-configured-secret-ref",
resolved.SecretValue)
if resolved.SecretValue != "Harness@123" {
t.Fatalf("expected the shipped constant, got %q", resolved.SecretValue)
}
}
```

Observed output on main at commit 912a1f3:

```text
--- PASS: TestPocHardcodedPassword (0.00s)
    poc_password_test.go:18:
Resolve(SecretRef="my-configured-secret-ref") = "Harness@123"
```

With a running deployment the account is then usable directly. Gitspace
ports are published as host port bindings
(`app/gitspace/orchestrator/container/devcontainer_container_utils.go:281`),
and the account name is the Gitspace owner's identifier
(`config.GitspaceUser.Identifier` in the same plumbing), so anyone who can
reach the published SSH port logs in with the public constant:

```sh
ssh <owner-identifier>@<gitspace-host> -p <published-port>
# password: Harness@123
```

## Impact

Use of a hard-coded password (CWE-798, CWE-259). An attacker who can reach
a Gitspace's published SSH or IDE endpoint gets the owner's full
environment: the source tree, any git credentials and tokens present in the
container, and the network position of the development sandbox. There is no
per-instance secret to stop them, because the value is universal, public in
the source repository, and cannot be changed through configuration since
the resolver ignores the reference. Anyone who has ever read the source, or
any attacker who obtained the constant from any other deployment, holds a
valid password for every Gitspace account in every Harness open source
installation.

## Solution

Make the resolver earn its name. Two workable directions, in order of
preference:

- Honor the configured reference. The codebase already defines the seam:
  `PlatformSecret.FetchSecret(ctx, secretRef, spacePath)`
  (`app/gitspace/platformsecret/platformsecret.go:23`). Its only
  implementation currently ignores both the reference and the space path and
  returns its input masked (`gitnessplatformsecret.go:31`), so wire it to
  the existing secret service and have `PasswordResolver.Resolve` read
  `ResolutionContext.SecretRef` through it. Users can then set and rotate
  the real password as a proper secret.
- Or drop shared passwords entirely: generate a random per-instance
  password with `crypto/rand` at Gitspace start and hand it to the owner
  through the control plane (the API or the IDE session), never storing a
  constant in the repository.

Either way, a resolver that cannot produce a real secret should return an
error, not a known constant. Until a fix lands, treat every published
Gitspace port as a pre-authenticated login for the owner account: keep the
ports off public networks (firewall, VPN or bind them to loopback with an
authenticated tunnel in front), because no configuration change inside the
product can change the password.

## Timeline

- 2026-09-24: Reported publicly as harness/harness#3725, found while
  scanning popular repositories with my static analyzer. The project's
  earlier security reports had gone unanswered; the current main branch
  (912a1f3) is affected.

## References

- [harness/harness#3725 - hardcoded password Harness@123 for every
gitspace user account](https://github.com/harness/harness/issues/3725)
- [harness/harness -
app/gitspace/secret/password_resolver.go](https://github.com/harness/harness/blob/main/app/gitspace/secret/password_resolver.go)
- [harness/harness -
app/gitspace/orchestrator/utils/script_templates/manage_user.sh](https://github.com/harness/harness/blob/main/app/gitspace/orchestrator/utils/script_templates/manage_user.sh)
- [harness/harness -
app/gitspace/platformsecret/platformsecret.go](https://github.com/harness/harness/blob/main/app/gitspace/platformsecret/platformsecret.go)
- [CWE-798: Use of Hard-coded
Credentials](https://cwe.mitre.org/data/definitions/798.html)
- [CWE-259: Use of Hard-coded
Password](https://cwe.mitre.org/data/definitions/259.html)
_______________________________________________
Sent through the Full Disclosure mailing list
https://nmap.org/mailman/listinfo/fulldisclosure
Web Archives & RSS: https://seclists.org/fulldisclosure/
```

---

[![Previous](/images/left-icon-16x16.png)](82)
[By Date](date.html#83)
[![Next](/images/right-icon-16x16.png)](71)

[![Previous](/images/left-icon-...