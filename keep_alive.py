import time
import os
from datetime import datetime

while True:
    print(f"Keep alive at {datetime.now()}")
    os.system('python rolex.py')  # This will run the `rolex.py` script itself
    time.sleep(300)  # Sleep for 5 minutes
