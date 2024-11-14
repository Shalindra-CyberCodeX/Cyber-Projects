import imaplib

# IMAP server settings
imap_host = 'imap.gmail.com'
imap_port = 993
username = 'priyathperera13@gmail.com'
password = 'oiae acab jkxp qwum'

try:
    # Connect to the IMAP server
    imap = imaplib.IMAP4_SSL(imap_host, imap_port)

    # Login to the IMAP server
    imap.login(username, password)

    # Select the Inbox folder
    imap.select('INBOX')

    # Search for unread emails sent to your Gmail address
    status, email_ids = imap.search(None, '(UNSEEN TO "{}")'.format(username))

    if status == 'OK':
        email_ids_list = email_ids[0].split()
        for email_id in email_ids_list:
            # Fetch the email for the given ID
            status, email_data = imap.fetch(email_id, '(RFC822)')
            if status == 'OK':
                # Process and parse the email data
                # Extract relevant information such as sender, subject, body, etc.
                print(email_data)

    # Logout from the IMAP server
    imap.logout()
except Exception as e:
    print("An error occurred:", e)
