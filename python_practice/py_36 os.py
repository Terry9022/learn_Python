import os
import shutil
n=eval(input())
if os.path.exists('files'):
    shutil.rmtree('files')
    
os.mkdir('files')
os.chdir('files')
for i in range(1,n+1):
    os.mkdir('f'+str(i))
p=os.listdir()
p.sort()
print(p)
os.rename('f1','folder1')
p=os.listdir()
p.sort()
print(p)
os.removedirs('folder1')
p=os.listdir()
p.sort()
print(p)
for i in os.listdir():
    os.removedirs(i)
os.chdir('../')
os.removedirs('files')
    
