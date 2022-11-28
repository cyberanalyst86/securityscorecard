import os
import requests
import sys
import time

# Function to remove organizations from portfolio

def remove_org(headers, my_portfolio, org_domain, api_url):
    # Iterate removal of organizations from portfolio

    for i in range(len(org_domain)):
        # API call (URL)
        url = api_url + '/portfolios/' + my_portfolio['id'] + '/companies/' + org_domain[i]

        response = requests.delete(url, headers=headers)
        response.raise_for_status()

    return