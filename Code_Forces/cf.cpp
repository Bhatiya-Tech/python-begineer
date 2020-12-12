#include<iostream>
using namespace std;
int main(){
    unsigned long long int m,n,a,ans1,ans2,answer;
    cin>>m;
    cin>>n;
    cin>>a;
    ans1=m/a;
    ans2=n/a;
    if (m%a!=0)
    {
        ans1=ans1+1;
    }
    if (n%a!=0)
    {
        ans2=ans2+1;
    }
    answer=ans1*ans2; 
    cout<<answer;
     return 0;    
}