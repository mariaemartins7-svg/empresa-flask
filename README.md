# Sistema de gestão

## Executar no VS Code

1. Abra esta pasta no VS Code.
2. Abra o terminal integrado em **Terminal > Novo Terminal**.
3. Inicie o servidor Flask:

   ```powershell
   .\venv\Scripts\python.exe app.py
   ```

4. Acesse `http://127.0.0.1:5000` no navegador.

O MySQL deve estar ativo e conter o banco `empresa_flask` com as tabelas
`usuario`, `empresa` e `funcionario`. A configuração da conexão fica em
`banco.py`.
