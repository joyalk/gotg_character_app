from flask import Blueprint
from controllers.characters_controller import index, new, create, edit, update, delete, comments, add_comment, display_comments

characters_routes = Blueprint('characters_routes', __name__)

characters_routes.route('')(index)
characters_routes.route('/new')(new)
characters_routes.route('', methods=['POST'])(create)
characters_routes.route('/<id>/edit')(edit)
characters_routes.route('/<id>', methods=['POST'])(update)
characters_routes.route('/<id>/delete', methods=['POST'])(delete)
characters_routes.route('/<id>/comment')(comments)
characters_routes.route('comment')(display_comments)
characters_routes.route('/<id>/comment', methods=['POST'])(add_comment)

