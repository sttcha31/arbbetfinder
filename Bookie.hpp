#include <utility>
using namespace std;

class Bookie {
    private:
        pair<double, double> odds;
        string sports_book;
    public:
        Bookie(string & sports_book_in, double odd1_in, double odd2_in) {};

        pair<double, double> get_odds() const;
        pair<double, double> get_prob() const;
        string get_sports_book() const;

};

double odds_to_prob(double odd);