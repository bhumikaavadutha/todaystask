import numpy as np
import os 
import tensorflow as tf
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Flatten, Dropout, BatchNormalization
from tensorflow.keras.regularizers import l2
from tensorflow.keras.callbacks import EarlyStopping


train_directory = "/home/bhumika-avadutha/Desktop/train"
valid_directory = "/home/bhumika-avadutha/Desktop/valid"
test_directory = "/home/bhumika-avadutha/Desktop/test"
image_width, image_height = 28, 28  # Image dimensions
batch_size = 32
epochs = 10

# Initialize lists to hold data and labels
train_data, train_labels = [], []
valid_data, valid_labels = [], []
test_data, test_labels = [], []

# Load and preprocess images for training
directory = train_directory
for filename in os.listdir(directory):
    if filename.endswith('.jpg') or filename.endswith('.png'):
        img_path = os.path.join(directory, filename)
        img = tf.keras.preprocessing.image.load_img(img_path, target_size=(image_width, image_height))
        img_array = tf.keras.preprocessing.image.img_to_array(img)
        train_data.append(img_array)
        train_labels.append(0)  # Assuming all images are of the same class (e.g., class 0)

# Load and preprocess images for validation
directory = valid_directory
for filename in os.listdir(directory):
    if filename.endswith('.jpg') or filename.endswith('.png'):
        img_path = os.path.join(directory, filename)
        img = tf.keras.preprocessing.image.load_img(img_path, target_size=(image_width, image_height))
        img_array = tf.keras.preprocessing.image.img_to_array(img)
        valid_data.append(img_array)
        valid_labels.append(0)  # Assuming all images are of the same class (e.g., class 0)

# Load and preprocess images for testing
directory = test_directory
for filename in os.listdir(directory):
    if filename.endswith('.jpg') or filename.endswith('.png'):
        img_path = os.path.join(directory, filename)
        img = tf.keras.preprocessing.image.load_img(img_path, target_size=(image_width, image_height))
        img_array = tf.keras.preprocessing.image.img_to_array(img)
        test_data.append(img_array)
        test_labels.append(0)  # Assuming all images are of the same class (e.g., class 0)

# Convert lists to numpy arrays
train_data = np.array(train_data)
train_labels = np.array(train_labels)
valid_data = np.array(valid_data)
valid_labels = np.array(valid_labels)
test_data = np.array(test_data)
test_labels = np.array(test_labels)

# Print number of images found
print(f"Found {len(train_data)} images for training.")
print(f"Found {len(valid_data)} images for validation.")
print(f"Found {len(test_data)} images for testing.")

# Set up data generators
train_datagen = ImageDataGenerator(
    rescale=1./255,
    shear_range=0.2,
    zoom_range=0.2,
    horizontal_flip=True
)

valid_datagen = ImageDataGenerator(rescale=1./255)

# Set up data generator for training
train_generator = train_datagen.flow(
    x=train_data,
    y=train_labels,
    batch_size=batch_size,
    shuffle=True
)

valid_generator = valid_datagen.flow(
    x=valid_data,
    y=valid_labels,
    batch_size=batch_size,
    shuffle=False  # No need to shuffle validation data
)

train_accuracies = []
valid_accuracies = []
test_accuracies = []

# Model building and training with L2 regularization
print("Model with L2 regularization:")
model_l2 = Sequential([
    Flatten(input_shape=(image_width, image_height, 3)),  # input layer
    Dense(128, activation='relu', kernel_regularizer=l2(0.001)),  # hidden layer with L2 regularization
    BatchNormalization(),  # batch normalization layer
    Dropout(0.5),  # dropout layer for regularization
    Dense(64, activation='relu', kernel_regularizer=l2(0.001)),  # additional hidden layer with L2 regularization
    BatchNormalization(),  # batch normalization layer
    Dropout(0.3),  # dropout layer for regularization
    Dense(1, activation='sigmoid')  # output layer, sigmoid for binary classification
])

