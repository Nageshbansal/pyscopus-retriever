import requests
import json
import pandas as pd
import httpx
from xml.etree import ElementTree

# retrieve using scopus
base_url = "https://api.elsevier.com/content/search/scopus"
apiKey = "45c6063a93408d8c4f3925dcf8e02e01"
headers = {
    'X-ELS-APIKey': '45c6063a93408d8c4f3925dcf8e02e01',
    'Accept': 'application/json'
}
title = []
url = []

headers_xml = {
    'X-ELS-APIKey': '45c6063a93408d8c4f3925dcf8e02e01',
    'Accept': 'application/xml'
}


def get_xml(paper_doi):
    response = requests.get(
        f'https://api.elsevier.com/content/article/doi/' + paper_doi, headers=headers_xml
    )
    print(response)
    root = ElementTree.fromstring(response.content)
    tree = ElementTree.ElementTree(root)
    file_name = '-'.join(paper_doi.split('/'))
    tree.write(f'./XML_Data/{file_name}.xml')


def get_doi(query, entry):
    response = requests.get(
        f'https://api.elsevier.com/content/search/scopus?query={query}&count=200',
        headers=headers
    )
    response_json = response.json()
    doi = response_json['search-results']['entry'][entry]['prism:doi']
    # print(response_json)
    return doi


def scopus_paper_date(paper_doi, apiKey=apiKey):
    timeout = httpx.Timeout(10.0, connect=60.0)
    client = httpx.Client(timeout=timeout, headers=headers)
    _query = "&view=FULL"
    _url = f"https://api.elsevier.com/content/article/doi/" + paper_doi
    r = client.get(_url)
    # print(r)
    if r.status_code == 404:
        return None
    return r


for i in range(0, 10):
    query = 'ALL ( "thermal adaptation"  AND  " behaviour"  AND  "buildings"  AND  "human" )'
    paper_doi = get_doi(query, i)
    # y = scopus_paper_date(paper_doi)
    get_xml(paper_doi)
    # if y:
    #     json_acceptable_string = y.text
    #     d = json.loads(json_acceptable_string)
    #     # print()
    #     file_name = '-'.join(paper_doi.split('/'))
    #     file_name = '-'.join(paper_doi.split('/'))
    #     with open(f'./XML_Data/{file_name}.txt', 'w') as fp:
    #         print(y, file=fp)

    # else:
    #     print('not able to retrieve')

# df = pd.DataFrame({'title':title,'url':url})
# df.to_csv('papers_info')
