from launch_ros.actions import Node

from launch import LaunchDescription


def generate_launch_description():
   return LaunchDescription(
       [
           Node(
               package="usb_cam",
               executable="usb_cam_node_exe",
               name="usb_cam",
               output="screen",
               parameters=[
                   # --- Essential Hardware/WSL Connection Settings ---
                   {"video_device": "/dev/video0"},  # 0: builtin, 2: external USB webcam
                   {"image_width": 320},
                   {"image_height": 240},
                   {"framerate": 30.0},
                   # {'pixel_format': 'mjpeg2rgb'},  # Hardware compression over usbipd
                   {"pixel_format": "yuyv2rgb"},
                   {"io_method": "mmap"},
                   # --- Image/Brightness Controls ---
                   # Note: Parameter names depend on the driver version.
                   # If these specific parameters aren't parsed by your version,
                   # keep using 'v4l2-ctl' in a separate terminal.
                   # {'brightness': 180},           # Boost low-light performance, was 200
                   # {'gain': 150},                 # Increases sensitivity if supported
                   # {'autoexposure': False},       # Set to False to manually override exposure
                   # {'exposure': 150},             # Adjust exposure absolute value
                   # --- Topic Configuration ---
                   # usb_cam ROS2 pkg behaves slightly uniquely: changing camera_name changes the metadata internally,
                   # but the node always publishes to the literal topic name /image_raw
                   # unless you use a ROS 2 Remapping rule inside the launch file.
                   {"camera_name": "default_cam"},
                   {"frame_id": "camera_link"},
               ],
           ),
           Node(
               package="ros2cv0_pkg",
               executable="image_view_exe",
               name="image_view",
               output="screen",
               # Passing the parameter to your custom image viewer node
               parameters=[{"cam_topic": "/image_raw"}],
           ),
       ]
   )
