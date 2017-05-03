import sqlite3, re, requests

#import sys
#from termcolor import colored

def insertLink(course, professor, http, description):
    con = sqlite3.connect("database.db")
    cur = con.cursor()
    try:
        request = requests.get(str(http))
        if request.status_code == 200:
            cur.execute("INSERT INTO links (course, professor, http, description) VALUES (?,?,?,?)", (((re.sub(r'\W+', '', course)).upper()), (professor.title()), http, (description.title())))
            con.commit()
    except:
        pass
    con.close()

def retrieveLinks():
	con = sqlite3.connect("database.db")
	cur = con.cursor()
	cur.execute("SELECT course, professor, http, description FROM links")
	links = cur.fetchall()
	con.close()
	return links

def queryLinks(query):
    fullLinks, links = retrieveLinks(), []
    #print(colored(fullLinks, 'green'), file=sys.stderr)
    for course in fullLinks:
        #print(colored(course, 'blue'), file=sys.stderr)
        if str(course[0]) == str(query):
            #print(colored(len(links), 'blue'), file=sys.stderr)
            links.append(tuple(course))
    #print(colored(links, 'yellow'), file=sys.stderr)
    return (fullLinks, links)
