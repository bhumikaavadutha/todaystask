
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Flatten, Dense
from tensorflow.keras.optimizers import Adam
from tensorflow.keras.losses import SparseCategoricalCrossentropy
from tensorflow.keras.callbacks import EarlyStopping
from sklearn.model_selection import train_test_split
import numpy as np

# Load MNIST data
mnist = tf.keras.datasets.mnist
(train_images, train_labels), (test_images, test_labels) = mnist.load_data()

# Preprocess data
train_images = train_images / 255.0
test_images = test_images / 255.0

# Define input shape and number of classes
input_shape = train_images[0].shape
num_classes = 10  # Since MNIST has 10 classes (digits 0-9)

# Build the model without dropout
model = Sequential([
    Flatten(input_shape=input_shape),           # Flatten input to 1D
    Dense(512, activation='relu'),              # Hidden layer with 512 neurons, ReLU activation
    Dense(256, activation='relu'),              
    Dense(128, activation='relu'),              
    Dense(num_classes, activation='softmax')    # Output layer with softmax activation for classification
])

# Compile the model
model.compile(optimizer=Adam(learning_rate=0.0001),   # Optimizer with lower learning rate
              loss=SparseCategoricalCrossentropy(),  # Loss function for multi-class classification
              metrics=['accuracy'])                 # Metrics to monitor during training

# Early stopping callback
early_stopping = EarlyStopping(monitor='val_accuracy', patience=5, restore_best_weights=True)

# Training
history = model.fit(train_images, train_labels,
                    epochs=50,
                    batch_size=128,
                    validation_split=0.2,
                    callbacks=[early_stopping],
                    verbose=1)

# Evaluate on test data
test_loss, test_acc = model.evaluate(test_images, test_labels, verbose=0)
print(f'Test accuracy: {test_acc:.4f}')