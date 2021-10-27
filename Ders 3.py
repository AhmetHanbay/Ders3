#!/usr/bin/env python
# coding: utf-8

# In[1]:


iscinineskimaası = int(input("isci maasını giriniz = "))
cocuksayısı = int(input("cocuk sayısı giriniz = " ))
iscininyenimaası = iscinineskimaası
if (cocuksayısı == 1):
    iscininyenimaası = iscinineskimaası * 1.05
else:
    if (cocuksayısı == 2):
        iscininyenimaası = iscinineskimaası * 1.10
    else:
        if (cocuksayısı >= 3):
                iscininyenimaası = iscinineskimaası * 1.15
print("iscinin yeni maası = ",iscininyenimaası) 


# In[11]:


iscinineskimaası = int(input("isci maası giriniz = "))
cocuksayısı = int(input("cocuk sayısını giriniz = "))
iscininyenimaası = iscinineskimaası
if (cocuksayısı==1):
    iscininyenimaası = iscinineskimaası * 1.05
else:
    if (cocuksayısı==2):
        iscininyenimaası = iscinineskimaası * 1.10
    else:
        if (cocuksayısı>=3):
            iscininyenimaası = iscinineskimaası * 1.15
print("iscinin yeni maası = ",iscininyenimaası)


# In[12]:


iscinineskimaası = int(input("isci maası giriniz = "))
cocuksayısı = int(input("cocuk sayısını giriniz = "))
iscininyenimaası = iscinineskimaası
if (cocuksayısı==1):
    iscininyenimaası = iscinineskimaası * 1.05
else:
    if (cocuksayısı==2):
        iscininyenimaası = iscinineskimaası *1.10
    else:
        if (cocuksayısı>=3):
            iscininyenimaası=iscinineskimaası* 1.15
print("iscinin yeni maası = ",iscininyenimaası)


# In[14]:


print("1:Toplama\n2:Çıkartma\n3:Çarpma\n4:Bölme")
c = float(input("Birinci sayıyı giriniz = "))
d = float(input("İkinci sayıyı giriniz = "))
a = int(input("İşlem seçiniz:"))
if (a==1):
    print("Toplama sonucu : ",c + d )
elif (a==2):
    print("Çıkartma sonucu = : ", c - d)
elif (a==3):
    print("Çarpma sonucu = : " , c * d)
elif(a==4):
    print("Bölme sonucu = : " , c / d)
else:
    print("Hatalı seçim \n İyi Günler ")


# In[7]:



print("1:Toplama\n2:Çıkartma\n3:Çarpma\n4:Bölme")
c = float(input("Birinci sayıyı giriniz = "))
d = float(input("İkinci sayıyı giriniz = "))
a = int(input("İşlem seçiniz:"))
if (a==1):
    print("Toplama sonucu : ",c + d )
elif (a==2):
    print("Çıkartma sonucu = : ", c - d)
elif (a==3):
    print("Çarpma sonucu = : " , c * d)
elif(a==4):
    print("Bölme sonucu = : " , c / d)
else:
    print("Hatalı seçim \n İyi Günler ")


# In[10]:


print("1:Toplama\n2:Çıkartma\n3:Çarpma\n4:Bölme")
c = float(input("Birinci sayıyı giriniz = "))
d = float(input("İkinci sayıyı giriniz = "))
a = int(input("İşlem seçiniz : "))
if (a==1):
    print("Toplama sonucu : " , c + d )
elif (a==2):
    print("Çıkarma sonucu : " , c - d )
elif (a==3):
    print("Çarpma sonucu : " , c * d )
elif (a==4):
    print("Bölme sonucu : " , c / d )
else:
    print("Hatalı seçim \n İyi Günler")


# In[6]:


import math
print("Çizgiye ait katsayıları giriniz: ")
a = int(input("a:"))
b = int(input("b:"))
c = int(input("c:"))
print("Daireye ait katsayıları giriniz:")
x = int(input("x:"))
y = int(input("y:"))
r = int(input("r:"))
d = abs(a*x + b*y + c) / math.sqrt( a**2 + b**2 )
print("Nokta uzaklığı=",d,"Yarıçap=",r)
if d>r:
    print("kesmiyor")
elif d==r:
    print("teğet")
else:
        print("kesiyor")


# In[7]:


import math
print(dir(math))


# In[8]:


x = 10
print(x)


# In[9]:


for x in range(10):
    print(x)


# In[12]:


for x in range(10):
    print(x, end = " ")


# In[1]:


for x in range(10):
    print(x)


# In[16]:


x = 1
while x<=20:
    print(x, end=" ")
    x = x +1


# In[18]:


x = 1
while x<100:
    print(x, end=" ")
    x = x + 1


# In[12]:


x = 60
while x<100:
    print(x, end=" ")
    x = x + 5


# In[4]:


print("Element     Value")

for x in range(10):
    print(x,"         ",2+x*2)


# In[16]:


for x in range(60,100,5):
    print(x, end=" ")


# In[18]:


for x in range(5):
    a = int(input("sayı : "))


# In[20]:


b = 0
for x in range(5):
    a = int(input("sayı : "))
    b += a
    print(b)


# In[27]:


Min = 0
Mak = 0
for x in range(5):
    a = int(input("sayı : "))
    if a < Min:
        
        Min = a
    if a > Mak:
            Mak = a
print("Maksimum=",Mak, "    Minimum=",Min)


# In[29]:


Min = a
Mak = a
for x in range(5):
    a = int(input("sayı : "))
    if a < Min:
        Min = a
    if a > Mak:
        Mak = a
print("Maksimum=",Mak,"     Minimum=",Min)


# In[33]:


Min = a
Mak = a
for x in range(10):
    a = int(input("Sayı giriniz : "))
    if a < Min:
        Min = a
    if a > Mak:
        Mak = a
print("Maksimum =",Mak,       "Minimum = ",Min)        


# In[6]:


iscinineskimaası = int(input("isci maası giriniz = "))
cocuksayısı = int(input("cocuk sayısını giriniz = "))
iscininyenimaası = iscinineskimaası
if (cocuksayısı == 1):
    iscininyenimaası = iscinineskimaası * 1.05
else:
    if (cocuksayısı == 2):
        iscininyenimaası = iscinineskimaası * 1.10
    else:
        if (cocuksayısı>=3):
                iscininyenimaası = iscinineskimaası * 1.15
print("iscinin yeni maası = ",iscininyenimaası)
                    
                
        
            


# In[6]:


k = 0
for x in range(5):
    l = int(input("Sayı : "))
    k += l
    print(k)
          
        


# In[5]:


Min = 0
Mak = 0
for x in range(5):
    a = int(input("Sayı giriniz = "))
    if a < Min :
        Min = a
    if a > Mak :
        Mak = a
print("Maksimum = ",  Mak , "Minimum = ",Min)


# In[11]:


N = int(input("N : "))
for x in range(1 , N+1):
    if (x%2) == 1 :
        print(x)
        


# In[12]:


N = int(input("N : "))
for x in range(1 , N + 1):
    if (N%x) == 0 :
        print(x)


# In[22]:


for harf in "Python":
    print(harf)


# In[29]:


for harf in "P y t h o n ":
    if harf == "h":
        break
    print(harf)
print("Program biti")


# In[32]:


for harf in "P y t h o n ":
    if harf == "h":
        continue
    print(harf)
print("Program bitti")


# In[34]:


a = int(input("a="))
b = int(input("b="))
sonuc = 1
for x in range (b):
    sonuc*=a
print(sonuc)

