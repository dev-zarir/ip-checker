from flask import Flask, render_template, request
from requests import get
from requests.exceptions import ConnectionError, ConnectTimeout

app=Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
	remote_ip=request.remote_addr
	success=False
	while not success:
		try:
			get_ip = get('https://api.ipify.org').text
			success=True
		except ConnectionError:
			continue
		except ConnectTimeout:
			continue
	return f"""<!DOCTYPE html>
<html>
<head>
	<title>Check Your IP</title>
</head>
<body>
	<div align="center">
		<h2>This is Found by "request.remote_addr" : { remote_ip }</h2>
	</div>
	<div align="center">
		<h2>And this is found by "requests.get('https://api.ipify.org').text" method : { get_ip }</h2>
		<h3>This one actually the servers ip. Cz the get method sent by the server with "requests" module</h3>
	</div>
</body>
</html>"""


if __name__=='__main__':
	app.run(host='0.0.0.0', port=80, debug=False)

