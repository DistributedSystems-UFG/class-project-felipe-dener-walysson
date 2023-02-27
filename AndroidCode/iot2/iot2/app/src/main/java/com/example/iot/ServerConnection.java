package com.example.iot;


public class ServerConnection {

    public static String IPAdress = "000";
    public static final String Port = "50051";

    public ServerConnection(){

    }

    public void setIP_Adress(String IPAdress){
        this.IPAdress = IPAdress;
    }

    public String getIPAdress(){
        return IPAdress;
    }

}