model_l2.compile(optimizer='adam',
              loss='binary_crossentropy',
              metrics=['accuracy'])

# Early stopping callback
early_stopping = EarlyStopping(
    monitor='val_loss',
    patience=3,
    restore_best_weights=True
)

# Train the model with L2 regularization
history_l2 = model_l2.fit(
    train_generator,
    steps_per_epoch=len(train_generator),
    epochs=epochs,
    validation_data=valid_generator,
    validation_steps=len(valid_generator),
    callbacks=[early_stopping]
)

# Evaluate the model with L2 regularization on training data
train_loss_l2, train_accuracy_l2 = model_l2.evaluate(train_generator, steps=len(train_generator))

# Evaluate the model with L2 regularization on validation data
valid_loss_l2, valid_accuracy_l2 = model_l2.evaluate(valid_generator, steps=len(valid_generator))

# Evaluate the model with L2 regularization on testing data
test_loss_l2, test_accuracy_l2 = model_l2.evaluate(test_data, test_labels)

print(f'Training accuracy: {train_accuracy_l2}')
print(f'Validation accuracy: {valid_accuracy_l2}')
print(f'Testing accuracy with L2 regularization: {test_accuracy_l2}')

# Store accuracies
train_accuracies.append(train_accuracy_l2)
valid_accuracies.append(valid_accuracy_l2)
test_accuracies.append(test_accuracy_l2)

# Model building and training with Dropout
print("\nModel with Dropout:")
model_dropout = Sequential([
    Flatten(input_shape=(image_width, image_height, 3)),  # input layer
    Dense(128, activation='relu'),  # hidden layer
    BatchNormalization(),  # batch normalization layer
    Dropout(0.5),  # dropout layer
    Dense(64, activation='relu'),  # additional hidden layer
    BatchNormalization(),  # batch normalization layer
    Dropout(0.3),  
    Dense(1, activation='sigmoid')  # output layer, sigmoid for binary classification
])

model_dropout.compile(optimizer='adam',
              loss='binary_crossentropy',
              metrics=['accuracy'])

# Train the model with Dropout
history_dropout = model_dropout.fit(
    train_generator,
    steps_per_epoch=len(train_generator),
    epochs=epochs,
    validation_data=valid_generator,
    validation_steps=len(valid_generator),
    callbacks=[early_stopping]
)

# Evaluate the model with Dropout on training data
train_loss_dropout, train_accuracy_dropout = model_dropout.evaluate(train_generator, steps=len(train_generator))

# Evaluate the model with Dropout on validation data
valid_loss_dropout, valid_accuracy_dropout = model_dropout.evaluate(valid_generator, steps=len(valid_generator))

# Evaluate the model with Dropout on testing data
test_loss_dropout, test_accuracy_dropout = model_dropout.evaluate(test_data, test_labels)


print(f'Training accuracy: {train_accuracy_dropout}')
print(f'Validation accuracy: {valid_accuracy_dropout}')
print(f'Testing accuracy with Dropout: {test_accuracy_dropout}')


# Store accuracies
train_accuracies.append(train_accuracy_dropout)
valid_accuracies.append(valid_accuracy_dropout)
test_accuracies.append(test_accuracy_dropout)

# Model building and training with Batch Normalization
print("\nModel with Batch Normalization:")
model_batchnorm = Sequential([
    Flatten(input_shape=(image_width, image_height, 3)),  
    Dense(128, activation='relu'),  # hidden layer
    BatchNormalization(),  # batch normalization layer
    Dropout(0.5),  # dropout layer
    Dense(64, activation='relu'), 
    BatchNormalization(), 
    Dropout(0.3),  
    Dense(1, activation='sigmoid')  # output layer, sigmoid for binary classification
])

model_batchnorm.compile(optimizer='adam',
              loss='binary_crossentropy',
              metrics=['accuracy'])

