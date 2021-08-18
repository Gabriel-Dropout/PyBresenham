from point import point
import numpy as np
import math
import cv2

def bresenham(p1, p2, img):
    dx=abs(p2.x - p1.x)
    dy=abs(p2.y - p1.y)

    if(dy<dx):#x방향을 기준으로 그리기
        if(p1.x>p2.x): p1,p2 = p2,p1 #p1.x<p2.x 조정
            
        inc= 1 if (p1.y<p2.y) else -1 #y축 반전 여부

        #초기좌표 설정
        p = 2*dy - dx
        x=p1.x; y=p1.y;
        img[y][x]=255

        #반복
        for i in range(p1.x+1, p2.x+1):
            if p>0:
                p = p + 2*dy - 2*dx
                x+=1
                y+=inc
            else:
                p = p + 2*dy
                x+=1
                  
            img[y][x]=255
    else:#y방향을 기준으로 그리기
        if(p1.y>p2.y): p1,p2 = p2,p1 #p1.y<p2.y 조정
            
        inc= 1 if (p1.x<p2.x) else -1 #x축 반전 여부

        #초기좌표 설정
        p = 2*dx - dy
        y=p1.y; x=p1.x;
        img[y][x]=255

        #반복
        for i in range(p1.y+1, p2.y+1):
            if p>0:
                p = p + 2*dx - 2*dy
                y+=1
                x+=inc
            else:
                p = p + 2*dx
                y+=1
                  
            img[y][x]=255


if __name__=="__main__":
    z = np.zeros((120, 120), dtype=np.uint8)
    zoom = 6

    def mouse_event(event, x, y, flags, param):
        if event == cv2.EVENT_MOUSEMOVE:
            z = np.zeros((120, 120), dtype=np.uint8)
            bresenham(point(60, 60), point(int(x/zoom), int(y/zoom)), z)
            ims = cv2.resize(z, (int(120*zoom), int(120*zoom)), interpolation=cv2.INTER_NEAREST)
            cv2.imshow('image', ims)


    ims = cv2.resize(z, (int(120*zoom), int(120*zoom)), interpolation=cv2.INTER_NEAREST)
    cv2.imshow('image', ims)
    cv2.setMouseCallback("image", mouse_event)
