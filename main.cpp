#include "Bookie.hpp"
#include <thread>
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

                    hash_map[{category, value}].push_back(Bookie(sports_book, over, under));
                }  

            } catch (const csvstream_exception &e){
                cout << "Error opening file: " << filename << endl;
                cerr << e.what() << "\n";
            }
        }
        //REQUIRES: Nothing
        //MODIFIES: Nothing
        //EFFECT: Prints what bets should be taken based on the data in the hash_map
        void bet_finder() {}

        //REQUIRES: Two valid Bookie objects
        //MODIFIES: Nothing
        //EFFECT: Return TRUE if there is a arbitrage bet between both bookies
        bool is_arb(const Bookie & book1, const Bookie & book2){

        }

        //REQUIRES: Arbitrage opportunity between both books
        //MODIFIES: Nothing
        //EFFECT: Prints how much money should be placed on which outome of book1
        // and does the same for bookie 2
        void money_distribution(const Bookie & book1, const Bookie & book2){

        }

    private:
        double budget;
        unordered_map<pair<string, double>, vector<Bookie>> hash_map;

};



int main() {

    return 0;
}


