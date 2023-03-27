import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt

# fashion datasetini yükleriz
fashionMnist = tf.keras.datasets.fashion_mnist
# resimleri çekeriz ederiz
(trImage, trLabel), (tsImage, tsLabel) = fashionMnist.load_data()

# Label	Class
# 0	    T-shirt/top
# 1	    Trouser
# 2	    Pullover
# 3	    Dress
# 4	    Coat
# 5	    Sandal
# 6	    Shirt
# 7	    Sneaker
# 8	    Bag
# 9	    Ankle boot

# sınıflara isim veriririz
class_names = ['T-shirt/top', 'Trouser', 'Pullover', 'Dress', 'Coat',
               'Sandal', 'Shirt', 'Sneaker', 'Bag', 'Ankle boot']

# veri setini inceleyebiliriz
# resimlerin adeti ve boyutu
print(trImage.shape)
# kaç adet resim olduğu
print(len(trLabel))
# sınıfların isimleri
print(trLabel)
# test resimleri adeti ve boyutu
print(tsImage.shape)
# test versetinini uzunlupu
print(len(tsLabel))

# daha detaylı inceleme
plt.figure()
plt.imshow(trImage[0])
plt.colorbar()
plt.grid(False)
plt.show()

# eğitim öncesi normalize edilir
trImage, tsImage = trImage / 255, tsImage / 255

# resimlere tekrar bakalım
plt.figure(figsize=(10,10))
for i in range(25):
    plt.subplot(5,5,i+1)
    plt.xticks([])
    plt.yticks([])
    plt.grid(False)
    plt.imshow(tsImage[i], cmap=plt.cm.binary)
    plt.xlabel(class_names[trLabel[i]])
plt.show()

# model kuruluyor
# flatten 2 boyutlu bir array i bir boyuta dönüştürür
# densler bir düğüm alanıdır. ilk katmnda 128 adet sinir ağı bulunur
# flattendaki her bir veri her bir dense ile bağlantılıdır, bu da öğrenmeyi
# gerçekleştir, en son katmnda 10 sinir ağı var ki bu da öğrenmek istediğimiz
# sınıf modeli ile aynı sayıda
model = tf.keras.Sequential([
    tf.keras.layers.Flatten(input_shape=(28,28)),
    tf.keras.layers.Dense(128, activation="relu"),
    tf.keras.layers.Dense(10)
])

# model derleme şeklini seçiyoruz
# adam yazan optimize eden fonksiyondur
# öğrenme oranı, beta değerleri gibi önceden belirli ifadeler 
# içerir, loss fonksiyonu eğitim esnasında modelin doğruluk oranını ölçer
# metric ise doğruluğu ölçer, bunu yaparken isabet oranına bakar 
model.compile(optimizer='adam',
              loss=tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True),
              metrics=['accuracy'])

# modeli eğitiyoruz
# öğrenmek için 10 tur atacak
# ağırlıkları bir tur sonunda belirlenen sinir ağları üzerinde tüm
# veri seti tekrar tur atacak bunu epoch ile belirliyoruz
# epoch değerini çok falzla vermek aşırı öğrenmeyi doğurur
# aşırı öğrenme ezberlemeye girer ve iyi değildir
model.fit(trImage, trLabel, epochs=10)

# modelin test karşısındaki hata ve doğruluk oranına bakalım
test_loss, test_acc = model.evaluate(tsImage,  tsLabel, verbose=2)

# modelin accurarcy değeri teste tabi tutulduktan sonra çıkan
# accurarcy değerinden büyükse bir diğer değişle test esnasında 
# doğruluğu daha az ise model aşırı öğrenmeye gitmiştir diyebiliriz
print('\nTest accuracy:', test_acc)

# eğitilen modeli görüntüler üzerinde tahmin yapacak şekilde
# dönüştürebiliriz, bunun için modelin üstüne SoftMax katmanı eklenir
probability_model = tf.keras.Sequential([model, 
                                        tf.keras.layers.Softmax()])

predictions = probability_model.predict(tsImage)
# ilk test resmi için her sınıf için olabilirlik değerini gösterir
print(predictions[0])
# bu da aralarında en büyünün hangi sınıfa ait olduğunu hızlıca bulur
print(np.argmax(predictions[0]))
#bakalım test sınıfındaki ilk değerin sınıfı ne
print(tsLabel[0])




