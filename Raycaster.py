import numpy as np 
import os,time

class Ray: #ray class
  def __init__(self, source, direction):
    self.source = source
    self.direction = direction

  def trace(self,t):
    return self.source+t*self.direction
  
  def d(self,t):
    s=self.direction*t
    return np.sqrt(s[0]*s[0]+s[1]*s[1])
  def checkIntersection(self,line):
    srcR = self.source
    dirR = self.direction
    srcL = line[0,:]
    dirL = line[1,:]-line[0,:]
    if (dirR[0]*dirL[1] - dirR[1]*dirL[0])!=0:
      u = (srcR[1]*dirL[0] + dirL[1]*srcL[0] - srcL[1]*dirL[0] - dirL[1]*srcR[0])/(dirR[0]*dirL[1] - dirR[1]*dirL[0])
      v = (srcR[0] + dirR[0] * u - srcL[0]) / dirL[0]
    else:
      u,v=-1,-1
    if u>0 and v>0:
      R = u*dirR
      L = v*dirL
      return [self.trace(u),self.d(u),np.arccos(np.dot(R,L)/np.sqrt((R[0]*R[0]+R[1]*R[1])*(L[0]*L[0]+L[1]*L[1])))]
    else:
      return False


angle = 0

l = np.array([[0.0,1.0],[1.0,0.0]]) #line segment

os.system('cls')

while True: #let ray rotate emitted from the origin
  r = Ray(np.array([0.0,0.0]),np.array([np.cos(angle),np.sin(angle)]))
  inters = r.checkIntersection(l)
  
  if inters!=False: #output
    print("At angle {:.4f}Pi, ray makes an angle of {:.4f}rad at a distance of {:.4f} from source".format(angle/np.pi, inters[2], inters[1]))
  else:
    print("At angle {:.4f}Pi, ray does not intersect".format(angle/np.pi))
    
  time.sleep(0.1)
  os.system('cls')
  angle +=0.01 #increment angle
