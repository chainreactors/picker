---
title: Multiple vulnerabilities in CTFd versions <= 3.7.4
url: https://seclists.org/fulldisclosure/2024/Dec/21
source: Full Disclosure
date: 2025-01-01
fetch_date: 2025-10-06T20:12:06.633470
---

# Multiple vulnerabilities in CTFd versions <= 3.7.4

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

[![Previous](/images/left-icon-16x16.png)](20)
[By Date](date.html#21)
![Next](/images/right-icon-16x16.png)

[![Previous](/images/left-icon-16x16.png)](20)
[By Thread](index.html#21)
![Next](/images/right-icon-16x16.png)

![](/shared/images/nst-icons.svg#search)

# Multiple vulnerabilities in CTFd versions <= 3.7.4

---

*From*: Blazej Adamczyk <blazej.adamczyk () gmail com>
*Date*: Tue, 24 Dec 2024 12:28:40 +0100

---

```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Multiple vulnerabilities in CTFd versions <= 3.7.4
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

1 General information
═════════════════════

  Multiple vulnerabilities in CTFd versions <= 3.7.4 allows a remote
  attacker who acquired user’s activation or password reset link (e.g.
  from browser history) to hijack victim’s account. Other vulnerability
  allows the user to pass access control and change an already set
  bracket.

  Product name: CTFd

  Website: <https://ctfd.io>

  Product description: CTFd is a Capture The Flag framework focusing on
  ease of use and customizability. It comes with everything you need to
  run a CTF and it's easy to customize with plugins and themes.

2 [Vulnerability #1] User can change the bracket without administrator
══════════════════════════════════════════════════════════════════════

2.1 CVE
───────

  CVE-2024-11716

2.2 Affected versions
─────────────────────

  CTFd (<https://ctfd.io>) versions <= 3.7.4

2.3 CVSSv4
──────────

  5.3 Medium
  (CVSS:4.0/AV:N/AC:L/AT:N/PR:L/UI:N/VC:N/VI:L/VA:N/SC:N/SI:N/SA:N)

2.4 Description
───────────────

  CTFd offers scoreboard bracket function where users can be assigned to
  a bracket and are scoring is grouped by brackets. The function allows
  the user to pick a bracket once at start. It seems the logic's
  intention is to not allow the user to change the bracket when it was
  already assigned:

  ┌────
  │ 195  @pre_load
  │ 196  def validate_bracket_id(self, data):
  │ 197      bracket_id = data.get("bracket_id")
  │ 198      if bracket_id is None:
  │ 199          return
  │ 200
  │ 201      current_user = get_current_user()
  │ 202      if is_admin():
  │ 203          bracket = Brackets.query.filter_by(id=bracket_id, type="users").first()
  │ 204          if bracket is None:
  │ 205              ValidationError(
  │ 206                  "Please provide a valid bracket id", field_names=["bracket_id"]
  │ 207              )
  │ 208      else:
  │ 209          if (
  │ 210              current_user.bracket_id == int(bracket_id)
  │ 211              or current_user.bracket_id is None
  │ 212          ):
  │ 213              bracket = Brackets.query.filter_by(id=bracket_id, type="users").first()
  │ 214              if bracket is None:
  │ 215                  ValidationError(
  │ 216                      "Please provide a valid bracket id", field_names=["bracket_id"]
  │ 217                  )
  │ 218          else:
  │ 219              raise ValidationError(
  │ 220                  "Please contact an admin to change your bracket",
  │ 221                  field_names=["bracket_id"],
  │ 222              )
  └────
  Listing 1: CTFd/schemas/users.py

  Please note in lines 210-211 the code verifies if user has changed the
  bracket_id and if so raises an error stating that only administrator
  can do so.

  This validation suggests the system treats this as a security control
  and does not allow to switch brackets. Some setups/deployments might
  assume trust to this function.

  The user can however *bypass the check* by:
  1. First saving user details with bracket_id=null - GUI blocks this
     but API allows according to line 198. E.g.
     ┌────
     │ curl 'http://ctfd/api/v1/users/me'; --H 'Content-Type: application/json' \
     │      -H 'Content-Type: application/json' -H "CSRF-Token: $CSRF" \
     │       --data-raw '{"name":"test","email":"t () t pl","bracket_id":null,"fields":[]}'
     └────
  2. Second saving again with the proper changed bracket_id - this will
     be allowed according to line 211. This can be done normally in GUI.

2.5 PoC example
───────────────

  Some contests can use the scoreboard bracket system to group users
  into different prize pools. Having the possibility to change the
  bracket might end up with cheating and getting the prize.

2.6 Solution
────────────

  It should not be possible to change an already set bracket to null and
  this should be verified in the API (backend) OR (if the security
  control is simply wrong) there should be no ValidationError in order
  not to confuse CTFd implementers.

  Fixed in: <https://github.com/CTFd/CTFd/pull/2636>

3 [Vulnerability #2] Multiple vulnerabilities in token handling
═══════════════════════════════════════════════════════════════

3.1 CVE
───────

  CVE-2024-11717

3.2 Affected versions
─────────────────────

  CTFd (<https://ctfd.io>) versions <= 3.7.4

3.3 CVSSv4
──────────

  6.3 Medium
  (CVSS:4.0/AV:N/AC:L/AT:P/PR:N/UI:N/VC:N/VI:L/VA:N/SC:N/SI:N/SA:N)

3.4 Description
───────────────

3.4.1 [Vulnerability #2.1] Account activation and password reset tokens can be interchanged
╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌

  CTFd uses the "itsdangerous" python package for creating activation
  and password reset tokens. In both cases it is done by signing user's
  e-mail address with timestamp with the system's secret_key.

  The generated token is directly used in URL sent to the user over
  e-mail. During token validation, in both activation and password
  reset, the system is checking if the HMAC signature is correct and if
  the token was not created more than 1800s (30min) ago. Then the system
  verifies if the signed value matches any user's e-mail address. The
  matched user is being either activated or setting new password is
  being permitted.

  The tokens for both use cases have exactly the same construction and
  can be used interchangeably. Particularly, activation token can be
  used in reset password function which is pretty dangerous especially
  when the user registers and the token was used in GET request what
  means it can be stored in many places - browser's history, proxy
  access logs, and so on. An attacker gaining access to such token
  within the expiration time can use it to gain control of the victim's
  account.

  Connected with the vulnerability #3 the impact is even more visible as
  the token can be reused many times and cannot be revoked by the user
  until it expires.

3.4.2 [Vulnerability #2.2] Account activation and password reset tokens are not single-use
╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌

  The described above mechanism of token generation is stateless. This
  means tokens are not single-use and can be used withing the expiration
  timeout (30min) multiple times.

  Tokens sent in URL can be stored in many places - e-mail, browser's
  history, proxy access logs and so on. An attacker gaining access to
  such token within the expiration time can use it to gain control of
  the victim's account.

3.4.3 [Vulnerability #2.3] Email in token sent in GET requests
╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌

  The tokens for resetting password and activating account have base64
  encoded email address of the user in plain text. They are opened via
  GET requests which means can be stored in many places and thus may
  leak user's email address.

3.5 PoC example
──...