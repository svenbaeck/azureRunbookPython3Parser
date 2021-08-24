#!/usr/bin/env python3

"""
Python 2 & 3 function to parse the JSON body of an AZURE Automation Runbook Webhook.
"""

import sys
import json
import re

def parse_webhook_data():
    request_body = ' '.join(sys.argv[1:])
    regex = re.compile('{}(.*){}'.format(re.escape('RequestBody:'), re.escape(',RequestHeader:')))
    clean_body = regex.findall(request_body)
    return json.loads(clean_body[0])
