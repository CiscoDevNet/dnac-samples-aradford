import os
DNAC=os.getenv("DNAC") or "sandboxdnac.cisco.com"
# NOTE port 8080 is only required if you are using sandboxdnac and want to use POST/DELETE as the devnetuser is RO
# the POST/DELETE url are restricted.

DNAC_PORT=os.getenv('DNAC_PORT') or 8080
DNAC_USER=os.getenv("DNAC_USER") or "devnetuser"
DNAC_PASSWORD=os.getenv("DNAC_PASSWORD") or "Cisco123!"