from flask import Blueprint, jsonify, request
import logging
from services.service_tfm import ServiceTFM
router = Blueprint('service_tfm_router', __name__, url_prefix='/service')


@router.get('/getDocuments/<id>')
def service_get(id: int):
    logging.info(f"Comenzando servicio apra obtener los documentos, request {request}")

    service = ServiceTFM()

    results, status = service.getDocuments(id)
    
    logging.info(f"Finalizando servicio para obtener los documentos request {request}")

    # Return response.
    return jsonify(results), status