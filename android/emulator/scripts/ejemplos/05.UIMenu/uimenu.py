import android
droid=android.Android()

droid.addOptionsMenuItem("Si","si",None,"star_on")
droid.addOptionsMenuItem("No","no","No","star_off")
droid.addOptionsMenuItem("Salir","off",None,"ic_menu_revert")

print "Presiona el menu para ver opciones extra.."
print "En 10 segundos se saldra si no hace nada"

while True: # Wait for events from the menu.
  response=droid.eventWait(10000).result
  if response==None:
    break
  print response
  if response["name"]=="off":
    break
print "Hecho."
