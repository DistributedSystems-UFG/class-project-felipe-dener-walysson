package com.example.iot;

import androidx.appcompat.app.AppCompatActivity;

import android.annotation.SuppressLint;
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
    private ToggleButton RedLed;
    private ToggleButton GreenLed;
    private ToggleButton PresentationButton;
    private TextView LedState;

    @SuppressLint("MissingInflatedId")
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        getSupportActionBar().setDisplayHomeAsUpEnabled(true);

        RedLed = findViewById(R.id.RedLedToggle);
        GreenLed = findViewById(R.id.GreenLedToggle);
        temperatura = findViewById(R.id.EditTextTemperatura);
        PresentationButton = findViewById(R.id.PresentationBtn);
        LedState = findViewById(R.id.LedStateText);


        ServerConnection SC = new ServerConnection();

        RedLed.setOnCheckedChangeListener(new CompoundButton.OnCheckedChangeListener() {
            @Override
            public void onCheckedChanged(CompoundButton compoundButton, boolean isON) {
                if(isON){
                    /*
                    Set Red LED to on
                    */
                    LedState.setText("Red Led is on");
                }
                else{
                    /*
                    Set Red LED to off
                    */
                    LedState.setText("Red Led is off");
                }
            }
        });

        GreenLed.setOnCheckedChangeListener(new CompoundButton.OnCheckedChangeListener() {
            @Override
            public void onCheckedChanged(CompoundButton compoundButton, boolean isON) {
                if(isON){
                    /*
                    Set Green LED to on
                    */
                    LedState.setText("Green Led is on");
                }
                else{
                    /*
                    Set Green LED to off
                    */
                    LedState.setText("Green Led is off");
                }
            }
        });

        PresentationButton.setOnCheckedChangeListener(new CompoundButton.OnCheckedChangeListener() {
            @Override
            public void onCheckedChanged(CompoundButton compoundButton, boolean isON) {
                if(isON){
                    /*
                    Start Presentation
                    */
                    LedState.setText("Start Presentation");
                }
                else{
                    /*
                    Close Presentation
                    */
                    LedState.setText("Close Presentation");
                }
            }
        });

        Thread thread = new Thread() {
            @Override
            public void run() {

                /*
                Loop get Temperatura
                */

                String[] temperaturas = {"26.5", "27.0", "27.5", "28.0",};
                Random random = new Random();
                while (true) {

                    int num = random.nextInt(temperaturas.length);
                    temperatura.setText(temperaturas[num]);
                    try {
                        TimeUnit.SECONDS.sleep(1);
                    } catch (InterruptedException e) {
                        e.printStackTrace();
                    }
                }
            }
        };

        thread.start();

    }
}