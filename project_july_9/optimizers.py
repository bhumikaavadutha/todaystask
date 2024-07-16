
import os
import numpy as np
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Flatten, Dropout, BatchNormalization
from tensorflow.keras.optimizers import SGD, RMSprop
from tensorflow.keras.callbacks import EarlyStopping
from tensorflow.keras.preprocessing.image import load_img, img_to_array
from sklearn.model_selection import train_test_split


image_width = 150
image_height = 150
epochs = 10 
# Define optimizers to compare
optimizers = {
    'adam': 'adam',
    'sgd': SGD(),
    'sgd_momentum': SGD(momentum=0.9),
    'rmsprop': RMSprop(learning_rate=0.001)  
}

# Initialize lists to hold accuracies for each optimizer
train_accuracies_opt = {opt_name: [] for opt_name in optimizers}
valid_accuracies_opt = {opt_name: [] for opt_name in optimizers}
test_accuracies_opt = {opt_name: [] for opt_name in optimizers}


train_dir = '/home/bhumika-avadutha/Desktop/train'
valid_dir = '/home/bhumika-avadutha/Desktop/valid'
test_dir = '/home/bhumika-avadutha/Desktop/test'

# Load and preprocess data for each dataset
for opt_name, optimizer in optimizers.items():
    print(f"\nTraining model with optimizer: {opt_name}")
    
    # Load training data
    train_images = []
    train_labels = []
    train_files = [os.path.join(train_dir, file) for file in os.listdir(train_dir)]
    for file in train_files:
        img = load_img(file, target_size=(image_width, image_height))
        img_array = img_to_array(img) / 255.0
        train_images.append(img_array)
        train_labels.append(1 if 'positive' in file else 0)  # Adjust label based on naming convention
    train_images = np.array(train_images)
    train_labels = np.array(train_labels)

    # Load validation data
    valid_images = []
    valid_labels = []
    valid_files = [os.path.join(valid_dir, file) for file in os.listdir(valid_dir)]
    for file in valid_files:
        img = load_img(file, target_size=(image_width, image_height))
        img_array = img_to_array(img) / 255.0
        valid_images.append(img_array)
        valid_labels.append(1 if 'positive' in file else 0)  # Adjust label based on naming convention
    valid_images = np.array(valid_images)
    valid_labels = np.array(valid_labels)

    # Load testing data
    test_images = []
    test_labels = []
    test_files = [os.path.join(test_dir, file) for file in os.listdir(test_dir)]
    for file in test_files:
        img = load_img(file, target_size=(image_width, image_height))
        img_array = img_to_array(img) / 255.0
        test_images.append(img_array)
        test_labels.append(1 if 'positive' in file else 0)  # Adjust label based on naming convention
    test_images = np.array(test_images)
    test_labels = np.array(test_labels)

    # Early stopping callback
    early_stopping = EarlyStopping(monitor='val_loss', patience=3)

    # Model definition
    model = Sequential([
        Flatten(input_shape=(image_width, image_height, 3)),
        Dense(128, activation='relu'),
        BatchNormalization(),
        Dropout(0.5),
        Dense(64, activation='relu'),
        BatchNormalization(),
        Dropout(0.3),
        Dense(1, activation='sigmoid')
    ])
    
    model.compile(optimizer=optimizer,
                  loss='binary_crossentropy',
                  metrics=['accuracy'])

    # Train the model
    history = model.fit(
        train_images, train_labels,
        epochs=epochs,
        batch_size=20,  # Mini-batch size
        validation_data=(valid_images, valid_labels),
        callbacks=[early_stopping]
    )

    # Evaluate the model on training data
    train_loss, train_accuracy = model.evaluate(train_images, train_labels)
    train_accuracies_opt[opt_name].append(train_accuracy)

    # Evaluate the model on validation data
    valid_loss, valid_accuracy = model.evaluate(valid_images, valid_labels)
    valid_accuracies_opt[opt_name].append(valid_accuracy)

    # Evaluate the model on testing data
    test_loss, test_accuracy = model.evaluate(test_images, test_labels)
    test_accuracies_opt[opt_name].append(test_accuracy)

    # Print accuracies
    print(f'Training accuracy: {train_accuracy}')
    print(f'Validation accuracy: {valid_accuracy}')
    print(f'Testing accuracy: {test_accuracy}')

# Print final results
for opt_name in optimizers:
    print(f"\nOptimizer: {opt_name}")
    print(f"Training accuracy: {train_accuracies_opt[opt_name]}")
    print(f"Validation accuracy: {valid_accuracies_opt[opt_name]}")
    print(f"Testing accuracy: {test_accuracies_opt[opt_name]}")
