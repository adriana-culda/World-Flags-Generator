import cv2

imagine_alba = cv2.imread("D:\PCLP2\Steaguri\imagine.jpg")
dim=(900,600)
imagine=cv2.resize(imagine_alba,dim,interpolation=cv2.INTER_AREA)

def steag_Bahrain(): 
    imagine[::]=(38, 17, 206)
    imagine[:,0:200]=(255,255,255)
    for i in range(0, 600):
     for j in range(200, 900):
        if j <350 * (1 - abs(i - 300) / 140): # triunghi mijloc
            imagine[i, j] = (255,255,255)
        if j <350 * (1 - abs(i-180) / 140): # triunghiuri partea de sus
            imagine[i, j] = (255,255,255)
        if j <350 * (1 - abs(i-60) / 140): 
            imagine[i, j] = (255,255,255)
        if j <350 * (1 - abs(i-420) / 140): # triunghiuri partea de jos
            imagine[i, j] = (255,255,255)
        if j <350 * (1 - abs(i-540) / 140):
            imagine[i, j] = (255,255,255)
        
def steag_Benin(): 
    imagine[::]=(38, 17, 206)
    imagine[0:300]=(22, 209, 252)
    imagine[:,0:350]=(81, 136, 0)

def steag_Bulgaria(): 
    imagine[::]=(255,255,255)
    imagine[200:400]=(0,128,0)
    imagine[400:600]=(0,0,255)

def steag_Cehia(): 
    imagine[::]=(255,255,255) 
    imagine[300:600]=(0,0,255)
    for i in range(0, 600):
      for j in range(0, 900):
        if j < 450 * (1 - abs(i - 300) / 300):
            imagine[i, j] = (255, 0, 0)

def steag_Congo(): 
    imagine[::]=(0, 221, 255)
    for i in range(0,600):
        for j in range(0,600-i):
           imagine[i,j]=(67, 173, 0)
    for i in range(0,600):
        for j in range(899,900-i,-1):
           imagine[i,j]=(38, 17, 206)
    
def steag_Emirate():
    imagine[::]=(255, 255, 255)
    imagine[0:200]=(81, 136, 0)
    imagine[400:600]=(0,0, 0)
    imagine[:,0:300]=(46, 16, 200)
    
def steag_Finlanda(): 
    imagine[::]=(255,255,255)
    imagine[:, 250:400] = (139,0,0)
    imagine[230:350] = (139,0,0)

def steag_Georgia():
    imagine[::] = (255, 255, 255)
    imagine[250:350, :] = (0, 0, 255)     
    imagine[:, 400:500] = (0, 0, 255) 
    
    imagine[100:150,125:275] = (0, 0, 255)  #stanga sus
    imagine[50:200,175:225] = (0, 0, 255)   

    imagine[100:150,625:775] = (0, 0, 255)  #dreapta sus
    imagine[50:200,675:725] = (0, 0, 255)

    imagine[450:500,125:275] = (0, 0, 255)  #stanga jos
    imagine[400:550,175:225] = (0, 0, 255)

    imagine[450:500,625:775] = (0, 0, 255)  #dreapta jos
    imagine[400:550,675:725] = (0, 0, 255)

def steag_Grecia(): 
    imagine[::]=(255,255,255)
    imagine[0:67]=(168, 56, 0)
    imagine[134:201]=(168, 56, 0)
    imagine[268:335]=(168, 56, 0)
    imagine[402:469]=(168, 56, 0)
    imagine[536:600]=(168, 56, 0)
    cv2.rectangle(imagine,(0,0),(334,334), (168, 56, 0),-1)
    imagine[0:335,133:200]=(255,255,255)
    imagine[133:200,0:335]=(255,255,255)
    
def steag_Islanda(): 
    imagine[::]=(91, 32, 0)
    imagine[:, 250:400] = (255,255,255) #alb
    imagine[230:350] = (255,255,255)
    imagine[:, 275:375] = (47, 12, 186) #rosu
    imagine[255:325] = (47, 12, 186)
    
def steag_Kuwait():
    imagine[::]=(255,255,255)
    imagine[0:215] = (61, 122, 0)
    imagine[386:600] = (38, 17, 206)
    for i in range(0, 600):
     for j in range(0, 900):
        if j<250 and j < 350 * (1 - abs(i - 300) / 300):
               imagine[i, j] = (0, 0, 0) 

def steag_Laos():
    imagine[::]=(38, 17, 206)
    imagine[150:450] = (168, 56, 0)
    cv2.circle(imagine, (450, 300), 120, (255, 255, 255), -1)

def steag_Maldive():
    imagine[::]=(0,0,204)
    cv2.rectangle(imagine,(150,150),(750,450), (0, 128, 0),-1)
    cv2.circle(imagine, (450, 300), 90, (255, 255, 255), -1)
    cv2.circle(imagine, (480, 300), 85, (0, 128, 0), -1)

def steag_Romania(): 
    imagine[::]=(255,255,255)
    imagine[:,0:300]=(127, 43, 0)
    imagine[:,300:600]=(22, 209, 252)
    imagine[:,600:900]=(38, 17, 206)
    
def steag_Tanzania():
    imagine[::]=(0, 0, 0)
    for i in range(0,600):        #galben
        for j in range(0,650-i):
           imagine[i,j]=(0, 209, 255)
    for i in range(0,600):        #verde
        for j in range(0,600-i):
           imagine[i,j]= (67, 173, 0)
    k=0
    for i in range(50,600):
        for j in range(899,900-k,-1):
           imagine[i,j]=(0, 209, 255)
        k+=1
    k=0
    for i in range(100,600):      #albastru
        for j in range(899,900-k,-1):
           imagine[i,j]=(219, 158, 0)
        k+=1
    
steaguri={
    "Bahrain":steag_Bahrain,
    "Benin":steag_Benin,
    "Bulgaria":steag_Bulgaria,
    "Cehia":steag_Cehia,
    "Congo":steag_Congo,
    "Emiratele Arabe Unite":steag_Emirate,
    "Finlanda":steag_Finlanda,
    "Georgia":steag_Georgia,
    "Grecia":steag_Grecia,
    "Islanda":steag_Islanda,
    "Kuwait":steag_Kuwait,
    "Laos":steag_Laos,
    "Maldive":steag_Maldive,
    "Romania":steag_Romania,
    "Tanzania":steag_Tanzania
}

f=open("D:\PCLP2\Steaguri\\tari.txt","r")
tari=[linie.strip() for linie in f.readlines()]
f.close()

for tara in tari:
    if(tara in steaguri):
        img=steaguri[tara]()
        cv2.imshow(f"{tara}", imagine)
    else:
        print(f"\n!!!Nu există steag pentru {tara}!!!")

cv2.waitKey(0)
cv2.destroyAllWindows()