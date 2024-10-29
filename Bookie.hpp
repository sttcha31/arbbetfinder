#include <utility>
using namespace std;

class Bookie {
    private:
        pair<double, double> odds;
    public:
        Bookie(double odd1in, double odd2in) {};

        pair<double, double> get_odds();
        pair<double, double> get_prob();

};

double odds_to_prob(double odd);