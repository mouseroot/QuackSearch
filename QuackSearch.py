#DuckDuckGo - QuackSearch
import webbrowser as web

#GET Parameters
#HTTPS - kh
#Safe search - kp
#1 = true
#-1 = false

#API
# api.duckduckgo.com/api



class Quack:
	#Constructor
	def __init__(self):
		self.settings = "kp=-1&"
		self.ddg = "https://duckduckgo.com/?"
		self.url = None
		self.quit_flags = ["quit","stop","end"]
		self.quit = False

	#Search function
	def search(self, keywords):
		self.url = self.ddg + self.settings + "q=" + keywords
		print "Searching: " + self.url
		web.open_new_tab(self.url)
		
def main():
	print "Quack Search v0.2"
	qs = Quack()
	while qs.quit == False:
		search = raw_input("Search>")
		if search.lower() in qs.quit_flags:
			qs.quit = True
		else:
			qs.search(search)

main()