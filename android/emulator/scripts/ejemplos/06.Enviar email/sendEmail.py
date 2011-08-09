#!/usr/bin/env python

#Se importa el modulo android
import android

#Se crea la instancia de la clase Android
droid = android.Android()

#Se define la direccion de correo, el asunto del correo y el contenido del mismo
asunto = "Prueba de envio de correo desde Android con un script de python"
para = "xxxx@neodoo.es"
cuerpo_correo = "Esta es una prueba de envio de correo\n El tiempo en el reloj es: %s\n ------\n Curso de Python\n" %time.ctime()

#Se llama a la funcion sendEmail con los datos necesarios.
#Esto llama a la aplicacion de envio de correo de forma grafica con la
#informacion que se pasa en la funcion.
droid.sendEmail(para,asunto,cuerpo_correo)

#Se finaliza la instancia de la clase.
droid.exit()
