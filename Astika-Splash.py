
import os
os.system( printf "\033[3;32m"  ) 
aaa=input( Entre name The LisT :  )
os.system( clear ) 
os.system( printf "\033[3;36m" ) 
os.system( figlet Good - list )
print( By : Astika asplash Baglab((HakerDz)) ) 
print( - *29)
file=open(aaa, w ) 
aa=set([]) 
oio=set([])
#iio=set([112233,332211,000,445566, $ *1, $ *2, $ *3, @ *1, @ *2, @ *3, € *1, € *2, € *3, & *1, & *2, & *3, ¥ *1, ¥ *2, ¥ *3, * *1, * *2, * *3, + *1, + *2, + *3])
kk=1
while True :
    b=input( Entre {} :  .format(kk))
    if b== exit  :
        print( \033[3;36m )
        file.close()
        qq=open(aaa,  r  )
        ll=len(qq.readlines())
        os.system( printf "\033[3;31m" )
        print( - *60)
        print( >> {} Passwords in ---> {}  .format(ll, aaa))
        print( - *60) 
        break ;
    aa.add(b)
    for i in aa:
        if len(i) >= 6 and i not in oio :
            oio.add(i)
            file.write(i)
            file.write( \n )
            #for o in iio:
             #   uau= {}{} .format(i,o) 
              #  ubu= {}{}{} .format(o,i,o)
               # ucu= {}{}{}  .format(i,o,i)
                #if len(uau)>= 6:
                   # file.write(uau)
                  #  file.write( \n )
               # if len(ubu) >= 6 and ubu != uau :
                   # file.write(ubu)
                   # file.write( \n )
                #if len(ucu) >= 6 and ucu != uau and ucu != ubu:
                  #  file.write(ucu)
                  #  file.write( \n )

        c=b+i
        d=i+b
        if len(c) >= 6 :
            file.write(c)
            file.write( \n ) 
        if c != d and len(d) >= 6:
            file.write(d)
            file.write( \n )
    kk=int(kk)+1
    print( - *40)
