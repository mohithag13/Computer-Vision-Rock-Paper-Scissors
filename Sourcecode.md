# Computer Vision - Rock-Paper-Scissors Project Guideline
1. You've probably played rock, paper, scissors before.  
The rules are simple:
- Rock smashes scissors.
- Paper covers rock.
- Scissors cut paper.
2. Technologies and Tools used are Teachable Machine, Python.
## Milestone 1: Create Model
- Create an image project model with four different classes: Rock, Paper, Scissors, Nothing.
  - Use Teachable Machine(Train a computer to recognize your own images, sounds, & poses), generated the model. Each class is trained with photos that show the camera each option. The 'Nothing' class reflects the absence of a choice. 
  - Download the model from Teachable-Machine's "Tensorflow" tab. The model's filename is keras model.h5, and the text file containing the labels is labels.txt. The downloaded file [converted_keras.zip](converted_keras.zip) contain the structure and parameters of a deep learning model.
## Milestone 2: Prerequisites
- Create the conda virtual environment and install the necessary packages to work on the model such as opencv-python, tensorflow, and ipykernel.
- Run the model [rps_template.py](rps_template.py) and get familiar with model
## Milestone 3: Manual Rock-Paper-Scissors game
- To play the game without the camera, use the [manual_rps.py](manual_rps.py) file.
- The random module can be used to pick a random option between rock, paper, and scissors and create the input function to get the user's choice.
- Create seperate functions to store the user's choice, computer's choice and get winner.
- Using if-elif-else statements, the script selects a winner based on the classic Rock-Paper-Scissors rules.
- Create a new function and call all the other three functions you've created.
## Milestone 4: Camera Rock-Paper-Scissors game
- Get user input from Camera instead of providing manual input.
- Keep a running countdown before starting the game.
- When either the user or the computer has won three times, the game is over.
- The countdown was displayed on the webcam display using OpenCV libraries.
- To play the game using camera, use the [camera_rps.py](camera_rps.py) file.
## Conclusions:
- Developed a Rock-Paper-Scissors game using a machine learning model and computer vision. 
- Could even make the game more accessible and user-friendly by adding GUI libraries.
