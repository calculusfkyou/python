#include <iostream>
#include <cmath>
#include <iomanip>
using namespace std;

int main()
{
    int x,n;
    while(cin>>x>>n){
        float p=pow(x,n);
        cout<<setprecision(4)<<p<<'\n';
    }
    return 0;
}
