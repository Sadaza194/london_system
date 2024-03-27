# london_system
CSCI 331

# Instructions 
Unzip the london_system-main.zip in your preferred location.

Once uncompressed do the following:

1. Check if  python 3 is installed by typing in the terminal python  - - version. If not, install it.
2. Then navigate with cd to your preferred location. You can also create the virtual environment within the london_system-main folder.
 to create the virtual environment run: python3 -m venv london_system-main
3. Type: source london_system-main/bin/activate to activate the virtual environment
4. Then install the requirement pip packages: python -m pip install -r requirements.txt
5. Then get into the app folder by typing: cd londonSystem
6. Type: python manage.py runserver. This will start the server.

After following the previous steps you will get a prompt announcing that the server is running. in it you will find the IP address where the server is running:



In this example you get that IP address and complete it with ‘rankings/’. So it ends up like this:

http://127 .0.0.1:8000/rankings/

Copy it and run it in your browser. 

Once there click on the Reload Data button. This will open a Firefox window. Wait until the firefox window closes. This indicates that the data has been updated. 

You will now be able to view, sort and filter the rankings in the web browser