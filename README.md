# veepee_scrapper

### This code is deployed on our ec2 instance : test-server1 under the folder /bm_rebuy

### to access in ssh mode : navigate to the folder when you put the "test-server1.pem" file then :

          ssh -i "test-server1.pem" ubuntu@ec2-35-180-131-203.eu-west-3.compute.amazonaws.com

### think to activate the python envirement : 
          source venManel/bin/activate
### access to the folder :
          cd bm_rebuy 

### both code files :  final.py and run_bm_rebuy.py are running on background 
      
          gunicorn --bind 0.0.0.0:8080 --workers 4 --timeout 36000 final:app
          
          nohup python run_bm_rebuy.py > output.log 2>&1 &

### the api is related with google sheet "rebuy_price" : 

        https://docs.google.com/spreadsheets/d/1m5MhvTdHXed2pU0m83eI6hD4rLm27CxIh0i126qlcrI/edit?pli=1#gid=1539464549

### the script function "rebuy_bm ()" that is running each morning before 7 AM using google apss trigger get :
        the last "final_result.json" available on the server

### the result of this script is on sheet : "BackMarket_rebuy_prices"

