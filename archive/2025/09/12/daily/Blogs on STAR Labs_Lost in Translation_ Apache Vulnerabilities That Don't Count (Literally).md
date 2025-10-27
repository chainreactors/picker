---
title: Lost in Translation: Apache Vulnerabilities That Don't Count (Literally)
url: https://starlabs.sg/blog/2025/09-lost-in-translation-apache-vulnerabilities-that-dont-count-literally/
source: Blogs on STAR Labs
date: 2025-09-12
fetch_date: 2025-10-02T20:01:33.749934
---

# Lost in Translation: Apache Vulnerabilities That Don't Count (Literally)

[![logo](https://starlabs.sg/logo-white.png)](https://starlabs.sg/ "  (Alt + H)")

* [Home](https://starlabs.sg/ "Home")
* [About](https://starlabs.sg/about/ "About")
* [Advisories](https://starlabs.sg/advisories/ "Advisories")
* [Blog](https://starlabs.sg/blog/ "Blog")
* [Achievements](https://starlabs.sg/achievements/ "Achievements")
* [Publications](https://starlabs.sg/publications/ "Publications")
* [Search](https://starlabs.sg/search/ "Search (Alt + /)")

[Home](https://starlabs.sg/) » [Blogs](https://starlabs.sg/blog/)

# Lost in Translation: Apache Vulnerabilities That Don't Count (Literally)

September 11, 2025 · 9 min · Li Jiantao (@CurseRed)

Table of Contents

* [Vulnerability #1: Server-Side Request Forgery in Apache Pony Mail Foal](#vulnerability-1-server-side-request-forgery-in-apache-pony-mail-foal)
  + [Summary](#summary)
  + [Product Overview](#product-overview)
  + [Technical Details](#technical-details)
  + [Proof-of-Concept](#proof-of-concept)
  + [Suggested Mitigations](#suggested-mitigations)
* [Vulnerability #2: Remote Code Execution on whimsy.apache.org](#vulnerability-2-remote-code-execution-on-whimsyapacheorg)
  + [Summary](#summary-1)
  + [Technical Details](#technical-details-1)
  + [Proof of Concept](#proof-of-concept-1)

    * [`File.read("/etc/hosts")`](#filereadetchosts)
    * [`File.read("/proc/self/environ")`](#filereadprocselfenviron)
    * [`Dir['/srv/*']`](#dirsrv)
    * [`IO.read("|id;whoami;ifconfig;ip addr")`](#ioreadidwhoamiifconfigip-addr)
  + [Remediation Advice](#remediation-advice)
  + [Credits](#credits)

During our security research in 2024, we discovered several vulnerabilities in Apache Foundation projects that seem to have gotten ’lost in translation’ between our bug reports and the CVE assignment process. While we’ve been patiently waiting for these findings to officially ‘count,’ they’ve apparently been stuck longer than a software update on a Friday afternoon. Almost a year went by without any CVEs assigned and which we completely forgot about until now. So we figured it was time to let these vulnerabilities see the light of day, even if they’re destined to remain the security world’s ‘ones that got away.’ The following vulnerabilities were responsibly disclosed to Apache and have been addressed, though they continue to exist in that special category of bugs that are real enough to fix but without CVEs.

## Vulnerability #1: Server-Side Request Forgery in Apache Pony Mail Foal[#](#vulnerability-1-server-side-request-forgery-in-apache-pony-mail-foal)

### Summary[#](#summary)

A blind Server-Side Request Forgery vulnerability in Apache Pony Mail Foal allows an attacker to send limited crafted requests to the server, potentially resulting in unauthorized access to internal resources.

### Product Overview[#](#product-overview)

Apache Pony Mail Foal is a web-based mail archive browser built to scale to millions of archived messages with hundreds of requests per second. It allows you to browse, search, and interact with mailing lists including creating replies to mailing list threads. The project uses OAuth2 for authentication to allow viewing private lists, and uses ElasticSearch for storage and searching.

### Technical Details[#](#technical-details)

The OAuth2 endpoint allows users to specify an arbitrary URL in the `oauth_token` parameter, including internal URLs that are not normally accessible to the public. This allows for an attacker to send limited crafted POST requests to internal URLs, as well as GET requests if a URL that triggers a redirection is provided.
The vulnerable code is in `server/plugins/oauthGeneric.py`:

```
async def process(
    server: plugins.server.BaseServer, session: plugins.session.SessionObject, indata: dict,
) -> typing.Union[dict, aiohttp.web.Response]:

    debug(server, f"oauth/indata: {indata}")
    key = indata.get("key", "")
    state = indata.get("state")
    code = indata.get("code")
    id_token = indata.get("id_token")
    oauth_token = indata.get("oauth_token")

    rv: typing.Optional[dict] = None

    # Google OAuth - currently fetches email address only
    if key == "google" and id_token and server.config.oauth.google_client_id:
        rv = await plugins.oauthGoogle.process(indata, session, server)

    # GitHub OAuth - Fetches name and email
    elif key == "github" and code and server.config.oauth.github_client_id:
        rv = await plugins.oauthGithub.process(indata, session, server)

    # Generic OAuth handler, only one we support for now. Works with ASF OAuth.
    elif state and code and oauth_token:
        rv = await plugins.oauthGeneric.process(indata, session, server)

  if rv:
    # [...]

  return {"okay": False, "message": "Could not process OAuth login!"}
```

As can be seen from the code, if the `key` provided is not `google` or `github`, the oAuthgeneric plugin is called. The code for this is in `server/plugins/oauthGeneric.py`:

```
async def process(formdata: dict, _session, _server) -> typing.Optional[dict]:
    # Extract domain, allowing for :port
    # Does not handle user/password prefix etc
    m = re.match(r"https?://([^/:]+)(?::\d+)?/", formdata["oauth_token"])
    if m:
        oauth_domain = m.group(1)
        headers = {"User-Agent": "Pony Mail OAuth Agent/0.1"}
        # This is a synchronous process, so we offload it to an async runner in order to let the main loop continue.
        async with aiohttp.client.request("POST", formdata["oauth_token"], headers=headers, data=formdata) as rv:
            js = await rv.json() # [1]
            js["oauth_domain"] = oauth_domain
        return js
    return None
```

The `oauth_token` parameter is used to make a POST request to the URL provided, which may be an internal URL. As long as the request contains the mandatory parameters (key, state, code and oauth\_token), the server will make the request to the URL provided in the `oauth_token` parameter, including any other additional parameters provided in the POST data. While the response is not returned to the user, the attacker can still use this to trigger actions on the server, with the impact depending on which services are present on the internal network (see <https://github.com/assetnote/blind-ssrf-chains> for examples of potential exploitation scenarios).

Additionally, in our research, we discovered that if a URL that triggers a redirection is provided in the `oauth_token` parameter, the server will follow the redirection and make a GET request to the final URL. This can be used make GET requests to internal URLs in addition to POST requests and expands the attack surface. We found in particular that if the attacker knows the URL of the Elasticsearch instance used to store session data, it is possible to make repeated requests to the server to extract valid session identifiers through inference techniques (akin to a blind SQL injection attack), which can then be used to access the server as an authenticated user.

### Proof-of-Concept[#](#proof-of-concept)

Our proof-of-concept assumes that there is an Elasticsearch server at `localhost:9200` that is only accessible from the server running Pony Mail and is used to store data including session identifiers. Our exploit makes use of the following behaviour of Elasticsearch:

* It is possible to send GET requests of the form `http://localhost:9200/_sql?source_content_type=application/json&source={"query":"SQL_QUERY"}&format=txt` to the SQL server and get a response with a `text/html` content type
* If the SQL query causes an error, the response will have an `application/json` content type and will send an error message in JSON format

Pony Mail’s OAuth2 endpoint will simply return a 200 OK response with the message “Could not process OAuth login!” if the request is successful and contains JSON data, but will return a 500 Internal Server Error if the request returns non-JSON data (caused by the failure of the `rv.json()` call at [1] above). Thus, we can send requests with th...