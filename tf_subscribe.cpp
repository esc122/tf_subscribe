#include "ros/ros.h"
#include "tf2_msgs/TFMessage.h"

void tfCallback(const tf2_msgs::TFMessage::ConstPtr& msg)
{
  ROS_INFO("translation_x: [%f]", msg->transforms[1].transform.translation.x);
  ROS_INFO("translation_y: [%f]", msg->transforms[1].transform.translation.y);
  ROS_INFO("rotation_z: [%f]", msg->transforms[1].transform.rotation.z);
}

int main(int argc, char **argv)
{
 
  ros::init(argc, argv, "tf_subscribe");
  ros::NodeHandle n;
  ros::Subscriber sub = n.subscribe<tf2_msgs::TFMessage>("/tf", 1000,tfCallback);
  ros::spin();

  return 0;
}