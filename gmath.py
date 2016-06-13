from math import sqrt

def calculate_normal( points, i ):
    #get as and bs to calculate the normal
    ax = points[i + 1][0] - points[ i ][0]
    ay = points[i + 1][1] - points[ i ][1]
    az = points[i + 1][2] - points[ i ][2]

    bx = points[i + 2][0] - points[ i ][0]
    by = points[i + 2][1] - points[ i ][1]
    bz = points[i + 2][2] - points[ i ][2]

    normal = [0,0,0]
    normal[0] = ay * bz - az * by
    normal[1] = az * bx - ax * bz
    normal[2] = ax * by - ay * bx

    return normal

def normalize(v):
    magnitude = sqrt(v[0]*v[0]+v[1]*v[1]+v[2]*v[2])
    if magnitude == 0:
        return 0
    return [v[x]/magnitude for x in xrange(3)]

def scalar_product(v, s):
    return [v[x]*s for x in xrange(len(v))]

def dot_product(v0, v1):
    return v0[0]*v1[0]+v0[1]*v1[1]+v0[2]*v1[2]

def add_vectors(v0, v1):
    return [v0[x]+v1[x] for x in xrange(len(v0))]

def sub_vectors(v0, v1):
    return [v0[x]-v1[x] for x in xrange(len(v0))]

def calculate_light(color, point_sources, constants, normal, view):
    iambient = [color[x]*constants[x] for x in xrange(3)]
    idiffuse = [0, 0, 0]
    ispecular = [0, 0, 0]

    for light in point_sources:
        l = light[0:3]

        diffuse_light = [light[x+3]*constants[x+3]*dot_product(normal, l) for x in xrange(3)]
        idiffuse = [idiffuse[x] + (diffuse_light[x] if diffuse_light[x] > 0 else 0) for x in xrange(3)]
        angle = pow(dot_product(sub_vectors(scalar_product(scalar_product(normal, dot_product(l, normal)), 2), l), view), 2)
        specular_light = [light[x+3]*constants[x+6]*angle for x in xrange(3)]
        ispecular = [ispecular[x] + (specular_light[x] if specular_light[x] > 0 else 0) for x in xrange(3)]

    return [min(255, iambient[x]+idiffuse[x]+ispecular[x]) for x in xrange(3)]