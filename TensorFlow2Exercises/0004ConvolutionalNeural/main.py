import tensorflow as tf
import matplotlib.pyplot as plt

# verilerin çekilmesi, CIFAR10 veri seti
(trImage, trLabel), (tsImage, tsLabel) = tf.keras.datasets.cifar10.load_data()

# piksel değerlerinin normalize edilmesi
trImage, tsImage = trImage / 255, tsImage / 255

# daha sonra kullanmak için sınıf isimlerini belirtiyoruz
# bunlar veri setinde 0 ile 9 arasındaki sayılar olarak tutuluyor
className = ['airplane', 'automobile', 'bird', 'cat', 'deer',
               'dog', 'frog', 'horse', 'ship', 'truck']

# birkaç resim gösterelim
# tüm resimler 10*10 boyutunda gösterilsin
# bir satırda 5 resim olsun
# resimlerin altında sınıfları yazsın
# ve tek seferde 25 resim gösterilsin
plt.figure(figsize=(10,10))
for i in range(25):
    plt.subplot(5,5, i+1)
    plt.xticks([])
    plt.yticks([])
    plt.grid(False)
    plt.imshow(trImage[i])
    plt.xlabel(className[trLabel[i][0]])
plt.show()

#convolution neural network model
model = tf.keras.models.Sequential()
 
model.add(tf.keras.layers.Conv2D(32, (3, 3), activation="relu", input_shape=(32, 32, 3)))
model.add(tf.keras.layers.MaxPooling2D((2, 2)))
model.add(tf.keras.layers.Conv2D(64, (3, 3), activation="relu"))
model.add(tf.keras.layers.MaxPooling2D((2, 2)))
model.add(tf.keras.layers.Conv2D(64, (3, 3), activation="relu"))


