from flask import jsonify
from flask_restful import Resource, reqparse
from GovOpendata.apps.service.GovernmentSrv import GovernmentSrv


class GovernmentCtrl(Resource):
    def get(self)-> object:
        res = GovernmentSrv.statistics()
        return jsonify(res)

    def post(self)->object:
        parser = reqparse.RequestParser()
        parser.add_argument('province', required=True, type=str)
        parser.add_argument('region', required=True, type=str)
        parser.add_argument('dir_path', required=True, type=str)
        parser.add_argument('file_num', required=True, type=int)
        parser.add_argument('file_size', required=True, type=int)
        parser.add_argument('dataset_num', required=True, type=int)
        parser.add_argument('acquire_date', required=True, type=str)
        args = parser.parse_args(strict=True)
        res = GovernmentSrv.add(
            province=args.get("province"),
            region=args.get("region"),
            dir_path=args.get("dir_path"),
            file_num=args.get("file_num"),
            file_size=args.get("file_size"),
            dataset_num=args.get("dataset_num"),
            acquire_date=args.get("acquire_date")
        )
        return jsonify(res)
