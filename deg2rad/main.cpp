#include <iostream>
#include "deg2rad.h"

int main(int argc, char* argv[]) {
    float input = std::stof(argv[1]);
    std::cout << deg2rad(input);
}