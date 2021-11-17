IMAGE_PATH=images_tmp

cd $IMAGE_PATH

for file in ./*
do
	if test -f $file
	then
		# echo $file
		folder_name=${file:2:1}
		
		if ! test -e $folder_name
		then
			echo 'create folder [' $folder_name ']'
			mkdir $folder_name
		fi

		cp $file $folder_name/$file

		# echo $folder_name
	fi
done
