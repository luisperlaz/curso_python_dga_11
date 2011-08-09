import gdata.docs.data
import gdata.docs.client

def PrintFeed(feed):
  print '\n'
  if not feed.entry:
    print 'No entries in feed.\n'
  for entry in feed.entry:
    print entry.title.text.encode('UTF-8'), entry.GetDocumentType(), entry.resource_id.text

    # List folders the document is in.
    for folder in entry.InFolders():
      print folder.title

client = gdata.docs.client.DocsClient(source='yourCo-yourAppName-v1')
client.ssl = True  # Force all API requests through HTTPS
client.http_client.debug = False  # Set to True for debugging HTTP requests
client.ClientLogin('rengar666@gmail.com', '1maysun8', client.source);

# Create an empty document
new_doc = client.Create(gdata.docs.data.DOCUMENT_LABEL, 'Documento - Curso Python')
print 'Document "%s" created' % new_doc.title.text

# Create an empty spreadsheet. By default, the writers_can_invite setting is True.
new_spreadsheet = client.Create(gdata.docs.data.SPREADSHEET_LABEL, 'Hoja de calculo - Curso Python', writers_can_invite=False)
print 'Spreadsheet "%s" created' % new_spreadsheet.title.text

# Create an empty presentation
new_preso = client.Create(gdata.docs.data.PRESENTATION_LABEL, 'Presentacion - Curso Python')
print 'Presentation "%s" created' % new_preso.title.text

feed = client.GetDocList()
PrintFeed(feed)

