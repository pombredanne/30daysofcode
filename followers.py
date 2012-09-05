import sys
from libsaas.services import github

def get_all_followers(service, username):
    followers = []
    empty = False
    page = 0
    while not empty:
        current_page = gh.user(name=username).followers(page=page)
        followers.extend(current_page)
        empty = len(current_page)==0
        page += 1
    return followers

if __name__  == '__main__':
    if len(sys.argv) != 4:
        print "Usage: %s <your_username> <password> <other_username>"%sys.argv[0]
        sys.exit(-1)
    gh = github.GitHub(sys.argv[1], sys.argv[2])
    print len(get_all_followers(gh, sys.argv[3]))
