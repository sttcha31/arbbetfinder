#include <utility>
#include "Bookie.hpp"
using namespace std;


Bookie::Bookie(string & sports_book_in, double odd1_in, double odd2_in) : sports_book(sports_book_in), odds(odd1_in, odd2_in) {};

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