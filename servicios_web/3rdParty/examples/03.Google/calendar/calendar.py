# -*- coding: utf-8 -*-

try:
  from xml.etree import ElementTree # for Python 2.5 users
except ImportError:
  from elementtree import ElementTree
import gdata.calendar.service
import gdata.service
import atom.service
import gdata.calendar
import atom
import sys
import time
import urllib2
from string import split
from string import find

def anadirEvento(user, password, mensaje):	

	calendar_service = gdata.calendar.service.CalendarService()
	calendar_service.email = user
	calendar_service.password = password
	calendar_service.source = 'Python'
	calendar_service.ProgrammaticLogin()

	event = gdata.calendar.CalendarEventEntry()
	event.content = atom.Content(text=mensaje)
	event.quick_add = gdata.calendar.QuickAdd(value='true')

	# Send the request and receive the response:
  	while True:
	    # Sometime Google Calendar service returns an error. This keeps trying until there's no error.
	    try:
	      new_event = calendar_service.InsertEvent(event, '/calendar/feeds/default/private/full')
      	      break
	    except gdata.service.RequestError as inst:
	      if inst[0]['status'] == 302:
	        time.sleep(1.0)
	        continue
	      raise
	    except:
	      raise

def main():
	EMAIL_USER = 'xxx@gmail.com'
	EMAIL_PSWD = 'xxxxx'
	anadirEvento(EMAIL_USER, EMAIL_PSWD, "Prueba calendario curso de python")

if __name__ == "__main__":
    main()

