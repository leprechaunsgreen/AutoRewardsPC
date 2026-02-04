# 🎯 AutoRewardsPC

Automatize tarefas repetitivas no Windows de forma simples, rápida e sem complicação.

O **AutoRewardsPC** é uma aplicação desktop desenvolvida em **Python**, distribuída como um **executável (.exe)** para Windows.  
O usuário final **não precisa instalar Python**, bibliotecas ou configurar nada — é só baixar e executar.

---

## 🚀 Download (Windows)

👉 **Baixe a versão mais recente do programa aqui:**

🔗 https://github.com/leprechaunsgreen/AutoRewardsPC/releases/latest

### 📦 Após o download

1. Extraia o arquivo `.zip` em uma pasta de sua preferência  
   (exemplo: `C:\AutoRewardsPC`)
2. Entre na pasta extraída
3. Crie **um atalho** do arquivo `AutoRewardsPC.exe` na área de trabalho
4. Clique no atalho para executar o sistema

---

## 🔍 Dependência externa – Tesseract OCR

Este programa utiliza o **Tesseract OCR** (Optical Character Recognition) para realizar a **leitura e reconhecimento de textos exibidos na tela**.

O Tesseract é responsável por converter imagens e capturas de tela em texto digital, permitindo que o sistema:

- identifique palavras, números e padrões visuais
- reconheça textos que não podem ser lidos diretamente pelo sistema
- automatize ações com base no conteúdo exibido na tela

Sem o Tesseract OCR, o programa **não consegue interpretar textos presentes em imagens ou capturas**, o que inviabiliza parte fundamental do funcionamento do sistema.

---

### 📌 Por que o Tesseract não vem embutido no executável?

O Tesseract OCR é uma ferramenta externa e independente do Python.  
Por boas práticas de distribuição e licenciamento, ele **não é incorporado diretamente** ao executável (`.exe`) do programa.

Isso traz vantagens como:

- executável mais leve
- menor chance de bloqueio por antivírus
- facilidade de atualização do OCR
- maior estabilidade e compatibilidade

---

### 📥 Instalação do Tesseract OCR (obrigatória)

1. Acesse o instalador oficial:  
   https://github.com/UB-Mannheim/tesseract/wiki

2. Baixe e instale normalmente no Windows

3. Durante a instalação, mantenha o caminho padrão:
   ```
   C:\Program Files\Tesseract-OCR\tesseract.exe
   ```

4. Caso utilize outro caminho, configure a variável de ambiente:
   ```
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
