from zendesk import *

zendesk = Zendesk('xx', 'xx', 'xx')
allTix = zendesk.list_tickets(view_id=28994374)

ticket_id = allTix[0]['nice_id']
status_id = allTix[0]['status_id']

print ticket_id, "|", status_id


