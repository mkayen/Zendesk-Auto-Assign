from zendesk import *

zendesk = Zendesk('https://divide.zendesk.com', 'max.kayen@enterproid.com', 'Nov91990')
allGroups = zendesk.list_groups()

support = allGroups[3]['users']
count=8
x=0
while x < count:
	user = support[x]['name']
	print user
	x = x+1


