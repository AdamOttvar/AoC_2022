//
// Created by AdamOttvar on 2022-11-16
//

#include "day00.h"

int day00(bool part_two) {
#ifndef AoC_RUN_TEST
    cout << "AoC day00: part " << (part_two ? "two" : "one") << endl;
#endif
    auto directions = AoC::read_file<char, vector<char>>("input/input00.txt");
    int result = 0;
    int nbrOfInstructions = 0;

    for (auto dir : directions)
    {
        nbrOfInstructions += 1;
        if (dir == '(')
        {
            result += 1;
        } 
        else if (dir == ')')
        {
            result -= 1;
        }
        else
        {
            cout << "Unknown direction" << endl;
        }
        if (part_two && (result < 0))
        {
            return nbrOfInstructions;
        }
        
 
    }
    return result;
}

#ifndef AoC_RUN_TEST
int main() {
    int result;
    result = day00(false);
    cout << "Result: " << result << endl;
    result = day00(true);
    cout << "Result: " << result << endl;
    return 0;
}
#endif