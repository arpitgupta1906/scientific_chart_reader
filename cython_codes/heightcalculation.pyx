import cython

@cython.boundscheck(False)
cdef list heightcalculation(unsigned char [:,:] image):
    cdef int h,w,xy,xx,flag,i
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
                xy=y 
                xx=x 
                break
        if flag==1:
            break 
    
    y=yiniial=xy
    x=xx
    heightpixellist=[]


    while x<w-30:
        while image[y,x]==255 and x<w-10:
            x=x+1
        
        flag=0
        while image[y,x]==0 and y>10:
            flag=1
            y=y-1

        if flag==1:
            heightpixellist.append(yiniial-y)
            y=yiniial

        while image[y,x]==0 and x<w-10:
            x=x+1

    return heightpixellist
