from os import replace

text_pro = '«Компьютеры становятся все умнее. Ученые утверждают, что скоро они смогут разговаривать с нами. (Говоря «они», я имею в виду компьютеры; я сомневаюсь, что ученые когда-либо смогут разговаривать с нами.)»'

def multiple_replace(target_str, replace_values):
    for i, j in replace_values.items():
        target_str = target_str.replace(i, j)
    return target_str


replace_values={'«':'', '.':'', ',':'', '(':'', '»':'', ';':'', '-':' ', ')':''}

text_new = multiple_replace(text_pro, replace_values)

print(text_new)

text_str=text_new.split(' ')

print(text_str)

def finish_text(text):
    text_new=multiple_replace(text, replace_values)
    text_str=text_new.split(' ')
    text_list=list(text_str)
    return text_list

text_list=finish_text(text_pro)
print(text_list)
print(type(text_list))