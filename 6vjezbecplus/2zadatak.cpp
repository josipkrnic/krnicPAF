#include <iostream>
#include <math.h>
using namespace std;
void kruznica() {
float x,y,r,x1,y1,d;
cout << "Unesite x koordinatu ishodišta kružnice:";
cin >> x;
cout << "Unesite y koordinatu ishodišta kružnice: ";
cin >> y;
cout << "Unesite radijus kružnice: ";
cin >> r;
cout << "Unesite x koordinatu proizvoljne točke: ";
cin >> x1;
cout << "Unesite y koordinatu proizvoljne točke: ";
cin >> y1;
d = sqrt(pow((x1-x),2.0) + pow((y1-y),2.0));
if (r < 0) {
    cout << "Radijus kružnice mora biti veći od 0!";
} else {
  if (d < r) {
    cout << "Točka se nalazi unutar kružnice.";
    } else if (d == r){
      cout << "Točka se nalazi na kružnici.";
    } else {
      cout << "Točka se nalazi izvan kružnice.";
        }
    }
}
int main() {
    kruznica();
    return 0;
}