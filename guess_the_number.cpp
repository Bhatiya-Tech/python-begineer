#include<iostream>
using namespace std;

int main(){
    int num1;
    cout<<"Guess the number between 1 to 20"<<endl;
    for (size_t i = 0; i < 4; i++)
    {
      cout<<"Enter the First number:";
      cin>>num1;
     if(num1==16){
        cout<<"Congrulation";
     }
     else if (num1>16)
     {
        cout<<"You number is greater";
     }
     else
     {
        cout<<"Your number is small";
     }
    } 
    return 0;
}