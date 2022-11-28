import os
import requests
import sys
import time

# Function to add organizations to portfolio

def add_org(headers, my_portfolio, org_domain, api_url):
    # Iterate addition of organizations to portfolio

    for i in range(len(org_domain)):
        # API call (URL)
        url = api_url + '/portfolios/' + my_portfolio['id'] + '/companies/' + org_domain[i]

        response = requests.put(url, headers=headers)
        response.raise_for_status()

    return




