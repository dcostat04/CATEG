#!/usr/bin/env python
# coding: utf-8

# In[1]:
##ESC TO EXIT AND SPACEBAR TO CAPTURE

import cv2


# In[2]:


import time


# In[3]:


start_time=time.time()
cam=cv2.VideoCapture(0)


# In[4]:


cv2.namedWindow("Capture Image")
img_counter=1


# In[5]:


while True:

    ret,frame=cam.read()
    cv2.imshow("Capture Image",frame)
    if not ret:
        break
    k=cv2.waitKey(1)
    if k%256 ==27:
        print ("Escape pressed ..")
        break
    curr_time=int(time.time())
    time_elasped=curr_time-int(start_time)
    if(time_elasped==20):
        break

    img_name = "{}.png".format(img_counter)
    cv2.imwrite('images/'+img_name, frame)
    print("{} written!".format(img_name))
    img_counter += 1
    time.sleep(5.00)
cam.release()

cv2.destroyAllWindows()


# In[ ]:





# In[ ]:


##will try to implement to remove the error: https://stackoverflow.com/questions/60007427/cv2-warn0-global-cap-msmf-cpp-674-sourcereadercbsourcereadercb-termina

