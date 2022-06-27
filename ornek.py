## TODO burada liste eklenecek
liste = ["Fatih","Gokhan","Mehmet","Ayşenur","Tahir","Banu","Bekir","Emre","Köksal","Mustafa","Talha","Özge","Özlem"]
folderName = "Egzersizler"
fileName = "selam.yaml" 
import os
for item in liste:
    if not os.path.exists(f"Egzersizler/{item}"):
        os.makedirs(f"Egzersizler/{item}")
    with open(f"Egzersizler/{item}/{fileName}", "w") as f:
        f.write(f"{item}")
    print(f"{item} klasörü oluşturuldu")
