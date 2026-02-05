import json
import sys
import time
from pathlib import Path
from typing import Dict, List, Tuple

import customtkinter as ctk
import pyautogui as ptg
from PIL import Image, ImageTk

from core.settings import CALIB_PATH, REGION_KEY, REQUIRED_CLICK_KEYS, RESOLUCOES


def get_backups_dir() -> Path:
    if hasattr(sys, "_MEIPASS"):
        p = Path(sys.executable).parent / "backups"
    else:
        p = Path(__file__).parent / "backups"
    p.mkdir(parents=True, exist_ok=True)
    return p


backups_dir = get_backups_dir()

MSG_INTRO = (
    "Siga as instruções abaixo e pressione Enter para capturar cada item.\n\n"
    "💡 Dica: para evitar mover o mouse ao clicar, apenas posicione o cursor \n"
    "sobre o local desejado e pressione Enter."
)

MSG_REGION_BLOCK_START = "📐 CAPTURA DA REGIÃO\n────────────────────"

MSG_REGION_BLOCK_END = "────────────────────"

MSG_DONE = "Todas as posições capturadas. Clique em 'Salvar calibração'."

LABELS = {
    # Exemplo (ajuste conforme seu projeto)
    "botao_microsoft_rewards": "botão do Microsoft Rewards",
    "detalhamentos_pontos": "Detalhamento dos pontos",
    "abrir_pc_search": "PC Search",
    "barra_pesquisa": "Barra de Pesquisa do https://www.bing.com",
    "aba_pesquisa": "Aba da Pagina de Pesquisa do https://www.bing.com",
    "aba_principal": "Aba da Pagina do https://rewards.bing.com",
}

# ======================================================
# UTILITÁRIOS
# ======================================================


def resource_path(relative_path: str) -> Path:
    """Resolve caminhos corretamente no PyInstaller e no modo desenvolvimento."""
    if hasattr(sys, "_MEIPASS"):
        return Path(sys._MEIPASS) / relative_path
    return Path(__file__).parent / relative_path


# ======================================================
# JANELA DE CALIBRAÇÃO
# ======================================================


