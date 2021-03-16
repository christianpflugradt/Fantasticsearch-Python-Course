from http.server import BaseHTTPRequestHandler, HTTPServer
from searchengine import has_database, search

search_form = """
	<html><title>Fantasticsearch</title><body>
	<form action="/">
	  <label for="search">Your Input:</label>
	  <input type="text" id="search" name="search" value="">
	  <input type="submit" value="Search">
	  ${PLACEHOLDER}
	</form> 
	</body></html>
"""

class FantasticServer(BaseHTTPRequestHandler):
	def do_GET(self):
		self.send_response(200)
		self.send_header("Content-type", "text/html")
		self.end_headers()
		if has_database():
			self.wfile.write(bytes(self.html(), "utf-8"))
		else:
			self.wfile.write(bytes("<p>still initializing...</p>", "utf-8"))
			
	def tokens(self):
		if "search=" in self.path:
			return self.path.split("search=")[1].split('+')
		else:
			return []
			
	def html(self):
		return search_form.replace("${PLACEHOLDER}", "<p>%s</p>" % str(self.render()))
		
	def render(self):
		lines = ["<a href=http://openjdk.java.net/jeps/%s>%s</a>" % (id, title) for id, title in sorted(search(self.tokens()), key=(lambda tuple: int(tuple[0])))]
		return "<br>".join(lines) if len(lines) > 0 else "<p>no jeps found for search term :-(</p>"
			
	def sort_val(self, tuple):
		id, _ = tuple
		return int(id)
		
def serve():
	server = HTTPServer(("localhost", 8080), FantasticServer)
	try:
		server.serve_forever()
	except KeyboardInterrupt:
		pass
	server.server_close()

