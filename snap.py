import piggyphoto

C = piggyphoto.Camera()

print C.abilities
C.capture_preview('preview.jpg')
C.capture_image('snap.jpg')
