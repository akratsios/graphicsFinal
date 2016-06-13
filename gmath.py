from math import sqrt

def calculate_normal(points,i):
    #calculate ax,ay,az, and bx,by,bz 
    ax = points[i+1][0] - points[i][0]
    ay = points[i+1][1] - points[i][1]
    az = points[i+1][2] - points[i][2]

    bx = points[i+2][0] - points[i][0]
    by = points[i+2][1] - points[i][1]
    bz = points[i+2][2] - points[i][2]

    #plug in to calculate normal
    normal = [0,0,0]
    
    normal[0] = ay * bz - az * by
    normal[1] = az * bx - ax * bz
    normal[2] = ax * by - ay * bx

    return normal

def scalar_product(v, s):
    return [v[x]*s for x in xrange(len(v))]

def dot_product(v0, v1):
    return v0[0] * v1[0] + v0[1] * v1[1] + v0[2] * v1[2]

def add_vectors(v0, v1):
    return [v0[x] + v1[x] for x in xrange(len(v0))]

def sub_vectors(v0, v1):
    return [v0[x] - v1[x] for x in xrange(len(v0))]

def normalize(v):
    m = sqrt(v[0] * v[0] + v[1] * v[1] + v[2] * v[2])
    if m == 0:
        return 0
    return [v[x]/m for x in xrange(3)]

def calculate_light(c, p_sources, constants, normal, view):
    # calculate ambient lighting
    iamb = [c[x] * constants[x] for x in xrange(3)]
    idiff = [0, 0, 0]
    ispec = [0, 0, 0]

    for light in p_sources:
        l = light[0:3]

        # calculating diffuse lighting, specular lighting, for use in lighting equation
        spec_light = [light[x+3] * constants[x+6]*angle for x in xrange(3)]
        ispec = [ispec[x] + (spec_light[x] if spec_light[x] > 0 else 0) for x in xrange(3)]
        diff_light = [light[x+3] * constants[x+3] * dot_product(normal, l) for x in xrange(3)]
        idiff = [idiff[x] + (diff_light[x] if diff_light[x] > 0 else 0) for x in xrange(3)]
        angle = pow(dot_product(sub_vectors(scalar_product(scalar_product(normal, dot_product(l, normal)), 2), l), view), 2)

    # lighting equation
    return [min(255, iamb[x] + idiff[x] + ispec[x]) for x in xrange(3)]
