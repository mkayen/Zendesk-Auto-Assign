from zendesk import *

zendesk = Zendesk('xx', 'xx', 'xx')
allTix = zendesk.list_tickets(view_id=28994374)

print allTix

count=len(allTix)
print count
x=0
print 'ticket_id | ticket_status | group_name | assignee_name'
while x < count:
	ticket_id = allTix[x]['nice_id']
	status_id = allTix[x]['status_id']
	group_name = allTix[x]['group_name']
	assignee_name = allTix[x]['assignee_name']
	print ticket_id,'|', status_id, '|', group_name, '|', assignee_name
	x=x+1

