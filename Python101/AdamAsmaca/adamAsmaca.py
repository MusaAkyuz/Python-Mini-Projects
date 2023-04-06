# Problem Seti 2, adamAsmaca.py
# İsim:
# Ortak çalişanlar:
# Harcanan zaman:

# Adam Asmaca Oyunu
#------------------------------------
# Yardimci kod
# Bu yardimci kodu anlamaniza gerek yok,
# ama fonksiyonlari nasil kullanacağini bilmeniz gerekecek
# (dökümanlari okuduğunuzdan emin olun!)
import random
import string

WORDLIST_FILENAME = "kelimeler.txt"


def load_words():
    """
    Geçerli kelimelerin bir listesini döndürür.
    Kelimeler küçük harf dizileridir.
    Kelime listesinin boyutuna bağli olarak,
    bu fonksiyonun tamamlanmasi biraz zaman alabilir.
    """
    print("Dosyadan kelime listesi yükleniyor...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "kelimeler yüklendi.")
    return wordlist



def choose_word(wordlist):
    """
    wordlist (list): kelime listesi(strings)
    
    Kelime listesinden rastgele bir kelime döndürür
    """
    return random.choice(wordlist)

# yardimci kodun sonu

#------------------------------------

# Programdaki herhangi bir yerden erişilebilmesi için
# kelime listesini değişken kelime listesine yükleyin
wordlist = load_words()


def is_word_guessed(secret_word, letters_guessed):
    '''
    secret_word: string, kullanicinin tahmin ettiği kelime;
    tüm harflerin küçük olduğunu varsayar
    letter_guessed: şimdiye kadar hangi harflerin tahmin edildiği (harflerin listesi);
    tüm harflerin küçük olduğunu varsayar
    returns: boolean, secret_word'ün tüm harfleri letter_guessed içindeyse True;
    Aksi takdirde yanliş
    '''
    for letter in secret_word:
        if letter not in letters_guessed:
            return False

    return True    




def get_guessed_word(secret_word, letters_guessed):
    '''
    secret_word: string, kullanicinin tahmin ettiği kelime
    letter_guessed: şimdiye kadar hangi harflerin tahmin edildiği (harflerin listesi)
    returns: harflerden, alt çizgilerden (_) ve şu ana kadar secret_word
    içindeki hangi harflerin tahmin edildiğini gösteren boşluklardan oluşan dize.
    '''
    result = ""
    for letter in secret_word:
        if letter in letters_guessed:
            result += " " + letter
        else:
            result += " _"

    return result          



def get_available_letters(letters_guessed):
    '''
    letter_guessed: şimdiye kadar hangi harflerin tahmin edildiği (harflerin listesi)
    returns: dize (harfler), hangi harflerin henüz tahmin edilmediğini temsil eden harflerden oluşur.
    '''
    result = ""
    for letter in string.ascii_lowercase:
        if letter not in letters_guessed:
            result += letter

    return result        
    
    

def adamAsmaca(secret_word):
    '''
    secret_word: string, tahmin edilecek gizli kelime.
    Etkileşimli bir Adam Asmaca oyununu başlatir.
    * Oyunun başinda, kullaniciya secret_word'ün kaç harf içerdiğin
    ve kaç tahminle başladiğini bildirin
    * Kullanici 6 tahminle başlamalidir
    * Her turdan önce kullaniciya kaç tahmin kaldiğini ve
    kullanicinin henüz tahmin etmediği harfleri göstermelisiniz.
    * Kullanicidan tur başina bir tahmin vermesini isteyin
    Kullanicinin bir mektup yazdiğindan emin olmayi unutmayin!
    * Kullanici, her tahminden hemen sonra tahminlerinin bilgisayarin
    kelimesinde görünüp görünmediği hakkinda geri bildirim almalidir.
    * Her tahminden sonra, o ana kadar kismen tahmin edilen kelimeyi
    kullaniciya göstermelisiniz.
    Problem yaziminda detaylandirilan diğer sinirlamalari takip eder.
    '''
    vowels = "aeiou"
    letter_guessed = []
    remain_guess = 6
    remain_warning = 3

    print("Adam asmaca oyununa hoş geldiniz!")
    print(len(secret_word), " harf uzunluğunda bir kelime düşünüyorum!")
    print(remain_warning, " uyariniz kaldi.")
    print("--------------------------------------------")

    while remain_guess > 0:
        print(remain_guess, " tahmininiz kaldi.")
        print("Kullanilabilir harfler: ", get_available_letters(letters_guessed=letter_guessed))

        guesed_letter = input("Lütfen bir harf tahmin edin: ")
        
        # buraya kontrol yazılacak
        if(len(guesed_letter) != 1 or not str.isalpha(guesed_letter)):
            print("Hata! Bu geçerli bir harf değil.", end=" ")
            if(remain_warning >= 1):
                remain_warning -= 1
                print(remain_warning, " uyariniz kaldi.", end="")
            else:
                remain_guess -=1  
                print("Hiçbir uyariniz kalmadigindan bir tahmininizi kaybedersiniz")  
            continue    
        else:    
            guesed_letter = str.lower(guesed_letter)
            if(guesed_letter in letter_guessed):
                if(remain_warning >= 1):
                    remain_warning -= 1
                else:
                    remain_guess -=1 
                print("Hata! Bu harfi zaten tahmin ettin. Artik ", remain_warning, " uyariniz var:", end="")
            else:
                letter_guessed.append(str.lower(guesed_letter))
                if(guesed_letter in secret_word):
                    print("İyi tahmin:", end="")
                else:
                    print("Hata! O harf bu kelimede yok:", end="") 
                    if(guesed_letter in vowels):
                        remain_guess -= 1
                    remain_guess -= 1    
        
        print(get_guessed_word(secret_word=secret_word, letters_guessed=letter_guessed))
        print("--------------------------------------------")     

        if(is_word_guessed(secret_word=secret_word, letters_guessed=letter_guessed)):
            print("Tebrikler Kazandiniz!")
            print("Bu oyun için toplam puaniniz:", end="")
            print(len(set(secret_word)) * remain_guess)
            break

    if(remain_guess <= 0):
        print("Üzgünüm, tahmininiz kalmadi. Kelime başkaydi")  


# Adam asmaca işlevinizi tamamladiğinizda, dosyanin
#en altina gidin ve test edilecek ilk iki satirin yorumunu kaldirin
# (ipucu: kendi testinizi yaparken kendi secret_word'ünüzü
# seçmek isteyebilirsiniz)

# -----------------------------------



def match_with_gaps(my_word, other_word):
    '''
    my_word: _ karakterli dize, gizli kelimenin geçerli tahmini
    other_word: string, normal İngilizce kelime
    returns: boolean, True, eğer my_word'ün tüm gerçek harfleri other_word'ün karşilik gelen harfleriyle eşleşiyorsa veya harf özel sembol _ ise ve my_word ile other_word ayni uzunluktaysa; Aksi takdirde False:
    '''
    other_word = other_word.replace(" ", "")

    if(len(my_word) == len(other_word)):
        for i in range(len(my_word)):
            if(my_word[i] == "_"):
                continue
            if(my_word[i] != other_word[i]):
                return False
        return True    
    else:
        return False    


def show_possible_matches(my_word):
    '''
    my_word: _ karakterli dize, gizli kelimenin geçerli tahmini
    returns: hiçbir şey, ancak kelime listesindeki my_word ile eşleşen
    her kelimeyi yazdirmalidir.
    adamAsmaca ile bir harf tahmin edildiğinde, o harfin gizli kelimede
    geçtiği tüm pozisyonlarin ortaya çiktiğini unutmayin.
    Bu nedenle, gizli harf(_ ) zaten ortaya çikmiş olan kelimedeki
    harflerden biri olamaz.
    '''
    my_word = my_word.replace(" ", "")
    result = []

    for word in wordlist:
        if(match_with_gaps(my_word=my_word, other_word=word)):
            result.append(word)
            
    if len(result) > 0:
        return result
    else:
        return "Hiçbir sonuç bulunamadi!"


def adamAsmaca_ipuclu(secret_word):
    '''
    secret_word: string, tahmin edilecek gizli kelime.
    Etkileşimli bir Adam Asmaca oyunu başlatir.
    * Oyunun başinda, kullaniciya secret_word'ün kaç harf içerdiğini ve
    kaç tahminle başladiğini bildirin.
    * Kullanici 6 tahminle başlamalidir
    * Her turdan önce kullaniciya kaç tahmin kaldiğini ve kullanicinin
    henüz tahmin etmediği harfleri göstermelisiniz.
    * Kullanicidan tur başina bir tahmin vermesini isteyin.
    Kullanicinin bir harf tahmin ettiğini kontrol ettiğinizden emin olun.
    * Kullanici, her tahminden hemen sonra tahminlerinin bilgisayarin
    kelimesinde görünüp görünmediği hakkinda geri bildirim almalidir.
    * Her tahminden sonra, o ana kadar kismen tahmin edilen kelimeyi
    kullaniciya göstermelisiniz.
    * Tahmin sembolü * ise, kelime listesindeki mevcut tahmin edilen
    kelimeyle eşleşen tüm kelimeleri yazdirin.
    Problem yaziminda detaylandirilan diğer sinirlamalari takip eder.
    '''
    vowels = "aeiou"
    letter_guessed = []
    remain_guess = 6
    remain_warning = 3

    print("Adam asmaca oyununa hoş geldiniz!")
    print(len(secret_word), " harf uzunluğunda bir kelime düşünüyorum!")
    print(remain_warning, " uyariniz kaldi.")
    print("--------------------------------------------")

    while remain_guess > 0:
        print(remain_guess, " tahmininiz kaldi.")
        print("Kullanilabilir harfler: ", get_available_letters(letters_guessed=letter_guessed))

        guesed_letter = input("Lütfen bir harf tahmin edin: ")
        
        # buraya kontrol yazılacak
        if(guesed_letter == "*"):
            print("Olasi kelimeler şunlardır: ", end="")
            print(show_possible_matches(my_word=get_guessed_word(secret_word=secret_word, letters_guessed=letter_guessed)))
            continue
        elif(len(guesed_letter) != 1 or not str.isalpha(guesed_letter)):
            print("Hata! Bu geçerli bir harf değil.", end=" ")
            if(remain_warning >= 1):
                remain_warning -= 1
                print(remain_warning, " uyariniz kaldi.", end="")
            else:
                remain_guess -=1  
                print("Hiçbir uyariniz kalmadigindan bir tahmininizi kaybedersiniz")  
            continue    
        else:    
            guesed_letter = str.lower(guesed_letter)
            if(guesed_letter in letter_guessed):
                if(remain_warning >= 1):
                    remain_warning -= 1
                else:
                    remain_guess -=1 
                print("Hata! Bu harfi zaten tahmin ettin. Artik ", remain_warning, " uyariniz var:", end="")
            else:
                letter_guessed.append(str.lower(guesed_letter))
                if(guesed_letter in secret_word):
                    print("İyi tahmin:", end="")
                else:
                    print("Hata! O harf bu kelimede yok:", end="") 
                    if(guesed_letter in vowels):
                        remain_guess -= 1
                    remain_guess -= 1    
        
        print(get_guessed_word(secret_word=secret_word, letters_guessed=letter_guessed))
        print("--------------------------------------------")     

        if(is_word_guessed(secret_word=secret_word, letters_guessed=letter_guessed)):
            print("Tebrikler Kazandiniz!")
            print("Bu oyun için toplam puaniniz:", end="")
            print(len(set(secret_word)) * remain_guess)
            break

    if(remain_guess <= 0):
        print("Üzgünüm, tahmininiz kalmadi. Kelime başkaydi")



# adamAsmaca_ipuclu işlevinizi tamamladiğinizda, yukaridaki adam asmaca
# fonksiyonunu çaliştirmak için kullanilan benzer iki satiri yorumlayin ve
# ardindan bu iki satirin yorumunu kaldirin ve test etmek için bu dosyayi çaliştirin!
# İpucu: Test ederken kendi secret_word'ünüzü seçmek isteyebilirsiniz.


if __name__ == "__main__":
    # pass

    # 2. bölümü test etmek için yukaridaki pass satirinda # işaretini kullanin ve aşağidaki iki satirda # işaretini silin
    # secret_word = choose_word(wordlist)
    # adamAsmaca(secret_word=secret_word)

###############
    
# 3. bölümü test etmek için yukaridaki satirlarlarda yeniden # işaretini kullanin ve aşağidaki iki satirda # işaretini silin

    secret_word = choose_word(wordlist)
    adamAsmaca_ipuclu(secret_word)
