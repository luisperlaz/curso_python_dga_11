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
import android
import sys
import time
import urllib2
from string import split
from string import find


droid = android.Android()

def localizar():
    droid.makeToast(u"Empezando a localizar la posicion")
    droid.startLocating(3600,1)

    time.sleep(10)
    
    fin = True
    segundos = 300
    seg_trancurridos = 0
    
    while fin:
        time.sleep(1)
        seg_trancurridos += 1
        l = droid.readLocation()
        ll = l.result
        
        if "gps" in ll:
            mensaje = u"Posición actual: "
            pos = (str(ll["gps"]["latitude"]), str(ll["gps"]["longitude"]))
            fin = False
            droid.makeToast(u"Posición GPS encontrada")
        else:

            if seg_trancurridos == segundos: 
                fin = False
                
                if "network" in ll:
                    pos = (str(ll["network"]["latitude"]), str(ll["network"]["longitude"]))
                    mensaje = u"Posición red celular: "
                    droid.makeToast(u"Posición Red Celular encontrada")
                else:
                    
                    ll = droid.getLastKnownLocation().result
                    pos = (str(ll["network"]["latitude"]), str(ll["network"]["longitude"]))
                    mensaje = u"Ultima posición red celular: "
                    droid.makeToast(u"No se pudo establecer conexión, se enviara la ultima posición registrada")
    
    droid.makeToast(u"Terminado de localizar la posicion")

    pll = "%s,%s" % (str(pos[0]), str(pos[1]))

    mapa = "http://maps.google.com/maps?ll=%s&q=%s" % (pll, pll)

    droid.stopLocating()
    
    return mensaje, mapa    

def enviar_mensaje(numero):
    try: 
        mensaje, mapa = localizar()
        msg = "%s %s" % (mensaje,  mapa)
	asunto = u"Respuesta a la peticion de localización GPS desde el numero %s" % (numero)
	para = "xxxx666@gmail.com"
        droid.sendEmail(para, asunto, msg.encode('ascii', 'replace'))
	droid.makeToast(u"Enviada respuesta")
	anadirEvento(msg)
	droid.makeToast(u"Evento añadido al calendario")
    except:
        droid.makeToast("Error: " + str(sys.exc_info()[0]))

def anadirEvento(mensaje):
	EMAIL_USER = 'xxxx@gmail.com'
	EMAIL_PSWD = 'xxxxxxxx'

	calendar_service = gdata.calendar.service.CalendarService()
	calendar_service.email = EMAIL_USER
	calendar_service.password = EMAIL_PSWD
	calendar_service.source = 'Android'
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



def servicio():
    
    while True:
        time.sleep(10)
	# Escuchar los mensajes SMS
        msg_solicitud = droid.smsGetMessages(True)
        
        for i in msg_solicitud.result:
            
            msg_sms = i["body"].strip().upper()
            if msg_sms == "GPS":
                droid.makeToast(u"Solicitud de localización recibida")
                droid.smsMarkMessageRead([i["_id"]], True)
                telefono = i["address"]
                enviar_mensaje(telefono)
		droid.makeToast(u"%s: %s" % (telefono,msg_sms))
                
                
                
    
if __name__ == "__main__":
    servicio()
