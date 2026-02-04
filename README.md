# 🎯 AutoRewardsPC

Automatize tarefas repetitivas no Windows de forma simples, rápida e sem complicação.

O **AutoRewardsPC** é uma aplicação desktop desenvolvida em **Python**, distribuída como um **executável (.exe)** para Windows.  
O usuário final **não precisa instalar Python**, bibliotecas ou configurar nada — é só baixar e executar.

---

## 🚀 Download (Windows)

👉 **Baixe a versão mais recente do programa aqui:**

🔗 https://github.com/leprechaunsgreen/AutoRewardsPC/releases/latest

📦 Após o download:
1. Extraia o arquivo `.zip`
2. Execute o `AutoRewardsPC.exe`

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

```
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
