import json, logging
from flask import Flask, jsonify
import firebase_admin
from firebase_admin import credentials, firestore

class ServiceTFM():
    cred = None
    db = None

    def __init__(self):
        # Inicializa la aplicación Firebase con las credenciales del archivo JSON
        if not firebase_admin._apps:
            self.cred = credentials.Certificate('/configuration/serviceAccountKey.json')
            firebase_admin.initialize_app(self.cred)

        self.db = firestore.client()

    def getDocuments(self, id_edificio):
        try:
            docs = self.db.collection('elementos').where('id_edificio', '==', str(id_edificio)).stream()
            results = [{doc.id: doc.to_dict()} for doc in docs]
            status = 200 if len(results) != 0 else 404
            return results, status
        except Exception as e:
            logging.error(f"Ha ocurrido una excepción no controlada {e}")

            return [], 500
        
