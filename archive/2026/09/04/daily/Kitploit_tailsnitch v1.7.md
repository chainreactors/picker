---
title: tailsnitch v1.7
url: https://kitploit.com/en/posts/github-adversis-tailsnitch-v17
source: Kitploit
date: 2026-09-04
fetch_date: 2026-09-05T06:28:11.169680
---

# tailsnitch v1.7

[Skip to content](#main-content)

[![Kitploit](/_next/image?url=%2Flogo.png&w=64&q=75)KITPLOIT](/en)[Tools](/en/tools)[Blog](/en/blog)Categories

EN

[Submit](/en/submit)

[Tools](/en/tools)[Blog](/en/blog)Categories

[Submit](/en/submit)

EN

Hacking, PenTest, and Cybersecurity Tools for Your Security Arsenal!

[Back to updates](/en/updates)

![](https://assets.kitploit.com/production/public/tools/10492/e530f0552352cfe9de08d31f65a656b97264d4e5c7641c48ae6535934db0033c.png)

New releaseSep 4, 2026

# tailsnitch v1.7

A security auditor for Tailscale configurations. Scans your tailnet for misconfigurations, overly permissive access controls, and security best practice violations.

Share

# Tailsnitch

A security auditor for Tailscale configurations. Tailsnitch scans your tailnet for 57 misconfigurations, overly permissive access controls, and security best practice violations.

## Quick Start

root@kitploit:~

```
# 1. Set your Tailscale API credentials
export TS_API_KEY="tskey-api-..."

# 2. Run audit
tailsnitch

# 3. See only high-severity findings
tailsnitch --severity high

# 4. Fix some issues  ~interactively~ yolo mode
tailsnitch --fix
```

## Installation

### Download Pre-built Binary

Download the latest release from [GitHub Releases](https://github.com/Adversis/tailsnitch/releases).

**macOS users:** Remove quarantine attribute after download:

root@kitploit:~

```
sudo xattr -rd com.apple.quarantine tailsnitch
```

### Install via Go

root@kitploit:~

```
go install github.com/Adversis/tailsnitch@latest
```

### Build from Source

root@kitploit:~

```
git clone https://github.com/Adversis/tailsnitch.git
cd tailsnitch
go build -o tailsnitch .
```

## Authentication

Tailsnitch supports two authentication methods. OAuth is preferred when both are configured.

### Option 1: OAuth Client (Recommended)

OAuth clients provide scoped, auditable access that doesn't expire when employees leave.

root@kitploit:~

```
export TS_OAUTH_CLIENT_ID="..."
export TS_OAUTH_CLIENT_SECRET="tskey-client-..."
```

Create an OAuth client at: <https://login.tailscale.com/admin/settings/oauth>

**Required scopes for read-only audit:**

`all:read` covers everything. Granting scopes individually:

| Scope | Used for |
| --- | --- |
| `policy_file:read` | Tailnet policy file — ACL-*, NET-*, SSH-\* |
| `devices:core:read` | Device list — DEV-*, NET-*, ACL-011 |
| `dns:read` | DNS configuration — DNS-001, DEV-007 |
| `auth_keys:read` | Machine auth keys — AUTH-\*, ACL-011 |
| `feature_settings:read` | Tailnet settings — DEV-008, DEV-009, DEV-014 |
| `logs:network:read` | Network flow logging setting — LOG-001 |
| `networking_settings:read` | HTTPS certificate setting — NET-004 |
| `log_streaming:read` | Log stream destinations — LOG-002 |
| `webhooks:read` | Webhook endpoints — LOG-005, LOG-012 |
| `oauth_keys:read` | OAuth clients — LOG-006 |
| `users:read` | User roles and status — USER-001, LOG-006 |
| `account_settings:read` | Security contact — LOG-011 |
| `devices:posture_attributes:read` | Posture integrations — DEV-014 |

Any scope you leave out only affects the checks that need it: those
checks report that they could not read the setting rather than passing.

AUTH-005 and AUTH-006 read the tailnet's federated identities, which the admin
console calls trust credentials. They arrive from the same keys listing as auth
keys, so `auth_keys:read` is expected to cover them. That has not been confirmed
against a live tailnet. If the keys listing cannot be read, both checks report
not evaluated rather than passing. Whether a missing scope returns an error or
instead returns the listing with the identities filtered out is unconfirmed; if
it filters silently, AUTH-005 would report that no trust credentials exist and
AUTH-006 would find nothing to check.

**Additional scopes for fix mode:**

* `devices:core` - Delete devices, modify tags (requires tag selection)
* `auth_keys` - Delete auth keys

### Tailnet Lock

DEV-010 and DEV-012 report on Tailnet Lock, which the Tailscale API does not
expose as a tailnet setting. Devices locked out by it are visible through the
API, but determining whether lock is enabled needs the local `tailscale` CLI,
which reads the daemon on the machine running tailsnitch. When auditing another
tailnet with `--tailnet`, treat that part of the result accordingly. Use
`--tailscale-path` if the binary is in a non-standard location.

### Option 2: API Key

API keys operate as the user who created them and inherit that user's permissions.

root@kitploit:~

```
export TS_API_KEY="tskey-api-..."
```

Create an API key at: <https://login.tailscale.com/admin/settings/keys>

## Usage Examples

### Basic Audit

root@kitploit:~

```
# Run full audit
tailsnitch

# Show passing checks too (verbose)
tailsnitch --verbose

# Output as JSON for processing
tailsnitch --json

# Audit a specific tailnet (when OAuth client has access to multiple)
tailsnitch --tailnet mycompany.com
```

### Filter Results

root@kitploit:~

```
# Only show critical and high severity issues
tailsnitch --severity high

# Filter by category
tailsnitch --category access    # ACL issues
tailsnitch --category auth      # Authentication & keys
tailsnitch --category device    # Device security
tailsnitch --category network   # Network exposure
tailsnitch --category ssh       # SSH rules
tailsnitch --category log       # Logging & admin

# Run specific checks only
tailsnitch --checks ACL-001,AUTH-001,DEV-010
tailsnitch --checks stale-devices,tailnet-lock-not-enabled

# List all available checks
tailsnitch --list-checks
```

### Interactive Fix Mode

Fix mode allows you to remediate issues directly via the Tailscale API:

root@kitploit:~

```
# Interactive fix mode
tailsnitch --fix

# Preview what would be fixed (dry run)
tailsnitch --fix --dry-run

# Auto-select safe fixes (still requires confirmation)
tailsnitch --fix --auto

# Disable audit logging of fix actions
tailsnitch --fix --no-audit-log
```

**API-fixable items:**

| Check | Action |
| --- | --- |
| AUTH-001, AUTH-002, AUTH-003 | Delete auth keys |
| DEV-002 | Remove tags from user devices |
| DEV-004 | Delete stale devices |
| DEV-005 | Authorize pending devices |

Fix mode also provides direct links to the admin console for issues that require manual intervention.

### SOC 2 Evidence Export

Generate evidence reports for SOC 2 audits with Common Criteria (CC) control mappings:

root@kitploit:~

```
# Export as JSON
tailsnitch --soc2 json > soc2-evidence.json

# Export as CSV (for spreadsheets)
tailsnitch --soc2 csv > soc2-evidence.csv
```

The SOC 2 report includes:

* Per-resource test results (each device, key, ACL rule tested individually)
* CC code mappings (CC6.1, CC6.2, CC6.3, CC6.6, CC7.1, CC7.2, etc.)
* Pass/Fail/N/A status for each control test
* Timestamp for audit trail

**Example CSV output:**

root@kitploit:~

```
resource_type,resource_id,resource_name,check_id,check_title,cc_codes,status,details,tested_at
device,node123,prod-server,DEV-001,Tagged devices with key expiry disabled,CC6.1;CC6.3,PASS,Tags: [tag:server] key expiry enabled,2025-01-05T10:30:00Z
key,tskey-auth-xxx,tskey-auth-xxx,AUTH-001,Reusable auth keys exist,CC6.1;CC6.2;CC6.3,FAIL,Reusable key expires in 45 days,2025-01-05T10:30:00Z
```

### Ignore Known Risks

Create a `.tailsnitch-ignore` file to suppress findings for known-accepted risks:

root@kitploit:~

```
# .tailsnitch-ignore
# Ignore informational checks
ACL-008  # We intentionally don't use groups
ACL-009  # Legacy ACLs are fine for our use case

# Ignore specific medium checks with justification
DEV-006  # External devices are approved contractors
LOG-001  # Flow logs require Enterprise plan

# Ignore one item within a check, instead of muting the whole check
ACL-011:tag:monitoring  # broad by design; every other tag is still checked
AUTH-001:tskey-auth-xxxx  # rotates automatically via CI, tracked in TICKET-123
```

A line names either a whole check (`ACL-011`) or one item within it
(`CHECK-ID:it...