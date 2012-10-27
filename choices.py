import piggyphoto as pp

cam = pp.Camera()

print cam.config.main.capturesettings.shutterspeed.choices

cam.close()