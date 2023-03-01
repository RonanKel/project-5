"""
Replacement for RUSA ACP brevet time calculator
(see https://rusa.org/octime_acp.html)

"""



import flask
from flask import request
from flask import jsonify
import arrow  # Replacement for datetime, based on moment.js
import acp_times  # Brevet time calculations
import config
from mypymongo import brevet_insert, brevet_find

import logging

###
# Globals
###
app = flask.Flask(__name__)
CONFIG = config.configuration()




###
# Pages
###


@app.route("/")
@app.route("/index")
def index():
    app.logger.debug("Main page entry")
    return flask.render_template('calc.html')


@app.errorhandler(404)
def page_not_found(error):
    app.logger.debug("Page not found")
    return flask.render_template('404.html'), 404


###############
#
# AJAX request handlers
#   These return JSON, rather than rendering pages.
#
###############
@app.route("/_calc_time")
def _calc_times():

    """
    Calculates open/close times from miles, using rules
    described at https://rusa.org/octime_alg.html.
    Expects one URL-encoded argument, the number of miles.
    """
    app.logger.debug("Got a JSON request")
    km = request.args.get('km', 999, type=float)
    distance = request.args.get("distance", 999, type=float)
    begin_date = request.args.get("begin_date", type=str)

    begin_date_arrow = arrow.get(begin_date, "YYYY-MM-DDTHH:mm")

    # app.logger.debug("dist_int = {}".format(distance_int))
    # app.logger.debug("begin_date_arrow = {}".format(begin_date_arrow))


    app.logger.debug("km={}".format(km))
    app.logger.debug("request.args: {}".format(request.args))
    # FIXME!
    # Right now, only the current time is passed as the start time
    # and control distance is fixed to 200
    # You should get these from the webpage!
    open_time = acp_times.open_time(km, distance, begin_date_arrow).format('YYYY-MM-DDTHH:mm')
    close_time = acp_times.close_time(km, distance, begin_date_arrow).format('YYYY-MM-DDTHH:mm')
    result = {"open": open_time, "close": close_time}
    return flask.jsonify(result=result)


#############

@app.route("/_insert_brevet", methods=["POST"])
def _insert():

    try:
        app.logger.debug("Got a JSON find request")

        input_json = request.json

        begin_date = input_json["begin_date"]
        distance = input_json["distance"]
        checkpoints = input_json["checkpoints"]

        if len(checkpoints) == 0:
            return flask.jsonify({"error": "Unable to insert an empty list"})

        app.logger.debug(checkpoints)

        brevet_insert(begin_date, distance, checkpoints);

        return flask.jsonify(result = {}, message = "Success!", status = 1)

    except:
        return flask.jsonify(result = {}, message = "Server Error!", status = 0)




@app.route("/_find_brevet")
def _find():

    try:
        app.logger.debug("Got a JSON find request")
        result = brevet_find()
        app.logger.debug(result)
        return flask.jsonify(result=result, message="Success!", status=1)

    except:
        return flask.jsonify(result={}, message="Server Error!", status=0)



app.debug = CONFIG.DEBUG
if app.debug:
    app.logger.setLevel(logging.DEBUG)

if __name__ == "__main__":
    print("Opening for global access on port {}".format(CONFIG.PORT))
    app.run(port=CONFIG.PORT, host="0.0.0.0")
