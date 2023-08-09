from flask_restx import Resource
from flask_apispec import doc,marshal_with
from flask_apispec.views import MethodResource
from app import API, SQL_DB
from app.models.project_user import DataStore, DataSchema




@API.route("/manipule/<int:data_id>")
class DataCrud(MethodResource, Resource):
    
    @doc(description="Get data", tags=["Datas Manipule"])
    @marshal_with(DataSchema)
    def get(self, data_id):
        return SQL_DB.get_or_404(DataStore, data_id)
    def save(self):

        # inject self into db session    
        SQL_DB.session.add ( self )

        # commit change and save the object
        SQL_DB.session.commit( )

        return self