# Train the model with Batch Normalization
history_batchnorm = model_batchnorm.fit(
    train_generator,
    steps_per_epoch=len(train_generator),
    epochs=epochs,
    validation_data=valid_generator,
    validation_steps=len(valid_generator),
    callbacks=[early_stopping]
)

# Evaluate the model with Batch Normalization on training data
train_loss_batchnorm, train_accuracy_batchnorm = model_batchnorm.evaluate(train_generator, steps=len(train_generator))

# Evaluate the model with Batch Normalization on validation data
valid_loss_batchnorm, valid_accuracy_batchnorm = model_batchnorm.evaluate(valid_generator, steps=len(valid_generator))

# Evaluate the model with Batch Normalization on testing data
test_loss_batchnorm, test_accuracy_batchnorm = model_batchnorm.evaluate(test_data, test_labels)
print(f'Training accuracy: {train_accuracy_batchnorm}')
print(f'Validation accuracy: {valid_accuracy_batchnorm}')
print(f'Testing accuracy with Batch Normalization: {test_accuracy_batchnorm}')

# Store accuracies
train_accuracies.append(train_accuracy_batchnorm)
valid_accuracies.append(valid_accuracy_batchnorm)
test_accuracies.append(test_accuracy_batchnorm)

# Model building and training with Early Stopping

print("\nModel with Early Stopping:")
model_earlystop = Sequential([
    Flatten(input_shape=(image_width, image_height, 3)),  # input layer
    Dense(128, activation='relu'),  # hidden layer
    BatchNormalization(),  # batch normalization layer
    Dropout(0.5),  # dropout layer
    Dense(64, activation='relu'),  # additional hidden layer
    BatchNormalization(),  # batch normalization layer
    Dropout(0.3),  # dropout layer
    Dense(1, activation='sigmoid')  # output layer, sigmoid for binary classification
])

model_earlystop.compile(optimizer='adam',
              loss='binary_crossentropy',
              metrics=['accuracy'])

# Train the model with Early Stopping
history_earlystop = model_earlystop.fit(
    train_generator,
    steps_per_epoch=len(train_generator),
    epochs=epochs,
    validation_data=valid_generator,
    validation_steps=len(valid_generator),
    callbacks=[early_stopping]
)

# Evaluate the model with Early Stopping on training data
train_loss_earlystop, train_accuracy_earlystop = model_earlystop.evaluate(train_generator, steps=len(train_generator))

# Evaluate the model with Early Stopping on validation data
valid_loss_earlystop, valid_accuracy_earlystop = model_earlystop.evaluate(valid_generator, steps=len(valid_generator))

# Evaluate the model with Early Stopping on testing data
test_loss_earlystop, test_accuracy_earlystop = model_earlystop.evaluate(test_data, test_labels)

print(f'Training accuracy: {train_accuracy_earlystop}')
print(f'Validation accuracy: {valid_accuracy_earlystop}')
print(f'Testing accuracy with Early Stopping: {test_accuracy_earlystop}')

# Store accuracies
train_accuracies.append(train_accuracy_batchnorm)
valid_accuracies.append(valid_accuracy_batchnorm)
test_accuracies.append(test_accuracy_batchnorm)

# Print final accuracies
print("\nFinal accuracies:")
print(f'L2 Regularization - Training: {train_accuracies[0]}, Validation: {valid_accuracies[0]}, Testing: {test_accuracies[0]}')
print(f'Dropout - Training: {train_accuracies[1]}, Validation: {valid_accuracies[1]}, Testing: {test_accuracies[1]}')
print(f'Batch Normalization - Training: {train_accuracies[2]}, Validation: {valid_accuracies[2]}, Testing: {test_accuracies[2]}')
print(f'Early Stopping - Training: {train_accuracies[3]}, Validation: {valid_accuracies[3]}, Testing: {test_accuracies[3]}')
