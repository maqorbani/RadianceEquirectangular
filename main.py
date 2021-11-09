# import subprocess

# ===============Variables===============
# General
ncores = 10  # number of cores to render
x_res = 2048  # Width of the image which is 2x the height
y_res = x_res / 2  # Do not touch this one
oconv = 'render.oct'  # Octree's name

# Camera's position
x = 5.000  # X
y = 3.500  # Y
z = 1.200  # Z

# Render Quality
quality = 'HIGH'  # choose from LOW, MEDIUM, or HIGH
mesh_det = 'HIGH'  # Mesh detail, LOW, MEDIUM, or HIGH
variability = 'MEDIUM'  # light value variance variability
indirect = 2  # Choose how indirect the lighting is
# ===============Variables===============


