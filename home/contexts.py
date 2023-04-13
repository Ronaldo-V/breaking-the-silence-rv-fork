from connections.models import ConnectionRequest

def connect_context(request):
    if request.user.is_authenticated:
        connection_requests = ConnectionRequest.objects.filter(
            receiver=request.user,
            accepted=False,
            dismissed=False
            )
    else:
        connection_requests = []
    
    context = {
        'connection_requests': connection_requests,
    }

    return context