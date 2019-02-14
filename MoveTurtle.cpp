// How to use pose to make changes ??


#include "ros/ros.h"
#include "geometry_msgs/Twist.h"
#include "turtlesim/Pose.h"
#include <math.h>

const double PI = 3.14159;

class Update{

	public:
	double x, y, theta;
	void update_pose(const turtlesim::PoseConstPtr& msg)
	{
	
		// This gives us fixed number of values after the decimal
		this->x = ((int) (msg->x*100 +0.5));
		this->y = ((int) (msg->y*100 +0.5));
	
		this->x = x/100;
		this->y = y/100;
		if(msg->theta > 0)
			this->theta = ((int) (msg->theta*100 +0.5));
		else
			this->theta = ((int) (msg->theta*100 - 0.5));
		this->theta = this->theta/100;


		ROS_INFO("x: %f, y: %f, theta: %f", x, y, theta);
	
		
	}
};
double ret_degree(double initial, double new_value)
{
	if(initial + new_value > 360)
		return ((initial+new_value) - 360);
	else
		return (initial + new_value);
}
double abs_value(double initial, double new_value)
{
	if(initial > new_value)
		return initial-new_value;
	else
		return new_value-initial;
}
void rotate(double check_angle, ros::Publisher pub, Update& u)
{
	
	geometry_msgs::Twist msg;
	
	double ang_rad = check_angle*PI/180;
	ROS_INFO("Radian value is %f %f", check_angle, ang_rad);
	
	ros::spinOnce();
	while(abs_value(u.theta,ang_rad) > 0.02)
	{	
		ros::spinOnce();		
		msg.linear.x = 0;
		msg.linear.y = 0;
		msg.linear.z = 0;
		
		msg.angular.x = 0;
		msg.angular.y = 0;
		
		if(u.theta > ang_rad- 0.02)
			msg.angular.z = 0.5*(u.theta - ang_rad);
		else
			msg.angular.z = 0.5*(ang_rad - u.theta);
		pub.publish(msg);			
	}
	msg.angular.z = 0;
	pub.publish(msg);
}

double euclid(double initial_x,double initial_y, double final_x,double final_y)
{
	return sqrt(pow(final_x-initial_x, 2) + pow(final_y-initial_y, 2)); 
}	
void move(double speed, double distance, double linear_distance, bool isForward, ros::Publisher pub, Update& u)
{
	
	geometry_msgs::Twist msg;
	float initial_x, initial_y, initial_theta;

	
	ros::spinOnce();

	initial_x = u.x;
	initial_y = u.y;	
		
	
	while(distance - euclid(initial_x, initial_y , u.x, u.y) > 0.02)
	{		
		ros::spinOnce();
		double value = distance - euclid(initial_x, initial_y , u.x, u.y);
		msg.linear.x = (0.5) *value;
		msg.linear.y = 0;
		msg.linear.z = 0;
	
		msg.angular.x = 0;
		msg.angular.y = 0;
		msg.angular.z = 0;


		pub.publish(msg);							
	}
	msg.linear.x = 0;
	pub.publish(msg);
}

int main(int argc, char **argv)
{
	const double LINEAR_SPEED = 0.25;
        const double LINEAR_SPEED_2 = 1;
	
	double angle = 0;

	int flag = 0;

	ros::init(argc, argv, "move_turtle");
	ros::NodeHandle node;
	Update u;
	ros::Publisher pub = node.advertise<geometry_msgs::Twist> ("/turtle1/cmd_vel", 10);
	ros::Subscriber sub = node.subscribe("/turtle1/pose",1,&Update::update_pose, &u);
	
	ros::Rate rate(10);
	ROS_INFO("Starting to move forward");


	while (ros::ok())
	{	

		while (flag == 0)
		{											
			ros::Duration(1).sleep();
			
			angle = ret_degree(angle,180);			
			rotate(angle, pub,u);		
			move(LINEAR_SPEED, 0.5, 0 , true, pub,u);
			
			angle = ret_degree(angle,90);			
			rotate(angle, pub,u);	
			move(LINEAR_SPEED, 0.5, 0, true, pub,u);

			angle = ret_degree(angle,90);
			rotate(angle, pub,u);	
			move(LINEAR_SPEED_2,2, 0, true, pub,u);
			
			angle = ret_degree(angle,90);
			rotate(angle, pub,u);	
			move(LINEAR_SPEED,0.5, 0, true, pub,u);

			angle = ret_degree(angle,90);
			rotate(angle, pub,u);	
			move(LINEAR_SPEED,0.5, 0, true, pub, u);
			
			angle = ret_degree(angle,270);
			rotate(angle, pub,u);	
			move(LINEAR_SPEED_2,4, 0, true, pub, u);

			angle = ret_degree(angle,270);
			rotate(angle, pub,u);	
			move(LINEAR_SPEED,0.5, 0, true, pub, u);
			
			angle = ret_degree(angle,90);
			rotate(angle, pub,u);;	
			move(LINEAR_SPEED,0.5, 0, true, pub, u);
			
			angle = ret_degree(angle,90);
			rotate(angle, pub,u);	
			move(LINEAR_SPEED,1.5, 0, true, pub, u);
			
			angle = ret_degree(angle,45);
			rotate(angle, pub,u);	
			move(LINEAR_SPEED_2,2, 0, true, pub, u);

			angle = ret_degree(angle,270);
			rotate(angle, pub,u);
			move(LINEAR_SPEED_2,2, 0, true, pub, u);
			
			angle = ret_degree(angle,45);
			rotate(angle, pub,u);	
			move(LINEAR_SPEED,1.5, 0, true, pub, u);
			
			angle = ret_degree(angle,90);
			rotate(angle, pub,u);	
			move(LINEAR_SPEED, 0.5, 0, true, pub, u);

			angle = ret_degree(angle,90);
			rotate(angle, pub,u);;	
			move(LINEAR_SPEED, 0.5, 0, true, pub, u);
			
			angle = ret_degree(angle,270);
			rotate(angle, pub,u);	
			move(LINEAR_SPEED_2,4, 0, true, pub, u);
			
			angle = ret_degree(angle,270);
			rotate(angle, pub,u);	
			move(LINEAR_SPEED, 0.5, 0, true, pub, u);
			
			angle = ret_degree(angle,90);
			rotate(angle, pub,u);	
			move(LINEAR_SPEED, 0.5, 0, true, pub, u);
			
			angle = ret_degree(angle,90);
			rotate(angle, pub,u);	
			move(LINEAR_SPEED_2,2, 0, true, pub, u);
			
			angle = ret_degree(angle,90);
			rotate(angle, pub,u);	
			move(LINEAR_SPEED,0.5, 0, true, pub, u);
			
			angle = ret_degree(angle,90);
			rotate(angle, pub,u);	
			move(LINEAR_SPEED,0.5, 0, true, pub, u);
				
			angle = ret_degree(angle,270);
			rotate(angle, pub,u);	
			move(LINEAR_SPEED_2,3, 0, true, pub, u);
			
			angle = ret_degree(angle,225);
			rotate(angle, pub,u);	
			move(LINEAR_SPEED_2,2, 0, true, pub, u);

			angle = ret_degree(angle,90);
			rotate(angle, pub,u);	
			move(LINEAR_SPEED_2,2, 0, true, pub, u);
			
			angle = ret_degree(angle,225);
			rotate(angle, pub,u);	
			move(LINEAR_SPEED_2,3, 0, true, pub, u);
				
			
			flag = 1;
	
		
		}
		rate.sleep(); // loop for the rest of the cycle	
	}
	
}
