from flask import Flask, request
import management
from management import all_sparta_dict
from spartan import Spartan


flask_object = Flask(__name__)

# GET for homepage
@flask_object.route("/", methods = ["GET"])
def home_page():
    return "Welcome to the home page, API allow application to interact with external data resources"


# POST for add spartan
@flask_object.route("/spartan/add", methods = ["POST"])

def spartan_add():
    management.load_from_json()
    spartan_file = request.json
    spartan_id = spartan_file["spartan_id"]
    first_name = spartan_file["first_name"]
    last_name = spartan_file["last_name"]
    birth_day = spartan_file["birth_day"]
    birth_month = spartan_file["birth_month"]
    birth_year = spartan_file["birth_year"]
    course = spartan_file["course"]
    stream = spartan_file["stream"]

    spartan_object = Spartan(spartan_id, first_name, last_name, birth_day, birth_month, birth_year, course, stream)

    spartan_object.print_spartan_data()

    all_sparta_dict[spartan_id] = spartan_object

    management.save_to_json()

    return f"The Spartan, {first_name} {last_name}, with Spartan ID: {spartan_id} will be added to the database."



# GET for to view certain spartan
@flask_object.route("/spartan/<spartan_id>", methods = ["GET"])
def spartan_file_getter(spartan_id):
    management.load_from_json()
    print(all_sparta_dict)
    if int(spartan_id) in all_sparta_dict.keys():
        spartan_object = all_sparta_dict[int(spartan_id)]
        return spartan_object.__dict__
    else:
        print("WARNING: Spartan ID entered does not exist in the system")


# POST to remove spartan
@flask_object.route("/spartan/remove", methods = ["POST"])
def spartan_file_remover():
    management.load_from_json()
    spartan_id = request.args.get("id")
    if int(spartan_id) in all_sparta_dict.keys():
        del all_sparta_dict[int(spartan_id)]
        print(all_sparta_dict)
        management.save_to_json()
        return f"The Spartan, with Spartan ID: {spartan_id}, has been successfully removed from the system"
    else:
        print("WARNING: Spartan ID entered does not exist in the system")

# GET to view spartan list
@flask_object.route("/spartan", methods = ["GET"])
def all_spartan_file_getter():
    management.load_from_json()
    temp_dict_of_dict = {}

    for spartan_id in all_sparta_dict:
        spartan_obj = all_sparta_dict[spartan_id]
        spartan_dict = spartan_obj.__dict__
        temp_dict_of_dict[spartan_id] = spartan_dict
    return temp_dict_of_dict

if __name__ == "__main__":

    flask_object.run()
