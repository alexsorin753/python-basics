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
    new_line = '\n'
    
    def find_length():
        spl = text.splitlines()
        biggest_line = 0
        if len(spl) > 1:
            for line in spl:
                if len(line) > biggest_line:
                    biggest_line = len(line)
            return frame.top * biggest_line
        else: 
            return frame.top * len(text)
                
    top_bottom_len = find_length()


    strings = f"{frame.top_left}{top_bottom_len}{frame.top_right}{new_line}{frame.left}{text}{frame.right}{new_line}{frame.bottom_left}{top_bottom_len}{frame.bottom_right}"
    
    height_len = strings.count("\n")

    print(height_len)
    print(len(text.splitlines()))


    return strings

text = f"It is {datetime.now():%H:%I:%S}."
text = frame_text(text, invisible_frame)
text = frame_text(text, fancy_frame)

print(text)

# print(frame_text(f"It is {datetime.now():%H:%I:%S}.", fancy_frame))