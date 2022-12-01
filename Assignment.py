

n= int(input("Enter the number of polygon points: "))
print("Enter x and y coordinate for polygon points: x y")

xvalue=[]
yvalue=[]
for i in range(n):
        x, y = map(float, input(f"{'Point'} {i+1} {':    '}").split())
        xvalue.append(x)
        yvalue.append(y)


print()
print(f"{'point':>0} {'x':>10} {'y':>15} ")
print("-" * 35)

for i in range(n):
    print(f"{i + 1:>0} {xvalue[i]:>14}  {yvalue[i]:>14}")
print()
print("Geometric characteristics:")


A=0
Sx=0
for p in range(n):
    Xa= (xvalue[p] + xvalue[p-1])
    Ya= (yvalue[p] - yvalue[p-1])
    A= (Xa*Ya)+A
Ax=A/2

for g in range(n):
     Xs = (xvalue[g] - xvalue[g-1])
     Ys = pow(yvalue[g],2) + ((yvalue[g] * yvalue[g-1]))+ pow(yvalue[g-1],2)
     Sx= (Xs*Ys)+Sx
Sx=Sx*(-1/6)

Sy=0
for t in range(n):
     Yd = (yvalue[t] - yvalue[t-1])
     Xd = pow(xvalue[t],2) + (xvalue[t] * xvalue[t-1]) + pow(xvalue[t-1],2)
     Sy= (Xd*Yd)+Sy
Sy=Sy*(1/6)

Ix=0
for l in range(n):
     XI=(xvalue[l] - xvalue[l-1])
     YI=pow(yvalue[l],3)+(pow(yvalue[l],2)*yvalue[l-1])+(pow(yvalue[l-1],2)*yvalue[l])+pow(yvalue[l-1],3)
     Ix= (XI*YI)+Ix
Ix=Ix*(-1/12)
Iy=0
for l in range(n):
     XI = (yvalue[l] - yvalue[l-1])
     YI=pow(xvalue[l],3)+(pow(xvalue[l],2)*xvalue[l-1])+(pow(xvalue[l-1],2)*xvalue[l])+pow(xvalue[l-1],3)
     Iy= (XI*YI)+Iy
Iy=Iy*(1/12)

Ixy=0
for l in range(n):
     XYI = (yvalue[l] - yvalue[l-1])
     INSX=  (3*(pow(xvalue[l],2)))+( 2* xvalue[l] *xvalue[l-1])+(pow(xvalue[l-1],2))
     INSY=  (3*(pow(xvalue[l-1],2)))+( 2* xvalue[l] *xvalue[l-1])+(pow(xvalue[l],2))
     IxyD= (yvalue[l] - yvalue[l-1]) * ((yvalue[l] * INSX) + (yvalue[l-1] * INSY))
     Ixy = IxyD + Ixy
Ixy=Ixy*(-1/24)
xt=Sy/Ax
yt=Sx/Ax
Ixt= Ix-(pow(yt,2)* Ax)
Iyt=Iy-pow(xt,2)*Ax
Ixyt=Ixy+xt*yt*Ax

#result

print(f"{'Ax:':>0} {format(Ax,'.2f'):>14}")
print(f"{'Sx:':>0} {format(Sx,'.2f'):>14}")
print(f"{'Sy:':>0} {format(Sy,'.2f'):>14}")
print(f"{'Ix:':>0} {format(Ix,'.2f'):>14}")
print(f"{'Iy:':>0} {format(Iy,'.2f'):>14}")
print(f"{'Ixy:':>0} {format(Ixy,'.2f'):>13}")
print(f"{'xt:':>0} {format(xt,'.2f'):>14}")
print(f"{'yt:':>0} {format(yt,'.2f'):>14}")
print(f"{'Ixt:':>0} {format(Ixt,'.2f'):>13}")
print(f"{'Iyt:':>0} {format(Iyt,'.2f'):>13}")
print(f"{'Ixyt:':>0} {format(Ixyt,'.2f'):>12}")
print("(Takyaldeen Alarmouty, 2022), BIMA+, Assignment")
print()
exit()


