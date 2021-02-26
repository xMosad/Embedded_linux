#!/bin/bash
. ./func.sh
number=0
###Entery point 
echo hi 
i=1

#var=$( cat text | grep ali )
#echo $var
#var1=$(echo $var | cut -f2 -d:)
#echo $var1
while [ 1 ]
do
        print_mainScreen 
		read -p "please enter a number : " number
		echo 
		echo
		if [ $number == 1 ]
		then
			list_users
		elif [ $number == 2 ]
		then
			add_user
		elif [ $number == 3 ]
		then
			search_user
		elif [ $number == 4 ]
		then
			edit_user	
		elif [ $number == 5 ]
		then
			remove_user
		elif [ $number == q ]
		then
			break		
		fi
		echo 
		echo
		echo
done
echo Bye
echo 