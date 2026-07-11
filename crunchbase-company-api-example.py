"""
Crunchbase Company API: A Quick Start Example
See more at: https://apify.com/johnvc/crunchbase-company-api?fpr=9n7kx3
Input schema: https://apify.com/johnvc/crunchbase-company-api/input-schema?fpr=9n7kx3

This script shows how to call the Crunchbase Company API on Apify from Python and
read its structured JSON output. Send one or many public Crunchbase organization
URLs and get one clean row per company (name, industries, total funding,
investors, employee count, HQ location, rank, IPO status, and more).

Get your free Apify API key at: https://apify.com?fpr=9n7kx3
"""

import os
from dotenv import load_dotenv
from apify_client import ApifyClient

load_dotenv()

# Initialize the Apify client with your API token (read from .env)
client = ApifyClient(os.getenv("APIFY_API_TOKEN"))

# Build the Actor input.
# Kept to a single company URL so your first run stays cheap (you pay per
# company returned). Add more URLs to the list to collect many companies in one
# batch; they are collected in parallel and returned one row each.
run_input = {
    "companyUrls": [
        "https://www.crunchbase.com/organization/apple",
        # "https://www.crunchbase.com/organization/anthropic",
    ],
}

# Run the Actor and wait for it to finish
run = client.actor("johnvc/crunchbase-company-api").call(run_input=run_input)
if run is None:
    raise SystemExit("The Actor run did not return a result.")

# Read structured results from the run's default dataset
# (apify-client 3.x returns a Run object; use .default_dataset_id, not run["..."])
items = list(client.dataset(run.default_dataset_id).iterate_items())
print(f"Returned {len(items)} company(ies).\n")

# Show a few key fields from each company.
for item in items:
    print(f"Name:           {item.get('name')}")
    print(f"Industries:     {item.get('industries')}")
    print(f"Total funding:  {item.get('totalFunding')}")
    print(f"Employees:      {item.get('employeeCount')}")
    print(f"HQ location:    {item.get('hqLocation')}")
    print(f"Crunchbase rank:{item.get('cbRank')}")
    print(f"Funding rounds: {item.get('numFundingRounds')}")
    print(f"Investors:      {item.get('numInvestors')}")
    print(f"IPO status:     {item.get('ipoStatus')}")
    print(f"URL:            {item.get('companyUrl')}")
    print(f"Summary:        {item.get('summary')}")
    print("-" * 60)
