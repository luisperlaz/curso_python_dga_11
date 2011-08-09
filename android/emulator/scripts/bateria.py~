#!/usr/bin/env python2.6
# -*- coding: utf-8 -*-

import android

droid = android.Android()

#Se monitoriza la bateria
droid.batteryStartMonitoring()

#Se captura la información de la bateria
bateriaHealth = droid.batteryGetHealth()[1]
if bateriaHealth == 2:
        print "La bateria está bien"
elif bateriaHealth == 1:
        print "Salud de la Bateria desconocido"
elif bateriaHealth == 3:
	print "La bateria tiene sobrecarga"
elif bateriaHealth == 4:
        print "La bateria está muerta"
elif bateriaHealth == 5:
        print "La bateria tiene sobrevoltaje"
else:
        print "falla desconocida"
#Se captura el tipo de conexión que usa el dispositivo
tipoConexion = droid.batteryGetPlugType()[1]
if tipoConexion == 0:
        print "Cable desconectado"
elif tipoConexion == 1:
        print "Fuente de alimentación: cargador AC"
elif tipoConexion == 2:
        print "Fuente de alimentación: cable USB"
else:
        print "Desconocido"

#Se captura lel estatus de la bateria
estatus = droid.batteryGetStatus()[1]
if estatus == 2:
        print "Bateria cargandose"
elif estatus == 3:
        print "Bateria descargandose"
elif estatus == 4:
        print "Bateria no se está cargando"
elif estatus == 5:
        print "Bateria full de carga"

print "Tipo de tecnología: ",droid.batteryGetTechnology()[1]
print "Temperatura: ",droid.batteryGetTemperature()[1]
print "voltaje: ",droid.batteryGetVoltage()[1]

#Se deja de monitorizar la bateria
droid.batteryStopMonitoring()

