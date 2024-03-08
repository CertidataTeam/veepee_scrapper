# veepee_scrapper

### This code is deployed on our ec2 instance : test-server1 under the folder /veppee_scrapper

### to access in ssh mode : navigate to the folder when you put the "test-server1.pem" file then :

          ssh -i "test-server1.pem" ubuntu@ec2-35-180-131-203.eu-west-3.compute.amazonaws.com

### think to activate the python envirement : 
          source venManel/bin/activate
### access to the folder :
          cd veppee_scrapper 

### both code files :  app.py and veepee_scraping_script.py are running on background 
      
          gunicorn --bind 0.0.0.0:8080 --workers 4 --timeout 36000 app:app
          
          nohup python veepee_scraping_script.py > output.log 2>&1 &

### the api is related with google sheet "OD_APPLE448-prix V2_dRAFT" : 

        https://docs.google.com/spreadsheets/d/16TVOI2gjTtaFmiiARsfHcj_VLzLSGWsMZuAue33JC48/edit#gid=313227002

### the script function "veepee_scrapper ()" that is running each morning before 7 AM using google apss trigger get :
        the last "veepee_prices.json" available on the server

### the result of this script is on sheet : "Prix VP"

