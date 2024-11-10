# Parrot Minidrone Navigator

This repository contains an implementation of an autonomous navigation system for a Parrot Minidrone, making use of a Convolutional Neural Network to classify the camera feed in real time. The CNN once trained and integrated within a Simulink model, provides the drone with navigation instructions based on visual feedback, allowing it to traverse an arena track.

## Project Overview

The objective of this project is to train a CNN that enables a Parrot Minidrone to autonomously navigate a track. The CNN thus trained has one purpose, to classify images from the drone's camera, helping the drone decide when to move forward, turn, or adjust its orientation. The classifications from the CNN guide the drone’s movement by informing a Stateflow chart, which adjusts the drone's speed and direction accordingly.

## Approach

### 1. Dataset Creation and Preprocessing

To ensure effective navigation, the CNN was trained on images that the drone's camera would encounter along the track, with the following constraints:

- **Orientation-Dependent Labels**: The training dataset includes images that align with the direction of the track and those that require the drone to rotate about the z-axis. This helps the drone in handling junctions and orientations that it could initially be in.
- **Constraints on Dataset Size**: By restricting the dataset to images relevant to the navigation task, the dataset was reduced to 9,700 images.
- **Image Generation and Processing**: 
  - Images were generated using **GIMP** for simulation purposes, with [SlyPredator](https://github.com/SlyPredator) handling 80% of the dataset creation.
  - Images were preprocessed by cropping from `120x160` to `100x100` pixels, then resizing to `50x50` pixels to increase efficiency.
  - Images were converted to grayscale with pixel values ranging from 0 to 255.

### 2. CNN Architecture

The CNN includes:

- **Convolutional Layers**: Two convolutional layers to extract spatial features from the image input.
- **Pooling Layers**: Two max-pooling layers to downsample feature maps.
- **Fully Connected Layers**: Two fully connected layers to refine feature representation before classification.
- **Softmax Layer**: A softmax layer at the top for classification into navigation labels.

With this structure, the CNN contains **52,832 parameters**.

### 3. Real-Time Image Classification and Integration with Simulink

- **Image Processing Compatibility Issue**: During integration, it was discovered that Simulink processes camera images as binary maps (values 0 and 1) post the grayscale conversion. This was incompatible with the CNN trained on grayscale images with values ranging from 0 to 255. This misalignment caused classification errors, which were resolved by aligning the Simulink output with the CNN's expected input format.

### 4. Refining Navigation Labels

Initially, the CNN’s output distribution was set to 8 labels. However, after extensive testing, it was determined that 3 labels were redundant for optimized navigation. The CNN model was retrained with the 5 essential labels to improve performance, resulting in more efficient navigation:

## Technical Summary

- **Architecture**: Custom CNN with 2 convolutional layers, 2 max-pooling layers, and 2 fully connected layers, outputting to a softmax classifier.
- **Input Processing**: Grayscale images resized to `50x50` pixels.
- **Training Dataset**: 9,700 images with constraints for task-specific relevance.
- **Labeling**: Five classification labels guiding the Stateflow control logic.
- **Integration with Simulink**: The model outputs classifications to a Stateflow chart, which adjusts drone speed and direction in real-time.

## Challenges and Solutions

1. **Image Value Mismatch**: The CNN was trained on grayscale values (0-255), but Simulink provided binary outputs (0 or 1). Solution: Align the Simulink image processing pipeline to match the CNN’s input requirements.
2. **Redundant Labels**: Initial testing with 8 labels resulted in unnecessary complexity. Solution: After refining the behavior model, the CNN was reconfigured to classify into only 5 relevant labels, improving navigation stability.
3. **Simulation Physics**: The physics involved could only be incorporated for by the use of a camera that could capture high resolution images. The issue with having a low resolution camera meant that the difference in 1 degree offset and 0.5 would have a mismatch in the output classification label, thereby rendering the entire model useless.

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/R2D2-08/MiniDroneCNN.git
   cd MiniDroneCNN
