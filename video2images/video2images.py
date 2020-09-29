#!/usr/bin/python3

"""Video2Frames a python library which helps to convert the video into
   frames with various custom settings available
"""

from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip
import imageio
import moviepy.editor
import os
import argparse
from tqdm import tqdm
import sys
from datetime import datetime as dt


class Video2Images:

    def __init__(self,
                 video_filepath,
                 start_time=None,
                 end_time=None,
                 capture_rate=None,
                 save_format=".jpg",
                 out_dir=None):

        """
        Args:

            video_filepath ([str]): source path of the video.

            start_time ([int], optional): Start time point of the video from\
                                           where the frames needs to be taken.
                                          Default is 0s will be taken.

            end_time ([int], optional): End time point of video from where the\
                                         frames capturing needs stop.
                                        Default is original video duration\
                                         will be taken.

            capture_rate ([int], optional): It is no. of frames which\
                                            needs to be captured per second.
                                            Default is original frame rate.


            out_dir (str, optional): The out directory where we want to\
                                     save the files. Defaults to
                                     Current working directory folder
        """

        self.video_filepath = video_filepath

        self.start_time = start_time

        self.end_time = end_time

        self.capture_rate = capture_rate

        self.save_format = save_format

        self.out_dir = out_dir

        # Capture rate should not be negative condition check
        if capture_rate <= 0:
            sys.exit("Frame Capture Rate cannot be <= 0")

        # Folder time stamp
        folder = "frames_folder" + str(dt.now().strftime('%Y-%m-%d %H:%M:%S'))

        # If output directory is not specified
        if self.out_dir is None:

            os.mkdir(os.getcwd() + os.path.sep + folder)

            self.out_dir = os.path.join(os.getcwd(), folder, )

            print("Making directory in", self.out_dir)

        else:

            # Checking if output directory exist or not
            print(self.out_dir)
            if os.path.exists(self.out_dir):

                os.mkdir(self.out_dir + os.path.sep + folder)
                self.out_dir = self.out_dir + os.path.sep + folder

            else:
                sys.exit("Output directory doesnot exist! Please check the output path")

        # Getting base vide filename
        video_filename = self.video_filepath.split(os.path.sep)[-1]

        # Extracting extension of input vide file
        file_extension = video_filename.split(".")[-1]

        # Valid Video Extensions
        VIDEO_EXTENSIONS = ["mov", "avi", "mpg", "mpeg", "mp4", "mkv", "wmv"]

        # Valid Output Image Extension
        IMAGE_EXTENSIONS = [".jpg", ".png", ".jpeg", ".bmp",
                            ".tiff", ".tif", ".dicom", ".dcm"]

        # Checking for valid input video file extension
        if file_extension not in VIDEO_EXTENSIONS:

            sys.exit("Input a Valid Video File")

        # Checking for valid output image file extension format
        if self.save_format not in IMAGE_EXTENSIONS:

            sys.exit("Input a valid image format")

        # Getting duration of the original inout video
        video_duration, vformat = self.__getDuration()

        print("Video Duration is-" + f"{vformat[0]}:{vformat[1]}:{vformat[2]}")

        # Checking if the input end time is > total duration of video or not
        if self.end_time is not None and self.end_time > video_duration:

            sys.exit("End time is greater than total duration of video")

        # Video clip extraction from original video input
        if self.start_time is not None or self.end_time is not None:

            if self.start_time is None:
                self.start_time = 0

            elif self.end_time is None:
                self.end_time = video_duration

            # Output filename for clipped video
            filename = f'{video_filename.split(".")[0]}_cut.{file_extension}'

            # Extraction of subclip function call
            ffmpeg_extract_subclip(
                self.video_filepath,
                self.start_time,
                self.end_time,
                targetname=self.out_dir + os.path.sep + filename)

            # Setting Video filepath to clipped video filepath
            self.video_filepath = os.path.join(self.out_dir, filename)

        # Initiate the video2image conversion
        self.__start()

    # Get total duration of input video
    def __getDuration(self):
        """To get overall duration of video

        Returns:
            video duration &
            [hours , minutes , seconds]  
        """

        # Reading the video file
        video = moviepy.editor.VideoFileClip(self.video_filepath)

        # Getting total duration in sec
        video_duration = int(video.duration)

        seconds = video_duration

        hours = seconds // 3600
        seconds %= 3600

        mins = seconds // 60
        seconds %= 60

        return video_duration, [hours, mins, seconds]

    # The Start
    def __start(self):
        """ Method which starts the frame capturing
        """

        # Reading video
        video_reader = imageio.get_reader(self.video_filepath)

        # meta_data of video
        meta_data = video_reader.get_meta_data()

        # Getting Frames per second value
        FPS = meta_data['fps']

        if self.capture_rate >= FPS:
            sys.exit("Capture rate cannot be greater than maximum FPS of input video")

        duration = meta_data['duration']

        print("Frames per Sec", FPS)

        print(meta_data)

        image_count = 1

        # Capture rate after how many sec need to save the image
        if self.capture_rate is not None:

            FPS = int(FPS/self.capture_rate)

        # Iterate over entire frames in video
        for i, img in tqdm(enumerate(video_reader),
                           desc="Capturing...",
                           unit="frames",
                           total=int(duration*meta_data['fps'])):

            # main capture frame logic
            if (i+1) % FPS == 0:

                imageio.imsave(
                    os.path.join(self.out_dir, '%08d.jpg' % image_count),
                    im=img
                    )

                image_count += 1

        print("Done. Total frames captured:", image_count)
