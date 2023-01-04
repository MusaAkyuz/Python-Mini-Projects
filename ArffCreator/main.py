import shutil

file = open("dataSet.txt", "w+")

# Static area
file.write("@relation dataSet\n")
file.write("@attribute fileName string\n")
file.write("@attribute class {Zero, One, Two, Three, Four, Five, Six, Seven, Eight, Nine}\n")
file.write("@data\n")

# taking 500 images per class
# in dataset the image names between "image1" and "image1000"
for i in range(500):
    file.write("image0" + str(i) + ".png, Zero\n")
    shutil.copy("DigitDataset\\Zero\\image" + str(i + 1) + ".PNG", "ImageMixed\\image0" + str(i + 1) + ".PNG")
    file.write("image1" + str(i) + ".png, One\n")
    shutil.copy("DigitDataset\\One\\image" + str(i + 1) + ".png", "ImageMixed\\image1" + str(i + 1) + ".png")
    file.write("image2" + str(i) + ".png, Two\n")
    shutil.copy("DigitDataset\\Two\\image" + str(i + 1) + ".png", "ImageMixed\\image2" + str(i + 1) + ".png")
    file.write("image3" + str(i) + ".png, Three\n")
    shutil.copy("DigitDataset\\Three\\image" + str(i + 1) + ".png", "ImageMixed\\image3" + str(i + 1) + ".png")
    file.write("image4" + str(i) + ".png, Four\n")
    shutil.copy("DigitDataset\\Four\\image" + str(i + 1) + ".png", "ImageMixed\\image4" + str(i + 1) + ".png")
    file.write("image5" + str(i) + ".png, Five\n")
    shutil.copy("DigitDataset\\Five\\image" + str(i + 1) + ".png", "ImageMixed\\image5" + str(i + 1) + ".png")
    file.write("image6" + str(i) + ".png, Six\n")
    shutil.copy("DigitDataset\\Six\\image" + str(i + 1) + ".png", "ImageMixed\\image6" + str(i + 1) + ".png")
    file.write("image7" + str(i) + ".png, Seven\n")
    shutil.copy("DigitDataset\\Seven\\image" + str(i + 1) + ".png", "ImageMixed\\image7" + str(i + 1) + ".png")
    file.write("image8" + str(i) + ".png, Eight\n")
    shutil.copy("DigitDataset\\Eight\\image" + str(i + 1) + ".png", "ImageMixed\\image8" + str(i + 1) + ".png")
    file.write("image9" + str(i) + ".png, Nine\n")
    shutil.copy("DigitDataset\\Nine\\image" + str(i + 1) + ".png", "ImageMixed\\image9" + str(i + 1) + ".png")

