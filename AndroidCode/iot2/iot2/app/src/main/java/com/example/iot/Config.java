package com.example.iot;

import androidx.appcompat.app.AppCompatActivity;

import android.content.Intent;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.TextView;

public class Config extends AppCompatActivity {

    private Button SalvarButton;
    private TextView TextIP;
    private TextView ErrorMessage;



    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_config);
        getSupportActionBar().setDisplayHomeAsUpEnabled(true);

        ErrorMessage = findViewById(R.id.ErrorMessage2);

        SalvarButton = findViewById(R.id.SalvarBtn);

        SalvarButton.setOnClickListener(new View.OnClickListener() {

            @Override
            public void onClick(View view) {

                TextIP = findViewById(R.id.editTextIP);
                String IP = TextIP.getText().toString();

                /*
                Estabelece Conexão com o servidor
                */
                Boolean Connection = false;

                if(IP.equals("123")) {
                    Connection = true;
                }

                if(Connection){
                    ErrorMessage.setText("Conexão Realizada com Sucesso");
                }
                else{
                    ErrorMessage.setText("Falha na Conexão com o Servidor");
                    return;
                }

            }
        });

    }
}