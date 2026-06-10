---
title: Securing API Keys on Your Workstation
url: https://zeltser.com/securing-api-keys-on-your-workstation
source: Lenny Zeltser
date: 2026-06-09
fetch_date: 2026-06-10T06:17:13.150577
---

# Securing API Keys on Your Workstation

[Lenny Zeltser](/)Security builder & leader

 [Projects](/projects) [Writing](/writing) [About](/about)

×

# Securing API Keys on Your Workstation

Every dev tool you grant API access to, AI assistants included, can read the keys within its reach. No setup removes that risk entirely, so the goal is fewer secrets exposed and less damage when one leaks.

![Securing API Keys on Your Workstation - illustration](/assets/securing-api-keys-on-your-workstation.DZEN6qaS_Z11S7ob.webp)

Developer workstations accumulate API keys and other secrets that malware can read from .env files, shell history, and saved CLI credentials. An infostealer only has to steal the key, and using it skips the second authentication factor a person would need. AI agents increase the risk, since they generally require broad access to be useful.

For example, attackers behind the [s1ngularity attack](https://blog.gitguardian.com/the-nx-s1ngularity-attack-inside-the-credential-leak/) compromised *nx*, a popular JavaScript build tool, and pulled API keys and SSH keys from over a thousand developer machines. The attackers also weaponized developers’ AI coding agents, [prompting installed CLIs](https://www.wiz.io/blog/s1ngularity-supply-chain-attack) to comb the filesystem for secrets.

Several free open-source tools can help reduce the number of secrets you leave exposed and limit the damage when one of them leaks.

## Start by seeing what’s already exposed.

Before you change anything, scan your workstation to learn where secrets already live. A good starting point is [bagel](https://github.com/boostsecurityio/bagel), which reports secrets and insecure settings across your system, including AI tool credential files, cloud keys, and unsafe Git or SSH configurations.

For secrets already committed to Git, a verifying scanner such as [TruffleHog](https://github.com/trufflesecurity/trufflehog) can not only locate the access keys but also test them against the provider to determine whether they still work.

Your first scan will probably find more secrets than you remember creating. Re-run it after each cleanup step to confirm the count drops.

## Aim for four reachable wins.

Your tools need access to the API keys and tokens to do their job, so reduce both the chances they’re abused and the damage when one leaks. To do that:

* Keep secrets out of plaintext files.
* Stop them from spreading into Git and logs.
* Require your approval before a sensitive key gets used.
* Minimize the damage if a key leaks.

Your exposure and convenience depend on where you put your secrets, so let’s start there.

## Weigh exposure against convenience.

You can keep a secret in several places, from a plaintext file to a vault that prompts you each time. More protection usually means less convenience, so the right store depends on the key’s sensitivity, what you’re defending against, and how much inconvenience you’re willing to tolerate.

A secret’s exposure in a store is based on two factors:

* Whether software running as you can read it without your approval, and
* How many other secrets an attacker gets by compromising that store.

The table below rates the store options on both, so you can pick the approach that works for you.

| Approach | Silent read by malware running as you? | Blast radius of one compromise | Automation / headless | Key tradeoff |
| --- | --- | --- | --- | --- |
| **Plaintext File (e.g., .env)** | Yes | The keys in that file | Works everywhere | Most leaks start here |
| **OS Keychain** | Yes, while unlocked | That store’s items | Good, auto-unlocked | Once unlocked, code running as you can read it, with a per-item prompt on macOS |
| **Password Vault (e.g., 1Password)** | No, each use needs approval | The whole authorized account | Poor, needs a person to approve | One approval, or an open session, exposes the account |
| **Scoped Password Vault** | No | Only that one vault | Poor, still interactive | Needs an extra limited identity to set up |
| **Service Account** | The token sits at rest | Only its granted vaults | Good, non-interactive | The token unlocks everything in its scope |

## The OS keychain is convenient but stays unlocked.

If you’re not sure where to start, the OS keychain is a good default, since infostealers often focus on plaintext files. Every major desktop platform includes one:

* **macOS:** The [macOS Keychain](https://support.apple.com/guide/keychain-access/welcome/mac), driven by the [security](https://keith.github.io/xcode-man-pages/security.1.html) command.
* **Windows:** [Credential Manager](https://support.microsoft.com/en-us/windows/accessing-credential-manager-1b5c916a-6a16-889f-8581-fc16e8165ac0), via [cmdkey](https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/cmdkey).
* **Linux:** The [Secret Service](https://specifications.freedesktop.org/secret-service-spec/latest/), via [secret-tool](https://man.archlinux.org/man/secret-tool.1.en).

The keychain is unlocked the entire time you’re logged in, which is both convenient and risky. The convenience is that your tools read a key without prompting you, even ones running in the background or headless. Your system usually unlocks it at login and holds it open for the session, so code running as you can read the keys it stores. On Windows and Linux, that code reads the store without prompting. macOS adds a per-item prompt when an app tries to access something it didn’t store, though there are ways around it. A file scraper still finds nothing, but code that reads the keychain directly gets the key.

## Getting the secret to a tool is its own task.

How you deliver a secret depends on how the tool is started. If you start the tool yourself, you can inject the secret as you launch it. A tool that another program spawns or runs headless needs an auto-unlocked store or a lookup at the moment of use.

You can get the secret to a tool in three ways:

* You look it up at the moment of use, for example, using `security find-generic-password` or 1Password’s `op read`.
* You inject it into the tool’s environment when you launch the tool.
* The tool reads it from its own config file, where you’ve replaced the secret with an environment variable reference.

You can use these methods with any store you choose.

## A password vault adds a per-use checkpoint.

For the few sensitive keys you want to approve each time, use a vault such as 1Password instead of the OS keychain. Unlike the keychain, 1Password asks for your biometric approval at the moment a tool needs the key, and caches it only for a short session. You replace the literal key with a 1Password [secret reference](https://www.1password.dev/cli/secret-references) in a config or env file, and 1Password’s CLI resolves it to the value when a tool needs it.

The downside of using 1Password is that once you [give the tool access](https://developer.1password.com/docs/cli/app-integration-security/), it can read all data stored in your 1Password account, not just the secret you have in mind. As a result, if you or your AI tool is tricked into requesting access, you might inadvertently give the requesting software access to a lot of sensitive data.

To lower your exposure, consider creating a 1Password vault just for the secrets you use for your dev work. Then, create a limited 1Password identity with access restricted to that one vault. Cleanly doing that requires a [service account](https://developer.1password.com/docs/service-accounts/) that’s available only to 1Password business customers. You can mimic this approach using a [guest account](https://support.1password.com/guests/) on a personal plan.

On a personal plan, the guest route needs one more step. You need to turn off the app’s biometric CLI integration and [sign in](https://www.1password.dev/cli/sign-in-manually/) as the guest from the terminal. Signing in manually requires a password for the guest account and doesn’t work with 1Password biometric authentication.

For a hybrid appro...