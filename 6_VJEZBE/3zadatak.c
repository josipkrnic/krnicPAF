#include <iostream>
#include <math.h>
#include<algorithm>
using namespace std;
void polje_realnih_brojeva(float polje[], int R) {
    for(int i = 0; i < R; i++) {
        cout << polje[i] << " ";
    }
    cout <<endl;
}
void polje_u_intervalu(float polje[], int R, int a, int b) {
    for(int i = 0; i < R; i++) {
        if(polje[i] >= a && polje[i] <= b) {
            cout << polje[i] <<" ";
        }
    }
    cout <<endl;
}
void razmjena(float polje[], int i, int j) {
    float k = polje[i];
    polje[i] = polje[j];
    polje[j] = k;
}
int main() {
    float polje[7] = {4, -2, 3.14, -1.41, 10, -5, 8};
    polje_realnih_brojeva(polje, 7);
    polje_u_intervalu(polje, 7, -3, 7);
    razmjena(polje, 4, 5);
    polje_realnih_brojeva(polje, 7);
    reverse(begin(polje), end(polje));
    polje_realnih_brojeva(polje, 7);
    sort(begin(polje), end(polje));
    polje_realnih_brojeva(polje, 7);
    return 0;
}
