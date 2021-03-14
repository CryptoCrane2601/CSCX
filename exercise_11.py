def volume(w,h,d):
    return w * h * d

def area(w,h,d):
    return 2*w*h + 2*w*d + 2*d*h

w, h, d = input().split()
w = int(w)
h = int(h)
d = int(d)

volume1 = volume(w, h, d)
print('The volume of a ' +str(w) + ' by ' +str(h) + ' by ' +str(d) + ' box is ' +str(volume1) + '.')
area1 = area(w, h, d,)
print('The surface area of a ' +str(w) + ' by ' +str(h) + ' by ' +str(d) + ' box is ' +str(area1) + '.')



