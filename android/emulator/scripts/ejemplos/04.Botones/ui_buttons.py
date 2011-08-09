#!/usr/bin/env python
import android
droid = android.Android()
title = 'Alerta'
message = ('Esta alerta tiene 3 botones y' 'se espera que presione uno')
droid.dialogCreateAlert(title, message)
droid.dialogSetPositiveButtonText('Si')
droid.dialogSetNegativeButtonText('No')
droid.dialogSetNeutralButtonText('Cancelar')
droid.dialogShow()
response = droid.dialogGetResponse()
droid.makeToast('El resultado de la ejecucion del boton es: %s'    %response[1]['which'])
