from flask import Flask, jsonify, request, Response
from pymongo import MongoClient
from bson.objectid import ObjectId
from datetime import datetime
import json

app = Flask(__name__)

client = MongoClient("mongodb://localhost:27017/")
db = client["AIHack_Solutions"]

collections = {
    "consultas": db.consultas,
    "exames": db.exames,
    "farmacias": db.farmacias,
    "medicamentos": db.medicamentos,
    "medicos": db.medicos,
    "pacientes": db.pacientes,
    "postossaude": db.postossaude,
    "prescricao": db.prescricao,
    "procedimentos": db.procedimentos,
    "transacoesfinanceiras": db.transacoesfinanceiras
}

def serialize_doc(doc):
    if isinstance(doc, dict):
        return {key: serialize_doc(value) for key, value in doc.items()}
    elif isinstance(doc, list):
        return [serialize_doc(item) for item in doc]
    elif isinstance(doc, ObjectId):
        return str(doc)
    elif isinstance(doc, datetime):
        return doc.isoformat()
    else:
        return doc

@app.route('/<collection_name>', methods=['POST'])
def create_document(collection_name):
    data = request.json
    if collection_name in collections:
        collection = collections[collection_name]
        result = collection.insert_one(data)
        return jsonify({"_id": str(result.inserted_id)}), 201
    else:
        return jsonify({"error": "Collection not found"}), 404

@app.route('/<collection_name>', methods=['GET'])
def get_all_documents(collection_name):
    if collection_name in collections:
        collection = collections[collection_name]
        documents = [serialize_doc(doc) for doc in collection.find()]
        return jsonify(documents)
    else:
        return jsonify({"error": "Collection not found"}), 404

@app.route('/<collection_name>/<doc_id>', methods=['GET'])
def get_document(collection_name, doc_id):
    if collection_name in collections:
        collection = collections[collection_name]
        try:
            clean_doc_id = doc_id.strip()
            document = collection.find_one({"_id": ObjectId(clean_doc_id)})
            if document:
                return jsonify(serialize_doc(document)), 200
            else:
                return jsonify({"error": "Document not found"}), 404
        except (TypeError):
            return jsonify({"error": "Invalid ID format"}), 400
    else:
        return jsonify({"error": "Collection not found"}), 404

@app.route('/<collection_name>/<doc_id>', methods=['PUT'])
def update_document(collection_name, doc_id):
    data = request.json
    if collection_name in collections:
        collection = collections[collection_name]
        try:
            result = collection.update_one({"_id": ObjectId(doc_id)}, {"$set": data})
            if result.modified_count > 0:
                return jsonify({"message": "Document updated successfully"}), 200
            else:
                return jsonify({"error": "Document not found or no change in data"}), 404
        except:
            return jsonify({"error": "Invalid ID format"}), 400
    else:
        return jsonify({"error": "Collection not found"}), 404

@app.route('/<collection_name>/<doc_id>', methods=['DELETE'])
def delete_document(collection_name, doc_id):
    if collection_name in collections:
        collection = collections[collection_name]
        try:
            result = collection.delete_one({"_id": ObjectId(doc_id)})
            if result.deleted_count > 0:
                return jsonify({"message": "Document deleted successfully"}), 200
            else:
                return jsonify({"error": "Document not found"}), 404
        except:
            return jsonify({"error": "Invalid ID format"}), 400
    else:
        return jsonify({"error": "Collection not found"}), 404

@app.route('/export/<collection_name>', methods=['GET'])
def export_collection(collection_name):
    if collection_name in collections:
        collection = collections[collection_name]
        documents = [serialize_doc(doc) for doc in collection.find()]
        return Response(json.dumps(documents), mimetype='application/json',
                        headers={"Content-Disposition": f"attachment;filename={collection_name}.json"})
    else:
        return jsonify({"error": "Collection not found"}), 404

@app.route('/export_all', methods=['GET'])
def export_all_collections():
    all_data = {}
    for collection_name, collection in collections.items():
        documents = [serialize_doc(doc) for doc in collection.find()]
        all_data[collection_name] = documents  # Adiciona cada coleção ao JSON principal
    
    return Response(json.dumps(all_data), mimetype='application/json',
                    headers={"Content-Disposition": "attachment;filename=all_collections.json"})


if __name__ == '__main__':
    app.run(debug=True)