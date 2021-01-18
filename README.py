
#Baumer Camera

import sys
import neoapi

result = 0
try:
    camera = neoapi.Cam()
    camera.Connect()
    camera.f.ExposureTime.Set(10000)

    image = camera.GetImage()
    image.Save("getting_started.bmp")

except (neoapi.NeoException, Exception) as exc:
    print('error: ', exc.GetDescription())
    result = 1

sys.exit(result)
