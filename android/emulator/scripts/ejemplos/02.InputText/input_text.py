import android
droid = android.Android()
texto = droid.dialogGetInput("Escriba su nombre","Nombre:")
droid.makeToast('Hola %s' %texto[1])
