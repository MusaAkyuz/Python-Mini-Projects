import tensorflow as tf
import matplotlib.pyplot as plt

#Versiyonunu inceleme
print("TensorFlow version:", tf.__version__)

#veri setinin yüklenmesi
#tensorfow veri setleri ile birlikte geliyor
#internet ortamından bu verileri çekebiliyoruz

mnist = tf.keras.datasets.mnist

#XTR x train
#YTR y train
#xts x test
#yts y test

#downloaded datas
(xtr, ytr),(xts, yts) = mnist.load_data()
xts, xts = xtr / 255.0, xts / 250.0

# Building model
# buradaki model tasarlama işlemini araştır
model = tf.keras.models.Sequential(
    [
        tf.keras.layers.Flatten(input_shape=(28,28)),
        tf.keras.layers.Dense(128, activation='relu'),
        tf.keras.layers.Dropout(0.2),
        tf.keras.layers.Dense(10)
    ]
)

# xtr[:1] neymiş görelim
# print(xtr[:1])
# 28 x 28 piksellik el yazısı çizimlerden oluşuyor
plt.imshow(xtr[0])
plt.show()

# tahminleri görürüz
predictions = model(xtr[:1]).numpy()
print(predictions)

# bu tahminleri olasılıklara dönüştürmek için
probability = tf.nn.softmax(predictions).numpy()
print(probability)

# bir loss fonksiyonu, tanımlayabiliriz
# kayıp fonksiyonu eğer model doğru sınıftaysa 0 olur
lossFunction = tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True)
lossValue = lossFunction(ytr[:1], predictions).numpy()
print(lossValue)

#eğitime başlamadan önce optimize edilir
model.compile(optimizer='adam',
              loss=lossFunction,
              metrics=['accuracy'])

# model eğitilir
model.fit(xtr, ytr, epochs=10)

#model test edilir
model.evaluate(xts, yts, verbose=2)

predictions = model(xtr[:1]).numpy()
print(predictions)