class Calibrator(ctk.CTkToplevel):
    def __init__(self, master, resolution_name: str):
        super().__init__(master)

        self.title("Calibragem de Coordenadas")
        self.resolution_name = resolution_name

        self.posicoes: Dict[str, Tuple] = {}
        self.region_points: List[Tuple[int, int]] = []

        self._capture_order = REQUIRED_CLICK_KEYS + [REGION_KEY]
        self._current_index = 0

        self._setup_icon()
        self._setup_ui()
        self._setup_keyboard_listener()

        self._show_next_instruction()

    # --------------------------------------------------

    def _setup_icon(self):
        icon_ico = resource_path("app/assets/icon.ico")
        icon_png = resource_path("app/assets/icon.png")

        try:
            if icon_ico.exists():
                self.iconbitmap(str(icon_ico))
        except Exception as e:
            print("Erro iconbitmap:", e)

        try:
            if icon_png.exists():
                img = Image.open(icon_png)
                self._icon_photo = ImageTk.PhotoImage(img)
                self.iconphoto(True, self._icon_photo)
        except Exception as e:
            print("Erro iconphoto:", e)

    # --------------------------------------------------

    def _setup_ui(self):
        self.label = ctk.CTkLabel(self, text=MSG_INTRO, justify="left")
        self.label.pack(pady=8)

        self.listbox = ctk.CTkTextbox(self, width=550, height=220)
        self.listbox.pack(pady=8)
        self.listbox.configure(state="disabled")

        self.btn_frame = ctk.CTkFrame(self)
        self.btn_frame.pack(pady=6)

        self.btn_capture = ctk.CTkButton(
            self.btn_frame, text="Capturar próximo", command=self.capture_next
        )
        self.btn_capture.grid(row=0, column=0, padx=6)

        self.btn_save = ctk.CTkButton(
            self.btn_frame,
            text="Salvar calibração",
            command=self.save,
            state="disabled",
        )
        self.btn_save.grid(row=0, column=1, padx=6)

        self.btn_cancel = ctk.CTkButton(
            self.btn_frame, text="Cancelar", command=self.destroy
        )
        self.btn_cancel.grid(row=0, column=2, padx=6)

    # --------------------------------------------------

    def _setup_keyboard_listener(self):
        try:
            from pynput import keyboard

            def on_press(key):
                if key == keyboard.Key.enter:
                    self.after(0, self.capture_next)

            self._keyboard_listener = keyboard.Listener(on_press=on_press)
            self._keyboard_listener.daemon = True
            self._keyboard_listener.start()
            self._hotkey_available = True
        except Exception:
            self._keyboard_listener = None
            self._hotkey_available = False
            self._append_log("⚠️ Captura via Enter global indisponível.")

    # --------------------------------------------------

    def _append_log(self, text: str):
        self.listbox.configure(state="normal")
        self.listbox.insert("end", text + "\n")
        self.listbox.see("end")
        self.listbox.configure(state="disabled")

    # --------------------------------------------------

    def _show_next_instruction(self):
        if self._current_index >= len(self._capture_order):
            self._append_log(MSG_DONE)
            self.btn_capture.configure(state="disabled")
            self.btn_save.configure(state="normal")
            return

        key = self._capture_order[self._current_index]

        if key == REGION_KEY:
            if len(self.region_points) == 0:
                self._append_log(MSG_REGION_BLOCK_START)
                self._append_log("1️⃣Canto superior esquerdo:")
                self._append_log("🔍 Posicione o mouse e pressione Enter.")
            elif len(self.region_points) == 1:
                self._append_log("2️⃣Canto inferior direito:")
                self._append_log("🔍 Posicione o mouse e pressione Enter.")
        else:
            label = LABELS.get(key, key)
            self._append_log(f"🔍 Posicione o mouse sobre: {label} e pressione Enter.")

    # --------------------------------------------------

    def capture_next(self):
        if self._current_index >= len(self._capture_order):
            return

        pos = ptg.position()
        key = self._capture_order[self._current_index]

        if key == REGION_KEY:
            if len(self.region_points) >= 2:
                return

            # registra ponto
            self.region_points.append((pos.x, pos.y))
            self._append_log(f"Ponto capturado: ({pos.x}, {pos.y})")

            # separador visual após o primeiro ponto
            if len(self.region_points) == 1:
                self._append_log("")

            # segundo ponto → fecha a região
            if len(self.region_points) == 2:
                (x1, y1), (x2, y2) = self.region_points
                left, top = min(x1, x2), min(y1, y2)
                w, h = abs(x2 - x1), abs(y2 - y1)

                self.posicoes[REGION_KEY] = (left, top, w, h)

                # fecha o bloco visual da região
                self._append_log(MSG_REGION_BLOCK_END)

                self.region_points.clear()
                self._current_index += 1

        else:
            # captura normal (botões, alvos etc.)
            self.posicoes[key] = (pos.x, pos.y)
            self._append_log(f"Ponto capturado: ({pos.x}, {pos.y})")
            self._current_index += 1

        self._show_next_instruction()

    # --------------------------------------------------

    def save(self):
        missing = [k for k in self._capture_order if k not in self.posicoes]
        if missing:
            self._append_log(f"❌ Itens não capturados: {missing}")
            return

        try:
            w, h = map(int, self.resolution_name.lower().strip().split("x"))
        except Exception:
            w, h = ptg.size()
            self.resolution_name = f"{w}x{h}"

        calib = {}
        for k, v in self.posicoes.items():
            if k == REGION_KEY:
                left, top, ww, hh = v
                calib[k] = [left / w, top / h, ww / w, hh / h]
            else:
                x, y = v
                calib[k] = [x / w, y / h]

        CALIB_PATH.parent.mkdir(parents=True, exist_ok=True)

        data = {}
        if CALIB_PATH.exists():
            try:
                data = json.loads(CALIB_PATH.read_text(encoding="utf-8"))
            except Exception as e:
                self._append_log(f"⚠ Erro lendo calibração antiga: {e}")

        data[self.resolution_name] = calib
        CALIB_PATH.write_text(
            json.dumps(data, indent=2, ensure_ascii=False), encoding="utf-8"
        )

        self._append_log(f"✅ Calibração salva em: {CALIB_PATH}")
        self.btn_save.configure(state="disabled")

    # --------------------------------------------------

    def destroy(self):
        try:
            if self._keyboard_listener:
                self._keyboard_listener.stop()
        finally:
            super().destroy()


