import cv2
import numpy as np
cap = cv2.VideoCapture(0)

if (cap.isOpened() is False):
    print("Unable to read camera feed")

frame_width = int(cap.get(3))
frame_height = int(cap.get(4))

frame_values=np.zeros((frame_height,frame_width))
limit=[]
conf=np.zeros(10)
while(True):
    ret, frame = cap.read()
    if ret:

        red = frame[..., 0]
        green = frame[..., 1]
        blue = frame[..., 2]
        gray = 0.21 * red + 0.72 * green + 0.07 * blue
        res=np.subtract(frame_values,gray)
        res2=np.where(abs(res)>20,255,0)
        res=np.uint8(res2)
        
        # part A of question 1 done above
        # part B of question 1 below

        topi=0
        topj=0

        countl=[]
        countr=[]

        for i in range(0,len(res)):
            if np.any(res[i]==255):
                topi=i
                break   
        for j in range(0,len(res[topi])):
            if res[topi][j]==255:
                topj=j
                break

        left=right=topj
        k=topi
        while k<len(res) :
            i=int(k)
            if left>0 and right<len(res[i])-1:
                left-=1
                right+=1
                countl.append(res[i][left])
                countr.append(res[i][right])
                # res[i][left]=res[i][right]=255
            k+=1.3

        
        countl = [countl[i] for i in range(len(countl)) if countl[i] != countl[i-1]]
        countr = [countr[i] for i in range(len(countr)) if countr[i] != countr[i-1]]


        if len(limit)<30:
            if len(countl)>0 and len(countr)>0:
                # print(countl,countr)
                ans=(len(countl)//4)+((len(countr))//3)
                if ans<6:
                    limit.append(ans)
        else:
            print(max(set(limit), key=limit.count))
            limit=[]


        frame_values=gray

        cv2.imshow('res', res)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    else:
        break
# print(res)
cap.release()
cv2.destroyAllWindows()