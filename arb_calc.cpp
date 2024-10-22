
#include "Bookie.hpp";
#include <vector>;
using namespace std;

double odds_to_prob(double odd){
    if(odd<0){
        return (-odd/(-odd+100));
    }
        return (100/(odd+100));
}

vector<int> arb_calc(Bookie book1, Bookeie Book2){

}