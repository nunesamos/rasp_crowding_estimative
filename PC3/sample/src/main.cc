#include <boost/filesystem.hpp>
#include <boost/filesystem/path.hpp>
#include <boost/timer/timer.hpp>

#include <opencv2/dnn.hpp>
#include <opencv2/highgui.hpp>
#include <opencv2/imgproc.hpp>
#include <opencv2/objdetect.hpp>
#include <opencv2/highgui.hpp>
#include <opencv2/videoio.hpp>

#include <mtcnn/detector.h>

#include <iostream>
#include <string>
#include <dirent.h>

using namespace std;
using namespace cv;

namespace fs = boost::filesystem;

using rectPoints = std::pair<cv::Rect, std::vector<cv::Point>>;
CascadeClassifier DETECTOR;

static cv::Mat drawRectsAndPoints(const cv::Mat &img,
                                  const std::vector<rectPoints> data) {
  cv::Mat outImg;
  img.convertTo(outImg, CV_8UC3);

  for (auto &d : data) {
    cv::rectangle(outImg, d.first, cv::Scalar(0, 0, 255));
    auto pts = d.second;
    for (size_t i = 0; i < pts.size(); ++i) {
      cv::circle(outImg, pts[i], 3, cv::Scalar(0, 0, 255));
    }
  }
  return outImg;
}


int main(int argc, char **argv) {

 
	fs::path modelDir = fs::path(argv[1]);

	ProposalNetwork::Config pConfig;
	pConfig.caffeModel = (modelDir / "det1.caffemodel").string();
	pConfig.protoText = (modelDir / "det1.prototxt").string();
	pConfig.threshold = 0.6f;

	RefineNetwork::Config rConfig;
	rConfig.caffeModel = (modelDir / "det2.caffemodel").string();
	rConfig.protoText = (modelDir / "det2.prototxt").string();
	rConfig.threshold = 0.7f;

	OutputNetwork::Config oConfig;
	oConfig.caffeModel = (modelDir / "det3.caffemodel").string();
	oConfig.protoText = (modelDir / "det3.prototxt").string();
	oConfig.threshold = 0.7f;

	MTCNNDetector detector(pConfig, rConfig, oConfig);
	cv::Mat target_image = cv::imread(argv[2]);

	std::vector<rectPoints> data;
	std::vector<Face> det;

	det = detector.detect(target_image, 20.f, 0.709f);

	for (size_t i = 0; i < det.size(); ++i) {
	std::vector<cv::Point> pts;
	for (int p = 0; p < NUM_PTS; ++p) {
	pts.push_back(
	  cv::Point(det[i].ptsCoords[2 * p], det[i].ptsCoords[2 * p + 1]));
	}

	auto rect = det[i].bbox.getRect();
	auto d = std::make_pair(rect, pts);
	data.push_back(d);
	}

	auto result_image = drawRectsAndPoints(target_image, data);
	auto result_image2 = result_image.clone();


	char cascade_name[400];

	if (auto dir = opendir("../detector_architectures/")) {

		while (auto detector = readdir(dir)) {

			if (!detector->d_name || detector->d_name[0] == '.') continue; 

			sprintf(cascade_name,"../detector_architectures/%s", detector->d_name);
			DETECTOR.load(cascade_name);
			// DETECTOR.load("../detector_architectures/haarcascade_frontalface_alt2.xml");

			// equalizeHist(target_image, target_image );
			
			cout << cascade_name << endl;

			std::vector<Rect> detect;
			DETECTOR.detectMultiScale(target_image, detect);

			for ( size_t i = 0; i < detect.size(); i++ ){
				cv::Point pt1(detect[i].x, detect[i].y);
				cv::Point pt2(detect[i].x + detect[i].width, detect[i].y + detect[i].height);
				cv::rectangle(result_image2, pt1, pt2, cv::Scalar(0, 255, 0));
			}

		}

			
			closedir(dir);

	}
	else {
		cout << "Nao foi possivel abrir diretorio" << endl;
	}


	cv::imshow("Resultado", result_image2);
	cv::waitKey(0);

  return 0;
}
