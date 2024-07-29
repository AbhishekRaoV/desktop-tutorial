'''This is the example ML Job to calculate the energy metrics'''
'''The code should contain a main function through which the implementation should be run''' 



import tensorflow as tf


def func():
    for i in range(10000):
        for j in range(10000):
            t=i*2

def train_model():
    #func()
    mnist = tf.keras.datasets.mnist
    (x_train, y_train), (x_test, y_test) = mnist.load_data()
    x_train, x_test = x_train / 255.0, x_test / 255.0
    #func()
    model = tf.keras.models.Sequential(
        [
            tf.keras.layers.Flatten(input_shape=(28, 28)),
            tf.keras.layers.Dense(128, activation="relu"),
            tf.keras.layers.Dropout(0.2),
            tf.keras.layers.Dense(10),
        ]
    )
    #func()
    loss_fn = tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True)
    model.compile(optimizer="adam", loss=loss_fn, metrics=["accuracy"])

    model.fit(x_train, y_train, epochs=20)

    return model


def main():
    model = train_model()

if __name__ == "__main__":
    main()
