/*
MODULE: SECURE CODING
MODULE CODE: CSEC 1003
DATE SET: 23rd March 2023 - Week 25
DUE DATE: 28th April 2023 - Week 25

This program prompts the user to pick an option via an integer.
depending on the option, prints out the calculated time conversion.
I added remainder for a few of the conversion as I wanteed to show the left over time that was not used in the conversion. 
additionally the output looked cleaner with it.
I did not include it for a few of the checks as the output only needed to be in seconds or hours.
*/

/*
line 55 can be improved, we shoudn't use a break in a method.
and never do a while else. again line 55.
*/

#include <iostream>
#include <ios> // used to get stream size
#include <limits> // used to get numeric limits
using namespace std;

#define Seperator "= = = = = = = = = = = = = = = = = = = = = = = = = = ="

class TimeConversion{
    public:
    /* Objects for conversion*/
    void convertSecondsToHours(); 
    void convertSecondsToMinutes(); 
    void convertMinutesToHours(); 
    void convertHoursToSeconds();
    void convertMinutesToSeconds(); 

};

/* User input validation */
class CheckUserInput{
    public:
    static void CheckIntInput(int& int_value){
        while(true){
            std::cin >> int_value; // gets users input
            if (cin.fail()){ // user fails to enter a integer
            cin.clear(); // clears cin
            cin.ignore(numeric_limits<streamsize>::max(), '\n'); // clears buffer and ignores all characters upto the new line.
            cout << "invalid input. Please only enter an integer value.\n> ";
            
        }
        if (int_value < 0){
            std::cout << "- - - Cannot enter value less than 0, try again. - - -" << endl;
            std::cout << "> ";
        }
        else {
            break; // if user input is valid, breaks from loop. could exit? unsure
            }   
        }
    }
};

void TimeConversion::convertSecondsToHours(){ // option 1
    int seconds,hours, minutes, remainder_in_seconds, remainder_in_minutes;

    cout << "SELECTED: Seconds to hours" << endl;
    cout << "Enter time IN SECONDS\n> ";
    CheckUserInput::CheckIntInput(seconds); // grabs users input in seconds
    cout << endl;

    if (seconds != 0){
        hours = seconds / 3600;
        minutes = seconds / 60;
        remainder_in_seconds = seconds % 60; // finds remainder in seconds
        remainder_in_minutes = minutes % 60; // finds remainder in minutes
        cout << Seperator << endl;
        cout << "\t" << seconds << " seconds to an hour is: " << int(hours) << " hours and " << remainder_in_minutes << " minutes and " << remainder_in_seconds << " seconds" << endl;
        cout << Seperator << endl;
        }

    else{
        cout << "Cannot divide by 0.\n"; // zero division check
        }
};


void TimeConversion::convertSecondsToMinutes(){ // option 2
        int seconds, minutes, remainder_in_seconds;
    
        cout << "SELECTED: Seconds to minutes" << endl;
        cout << "Enter time IN SECONDS\n> ";
        CheckUserInput::CheckIntInput(seconds); // grabs users input in seconds
        cout << endl;

        
        if (seconds != 0){
            minutes = seconds / 60;
            remainder_in_seconds = seconds % 60;
            cout << Seperator << endl;
            cout << "\t" << seconds << " seconds to a minute is: " << int(minutes) << " minutes and " << remainder_in_seconds << " seconds" << endl;
            cout << Seperator << endl;
            }

        else{
            cout << "Cannot divide by 0.";
        }
    
};


void TimeConversion::convertMinutesToHours(){ // option 3
    int minutes,hours,seconds,remainder_in_minutes;

    cout << "SELECTED: Minutes to hours" << endl;
    std::cout << "Enter time IN MINUTES\n> ";
    CheckUserInput::CheckIntInput(minutes); // grabs users input in minutes
    cout << endl;

    if (minutes != 0){
        hours = minutes / 60;
        remainder_in_minutes = minutes % 60; // finds remainder in minutes
        cout << Seperator << endl;
        cout << "\t" << minutes << " minutes to hours is: " << int(hours) << " hours and " << remainder_in_minutes << " minutes" << endl;
        cout << Seperator << endl;
        }

    else{
        cout << "Cannot divide by 0."; // zero division check
        }
};


