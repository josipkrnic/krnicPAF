#include <iostream>
using namespace std;
void pravac() {
float x1,y1,x2,y2;
float k,l;
cout << "Unesite x koordinatu prve tocke: ";
cin >> x1;
cout << "Unesite y koordinatu prve tocke: ";
cin >> y1;
cout << "Unesite x koordinatu druge tocke: ";
cin >> x2;
cout << "Unesite y koordinatu druge tocke: ";
cin >> y2;
k = (y2-y1)/(x2-x1);
l = y1 - k*x1;
if (x1 == x2) {
cout << "Jednadzba pravca jest x = " << x1 <<endl;
}
else {
cout << "Jednadzba pravca jest y = " << k << "x + " << l <<endl;
}
}
int main() {
pravac();
return 0;
}
