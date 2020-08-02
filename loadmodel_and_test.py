import tensorflow as tf 
import numpy as np
from keras.models import load_model

#Load model
mymodel = tf.keras.models.load_model("../input/barplot-classification-vgg16/bargraph_classifier_50epoch_vgg16.h5")

#testing
IMAGE_SIZE    = (400, 400)
test_image = image.load_img("../input/supertest/GPICS1.png",target_size =IMAGE_SIZE )
test_image = image.img_to_array(test_image)

test_image = test_image.reshape((1, test_image.shape[0], test_image.shape[1], test_image.shape[2]))
test_image = preprocess_input(test_image)

prediction = mymodel.predict(test_image)
df = pd.DataFrame({'pred':prediction[0]})
# print(prediction[0])
df = df.sort_values(by='pred', ascending=False, na_position='first')
#print prediction
print(df)
print("Classification Type_index")
index=df[df == df.iloc[0]].index[0]
print(index)

#if want name too
Type=['abar_vertical_stacked', 'bar_horizontal_stacked', 'cvertical_bargraph', 'horizontal_bargraph']
print("Type_name")
print(Type[index])
