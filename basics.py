from dataclasses import dataclass
from datetime import datetime

@dataclass
class Frame:
    top: str = "-"
    left: str = "|"
    bottom: str = "-"
    right: str = "|"
    top_left: str = "+"
    top_right: str = "+"
    bottom_left: str = "+"
    bottom_right: str = "+"

fancy_frame = Frame("─", "│", "─", "│", "╭", "╮", "╰", "╯")
invisible_frame = Frame(" ", " ", " ", " ", " ", " ", " ", " ")

def frame_text(text: str, frame: Frame) -> str:
    space = " " * 2
    new_line = '\n'
    text_len = len(text) + 4
    top_bottom_len = frame.top * text_len

    return f"{frame.top_left}{top_bottom_len}{frame.top_right}{new_line}{frame.left}{space}{text}{space}{frame.right}{new_line}{frame.bottom_left}{top_bottom_len}{frame.bottom_right}"

text = f"It is {datetime.now():%H:%I:%S}."
text = frame_text(text, invisible_frame)
text = frame_text(text, fancy_frame)

print(text)

# print(frame_text(f"It is {datetime.now():%H:%I:%S}.", fancy_frame))