from django.http import JsonResponse
import grpc
import iot_service_pb2
import iot_service_pb2_grpc
from django.shortcuts import render 
from django.shortcuts import redirect

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        # Open a gRPC channel to the remote service
        with grpc.insecure_channel('34.86.129.130:50051') as channel:
            # Create a gRPC stub for the IoTService service
            stub = iot_service_pb2_grpc.IoTServiceStub(channel)

            # Call the Login method
            response = stub.Login(iot_service_pb2.UserRequest(name=username, password=password))

            if response.status:
                # Save the token to the session so it can be used in future requests
                request.session['token'] = response.token
                return redirect('home') # Replace 'home' with the name of your desired redirect URL
            else:
                # Return an error message to the user
                return render(request, 'login.html', {'error': 'Invalid username or password'})
    elif request.method == 'GET':
        return render(request, 'usermanagement/login.html')
    
def register_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        # Open a gRPC channel to the remote service
        with grpc.insecure_channel('34.86.129.130:50051') as channel:
            # Create a gRPC stub for the IoTService service
            stub = iot_service_pb2_grpc.IoTServiceStub(channel)

            # Call the CreateUser method
            response = stub.CreateUser(iot_service_pb2.UserCreateRequest(name=username, password=password))

            if response.status:
                # Registration successful, redirect to login page
                return redirect('login') # Replace 'login' with the name of your desired redirect URL
            else:
                # Return an error message to the user
                return render(request, 'register.html', {'error': 'Failed to create user'})
    elif request.method == 'GET':
        return render(request, 'usermanagement/register.html')


def home(request):
    return render(request, 'usermanagement/home.html')

def temperature_view(request):
    return render(request, 'usermanagement/temperatureView.html')

def light_sensor_view(request):
    return render(request, 'usermanagement/lightsensorView.html')


def temperature(request):
    token = request.headers['Authorization']
    channel = grpc.insecure_channel('34.86.129.130:50051')
    stub = iot_service_pb2_grpc.IoTServiceStub(channel)
    response = stub.SayTemperature(iot_service_pb2.TemperatureRequest(sensorName='my_sensor', token=token))
    return JsonResponse({'temperature': response.temperature})

def light_sensor(request):
    token = request.headers['Authorization']
    channel = grpc.insecure_channel('34.86.129.130:50051')
    stub = iot_service_pb2_grpc.IoTServiceStub(channel)
    response = stub.SayLightLevel(iot_service_pb2.LightLevelRequest(sensorName='my_sensor', token=token))
    return JsonResponse({'light_sensor': response.lightLevel})

def action(request):
    token = request.headers['Authorization']
    channel = grpc.insecure_channel('34.86.129.130:50051')
    stub = iot_service_pb2_grpc.IoTServiceStub(channel)
    response = stub.Action(iot_service_pb2.ActionRequest(action='there_is_action?', token=token))
    print("action",response)
    return JsonResponse({'action': response.status})

def led(request):
    token = request.headers['Authorization']
    state = int(request.GET['state'])
    ledname = request.GET['ledname']
    channel = grpc.insecure_channel('34.86.129.130:50051')
    stub = iot_service_pb2_grpc.IoTServiceStub(channel)
    response = stub.BlinkLed(iot_service_pb2.LedRequest(state=state, ledname=ledname, token=token))
    return JsonResponse({'status': str(response.ledstate)})

def led_status(request):
    token = request.headers['Authorization']
    channel = grpc.insecure_channel('34.86.129.130:50051')
    stub = iot_service_pb2_grpc.IoTServiceStub(channel)
    response = stub.LightStatus(iot_service_pb2.LedStatusRequest(token=token))
    return JsonResponse({'green': response.status_green, 'red': response.status_red})