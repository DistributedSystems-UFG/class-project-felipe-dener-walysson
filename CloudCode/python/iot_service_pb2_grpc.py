# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import iot_service_pb2 as iot__service__pb2


class IoTServiceStub(object):
    """The temperature service definition.
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.SayTemperature = channel.unary_unary(
                '/iot_service.IoTService/SayTemperature',
                request_serializer=iot__service__pb2.TemperatureRequest.SerializeToString,
                response_deserializer=iot__service__pb2.TemperatureReply.FromString,
                )
        self.BlinkLed = channel.unary_unary(
                '/iot_service.IoTService/BlinkLed',
                request_serializer=iot__service__pb2.LedRequest.SerializeToString,
                response_deserializer=iot__service__pb2.LedReply.FromString,
                )
        self.SayLightLevel = channel.unary_unary(
                '/iot_service.IoTService/SayLightLevel',
                request_serializer=iot__service__pb2.LightLevelRequest.SerializeToString,
                response_deserializer=iot__service__pb2.LightLevelReply.FromString,
                )
        self.Login = channel.unary_unary(
                '/iot_service.IoTService/Login',
                request_serializer=iot__service__pb2.UserRequest.SerializeToString,
                response_deserializer=iot__service__pb2.UserResponse.FromString,
                )


class IoTServiceServicer(object):
    """The temperature service definition.
    """

    def SayTemperature(self, request, context):
        """Responds with a temperature measurement
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def BlinkLed(self, request, context):
        """Send a command to the led
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SayLightLevel(self, request, context):
        """Responds with the current reading of a given light sensor
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Login(self, request, context):
        """login
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_IoTServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'SayTemperature': grpc.unary_unary_rpc_method_handler(
                    servicer.SayTemperature,
                    request_deserializer=iot__service__pb2.TemperatureRequest.FromString,
                    response_serializer=iot__service__pb2.TemperatureReply.SerializeToString,
            ),
            'BlinkLed': grpc.unary_unary_rpc_method_handler(
                    servicer.BlinkLed,
                    request_deserializer=iot__service__pb2.LedRequest.FromString,
                    response_serializer=iot__service__pb2.LedReply.SerializeToString,
            ),
            'SayLightLevel': grpc.unary_unary_rpc_method_handler(
                    servicer.SayLightLevel,
                    request_deserializer=iot__service__pb2.LightLevelRequest.FromString,
                    response_serializer=iot__service__pb2.LightLevelReply.SerializeToString,
            ),
            'Login': grpc.unary_unary_rpc_method_handler(
                    servicer.Login,
                    request_deserializer=iot__service__pb2.UserRequest.FromString,
                    response_serializer=iot__service__pb2.UserResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'iot_service.IoTService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class IoTService(object):
    """The temperature service definition.
    """

    @staticmethod
    def SayTemperature(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/iot_service.IoTService/SayTemperature',
            iot__service__pb2.TemperatureRequest.SerializeToString,
            iot__service__pb2.TemperatureReply.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def BlinkLed(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/iot_service.IoTService/BlinkLed',
            iot__service__pb2.LedRequest.SerializeToString,
            iot__service__pb2.LedReply.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def SayLightLevel(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/iot_service.IoTService/SayLightLevel',
            iot__service__pb2.LightLevelRequest.SerializeToString,
            iot__service__pb2.LightLevelReply.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Login(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/iot_service.IoTService/Login',
            iot__service__pb2.UserRequest.SerializeToString,
            iot__service__pb2.UserResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
