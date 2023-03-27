import os
import tensorflow as tf

print("Tensorflow version: ", tf.__version__)

# MNIST datasetinden veriler çekiliyor, 
(train_images, train_labels), (test_images, test_labels) = tf.keras.datasets.mnist.load_data()

# verilerin ilk 1000 kaydı alınıyor
train_labels = train_labels[:1000]
test_labels = test_labels[:1000]

# veriler resim olduğu için resim üzerinde optimize edilme işlemleri
# yapılıyor, örneğin burada 28*28 lik resimleri doğrudan flatten katmanı kullanmadan
# flatten işlemi yapılmış ardından 0-255 arasındaki değerleri 0-1 arasındaki değerlere
# dönüştürerek makine öğrenmei için uygun hale geitrilmiş
train_images = train_images[:1000].reshape(-1, 28 * 28) / 255.0
test_images = test_images[:1000].reshape(-1, 28 * 28) / 255.0

# Define a simple sequential model
# basit ardışık model kullanılıyor
# ilk nöronu 512 katmanlı ve aktivasyonu relu
# daha önce yukarıda resimleri iki boyutludan bir boyutluya dönüştürmüşütük
# burada tek boyutlu 784 uzunlupunda bir dizi olduğunu belirmiş
# Dropout, aşırı uydurmayı önlemek için sinir 
# ağlarında yaygın olarak kullanılan bir düzenlileştirme 
# tekniğidir. Bir sinir ağındaki bırakma katmanı, eğitim 
# sırasında girdi birimlerinin belirli bir kısmını rastgele 
# "çıkarır" (yani sıfıra ayarlar). Bu, herhangi bir tek nöronun
# ağda çok önemli hale gelmesini önleme etkisine sahiptir ve ağı, 
# farklı girdi örnekleri arasında alakalı olan daha sağlam 
# özellikleri öğrenmeye zorlar.

def create_model():
  model = tf.keras.Sequential([
    tf.keras.layers.Dense(512, activation='relu', input_shape=(784,)),
    tf.keras.layers.Dropout(0.2),
    tf.keras.layers.Dense(10)
  ])

# model derlenir, optimize elemanı adam seçilir
# kayıp fonksiyonu ve metrik değerleri belirlenir
  model.compile(optimizer='adam',
                loss=tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True),
                metrics=[tf.keras.metrics.SparseCategoricalAccuracy()])

# ortaya model çıkmış olur
  return model

# Create a basic model instance
model = create_model()

# Display the model's architecture
model.summary()

# checkpointler modelin eğitimi sırasında ortasında başında sonunda 
# birden çok modeli çıktı olarak kaydetmemize yarayan noktalar oluşturur

# checkpointlerin klasör konumu belirlenir
checkpoint_path = "0003SaveAndLoadModel/checkpoints"
checkpoint_dir = os.path.dirname(checkpoint_path)

# Create a callback that saves the model's weights
cp_callback = tf.keras.callbacks.ModelCheckpoint(filepath=checkpoint_path,
                                                 save_weights_only=True,
                                                 verbose=1)

# Train the model with the new callback
model.fit(train_images, 
          train_labels,  
          epochs=10,
          validation_data=(test_images, test_labels),
          callbacks=[cp_callback])  # Pass callback to training

# This may generate warnings related to saving the state of the optimizer.
# These warnings (and similar warnings throughout this notebook)
# are in place to discourage outdated usage, and can be ignored.

# checkpointlerden önceki oluşturulan model tekrar kullanılabilir
# Evaluate the model
loss, acc = model.evaluate(test_images, test_labels, verbose=2)
print("Untrained model, accuracy: {:5.2f}%".format(100 * acc))

# Loads the weights
model.load_weights(checkpoint_path)

# Re-evaluate the model
loss, acc = model.evaluate(test_images, test_labels, verbose=2)
print("Restored model, accuracy: {:5.2f}%".format(100 * acc))

# tüm modeli kaydetmek için 
model.save('saved_model/my_model')

# sonradan bu model tekrar kullanılabilir
new_model = tf.keras.models.load_model('saved_model/my_model')

# Check its architecture
new_model.summary()