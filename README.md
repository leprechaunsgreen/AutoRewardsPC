# 🎯 AutoRewardsPC

Automatize tarefas repetitivas no Windows de forma simples, rápida e sem complicação.

O **AutoRewardsPC** é uma aplicação desktop desenvolvida em **Python**, distribuída como um **executável (.exe)** para Windows.  
O usuário final **não precisa instalar Python**, bibliotecas ou configurar nada — é só baixar e executar.

---

## 🚀 Download (Windows)

👉 **Baixe a versão mais recente do programa aqui:**

🔗 <https://github.com/leprechaunsgreen/AutoRewardsPC/releases/latest>

📦 Após o download:

1. Extraia o arquivo `.zip` em uma pasta de sua preferência  
   (exemplo: `C:\AutoRewardsPC`)
2. Entre na pasta extraída
3. Crie **um atalho** do arquivo `AutoRewardsPC.exe` na área de trabalho
4. Clique no atalho para executar o sistema

---

## 🔍 Dependência externa – Tesseract OCR

Este programa utiliza o **Tesseract OCR** para reconhecimento de texto.

### É necessário instalar o Tesseract

1. Baixe o instalador oficial:
   <https://github.com/UB-Mannheim/tesseract/wiki>

2. Instale normalmente no Windows

3. O instalador padrão já configura o caminho automaticamente:
   C:\Program Files\Tesseract-OCR\tesseract.exe

4. Caso utilize outro caminho, crie a variável de ambiente:
   TESSERACT_PATH=C:\caminho\para\tesseract.exe
   ```

**Observação:**  
O nome da variável de ambiente deve ser exatamente **`TESSERACT_PATH`**.

---

### 🧪 Como o programa localiza o Tesseract

1. Variável de ambiente `TESSERACT_PATH`
2. Caminho padrão de instalação do Windows
3. Caso não encontre, o programa exibirá um erro orientando a instalação

---

## 🖥️ Requisitos

- Windows 10 ou superior (64 bits)
- Não é necessário Python instalado
- Não é necessário Git ou GitHub

---

## ✨ Funcionalidades

- Interface simples e intuitiva
- Captura automatizada de ações na tela
- Execução por mouse ou teclado
- Captura sem mover o mouse (Enter)
- Aplicação portátil
- Build automático via GitHub Actions

---

## 🏷️ Como criar uma nova tag (release)

```bash
git pull origin main
git tag v1.0.1
git push origin v1.0.1
```

---

## 🛠️ Tecnologias utilizadas

- Python 3
- PyInstaller
- Tesseract OCR
- pytesseract
- GitHub Actions (CI/CD)
- Windows Desktop

---

## 📜 Licença

Distribuído sob a licença **MIT**.

---

Desenvolvido com ❤️ em Python
