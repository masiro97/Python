#pragma config(Sensor, S1,     ultra,          sensorSONAR)
#pragma config(Sensor, S2,     color,          sensorColorNxtFULL)
#pragma config(Sensor, S3,     touch_100,      sensorTouch)
//*!!Code automatically generated by 'ROBOTC' configuration wizard               !!*//

#define distance_m 150   // money distance
#define DIAMETER 55
#define distance_100 38//24


float convert(float dis){

	float angle;
	angle = (360*dis/DIAMETER/PI);
	return angle;

}

task main()
{
	int rotation;
	int count =0;
	int param = 0;
	int count_10000 =0;
	int count_5000=0;
	int count_1000=0;
	int total_coin_100 = 0;
	int coin_100_distance = 0;
	int i = 0;


	while(1){
			count =0;
			param = 0;
			i=0;

			coin_100_distance = (int) convert((float)distance_100 * total_coin_100);

			total_coin_100 = count_10000 * 100 + count_5000 * 50 + count_1000 * 10;




			if(SensorValue(ultra) < 10){


			motor[motorA] = 40;
			motor[motorC] = 40;
			wait1Msec(3000);

			}

			else{
				motor[motorA] = 0;
				motor[motorC] = 0;
}
			if(SensorValue(color) == GREENCOLOR){
				param = 3;
				count = 3;
				sendMessageWithParm(count);
				while(SensorValue(color) == GREENCOLOR){}

			}

			else if(SensorValue(color) == BLUECOLOR){
				param = 1;
				count = 1;
				sendMessageWithParm(count);
				while(SensorValue(color) == BLUECOLOR){}

			}

			else if(SensorValue(color) == YELLOWCOLOR){
				param =2;
				count = 2
				sendMessageWithParm(count);
				while(SensorValue(color) == YELLOWCOLOR){}


				}
				if(param ==3){
					count_10000++;
				}
				if(param ==2){
					count_5000++;
				}
				if(param ==1){
					count_1000++
				}


			if(SensorValue(touch_100) == 1){


				nMotorEncoder[motorB] = 0;
				while(nMotorEncoder[motorB] >-coin_100_distance){
				nMotorEncoderTarget[motorB] =-coin_100_distance;
				motor[motorB] = -70;

				}

					motor[motorB] = 0;

				count_1000 =0;
				count_5000 = 0;
				count_10000 = 0;

			}

			nxtDisplayTextLine(2,"total_100 = %d",total_coin_100);


	if(total_coin_100>0)
	{

		clearTimer(T1);

		if(time1[T1]<5000)
		{
			i++;

			while(time1[T1]<10000)
			{

				if(SensorValue(touch_100)==1)
				{
					i=0;
					break;

				}

			}

		}

	}
			if(i==1)
			{
				count_1000 = 0;
				count_5000 = 0;
				count_10000 = 0;
			}


				nxtDisplayTextLine(3,"%d",SensorValue(touch_100));
				nxtDisplayTextLine(4,"ultra = %d",SensorValue(ultra));
				nxtDisplayTextLine(5,"color = %d",SensorValue(color));
				wait1Msec(200);

	}


	}
