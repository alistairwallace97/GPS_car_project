#include <iostream>
#include <string>
#include <cstdlib>

using namespace std;

void parse_text_input(string input_string);
int work_out_where_to_go(string latitude, string longditude);
void control_motors(int direction_angle_number);

int main(){

  cout<<'example test'<<endl;
  //Open infile stream to text_data.txt
  bool not_done = false;
  string coordinates_text, lat, longd;
  while(!not_done){
    parse_text_input(coordinates_text, lat, longd);
    int direction = work_out_where_to_go(lat, longd);
  }


  return 0;
}

//Define Functions below

string parse_text_input(string input_string, string& latitude, string& longditude){

  cout<<'example'<<endl;
  //Data will be piped to text_data.txt and overwritten each time there is new data
  //Or we can just set this up to work with AT commands
  //Access text_data.txt via the infile stream and parse latitude and longditude data
  //Pass these quantities back by reference

}

int work_out_where_to_go(string latitude, string longditude){

  cout<<'example'<<endl;
  //Pole GPS module
  //Subtract current location from final destination and calculate where
  // it needs to go (write function)
  //Get bearing from compass (write function)
  //Work out what to do with motors (write function)
  //Return motor instruction in form of number or whatever

}

void control_motors(int direction_angle_number){

  //Use input from the function working out where to go
  //Convert this into signals at GPIO pins using a library

}
