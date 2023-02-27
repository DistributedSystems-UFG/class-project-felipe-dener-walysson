package com.example.iot;

import androidx.appcompat.app.AppCompatActivity;

import android.content.Intent;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.TextView;

public class Login extends AppCompatActivity {

    private Button LoginButton;
    private TextView Cadastro;
    private TextView Config;

    private TextView TextUsuario;
    private TextView TextSenha;
    private TextView ErrorMessage;


    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_login);

        ServerConnection SC = new ServerConnection();

        LoginButton = findViewById(R.id.LoginBtn);

        LoginButton.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {

                TextUsuario = findViewById(R.id.editTextUsuario);
                String Usuario = TextUsuario.getText().toString();

                TextSenha = findViewById(R.id.editTextSenha);
                String Senha = TextSenha.getText().toString();

                ErrorMessage = findViewById(R.id.ErrorMessage);

                /*
                Conectando ao Server
                */

                if(!SC.getIPAdress().equals("123")){
                    ErrorMessage.setText("Falha na Conexão com o Servidor");
                    return;
                }


                /*
                Buscando Usuario no banco de dados
                */

                if (Usuario.equals("abc") && Senha.equals("abc")){
                    Intent intent = new Intent(Login.this, MainActivity.class);
                    startActivity(intent);
                }
                else{
                    ErrorMessage.setText("Usuario ou Senha Incorretos");
                    return;
                }

            }
        });

        Cadastro = findViewById(R.id.Cadastro);

        Cadastro.setOnClickListener(new View.OnClickListener() {

            @Override
            public void onClick(View view) {
                Intent intent = new Intent(Login.this, CadastrarUsuario.class);
                startActivity(intent);
            }
        });

        Config = findViewById(R.id.Config);

        Config.setOnClickListener(new View.OnClickListener() {

            @Override
            public void onClick(View view) {
                Intent intent = new Intent(Login.this, Config.class);
                startActivity(intent);
            }
        });


    }




}