print("\033c\033[43;30m\ngive me a file to input? ")
filesvarcube="""b,b,b,a,b,b
a,b,b,a,a,b
a,a,b,b,a,b
b,a,b,b,b,b
b,b,a,a,b,a
a,b,a,a,a,a
a,a,a,b,a,a
b,a,a,b,b,a
b,b,b,b,b,a
a,b,b,a,b,a
a,a,b,a,a,a
b,a,b,b,a,a"""
filesvarpiramid="""b,b,b,a,b,b
b,b,a,a,b,a
b,b,b,b,b,a
a,b,a,a,b,b
b,b,b,c,a,c
a,b,b,c,a,c
b,b,a,c,a,c
a,b,a,c,a,c"""

filevarin=""
filevarout=""
var1=[]
var2=[]
var3=[]
var4=[]
start1=0
start2=0
start3=0
i=0
n=0
m=0
t=0
u=0
x=0
y=0
z=0
w=0
tlines=1
filesin="cube.txt"
filesin=input()
print("\033[43;30m\ngive me a file to output? ")
filesout="out.csv"
filesout=input()

r=1
#r=int(input())

f1=open(filesin,"r")
filevarin=f1.read()
f1.close()

var1=filevarin.split("\n")
start1=0
for n in var1:
    n=n.strip() 
    
    var2=n.split(",")
    
    if n!="" and n.find("#")<0:
        if len(var2)>4:
            if  var2[0].lower().strip()=="cube":
                var3=filesvarcube.split("\n")
                
                x=int(var2[1].strip())
                y=int(var2[2].strip())
                z=int(var2[3].strip())
                r=int(var2[4].strip())
                
                for m in var3:
                    m=m.strip()
                    if start1!=0:
                        filevarout=filevarout+"\n"
                    start1=start1+1
                    start2=0
                    start3=0
                    var4=m.split(",")
                    for t in var4:
                        t=t.strip()
                        if start3!=0:
                            filevarout=filevarout+","
                        if t.lower()=="b":
                            if start2==0:
                                filevarout=filevarout+str(x)
                            if start2==1:
                                filevarout=filevarout+str(y)
                            if start2==2:
                                filevarout=filevarout+str(z)
                        else:
                            if start2==0:
                                filevarout=filevarout+str(x+r)
                            if start2==1:
                                filevarout=filevarout+str(y+r)
                            if start2==2:
                                filevarout=filevarout+str(z+r)
                        start2=start2+1
                        start3=start3+1
                        if start2==3:
                            start2=0

            if  var2[0].lower().strip()=="pyramid":
                var3=filesvarpiramid.split("\n")
                
                x=int(var2[1].strip())
                y=int(var2[2].strip())
                z=int(var2[3].strip())
                r=int(var2[4].strip())
                
                for m in var3:
                    m=m.strip()
                    if start1!=0:
                        filevarout=filevarout+"\n"
                    start1=start1+1
                    start2=0
                    start3=0
                    var4=m.split(",")
                    for t in var4:
                        t=t.strip()
                        if start3!=0:
                            filevarout=filevarout+","
                        if t.lower()=="b":
                            if start2==0:
                                filevarout=filevarout+str(x)
                            if start2==1:
                                filevarout=filevarout+str(y)
                            if start2==2:
                                filevarout=filevarout+str(z)
                        elif t.lower()=="c":
                            if start2==0:
                                filevarout=filevarout+str(x+(r//2))
                            if start2==1:
                                filevarout=filevarout+str(y+(r//2))
                            if start2==2:
                                filevarout=filevarout+str(z+(r//2))
                        elif t.lower()=="a":
                            if start2==0:
                                filevarout=filevarout+str(x+(r))
                            if start2==1:
                                filevarout=filevarout+str(y+(r))
                            if start2==2:
                                filevarout=filevarout+str(z+(r))
                        start2=start2+1
                        start3=start3+1
                        if start2==3:
                            start2=0
        else:
            print("error on line :"+str(tlines))
    else:
        print(n)
    tlines=tlines+1
fa=open(filesout,"w") 
fa.write(filevarout)
fa.close()