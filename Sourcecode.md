# Computer Vision - Rock-Paper-Scissors Project Guideline
1. You've probably played rock, paper, scissors before. Perhaps you've used it to decide who pays for dinner or who gets first pick of a team's players. If you're not familiar, rock paper scissors is a two- or more-player hand game. Participants say "rock, paper, scissors," then make their hands into the shapes of a rock (a fist), a piece of paper (a palm), or a pair of scissors(two fingers extended) at the same time. 
The rules are simple:
- Rock smashes scissors.
- Paper covers rock.
- Scissors cut paper.
2. Technologies and Tools used are Teachable Machine, Python.
## Milestone 1: Create Model
- Create an image project model with four different classes: Rock, Paper, Scissors, Nothing.
  - Use Teachable Machine(Train a computer to recognize your own images, sounds, & poses), generated the model. Each class is trained with photos that show the camera each option. The 'Nothing' class reflects the absence of a choice. 
  - Download the model from Teachable-Machine's "Tensorflow" tab. The model's filename is keras model.h5, and the text file containing the labels is labels.txt. The downloaded file [converted_keras.zip](converted_keras.zip) contain the structure and parameters of a deep learning model.
## Milestone 2: Install the dependencies
- Create the conda virtual environment and install the necessary packages to work on the model such as opencv-python, tensorflow, and ipykernel.
- Run the model [rps_template.py](rps_template.py) and get familiar with model
## Milestone 3: Create Rock-Paper-Scissors game
- The code must select an option at random (rock, paper, or scissors) and then prompt the user for input. To play the game without the camera, use the [manual rps.py](manual rps.py) file.
- The random module can be used to pick a random option between rock, paper, and scissors and create the input function to get the user's choice.
- Create seperate functions to store the user's choice, computer's choice and get winner.
- Using if-elif-else statements, the script selects a winner based on the classic Rock-Paper-Scissors rules.
- Create a new function called play. Inside the function call all the other three functions you've created.
