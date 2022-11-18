from typing import Tuple


def form_response(msg: str, code: int, data: str = None,
                  err: str = None) -> Tuple:
    """
    Generic JSON response generator for given params
    """
    return {
            "message": msg,
            "error": err,
            "data": data,
            }, code
