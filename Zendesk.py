show_ticket_url = 'https://thegizzle.zendesk.com/api/v2/tickets/18618.json'
headers = {'Accept':'application/json'}
show_ticket = requests.get(show_ticket_url, auth=(os.environ['xx'], os.environ['xx']), headers=headers)
print show_ticket.headers
print show_ticket.text
- See more at: http://developer.zendesk.com/blog/2013/01/03/accessing-the-api-with-python/#sthash.KEYqrr50.dpuf