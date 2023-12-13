"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
import os
from flask import Flask, request, jsonify, url_for
from flask_cors import CORS
from utils import APIException, generate_sitemap
from datastructures import FamilyStructure #we need to import the data structure from the other file we have
#from models import Person

app = Flask(__name__)
app.url_map.strict_slashes = False
CORS(app)

# here we create the jackson family object, which will use the FamilyStructure class we created in datastructure.py file, and we pass it the last name Jackson as an argument
jackson_family = FamilyStructure("Jackson")

last_name = "Jackson"
# Handle/serialize errors like a JSON object
@app.errorhandler(APIException)
def handle_invalid_usage(error):
    return jsonify(error.to_dict()), error.status_code


# generate sitemap with all your endpoints
@app.route('/')
def sitemap():
    return generate_sitemap(app)

#### GET ####
@app.route('/members', methods=['GET'])
def get_members():
    # this is how you can use the Family datastructure by calling its methods
    members = jackson_family.get_all_members()  # this is the method for returning a list with all the family members
    response_body = {
        "results": members # we defined the attribute members in datastructure.py file as an empty array so this is exactly what I would see in Postman. To see members in the list, we need to use the method POST
    }
    return jsonify(response_body), 200   # jsonify transforms our python code into JSON so our front can receive it. We can receive 2 parameters in our return, so we also receive the success code 200 (ok)

#### POST ####
@app.route('/members', methods=['POST'])
def handle_add_members():
    new_family_member = request.json # As we want to add 3 family members, then is best to send the request from Postman, writing the the dictionary (as the one below for kate) in the body, and receive that request here as json. We create for 1 member and post, another member and post, and so on.

    #kate = {                    # initially as test we create the dictionary with the family member kate. We test in Postman and we see the same.
        #"first_name": "Kate",
        #"last_name": last_name,
        #"age": 35,
        #"lucky_numbers": [5, 7, 11],}
    
    members = jackson_family.add_member(new_family_member) # this is the method for adding a new family member to the list. 
    response_body = {
        "results": members
    }
    return jsonify(response_body), 200

#### GET 1 ####
@app.route('/members/<int:member_id>', methods=['GET'])
def get_specific_member(member_id): #whatever we put as id after the endpoint we need to also pass it as a parameter here
    single_member = jackson_family.get_member(member_id) # this is the method for getting a particular family member from the list. 
    if single_member:
        response_body = {"message": "family member found",
                        "results": single_member }
        return jsonify(response_body), 200
    response_body = {"message": "family member not found",
                            "results": [] }
    return jsonify(response_body), 404
    
#### DELETE ####
@app.route('/members/<int:member_id>', methods=['DELETE'])
def handle_delete_member(member_id):   #whatever we put as id after the endpoint we need to also pass it as a parameter here   
    deleted_member = jackson_family.delete_member(member_id) # this is the method for deleting a family member from the list. 
    if deleted_member:
        response_body = {"message": "family member deleted",
                        "results": deleted_member }
        return jsonify(response_body), 200
    response_body = {"message": "family member not found",
                    }
    return jsonify(response_body), 404

    
#### PUT ####
@app.route('/members/<int:member_id>', methods=['PUT'])
def handle_update_member(member_id):   #whatever we put as id after the endpoint we need to also pass it as a parameter here   
      # Get the updated member data from the request body
    updated_member_data = request.json
    updated_member = jackson_family.update_member(member_id, updated_member_data) # this is the method for updating a family member from the list. 
    if updated_member:
        response_body = {"message": "family member updated",
                        "results": updated_member }
        return jsonify(response_body), 200
    response_body = {"message": "family member not found",
                    }
    return jsonify(response_body), 404
# REMEMBER: When sending a PUT request with JSON data, make sure to set the in Postman headers the "Content-Type" (key) as "application/json" (value)!


# this only runs if `$ python src/app.py` is executed
if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=PORT, debug=True)
