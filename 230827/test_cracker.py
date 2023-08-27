import CaptchaCracker as cc

weights_path = "./weights1.h5"

img_width = 120 
img_height = 40

max_length = 6

characters = {'0', '1', '2', '3', '4', '5', '6', '7', '8', '9'}

AM = cc.ApplyModel(weights_path, img_width, img_height, max_length , characters)

target_img = "./test.png"

pred = AM.predict(target_img)

print(pred)
