

def form_response(msg: str, code: int = 200, data: str = None,
                  err: str = None):
    """
    Generic JSON response generator for given params
    """
    return {
            "message": msg,
            "error": err,
            "data": data,
            }, code
