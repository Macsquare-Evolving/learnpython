# s1=72
# s2=85
# r=(s2-s1)/s1
# print('{:.1f}%'.format(r*100))
#learn print
# def my_abs(x):
#     if x>=0:
#         return x
#     else:
#         return -x;
# def my_abs(x):
#     if not isinstance(x,(int, float)):
#         raise TypeError('bad operand type')
#     if x>=0:
#         return x
#     else:
#         return -x

# # print(my_abs(-99))
# # my_abs('a')
# import math
# def move(x,y,step,angle=0):
#     import math
#     nx=x+step*math.cos(angle)
#     ny=y-step*math.sin(angle)
#     return nx,ny
#练习题
import math

def quadratic(a,b,c):
    if b**2-4*a*c<0:
        return 'wrong'
    else:
        x1=(-b+math.sqrt(b**2-4*a*c))/(2*a)
        x2=(-b-math.sqrt(b**2-4*a*c))/(2*a)
        return x1,x2
    
