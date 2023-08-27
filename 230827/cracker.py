import glob
import CaptchaCracker as cc

train_img_path_list = glob.glob("../captcha image/*.png")

img_width = 120
img_height = 40

CM = cc.CreateModel(train_img_path_list, img_width, img_height)

model = CM.train_model(epochs = 200)

model.save_weights("weights.h5")