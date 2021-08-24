# azureRunbookPython3Parser
When assigning a webhook to an AZURE Automation Python Runbook, parsing the request body is not so straightforward. The body is passed to the script through ``sys.argv[1:]``. The first problem is that the entire body may be split over multiple entries in the array. Secondly, the data is not encoded following strict JSON syntax.

The function defined in this json_body_parser.py extracts the body from the ``sys.argv`` parameters and converts it to a Python dictionnary. Simply copy the Python code into your project or include the file as a module in your AZURE Automation account. Getting the body for use in your code is then as easy as calling ``parse_webhook_data()``.
