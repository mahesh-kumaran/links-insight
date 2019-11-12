from flask import Flask, jsonify, request
from link_insight.common.exceptions import *
from link_insight.parser import parse_link_information
from pprint import pprint


app = Flask(__name__)


@app.route('/link_insight', methods=['GET'])
def link_insight() :
    link_response = {}
    if request.args.get('link') == None:
        bad_request(400, "missing_argument_link")
    else:
        link = request.args.get('link').strip()
        link_response['for_url'] = link
        link_response['response']  = parse_link_information(link) 
        return jsonify(link_response)
