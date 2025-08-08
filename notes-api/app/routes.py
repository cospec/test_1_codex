
from flask import Blueprint, request, jsonify, current_app
from sqlalchemy import select
from .models import db, Note

bp = Blueprint("notes", __name__)

def _pagination_params():
    try:
        page = int(request.args.get("page", "1"))
        per_page = int(request.args.get("per_page", str(current_app.config["PAGE_SIZE_DEFAULT"])))
    except ValueError:
        return 1, current_app.config["PAGE_SIZE_DEFAULT"]
    per_page = max(1, min(per_page, current_app.config["PAGE_SIZE_MAX"]))
    return max(1, page), per_page

@bp.route("/notes", methods=["POST"])
def create_note():
    payload = request.get_json(silent=True) or {}
    title = (payload.get("title") or "").strip()
    content = (payload.get("content") or "").strip()
    if not title or not content:
        return jsonify({"error": "title and content are required"}), 400
    note = Note(title=title, content=content)
    db.session.add(note)
    db.session.commit()
    return jsonify(note.to_dict()), 201

@bp.route("/notes", methods=["GET"])
def list_notes():
    q = (request.args.get("q") or "").strip()
    page, per_page = _pagination_params()

    query = select(Note)
    if q:
        like = f"%{q}%"
        query = query.filter((Note.title.ilike(like)) | (Note.content.ilike(like)))

    pagination = db.paginate(query, page=page, per_page=per_page, error_out=False)
    return jsonify({
        "items": [n.to_dict() for n in pagination.items],
        "page": pagination.page,
        "pages": pagination.pages,
        "per_page": pagination.per_page,
        "total": pagination.total,
    }), 200

@bp.route("/notes/<int:note_id>", methods=["GET"])
def get_note(note_id: int):
    note = db.get_or_404(Note, note_id)
    return jsonify(note.to_dict()), 200

@bp.route("/notes/<int:note_id>", methods=["PUT"])
def update_note(note_id: int):
    note = db.get_or_404(Note, note_id)
    payload = request.get_json(silent=True) or {}
    title = payload.get("title")
    content = payload.get("content")

    if title is not None:
        title = title.strip()
        if not title:
            return jsonify({"error": "title cannot be empty"}), 400
        note.title = title
    if content is not None:
        content = content.strip()
        if not content:
            return jsonify({"error": "content cannot be empty"}), 400
        note.content = content

    db.session.commit()
    return jsonify(note.to_dict()), 200

@bp.route("/notes/<int:note_id>", methods=["DELETE"])
def delete_note(note_id: int):
    note = db.get_or_404(Note, note_id)
    db.session.delete(note)
    db.session.commit()
    return jsonify({"deleted": note_id}), 200
