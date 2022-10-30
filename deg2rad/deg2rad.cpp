#include "deg2rad.h"
#include <cmath>


/* constexpr float pi = 3.14159265358979323846;*/
float deg2rad(float deg) {
    return deg * (static_cast<float>(M_PI) / 180.0f);
}
