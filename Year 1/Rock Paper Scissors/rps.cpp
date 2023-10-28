/*
MODULE: SECURE CODING
MODULE CODE: CSEC 1003
DATE SET: 23rd March 2023 - Week 25
DUE DATE: 28th April 2023 - Week 25

This rock paper scissors game asks the user to authenticate through a password
before allowing them to play.
The computer picks a random number between 1 to 3 and depending on the number the computer will either pick rock/paper/scissors. 
depending on what the user picks and the computer picks, there are three outcomes for both the computer and user: draw/win/lose.
*/

#include <iostream>
using namespace std;
#include <string.h>
#define line_seperator "= = = = = = = = = = = = = = = =" // seperates line / neatens it.
        /* Scores */
        int gWins; // global variable wins
        int gLosses; // global variable losses
        int gDraws; // global variable draws
        
/* AUTHENTICATION BEGINS */
class User_Authentication {
    private:
        const char user_password[10] = "Encrypted"; // HERE IS THE PASSWORD TO BEGIN THE GAME!!!
        int time_out = 0;
        bool authenticated = false;

    public:
        void authentication_Process(){
        while (time_out < 3 && !authenticated){ // checks if time_out is less than 3 and if the user is not authenticated
            string input_password;
            cout << "please enter your password\n";
            cout << "> ";
            getline(cin, input_password); // Grabs users input

            /* PASS WORD CHECK BEGINS HERE*/
            if (input_password != user_password){ // Checks users input against stored password
                cout << "\nincorrect password.\n";
                cout << "AMOUNT OF ATTEMPTS LEFT: " << 2 - time_out  << " / 3"<< endl; // Shows users how many attempts left they have before program stops.
                time_out++;
                }

            else{
                cout << "correct password.\n"; // if password matches, program returns TRUE and runs.
                authenticated = true; // sets authenticated to TRUE.
                }  
        }
        if(!authenticated){
            cout << "= = = = too many failed attempts.. aborting = = = =";
            exit(1); //  Exits the program if user failed to authorize.
        }
    }   
};
/* AUTHENTICATION STOPS */


class Rock_Paper_Scissors {
    private:
    // Array of possabilitys, third index is who wins/losses/draws
    string rps[9][3] = {
        {"rock",    "rock",     "It's a draw!"}, 
        {"rock",    "paper",    "You lost!"}, 
        {"rock",    "scissors", "You win!"}, 

        {"paper",   "rock",     "You win!"}, 
        {"paper",   "paper",    "It's a draw!"}, 
        {"paper",   "scissors", "You lost!"}, 

        {"scissors", "rock",     "You lost!"}, 
        {"scissors", "paper",    "You win!"}, 
        {"scissors", "scissors", "It's a draw!"} 
        };  

    public:
        void Start_Game(){ // Class game loop begins here

        bool game_loop = true; // If true; game will continue to loop until it returns false.
        while (game_loop == true){ // game loop begins

            string users_input; //stores users input here
            cout << "Enter 'rock', 'paper', 'scissors' or 'quit'" << endl;
            cout << "> ";
            cin >> users_input; // asks user for input.

            for (int i=0; i < users_input.length(); i++){  
                    users_input[i]=tolower(users_input[i]); // checks each individual character and forces to lower case to prevent logical error.
                }

            while (users_input != "rock" && users_input != "paper" && users_input != "scissors" && users_input != "quit"){ // Checks users input to see if they entered the correct option.
                cout << "Please enter 'rock' 'paper' 'scissors' or 'quit" << endl;
                cout << "> ";
                cin >> users_input;
            }

             // generates a random number
                int computers_number = rand() % 3 + 1; // generates random number between 1 and 3
                string computers_pick; // holds computers pick

            if (computers_number  == 1){
                computers_pick = "rock"; // Computers pick is rock
            }

            else if (computers_number  == 2){
                computers_pick = "paper"; // Computers pick is paper
            }

            else if (computers_number == 3){
                computers_pick = "scissors"; // Computers pick is scissors
            }
    
    
            string result; // holds game results here
            for (int i = 0; i < 9; i++){ // loops over rps Array
                if (users_input == rps[i][0] && computers_pick == rps[i][1]){ // checks users & computers for a matching result
                    result = rps[i][2]; // checks 3rd index for winner/loser/draw  
                }   
            }


            if (result == "It's a draw!"){
                gDraws++; // increases draws score by 1.
                    }
            else if (result == "You win!"){
                gWins++; // increases win score by 1.
                    }
            else if (result== "You lost!"){
                gLosses++; // increases losses score by 1.
                }
    
            if (users_input == "quit"){ // quits the game 
                    std::cout << "- - - - - -SCORE - - - - - -" << endl;
                    std::cout << "WINS: " << gWins << endl << "LOSSES: " << gLosses << endl << "DRAWS: "<< gDraws << endl; // displays score at end of game
                    std::cout << "= = = = = = = = Thank you for playing! = = = = = = = = ";
                    game_loop = false; // returns false which stops the game from looping.
                }
                
            if (!(users_input == "quit")){ // prevents this code from being printed out if user choices to quit.
                cout << result;
                cout << endl << endl;
                cout << line_seperator << endl;
                cout << "USER \t  CHOSE: \t" << "["<< users_input << "]" << endl; // pastes users input
                cout << "COMPUTER CHOSE: \t" << "["<< computers_pick << "]"<< endl; // pastes computers input
                cout << line_seperator << endl;
                cout << endl  << "\t" << result << endl << endl;
            }
        }
    }
};



int main(){
    User_Authentication authentication; // creates object using User_Authentication class
    authentication.authentication_Process();

    Rock_Paper_Scissors start_Game; // creates new object called start_game
    cout << endl;
    cout << "= = = = Welcome to the ROCK PAPER SCISSORS GAME! = = = =" << endl;
    cout << "Pick from the following options: \n'rock' 'paper', 'scissors' or 'quit' to exit the game." << endl;
    cout << "Good luck!";
    cout << endl << endl;
    start_Game.Start_Game(); // starts the game    
}

/*
Bibliography:
    https://www.digitalocean.com/community/tutorials/two-dimensional-array-in-c-plus-plus
    https://isaaccomputerscience.org/concepts/dsa_datastruct_two_dimensional_arrays
    https://users.ece.cmu.edu/~eno/coding/CppCodingStandard.html - mostly for nameing variables/classes/methods
*/
