from . import errors_bp


@errors_bp.route('/raise_exception')
def raise_exception():
    raise Exception('Something went wrong!')
