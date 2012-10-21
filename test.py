import ctypes
gp = ctypes.CDLL('libgphoto2.dylib')
print(gp)

gp.gp_context_new.restype = ctypes.c_void_p
ctx = ctypes.c_void_p(gp.gp_context_new())
print(ctx)

lst = ctypes.c_void_p()
gp.gp_list_new(ctypes.byref(lst))
print(lst)

num = gp.gp_camera_autodetect(lst, ctx)
print(num)