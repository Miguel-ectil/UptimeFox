from flask import Blueprint, request, jsonify
from app.extensions import db
from app.models.site import Site

bp = Blueprint('site_routes', __name__)

@bp.route('/sites', methods=['POST'])
def add_site():
    data = request.get_json()
    url = data.get('url')

    if not url:
        return jsonify({'error': 'URL obrigatória'}), 400

    if Site.query.filter_by(url=url).first():
        return jsonify({'error': 'Site já cadastrado'}), 409

    site = Site(url=url)
    db.session.add(site)
    db.session.commit()

    return jsonify({'message': 'Site cadastrado com sucesso'}), 201

@bp.route('/sites', methods=['GET'])
def list_sites():
    sites = Site.query.all()
    return jsonify([{'id': s.id, 'url': s.url} for s in sites])
