## TODO burada liste eklenecek
liste = ["Fatih","Gokhan","Mehmet","Ayşenur","Tahir","Banu","Bekir","Emre","Köksal","Mustafa","Talha","Özge","Özlem","İbrahim"]
folderName = "Egzersizler"
fileName = "serviceEgzersiz" 
dosyatip = 1
import os
for item in liste:
    if not os.path.exists(f"Egzersizler/{item}"):
        os.makedirs(f"Egzersizler/{item}")
    if dosyatip == 1:
        with open(f"Egzersizler/{item}/{item}_{fileName}.yaml", "x") as f:
            f.write(f"# {item}")
    else:
        with open(f"Egzersizler/{item}/{item}_{fileName}.txt", "x") as f:
            f.write(f"# {item}")
    print(f"{item} klasörü oluşturuldu")




