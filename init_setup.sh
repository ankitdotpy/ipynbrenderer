echo [$(date)]: "START"
python3 -m venv venv
source venv/bin/activate
pip install -r requirements_dev.txt
echo [$(date)]: "FINISH"