#include <ros/ros.h>
#include <jsk_rviz_plugins/OverlayText.h>
#include <std_msgs/String.h>
#include <string>

void chatterCallback(const std_msgs::String::ConstPtr& msg);

jsk_rviz_plugins::OverlayText text;
int main(int argc, char** argv)
{
  ros::init(argc, argv, "info_overlay_text_publisher");
  ros::NodeHandle nh;
  ros::Rate loop_rate(15);
  ros::Subscriber sub = nh.subscribe("logger", 1000, chatterCallback);
  text.text = "logger started";
  ros::Publisher text_pub = nh.advertise<jsk_rviz_plugins::OverlayText>("text", 1);
  while (ros::ok()){
    text_pub.publish(text);
    ros::spinOnce();
    loop_rate.sleep();
  }
  return 0;
}

void chatterCallback(const std_msgs::String::ConstPtr& msg)
{
  text.line_width = 1;
  text.text_size = 14;
  text.font = "Ubuntu";
  text.action = jsk_rviz_plugins::OverlayText::ADD;
  text.text = text.text+"\n"+msg->data;
}