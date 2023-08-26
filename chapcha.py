import glob
import CaptchaCracker as cc

img_width = 200
img_height = 50

max_length = 6

characters = {'0', '1', '2', '3', '4', '5', '6', '7', '8', '9'}
weights_path = "./weights.h5"
AM = cc.ApplyModel(weights_path, img_width, img_height, characters)

target_img = "./sample/train_numbers_only/008469.png"

pred = AM.predict(target_img)

print(pred)