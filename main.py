
from unpaywall import unpaywall_utils

CLIENT_EMAIL = "example@company.org"
DOI = "10.4304/jnw.3.2.38-47"

if unpaywall_utils.checkIfDOIIsOpenAccess(DOI, CLIENT_EMAIL):
    print("DOI " + DOI + " is available as Open Access")
    url = unpaywall_utils.getOpenAccessURLForDOI(DOI, CLIENT_EMAIL)
    if url:
        print("An open access version of this publication is available at " + url)
else:
    print("DOI " + DOI + " is not available as Open Access")
