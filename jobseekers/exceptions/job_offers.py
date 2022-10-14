from utils.exceptions.handler import boolean_field_error_handler


def handler (response):
    if 'is_accepted' in response.data:
        data = response.data['is_accepted'][0]
        return boolean_field_error_handler(
            response,
            field_name='Accept',
            data=data
        )
    
    return response
