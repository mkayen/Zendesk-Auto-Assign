from zendesk import *

zendesk = Zendesk('https://divide.zendesk.com', 'max.kayen@enterproid.com', 'Nov91990')
allTix = zendesk.list_tickets(view_id=28994374)
show_

ticket_id = allTix[0]['nice_id']
status_id = allTix[0]['status_id']

print ticket_id, "|", status_id


