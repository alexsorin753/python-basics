#Calculator
import sys

print(sys.argv)


#Text framing

# from dataclasses import dataclass
# from datetime import datetime
# from email.mime import text

# @dataclass
# class Frame:
#     top: str = "-"
#     left: str = "|"
#     bottom: str = "-"
#     right: str = "|"
#     top_left: str = "+"
#     top_right: str = "+"
#     bottom_left: str = "+"
#     bottom_right: str = "+"

# fancy_frame = Frame("─", "│", "─", "│", "╭", "╮", "╰", "╯")
# invisible_frame = Frame(" ", " ", " ", " ", " ", " ", " ", " ")
# piramid_frame = Frame('-', '|', '-', '|', '+', '+', '+', '+')

# def frame_text(text: str, frame: Frame) -> str:
#     new_line = '\n'
#     strings = ""
    
    
#     def find_length():
#         spl = text.splitlines()
#         biggest_line = 0
#         if len(spl) > 1:
#             for line in spl:
#                 if len(line) > biggest_line:
#                     biggest_line = len(line)
#             return frame.top * biggest_line
#         else: 
#             return frame.top * len(text)
                
#     top_bottom_len = find_length()

#     height_len = text.count("\n")

#     if height_len > 0:
#         text = text.replace("\n", f"{frame.right}{new_line}{frame.left}")

#     strings = f"{frame.top_left}{top_bottom_len}{frame.top_right}{new_line}{frame.left}{text}{frame.right}{new_line}{frame.bottom_left}{top_bottom_len}{frame.bottom_right}"

#     split_strings = strings.splitlines()

#     same_length = True
#     str_length = 0
#     for indx, length in enumerate(split_strings):
#         if indx > 0:
#             if str_length != len(length):
#                 same_length = False
#                 break
#         str_length = len(length)

#     if same_length == False:
#         for indx, string in enumerate(split_strings):
            
#             empty_space = " "
#             count_empty = string.count(" ")
#             last_char = string[-1]
#             new_string = string[:-1]

#             if indx > 0:
#                 strings += f"{new_string}{empty_space * count_empty}{last_char}{new_line}"
#             else:
#                 strings = strings.splitlines()[0] + new_line


#     return strings

# text = f"It is {datetime.now():%H:%I:%S}."
# text = frame_text(text, invisible_frame)
# text = frame_text(text, fancy_frame)

# print(text)

# print(frame_text(f"It is {datetime.now():%H:%I:%S}.", fancy_frame))
# print(frame_text('      *\n     ***\n    *****\n   *******\n    *****\n   *******\n  *********\n ***********\n*************\n     |||\n     |||', piramid_frame))
