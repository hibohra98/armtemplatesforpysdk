import os
import subprocess
import json

from flask import Flask, request ,render_template
app = Flask(__name__)
 
@app.route("/")
def hello():
 return render_template('echo.html')
 
@app.route("/echo", methods=['POST'])
 
@app.route("/echo")
def echo():
    alias = request.args.get('text', '')
    ##aa = os.system('az account list')
    ##aa = os.system(f'az ad user show --id {alias}@microsoft.com')
    #alias=input("Input you alias:")
    users = subprocess.check_output(f'az ad user show --id {alias}@microsoft.com',shell=True)
    my_json = users.decode('utf8').replace("'", '"')
    users_obj = json.loads(my_json)
    print(users_obj.get("objectId"),users_obj.get("jobTitle"),users_obj.get("department"), users_obj.get("city"),users_obj.get("extension_18e31482d3fb4a8ea958aa96b662f508_ReportsToEmailName"))
    var = users_obj.get("objectId"),users_obj.get("jobTitle"),users_obj.get("department"), users_obj.get("city"),users_obj.get("extension_18e31482d3fb4a8ea958aa96b662f508_ReportsToEmailName") 
    return render_template('echo.html', var);

if __name__ == "__main__":
    app.run()
