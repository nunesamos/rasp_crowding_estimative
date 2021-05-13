#!/bin/bash

cd opencv-mtcnn
mkdir build
cd build
cmake ..
cmake --build .

./sample/crwd_fd ../data/models ../mercado2.jpg
./sample/crwd_fd ../data/models ../crowd.jpg



clear
<<<<<<< HEAD
=======

>>>>>>> 07fbd9d7cfc9bb16c976d2e78c1f25dcb22ae50d
