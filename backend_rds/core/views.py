from django.http import JsonResponse
from django.db import connections
import logging

logger = logging.getLogger(__name__)

def test_connection(request):
    try:
        with connections['postgre'].cursor() as cursor:
            cursor.execute("SELECT 1")
            row = cursor.fetchone()
            if row and row[0] == 1:
                return JsonResponse({'message': 'Connection to Backend RDS is successful!'})
            else:
                logger.error("Database query returned unexpected result")
                return JsonResponse({'error': 'Database query failed'}, status=500)
    except Exception as e:
        logger.error(f"Database connection failed: {str(e)}")
        return JsonResponse({
            'error': 'Database connection failed',
            'details': str(e)
        }, status=500)
    
