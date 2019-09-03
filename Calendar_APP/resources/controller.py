from flask_restful import Resource
from Model import db, Events, EventsSchema
from flask import request
from datetime import date
from flask import jsonify
from flask_restful import Resource


events_schema = EventsSchema(many=True)
event_schema = EventsSchema()


class GetEvents(Resource):
    def get(self):
        events = Events.query.all()
        return {"events": events}

    def post(self):
        try:
            json_data = request.get_json(silent=True)
            try:
                start_date = json_data['start_date']
                end_date = json_data['end_date']
                if ((start_date == '') or (end_date == '')):
                    return {"message": 'Please provide dates values'}
            except Exception as e:
                return {"message": 'start_date and end_date is required'}
            start_date_list = start_date.split('-')
            end_date_list = end_date.split('-')
            start = date(year=int(start_date_list[0]),month=int(start_date_list[1]),day=int(start_date_list[2]))
            end = date(year=int(end_date_list[0]),month=int(end_date_list[1]),day=int(end_date_list[2]))
            if start_date <= end_date:
                events = Events.query.filter(Events.start_date <= end).filter(Events.start_date >= start).order_by(Events.start_date.asc()).all()
                events_data = events_schema.dump(events).data
                return {'status': 'success', 'count':len(events), 'result': events_data}, 200
            else:
                return {"message": 'start date must be less than end date'}
        except Exception as e:
            return {"message": e}