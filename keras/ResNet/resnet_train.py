import numpy as np
from keras import layers
from keras_preprocessing import image
from keras.utils import layer_utils
from keras.applications.imagenet_utils import preprocess_input
import pydot
from IPython.display import SVG
from keras.utils.vis_utils import model_to_dot
from keras.utils import plot_model
from resnet_utils import *
from resnet_model import *
import scipy.misc
from matplotlib.pyplot import imshow

NUM_EPOCHS = 60

def one_epoch(train_X, train_Y, dev_X, dev_Y, batch_size, epoch_count):
    model.fit(train_X, train_Y, epochs=1, batch_size=batch_size)
    preds = model.evaluate(dev_X, dev_Y)
    print ("Epoch " + str(epoch_count) + " : Loss = " + str(preds[0]))
    print ("Test Accuracy = " + str(preds[1]))

if __name__ == '__main__':
    cifar_traindata, cifar_trainlabels = get_data_set("train")

    cifar_cvdata, cifar_cvlabels = get_data_set("test")

    cifar_cvdata, cifar_cvlabels = shuffle_data(cifar_cvdata, cifar_cvlabels)

    model = ResNet50(input_shape=(shape_x,shape_y,3), num_classes=NUM_CLASSES)

    model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])

    cifar_traindata = cifar_traindata.reshape([-1, 3, 32, 32])
    cifar_traindata = cifar_traindata.transpose([0, 2, 3, 1])
    cifar_cvdata = cifar_cvdata.reshape([-1, 3, 32, 32])
    cifar_cvdata = cifar_cvdata.transpose([0, 2, 3, 1])
    # model.fit(cifar_traindata, cifar_trainlabels, epochs=60, batch_size=32)

    for epoch in range(1, NUM_EPOCHS + 1):
        cifar_traindata, cifar_trainlabels = shuffle_data(cifar_traindata, cifar_trainlabels)
        one_epoch(cifar_traindata, cifar_trainlabels, cifar_cvdata, cifar_cvlabels, 32, epoch)


    preds = model.evaluate(cifar_cvdata, cifar_cvlabels)
    print ("Loss = " + str(preds[0]))
    print ("Test Accuracy = " + str(preds[1]))