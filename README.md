# GUI_Drive_Me
A project for workers who drive to work in pairs
<img src="https://user-images.githubusercontent.com/109242797/180848837-3e412c0d-0c18-4237-9c24-3f781efcacf1.png" alt='not found' title='Program View'>

# Definition of using
Program could be used by users who split by cars during driving to work. Each user has 2 cars and they should take turns in driving.

First of all user has to pick a date in a calendar view 


<img src="https://user-images.githubusercontent.com/109242797/180849055-44cbb327-01d0-49a2-9712-e32bd24d8a2e.png" alt='not found' title='Calendar View'>

By 'GET THIS DATE INFO' the data is beeing selected from connected sqlite3 according to day choosen in calendar.
Data about cars for each user is beeing shown below the Button.

After picking a day user can update a cars on the right side of program
<img src="https://user-images.githubusercontent.com/109242797/180849553-0893f35f-b842-4798-adb9-67e7902bc261.png" alt='not found' title='Cars View'>

This view is separated for each user.
Individual cars are assigned to the appropriate persons - in this case first two are for Pioter User, 3rd and 4th are for Karol User.
If users pick the same car it means they drove work together. Program checks whos car they came in and count +1 ride for this user.
In this case any user can clik "Who Drive NEXT?" Button and see the satitistics about rides and get simple information whose turn is driving.

![Screenshot from 2022-07-25 20-39-45](https://user-images.githubusercontent.com/109242797/180850337-c4edea25-3952-4027-a6e4-45a9d0ccea65.png)
