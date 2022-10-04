from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash

class Sighting:
    db_name = "sasquatch"
    def __init__(self,db_data):
        self.id = db_data['id']
        self.location = db_data['location']
        self.date_made = db_data['date_made']
        self.description = db_data['description'] 
        self.sasquatches_seen = db_data['sasquatches_seen']
        self.user_id = db_data['user_id']
        self.created_at = db_data['created_at']
        self.updated_at = db_data['updated_at']

    @classmethod
    def create_sighting(cls, data):
        query = "INSERT INTO sightings (location, date_made, description, sasquatches_seen, user_id) VALUES (%(location)s, %(date_made)s, %(description)s, %(sasquatches_seen)s, %(user_id)s);"
        return connectToMySQL(cls.db_name).query_db(query, data)

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM sightings;"
        results = connectToMySQL(cls.db_name).query_db(query)
        all_sightings = []
        for row in results:
            print(row['date_made'])
            all_sightings.append( cls(row) )
        return all_sightings

    @classmethod
    def get_one(cls, data,):
        qeury = "SELECT * FROM sightings WHERE id = %(id)s;"
        results = connectToMySQL(cls.db_name).query_db(data, query)
        return cls( results[0] )

    @classmethod
    def update(cls, data):
        query = "UPDATE sightings SET location=%(location)s, date_made=%(date_made)s, description=%(description)s, sasquatches_seen=%(sasquatches_seen)s, updated_at=NOW() WHERE id = %(id)s;"
        return connectToMySQL(cls.db_name).query_db(query, data)

    @classmethod
    def destroy(cls, data):
        query = "DELETE FROM sightings WHERE id = %(id)s;"
        return connectToMySQL(cls.db_name).query_db(query, data)

    @staticmethod
    def validate_sighting(sighting):
        is_valid = True
        if len(sighting['location']) <= 0:
            is_valid = False
            flash('Location must be filled out','sighting')
        if sighting['date_made'] == "":
            is_valid = False
            flash('Date must be entered', 'sighting')
        if len(sighting['description']) <= 0:
            is_valid = False
            flash('Description must be filled out','sighting')
        if int(sighting['sasquatches_seen']) < 1:
            is_valid = False
            flash('Must have seen at least 1 Sasquatch', 'sighting')
        return is_valid
