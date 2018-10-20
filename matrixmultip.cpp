//
//  main.cpp
//  ScientificCpp
//
//  Created by Sema Kuru on 09/10/2018.
//  Copyright © 2018 Sema Kuru. All rights reserved.
//

#include <iostream>
#include <cmath>                            // http://www.cplusplus.com/reference/cmath/
using namespace std;

int const row1 = 3;                         // Enter sizes of matrices being entered
int const col1 = 3;
int const row2 = 3;
int const col2 = 3;
int const row3 = row1;
int const col3 = col2;

int main() {
    // TESTESTESTSET
    if ( row1 != col2) {
             cout << "These matrices cannot be multiplied due to size" << endl ;
          }
    
    else {
        cout << "Multiplying..." << endl;
        int matrix1[row1][col1] = {                             // Enter matrix 1 values here
            { 2, -5 , 2},
            { 0, -1 , 3},
            { -1, 6 , 1} };
        int matrix2[row2][col2] = {                             // Enter matrix 2 values here
            { 0, -1 , 9 },
            { 12, 3 , -2 },
            { -2, 2 , 1 }};
        int matrixSum[row3][col3];
        
        for( int i = 0 ; i < row1 ; i++ ){                        // For each row in first matrix
            for ( int j = 0 ; j < col2 ; j++ ) {                  // For each column in second matrix while at same row of first matrix
                int sumElements = 0;
                for ( int k = 0 ; k < col1 ; k++ ) {              // Each element in that row (M1) and column (M2) multiplied and summed over
                    sumElements = sumElements + matrix1[i][k]*matrix2[k][j];
                };
                matrixSum[i][j] = sumElements;
                cout << "MATRIX SUM " << matrixSum[i][j] << " i = " << i << " j = " << j << flush;
                // CHECKED ONLINE, GIVES CORRECT RESULT
            };
        };
        
    }
    return 0;
}