def generate_all_from_resolucoes(path: str | None = None):
    """Gera calibração percentual para todas as resoluções definidas em RESOLUCOES.

    Retorna o caminho do arquivo salvo.
    """
    backups_dir.mkdir(parents=True, exist_ok=True)
    p = (
        Path(path)
        if path
        else backups_dir / f"calibration_backup_{int(time.time())}.json"
    )
    data = {}
    for res_name, base in RESOLUCOES.items():
        try:
            w, h = map(int, res_name.split("x"))
        except Exception:
            w, h = ptg.size()

        calib = {}
        for k, v in base.items():
            if k == REGION_KEY:
                left, top, ww, hh = v
                calib[k] = [left / w, top / h, ww / w, hh / h]
            else:
                x, y = v
                calib[k] = [x / w, y / h]

        data[res_name] = calib

    p.write_text(json.dumps(data, indent=2), encoding="utf-8")
    return p


def remove_calibration(resolution_name: str, path: str | None = None) -> Path | None:
    """Remove calibração para `resolution_name` do arquivo de calibração.

    Antes de remover, cria um backup com `export_calibrations()` e retorna o Path do backup.
    Retorna None se nada foi removido ou em caso de erro.
    """
    p = Path(path) if path else CALIB_PATH
    if not p.exists():
        return None
    try:
        data = json.loads(p.read_text(encoding="utf-8"))
    except Exception:
        return None

    if resolution_name in data:
        # cria backup completo antes de alterar
        try:
            backup = export_calibrations()
        except Exception:
            backup = None

        del data[resolution_name]
        try:
            p.write_text(json.dumps(data, indent=2), encoding="utf-8")
        except Exception:
            return None

        return backup
    return None


def restore_backup(backup_path: str) -> bool:
    """Restaura o arquivo principal de calibração a partir de `backup_path`.

    Retorna True se sucesso.
    """
    bp = Path(backup_path)
    if not bp.exists():
        return False
    try:
        content = bp.read_text(encoding="utf-8")
        # valida JSON
        json.loads(content)
        CALIB_PATH.write_text(content, encoding="utf-8")
    except Exception:
        return False
    return True


def export_calibrations(dest_path: str | None = None) -> Path:
    """Exporta o conteúdo de `calibration.json` para `dest_path` (ou gera um backup).

    Retorna o Path do arquivo salvo.
    """
    backups_dir.mkdir(parents=True, exist_ok=True)
    p = (
        Path(dest_path)
        if dest_path
        else backups_dir / f"calibration_backup_{int(time.time())}.json"
    )
    data = {}
    if CALIB_PATH.exists():
        try:
            data = json.loads(CALIB_PATH.read_text(encoding="utf-8"))
        except Exception:
            data = {}
    p.write_text(json.dumps(data, indent=2), encoding="utf-8")
    return p


def import_calibrations(file_path: str) -> bool:
    try:
        new_data = json.loads(Path(file_path).read_text(encoding="utf-8"))

        if CALIB_PATH.exists():
            current = json.loads(CALIB_PATH.read_text(encoding="utf-8"))
        else:
            current = {}

        # sobrescreve / adiciona
        current.update(new_data)

        CALIB_PATH.write_text(
            json.dumps(current, indent=2, ensure_ascii=False), encoding="utf-8"
        )
        return True

    except Exception as e:
        print("Erro import_calibrations:", e)
        return False


def load_calibration_for_resolution(resolution: str) -> dict | None:
    if not CALIB_PATH.exists():
        return None

    try:
        data = json.loads(CALIB_PATH.read_text(encoding="utf-8"))
        return data.get(resolution)
    except Exception:
        return None


# ======================================================
# DEBUG LOCAL
# ======================================================

if __name__ == "__main__":
    root = ctk.CTk()
    Calibrator(root, "1280x1024")
    root.mainloop()
