import cython

@cython.boundscheck(False)
cdef list xaxiscoordinate(unsigned char [:,:] image):
    cdef int h,w,flag,y,x,i 
    h=image.shape[0]
    w=image.shape[1]
    flag=0
    for y in range(h-1,0,-1):
        for x in range(0,w*2//3,5):
            flag=1
            for i in range(0,5):
                if image[y,x+i]!=0:
                    flag=0
                    break
            if flag==1:
                return [y,x] 