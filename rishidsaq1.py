def isunique(a):
     flag="true"
     for i in range(len(a)):
          for j in range(i+1,len(a)):
               if a[i]==a[j]:
                    flag="false"
                    break
     print(flag)


a=input()
isunique(a)
