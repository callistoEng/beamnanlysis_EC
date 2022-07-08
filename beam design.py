import math

print('DESIGN OF STEEL BEAM WITHOUT LATERAL TORTIONAL BUCKLING')
print('CHARACTERISTIC ACTIONS')
print('Permanent Action')
print('*self weight of the floor')

'''
def self_weight_of_floor():
    thickness = float(input('Please enter the thickness of the slab(m): '))
    area = float(input('Please enter the area of the slab(m*: '))
    density = float(input('Please enter the density of the concrete for the slab: '))
    span = float(input('Please enter the span of the beam supporting the slab: '))

    self_weight= (thickness * area * density)/span
    print('The self weight of the floor is ', str(self_weight), 'Kn/m')

self_weight_of_floor()
'''
w1 = 0


def self_weight_of_floors(thickness, area, density, span):
    self_weight = (thickness * area * density) / span
    global w1
    w1 = self_weight
    return self_weight


thickness = float(input('Please enter the thickness of the slab: '))
area = float(input('Please enter the area of the slab: '))
density = float(input('Please enter the density of the concrete for the slab: '))
span = float(input('Please enter the span of the beam supporting the slab: '))

result = self_weight_of_floors(thickness, area, density, span)
print('The self weight of the floor is ', str(result) , 'Kn/m')

print('*self weight of the finishes, screed and ceiling')

constant = float(input('Please enter the constant for finishes, screed and ceiling : '))
w2 = 0


def self_weight_of_finishes_and_screed():
    self_weight1= (constant * area)/span
    global w2
    w2 = self_weight1
    #print('The self weight of the finishes, screed and ceiling ', str(self_weight1), 'Kn/m')
    return self_weight1

print('The self weight of the finishes, screed and ceiling',self_weight_of_finishesAndScreed(), 'Kn/m')

Gk = w1 + w2

print('THE TOTAL PERMANENT ACTION ACTION, Gk IS: ', str(Gk), 'kN/m')

print('VARIABLE ACTIONS:')

Qk = 0


def imposed_load(qk):
    imposed_loads = (qk * area)/span
    global Qk
    Qk = imposed_loads
    #print('The self weight of the finishes, screed and ceiling ', str(self_weight1), 'Kn/m')
    return imposed_loads


qk = int(input('Enter the appropriate imposed load (qk(kN/m*2)) from EC1, table 6.2: '))
out = imposed_load(qk)
print('The variable action Qk is: ', str(out), 'kN/m')
print(Qk)
print('COMBINATION OF ACTIONS AT ULS:')

Fed = 0


def combination_of_actions_at_uls(zeta, gammaG, gammaQ):
    n = zeta * gammaG * Gk + gammaQ*Qk
    global Fed
    Fed = n
    return n


zeta = float(input('enter your value of zeta: '))
gammaG = float(input('enter your value of Yg: '))
gammaQ = float(input('enter your value of Yq: '))

out2 = combination_of_actions_at_ULS(zeta, gammaG, gammaQ)

print('The combination of actions at ULS is a UDL of value: ', str(out2), 'kN/m')

print('Assuming a simply supported beam')

print('The maximum moment My,ed occurs at the mid span for bending about the Y-Y axiz ')

Myed = (Fed * span**2)/8

print('The maximum moment My,ed is: ', str(Myed))

Vyed = (Fed * span)/2

print('The maximum moment Vy,ed at end support is: ', str(Vyed))

print('MEMBER SELECTION')

tf1 = 16
tw1 = 16
fy = 275

print('Assuming the norminal thickness of flange less than ',
      str(tf1),' mm and thickness of web less than ', str(tw1), 'mm,: yield strength = ', str(fy), 'N/mm*2')

print('SECTION PLASTIC MODULUS')

Wply = (Myed/fy) * 10**3

print('The plastic modulus Wpl,y: ', str(Wply), 'cm*3')

print('from British standards steel tables, ')

reqWply = Wply * 2

print('Try section with Wpl,y: ', str(reqWply))

print('SECTION DIMENSIONS AND PROPERTIES')

