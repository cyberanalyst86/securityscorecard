import os
import requests
import sys
import time
from add_org import *
from remove_org import *
from create_dataframe import *
from tabulate_scorecard import *

# Declaration

"""----------set the organisations that you want to compare over here !!!----------"""
"""----------comma delimited ----------"""
# ------------------------------- set the organization domains to be queried -------------------------------
organisation_domain = ["google.com", "apple.com", "amazon.com", "netflix.com"]

# ------------------------------- api header -------------------------------
token = os.getenv('SSC_API_TOKEN')
api_url = os.getenv('API_URL', 'https://api.securityscorecard.io')

# Replace 'API Key' with your actual API Key
headers = {
    'Accept': 'application/json; charset=utf-8',
    'Content-Type': 'application/json',
    'Authorization': 'Token ' + 'API Key',
    'cache-control': 'no-cache',
}

# ------------------------------- set api header -------------------------------
url = api_url + '/portfolios'
response = requests.get(api_url + '/portfolios', headers=headers)
response.raise_for_status()

# ------------------------------- get organisations in portfolio -------------------------------
portfolios = response.json()['entries']
my_portfolio = [
    item for item in portfolios
    # My Portfolio is read_only and private
    if 'read_only' in item and item['read_only'] == True and item['privacy'] == 'private'
][0]

# ------------------------------- define variables -------------------------------
org_domain = []  # empty domain list

# ------------------------------- get scorecards in "portfolio" -----------------------------
url = api_url + '/portfolios/' + my_portfolio['id'] + '/companies'
response = requests.get(url, headers=headers)
response.raise_for_status()

scorecards = response.json()['entries']

for i in range(len(scorecards)):
    org_domain.append(scorecards[i]["domain"])

if len(org_domain) == 0:

    # 1.) add organization to portfolio
    print("adding organisations to portfolio...")

    add_org(headers, my_portfolio, organisation_domain, api_url)

    # 2.) generate local organization scorecard

    print("generating portfolio scorecard...")

    # 3.) tabulate portfolio scorecard

    tabulate_scorecard(headers, organisation_domain, api_url)

    # 4.) remove organization from porfolio
    print("removing companies from portfolio...")

    remove_org(headers, my_portfolio, organisation_domain, api_url)

    print("Operation completed !!!")


# --------------------------------------------------------------
else:

    print("existing companies in portfolio: \n")
    print(org_domain)
    print("\n")

    print("removing " + str(org_domain) + " from portfolio...")

    for i in range(len(org_domain)):
        delete_url = url = api_url + '/portfolios/' + my_portfolio['id'] + '/companies/' + org_domain[i]

        response = requests.delete(url, headers=headers)
        response.raise_for_status()

    # 1.) add organization to portfolio
    print("adding organisations to portfolio...")

    add_org(headers, my_portfolio, organisation_domain, api_url)

    # 2.) generate local organization scorecard

    print("generating portfolio scorecard...")

    # 3.) tabulate portfolio scorecard

    tabulate_scorecard(headers, organisation_domain, api_url)

    # 4.) remove organization from porfolio
    print("removing companies from portfolio...")

    remove_org(headers, my_portfolio, organisation_domain, api_url)

    print("Operation completed !!!")