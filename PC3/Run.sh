#!/bin/bash

cd opencv-mtcnn
mkdir build
cd build
cmake ..
cmake --build .

./sample/crwd_fd ../data/models ../data/2007_007763.jpg
