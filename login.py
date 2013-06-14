#!/usr/bin/env python

import requests

#requests.adapters.DEFAULT_RETRIES = 5

payload = {
	'action': 'login',
	'NameOfTheUsernameField': 'YourUserName',
	'NameOfThePasswordField': 'YourPassWord'
}

login_url     = 'http://www.pepeshochschule.de/login.html'
protected_url = 'http://www.pepeshochschule./OnlyReachableAfterLogin.html'

with requests.session() as c:
	c.post(login_url, data=payload)
	r = c.get(protected_url)

	print(r.status_code)  # <200> means OK

	if (r.ok == True):
		f = open('response.html', 'w')
		f.write(r.text)
		f.close()

