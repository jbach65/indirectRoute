//
//  main.cpp
//  indirect_route
//
//  Created by Joshua Steinbach on 11/17/15.
//  Copyright (c) 2015 Joshua Steinbach. All rights reserved.
//

#include <iostream>
#include <vector>
#include <random>
#include <time.h>
#include <math.h>

#define PI 3.14159265

using namespace std;

void path(int destination_x, int destination_y, vector<double> &point_list)
{
    double current_x = point_list[point_list.size()-2];
    double current_y = point_list[point_list.size()-1];
    int fix_quadrant_x = 0;
    int fix_quadrant_y = 0;
    int direction_change_x = 0;
    int direction_change_y = 0;
    if (current_x > destination_x)
    {
        fix_quadrant_x = 180;
    }
    if (current_y > destination_y)
    {
        fix_quadrant_y = 180;
    }

    if(abs(destination_x - current_x) <= 1 && abs(destination_y - current_y) <= 1)
    {
        point_list.push_back(destination_x);
        point_list.push_back(destination_y);
        return;
    }
    else
    {
        int angle_sway = 45;
        double random_generated_angle = rand() % (angle_sway*2) + 1;
        double variation_angle = random_generated_angle - angle_sway;
        double destination_angle  = (180.0/PI) * atan((destination_y - point_list[1])/(destination_x - point_list[0]));
        double direction = destination_angle + variation_angle;
        double length = (rand() % 5 + 1);
        point_list.push_back(current_x + sin((direction+fix_quadrant_x) * (PI/180))*length);
        point_list.push_back(current_y + cos((direction+fix_quadrant_y) * (PI/180))*length);
        path(destination_x, destination_y, point_list);
    }
}

int main(int argc, const char * argv[]) {
    int start_point_x = 0;
    int start_point_y = 0;
    int end_point_x = 10;
    int end_point_y = 10;
    vector<double> point_list;
    point_list.push_back(start_point_x);
    point_list.push_back(start_point_y);
    srand (time(NULL));
    path(end_point_x, end_point_y, point_list);
    for (int i = 0; i < point_list.size() / 2 ; i++)
    {
        cout << "(" << point_list[i*2] << "," << point_list[i*2+1] << ")" << endl;
    }
    return 0;
}
