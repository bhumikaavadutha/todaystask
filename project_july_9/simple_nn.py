
import os
import numpy as np
import pandas as pd
import tensorflow as tf
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Flatten, Dropout

# Define constants
train_directory = '/home/bhumika-avadutha/Desktop/train'
valid_directory = '/home/bhumika-avadutha/Desktop/valid'
test_directory = '/home/bhumika-avadutha/Desktop/test'
image_width, image_height = 28, 28  # Image dimensions
batch_size = 32
epochs = 2

# Check if directories exist
if not os.path.exists(train_directory):
    raise FileNotFoundError(f"Training directory '{train_directory}' not found.")
if not os.path.exists(valid_directory):
    raise FileNotFoundError(f"Validation directory '{valid_directory}' not found.")
if not os.path.exists(test_directory):
    raise FileNotFoundError(f"Testing directory '{test_directory}' not found.")

# Load filenames and labels from directory
train_filenames = []
train_labels = []
for filename in os.listdir(train_directory):
    if filename.endswith('.jpg') or filename.endswith('.png'):
        train_filenames.append(os.path.join(train_directory, filename))
        train_labels.append(1)  # Assuming all are of the same class

valid_filenames = []
valid_labels = []
for filename in os.listdir(valid_directory):
    if filename.endswith('.jpg') or filename.endswith('.png'):
        valid_filenames.append(os.path.join(valid_directory, filename))
        valid_labels.append(1)  # Assuming all are of the same class

test_filenames = []
test_labels = []
for filename in os.listdir(test_directory):
    if filename.endswith('.jpg') or filename.endswith('.png'):
        test_filenames.append(os.path.join(test_directory, filename))
        test_labels.append(1)  # Assuming all are of the same class

# Convert lists to numpy arrays
train_filenames = np.array(train_filenames)
train_labels = np.array(train_labels)
valid_filenames = np.array(valid_filenames)
valid_labels = np.array(valid_labels)
test_filenames = np.array(test_filenames)
test_labels = np.array(test_labels)

# Print number of images found
print(f"Found {len(train_filenames)} images for training.")
print(f"Found {len(valid_filenames)} images for validation.")
print(f"Found {len(test_filenames)} images for testing.")

# Set up data generators
train_datagen = ImageDataGenerator(
    rescale=1./255,
    shear_range=0.2,
    zoom_range=0.2,
    horizontal_flip=True
)

valid_datagen = ImageDataGenerator(rescale=1./255)
test_datagen = ImageDataGenerator(rescale=1./255)

# Flow data from arrays
train_generator = train_datagen.flow_from_dataframe(
    dataframe=pd.DataFrame({'filename': train_filenames, 'label': train_labels}),
    x_col='filename',
    y_col='label',
    target_size=(image_width, image_height),
    batch_size=batch_size,
    class_mode='binary' 
)

valid_generator = valid_datagen.flow_from_dataframe(
    dataframe=pd.DataFrame({'filename': valid_filenames, 'label': valid_labels}),
    x_col='filename',
    y_col='label',
    target_size=(image_width, image_height),
    batch_size=batch_size,
    class_mode='binary'  
)

test_generator = test_datagen.flow_from_dataframe(
    dataframe=pd.DataFrame({'filename': test_filenames, 'label': test_labels}),
    x_col='filename',
    y_col='label',
    target_size=(image_width, image_height),
    batch_size=batch_size,
    class_mode='binary'  

# Build the model
model = Sequential([
    Flatten(input_shape=(image_width, image_height, 3)),  # input layer
    Dense(128, activation='relu'),  
    Dropout(0.5),  # dropout layer for regularization
    Dense(1, activation='sigmoid')  # output layer, sigmoid for binary classification
])

# Compile the model
model.compile(optimizer='adam',
              loss='binary_crossentropy',
              metrics=['accuracy'])

# Print model summary
model.summary()

# Train the model
history = model.fit(
    train_generator,
    steps_per_epoch=len(train_generator),
    epochs=epochs,
    validation_data=valid_generator,
    validation_steps=len(valid_generator)
)

# Evaluate the model on training data
train_loss, train_accuracy = model.evaluate(train_generator, steps=len(train_generator))
print(f'Training accuracy: {train_accuracy}')

# Evaluate the model on validation data
valid_loss, valid_accuracy = model.evaluate(valid_generator, steps=len(valid_generator))
print(f'Validation accuracy: {valid_accuracy}')

# Evaluate the model on test data
test_loss, test_accuracy = model.evaluate(test_generator, steps=len(test_generator))
print(f'Test accuracy: {test_accuracy}')
