"""Simple Textual-based TUI for iomx."""
from textual.app import App, ComposeResult
from textual.widgets import Header, Footer, Static
from textual.containers import Vertical


class IOMXTUI(App):
	CSS_PATH = None
	BINDINGS = [("q", "quit", "Quit")]

	def compose(self) -> ComposeResult:
		yield Header(show_clock=True)
		with Vertical():
			yield Static("Welcome to iomx TUI", id="welcome")
			yield Static("Press q to quit.", id="hint")
		yield Footer()

	def on_mount(self) -> None:
		self.query_one("#welcome", Static).styles.align = ("center", "middle")


def run_tui():
	IOMXTUI().run()
