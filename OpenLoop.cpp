// This is the program to do open loop control for drawing M.
#include "ros/ros.h"
#include "geometry_msgs/Twist.h"
const double PI = 3.14159;

void rotate(double speed, double distance, double angular_distance, bool isClock, ros::Publisher pub)
{
	
	geometry_msgs::Twist msg;

	double angular_speed = speed *PI/180;
	double relative_distance = distance * PI /180;
	
	if(isClock == true)
		msg.angular.z = angular_speed;
	else
		msg.angular.z = - angular_speed;

	double t0, t1;     	
	t0 = ros::Time::now().sec;

	while(angular_distance < relative_distance)
	{
		pub.publish(msg);
		t1 = ros::Time::now().sec;
		angular_distance = angular_speed*(t1-t0);			
	}
	msg.angular.z = 0;
	pub.publish(msg);
}

void move(double speed, double distance, double linear_distance, bool isForward, ros::Publisher pub)
{
	
	geometry_msgs::Twist msg;
	
	if(isForward == true)
		msg.linear.x = speed;
	else
		msg.linear.x = -speed;
	double t0, t1;     	
	t0 = ros::Time::now().sec;

	while(linear_distance < distance)
	{
		pub.publish(msg);
		t1 = ros::Time::now().sec;
		linear_distance = speed*(t1-t0);			
	}
	msg.linear.x = 0;
	pub.publish(msg);
}

int main(int argc, char **argv)
{
	const double ANGULAR_SPEED = 15;
	const double ANGULAR_SPEED_2 = 30;
	const double LINEAR_SPEED = 0.5;
        const double LINEAR_SPEED_2 = 1;
	
	const double DISTANCE = 2.828;
	const double DIST = 45;
	
	double linear_distance = 0;   
	double angular_distance = 0;

	int flag = 0;

	ros::init(argc, argv, "move_turtle");
	ros::NodeHandle node;
	ros::Publisher pub = node.advertise<geometry_msgs::Twist> ("/turtle1/cmd_vel", 10);
	ros::Rate rate(10);	
	
	ROS_INFO("Starting to move forward");

	while (ros::ok())
	{	
		while (flag == 0)
		{		
			move(LINEAR_SPEED, 0.8, 0 , false, pub);
			
			rotate(ANGULAR_SPEED_2, 90, 0, false, pub);	
			move(LINEAR_SPEED, 0.5, 0, true, pub);

			rotate(ANGULAR_SPEED_2, 90, 0, true, pub);	
			move(LINEAR_SPEED_2,2, 0, true, pub);
			
			rotate(ANGULAR_SPEED_2, 90, 0, true, pub);	
			move(LINEAR_SPEED,0.5, 0, true, pub);
			
			rotate(ANGULAR_SPEED, 90, 0, true, pub);	
			move(LINEAR_SPEED,0.5, 0, true, pub);
			
			rotate(ANGULAR_SPEED_2, 90, 0, false, pub);	
			move(LINEAR_SPEED_2,4, 0, true, pub);

			rotate(ANGULAR_SPEED_2, 90, 0, false, pub);	
			move(LINEAR_SPEED,0.5, 0, true, pub);
			
			rotate(ANGULAR_SPEED_2, 90, 0, true, pub);	
			move(LINEAR_SPEED,0.5, 0, true, pub);
			
			rotate(ANGULAR_SPEED_2, 90, 0, true, pub);	
			move(LINEAR_SPEED,1.5, 0, true, pub);
			
			rotate(ANGULAR_SPEED, 45, 0, true, pub);	
			move(LINEAR_SPEED_2,2, 0, true, pub);

			rotate(ANGULAR_SPEED_2, 90, 0, false, pub);	
			move(LINEAR_SPEED_2,2, 0, true, pub);
			
			rotate(ANGULAR_SPEED, 45, 0, true, pub);	
			move(LINEAR_SPEED,1.5, 0, true, pub);
			
			rotate(ANGULAR_SPEED, 90, 0, true, pub);	
			move(LINEAR_SPEED, 0.5, 0, true, pub);

			rotate(ANGULAR_SPEED_2, 90, 0, true, pub);	
			move(LINEAR_SPEED, 0.5, 0, true, pub);
			
			rotate(ANGULAR_SPEED_2, 90, 0, false, pub);	
			move(LINEAR_SPEED_2,4, 0, true, pub);
			
			rotate(ANGULAR_SPEED_2, 90, 0, false, pub);	
			move(LINEAR_SPEED, 0.5, 0, true, pub);
			
			rotate(ANGULAR_SPEED, 90, 0, true, pub);	
			move(LINEAR_SPEED, 0.5, 0, true, pub);
			
			rotate(ANGULAR_SPEED_2, 90, 0, true, pub);	
			move(LINEAR_SPEED_2,2, 0, true, pub);
			
			rotate(ANGULAR_SPEED_2, 90, 0, true, pub);	
			move(LINEAR_SPEED,0.5, 0, true, pub);
			
			rotate(ANGULAR_SPEED_2, 90, 0, true, pub);	
			move(LINEAR_SPEED,0.5, 0, true, pub);
				
			rotate(ANGULAR_SPEED, 90, 0, false, pub);	
			move(LINEAR_SPEED_2,3, 0, true, pub);
			
			rotate(ANGULAR_SPEED, 135, 0, false, pub);	
			move(LINEAR_SPEED_2,2, 0, true, pub);

			rotate(ANGULAR_SPEED_2, 90, 0, true, pub);	
			move(LINEAR_SPEED_2,2, 0, true, pub);
			
			rotate(ANGULAR_SPEED, 135, 0, false, pub);	
			move(LINEAR_SPEED_2,3, 0, true, pub);
				
			flag = 1;
	
		
		}
		rate.sleep(); // loop for the rest of the cycle	
	}
	
}
