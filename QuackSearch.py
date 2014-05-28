import webbrowser as web
from optparse import OptionParser

if __name__ == "__main__":
	usage = "QuackSearch [Safe Mode] [Search term]"
	desc = "Opens a browser with the given search"
	parser = OptionParser(usage=usage,description=desc)
	parser.add_option("-n","--safe-off",action="store_true",default=False,dest="safe_mode",help="Disables filtering adult content (safe mode)")
	(options,args) = parser.parse_args()
	if len(args) > 0:
		if options.safe_mode:
			safe_str = "&kp=-1"
		else:
			safe_str = "&kp=1"
		search_term = args[0]
		web.open_new_tab("".join(["https://duckduckgo.com/?","q=",search_term,safe_str]))
	else:
		parser.print_help()
