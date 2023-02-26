package com.example.iot;

import androidx.appcompat.app.AppCompatActivity;

import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.TextView;

public class CadastrarUsuario extends AppCompatActivity {

    private Button CadastroButton;
    private TextView TextUsuario;
    private TextView TextSenha;
    private TextView ErrorMessage;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_cadastrar_usuario);
        getSupportActionBar().setDisplayHomeAsUpEnabled(true);

        CadastroButton = findViewById(R.id.CadastroBtn);

        CadastroButton.setOnClickListener(new View.OnClickListener() {

            @Override
            public void onClick(View view) {

                TextUsuario = findViewById(R.id.editTextUsuario);
                String Usuario = TextUsuario.getText().toString();

                TextSenha = findViewById(R.id.editTextSenha);
                String Senha = TextSenha.getText().toString();

                ErrorMessage = findViewById(R.id.ErrorMessage);

                /*
                Buscando Usuario no banco de dados
                */
                Boolean UserExist = false;

                if( Usuario.equals("abc")){
                    UserExist = true;
                }

                if (UserExist){
                    ErrorMessage.setText("Nome de Usuario já existente");
                    return;
                }
                else{
                    ErrorMessage.setText("Usuario cadastrado com sucesso");
                }
            }
        });

    }
}