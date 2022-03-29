# Store

SETUP: 
  shell:
  
    * python3 -m venv ./venv
    * source ./venv/bin/activate
    * pip3 install -r requiremnets.txt
    
    * flask init db
    * flask migrate
    * flask upgrade
   
  
  
RUN:
  * python3 run.py
