#!/usr/bin/env python
# -*- coding: utf-8 -*-
import re,sys
regex_input = raw_input('Enter regex > ')
regexp = re.compile(regex_input, re.IGNORECASE)
test_email_addresses = ['abc@gmail.com', 'xyz123@hotmail.com', 'blahblah09@gmail.com']
matched_address = []
for email_address in test_email_addresses:
    if regexp.search(email_address):
        matched_address.append(email_address)
print matched_address
