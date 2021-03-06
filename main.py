import subprocess
import os
import sys


# ===============Sys__Args===============
args = sys.argv

try:
    oconv = args[args.index('-o') + 1]  # Octree's name
except ValueError:
    oconv = 'render.oct'  # Octree's name

try:
    rad = args[args.index('-r') + 1]  # Rad's name
except ValueError:
    rad = 'Geo.rad'  # Rad's name

try:
    ncores = int(args[args.index('-n') + 1])  # number of cores to render
except ValueError:
    ncores = 1  # number of cores to render

try:
    x_res = int(args[args.index('-x') + 1])  # Width of the image which is 2x the height
except ValueError:
    x_res = 2048  # Width of the image which is 2x the height

y_res = x_res // 2  # Do not touch this one

try:
    po = args.index('-p')
    x = float(args[po + 1])  # X
    y = float(args[po + 2])  # Y
    z = float(args[po + 3])  # Z
except ValueError:
    x = 5.000  # X
    y = 3.500  # Y
    z = 1.200  # Z

try:
    quality = args[args.index('--quality') + 1]  # choose from LOW, MEDIUM, or HIGH
    assert quality in ['LOW', 'MEDIUM', 'HIGH']
except ValueError:
    quality = 'HIGH'  # choose from LOW, MEDIUM, or HIGH

try:
    mesh_det = args[args.index('--mesh') + 1]  # Mesh detail, LOW, MEDIUM, or HIGH
    assert mesh_det in ['LOW', 'MEDIUM', 'HIGH']
except ValueError:
    mesh_det = 'HIGH'  # Mesh detail, LOW, MEDIUM, or HIGH

try:
    variability = args[args.index('--lvar') + 1]  # light value variance variability
    assert variability in ['LOW', 'MEDIUM', 'HIGH']
except ValueError:
    variability = 'MEDIUM'  # light value variance variability

try:
    indirect = int(args[args.index('--indir') + 1])  # light value variance variability
    assert indirect in [0 ,1, 2]
except ValueError:
    indirect = 2  # Choose how indirect the lighting is

try:
    output = args[args.index('--output') + 1]   # Output image name
except ValueError:
    output = 'out.hdr'  # Output image name

# ===============Sys__Args===============

# Checking for Radiance installation + Radiance rtrace commands
if os.path.exists('/usr/local/radiance/'):
    print('Radiance folder was found at usr/local/radiance/')
else:
    print('Please make sure Radiance is installed at /usr/local/radiance/')

if os.path.exists('/usr/local/radiance/bin/rtrace'):
    print('Radiance rtrace was found')

# Set the PATH variables
os.environ['PATH'] += os.pathsep + ':/usr/local/radiance/bin'
os.environ['RAYPATH'] = '.:/usr/local/radiance/lib'


def getbbox(rad):
    bbox = subprocess.run(['getbbox', rad], capture_output=1, text=1)
    if bbox.returncode:
        print('An error has occured while getting the bounding box!')
        print(bbox.stderr)
        raise ValueError('Please check the error message.')

    bounding_box = bbox.stdout.strip().split('\n')[-1].split('       ')[1:]
    bounding_box = [i.strip() for i in bounding_box]
    return bounding_box


if __name__ == "__main__":
    bounding_box = getbbox(rad)


file = f'''\
# Specify where the compiled octree should be generated
OCTREE={oconv}
# Specify an (I)nterior or (E)xterior scene, along with the bounding box of \
the scene, obtainable via `getbbox scene.rad`
ZONE=E  {'  '.join(bounding_box)}
# A list of of the rad files which make up our scene
scene={rad}
# Camera view options
view=-vp {x} {y} {z} -vd 0.000 -1 0.000 -vu 0.000 0.000 1.000
# Option overrides to specify when rendering
# render=-av 1 1 1
# Choose how indirect the lighting is
INDIRECT={indirect}
# Choose the quality of the image, from LOW, MEDIUM, or HIGH
QUALITY={quality}
# Choose the resolution of mesh detail, from LOW, MEDIUM, or HIGH
DETAIL={mesh_det}
# Choose the light value variance variability, from LOW, MEDIUM, or HIGH
VARIABILITY={variability}
# Where to output the raw render
RAWFILE=output_raw.pic
# Where to output a filtered version of the render (scaled down for\
 antialiasing, exposure correction, etc)
PICTURE=output.pic
# The time duration in minutes before reporting a status update of the\
 render progress
REPORT=0.1
'''


def rif_write(file):
    with open('scene.rif', 'w') as f:
        f.write(file)


def opt_write():
    opt = subprocess.run(['rad', '-v', '0', 'scene.rif', 'OPT=saved.opt'],
                         capture_output=1, text=1)
    if opt.returncode:
        print('An error has occured while creating the opt file!')
        print(opt.stderr)
        raise ValueError('Please check the error message.')


args_ = [f'X={x_res};', f'Y={y_res};', 'cnt', '$Y', '$X', '|', 'rcalc', '-f',
        '2d360.cal', '-e', f'"XD=$X;YD=$Y;X={x};Y={y};Z={z}"', '|',
        'rtrace', '-n', str(ncores), '-x', '$X', '-y', '$Y', '-fac',
        '@saved.opt', oconv, '>', f'{output}']


def render(args):
    os.system(' '.join(args))
    # out = subprocess.run(args, shell=1, capture_output=1, text=1)
    # if out.returncode:
    #     print('An error has occured while rendering the image!')
    #     print(out.stderr)
    #     raise ValueError('Please check the error message.')


rif_write(file)
opt_write()
render(args_)
