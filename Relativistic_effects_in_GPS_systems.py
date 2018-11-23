

def var():
    R_E=float(6371*10**3) # m
    M_E=float(5.9736*10**24) # kg
    G=float(6.674*10**-11) # N kg^–2 m^2 
    c=float(2.99792458*10**8)
    
    return G, M_E, R_E, c

def print_orbit():
    print("""\nRelativistic time dilation calculator for GPS atomic clock systems  
    Low Earth orbit (LEO): 160-2000 km
    Medium Earth orbit (MEO): 2000-35000 km
    High Earth orbit (HEO) : > 35786 km
    """)

#--------------------- GR -------------------------

# The coordinate time interval at R_E and R_E + h are related by 
def user_input():
    h=float(input("Please enter the height of the satellite in km: "))
    t=float(input("Please enter a time period to consider in days: "))
    return h, t

# Since \delta T will be small, we use the first few terms of a Taylor expansion to evaluate
# The expansion (1+x/2)(1-y/2)\approx 1+x/2-y/2, evaluating and reducing
def taylor_expansion():
    x=(M_E*G)/(c**2*(R_E + h*10**3))  
    y=(M_E*G)/(c**2*(R_E)) 
    z=-((M_E*G*h*10**3)/((c**2)*R_E*(R_E+h*10**3)))*t*24*3600*10**6#microseconds
    zaf=-((M_E*G*h*10**3)/((c**2)*R_E*(R_E+h*10**3)))
    return z,zaf

def print_general():
    print("\nThe general relativistic contribution to time dilation over the period of"
    ,t ,"days","is",round(z,2),
   "µs (2 d.p) \nWhere the negative sign indicates the satellites clock runs more rapidly than a ground based one.")

#----------------------- SR --------------------------
def special_time():
    r=((G*M_E)/(2*c**2*(R_E+h*10**3)))*t*24*3600*10**6
    raf=((G*M_E)/(2*c**2*(R_E+h*10**3)))
    return r,raf
def print_special():
    print("\nThe special relativistic contribution to time dilation over the period of",t,
          "days","is",round(r,2),
          "µs (2 d.p) \nWhere the positive sign indicates the satellites clock runs more slowly than a ground based one.")

#----------------------- Combined --------------------------
def print_comb():
    s=r+z
    error=c*s*10**-9*(-1)
    af=raf-zaf
    freq=((1-af)*10.23)
    print("\nThe combined relativistic contribution to time dilation over the period of",t,
          "days","is",round(s,2),
          "µs (2 d.p) ")
    print("\nSince the basis of GPS is accurate timing of radio pulses, over the period",t,
          "days","this could lead to a distance error of up to ",round(error,1),"km")
    print("The nominal frequency of pulses 10.23 MHz should be adjusted to ", freq,"MHz")
   

#---------------------- Main programme -----------------
G, M_E, R_E, c = var() # m/s 
print_orbit()
h,t=user_input()
z,zaf= taylor_expansion()
print_general()
r,raf=special_time()
print_special()
print_comb()
input("")








