import piggyphoto

C = piggyphoto.Camera()

print(C.abilities)
C.capture_preview().save() #('preview.jpg')
C.capture_image('snap.jpg')

C.close()