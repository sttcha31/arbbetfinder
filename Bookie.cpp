#include <utility>
#include "Bookie.hpp"
using namespace std;


Bookie::Bookie(double odd1in, double odd2in) : odds(odd1in, odd2in) {};

pair<double, double> Bookie::get_odds() {
    return odds;
}
pair<double, double> Bookie::get_prob() {
    return {odds_to_prob(odds.first), odds_to_prob(odds.second)};
}

double odds_to_prob(double odd){
    if(odd<0){
        return (-odd/(-odd+100));
    }
        return (100/(odd+100));
}