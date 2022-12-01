//
// Created by AdamOttvar on 2022-12-01
//

#include "day01.h"
#include <string>
#include <algorithm>

int day01(bool part_two) {
#ifndef AoC_RUN_TEST
    cout << "AoC day01: part " << (part_two ? "two" : "one") << endl;
#endif
    ifstream input("input/input01.txt");

    vector<int> all_elf_calories;

    float result = 0.0;
    int elf_calories = 0;
    if (input.is_open()) {
        for (std::string line; getline(input, line);) {
            try {
                elf_calories += std::stoi(line);
            }

            catch (std::invalid_argument &e) {
                all_elf_calories.push_back(elf_calories);
                elf_calories = 0;
            }
        }
    }
    std::sort(all_elf_calories.begin(), all_elf_calories.end());

    if (part_two) {
        return *(all_elf_calories.end() - 1) + *(all_elf_calories.end() - 2) + *(all_elf_calories.end() - 3);
    }
    else {
        return *(all_elf_calories.end() - 1);
    }
    
}

#ifndef AoC_RUN_TEST
int main() {
    int result;
    result = day01(false);
    cout << "Result: " << result << endl;
    result = day01(true);
    cout << "Result: " << result << endl;
    return 0;
}
#endif