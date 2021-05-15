[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
![PyPI](https://img.shields.io/pypi/v/video2images?style=plastic)
![Open Source? Yes!](https://badgen.net/badge/Open%20Source%20%3F/Yes%21/blue?icon=github)
![Python3](https://img.shields.io/badge/python->=3.5-green.svg)
[![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)](https://www.python.org/)
[![install](https://img.shields.io/badge/pip%20install-video2images-green)](https://pypi.org/project/video2images/)

[![DOI](https://zenodo.org/badge/299598465.svg)](https://zenodo.org/badge/latestdoi/299598465)
[![Downloads](https://pepy.tech/badge/video2images)](https://pepy.tech/project/video2images)
[![Downloads](https://pepy.tech/badge/video2images/month)](https://pepy.tech/project/video2images)
[![Downloads](https://pepy.tech/badge/video2images/week)](https://pepy.tech/project/video2images)

<p align="center">
<img src="https://raw.githubusercontent.com/AbhishekSalian/Video2Images/master/image/logo.png"></a>
</p>


## About
A library that helps to convert volumetric video data into image frames with adjustable frame capturing rate functionality.

The main reason why I created this library is to ease the video to image frames conversion process. During video annotation we need frames of an video or a subpart of a video and that too custom frame capture rate, so this problems led to this library development.

## How to install?
```pip install video2images```


## Requirements
It will be automatically installed
- tqdm, imageio, imageio-ffmpeg, moviepy

## Class Object Argument Description
<table>
<thead>
  <tr>
    <th>Argument</th>
    <th>Description</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td>video_filepath</td>
    <td>source path of the video</td>
  </tr>
  <tr>
    <td>start_time</td>
    <td>Default is None i.e 0s will be considered</td>
  </tr>
  <tr>
    <td>end_time</td>
    <td>Default is None i.e  till last duration will be <br>considered</td>
  </tr>
  <tr>
    <td>capture_rate</td>
    <td>No. of frames you want to capture per second.<br>For e.g if my capture_rate= 20 then only first 20<br>frames will captured out of input Frames per second rate</td>
  </tr>
  <tr>
    <td>save_format</td>
    <td>Output frame image extension. By default ".jpg"</td>
  </tr>
  <tr>
    <td>out_dir</td>
    <td>Output directory for saving images. If not specified <br>a folder will be made in current directory and saved</td>
  </tr>
</tbody>
</table>
</br>

#### **Note**:- The capture_rate if not specified will consider the original video frames per second rate

## Frame Capture Rate Explaination
<p align="center">
<img src="https://raw.githubusercontent.com/AbhishekSalian/Video2Images/master/image/capture%20rate.png"></a>
</p>

## Valid Extensions

### For Video
- .mov
- .avi
- .mpg
- .mpeg
- .mp4
- .mkv
- .wmv

### For Image
- .jpg, .jpeg
- .png
- .bmp
- .tiff, .tif
- .dicom, .dcm

## How to use?

### Minimal setting (Basic)
```
from video2images import Video2Images


Video2Images(video_filepath="--path-to-video-file--",
             out_dir="--path-to-output-directory--")

```

### Want to capture frames in between some interval
```
from video2images import Video2Images


# Lets take start_time to be 2mins i.e 120s
# & end_time to be 10 mins i,e 600s out of 20mins videos

Video2Images(video_filepath="--path-to-video-file--",
             start_time=120,
             end_time=600,
             out_dir="--path-to-output-directory--")

```
### Want only first 'f' frames out of 30 frames per second
```
from video2images import Video2Images


# Let say f = 20 i.e capturing only first 20 frames
Video2Images(video_filepath="--path-to-video-file--",
             capture_rate=20,
             out_dir="--path-to-output-directory--")
```

### Want output image to be saved in png or other format
```
from video2images import Video2Images


Video2Images(video_filepath="--path-to-video-file--",
             save_format=".png",
             out_dir="--path-to-output-directory--")

```
## From command line 
We can convert video frames to images by using simple command line as follows
```
$video2images --video_filepath <input video filepath> \
--start_time <some integer number in seconds> \ 
--end_time <some integer number in seconds> \
--capture_rate <some integer capture rate> \
--save_format <any one image extension> \
--out_dir <output folder name where all images will be pushed>
```

#### **Note**:- The output will be saved in a folder named frames_folder_{timestamp}


## Output Process Screenshot


<p align="left">
<img src="https://raw.githubusercontent.com/AbhishekSalian/Video2Images/master/image/output_ss.png"></a>
</p>

## Author

I will be happy to connect with you guys!!

[Linkedin](https://www.linkedin.com/in/abhishek-c-salian/)

[Twitter](https://www.twitter.com/@ACSalian)


## Citation
```
@software{abhishek_c_salian_2020_4384148,
  author       = {Abhishek C. Salian},
  title        = {Video2Images: A python library for video frames extraction for video annotation based task},
  month        = dec,
  year         = 2020,
  publisher    = {Zenodo},
  version      = {v1.1},
  doi          = {10.5281/zenodo.4384147},
  url          = {http://doi.org/10.5281/zenodo.4384147}
}
```

### **Any suggestions are most welcome.**
