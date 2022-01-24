import os
cmds = '''
set -e
printf "\n\n------// \033[1;33mSelect One: \n
	1) Heroku login?
	2) Already Logged in !
	=> "

read log

if [ $log -eq 1 ]; then
	heroku login
else [ $log -eq 2 ];
	printf "\n\n------// \033[1;33mSelect One: \n
		1) New Bot
		2) Existing Bot
		3) Delete a project !
		=> "
	read sel
fi

printf " \033[1;33m=========================================================


			\033[0;32mEnter Your appname !\033[1;33m


===================\033[0;35m-^ MeEk_0 ^-\033[1;33m=========================== \n \n \033[0;32m" 

read appname		# all 3 options need a name, so i'm not putting it in statements

if [ $sel -eq 1 ]; then
	heroku create $appname				# for new bot
	heroku git:remote -a $appname

elif [ $sel -eq 2 ]; then
	heroku git:remote -a $appname		# for Existing bot

elif [ $sel -eq 1 ] && [ $sel -eq 2 ]; then
	heroku stack:set container
	heroku addons:create heroku-postgresql:hobby-dev
	printf "\n\n\n"
	heroku config:get DATABASE_URL -a $appname
	printf "\n\n \033[1;33mCopy the avobe DATABASE_URL and paste it into  --  DB_URL  -- function and then press enter !\n\n\033[0;32m"
	read enter
	`echo heroku config:get DATABASE_URL -a $appname` | python3 create_table.py
	heroku git:remote -a $appname
	rm -rf .git
	git init
	git add .
	git commit -am "make it better"
	git push heroku master --force
	printf "\n\n------// \033[1;33mSelect Dyno to scale: \n
		1) worker
		2) web
		3) worker & web
		=> "
	read dyno
	if [ $dyno -eq 1 ]; then
		heroku ps:scale worker=1

	elif [ $dyno -eq 2 ]; then
		heroku ps:scale web=1
	else [ $dyno -eq 3 ]
		heroku ps:scale worker=1
		heroku ps:scale web=1
	fi

else [ $sel -eq 3 ]
 	heroku apps:destroy $appname
fi
printf " Done! "
'''
os.system(cmds)
