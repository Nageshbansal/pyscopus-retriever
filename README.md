
<!-- README.md is generated from README.Rmd. Please edit that file -->

Python Package to interface with Elsevier and Scopus APIs for retreival of articles/journals text




## Steps to get API key

In order to use this package, you need an API key from
<https://dev.elsevier.com/sc_apis.html>. You should login from your
institution and go to Create API Key. You need to provide a website URL
and a label, but the website can be your personal website, and agree to
the terms of service.

1.  Go to <https://dev.elsevier.com/user/login>. Login or create a free
    account.
2.  Click “Create API Key”. Put in a label, such as `rscopus key`. Add a
    website. <http://example.com> is fine if you do not have a site.
3.  **Read** and agree to the TOS if you do indeed agree.




You should be able to test out the API key using the [interactive Scopus
APIs](https://dev.elsevier.com/scopus.html).

### A note about API keys and IP addresses

The API Key is bound to a set of IP addresses, usually bound to your
institution. Therefore, if you are using this for a Shiny application,
you must host the Shiny application from your institution servers in
some way. Also, you cannot access the Scopus API with this key if you
are offsite and must VPN into the server or use a computing cluster with
an institution IP.

See <https://dev.elsevier.com/tecdoc_api_authentication.html>

## Example

This is a basic example which shows you how to solve a common problem:

``` python
from pyscopus import get_doi

doi = get_doi(api_key, query = "ALL( "ecology" AND "crown trees")", start_date = 01-2015, end_date=02-2016)
print(doi)

>> 10.1038/s41598-022-06383-5
10.1016/j.jobe.2022.104755
10.1016/j.energy.2022.124399
10.1007/s10661-022-10172-y
10.1016/j.rser.2022.112507
10.1016/j.scitotenv.2022.153698
10.1016/j.egyr.2022.01.032
10.1016/j.buildenv.2022.109015

```
## Using an Institution Token

As per <https://dev.elsevier.com/tecdoc_api_authentication.html>: “Using
a proprietary token (an”Institutional Token“) created for you by our
integration support team”, so you need to contact Scopus to get one. If
you have one and it’s located in an object called `token`, you should be
able to use it as:

``` r
# token is from Scopus dev
hdr = inst_token_header(token)
res = author_df(last_name = "Muschelli", first_name = "John", verbose = FALSE, general = FALSE, headers = hdr)
```

