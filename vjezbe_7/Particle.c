#include <iostream>
#include <math.h>
using namespace std;
class Particle{
    public:
        float v_,kut_,x_,y_,vx,vy;
        float pi = 3.14159;
        float g = 9.81;
        float t= 0;
        Particle(float v, float kut, float x, float y){
        v_= v;
        kut_= kut;
        x_ = x;
        y_ = y;
        float kut_r;
        kut_r= kut_*pi/180;
        vx = v*cos(kut_r);
        vy = v*sin(kut_r);
        }
    private:
        float __move(float dt){
            x_ = x_ + vx*dt;
            vy = vy - g*dt;
            y_ = y_+ vy*dt;
            t = t + dt;
            }
    public:
        float domet(float dt){
            do{
                __move(dt);
            }
            while (y_>=0);
            cout << x_ << endl;
        }
        float vrijeme(float dt){
            do{
                __move(dt);
            }
            while (y_>=0);
            cout << t << endl;
        }
};
int main(){
   Particle p1(50,45,0,0);
   p1.domet(0.01);
   p1.vrijeme(0.01);
}