void TimeConversion::convertHoursToSeconds(){ // option 4
    int hours,seconds;

    cout << "SELECTED: Hours to seconds" << endl;
    std::cout << "Enter time IN HOURS5\n> ";
    CheckUserInput::CheckIntInput(hours); // grabs users input in hours
    cout << endl;

    if (hours != 0){
        seconds = hours * 3600;
        
        cout << Seperator << endl;
        cout << "\t" << hours << " hours to seconds is: " << int(seconds) << " seconds" << endl;
        cout << Seperator << endl;
        }

     else{
        cout << "Cannot divide by 0."; // zero division check
        }       
};

// FIXED: Had an issue where I wasn't converting from minutes to seconds - 19/05/2023
void TimeConversion::convertMinutesToSeconds(){ // option 5
    int minutes,seconds;

    cout << "SELECTED: Minutes to seconds" << endl;
    cout << "Enter time IN MINUTES\n> ";
    CheckUserInput::CheckIntInput(minutes); // grabs users input in minutes
    cout << "\n";

    if (minutes != 0){
        seconds = minutes * 60; // takes seconds and times by amount of minutes by 60.
        cout << Seperator << endl;
        cout << "\t" << " Minutes to seconds: " << int(seconds) << " seconds" << endl;
        cout << Seperator << endl;
        }

    else{
        cout << "Cannot divide by 0." << endl;
    }
};



int main(){
    /* basic information for the user to use in order to convert without googling*/
    std::cout << endl;
    std::cout << "\t\t\t\t\t- - - BASIC CONVERSION - - -" << endl;
    std::cout << "\t| 3600 seconds in 1 hour | ";
    std::cout << "60 seconds in 1 minute | ";
    std::cout << "60 minutes in 1 hour | ";
    std::cout << "1440 minutes in 24 hours |" << endl;
    
    /* Creates object for each conversion */
    TimeConversion convert_seconds_to_hours;
    TimeConversion convert_seconds_to_minutes;
    TimeConversion convert_minutes_to_hours;
    TimeConversion convert_hours_to_seconds;
    TimeConversion convert_minutes_to_seconds;
    
    /* Allows user to enter multiple entrys */
    bool continue_calculation = true;
    while (continue_calculation == true){ // infinite loop begins

        int pick_option; // Users pick gets stored here

        cout << "\n\tSelect option.\n" << "-------------------------------";
        cout << "\n[1] Convert Seconds to hours\n[2] Convert Seconds to minutes\n[3] Convert Minutes to hours\n[4] Convert Hours to Seconds\n[5] Convert Minute to Seconds\n[6] Quit program\n> ";
        
        cin >> pick_option; // Grabs users input
        cout << endl;

        if (cin.fail()){ // user fails to enter a integer
            cin.clear(); // clears cin
            cin.ignore(numeric_limits<streamsize>::max(), '\n'); // clears buffer and ignores all characters upto the new line.
            cout << "invalid input. Please only enter an integer value." << endl;
        }
        else{

        if (pick_option == 1){
           convert_seconds_to_minutes.convertSecondsToHours(); // Calls conversion from seconds to minutes : option 1
        }

        else if (pick_option == 2){
            convert_seconds_to_hours.convertSecondsToMinutes(); // Calls conversion from seconds to hours : option 2
        }

        else if (pick_option == 3){
            convert_minutes_to_seconds.convertMinutesToHours(); // Calls conversion from minutes to seconds : option 3
        }

        else if (pick_option == 4){
            convert_minutes_to_hours.convertHoursToSeconds(); // Calls conversion from minutes to hours : option 4
        }

        else if (pick_option == 5){
          convert_hours_to_seconds.convertMinutesToSeconds(); // Calls conversion from hours to minutes : option 5
        }

        else if (pick_option == 6) { // exits program : option 6
            continue_calculation = false;
        }

        else{
            cout << Seperator << endl;
            cout << " No correct input detected. Try again. " << endl; // incorrect input detection (number 0 < or > 6)
            cout << Seperator << endl;
            }
        }
    }
    return 0; 
}
        


/*
Bibliography:
    https://stackoverflow.com/questions/25696992/converting-seconds-to-hours-and-minutes-and-seconds
    https://users.ece.cmu.edu/~eno/coding/CppCodingStandard.html - mostly for nameing variables/classes/methods
*/
