package com.example.iot;


import java.util.concurrent.TimeUnit;

import io.grpc.ManagedChannel;
import io.grpc.ManagedChannelBuilder;
import io.grpc.StatusRuntimeException;
import io.grpc.examples.iotservice.ActionRequest;
import io.grpc.examples.iotservice.IoTServiceGrpc;
import io.grpc.examples.iotservice.LedRequest;
import io.grpc.examples.iotservice.LightLevelReply;
import io.grpc.examples.iotservice.LightLevelRequest;
import io.grpc.examples.iotservice.TemperatureReply;
import io.grpc.examples.iotservice.TemperatureRequest;
import io.grpc.examples.iotservice.UserCreateRequest;
import io.grpc.examples.iotservice.UserRequest;
import io.grpc.examples.iotservice.UserResponse;

public class ServerConnection {

    public static String IPAdress = "34.123.130.49";
    public static final String Port = "50051";

    private final ManagedChannel channel;
    private final IoTServiceGrpc.IoTServiceBlockingStub blockingStub;

    public ServerConnection() {
        channel = ManagedChannelBuilder.forAddress(this.IPAdress, 50051)
                .usePlaintext()
                .build();
        blockingStub = IoTServiceGrpc.newBlockingStub(channel);
    }

    public void setIP_Adress(String IPAdress){
        this.IPAdress = IPAdress;
    }

    public String getIPAdress(){
        return IPAdress;
    }

    public String login(String username, String password) {
        UserRequest request = UserRequest.newBuilder()
                .setName(username)
                .setPassword(password)
                .build();
        UserResponse response;
        try {
            System.out.println("Sending request" + request);
            response = blockingStub.login(request);
            String token = response.getToken();
            return token;
        } catch (StatusRuntimeException e) {
            System.out.println("RPC failed: " + e.getStatus());
        }
        return null;
    }

    public String getTemperature(String token) {
        TemperatureRequest request = TemperatureRequest.newBuilder()
                .setSensorName("sensor1")
                .setToken(token)
                .build();

        TemperatureReply response = blockingStub.sayTemperature(request);
        System.out.println("Temperature: " + response.getTemperature());

        return response.getTemperature();
    }

    public String sayLightLevel(String token) {
        LightLevelRequest request = LightLevelRequest.newBuilder()
                .setSensorName("sensor1")
                .setToken(token)
                .build();

        LightLevelReply response;
        try {
            response = blockingStub.sayLightLevel(request);
        } catch (StatusRuntimeException e) {
            System.err.println("RPC failed: " + e.getStatus());
            return null;
        }
        return response.getLightLevel();
    }

    public void blinkLed(String ledName, int state, String token) {
        LedRequest request = LedRequest.newBuilder()
                .setState(state)
                .setLedname(ledName)
                .setToken(token)
                .build();

        try {
            blockingStub.blinkLed(request);
        } catch (StatusRuntimeException e) {
            System.err.println("RPC failed: " + e.getStatus());
        }
    }

    public void executeAction(String action, String token) {
        String actionName = "full_screen, exit_full_screen, go_to_lightsensor, go_to_home, go_to_temperature";
        ActionRequest request = ActionRequest.newBuilder()
                .setAction(action)
                .setToken(token)
                .build();
        try {
            blockingStub.action(request);
        } catch (StatusRuntimeException e) {
            System.err.println("RPC failed: " + e.getStatus());
        }
        }
    public void registerUser(String username, String password) {
        UserCreateRequest request = UserCreateRequest.newBuilder()
                .setName(username)
                .setPassword(password)
                .build();
        try {
            blockingStub.createUser(request);
        } catch (StatusRuntimeException e) {
            System.err.println("RPC failed: " + e.getStatus());
            channel.shutdown();
        }
    }

        public void shutdown() throws InterruptedException {
        channel.shutdown().awaitTermination(5, TimeUnit.SECONDS);
    }


////////////////////////////////////////////////////////////////////////

    // getRedLedStatus
    public int getRedLedStatus(){
        LedStatusRequest request = LedStatusRequest.newBuilder()
                .setToken("my_token")
                .build();

        LedStatusResponse response = mStub.lightStatus(request);

        int redStatus = response.getStatusRed();
        return redStatus;
    }

    // getGreenLedStatus
    public int getGreenLedStatus(){
        LedStatusRequest request = LedStatusRequest.newBuilder()
                .setToken("my_token")
                .build();

        LedStatusResponse response = mStub.lightStatus(request);

        int greenStatus = response.getStatusRed();
        return greenStatus;
    }

////////////////////////////////////////////////////////////////////////////

}
