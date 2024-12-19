#include "Bookie.hpp"
#include <string>
#include <iostream>
#include "csvstream.hpp"
#include <fstream>
#include <vector>
#include <unordered_map>
#include <map>

using namespace std;
class ArbFinder {
    public:
        ArbFinder(string & odds_file_in, double budget_in): budget(budget_in) {
            hash_map_builder(odds_file_in);
        }

        //REQUIRES: valid filename in correct formatting
        //MODIFIES: hash_map
        //EFFECT: reads in all odds data from filename and places it into a hash_map
        void hash_map_builder(string & filename) {
            csvstream csvin(filename);
            map<string, string> row;
            try{
                while(csvin >> row){
                    string sports_book = row["sports_book"];
                    string player_name = row["player_name"];
                    string category = row["category"];
                    double value = stod(row["value"]);
                    int over = stoi(row["over"]);
                    int under = stoi(row["under"]);

                    hash_map[{category, value}].push_back(Bookie(sports_book, player_name, over, under));
                }  

            } catch (const csvstream_exception &e){
                cout << "Error opening file: " << filename << endl;
                cerr << e.what() << "\n";
            }
        }
        //REQUIRES: Nothing
        //MODIFIES: Nothing
        //EFFECT: Prints what bets should be taken based on the data in the hash_map
        void bet_finder() {
            for(auto it=hash_map.begin(); it!=hash_map.end(); ++it){
                if((*it).second.size()>1){
                    for(auto combination : combinations((*it).second.size())){
                        if(is_arb((*it).second[combination.first], (*it).second[combination.second])){
                            cout << "Arbitrage Opportunity Found Between " << (*it).second[combination.first].get_sports_book() 
                            << "and" << (*it).second[combination.second].get_sports_book() <<  endl;
                            cout << (*it).second[combination.first].get_player_name() << ": " << (*it).first.second << (*it).first.first << endl;
                            money_distribution((*it).second[combination.first], (*it).second[combination.second]);
                        }
                    }
                }
            }
        }

        //REQUIRES: n > 1
        //MODIFIES: Nothing
        //EFFECT: Returns all combination of two numbers 0 to n.
        vector<pair<int, int>> combinations(int n){
            vector<pair<int, int>> output;
            for(int i = 0; i < n; ++i){
                for(int j = i+1; j <=n; ++j){
                    output.push_back({i,j});
                }
            }
            return output;
        }
        //REQUIRES: Two valid Bookie objects
        //MODIFIES: Nothing
        //EFFECT: Return TRUE if there is a arbitrage bet between both bookies
        bool is_arb(const Bookie & book1, const Bookie & book2){
            if(odds_to_prob(book1.get_odds().first) + odds_to_prob(book2.get_odds().second) < 1){
                return true;
            } else if (odds_to_prob(book1.get_odds().second) + odds_to_prob(book2.get_odds().first) < 1){
                return true;
            } else {
                return false;
            }
        }

        //REQUIRES: Arbitrage opportunity between both books
        //MODIFIES: Nothing
        //EFFECT: Prints how much money should be placed on which outome of book1
        // and does the same for bookie 2
        void money_distribution(const Bookie & book1, const Bookie & book2){
            if(odds_to_prob(book1.get_odds().first) + odds_to_prob(book2.get_odds().second) < 1){
                int total = odds_to_prob(book1.get_odds().first) + odds_to_prob(book2.get_odds().second);
                cout << book1.get_sports_book() << " OVER: " << budget*odds_to_prob(book1.get_odds().first)/total << endl;
                cout << book2.get_sports_book() << " UNDER: " << budget*odds_to_prob(book2.get_odds().second)/total << endl;
            } else if (odds_to_prob(book1.get_odds().second) + odds_to_prob(book2.get_odds().first) < 1){
                int total = odds_to_prob(book1.get_odds().second) + odds_to_prob(book2.get_odds().first);
                cout << book1.get_sports_book() << " UNDER: " << budget*odds_to_prob(book1.get_odds().second)/total << endl;
                cout << book2.get_sports_book() << " OVER: " << budget*odds_to_prob(book2.get_odds().first)/total << endl;
            }
        }

    private:
        double budget;
        unordered_map<pair<string, double>, vector<Bookie>> hash_map;

};



int main() {

    return 0;
}


