from launch import LaunchDescription
from launch_ros.actions import Node
from launch.actions import ExecuteProcess

def generate_launch_description():
    
    # 1. Path to your bag file directory (Replace with your actual path)
    # Example: '/home/user/bag_files/my_camera_data'
    bag_file_path = 'PATH_TO_YOUR_BAG_FILE_DIRECTORY'

    # 2. Process to play the rosbag file
    rosbag_play = ExecuteProcess(
        cmd=['ros2', 'bag', 'play', bag_file_path, '--loop'],  
        output='screen'
    )

    # 3. Your image viewer node listening to the bag file's topic
    image_view_node = Node(
        package='ros2cv0_pkg',
        executable='image_view_exe',
        name='image_view',
        output='screen',
        # Updated to match the /cam_pub/image_raw topic stored inside the bag
        parameters=[
            {'cam_topic': '/cam_pub/image_raw'}
        ]
    )