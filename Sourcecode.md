# Computer Vision - Rock-Paper-Scissors Project Guideline
1. You've probably played rock, paper, scissors before. Perhaps you've used it to decide who pays for dinner or who gets first pick of a team's players. If you're not familiar, rock paper scissors is a two- or more-player hand game. Participants say "rock, paper, scissors," then make their hands into the shapes of a rock (a fist), a piece of paper (a palm), or a pair of scissors(two fingers extended) at the same time. 
The rules are simple:
- Rock smashes scissors.
- Paper covers rock.
- Scissors cut paper.
2. Technologies and Tools used are Teachable Machine, Python.
## Milestone 1: Create Model
- Create an image project model with four different classes: Rock, Paper, Scissors, Nothing.
  - Using Teachable Machine, generated the model. Each class is trained with photos that show the camera each option. The 'Nothing' class reflects the absence of a choice. 
  - Download the model from Teachable-Machine's "Tensorflow" tab. The model's filename is keras model.h5, and the text file containing the labels is labels.txt. The downloaded file [converted_keras.zip](converted_keras.zip) contain the structure and parameters of a deep learning model. They are neither executable files, nor do they contain anything readable if you look inside. In the following milestone, you will load them into your Python programme.