h = float(input('Depth'))
b = float(input('Breadth'))
#try:
#    tw = float(input('tw'))
tw = float(input('tw'))
if tw > tw1:
    print('INVALID SECTION. ASSUMPTION ON tw <=16mm NOT SATISFIED')
    print('STOP THE PROGRAMME AND SELECT A SATISFACTORY SECTION')
    print('CALLIBOT WISHES YOU GOOD LUCK IN THE NEXT SELECTION')

else:
    print('Good Selection')
    tf = float(input('tf'))
    r = float(input('Radius'))
    hw = h - 2*tf
    iy = float(input('Radius of gyration iy'))
    iz = float(input('Radius of gyration iz'))
    Iy = float(input('Second moment of area Iy'))
    Iz = float(input('Second moment of area Iz'))
    Wely = float(input('Wel,y'))
    Welz = float(input('Wel,z'))
    Wply2 = float(input('Wpl,y'))
    Wplz = float(input('Wpl.z'))
    A = float(input('Area'))

print('CLASSIFICATION OF X-SECTION')

eplslon = math.sqrt(235/fy)

print('Epslon: ', str(eplslon))


print('OUTSTAND FLANGE CLASSIFICATION, C')

c = (b - tw - 2*2)/2

print('C: ', str(c))

cbytf = c/tf

print(' C/tf:', str(cbytf))

print('Checking Limiting Value For Classes...')

if cbytf <= 9*eplslon:
    print('Outstand flange is class 1 in compression')

elif cbytf <= 10*eplslon:
    print('Outstand flange is class 2 in compression')

else:
    print('Outstand flange is class 3 in compression')

print('WEB CLASSIFICATION')

c2 = h - 2*tf -2*r

print('C: ', str(c2))

cbytw = c2/tw

print(' C/tw:', str(cbytw))

print('Checking Limiting Value For Classes...')

if cbytw <= 72*eplslon:
    print('Web is class 1 in bending')

elif cbytw <= 83*eplslon:
    print('Web is class 2 in bending')

else:
    print('Web is class 3 in bending')


print('RESISTANCE OF BEAM CROSS-SECTION IN BENDING')

print('Moment Resistance of X-Section')
print('My,ed: ',str(Myed))

gammaMO = 1
Mcrd = (Wply * fy)/ gammaMO

print('Mc,rd: ', str(Mcrd))

CalMyedMcrdRatio = Myed/Mcrd

print('Ratio of My,ed to Mc,rd: ')

if CalMyedMcrdRatio <= 1:
    print('Design Bending Resistance of Section is Adequate')

else:
    print('Choose a bigger section!!')

print('SHEAR RESISTANCE')

print('Vy,ed: ', str(Vyed))

Av = A * 10**2 - 2*b*tf + (tw+2*r)*tf

print('Av: ',str(Av))

condition = hw*tw

print('nhwtw: ', condition)

Vplrd = ((Av * (fy/math.sqrt(3)))/1) * 10**-3

print('design shear resistance, Vpl,rd: ', str(Vplrd))

CalVyedVplrdRation = Vyed/Vplrd

print('The ratio of Vy,ed to Vpl,rd: ', str(CalVyedVplrdRation))

if CalVyedVplrdRation <= 1:
    print('Design shear Resistance of Section is Adequate')

else:
    print('Choose a bigger section!!')

print('SHEAR BUCKLING')

a = hw/tw
b = 72*eplslon

if a <= b:
    print('No shear buckling verification required')

print('DEFLECTION CHECK')

print('Characteristic load combination at SLS')
neta = 1*Gk + 1*Qk

print('combination at SLS: ', str(neta))

Actual_Deflection = (5 * neta * (span*1000)**4 * 10**-7)/(384 * 210 * Iy)

print('The actual deflection is: ', str(Actual_Deflection))

Ver_Deflection_Limit = span*1000/360

print('But the vertical deflection limit: ', str(Ver_Deflection_Limit))

if Ver_Deflection_Limit > Actual_Deflection:
    print('SectionOk In Deflection')

else:
    print('Since Actual Deflection is Greater Than Vertical Deflection Limit')
    print('Section Fail in Deflection')


















