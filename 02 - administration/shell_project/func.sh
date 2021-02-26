STD_MSG="About to do some operations"

address_file=~/.addressbock 
# This functions will list all the users and takes no parameters
print_mainScreen()
{
	echo "####################"
	echo " -- Address Book -- "
	echo "1- list all users "
	echo "2- add user "
	echo "3- Search for user "
	echo "4- Edit user "
	echo "5- Remove user "
	echo "q- Quit "	
	echo "####################"
}
list_users()
{
	echo '####### list #########'
	while read p; do
		name=$(echo $p | cut -f1 -d:)
		number=$(echo $p | cut -f2 -d:)
		mail=$(echo $p | cut -f3 -d:)
		echo "$name   $number   $mail"
	done <$address_file
	echo '####################'
}
# This function will search for user 
search_user()
{
	read -p "please enter the name : " name
	var=$( cat $address_file | grep $name )
	#match=$(cat $address_file | grep -c $name )
	
	if [ ! -z "$var" ]
	then
		number=$(echo $var | cut -f2 -d:)
		mail=$(echo $var | cut -f3 -d:)
		echo "$name   $number   $mail"
	else 
		echo "Not found"
	fi
}
add_user()
{
	read -p "Please enter the name : " name
	read -p "Please enter the number : " number
	read -p "Please enter the name : " mail
	echo "$name : $number : $mail" >>$address_file
	echo "done"
}
edit_user()
{
	read -p "Please enter the name : " name 
	var=$( cat $address_file | grep $name )
	if [ ! -z "$var" ]
	then
		number=$(echo $var | cut -f2 -d:)
		mail=$(echo $var | cut -f3 -d:)
		read -p "Name [ $name ] : " name
		read -p "Name [ $number ] : " number
		read -p "Name [ $mail ] : " mail
		newvar="$name : $number : $mail"
		sed -i "s/${var}/${newvar}/" $address_file
	else 
		echo "Not found"
	fi

}
remove_user()
{
	read -p "Please enter the name : " name 
	var=$( cat $address_file | grep $name )
	if [ ! -z "$var" ]
	then
		echo var
		sed -i "/${var}/d" $address_file
		echo Done 
	else 
		echo "Not found"
	fi
}
