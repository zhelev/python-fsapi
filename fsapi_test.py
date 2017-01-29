from fsapi import FSAPI

fs = FSAPI('http://192.168.1.180:80/device', 1234)
print('Name: %s' % fs.friendly_name)
print('Mute: %s' % fs.mute)
print('Mode: %s' % fs.mode)
print('Power: %s' % fs.power)
print('Volume: %s' % fs.volume)
print('Track name: %s' % fs.play_info_name)
print('Track text: %s' % fs.play_info_text)
print('Graphics: %s' % fs.play_info_graphics)
