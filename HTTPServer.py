#!/usr/bin/python3
from http.server import HTTPServer, CGIHTTPRequestHandler
import sys

class Logger(object):
	def __init__(self, filename):
		self.terminal = sys.stdout
		self.log = open(filename, 'a', buffering=1)

	def write(self, message):
		self.terminal.write(message)
		self.log.write(message)

	def flush(self):
		pass

port = 8080
logfile = 'log.txt'

sys.stderr = Logger(logfile)

httpd = HTTPServer(('', port), CGIHTTPRequestHandler)
print("Starting HTTPServer on port: " + str(httpd.server_port))
httpd.serve_forever()
