# 🎯 AutoRewardsPC

Automatize tarefas repetitivas no Windows de forma simples, rápida e sem complicação.

O **AutoRewardsPC** é uma aplicação desktop desenvolvida em **Python**, distribuída como um **executável (.exe)** para Windows.  
O usuário final **não precisa instalar Python**, bibliotecas ou configurar nada — é só baixar e executar.

---

## 🚀 Download (Windows)

👉 **Baixe a versão mais recente do programa aqui:**

🔗 <https://github.com/leprechaunsgreen/AutoRewardsPC/releases/latest>

📦 Após o download:

1. Extraia o arquivo `.zip`
2. Execute o `AutoRewardsPC.exe`

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

**Observação:**  
O nome da variável de ambiente deve ser exatamente **`TESSERACT_PATH`** (maiúsculo), conforme utilizado pelo programa.

---

## 🖥️ Requisitos

- Windows 10 ou superior (64 bits)
- Não é necessário Python instalado
- Não é necessário Git ou GitHub para usar o programa

---

## ✨ Funcionalidades

- Interface simples e intuitiva
- Captura automatizada de ações na tela
- Execução por mouse ou teclado
- Captura sem mover o mouse (pressionando **Enter**)
- Aplicação portátil (não requer instalação)
- Executável leve
- Build automático via GitHub Actions

---

## 📦 Como usar

1. Abra o `AutoRewardsPC.exe`
2. Siga as instruções exibidas na interface
3. Para capturar **sem clicar com o mouse**:
   - Posicione o cursor sobre o alvo
   - Pressione **Enter**
4. Repita o processo para cada item desejado

---

## 🔄 Build automático do executável

Este projeto utiliza **GitHub Actions** para gerar automaticamente o executável do Windows.

Sempre que ocorre:

- um `push` no repositório
- ou a criação de uma nova tag (ex: `v1.0.0`)

## 🏷️ Como criar uma nova tag (release)

As **tags** são usadas para versionar o projeto e gerar novas versões do executável automaticamente.

### 1️⃣ Atualize o repositório local

Antes de criar a tag, certifique-se de que o código está atualizado:

```bash
git pull origin main

```

## 2️⃣ Comando para verificar quais Tags existem na sua maquina

```bash
git tag

```

## 3️⃣ Crie a tag localmente

```bash
git tag v1.0.1

```

## 4️⃣ Crie a tag localmente

```bash
git tag v1.0.1

```

## 2️⃣ Envie a tag para o GitHub

```bash
git push origin v1.0.1

```

Após esse comando:

1. O GitHub receberá a nova tag
2. O GitHub Actions será executado automaticamente
3. O executável (.exe) será gerado

5️⃣ Acesse a Release no GitHub

1. Vá até o repositório no GitHub
2. Clique em Releases
3. A nova versão estará disponível para download

ℹ️ Observações importantes

- Se a tag já existir, o Git exibirá o erro:

```bash
fatal: tag 'v1.0.1' already exists

```

Nesse caso, crie uma nova versão (ex: v1.0.2).

- As tags não devem ser alteradas após publicadas.

O GitHub:

- executa o workflow de build
- gera o `.exe`
- publica o artefato para download

---

## 🛠️ Tecnologias utilizadas

- **Python 3**
- **PyInstaller**
- **GitHub Actions (CI/CD)**
- Ambiente virtual (`venv`)
- Runner Windows (`windows-latest`)

---

## 🧑‍💻 Para desenvolvedores

### Clonar o projeto

```bash
git clone https://github.com/leprechaunsgreen/AutoRewardsPC.git
cd AutoRewardsPC
```

### Criar ambiente virtual

```bash
python -m venv .venv
.venv\Scripts\activate
```

### Instalar dependências

```bash
pip install -r requirements.txt
```

### Gerar o executável localmente

```bash
pyinstaller --onefile main.py
```

---

## 📁 Estrutura do projeto (resumida)

```bash
AutoRewardsPC/
├─ .github/
│  └─ workflows/
│     └─ build-exe.yml
├─ src/
│  └─ main.py
├─ requirements.txt
├─ README.md
└─ AutoRewardsPC.exe
```

---

## 🧾 Versionamento

Este projeto segue versionamento semântico:

- `v1.0.0` – versão inicial estável
- `v1.0.x` – correções
- `v1.x.0` – novas funcionalidades

---

## ⚠️ Aviso sobre antivírus

Por ser um executável gerado automaticamente, alguns antivírus podem acusar **falso positivo**.

✔️ O código é **100% open source**  
✔️ O build é feito diretamente no GitHub Actions  
✔️ Qualquer pessoa pode auditar o código

---

## 📜 Licença

Distribuído sob a licença **MIT**.

---

Desenvolvido com ❤️ em Python
