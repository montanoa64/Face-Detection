

import cv2
import numpy as np
import os

###################################################################################################

##################
# GET THE NAME OF ALL THE JPG FILES
def getNames():
    listOfNames = []
    namefile = open("all_file.txt","r")
    if namefile is None:
        system("pause")
        return
    else:
        listOfNames = namefile.read().split('\n')
        return listOfNames

def main():
    #####################
    # PATH TO ALL THE IMAGES
    path = "P2E_S5_C1.1/"
    ####################################
    #       LOAD CascadeClassifier
    face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_alt2.xml')
    #####################
    #  GET ONE IMAGE TO SET UP THE VIDEO SIZE
    imager = cv2.imread("P2E_S5_C1.1/00000000.jpg")
    #####################################
    #    EXTRACT SIZE OF IMGAE
    height, width,  chanel = imager.shape
    ###########################
    # SET UP THE OUTPUT VIDEO FILE
    outvid = cv2.VideoWriter('output.avi',-1,20.0 ,(width,height))
    #####
    # SET UP THE FONT FOR THE ID
    font = cv2.FONT_HERSHEY_SIMPLEX
    lists = getNames()
    id=0
    facenum=0
    for l in lists:
        pathx = path + l
        imgx = cv2.imread(pathx)
        ########
        # IF IMAGE IS EMPTY BREAK
        if imgx is None:
            print "Press any key on video screen"
            break
        else:
            ##############
            #GET THE IMAGE AND TURN IT GRAY
            gray = cv2.cvtColor(imgx,cv2.COLOR_BGR2GRAY)
            #############
            # DETECT FACES IN IMAGE
            faces = face_cascade.detectMultiScale(gray,1.3,5)
            #############
            #  FOR LOOP TO DRAW THE RECTANGLE AND ID
            for (x,y,w,h) in faces:
                ############
                # CHECKS IF RECTANGLE HAS CHANGE SIZE
                if isinstance(faces, tuple) == False:
                    id = id +1
                ######
                # DRAWS RECTANGLE
                cv2.rectangle(imgx,(x,y),(x+w,y+h),(255,0,0),2)
                ######
                # DRAWS ID
                cv2.putText(imgx,'#'+str(id),(int(x-w*.4),y+h+25), font, 1,(255,255,255),1,cv2.LINE_AA)
            #####
            # SAVES IMAGE TO VIDEO
            outvid.write(imgx)
            ######
            # SHOWS FRAMES TO USER WHILE PROGRAM RUNS
            cv2.imshow('nada',imgx)
        ####
        # USE TO RUN IMAGES W/O PRESSING KEYS
        cv2.waitKey(2)
    ######
    # RELEASES VIDEO
    outvid.release()
    #######
    # PRESS ANY KEY TO EXIT PROGRAM
    cv2.waitKey()
    cv2.destroyAllWindows()
    return

###################################################################################################
if __name__ == "__main__":
    main()
