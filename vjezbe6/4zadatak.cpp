#include <iostream>
#include <math.h>
using namespace std;
void sustav() {
    float a1,b1,c1,a2,b2,c2,D,Dx,Dy,x,y;
    cout << "Prva jednadžba: a1*x + b1*y = c1 \n";
    cout << "Unesite koeficijent(a1) uz x za prvu jednadžbu: ";
    cin >> a1;
    cout << "Unesite koeficijent(b1) uz y za prvu jednadžbu: ";
    cin >> b1;
    cout << "Unesite iznos prve jednadžbe(c1): ";
    cin >> c1;
    cout << "Druga jednadžba: a2*x + b2*y = c2 \n";
    cout << "Unesite koeficijent(a2) uz x za drugu jednadžbu: ";
    cin >> a2;
    cout << "Unesite koeficijent(b2) uz y za drugu jednadžbu: ";
    cin >> b2;
    cout << "Unesite iznos druge jednadžbe(c2): ";
    cin >> c2;
    D = (a1*b2-a2*b1);
    Dx = (c1*b2-b1*c2);
    Dy = (a1*c2-a2*c1);
    x = (Dx/D);
    y = (Dy/D);
    cout << "x iznosi " << x << ",a y " << y <<endl;
}
int main() {
    sustav();
    return 0;
}
