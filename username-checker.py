import urllib.request as urllib2
import sys
# define ANSI escape sequences for colored output
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

# a function for each site, which creates the request according to the username
def bitbucket(username):
    url = "https://bitbucket.org/" + username + "/"
    request = urllib2.Request(url)
    parse(request,username)
def github(username):
    url = "https://github.com/" + username + "/"
    request = urllib2.Request(url)
    parse(request,username)
def twitter(username):
    url = "https://twitter.com/" + username + "/"
    request = urllib2.Request(url)
    parse(request,username)
def instagram(username):
    url = "https://instagram.com/" + username + "/"
    request = urllib2.Request(url)
    parse(request,username)
def medium(username):
    url = "https://medium.com/@" + username + "/"
    # Medium requires a browser as a user agent, such as chrome
    headers = {
    "User-Agent" : "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2490.86 Safari/537.36"
    }
    request = urllib2.Request(url, None, headers)
    parse(request,username)
def facebook(username):
    url = "http://facebook.com/" + username + "/"
    request = urllib2.Request(url)
    parse(request,username)

# process the request and capture the response code
def middleware(request, username):
    try:
        response = urllib2.urlopen(request)
    except urllib2.HTTPError as e:
        if e.code == 404:
            return (e.code, bcolors.OKGREEN, "Available")
        else:
            return (e.code, bcolors.WARNING, e.reason)
    else:
        if response.getcode() == 200:
            return (response.getcode(), bcolors.FAIL, "Already exists")

# used for generating colored responses
def parse(request, username):
    response = middleware(request, username)
    print(response[1] + request.get_full_url()+" ["+str(response[0])+"] "+response[2]+bcolors.ENDC);

# ask for a username, instead of an argument
# username = raw_input("Username to check: ")
# take username as a system argument
username = sys.argv[1]
print(bcolors.HEADER + ("Checking for availability of '"+username+"', please wait...") + bcolors.ENDC);
facebook(username)
twitter(username)
instagram(username)
github(username)
#medium(username)
#bitbucket(username)
