package com.example.iot;

import androidx.appcompat.app.AppCompatActivity;

import android.annotation.SuppressLint;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.TextView;

import java.util.Random;
import java.util.concurrent.TimeUnit;

public class MainActivity extends AppCompatActivity {

    private TextView temperatura;
    private TextView estado_led;
    private Button led_controller;

    @SuppressLint("MissingInflatedId")
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        led_controller = findViewById(R.id.Interruptor);
        estado_led = findViewById(R.id.Estado_led);
        temperatura = findViewById(R.id.Temp_atual);

        led_controller.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                if (estado_led.getText().equals("Ligado")) {
                    estado_led.setText("Desligado");
                } else {
                    estado_led.setText("Ligado");
                }
            }
        });

        String[] temperaturas = {"26.5", "27.0", "27.5", "28.0",};
        Random random = new Random();
        int cont = 0;
        while (true) {

            int num = random.nextInt(temperaturas.length);
            temperatura.setText(temperaturas[num]);
            try {
                TimeUnit.SECONDS.sleep(1);
            } catch (InterruptedException e) {
                e.printStackTrace();
            }
            if (cont > 5){
                break;
            }
            cont ++;
        }
    }
}