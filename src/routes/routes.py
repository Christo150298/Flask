from flask import Blueprint, jsonify, request
from database.database import db
from controlers.get_todos import get_todos
from controlers.create_todos import create_todo

api = Blueprint("api", __name__)

@api.route('/todos', methods=['GET'])
def todos():
    if request.method == 'GET':
        return jsonify(get_todos())
    elif request.method == 'POST':
        return response_body
    return jsonify(get_todos())
