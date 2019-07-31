import numpy as np
import os
import cPickle
import math
import tensorflow as tf
from skimage import io
from skimage.transform import resize
from keras.utils import to_categorical
from random import shuffle

shape_x, shape_y = 32, 32
num_input = shape_x * shape_y * 3
NUM_CLASSES = 10


def unpickle(file):
    import cPickle
    with open(file, 'rb') as fo:
        dict = cPickle.load(fo)
    return dict


def get_data_set(name="train"):
    x = None
    y = None

    datapath = '/'
    folder_name = "cifar10-python"

    if name is "train":
        for i in range(5):
            f = open(datapath + folder_name + '/data_batch_' + str(i + 1), 'rb')
            datadict = cPickle.load(f)
            f.close()

            _X = datadict["data"]
            _Y = datadict['labels']

            _X = np.array(_X, dtype=float) / 255.0
            _X = _X.reshape([-1, 3, shape_x, shape_y])
            _X = _X.transpose([0, 2, 3, 1])
            _X = _X.reshape(-1, shape_x * shape_y * 3)

            if x is None:
                x = _X
                y = _Y
            else:
                x = np.concatenate((x, _X), axis=0)
                y = np.concatenate((y, _Y), axis=0)

                # x, y = extract_data(x, y, num_classes, 500)

    elif name is "test":
        f = open(datapath + folder_name + '/test_batch', 'rb')
        datadict = cPickle.load(f)
        f.close()

        x = datadict["data"]
        y = np.array(datadict['labels'])

        x = np.array(x, dtype=float) / 255.0
        x = x.reshape([-1, 3, shape_x, shape_y])
        x = x.transpose([0, 2, 3, 1])
        x = x.reshape(-1, shape_x * shape_y * 3)

    return x, dense_to_one_hot(y)


def dense_to_one_hot(labels_dense, num_classes=NUM_CLASSES):
    num_labels = labels_dense.shape[0]
    index_offset = np.arange(num_labels) * num_classes
    labels_one_hot = np.zeros((num_labels, num_classes))
    labels_one_hot.flat[index_offset + labels_dense.ravel()] = 1

    return labels_one_hot

def random_mini_batches(X, Y, mini_batch_size=64, seed=0):
    m = X.shape[0]
    mini_batches = []
    np.random.seed(seed)

    permutation = list(np.random.permutation(m))
    shuffled_X = X[permutation,:,:,:]
    shuffled_Y = Y[permutation,:]

    num_complete_minibatches = math.floor(m/mini_batch_size)

    for k in range(0, num_complete_minibatches):
        mini_batch_X = shuffled_X[k * mini_batch_size : (k+1) * mini_batch_size, :, :, :]
        mini_batch_Y = shuffled_Y[k * mini_batch_size : (k+1) * mini_batch_size, :]
        mini_batch = (mini_batch_X, mini_batch_Y)
        mini_batches.append(mini_batch)

    if m % mini_batch_size != 0:
        mini_batch_X = shuffled_X[num_complete_minibatches * mini_batch_size : m, :, :, :]
        mini_batch_Y = shuffled_Y[num_complete_minibatches * mini_batch_size : m, :]
        mini_batch = (mini_batch_X, mini_batch_Y)
        mini_batches.append(mini_batch)

    return mini_batches


def shuffle_data(train, target):
    indices = range(train.shape[0])
    shuffle(indices)
    train_new = train[indices, :]
    target_new = target[indices, :]

    return train_new, target_new


def normalize_image(image_arr):
    rshp_image = []
    i = 0
    for image in image_arr:
        i += 1
        image = np.transpose(np.reshape(image, (3, 32, 32)), (1, 2, 0))
        image = resize(image, (shape_x, shape_y, 3), anti_aliasing=True)
        # io.imsave('/data/sunit/out/image_dump/' + str(i) + '.jpg', image)
        image = np.reshape(image, (-1))
        image = image / 255
        rshp_image.append(image)
    rshp_image_arr = np.array(rshp_image)
    print(rshp_image_arr.shape)
    return rshp_image_arr


def extract_data(data, labels, num_labels, samples_per_label):
    iter_arr = np.zeros((num_labels, 1))
    new_data = []
    new_labels = []

    for i in range(0, data.shape[0]):
        sample_data = data[i]
        sample_label = labels[i]

        if len(new_data) == num_labels * samples_per_label:
            break

        if iter_arr[sample_label] < samples_per_label:
            iter_arr[sample_label] += 1
            new_data.append(sample_data)
            new_labels.append(sample_label)
        else:
            continue

    return np.array(new_data), np.array(new_labels)


def forward_propagation_for_predict(X, parameters, L):
    A = X
    for l in range(1,L+1):
        Z = tf.add(tf.matmul(parameters['W' + str(l)], A), parameters['b' + str(l)])
        if l != L:
            A = tf.nn.relu(Z)

    return Z


def predict(X, parameters):
    tf_parameters = {}
    for l in range(1, L+1):
        tf_parameters['W' + str(l)] = tf.convert_to_tensor(parameters['W' + str(l)])

    x = tf.placehoolder("float", [shape_x * shape_y * 3, 1])
    z = forward_propagation_for_predict(x, tf_parameters)
    p = tf.argmax(z)

    sess = tf.Session()
    prediction = sess.run(p, feed_dict={x : X})

    return prediction