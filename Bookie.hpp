#include <utility>
#include <string>
using namespace std;

class Bookie {
    private:
        pair<double, double> odds;
        string sports_book;
        string player_name;
    public:
        Bookie(string & sports_book_in, string &player_name_in, double odd1_in, double odd2_in);

        pair<double, double> get_odds() const;
        pair<double, double> get_prob() const;
        string get_sports_book() const;
        string get_player_name() const;

};

double odds_to_prob(double odd);

double odds_to_payout(double budget, double odd);