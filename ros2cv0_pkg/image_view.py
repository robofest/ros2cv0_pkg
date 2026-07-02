import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Image
import cv2
from cv_bridge import CvBridge

class ImageViewer(Node):

    def __init__(self):
        super().__init__('image_viewer_node')
        
        # Initialize the CvBridge utility
        self.bridge = CvBridge()
        
        # Subscribe to the webcam stream topic published by usb_cam using a param for the topic name

        # 1. Declare the parameter with a default topic name
        self.declare_parameter('cam_topic', '/image_raw')
        
        # 2. Read the parameter value
        cam_topic = self.get_parameter('cam_topic').value
        
        # 3. Terminate if the param configuration is empty or invalid
        if not cam_topic or cam_topic.strip() == "":
            self.get_logger().fatal("Camera topic parameter is empty! Terminating node.")
            raise RuntimeError("Invalid camera topic configuration.")
        
        # 4. Subscribe to the topic retrieved from the parameter
        self.subscription = self.create_subscription(
            Image, cam_topic, self.listener_callback, 10)
            
        self.get_logger().info('Image Viewer node started. Waiting for frames...')

    def listener_callback(self, msg):
        try:
            # Convert the ROS 2 Image message into a standard OpenCV image array
            cv_image = self.bridge.imgmsg_to_cv2(msg, desired_encoding='bgr8')
            
            # Display the frame in a window
            cv2.imshow("ROS2 Webcam Feed", cv_image)
            
            # Must call waitKey to refresh the GUI frame window
            cv2.waitKey(1)
            
        except Exception as e:
            self.get_logger().error(f'Failed to convert image: {str(e)}')

    def destroy_node(self):
        # Clean up OpenCV windows on shutdown
        cv2.destroyAllWindows()
        super().destroy_node()


def main(args=None):
    rclpy.init(args=args)
    image_viewer = ImageViewer()
    
    try:
        rclpy.spin(image_viewer)
    except KeyboardInterrupt:
        pass
    finally:
        image_viewer.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()
