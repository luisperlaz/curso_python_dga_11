import urllib
import xml.sax
import xml.sax.handler

class Photo():

    def __init__(self, id, owner, secret, server, farm, title, ispublic, isfriend, isfamily):
        self.id = id
        self.owner = owner
        self.secret = secret
        self.server = server
        self.farm = farm
        self.title = title
        self.ispublic = ispublic
        self.isfriend = isfriend
        self.isfamily = isfamily

    def getimageurl(self):
        return "http://farm%s.static.flickr.com/%d/%d_%s.jpg" % (self.farm, self.server, self.id, self.secret)

class PhotoHandler(xml.sax.handler.ContentHandler):

    def __init__(self):
        self.photos = []

    def startElement(self, name, attributes):
        if name == "photo":
            self.photos.append(Photo(int(attributes["id"]),
            attributes["owner"],
            attributes["secret"],
            int(attributes["server"]),
            int(attributes["farm"]),
            attributes["title"],
            attributes["ispublic"],
            attributes["isfriend"],
            attributes["isfamily"]))

def main():
	API_KEY = "00197acdd512ae6125518156fe657db5";
	url = "http://api.flickr.com/services/rest/?method=flickr.photos.getRecent&api_key=%s" % (API_KEY)
	content = urllib.urlopen(url).read()

	handler = PhotoHandler()
	xml.sax.parseString(content, handler)
	
	for photo in handler.photos:
	    print photo.getimageurl()


if __name__ == "__main__":
    main()
