import android
import time

droid = android.Android()
droid.toggleBluetoothState(True)
droid.dialogCreateAlert('¿Eres el servidoe?')
droid.dialogSetPositiveButtonText('Si')
droid.dialogSetNegativeButtonText('No')
droid.dialogShow()
result = droid.dialogGetResponse()
is_server = result.result['which'] == 'positive'
if is_server:
  droid.bluetoothMakeDiscoverable()
  droid.bluetoothAccept()
else:
  droid.bluetoothConnect()

if is_server:
  result = droid.getInput('Chat', 'Pon tu mensaje').result
  if result is None:
    droid.exit()
  droid.bluetoothWrite(result + '\n')

while True:
  message = droid.bluetoothReadLine().result
  droid.dialogCreateAlert('Chat recibido', message)
  droid.dialogSetPositiveButtonText('Ok')
  droid.dialogShow()
  droid.dialogGetResponse()
  result = droid.getInput('Chat', 'Pon tu mensaje').result
  if result is None:
    break
  droid.bluetoothWrite(result + '\n')

droid.exit()
