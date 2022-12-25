
# yay sabitini bulma

def yay_sabiti_bul(m,g,d):
    print("{}={}".format("k",m*g/d))

### k = mg/d

# k = yay sabiti
# m = kütle
# g = yerçekimi ivmesi
# d = alınan mesafe,yol

yay_sabiti_bul(1,9.8,9.8)



# HOOKE YASASI  (yayın geri çağırıcı kuvveti)

def geri_çağırıcı_kuvvet(k,x):
    print("{}={}".format("F",-k*x))

### F = -k*x

# F = geri çağırıcı kuvvet
# k = yay sabiti
# x = uzama miktarı

geri_çağırıcı_kuvvet(1,5)



# Yay Kuvvetinin Yaptığı İş

def yay_kuvvetinin_isi(k,x,y):
    print("{} = {}".format("W", 1/2*k*x*x-1/2*k*y*y) )

# W =1/2*k*x*x-1/2*k*y*y

# W = toplam iş
# k= yay sabiti
# x = yayın denge noktasından ilk uzaklığı
# y = yayın denge noktasından son uzaklığı

yay_kuvvetinin_isi(1,0,10)





