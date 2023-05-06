import tkinter as tk
from tkinter import messagebox
import math

# Pencere oluşturmak için nesne oluşturulur
# Bu nesnenin özelliklerini değiştirerek ve metodlarını kullanarak
# pencereyi şekillendiririz
window = tk.Tk()

# title metodu Pencerenin başlığını, programın ismini belirtir
window.title("Logaritma ve Üs Hesaplama Programı")

# geometri metodu pencere boyutlarını ayarlamaya yarar
# buradaki 500 x eskesnindeki piksel sayısını
# 150 sayısı ise y eksenindeki piksel sayısını temsil eder
window.geometry("500x150")

# hgLabel ile penceremizde görünecek bir yazı nesnesini temsil ediyoruz
# Label ın hangi pencerede olacağını, üzerinde ne yazacağını ve fontunu belirttik
# place metodu ile de konumunu ayarlıyoruz
hgLabel = tk.Label(window, text="Hoşgeldiniz", font="Ariel 13")
hgLabel.place(relx=0.5, rely=0.2, anchor="center")

'''
    Bu kısımda kullanıcıdan veri almak için text alanları oluşturdum
    Öncesinde de bu text alanlarının içine ne yazılması gerektiğini
    belirten label lar yerleştirdim, konumlardaki anchor değerleri
    east(doğu), west(batı) şeklinde ve relx değerleri de bu anchor değerine
    göre uzaklıkları belirtiyor
'''
questionLabel = tk.Label(window, text="Birinci sayı : ", font="Ariel 13")
questionLabel.place(relx=0.3, rely=0.4, anchor="w")
userInput = tk.Entry(window, width=20)
userInput.place(relx=0.5, rely=0.4, anchor="w")

questionLabel2 = tk.Label(window, text="İkinci sayı : ", font="Ariel 13")
questionLabel2.place(relx=0.3, rely=0.6, anchor="w")
userInput2 = tk.Entry(window, width=20)
userInput2.place(relx=0.5, rely=0.6, anchor="w")

# Hesaplama işleminin başlaması için bir buton oluşturup
# bu butonun tıklandığında aktif olacak fonksiyonu tanımlıyorum
def Hesapla():
    try:
        # kullanıcıdan alınan verileri sayıya dönüştürürüz
        # hata olması durumunda ekrana hata mesajı fırlatan
        # message box kullanacağız bunun için try, except
        # modülünü kullanıyoruz
        x = int(userInput.get())
        y = int(userInput2.get())
        sqarti = x**y
        logg = math.log2(x)
        strn = f"x**y : {str(sqarti)} --- log(x) : {str(logg)}"
        hgLabel.configure(text=strn)
    except:
        messagebox.showwarning(title="Hata", message="Girdiler hatalıdır. Kontrol ediniz")
        raise

hesaplaButton = tk.Button(window, text="Hesapla", font="Ariel 10", fg="red", command=Hesapla)
hesaplaButton.place(relx=0.5, rely=0.8, anchor="center")

# mainloop metodu pencere açık kaldığı sürece programın çalışmasını
#ve sürekli açık kalmasını sağlar
window.mainloop()