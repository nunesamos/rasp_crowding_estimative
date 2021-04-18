#include "opencv2/objdetect.hpp"
#include "opencv2/highgui.hpp"
#include "opencv2/imgproc.hpp"
#include "opencv2/videoio.hpp"
#include <iostream>
#include <string>
#include <dirent.h>


using namespace std;

using namespace cv;

/** Function Headers */
void detectAndDisplay( Mat frame );

/** Global variables */
CascadeClassifier DETECTOR;


/** @function main */
int main( int argc, const char** argv )
{

	Mat target_image = imread(argv[1]);
	auto copy_image = target_image.clone();
	char cascade_name[400];

	if (auto dir = opendir("../detector_architectures/")) {

		while (auto detector = readdir(dir)) {

			if (!detector->d_name || detector->d_name[0] == '.') continue; 

			sprintf(cascade_name,"../detector_architectures/%s", detector->d_name);
			DETECTOR.load(cascade_name);
			// DETECTOR.load("../detector_architectures/haarcascade_frontalface_alt2.xml");

			// equalizeHist(target_image, target_image );

			std::vector<Rect> detect;
			DETECTOR.detectMultiScale(target_image, detect);

			for ( size_t i = 0; i < detect.size(); i++ )
			{
				cv::Point pt1(detect[i].x, detect[i].y);
				cv::Point pt2(detect[i].x + detect[i].width, detect[i].y + detect[i].height);
				cv::rectangle(copy_image, pt1, pt2, cv::Scalar(0, 255, 0));
			}

		}

		imshow( "Capture - Face detection", copy_image);
		waitKey(0);
		closedir(dir);

	}

	
	return 0;
}

