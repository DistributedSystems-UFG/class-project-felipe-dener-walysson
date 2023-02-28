package com.example.iot;

import androidx.appcompat.app.AppCompatActivity;

import android.annotation.SuppressLint;
import android.content.Context;
import android.content.SharedPreferences;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.CompoundButton;
import android.widget.TextView;
import android.widget.ToggleButton;

import java.util.Random;
import java.util.concurrent.TimeUnit;

public class MainActivity extends AppCompatActivity {

    private TextView temperatura;
    private ToggleButton RedLedSwtich;
    private ToggleButton GreenLedSwtich;
    private ToggleButton PresentationButton;
    private Button HomeBtn;
    private Button LightBtn;
    private Button TempBtn;
    private TextView LedState;


    @SuppressLint("MissingInflatedId")
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        getSupportActionBar().setDisplayHomeAsUpEnabled(true);

        RedLedSwtich = findViewById(R.id.RedLedToggle);
        GreenLedSwtich = findViewById(R.id.GreenLedToggle);
        temperatura = findViewById(R.id.EditTextTemperatura);



        PresentationButton = findViewById(R.id.PresentationBtn);
        HomeBtn = findViewById(R.id.HomeBtn);
        LightBtn = findViewById(R.id.LightSensorBtn);
        TempBtn = findViewById(R.id.TempSensorBtn);

        LedState = findViewById(R.id.LedStateText);

        ServerConnection SC = new ServerConnection();

        SharedPreferences sharedPreferences = getSharedPreferences("MyPrefs", Context.MODE_PRIVATE);
        String token = sharedPreferences.getString("token", "");

        /*
        Upper part of the screen(IoT)
        */

        RedLedSwtich.setOnCheckedChangeListener(new CompoundButton.OnCheckedChangeListener() {
            @Override
            public void onCheckedChanged(CompoundButton compoundButton, boolean isON) {
                if(!isON){
                    SC.blinkLed("red", 0, token);
                    LedState.setText("Red Led is off");
                }
                else{
                    SC.blinkLed("red", 1, token);
                    LedState.setText("Red Led is on");
                }
            }
        });

        GreenLedSwtich.setOnCheckedChangeListener(new CompoundButton.OnCheckedChangeListener() {
            @Override
            public void onCheckedChanged(CompoundButton compoundButton, boolean isON) {
                if(!isON){
                    SC.blinkLed("green", 0, token);
                    LedState.setText("Green Led is off");
                }
                else{
                    SC.blinkLed("green", 1, token);
                    LedState.setText("Green Led is on");
                }
            }
        });


        Thread thread = new Thread() {
            @Override
            public void run() {
                while (true) {

                    String Temp = SC.getTemperature(token);
                    temperatura.setText(Temp);

/////////////////////////////////////////////////////////////////////////////////


/////////////////////////////////////////////////////////////////////////////////////

                    try {
                        TimeUnit.SECONDS.sleep(1);
                    } catch (InterruptedException e) {
                        e.printStackTrace();
                    }
                }
            }
        };

        thread.start();


        /*
        Lower part of the screen(Controles Web)
        */

        HomeBtn.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                SC.executeAction("go_to_home", token);
            }
        });

        LightBtn.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                SC.executeAction("go_to_lightsensor", token);
            }
        });

        TempBtn.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                SC.executeAction("go_to_temperature", token);
            }
        });

        PresentationButton.setOnCheckedChangeListener(new CompoundButton.OnCheckedChangeListener() {
            @Override
            public void onCheckedChanged(CompoundButton compoundButton, boolean isON) {
                if(isON){
                    SC.executeAction("full_screen", token);
                    LedState.setText("Start Presentation");
                }
                else{
                    SC.executeAction("exit_full_screen", token);
                    LedState.setText("Close Presentation");
                }
            }
        });

    }
}
