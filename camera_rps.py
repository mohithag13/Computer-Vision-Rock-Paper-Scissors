import random
from datetime import datetime
import cv2
from keras.models import load_model
import numpy as np


duration = 3 # count down to start game
model = load_model('keras_model.h5') # loading the trained model
cap = cv2.VideoCapture(0+cv2.CAP_DSHOW) # turns on camera
data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)
user_wins = 0
computer_wins = 0

while True: 
    ret, frame = cap.read()
    start_time = datetime.now()
    diff = (datetime.now() - start_time).seconds # converting into seconds
    while( diff <= duration ):
        ret, frame = cap.read()
        cv2.putText(frame, str(diff), (70,70), cv2.FONT_HERSHEY_SIMPLEX , 1, (255, 0, 0), 2, cv2.LINE_AA) #adding text timer
        cv2.imshow('frame', frame)
        diff = (datetime.now() - start_time).seconds
        if cv2.waitKey(10) & 0xFF == ord('q'):
           break
    resized_frame = cv2.resize(frame, (224, 224), interpolation = cv2.INTER_AREA)
    image_np = np.array(resized_frame)
    normalized_image = (image_np.astype(np.float32) / 127.0) - 1 # Normalize the image
    data[0] = normalized_image
    prediction = model.predict(data) # predict the class
    
    # Prediction using camera
    def get_prediction():
        if prediction[0][0] > 0.5:
            return 'rock'
        elif prediction[0][1] > 0.5:
            return 'paper'
        elif prediction[0][2] > 0.5:
            return 'scissors'
        else:
            print('Nothing')

    # Computer choice    
    def get_computer_choice():
        possible_choices = ['rock', 'paper', 'scissors']
        computer_option  = random.choice(possible_choices)
        return computer_option
    
    # Determining the winner based on choice
    def get_winner(user_choice, computer_choice):
        if user_choice == computer_choice:
            print(f"Both players chose {user_choice}. It is tie!")
        elif user_choice == 'rock':
            if computer_choice == 'scissors':
                print("Rock smashes scissors!")
                return 'user'
            else:
                print("Paper covers rock!")
                return 'computer'
        elif user_choice == 'paper':
            if computer_choice == 'rock':
                print("Paper covers rock!")
                return 'user'
            else:
                print("Scissors cuts paper!")
                return 'computer'
        elif user_choice == 'scissors':
            if computer_choice == 'paper':
                print("Scissors cuts paper!")
                return 'user'
            else:
                print("Rock smashes scissors!")
                return 'computer'
        
    # game play
    def play():
        user_action = get_prediction()
        computer_action = get_computer_choice()
        print(f"User choice is: {user_action}")
        print(f"Computer choice is: {computer_action}")
        winner = get_winner(user_choice=user_action, computer_choice=computer_action)
        print(f"The winner is:{winner}")
        return winner
            
    s = play()  
    if s == 'user':
        user_wins += 1
    elif s == 'computer':
        computer_wins += 1
    else:
        print('play again')
    print(f'User:{user_wins}')
    print(f'Computer:{computer_wins}')
    if user_wins == 3:  # If user or computer wins 3 games, game ends
        print('You Win') 
        break
    elif computer_wins == 3:
        print('You Lose')
        break
    # Press s to close the window
    if cv2.waitKey(1) & 0xFF == ord('s'):
        break
     

# After the loop release the cap object
cap.release()

# Destroy all the windows
cv2.destroyAllWindows()

